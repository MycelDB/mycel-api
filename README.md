# Mycel API

Language-independent protobuf contract for MycelDB daemon APIs.

This repository is the source of truth for Mycel Admin, Client, and Common API definitions. It intentionally does **not** contain daemon implementation code, SDK helpers, or committed generated language bindings.

## Contents

- `api/proto/`: protobuf source definitions for Mycel Admin, Client, and Common APIs.
- `buf.yaml`: Buf module, lint, and breaking-change configuration.

The proto files avoid language-specific generation options such as Go `go_package`; consumers provide those mappings in their own generation configuration.

Generated code belongs in the consuming project:

- `mycel` generates the Go server/client stubs it needs for the daemon and CLI.
- `mycel-go-sdk` generates the Go client stubs it needs for SDK helpers.
- `mycel-rust-sdk` generates Rust client stubs during Cargo builds.
- Other SDKs should generate bindings from `api/proto/` rather than committing generated output here.

Authentication is unified through `mycel.common.v1.AuthService`, which exposes short-lived access tokens plus durable refresh sessions for all principals. System management is modeled through `mycel.admin.v1.AdminPrincipalService` role bindings and capability grants, not separate admin/operator/user auth services.

Admin backup control is part of this public API surface through `mycel.admin.v1.AdminBackupService`. Backup policy supports interval schedules for compatibility plus calendar-style daily/weekly schedules using `schedule_kind`, `time_of_day`, `timezone`, `weekdays`, and `run_missed`. Backup archive format is represented by the `BackupArchiveFormat` enum via `archive_format`; supported values are ZIP, TAR, TAR_GZ, and TAR_ZST, while UNSPECIFIED defaults to ZIP. The legacy string `compression` field is deprecated for compatibility. The daemon remains the only component that reads, quiesces, snapshots, or restores Mycel storage; applications should call the Admin API instead of copying a live data directory.

## Graph change watch migration

The `add_callbacks` branch replaces the old public Client change-stream surface
with `mycel.client.v1.GraphChangeService.WatchGraphChanges` in
`api/proto/mycel/client/v1/graph_change.proto`.

Breaking migration notes:

- `ChangeStreamService.WatchDomainChanges` and related `WatchDomainChanges*`
  messages are removed.
- `GraphChangeService.WatchGraphChanges` streams committed graph-change
  envelopes for one space/domain.
- `WatchGraphChangesRequest.after_revision` resumes after the last processed
  event revision.
- `include_current` sends an initial checkpoint with the current observed
  revision before live events.
- `GraphChangeGap` means the requested history is unavailable; clients should
  rebuild or resync derived state and reconnect from a fresh checkpoint.
- `GraphChangeOrigin.operation_id` echoes transaction operation correlation
  metadata so clients can identify their own writes.

## Operation ID helper contract

Client SDKs should expose a small helper for transaction operation correlation:

- Generate UUID v4 strings for `mycel.client.v1.BeginTransactionRequest.operation_id`.
- Accept caller-provided operation IDs when beginning transactions.
- Return or expose `GraphTransaction.operation_id` and `TransactionCommit.operation_id` from begin/commit responses.

Recommended helper names:

- Go SDK: `NewOperationID() string` and a transaction-begin helper that accepts an operation ID.
- Rust SDK: `new_operation_id() -> String` and a transaction-begin helper that accepts an operation ID.

The API contract treats operation IDs as correlation metadata only. They are not idempotency keys, authorization credentials, replay protection, or commit ordering guarantees. The daemon validates non-empty client-provided values as UUID strings and generates one when omitted.

## Validate the contract

Install Buf or run it through your preferred toolchain, then validate:

```sh
make test
```

Equivalent direct command:

```sh
buf lint
```

If you maintain a breaking-change baseline, also run:

```sh
buf breaking --against <baseline>
```

## Generate bindings downstream

Consumers should keep language-specific generation config in their own repository. For example, a Go consumer can configure `protoc-gen-go`/`protoc-gen-go-grpc` or Buf in that project and write output to an ignored local generated directory. Rust consumers can use `tonic-build` in `build.rs`.

Do not commit generated code to this repository.
