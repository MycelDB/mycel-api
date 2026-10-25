# Changelog

All notable changes to Mycel API should be documented in this file.

This project follows the spirit of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Protobuf packages use explicit package versions such as `mycel.client.v1`; compatibility-affecting changes should be called out clearly even before a stable `v1.0.0` repository release.

## [Unreleased]

### Added

- Added direct semantic continuation tokens, typed hard-eligibility filters, authorization-safe filter diagnostics, and safe per-result generation/route provenance.
- Added Admin semantic reliability and rebuild RPCs with separately named analyzed/fresh frontiers, bounded gap/capacity diagnostics, generation/rebuild state, and work revision/generation evidence.
- Added typed, sanitized procedure-inference attempt/current-state/change-polling contracts, typed automation-run projections, procedure enable/disable barriers, and procedure/binding Intelligence Access selectors.
- Added daemon-owned semantic provider-budget policy, authenticated enforcement-capability discovery, retained-scope status/discovery, and append-only attempt-event reconciliation contracts for bounded live-provider operation.

### Compatibility

- Additive `mycel.client.v1` and `mycel.admin.v1` fields and RPCs preserve existing field numbers and wire compatibility. Clients must capability-check the new RPCs before requiring SGT5 or procedure-inference observability/control proof.
- Generated Go service interfaces gain the new automation RPC methods and four Admin Semantic Maintenance provider-budget RPC methods; custom implementations must update or embed the generated unimplemented servers. Additive Rust message fields affect exhaustive struct literals while preserving protobuf wire compatibility.

## [v0.20.1] - 2026-10-20

### Fixed

- Corrected `GraphTransaction`, `base_revision`, `QueryService.ExecuteQuery`, and `ImportExportService.ExportDomain` documentation to describe the implemented repeatable-read contract: read-only graph, query, and export operations remain pinned to the revision observed through the strong-read path when the transaction begins.

### Compatibility

- Documentation-only correction. Protobuf field numbers, types, services, RPCs, and wire behavior are unchanged from v0.20.0.

## [v0.20.0] - 2026-10-19

### Added

- Added durable graph transaction commit idempotency fields, including explicit scope, replay indication, the original idempotency key, and its retention expiry.
- Added graph idempotency replay, mismatch, capacity, eviction, and active-record diagnostics to cluster runtime status.

### Compatibility

- These `mycel.client.v1` and `mycel.admin.v1` additions are backward compatible; no existing fields or RPCs were removed or renumbered.

## [v0.19.0] - 2026-10-09

### Removed

- Removed the legacy `AdminSpaceService.GrantSpacePrincipal` RPC and request/response messages; space access grants are moving to identity scoped roles/capabilities while `Space.owner` remains the ownership field.

## [v0.18.0] - 2026-10-07

### Added

- Added asynchronous cluster backup operation API contracts to `mycel.admin.v1.AdminBackupService`, including start/status/cancel flow, lifecycle states, cancellation status, retry hints, and structured readiness blockers for Raft convergence.

### Removed

- Removed the synchronous `TriggerClusterBackup` API in favor of the cluster backup operation state machine.

## [v0.17.0] - 2026-09-30

### Added

- Added client space export job APIs to `mycel.client.v1.ImportExportService`, including create, status/list, download, delete, options, counts, and status messages.
- Added admin Raft snapshot and graph checkpoint status APIs, including explicit snapshot creation and graph checkpoint create/status requests.
- Added persistent graph index visibility to `mycel.admin.v1.GraphCheckpointStatus` so operators can inspect local derived index set presence, load result, fallback reason, and entry counts alongside checkpoint status.

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
