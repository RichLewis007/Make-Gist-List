# All-Contributors Icon Replacement Setup Guide

## Overview

This repository has a workflow to automatically replace emojis with themed icons in the README.md below the contributors added by the All Contributors bot. The workflow to do this is triggered by the All Contributors bot PRs (Pull Requests). Another workflow can be set up to run at a scheduled time every day, to ensure all `contributors` section icons are up to date. This workflow can also be activated manually.

## How It Works

1. **All Contributors bot** creates a PR
2. **Automated workflow** detects the bot and runs icon replacement
3. **Custom icons** are swapped with the default emojis in the README.md contributors section
4. **Changes committed** back to the same PR
5. **Comment added** to confirm automation completed

## Setup Required

### Repository Permissions

1. Go to **Settings** → **Actions** → **General**
2. Under **"Workflow permissions"**:
   - Select **"Read and write permissions"**
   - Check **"Allow GitHub Actions to create and approve pull requests"**

That's it! No tokens or secrets needed - uses the default `GITHUB_TOKEN`.

## Workflows Included

### 1. **Auto-replace Contributor Icons** (`auto-replace-contributor-icons.yml`)
- **Triggers**: When All Contributors bot creates/updates a PR
- **Action**: Automatically replaces emojis with custom icons
- **Result**: Changes committed back to the same PR

### 2. **Scheduled Icon Maintenance** (`scheduled-icon-maintenance.yml`)
- **Triggers**: Daily at 2 AM UTC (or manual)
- **Action**: Ensures all icons are up-to-date
- **Result**: Commits any needed updates

## Testing

### Test with Current PR:
Your existing All Contributors bot PR should automatically trigger the workflow.

### Test with New Contributor:
```bash
# Use the All Contributors bot
@all-contributors please add @username for ideas
```

The bot will:
1. Create a PR with emojis
2. Automation will detect it
3. Replace emojis with custom icons
4. Commit changes to the same PR
5. Add a confirmation comment

## What Happens Automatically

1. **All Contributors bot** creates PR with emojis
2. **Workflow detects** the bot automatically
3. **Icon replacement script** runs
4. **Custom icons applied** to README.md
5. **Changes committed** back to the PR
6. **Comment added** confirming completion
7. **PR ready to merge** with custom icons

## Files Structure

```
Make-Gist-List/
├── .github/workflows/
│   ├── auto-replace-contributor-icons.yml    # Main automation
│   └── scheduled-icon-maintenance.yml        # Daily maintenance
├── scripts/
│   └── replace-contribution-icons.js         # Icon replacement script
├── assets/icons/                             # Phosphor icon library svg images used to replace boring standard emojis
└── README.md                                 # Your gist list README
```

## Benefits

- ✅ **Fully Automatic**: No manual intervention needed
- ✅ **Self-contained**: Everything in one repository
- ✅ **Simple Setup**: Just enable repository permissions
- ✅ **Real-time**: Triggers immediately when bot creates PR
- ✅ **Clean**: No temporary files or external dependencies
- ✅ **Transparent**: Clear logging and status comments

## Troubleshooting

### Workflow Not Triggering:
- Check that the PR is from `allcontributors[bot]`
- Verify repository workflow permissions are enabled
- Check the Actions tab for any error messages

### Manual Override:
If automation fails, you can run the script manually:
```bash
node scripts/replace-contribution-icons.js
git add README.md
git commit -m "Update contributor icons"
git push
```

## Security

- Uses default `GITHUB_TOKEN` (no custom tokens needed)
- Only modifies `README.md` in the same repository
- All actions are logged and visible in Actions tab
- Can be disabled anytime by removing workflow files

## Maintenance

The system is completely hands-off:
- **Automatic**: Triggers on All Contributors bot PRs
- **Scheduled**: Daily maintenance to catch any missed updates
- **Self-healing**: Will fix any icon inconsistencies automatically

Your emoji to custom icon swap for all-contributors is now fully automated!
