# Contributing to Mycel API

Thank you for contributing to the MycelDB API contract. This repository is intentionally small and contract-focused: changes here affect every daemon, SDK, console, and application that consumes MycelDB APIs.

## Code of conduct

Be respectful, constructive, and patient. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards and reporting guidance.

## Before you start

- Discuss large or breaking API changes in an issue or design discussion before opening a PR.
- Keep changes focused on protobuf API definitions, validation configuration, and API documentation.
- Do not add daemon implementation code, SDK helper code, or generated language bindings to this repository.

## Local validation

Install [Buf](https://buf.build/), then run:

```sh
make test
```

This runs protobuf linting and formatting checks.

Useful targets:

```sh
make lint          # buf lint
make format        # rewrite proto files with buf format -w
make format-check  # verify proto formatting without rewriting
```

For compatibility-sensitive changes, run a breaking-change check against the agreed baseline:

```sh
make breaking BREAKING_AGAINST=<baseline>
```

The baseline may be a release tag, a Buf Schema Registry module reference, a remote branch, or another agreed source of truth.

## Protobuf compatibility rules

Treat every committed `.proto` file as a public contract.

Prefer additive changes:

- Add new fields with new field numbers.
- Add new messages, enums, services, or RPCs.
- Add new enum values only when clients are expected to tolerate unknown values.
- Deprecate before removal.
- Clarify comments when behavior is ambiguous.

Avoid breaking changes in existing `v1` packages:

- Do not remove or rename public fields, messages, enums, services, RPCs, or packages.
- Do not reuse field numbers.
- Do not change field types incompatibly.
- Do not move types between packages without a versioned migration.
- Do not change an RPC from unary to streaming, or streaming to unary, within the same package version.
- Do not silently change semantics that existing clients rely on.

When a field is removed as part of a deliberate versioned migration, reserve both its number and name:

```proto
message Example {
  reserved 3;
  reserved "old_field";
}
```

Substantial breaking changes should normally happen in a new package version, such as `mycel.client.v2`, with migration notes.

## Proto authoring checklist

For new or changed `.proto` files:

- Keep `// SPDX-License-Identifier: Apache-2.0` at the top of the file.
- Use `syntax = "proto3";`.
- Use packages under `mycel.common.v1`, `mycel.client.v1`, or `mycel.admin.v1` unless intentionally introducing a new API area or version.
- Prefer explicit request and response messages for every RPC.
- Use opaque string IDs unless the contract explicitly says otherwise.
- Treat pagination cursors as opaque values.
- Document streaming behavior, resume behavior, checkpoints, heartbeats, and gaps.
- Document authorization, concurrency, and idempotency semantics when they matter.
- Avoid language-specific generation options such as Go `go_package`.
- Do not commit generated code.

## Pull request expectations

A good API PR includes:

- A clear description of the API change and motivation.
- Notes on compatibility and migration impact.
- Updated README/docs when the public contract or conventions change.
- Passing `make test` output.
- Breaking-check evidence when the change might affect compatibility.

## Security issues

Do not report security vulnerabilities in public issues. See [SECURITY.md](SECURITY.md) for private reporting instructions.
