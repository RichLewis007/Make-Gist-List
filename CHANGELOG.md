# Changelog

All notable changes to this project will be documented in this file, in reverse chronological order by release.

The format is based on [Keep a Changelog](https://keepachangelog.com),
and this project adheres to [Semantic Versioning](https://semver.org).

## [Unreleased]

### Added
- **All Contributors integration** with custom Phosphor icons
- **Automated icon replacement system** for contributor badges
- **Comprehensive local command line documentation** in SETUP.md
- **Repository secrets support** for better forkability
- **Custom icon assets** (30+ Phosphor icons) for enhanced visual appeal
- **Automated workflows** for icon maintenance and contributor updates
- **Enhanced README** with improved badge layout and local usage instructions
- **Educational documentation** - Comprehensive optimization techniques guide for developers
- **Batched GraphQL implementation** for efficient star count fetching
- **Engagement metrics** - Comments, forks, and stars in the generated gist list
- **Professional logging system** with configurable verbosity levels and structured output

### Changed
- **Switched from environment secrets to repository secrets** for easier forking
- **Updated gist icons** from emojis to Unicode symbols (✓/✗) for better gist compatibility
- **Improved documentation structure** with clear local vs GitHub Actions usage
- **Enhanced environment variable documentation** with clearer required/optional distinctions
- **Streamlined workflow configuration** using built-in GitHub variables
- **Optimized API usage** - Replaced individual star count calls with batched GraphQL queries (26-40% fewer API calls)
- **Enhanced code documentation** with comprehensive docstrings and inline comments
- **Upgraded logging system** - Replaced print statements with professional Python logging module
- **Improved fallback handling** - Show "N/A" instead of "0" when star count data is unavailable

### Fixed
- **Gist markdown compatibility** - removed HTML img tags that don't work in gists
- **Badge layout** - All Contributors badge now displays inline with other badges
- **Documentation accuracy** - clarified which variables are required for full functionality

## [1.0.0] - 2024-01-15

### Added
- Initial release of Make Gist List
- Core functionality to fetch and list public GitHub gists
- Markdown table generation with gist metadata
- Gist updating capability
- GitHub Actions workflow for automated updates
- Cross-platform compatibility

### Features
- Fetches all public gists for a specified GitHub user
- Generates formatted markdown tables with:
  - Gist title and description
  - File count and primary language
  - Public/private status
  - Last updated timestamp
  - Direct links to gists
- Automatic daily updates via GitHub Actions
- Configurable via environment variables
- Minimal GitHub API permissions (gist scope only)

### Technical Details
- Python 3.10+ compatibility
- Uses GitHub REST API v3
- Built with `requests` library
- Follows PEP 8 coding standards
- Comprehensive error handling and retry logic
- Rate limiting awareness and handling

---

## Version History

- **1.0.0** - Initial release with core functionality
- **Future versions** - Will include new features, improvements, and bug fixes

## Contributing to the Changelog

When adding new entries to the changelog, please:
- Follow the existing format
- Use clear, concise language
- Group changes by type (Added, Changed, Deprecated, Removed, Fixed, Security)
- Include the date for new releases
- Keep entries focused and specific
