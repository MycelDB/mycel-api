# Mycel API

Language-independent protobuf and gRPC contract for MycelDB.

This repository is the source of truth for the public MycelDB daemon API surface. It defines the protobuf packages, messages, enums, and gRPC services used by the daemon, consoles, SDKs, and applications. It intentionally contains no daemon implementation code, SDK convenience helpers, or committed generated language bindings.

## API packages

The protobuf definitions live under `api/proto/` and are grouped by audience:

| Package | Purpose | Examples |
| --- | --- | --- |
| `mycel.common.v1` | Shared primitives used by both admin and client APIs. | Authentication, access/capability concepts, inference metadata. |
| `mycel.client.v1` | Application-facing APIs for graph users and client SDKs. | Spaces, sessions, transactions, graph operations, queries, blobs, schema, metadata catalogs, semantic search, import/export, automation, graph-change streaming. |
| `mycel.admin.v1` | Operator and administrative APIs. | Principals, role/capability grants, spaces/domains, cluster state, backups, inference catalog, semantic maintenance, activity/audit APIs. |

All current public API packages are versioned as `v1`. Package version is the compatibility boundary.

## Repository boundaries

This repo **does** contain:

- `.proto` source files for public MycelDB APIs.
- Buf configuration for linting and breaking-change checks.
- Documentation for API evolution and gRPC conventions.

This repo **does not** contain:

- MycelDB daemon/server implementation.
- Generated Go, Rust, TypeScript, Java, Python, or other bindings.
- SDK-level helper APIs or ergonomic wrappers.
- Product-specific client logic.

Generated code belongs in downstream consumers:

- `mycel` generates the Go server/client stubs it needs for the daemon and CLI.
- `mycel-go-sdk` generates the Go client stubs it needs for SDK helpers.
- `mycel-rust-sdk` generates Rust client stubs during Cargo builds.
- `mycel-console` and future tools should generate or consume bindings from `api/proto/` rather than committing generated output here.

The proto files avoid language-specific generation options such as Go `go_package`; consumers provide those mappings in their own generation configuration.

## gRPC conventions

MycelDB APIs use protobuf `proto3` service definitions exposed over gRPC.

### Authentication

Authentication is unified through `mycel.common.v1.AuthService`, which issues short-lived access tokens and durable refresh sessions for all principals.

Authenticated RPCs should receive the access token as gRPC metadata:

```text
authorization: Bearer <access-token>
```

Administrative authorization is modeled through `mycel.admin.v1.AdminPrincipalService` role bindings and capability grants, not through separate admin/operator/user auth services.

### Errors

Implementations should use canonical gRPC status codes consistently:

| Status | Typical meaning |
| --- | --- |
| `INVALID_ARGUMENT` | The request shape or field values are invalid. |
| `UNAUTHENTICATED` | Authentication is missing, expired, or invalid. |
| `PERMISSION_DENIED` | The principal is authenticated but lacks required capability. |
| `NOT_FOUND` | The requested space, domain, session, transaction, graph object, blob, or other resource does not exist. |
| `ALREADY_EXISTS` | Creation conflicts with an existing resource or unique constraint. |
| `FAILED_PRECONDITION` | The resource exists but is not in a state that allows the operation. |
| `ABORTED` | A transaction or optimistic concurrency operation conflicted. |
| `RESOURCE_EXHAUSTED` | A quota, limit, or capacity constraint was reached. |
| `UNAVAILABLE` | The daemon or dependent service is temporarily unavailable. |
| `INTERNAL` | An unexpected server-side failure occurred. |

Clients should not parse human-readable error strings for control flow. Use gRPC status codes and any structured error details exposed by the implementation.

### IDs and names

Resource IDs are opaque unless a field comment says otherwise. Clients should store and round-trip IDs exactly as returned by the API and should not infer meaning from their format.

### Pagination and limits

List/search RPCs should expose bounded result sets and cursor-style continuation where needed. Clients should treat cursors as opaque values and should not assume cursor stability across unrelated queries.

### Streaming

Streaming RPCs must document:

- Whether the stream is server-streaming, client-streaming, or bidirectional.
- The meaning of initial checkpoint messages, live event messages, heartbeats, and gap messages.
- How clients should resume after reconnecting.
- Whether stream events are best-effort, at-least-once, or exactly-once.

## Compatibility and evolution

API stability matters more in this repository than in an implementation repository. Treat every committed protobuf definition as a public contract.

Compatible changes within a `v1` package include:

- Adding a new field with a new field number.
- Adding a new message, enum, service, or RPC.
- Adding a new enum value when clients are expected to handle unknown values.
- Marking a field, enum value, service, or RPC as deprecated before a later package-version migration.
- Clarifying comments without changing behavior.

Breaking changes include:

- Removing or renaming a field, message, enum, enum value, service, RPC, or package.
- Reusing a field number or changing a field type incompatibly.
- Moving a type between packages.
- Changing request/response cardinality, such as unary to streaming or streaming to unary.
- Changing semantics in a way existing clients cannot safely tolerate.

When a field is removed in a future breaking package version, reserve both the field number and name in the old message shape to prevent accidental reuse:

```proto
message Example {
  reserved 3;
  reserved "old_field";
}
```

Substantial breaking changes should normally happen in a new package version, for example `mycel.client.v2`, with migration notes.

## Authoring protobuf changes

When changing `.proto` files:

- Keep `// SPDX-License-Identifier: Apache-2.0` at the top of each file.
- Use package names under `mycel.common.v1`, `mycel.client.v1`, or `mycel.admin.v1` unless introducing a deliberate new version or API area.
- Prefer explicit request and response messages for every RPC, even when the current request or response is empty.
- Add comments for public services, RPCs, messages, fields, and enum values when behavior is not obvious from the name.
- Do not reuse field numbers.
- Do not commit generated bindings.
- Do not add language-specific generation options to these proto files.
- Prefer additive evolution and deprecation over removal.
- Document streaming, pagination, authorization, and concurrency semantics at the service or field level when they are part of the contract.

## Validate the contract

Install [Buf](https://buf.build/) or run it through your preferred toolchain, then validate:

```sh
make test
```

`make test` runs protobuf linting and verifies that proto files are already formatted. To rewrite proto files in place, run:

```sh
make format
```

Before merging changes that may affect compatibility, also run a breaking-change check against the appropriate baseline:

```sh
make breaking BREAKING_AGAINST=<baseline>
```

The baseline may be a previous release tag, a remote branch, a Buf Schema Registry module reference, or another agreed contract source.

## Consuming the API

Downstream projects should pin this repository by tag, commit, or registry reference, then generate bindings in their own build system.

Examples:

- Go consumers can use Buf or `protoc` with `protoc-gen-go` and `protoc-gen-go-grpc` in the consuming repository.
- Rust consumers can use `tonic-build` from `build.rs`.
- TypeScript/JavaScript consumers can use their preferred protobuf/gRPC generator in the consuming repository.

Keep generated output out of this repository. If generated output is committed anywhere, it should be committed in the consuming project that owns its language-specific build and release lifecycle.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for API compatibility rules, protobuf authoring expectations, and the pull request checklist. See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) for community standards and [`CHANGELOG.md`](CHANGELOG.md) for release notes.

## Security

Please report suspected vulnerabilities privately through GitHub Security Advisories / private vulnerability reporting. See [`SECURITY.md`](SECURITY.md).

## License

Licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).
