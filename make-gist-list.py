#!/usr/bin/env python3
# file: make-gist-list.py

"""
Make Gist List - GitHub Gist Markdown List Generator

This script automatically generates a sortable markdown table of all your public GitHub gists
and updates a target gist with the generated list. Perfect for creating a portfolio, a showcase 
of your code snippets and projects, or even a much faster way to see all of your public gists in one place.

Features:
- Fetches all public gists from a GitHub username
- Generates a clean, sortable markdown table
- Includes gist metadata (title, files, language, date, links)
- Shows engagement metrics (comments, forks, stars)
- Uses efficient batched GraphQL API for star counts
- Uses custom icons for public/private status
- Updates a target gist on GitHub automatically
- Designed to be easily forkable and customizable

Usage:
    python make-gist-list.py

Environment Variables:
    GITHUB_USERNAME (required) - GitHub username from which to fetch public gists
    LIST_GIST_ID    (required) - Target gist ID to update with the generated list
    GIST_TOKEN      (required) - GitHub Personal Access Token (classic type) with "gist" scope (required if updating a gist)
    TARGET_MD_FILENAME (optional) - Filename for the markdown file in the target gist

Output:
    - Always prints the generated markdown to stdout
    - If LIST_GIST_ID and GIST_TOKEN are provided, the workflow updates the target gist
    - Creates a clean sortable table with all public gist information

For detailed setup instructions, see README.md and SETUP.md files.

Author: Rich Lewis
Repository: https://github.com/RichLewis007/Make-Gist-List

Output fields in the generated markdown table:
  Title (first line of gist description, truncated)
  Files (count)
  File Names (actual filenames, truncated if too many)
  Lang (primary language by largest file)
  Public (always checking this)
  Created (when gist was originally created)
  Updated (when gist was last modified)
  Link (to the gist)
  Comments (count)
  Forks (count)
  Stars (count)
  
Additionally, complete gist descriptions are shown on separate rows below each gist entry
for better readability and to preserve full context.
"""

from __future__ import annotations

import base64
import logging
import os
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Any, Dict, List, Optional, Tuple

import requests
from requests import Response, Session

# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not available, continue without it
    pass

API = "https://api.github.com"
TIMEOUT = 30
RETRIES = 3

# Configure logging
def setup_logging(verbose: bool = False) -> logging.Logger:
    """
    Set up logging configuration for the application.
    
    Args:
        verbose: If True, enables DEBUG level logging
        
    Returns:
        Configured logger instance
    """
    level = logging.DEBUG if verbose else logging.INFO
    
    # Create formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Create handler for stderr
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    
    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    # Prevent duplicate handlers if called multiple times
    if len(logger.handlers) == 1:
        logger.propagate = False
    
    return logger

# Initialize logger (will be reconfigured in main() if verbose mode is enabled)
logger = setup_logging()
RETRY_BACKOFF = 2.0
USER_AGENT = "make-gist-list-script/1.0 (+https://github.com/)"

@dataclass
class Cfg:
    username: str
    list_gist_id: Optional[str]
    token: Optional[str]
    target_md: str
    timezone: str
    date_format: str
    time_format: str

def getenv_required(name: str) -> str:
    v = os.getenv(name)
    if not v:
        logger.error(f"Missing required env: {name}")
        sys.exit(1)
    return v

def load_cfg() -> Cfg:
    token = os.getenv("GIST_TOKEN")
    return Cfg(
        username=getenv_required("GITHUB_USERNAME"),
        list_gist_id=os.getenv("LIST_GIST_ID"),
        token=token,
        target_md=os.getenv("TARGET_MD_FILENAME", "Public-gists.md"),
        timezone=os.getenv("TIMEZONE", "UTC"),
        date_format=os.getenv("DATE_FORMAT", "YYYY-MM-DD"),
        time_format=os.getenv("TIME_FORMAT", "24"),
    )

def make_session(token: Optional[str]) -> Session:
    s = requests.Session()
    s.headers.update({
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": USER_AGENT,
    })
    if token:
        s.headers["Authorization"] = f"token {token}"
    return s

def _req_with_retry(s: Session, method: str, url: str, **kw: Any) -> Response:
    last: Optional[Exception] = None
    for attempt in range(1, RETRIES + 1):
        try:
            r = s.request(method, url, timeout=TIMEOUT, **kw)
            if r.status_code == 403 and "rate limit" in (r.text or "").lower():
                reset = r.headers.get("X-RateLimit-Reset")
                if reset and reset.isdigit():
                    wait = max(0, int(reset) - int(time.time())) + 1
                    logger.warning(f"Rate limited. Sleeping {wait}s…")
                    time.sleep(wait)
                    continue
            if 500 <= r.status_code < 600:
                raise requests.HTTPError(f"{r.status_code} {r.reason}", response=r)
            return r
        except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as e:
            last = e
            if attempt == RETRIES:
                break
            backoff = RETRY_BACKOFF ** (attempt - 1)
            logger.warning(f"Transient error ({e}); retry {attempt}/{RETRIES-1} in {backoff:.1f}s…")
            time.sleep(backoff)
    assert last is not None
    raise last

def list_public_gists(s: Session, username: str) -> List[Dict[str, Any]]:
    gists: List[Dict[str, Any]] = []
    page = 1
    while True:
        r = _req_with_retry(s, "GET", f"{API}/users/{username}/gists",
                            params={"per_page": 100, "page": page})
        if r.status_code == 404:
            logger.error(f"User '{username}' not found or gists unavailable.")
            sys.exit(2)
        r.raise_for_status()
        chunk = r.json()
        if not chunk:
            break
        gists.extend(chunk)
        page += 1

    # Hard filter (defensive): only keep gists explicitly marked public
    public_only = [g for g in gists if bool(g.get("public", False))]
    if len(public_only) != len(gists):
        skipped = len(gists) - len(public_only)
        logger.info(f"Skipped {skipped} non-public gist(s).")
    return public_only

def primary_language(files: Dict[str, Dict[str, Any]]) -> str:
    best: Optional[Tuple[str, int]] = None
    for f in files.values():
        lang = f.get("language")
        size = int(f.get("size", 0) or 0)
        if lang and (best is None or size > best[1]):
            best = (lang, size)
    return best[0] if best else ""

def get_gist_star_counts_batch(session: Session, gist_ids: List[str]) -> Dict[str, int | str]:
    """
    Get star counts for multiple gists using a single GraphQL API call.
    
    This uses the viewer.gists query to get all gists with star counts,
    then matches them with the provided gist IDs by cross-referencing
    with the REST API data.
    
    Args:
        session: Authenticated requests session
        gist_ids: List of gist IDs to get star counts for
        
    Returns:
        Dictionary mapping gist_id -> star_count (int) or "N/A" (str) if unavailable
    """
    if not gist_ids:
        return {}
    
    # Use viewer.gists query to get all gists with star counts
    query = """
    query {
        viewer {
            gists(first: 100) {
                nodes {
                    id
                    stargazerCount
                    url
                }
            }
        }
    }
    """
    
    payload = {"query": query}
    
    try:
        logger.debug(f"Making GraphQL request to get all gists with star counts")
        response = session.post("https://api.github.com/graphql", json=payload)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and data["data"] and data["data"]["viewer"]:
                gists_data = data["data"]["viewer"]["gists"]["nodes"]
                
                # Create mapping from gist URL to star count
                # We'll match by URL since it contains the gist ID
                url_to_stars = {}
                for gist in gists_data:
                    url = gist.get("url", "")
                    if url:
                        # Extract gist ID from URL: https://gist.github.com/username/gist_id
                        gist_id_from_url = url.split("/")[-1]
                        url_to_stars[gist_id_from_url] = gist.get("stargazerCount", 0)
                
                # Map our gist_ids to star counts
                star_counts = {}
                for gist_id in gist_ids:
                    if gist_id in url_to_stars:
                        star_counts[gist_id] = url_to_stars[gist_id]
                    else:
                        star_counts[gist_id] = "N/A"
                
                logger.debug(f"Successfully retrieved star counts for {len(star_counts)} gists")
                return star_counts
            else:
                logger.warning("GraphQL response missing data field")
        else:
            logger.warning(f"GraphQL request failed with status {response.status_code}")
    except Exception as e:
        logger.warning(f"Failed to get star counts via GraphQL: {e}")
    
    # Fallback: return "N/A" for all gists if GraphQL fails
    return {gist_id: "N/A" for gist_id in gist_ids}

def build_markdown(gists: list[dict], username: str, session: Session, timezone: str = "UTC", date_format: str = "YYYY-MM-DD", time_format: str = "24") -> str:
    """
    Build markdown table with gist information including engagement metrics.
    
    This function fetches additional data (comments, forks, stars) for each gist
    and generates a comprehensive markdown table with the following columns:
    - Title: First line of gist description (truncated to 120 chars)
    - Files: Count of files in the gist
    - File Names: Actual filenames (shows first 3, with "+N more" if more exist)
    - Lang: Primary language by largest file size
    - Public: Checkmark (✓) for public, X (✗) for private
    - Created: When the gist was originally created (in configured timezone)
    - Updated: When the gist was last modified (in configured timezone)
    - Link: Clickable link to the gist
    - Comments: Number of comments
    - Forks: Number of forks
    - Stars: Number of stars
    
    Additionally, for gists with descriptions, a separate row is added below each gist
    containing the complete description (not truncated) for better readability.
    
    Data Sources:
    - REST API: Basic gist info, comments, forks
    - GraphQL API: Star counts (batched for efficiency)
    
    Args:
        gists: List of gist dictionaries from GitHub API
        username: GitHub username for display
        session: Authenticated requests session
        timezone: Timezone for timestamp display (e.g., "UTC", "America/New_York", "Europe/London")
        date_format: Date format ("YYYY-MM-DD", "DD-MM-YYYY", "MM-DD-YYYY")
        time_format: Time format ("12" for 12-hour, "24" for 24-hour)
        
    Returns:
        Formatted markdown string with comprehensive gist information
    """
    # Generate timestamp in configured timezone with custom date/time formats
    try:
        tz = ZoneInfo(timezone)
        now_local = datetime.now(tz)
        
        # Convert date format to strftime format
        date_strftime = date_format.replace("YYYY", "%Y").replace("MM", "%m").replace("DD", "%d")
        
        # Convert time format to strftime format
        if time_format == "12":
            time_strftime = "%I:%M %p"  # 12-hour format with AM/PM
        else:  # Default to 24-hour format
            time_strftime = "%H:%M"
        
        # Format with timezone abbreviation
        tz_abbr = now_local.strftime("%Z")
        timestamp = now_local.strftime(f"{date_strftime} {time_strftime} {tz_abbr}")
        
    except Exception as e:
        logger.warning(f"Invalid timezone '{timezone}', falling back to UTC: {e}")
        now_utc = datetime.now(ZoneInfo("UTC"))
        # Use default format for fallback
        fallback_date = "YYYY-MM-DD".replace("YYYY", "%Y").replace("MM", "%m").replace("DD", "%d")
        fallback_time = "%H:%M" if time_format == "24" else "%I:%M %p"
        timestamp = now_utc.strftime(f"{fallback_date} {fallback_time} UTC")

    lines = [
        f"# All public gists from {username}",
        "",
        "**Last updated:** " + timestamp,
        "",
    ]

    # Do assignment as a standalone statement (not inside the list literal)
    count = len(gists)
    lines += [
        f"**Total public gists:** {count}",
        "",
        "| Title | Files | File Names | Lang | Public | Created | Updated | Link | Comments | Forks | Stars",
        "|---|---:|---|:---:|---|---|---|---|---|---|---|",
    ]

    # Sort gists by update date (newest first)
    gists_sorted = sorted(gists, key=lambda x: x.get("updated_at") or "", reverse=True)
    
    # Collect all gist IDs for batched star count query
    gist_ids = [g.get("id", "") for g in gists_sorted if g.get("id")]
    
    # Get star counts for all gists in a single GraphQL request
    logger.info(f"Fetching star counts for {len(gist_ids)} gists via GraphQL...")
    star_counts = get_gist_star_counts_batch(session, gist_ids)
    
    # Process each gist and build table rows
    for g in gists_sorted:
        desc = (g.get("description") or "").strip() or "(no description)"
        title = desc.splitlines()[0][:120]
        full_description = desc  # Keep the full description
        
        files = g.get("files") or {}
        file_count = len(files)
        
        # Format file names (truncated if too many)
        file_names = list(files.keys())[:3]  # Show first 3 files
        if len(files) > 3:
            file_names.append(f"+{len(files)-3} more")
        file_names_str = ", ".join(file_names)
        
        lang = primary_language(files)
        
        # Format updated date
        try:
            raw = g.get("updated_at")
            dt_utc = datetime.fromisoformat(raw.replace("Z", "+00:00"))
            
            # Convert to user's configured timezone
            tz = ZoneInfo(timezone)
            dt_local = dt_utc.astimezone(tz)
            
            # Convert date format to strftime format
            date_strftime = date_format.replace("YYYY", "%Y").replace("MM", "%m").replace("DD", "%d")
            
            # Convert time format to strftime format
            if time_format == "12":
                time_strftime = "%I:%M %p"  # 12-hour format with AM/PM
            else:  # Default to 24-hour format
                time_strftime = "%H:%M"
            
            # Format with timezone abbreviation
            tz_abbr = dt_local.strftime("%Z")
            updated = dt_local.strftime(f"{date_strftime} {time_strftime} {tz_abbr}")
            
        except Exception as e:
            logger.warning(f"Failed to format gist updated date '{g.get('updated_at')}': {e}")
            updated = g.get("updated_at") or ""
            
        # Format created date
        try:
            raw_created = g.get("created_at")
            dt_created_utc = datetime.fromisoformat(raw_created.replace("Z", "+00:00"))
            
            # Convert to user's configured timezone
            tz = ZoneInfo(timezone)
            dt_created_local = dt_created_utc.astimezone(tz)
            
            # Format with timezone abbreviation
            created = dt_created_local.strftime(f"{date_strftime} {time_strftime} {tz_abbr}")
            
        except Exception as e:
            logger.warning(f"Failed to format gist created date '{g.get('created_at')}': {e}")
            created = g.get("created_at") or ""
            
        url = g.get("html_url") or ""
        gist_id = g.get("id", "")

        # Fetch comments and forks for each gist (REST API)
        # Note: These are still individual calls as they're not available in the main gist response
        try:
            comments_response = session.get(f"{API}/gists/{gist_id}/comments")
            comments = len(comments_response.json()) if comments_response.status_code == 200 else 0
        except Exception:
            comments = "N/A"
        try:
            forks_response = session.get(f"{API}/gists/{gist_id}/forks")
            forks = len(forks_response.json()) if forks_response.status_code == 200 else 0
        except Exception:
            forks = "N/A"
        
        # Get star count from batched GraphQL query (much more efficient)
        stars = star_counts.get(gist_id, "N/A")

        public_flag = '✓' if g.get("public") else '✗'
        lines.append(f"| {title} | {file_count} | {file_names_str} | {lang or ''} | {public_flag} | {created} | {updated} | [open]({url}) | {comments} | {forks} | {stars} |")
        
        # Add full description on a separate row below
        if full_description and full_description != "(no description)":
            lines.append(f"| **Description:** {full_description} |||||||||")

    lines += [
        "",
        f"_List created by [Make Gist List](https://github.com/{username}/Make-Gist-List)._",
    ]
    return "\n".join(lines)

def update_index_gist(s: Session, gist_id: str, target_md: str, content_md: str, username: str) -> str:
    """
    Update a target gist with the generated markdown content.
    
    This function updates an existing gist with the markdown table of public gists.
    The gist is identified by its ID and the content is placed in a specific file.
    
    Args:
        s: Authenticated requests session
        gist_id: ID of the gist to update
        target_md: Filename for the markdown content in the gist
        content_md: The markdown content to write
        username: GitHub username for the gist description
        
    Returns:
        URL of the updated gist
        
    Raises:
        SystemExit: If gist not found or token lacks access
    """
    payload = {
        "description": f"Public gists from {username}",
        "files": { target_md: {"content": content_md} },
    }
    r = _req_with_retry(s, "PATCH", f"{API}/gists/{gist_id}", json=payload)
    if r.status_code == 404:
        logger.error("LIST_GIST_ID not found or token lacks access to that gist.")
        sys.exit(4)
    r.raise_for_status()
    return r.json().get("html_url", "(unknown)")

def main() -> int:
    """
    Main function that orchestrates the gist list generation process.
    
    This function:
    1. Loads configuration from environment variables
    2. Creates an authenticated session
    3. Fetches all public gists for the specified user
    4. Generates a markdown table with engagement metrics
    5. Optionally updates a target gist with the generated content
    
    API Usage:
    - 1 REST API call to list all public gists (includes created_at, updated_at, files info)
    - 1 GraphQL API call to get star counts for all gists (batched)
    - 2 REST API calls per gist for comments and forks
    - 1 REST API call to update target gist (if configured)
    
    Total API calls: 1 + 1 + (2 × number_of_gists) + 1 (if updating gist)
    
    The GitHub REST API already provides created_at, updated_at, and files information
    in the initial gist listing, so no additional API calls are needed for these fields.
    
    Returns:
        0 on success, 5 on gist update error
    """
    # Check for verbose logging
    verbose = os.getenv("VERBOSE", "").lower() in ("1", "true", "yes")
    if verbose:
        # Reconfigure logger for verbose mode
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled")
    
    cfg = load_cfg()
    logger.debug(f"Configuration loaded: username={cfg.username}, has_token={bool(cfg.token)}, has_gist_id={bool(cfg.list_gist_id)}")
    
    s = make_session(cfg.token)
    gists = list_public_gists(s, cfg.username)
    logger.debug(f"Found {len(gists)} public gists")
    
    md = build_markdown(gists, cfg.username, s, cfg.timezone, cfg.date_format, cfg.time_format)

    # Always print Markdown to stdout
    print(md)

    # Update gist if both envs are present
    if cfg.list_gist_id and cfg.token:
        try:
            url = update_index_gist(s, cfg.list_gist_id, cfg.target_md, md, cfg.username)
            logger.info(f"Updated gist: {url}")
        except requests.HTTPError as e:
            status = getattr(e, "response", None).status_code if getattr(e, "response", None) else "HTTP"
            logger.warning(f"Gist update failed ({status}): {e}")
            return 5
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        logger.error(f"Unhandled error: {e!r}")
        sys.exit(6)
