# Changelog

All notable changes to Mycel API should be documented in this file.

This project follows the spirit of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Protobuf packages use explicit package versions such as `mycel.client.v1`; compatibility-affecting changes should be called out clearly even before a stable `v1.0.0` repository release.

## [Unreleased]

## [v0.16.0] - 2026-09-24

### Added

- Added the graph `replace_references` operation, including reference replacement modes, targets, and operation results so clients can reconcile relationship edges in one transaction-scoped graph operation.

## [v0.15.0] - 2026-09-18

### Added

- Added dimensioned cluster readiness fields to `mycel.admin.v1.ClusterReadiness`, including process, metadata, Raft, read, and write readiness signals.

## [v0.12.0] - 2026-09-09

### Added

- Added hybrid search API seams to `mycel.client.v1.SearchService`, including `SEARCH_MODE_HYBRID`, lexical/semantic candidate options, weighted reciprocal-rank fusion options, structured metadata filters, and source diagnostics.

## [v0.11.0] - 2026-09-07

### Added

- Added lexical search API contracts: `mycel.client.v1.SearchService` for lexical search/status and `mycel.admin.v1.AdminLexicalMaintenanceService` for rebuild maintenance.

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
