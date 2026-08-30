# Agent instructions for mycel-api

This repository is the language-independent protobuf and gRPC contract for MycelDB. It is API-contract-only.

## Scope

Agents may edit:

- `api/proto/**/*.proto`
- `buf.yaml`
- API documentation such as `README.md` and `CONTRIBUTING.md`
- CI/configuration files that validate this API contract

Agents must not add:

- MycelDB daemon implementation code
- SDK helper/client abstraction code
- Generated protobuf/gRPC bindings
- Language-specific generated directories
- Product-specific application behavior

## Protobuf rules

When editing `.proto` files:

- Preserve `// SPDX-License-Identifier: Apache-2.0` at the top of every proto file.
- Do not add language-specific generation options such as Go `go_package`.
- Do not reuse field numbers.
- Prefer additive changes in existing `v1` packages.
- Reserve removed field numbers and names when performing an intentional versioned migration.
- Prefer explicit request and response messages for RPCs.
- Keep resource IDs opaque unless comments define a format.
- Document streaming, pagination, authorization, concurrency, and idempotency semantics when relevant.

## Breaking changes

Ask for maintainer approval before making a breaking API change, including:

- Removing or renaming fields, messages, enums, services, RPCs, or packages
- Changing field types incompatibly
- Moving types between packages
- Changing unary RPCs to streaming RPCs, or streaming RPCs to unary RPCs
- Changing semantics in a way existing clients cannot safely tolerate

Substantial breaking changes should normally use a new package version, for example `mycel.client.v2`.

## Validation

Before handing off changes, run:

```sh
make test
```

If proto formatting changed or might be needed, run:

```sh
make format
make test
```

For compatibility-sensitive changes, also run the agreed breaking-change check, for example:

```sh
make breaking BREAKING_AGAINST=<baseline>
```

Report exactly which commands were run and their results.

## Documentation

When public API behavior changes, update the README or related docs in the same change. Do not leave branch-specific migration notes in the README unless the branch context is intentionally part of the current documentation.
