# Changelog

All notable changes to this project will be documented in this file, in reverse chronological order by release.

The format is based on [Keep a Changelog](https://keepachangelog.com),
and this project adheres to [Semantic Versioning](https://semver.org).

## [Unreleased]

### Added
- Enhanced documentation with better discoverability
- Improved setup guide with troubleshooting
- Better contributing guidelines
- Enhanced README with badges and clear structure

### Changed
- Simplified project structure for easier forking
- Removed complex multi-repo functionality
- Focused on core gist list generation functionality

## [1.0.0] - 2024-01-15

### Added
- Initial release of Make Gist List
- Core functionality to fetch and list public GitHub gists
- Markdown table generation with gist metadata
- Optional gist updating capability
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
