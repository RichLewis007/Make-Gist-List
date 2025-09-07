# <img src="assets/icons/handshake.svg" alt="Contributing" width="20" height="20" style="vertical-align: middle;"> Contributing to Make Gist List

Thank you for considering contributing to this project! We welcome contributions from developers of all skill levels.

## <img src="assets/icons/target.svg" alt="How to Contribute" width="20" height="20" style="vertical-align: middle;"> How to Contribute

### 1. Fork and Clone
1. **Fork this repository** to your GitHub account
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/Make-Gist-List.git
   cd Make-Gist-List
   ```

### 2. Create a Branch
Create a new branch for your changes:
```bash
git checkout -b feature/your-feature-name
# or for bug fixes:
git checkout -b fix/issue-description
```

### 3. Make Your Changes
- **Follow the coding conventions** (see below)
- **Test your changes** locally before submitting
- **Keep commits focused** and well-described

### 4. Submit a Pull Request
1. **Push your branch** to your fork
2. **Create a pull request** against the main branch
3. **Describe your changes** clearly in the PR description
4. **Link any related issues** if applicable

## <img src="assets/icons/file-text.svg" alt="Coding Conventions" width="20" height="20" style="vertical-align: middle;"> Coding Conventions

### Python Style
- **Follow PEP 8** for Python code style
- **Use type hints** where appropriate
- **Keep functions focused** and well-documented
- **Add docstrings** for new functions and classes

### Code Structure
- **Maintain the existing structure** of the project
- **Keep the script simple** and easy to understand
- **Add error handling** for new functionality
- **Use meaningful variable names**

### Testing
- **Test your changes** with different scenarios
- **Verify the output format** is correct
- **Check error handling** works as expected
- **Test with both valid and invalid inputs**

## <img src="assets/icons/rocket.svg" alt="Contribution Ideas" width="20" height="20" style="vertical-align: middle;"> Contribution Ideas

### High Priority
- **Add new gist fields** (stars, forks, comments count)
- **Improve error handling** and user feedback
- **Add support for filtering** gists by language or date
- **Enhance the markdown output** formatting

### Medium Priority
- **Add configuration options** for customization
- **Create alternative output formats** (JSON, CSV)
- **Add logging and debugging** capabilities
- **Improve GitHub API rate limiting** handling

### Low Priority
- **Add support for private gists** (with proper auth)
- **Create a web interface** for configuration
- **Add support for multiple gist lists**
- **Create browser extensions** or integrations

## <img src="assets/icons/bug.svg" alt="Bug Reports" width="20" height="20" style="vertical-align: middle;"> Bug Reports

When reporting bugs, please include:

- **Clear description** of the problem
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Environment details** (Python version, OS, etc.)
- **Error messages** or logs if applicable
- **Screenshots** if relevant

## <img src="assets/icons/lightbulb.svg" alt="Feature Requests" width="20" height="20" style="vertical-align: middle;"> Feature Requests

For new features, please describe:

- **What you want to achieve**
- **Why this feature would be useful**
- **How you envision it working**
- **Any examples** or mockups if possible

## <img src="assets/icons/wrench.svg" alt="Development Setup" width="20" height="20" style="vertical-align: middle;"> Development Setup

### Local Development
```bash
# Clone and setup
git clone https://github.com/your-username/Make-Gist-List.git
cd Make-Gist-List

# Install in development mode
pip install -e .

# Run the script
python make-gist-list.py
```

### Testing Changes
```bash
# Test with your own gists
export GITHUB_USERNAME="your-username"
export LIST_GIST_ID="your-gist-id"
export GIST_TOKEN="your-token"

python make-gist-list.py
```

## <img src="assets/icons/clipboard-text.svg" alt="Pull Request Guidelines" width="20" height="20" style="vertical-align: middle;"> Pull Request Guidelines

### Before Submitting
- [ ] **Code follows** the project's style guidelines
- [ ] **Changes are tested** and working
- [ ] **Documentation is updated** if needed
- [ ] **No sensitive information** is included
- [ ] **Commit messages are clear** and descriptive

### PR Description Template
```markdown
## Description
Brief description of what this PR accomplishes.

## Changes Made
- [ ] Change 1
- [ ] Change 2
- [ ] Change 3

## Testing
Describe how you tested these changes.

## Screenshots
If applicable, add screenshots of the changes.

## Related Issues
Closes #(issue number) if applicable.
```

## <img src="assets/icons/tag.svg" alt="Issue Labels" width="20" height="20" style="vertical-align: middle;"> Issue Labels

We use the following labels to organize issues:

- **`bug`** - Something isn't working
- **`enhancement`** - New feature or request
- **`documentation`** - Improvements or additions to docs
- **`good first issue`** - Good for newcomers
- **`help wanted`** - Extra attention is needed
- **`question`** - Further information is requested

## <img src="assets/icons/phone.svg" alt="Getting Help" width="20" height="20" style="vertical-align: middle;"> Getting Help

### Questions and Discussion
- **Open an issue** for questions or discussions
- **Use the issue template** to provide context
- **Be patient** - maintainers are volunteers

### Code Reviews
- **Be open to feedback** and suggestions
- **Respond to review comments** promptly
- **Make requested changes** or explain why not
- **Ask questions** if something isn't clear

## <img src="assets/icons/hands-praying.svg" alt="Recognition" width="20" height="20" style="vertical-align: middle;"> Recognition

Contributors will be:
- **Listed in the README** contributors table with their contribution types
- **Recognized for all types of contributions** (not just code) following the [All Contributors](https://github.com/all-contributors/all-contributors) specification
- **Mentioned in release notes** for their work
- **Thanked in the project** documentation

### Contribution Types

The All Contributors system recognizes many types of contributions:

- **<img src="assets/icons/terminal.svg" alt="Code" width="16" height="16" style="vertical-align: middle;"> Code** - Writing or reviewing code
- **<img src="assets/icons/books.svg" alt="Documentation" width="16" height="16" style="vertical-align: middle;"> Documentation** - Writing or improving docs
- **<img src="assets/icons/bug.svg" alt="Bug Reports" width="16" height="16" style="vertical-align: middle;"> Bug reports** - Finding and reporting issues
- **<img src="assets/icons/lightbulb.svg" alt="Ideas" width="16" height="16" style="vertical-align: middle;"> Ideas** - Planning, feedback, and suggestions
- **<img src="assets/icons/wrench.svg" alt="Maintenance" width="16" height="16" style="vertical-align: middle;"> Maintenance** - Ongoing project maintenance
- **<img src="assets/icons/palette.svg" alt="Design" width="16" height="16" style="vertical-align: middle;"> Design** - UI/UX improvements
- **<img src="assets/icons/globe.svg" alt="Translation" width="16" height="16" style="vertical-align: middle;"> Translation** - Localization and translations
- **<img src="assets/icons/clipboard-text.svg" alt="Review" width="16" height="16" style="vertical-align: middle;"> Review** - Code and PR reviews
- **<img src="assets/icons/question.svg" alt="Support" width="16" height="16" style="vertical-align: middle;"> Support** - Helping others with questions
- **And many more!** - See the [full list](https://allcontributors.org/docs/en/emoji-key)

### <img src="assets/icons/star.svg" alt="Adding Yourself to Contributors" width="20" height="20" style="vertical-align: middle;"> Adding Yourself to Contributors

If you've contributed to this repository in any way, you can add yourself to the Contributors list in the README.md file! Here's how:

1. **Comment on any Issue or Pull Request** with:
   ```
   @all-contributors please add @your-username for <contribution-type>
   ```

2. **Available contribution types** include:
   - `code` - Programming contributions
   - `doc` - Documentation improvements
   - `bug` - Bug reports
   - `ideas` - Ideas and planning
   - `review` - Code reviews
   - `test` - Testing and quality assurance
   - `infra` - Infrastructure and tooling
   - And many more!

3. **The bot will automatically**:
   - Create a Pull Request to add you
   - Update the Contributors section
   - Use your custom icons and styling

**Learn more**: Check out the [@all-contributors Bot Usage Guide](https://allcontributors.org/docs/en/bot/usage) for detailed instructions and all available contribution types.

> <img src="assets/icons/lightbulb.svg" alt="Tip" width="16" height="16" style="vertical-align: middle;"> **Pro Tip**: You can add multiple contribution types at once: `@all-contributors please add @username for code, doc, ideas`

## <img src="assets/icons/file-text.svg" alt="License" width="20" height="20" style="vertical-align: middle;"> License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

**Thank you for contributing to Make Gist List! <img src="assets/icons/rocket.svg" alt="Launch" width="20" height="20" style="vertical-align: middle;">**

Your contributions help make this tool better for everyone in the GitHub community.

Thanks goes to these wonderful people ([emoji key](docs/emoji-key.md)):

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
