# 🚀 Setup Guide

This comprehensive guide will walk you through setting up your own gist list updater. Follow these steps carefully to get everything working smoothly.

## 📋 Prerequisites

Before you begin, make sure you have:
- ✅ A GitHub account
- ✅ Some public gists (or create a few test ones)
- ✅ Basic familiarity with GitHub (forking, setting secrets)

## 🔄 Step 1: Fork This Repository

1. **Navigate to this repository**: [Make-Gist-List](https://github.com/RichLewis007/Make-Gist-List)
2. **Click the "Fork" button** at the top right of the page
3. **Choose your GitHub account** as the destination
4. **Wait for the fork to complete** (this may take a few seconds)

> 💡 **Tip**: After forking, you'll be redirected to your own copy of the repository.

## 📝 Step 2: Create a Gist

1. **Go to [gist.github.com](https://gist.github.com)**
2. **Click "New gist"** or the "+" button
3. **Add any content** (it will be overwritten by the script)
4. **Make it public** by selecting "Public" (not "Secret")
5. **Click "Create public gist"**
6. **Copy the gist ID** from the URL

> 🔍 **Finding the Gist ID**: The URL will look like `https://gist.github.com/username/abc123def456...` - the long alphanumeric string after your username is the gist ID.

## 🔑 Step 3: Create a GitHub Token

1. **Go to [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)**
2. **Click "Generate new token (classic)"**
3. **Give it a descriptive name** like "Gist List Updater"
4. **Set expiration** as desired (or select "No expiration")
5. **Select the "gist" scope** (this is the minimum required permission)
6. **Click "Generate token"**
7. **Copy the token immediately** - you won't see it again!

> ⚠️ **Important**: The token only needs "gist" scope. Don't give it more permissions than necessary for security.

## ⚙️ Step 4: Set Repository Secrets

1. **In your forked repository**, go to "Settings" → "Secrets and variables" → "Actions"
2. **Click "New repository secret"**
3. **Add these secrets one by one**:

| Secret Name | Value | Description |
|-------------|-------|-------------|
| `GITHUB_USERNAME` | Your GitHub username | The username whose gists you want to list |
| `LIST_GIST_ID` | The gist ID from Step 2 | The gist that will be updated with your list |
| `GIST_TOKEN` | The GitHub token from Step 3 | Token with permission to update gists |

> 🔒 **Security Note**: These secrets are encrypted and only visible to you and GitHub Actions.

## 🧪 Step 5: Test the Setup

1. **Go to the "Actions" tab** in your repository
2. **Click on "Update Gist List" workflow**
3. **Click "Run workflow"** → "Run workflow"
4. **Watch the workflow run** - it should complete successfully

> 📊 **Monitor Progress**: You can click on the running workflow to see detailed logs and progress.

## ✅ Step 6: Verify the Result

1. **Go to your gist** (using the ID from Step 2)
2. **You should see a nicely formatted markdown table** of your public gists
3. **The gist will be updated daily at 13:00 UTC** automatically

> 🎯 **Success Indicators**: 
> - The gist contains a markdown table with your gists
> - The table shows titles, file counts, languages, and links
> - The "Last updated" timestamp is recent

## 🔧 Troubleshooting

### ❌ "Gist not found" error
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

### ❌ "User not found" error
**Possible causes:**
- Incorrect `GITHUB_USERNAME` secret
- Username doesn't exist
- Username has no public gists

**Solutions:**
- Verify the username is correct
- Check that the user has public gists
- Ensure the username is spelled correctly

### ❌ Workflow fails to run
**Possible causes:**
- Missing required secrets
- Incorrect workflow file
- GitHub Actions disabled

**Solutions:**
- Verify all three secrets are set
- Check the Actions tab for detailed error messages
- Ensure GitHub Actions is enabled in your repository

### ❌ No gists showing up
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

## 🎨 Customization Options

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

## 🆘 Need Help?

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

## 🎉 You're All Set!

Once you've completed these steps, you'll have:
- ✅ An automatically updating list of your public gists
- ✅ A beautiful markdown table updated daily
- ✅ A system that's easy to customize and extend
- ✅ A project you can share with others

**Happy gist organizing! 🚀**
