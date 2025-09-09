# <img src="assets/icons/rocket.svg" alt="Setup Guide" width="20" height="20" style="vertical-align: middle;"> Setup Guide

This comprehensive guide will walk you through setting up your own gist list updater. Follow these steps carefully to get everything working smoothly.

## <img src="assets/icons/clipboard-text.svg" alt="Prerequisites" width="20" height="20" style="vertical-align: middle;"> Prerequisites

Before you begin, make sure you have:
- <img src="assets/icons/check.svg" alt="Required" width="16" height="16" style="vertical-align: middle;"> A GitHub account
- <img src="assets/icons/check.svg" alt="Required" width="16" height="16" style="vertical-align: middle;"> Some public gists (or create a few test ones)
- <img src="assets/icons/check.svg" alt="Required" width="16" height="16" style="vertical-align: middle;"> Basic familiarity with GitHub (forking, setting secrets)

## <img src="assets/icons/arrows-clockwise.svg" alt="Step 1" width="20" height="20" style="vertical-align: middle;"> Step 1: Fork This Repository

1. **Navigate to this repository**: [Make-Gist-List](https://github.com/RichLewis007/Make-Gist-List)
2. **Click the "Fork" button** at the top right of the page
3. **Choose your GitHub account** as the destination
4. **Wait for the fork to complete** (this may take a few seconds)

> <img src="assets/icons/lightbulb.svg" alt="Tip" width="16" height="16" style="vertical-align: middle;"> **Tip**: After forking, you'll be redirected to your own copy of the repository.

## <img src="assets/icons/file-text.svg" alt="Step 2" width="20" height="20" style="vertical-align: middle;"> Step 2: Create a Gist

1. **Go to [gist.github.com](https://gist.github.com)**
2. **Click "New gist"** or the "+" button
3. **Add any content** (it will be overwritten by the script)
4. **Make it public** by selecting "Public" (not "Secret")
5. **Click "Create public gist"**
6. **Copy the gist ID** from the URL

> <img src="assets/icons/magnifying-glass.svg" alt="Finding" width="16" height="16" style="vertical-align: middle;"> **Finding the Gist ID**: The URL will look like `https://gist.github.com/username/abc123def456...` - the long alphanumeric string after your username is the gist ID.

## <img src="assets/icons/key.svg" alt="Step 3" width="20" height="20" style="vertical-align: middle;"> Step 3: Create a GitHub Token

1. **Go to [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)**
2. **Click "Generate new token (classic)"**
3. **Give it a descriptive name** like "Gist List Updater"
4. **Set expiration** as desired (or select "No expiration")
5. **Select the "gist" scope** (this is the minimum required permission)
6. **Click "Generate token"**
7. **Copy the token immediately** - you won't see it again!

> <img src="assets/icons/warning.svg" alt="Important" width="16" height="16" style="vertical-align: middle;"> **Important**: The token only needs "gist" scope. Don't give it more permissions than necessary for security.

## <img src="assets/icons/wrench.svg" alt="Step 4" width="20" height="20" style="vertical-align: middle;"> Step 4: Set Repository Secrets

1. **In your forked repository**, go to "Settings" → "Secrets and variables" → "Actions"
2. **Click "New repository secret"**
3. **Add these secrets one by one**:

> <img src="assets/icons/lightbulb.svg" alt="Note" width="16" height="16" style="vertical-align: middle;"> **Note**: `GITHUB_USERNAME` is automatically set to the repository owner in GitHub Actions, so you don't need to create this secret!

| Secret Name | Value | Description |
|-------------|-------|-------------|
| `LIST_GIST_ID` | The gist ID from Step 2 | The gist that will be updated with your list |
| `GIST_TOKEN` | The GitHub token from Step 3 | Token with permission to update gists |

> <img src="assets/icons/lock.svg" alt="Security" width="16" height="16" style="vertical-align: middle;"> **Security Note**: These secrets are encrypted and only visible to you and GitHub Actions.

## <img src="assets/icons/test-tube.svg" alt="Step 5" width="20" height="20" style="vertical-align: middle;"> Step 5: Test the Setup

1. **Go to the "Actions" tab** in your repository
2. **Click on "Update Gist List" workflow**
3. **Click "Run workflow"** → "Run workflow"
4. **Watch the workflow run** - it should complete successfully

> <img src="assets/icons/chart-bar.svg" alt="Monitor" width="16" height="16" style="vertical-align: middle;"> **Monitor Progress**: You can click on the running workflow to see detailed logs and progress.

## <img src="assets/icons/check.svg" alt="Step 6" width="20" height="20" style="vertical-align: middle;"> Step 6: Verify the Result

1. **Go to your gist** (using the ID from Step 2)
2. **You should see a nicely formatted markdown table** of your public gists
3. **The gist will be updated daily at 13:00 UTC** automatically

> <img src="assets/icons/target.svg" alt="Success" width="16" height="16" style="vertical-align: middle;"> **Success Indicators**: 
> - The gist contains a markdown table with your gists
> - The table shows titles, file counts, languages, and links
> - The "Last updated" timestamp is recent

## <img src="assets/icons/wrench.svg" alt="Troubleshooting" width="20" height="20" style="vertical-align: middle;"> Troubleshooting

### <img src="assets/icons/x.svg" alt="Error" width="16" height="16" style="vertical-align: middle;"> "Gist not found" error
**Possible causes:**
- Incorrect `LIST_GIST_ID` secret
- Gist doesn't exist or was deleted
- Gist is private (must be public)
- `GIST_TOKEN` lacks proper permissions

**Solutions:**
- Double-check the gist ID in the URL
- Verify the gist is public
- Ensure the token has "gist" scope
- Test the token manually by accessing the gist

### <img src="assets/icons/x.svg" alt="Error" width="16" height="16" style="vertical-align: middle;"> "User not found" error
**Possible causes:**
- Incorrect `GITHUB_USERNAME` secret
- Username doesn't exist
- Username has no public gists

**Solutions:**
- Verify the username is correct
- Check that the user has public gists
- Ensure the username is spelled correctly

### <img src="assets/icons/x.svg" alt="Error" width="16" height="16" style="vertical-align: middle;"> Workflow fails to run
**Possible causes:**
- Missing required secrets
- Incorrect workflow file
- GitHub Actions disabled

**Solutions:**
- Verify all three secrets are set
- Check the Actions tab for detailed error messages
- Ensure GitHub Actions is enabled in your repository

### <img src="assets/icons/x.svg" alt="Error" width="16" height="16" style="vertical-align: middle;"> No gists showing up
**Possible causes:**
- No public gists exist
- Gists are marked as private
- GitHub API rate limiting
- Network connectivity issues

**Solutions:**
- Create some public gists for testing
- Check gist privacy settings
- Wait and try again (rate limiting)
- Check your internet connection

## <img src="assets/icons/palette.svg" alt="Customization" width="20" height="20" style="vertical-align: middle;"> Customization Options

### Change the Update Schedule
Edit `.github/workflows/update-gist-list-agent.yml` and modify the cron line:
```yaml
cron: "0 13 * * *"  # Daily at 13:00 UTC
```

Common schedules:
- `"0 */6 * * *"` - Every 6 hours
- `"0 9,21 * * *"` - Twice daily at 9 AM and 9 PM UTC
- `"0 9 * * 1"` - Weekly on Mondays at 9 AM UTC

### Modify the Markdown Format
Edit the `build_markdown()` function in `make-gist-list.py` to:
- Change table headers
- Add new columns
- Modify date formatting
- Customize styling

### Add Gist Filtering
Modify the `list_public_gists()` function to:
- Filter by language
- Filter by date range
- Filter by description keywords
- Exclude specific gists

## <img src="assets/icons/question.svg" alt="Help" width="20" height="20" style="vertical-align: middle;"> Need Help?

### Self-Help Resources
- **Check the [main README](README.md)** for overview and features
- **Review the [Contributing Guide](CONTRIBUTING.md)** for development details
- **Examine the workflow logs** in the Actions tab for specific errors

### Getting Support
- **Open an issue** in this repository with:
  - Clear description of the problem
  - Steps to reproduce
  - Error messages (if any)
  - Your GitHub username (for context)
- **Check existing issues** to see if your problem has been solved
- **Review the troubleshooting section** above for common solutions

### Community Help
- **GitHub Discussions** (if enabled)
- **Stack Overflow** with the `github-api` and `github-actions` tags
- **GitHub Community** forums

---

## <img src="assets/icons/terminal.svg" alt="Local Command Line Usage" width="20" height="20" style="vertical-align: middle;"> Local Command Line Usage

If you prefer to run the script locally on your machine instead of using GitHub Actions, follow these steps:

> <img src="assets/icons/lightbulb.svg" alt="Tip" width="16" height="16" style="vertical-align: middle;"> **Automatic .env Loading**: The script automatically loads your `.env` file using `python-dotenv`, so you don't need to manually source environment variables.

### <img src="assets/icons/rocket.svg" alt="Quick Setup" width="20" height="20" style="vertical-align: middle;"> Quick Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/Make-Gist-List.git
cd Make-Gist-List

# 2. Create environment file from example
cp env.example .env

# 3. Edit the .env file with your values
# (See detailed instructions below)

# 4. Install dependencies
uv sync

# 5. Run the script
uv run python make-gist-list.py
```

### <img src="assets/icons/wrench.svg" alt="Environment Configuration" width="20" height="20" style="vertical-align: middle;"> Environment Configuration

1. **Copy the example file**:
   ```bash
   cp env.example .env
   ```

2. **Edit the `.env` file** with your values:
   ```bash
   # Required for local runs
   GITHUB_USERNAME=your-github-username
   
   # Required - for updating a gist
   LIST_GIST_ID=your-gist-id-here
   GIST_TOKEN=your-github-token-here
   
   # Optional - customize filename in the gist
   TARGET_MD_FILENAME=Public-Gists.md
   
   # Optional - timezone for timestamp display
   TIMEZONE=America/New_York
   
   # Optional - date format for timestamp display
   DATE_FORMAT=DD-MM-YYYY
   
   # Optional - time format for timestamp display
   TIME_FORMAT=12
   ```

3. **Get your GitHub token** (if you want to update a gist):
   - Go to [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)
   - Click "Generate new token (classic)"
   - Select the "gist" scope
   - Copy the token and add it to your `.env` file

### <img src="assets/icons/test-tube.svg" alt="Testing Locally" width="20" height="20" style="vertical-align: middle;"> Testing Locally

```bash
# Test with just username (generates markdown to stdout)
export GITHUB_USERNAME="your-username"
python make-gist-list.py

# Test with gist updating (requires GIST_TOKEN and LIST_GIST_ID)
python make-gist-list.py
```

### <img src="assets/icons/lightbulb.svg" alt="Local vs GitHub Actions" width="20" height="20" style="vertical-align: middle;"> Local vs GitHub Actions

| Feature | Local Command Line | GitHub Actions |
|---------|-------------------|----------------|
| **Setup** | Manual environment setup | Automatic with secrets |
| **Scheduling** | Manual runs | Daily automatic |
| **GITHUB_USERNAME** | Must set manually | Auto-set to repo owner |
| **Dependencies** | Install locally | Managed by workflow |
| **Best for** | Development, testing | Production, automation |

### <img src="assets/icons/wrench.svg" alt="Local Development Tips" width="20" height="20" style="vertical-align: middle;"> Local Development Tips

- **Use `.env` file**: Keeps your credentials secure and out of version control
- **Test without gist updating**: Just set `GITHUB_USERNAME` to see the output
- **Debug mode**: Add `print()` statements to see what's happening
- **Customize output**: Modify the `build_markdown()` function for different formats

### <img src="assets/icons/clock.svg" alt="Timezone Configuration" width="20" height="20" style="vertical-align: middle;"> Timezone Configuration

The "Last updated" timestamp in your gist list can be displayed in your preferred timezone:

**Common timezone examples:**
- `TIMEZONE=UTC` - Coordinated Universal Time (default)
- `TIMEZONE=America/New_York` - Eastern Time (US)
- `TIMEZONE=America/Chicago` - Central Time (US)
- `TIMEZONE=America/Denver` - Mountain Time (US)
- `TIMEZONE=America/Los_Angeles` - Pacific Time (US)
- `TIMEZONE=Europe/London` - Greenwich Mean Time
- `TIMEZONE=Europe/Paris` - Central European Time
- `TIMEZONE=Asia/Tokyo` - Japan Standard Time

**How it works:**
- The script automatically detects your timezone and displays the abbreviation (e.g., "EST", "PST", "GMT")
- If an invalid timezone is specified, it falls back to UTC
- The timezone setting applies to both local runs and GitHub Actions

### <img src="assets/icons/calendar.svg" alt="Date & Time Format Configuration" width="20" height="20" style="vertical-align: middle;"> Date & Time Format Configuration

Customize how the "Last updated" timestamp is displayed with date and time format options:

**Date Format Options:**
- `DATE_FORMAT=YYYY-MM-DD` - ISO format (2025-09-09) - **Default**
- `DATE_FORMAT=DD-MM-YYYY` - European format (09-09-2025)
- `DATE_FORMAT=MM-DD-YYYY` - US format (09-09-2025)

**Time Format Options:**
- `TIME_FORMAT=24` - 24-hour format (18:10) - **Default**
- `TIME_FORMAT=12` - 12-hour format with AM/PM (6:10 PM)

**Example Combinations:**
```bash
# European style with 12-hour time
DATE_FORMAT=DD-MM-YYYY
TIME_FORMAT=12
# Result: "09-09-2025 6:10 PM EDT"

# US style with 24-hour time
DATE_FORMAT=MM-DD-YYYY
TIME_FORMAT=24
# Result: "09-09-2025 18:10 EDT"

# ISO style with 12-hour time
DATE_FORMAT=YYYY-MM-DD
TIME_FORMAT=12
# Result: "2025-09-09 6:10 PM EDT"
```

**How it works:**
- Date formats use YYYY (year), MM (month), DD (day) placeholders
- Time format "12" includes AM/PM, "24" uses 24-hour notation
- All formats work with any timezone setting
- Invalid formats fall back to defaults (YYYY-MM-DD, 24-hour)

## <img src="assets/icons/party-popper.svg" alt="Success" width="20" height="20" style="vertical-align: middle;"> You're All Set!

Once you've completed these steps, you'll have:
- <img src="assets/icons/check.svg" alt="Success" width="16" height="16" style="vertical-align: middle;"> An automatically updating list of your public gists
- <img src="assets/icons/check.svg" alt="Success" width="16" height="16" style="vertical-align: middle;"> A beautiful markdown table updated daily
- <img src="assets/icons/check.svg" alt="Success" width="16" height="16" style="vertical-align: middle;"> A system that's easy to customize and extend
- <img src="assets/icons/check.svg" alt="Success" width="16" height="16" style="vertical-align: middle;"> A project you can share with others

**Happy gist organizing! <img src="assets/icons/rocket.svg" alt="Launch" width="20" height="20" style="vertical-align: middle;">**
