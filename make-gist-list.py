#!/usr/bin/env python3
# file: make-gist-list.py

"""
Automatically generates a markdown table of ALL of your public GISTS 
and updates a gist with that list. Super handy! 

**Please see the README.md and SETUP.md files for more information on how to use this script.**

Behavior:
- Always prints the Markdown to stdout.
- If LIST_GIST_ID and GIST_TOKEN are set, also PATCHes that gist file.

Env variables:
  GITHUB_USERNAME (required) GitHub username to list PUBLIC gists from
  LIST_GIST_ID    (optional) The gist ID to overwrite (the list gist)
  GIST_TOKEN      (optional) Has "gist" scope, required for updating the gist.

Output fields:
  Title (first line of gist description, truncated)
  Files (count)
  Lang (primary language by largest file)
  Public (always checking this)
  Updated (UTC)
  Link (to the gist)
"""

from __future__ import annotations

import os
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Any, Dict, List, Optional, Tuple

import requests
from requests import Response, Session

API = "https://api.github.com"
TIMEOUT = 30
RETRIES = 3
RETRY_BACKOFF = 2.0
USER_AGENT = "make-gist-list-script/1.0 (+https://github.com/)"

@dataclass
class Cfg:
    username: str
    list_gist_id: Optional[str]
    token: Optional[str]
    target_md: str

def getenv_required(name: str) -> str:
    v = os.getenv(name)
    if not v:
        print(f"Missing required env: {name}", file=sys.stderr)
        sys.exit(1)
    return v

def load_cfg() -> Cfg:
    return Cfg(
        username=getenv_required("GITHUB_USERNAME"),
        list_gist_id=os.getenv("LIST_GIST_ID"),
        token=os.getenv("GIST_TOKEN"),
        target_md=os.getenv("TARGET_MD_FILENAME", "Public-Gists.md"),
    )

def make_session(token: Optional[str]) -> Session:
    s = requests.Session()
    s.headers.update({
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": USER_AGENT,
    })
    if token:
        s.headers["Authorization"] = f"Bearer {token}"
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
                    print(f"Rate limited. Sleeping {wait}s…", file=sys.stderr)
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
            print(f"Transient error ({e}); retry {attempt}/{RETRIES-1} in {backoff:.1f}s…", file=sys.stderr)
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
            print(f"User '{username}' not found or gists unavailable.", file=sys.stderr)
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
        print(f"[info] Skipped {skipped} non-public gist(s).", file=sys.stderr)
    return public_only

def primary_language(files: Dict[str, Dict[str, Any]]) -> str:
    best: Optional[Tuple[str, int]] = None
    for f in files.values():
        lang = f.get("language")
        size = int(f.get("size", 0) or 0)
        if lang and (best is None or size > best[1]):
            best = (lang, size)
    return best[0] if best else ""

def build_markdown(gists: list[dict], username: str) -> str:
    # UTC time for display
    now_utc = datetime.now(ZoneInfo("UTC"))
    timestamp = now_utc.strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        f"# Public Gists from {username}",
        "",
        "**Last updated:** " + timestamp,
        "",
    ]

    # Do assignment as a standalone statement (not inside the list literal)
    count = len(gists)
    lines += [
        f"**Total public gists:** {count}",
        "",
        "| Title | Files | Lang | Public | Updated | Link |",
        "|---|---:|---|:---:|---|---|",
    ]

    gists_sorted = sorted(gists, key=lambda x: x.get("updated_at") or "", reverse=True)
    for g in gists_sorted:
        desc = (g.get("description") or "").strip() or "(no description)"
        title = desc.splitlines()[0][:120]
        files = g.get("files") or {}
        file_count = len(files)
        lang = primary_language(files)
        try:
            raw = g.get("updated_at")
            dt_utc = datetime.fromisoformat(raw.replace("Z", "+00:00"))
            updated = dt_utc.strftime("%Y-%m-%d %H:%M UTC")
        except Exception:
            updated = g.get("updated_at") or ""
        url = g.get("html_url") or ""

        public_flag = "✅" if g.get("public") else "❌"
        lines.append(f"| {title} | {file_count} | {lang or ''} | {public_flag} | {updated} | [open]({url}) |")

    lines += [
        "",
        f"_Generated by [Make Gist List](https://github.com/{username}/Make-Gist-List)._",
    ]
    return "\n".join(lines)

def update_index_gist(s: Session, gist_id: str, target_md: str, content_md: str, username: str) -> str:
    payload = {
        "description": f"Public gists from {username}",
        "files": { target_md: {"content": content_md} },
    }
    r = _req_with_retry(s, "PATCH", f"{API}/gists/{gist_id}", json=payload)
    if r.status_code == 404:
        print("LIST_GIST_ID not found or token lacks access to that gist.", file=sys.stderr)
        sys.exit(4)
    r.raise_for_status()
    return r.json().get("html_url", "(unknown)")

def main() -> int:
    cfg = load_cfg()
    s = make_session(cfg.token)
    gists = list_public_gists(s, cfg.username)
    md = build_markdown(gists, cfg.username)

    # Always print Markdown to stdout
    print(md)

    # Optionally update gist if both envs are present
    if cfg.list_gist_id and cfg.token:
        try:
            url = update_index_gist(s, cfg.list_gist_id, cfg.target_md, md, cfg.username)
            print(f"\n[info] Updated gist: {url}", file=sys.stderr)
        except requests.HTTPError as e:
            status = getattr(e, "response", None).status_code if getattr(e, "response", None) else "HTTP"
            print(f"[warn] Gist update failed ({status}): {e}", file=sys.stderr)
            return 5
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"Unhandled error: {e!r}", file=sys.stderr)
        sys.exit(6)
