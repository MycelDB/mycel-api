# Changelog

All notable changes to Mycel API should be documented in this file.

This project follows the spirit of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Protobuf packages use explicit package versions such as `mycel.client.v1`; compatibility-affecting changes should be called out clearly even before a stable `v1.0.0` repository release.

## [Unreleased]

## [v0.9.0] - 2026-08-31

### Added

- First public-release baseline for the MycelDB protobuf/gRPC API contract.
- Open-source project documentation: contributing guide, security policy, code of conduct, changelog, pull request template, and issue templates.

### Changed

- Documented repository boundaries for daemon, SDK, console, and generated binding consumers.
- Documented protobuf compatibility, authoring, validation, authentication, error, pagination, and streaming conventions.

## Release notes policy

For each release, add a dated section such as:

```md
## [v0.9.0] - YYYY-MM-DD

### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
```

Include notes for public package/service/RPC/message/field changes, compatibility impact, deprecations, breaking-change checks, migration requirements, and matching daemon/SDK/console versions.
