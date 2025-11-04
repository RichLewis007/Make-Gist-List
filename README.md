# Make Gist List <img src="assets/icons/file-text.svg" alt="Documentation" width="25" height="25" style="vertical-align: middle;">
Updated: 2025-11-03

<div align=center>
  <img src="assets/make-gist-list-readme-header3.png" alt="Make-Gist-List-README-heading" width="894" height="300" style="vertical-align: middle;">


  [![Update Gist List](https://github.com/RichLewis007/Make-Gist-List/actions/workflows/update-gist-list-agent.yml/badge.svg)](https://github.com/RichLewis007/Make-Gist-List/actions/workflows/update-gist-list-agent.yml)
  [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com) <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
  [![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
  <!-- ALL-CONTRIBUTORS-BADGE:END -->

</div>

> **Automatically generate and maintain a markdown list of all your public GitHub gists**

A simple, lightweight Python script that fetches your public GitHub gists and creates an easy to read markdown table. Perfect for maintaining an up-to-date index of your code snippets, utilities, and examples.

## <img src="assets/icons/sparkle.svg" alt="Features" width="25" height="25" style="vertical-align: middle;"> Features

- <img src="assets/icons/arrows-clockwise.svg" alt="Updates" width="21" height="21" style="vertical-align: middle;"> **Automatic Updates**: Runs daily via GitHub Actions
- <img src="assets/icons/chart-bar.svg" alt="Data" width="21" height="21" style="vertical-align: middle;"> **Rich Information**: Title, file count, file names, language, public status, created date, update date, engagement metrics, and links, with full descriptions shown below each gist
- <img src="assets/icons/lightning.svg" alt="Performance" width="21" height="21" style="vertical-align: middle;"> **Optimized Performance**: Uses batched GraphQL queries for 26-40% fewer API calls
- <img src="assets/icons/bug.svg" alt="Debugging" width="21" height="21" style="vertical-align: middle;"> **Professional Logging**: Structured logging with configurable verbosity levels
- <img src="assets/icons/target.svg" alt="Integration" width="21" height="21" style="vertical-align: middle;"> **Gist Integration**: Updates a target gist with the generated list
- <img src="assets/icons/rocket.svg" alt="Setup" width="21" height="21" style="vertical-align: middle;"> **Easy Setup**: Fork, configure secrets, and you're done!
- <img src="assets/icons/palette.svg" alt="Customization" width="21" height="21" style="vertical-align: middle;"> **Customizable**: Easy to modify output format and add new fields
- <img src="assets/icons/lock.svg" alt="Security" width="21" height="21" style="vertical-align: middle;"> **Secure**: Uses minimal GitHub token permissions (gist scope only)

## <img src="assets/icons/graduation-cap.svg" alt="Learning" width="25" height="25" style="vertical-align: middle;"> Learning Resources

This project demonstrates several important programming concepts and optimization techniques:

- **[Optimization Techniques Guide](docs/OPTIMIZATION-TECHNIQUES.md)** - Learn about API optimization, GraphQL vs REST, batching strategies, and performance considerations
- **Code Examples** - See real-world implementations of error handling, type hints, and clean architecture
- **Best Practices** - Understand how to write maintainable, efficient code when working with external APIs

Perfect for developers looking to understand how to optimize API usage and write production-ready code!

## <img src="assets/icons/rocket.svg" alt="Quick Start" width="25" height="25" style="vertical-align: middle;"> Quick Start

### Option 1: Fork & Use (Recommended)

1. **Fork this repository** <img src="assets/icons/arrow-up.svg" alt="Fork" width="25" height="25" style="vertical-align: middle;">
2. **Create a gist** to hold your list (copy its ID from the URL)
3. **Set up GitHub secrets** in your forked repo:
   - `LIST_GIST_ID`: The gist ID you created
   - `GIST_TOKEN`: A GitHub token with "gist" scope
   - *Note: `GITHUB_USERNAME` is automatically set to the repository owner*
4. **That's it!** <img src="assets/icons/party-popper.svg" alt="Success" width="25" height="25" style="vertical-align: middle;"> The workflow runs daily at 13:00 UTC

### Option 2: Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/Make-Gist-List.git
cd Make-Gist-List

# 2. Create environment file from example
cp env.example .env

# 3. Edit .env file with your values
# GITHUB_USERNAME=your-username  # Required for local runs
# LIST_GIST_ID=your-gist-id      
# GIST_TOKEN=your-github-token   
# VERBOSE=1                      # Optional: enable debug logging
# TIMEZONE=America/New_York      # Optional: timezone for timestamps
# DATE_FORMAT=DD-MM-YYYY         # Optional: date format
# TIME_FORMAT=12                 # Optional: 12-hour time format
# USE_HTML_TABLE=true            # generate markdown or html format table

# 4. Install dependencies
uv sync

# 5. Run the script
uv run python make-gist-list.py

# Windows users: Use PowerShell or Command Prompt
# PowerShell: uv run python make-gist-list.py
# CMD: uv run python make-gist-list.py
```

> <img src="assets/icons/lightbulb.svg" alt="Tip" width="16" height="16" style="vertical-align: middle;"> **Tip**: The script automatically loads your `.env` file. For detailed local setup instructions, see the [Setup Guide](SETUP.md#local-command-line-usage).

### <img src="assets/icons/wrench.svg" alt="Configure" width="20" height="20" style="vertical-align: middle;"> Alternate Configuration Method

If you prefer not to use a `.env` file, you can configure the script using export variables:

**Export Variables**
```bash
# Linux/macOS
export GITHUB_USERNAME="your-username"
export TIMEZONE="America/New_York"
export DATE_FORMAT="MM-DD-YYYY"
export TIME_FORMAT="12"
export USE_HTML_TABLE="true"
uv run python make-gist-list.py

# Windows PowerShell
$env:GITHUB_USERNAME="your-username"
$env:TIMEZONE="America/New_York"
$env:DATE_FORMAT="MM-DD-YYYY"
$env:TIME_FORMAT="12"
$env:USE_HTML_TABLE="true"
uv run python make-gist-list.py
```

## <img src="assets/icons/clipboard-text.svg" alt="Output" width="25" height="25" style="vertical-align: middle;"> What You Get

The script generates a markdown table like this:

# Public Gists from your-username

**Last updated:** 2025-01-15 13:00 UTC

**Total public gists:** 42

<table>
<tr>
<th>Title</th><th>Files</th><th>File Names</th><th>Lang</th><th>Public</th><th>Created</th><th>Updated</th><th>Link</th><th>Comments</th><th>Forks</th><th>Stars</th>
</tr>
<tr><td>My awesome script</td><td>3</td><td>script.py, config.json, README.md</td><td>Python</td><td>✓</td><td>2024-01-10 09:15 EST</td><td>2024-01-15 12:30 EST</td><td><a href='https://gist.github.com/...'>open</a></td><td>2</td><td>1</td><td>5</td></tr>
<tr><td colspan='11'><strong>Description:</strong> A comprehensive script for data processing with configuration support and documentation</td></tr>
<tr><td>Quick utility</td><td>1</td><td>utils.js</td><td>JavaScript</td><td>✓</td><td>2024-01-14 14:00 EST</td><td>2024-01-14 15:20 EST</td><td><a href='https://gist.github.com/...'>open</a></td><td>0</td><td>0</td><td>3</td></tr>
<tr><td colspan='11'><strong>Description:</strong> Simple utility function for common tasks</td></tr>
</table>

List created by [Make Gist List](https://github.com/your-username/Make-Gist-List).

## <img src="assets/icons/wrench.svg" alt="Configuration" width="25" height="25" style="vertical-align: middle;"> Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GITHUB_USERNAME` | <img src="assets/icons/check.svg" alt="Required" width="16" height="16" style="vertical-align: middle;"> | Your GitHub username |
| `LIST_GIST_ID` | <img src="assets/icons/check.svg" alt="Required" width="16" height="16" style="vertical-align: middle;"> | ID of the gist to update |
| `GIST_TOKEN` | <img src="assets/icons/check.svg" alt="Required" width="16" height="16" style="vertical-align: middle;"> | GitHub token with "gist" scope |
| `TARGET_MD_FILENAME` | <img src="assets/icons/x.svg" alt="Optional" width="16" height="16" style="vertical-align: middle;"> | Filename for the markdown in the gist (defaults to "Public-Gists.md") |
| `TIMEZONE` | <img src="assets/icons/x.svg" alt="Optional" width="16" height="16" style="vertical-align: middle;"> | Timezone for timestamp display (e.g., "UTC", "America/New_York", "Europe/London") |
| `DATE_FORMAT` | <img src="assets/icons/x.svg" alt="Optional" width="16" height="16" style="vertical-align: middle;"> | Date format ("YYYY-MM-DD", "DD-MM-YYYY", "MM-DD-YYYY") |
| `TIME_FORMAT` | <img src="assets/icons/x.svg" alt="Optional" width="16" height="16" style="vertical-align: middle;"> | Time format ("12" for 12-hour, "24" for 24-hour) |
| `USE_HTML_TABLE` | <img src="assets/icons/x.svg" alt="Optional" width="16" height="16" style="vertical-align: middle;"> | Output format ("true" for HTML tables, "false" for markdown tables) |

### Output Formats

The script supports two output formats:

**HTML Tables (`USE_HTML_TABLE=true`)** - Recommended for GitHub gists:
- Renders as actual tables in GitHub gists
- Supports full-width description rows using `colspan`
- Better for viewing in GitHub gist interface
- <img src="assets/icons/test-tube.svg" alt="Tests" width="16" height="16" style="vertical-align: middle;"> **Note**: GitHub repository READMEs strip `colspan` attributes, so this format doesn't work there

**Markdown Tables (`USE_HTML_TABLE=false`)** - Recommended for repository README files:
- Standard markdown table syntax
- Renders properly in GitHub repositories, README files, etc.
- More portable across different markdown viewers
- Description appears in its own column (second position)

### GitHub Token Setup

1. Go to [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a name like "Gist List Updater"
4. Select the "gist" scope (this is the minimum required permission)
5. Copy the token and add it as `GIST_TOKEN` in your repository secrets

## <img src="assets/icons/palette.svg" alt="Customization" width="25" height="25" style="vertical-align: middle;"> Customization

The script is designed to be easily customizable:

- **Change the markdown format**: Modify the `build_markdown()` function
- **Add more fields**: Extend the table structure in the markdown output
- **Change the schedule**: Update the cron in `.github/workflows/update-gist-list-agent.yml`
- **Add filtering**: Modify the `list_public_gists()` function to filter gists differently
- **Custom styling**: Modify the table headers, formatting, and layout

## <img src="assets/icons/books.svg" alt="Documentation" width="25" height="25" style="vertical-align: middle;"> Documentation

- **[Setup Guide](SETUP.md)** - Detailed step-by-step setup instructions
- **[Environment Example](env.example)** - Example environment variable configuration
- **[Contributing Guidelines](CONTRIBUTING.md)** - How to contribute to this project

> <img src="assets/icons/student.svg" alt="Data" width="25" height="25" style="vertical-align: middle;"> **Are you interested in how this open source program was crafted?**
> 
> Do you want to learn how the open source developers made this program efficient, how the code was organized and errors
> were logged and handled? Check out the included educational guide which goes into technical depth, discussing the 
> API optimization strategies used to pull data from potentially many gists from the back-end GitHub systems, the performance
> considerations and demonstrations of best practices in Python coding.
> 
> **Read [Optimization Techniques & Programming Concepts](docs/OPTIMIZATION-TECHNIQUES.md)**

## <img src="assets/icons/wrench.svg" alt="Requirements" width="25" height="25" style="vertical-align: middle;"> Requirements

- **Python**: 3.10 or higher
- **Dependencies**: `requests` library
- **GitHub**: Account with public gists
- **Optional**: GitHub token with gist scope (for automatic updates)

## <img src="assets/icons/handshake.svg" alt="Contributing" width="25" height="25" style="vertical-align: middle;"> Contributing

Contributions are welcome! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Contribution Ideas

- Add support for filtering gists by language or date
- Create alternative output formats (JSON, CSV, etc.)
- Add support for private gists (with proper authentication)

## <img src="assets/icons/file-text.svg" alt="License" width="25" height="25" style="vertical-align: middle;"> License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## <img src="assets/icons/hands-praying.svg" alt="Acknowledgments" width="25" height="25" style="vertical-align: middle;"> Acknowledgments

- Built with the GitHub API
- Uses GitHub Actions for automation
- Inspired by the need for better gist organization

---

**⭐ If this project helps you, please give it a star!**

**<img src="assets/icons/arrow-up.svg" alt="Fork" width="25" height="25" style="vertical-align: middle;"> Fork it to easily create your own gist list updater!**

## <img src="assets/icons/users.svg" alt="Contributors" width="25" height="25" style="vertical-align: middle;"> Contributors

Thanks goes to these wonderful people ([emoji key](docs/emoji-key.md)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/RichLewis007"><img src="https://avatars.githubusercontent.com/u/1149213?v=4?s=100" width="100px;" alt="Rich Lewis"/><br /><sub><b>Rich Lewis</b></sub></a><br /><a href="https://github.com/RichLewis007/Make-Gist-List/commits?author=RichLewis007" title="Code"><img src="assets/icons/terminal.svg" alt="Code" width="16" height="16" style="vertical-align: middle;"></a> <a href="#ideas-RichLewis007" title="Ideas, Planning, & Feedback"><img src="assets/icons/book-open-user.svg" alt="Ideas" width="16" height="16" style="vertical-align: middle;"></a> <a href="#maintenance-RichLewis007" title="Maintenance"><img src="assets/icons/wrench.svg" alt="Maintenance" width="16" height="16" style="vertical-align: middle;"></a> <a href="#question-RichLewis007" title="Answering Questions"><img src="assets/icons/question.svg" alt="Questions" width="16" height="16" style="vertical-align: middle;"></a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://dima-portfolio.vercel.app"><img src="https://avatars.githubusercontent.com/u/170177550?v=4?s=100" width="100px;" alt="Joshua Dimaunahan"/><br /><sub><b>Joshua Dimaunahan</b></sub></a><br /><a href="#ideas-MindfulLearner" title="Ideas, Planning, & Feedback"><img src="assets/icons/book-open-user.svg" alt="Ideas" width="16" height="16" style="vertical-align: middle;"></a> <a href="https://github.com/RichLewis007/Make-Gist-List/commits?author=MindfulLearner" title="Code"><img src="assets/icons/terminal.svg" alt="Code" width="16" height="16" style="vertical-align: middle;"></a> <a href="https://github.com/RichLewis007/Make-Gist-List/issues?q=author%3AMindfulLearner" title="Bug reports"><img src="assets/icons/bug.svg" alt="Bug" width="16" height="16" style="vertical-align: middle;"></a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
