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

Admin backup control is part of this public API surface through `mycel.admin.v1.AdminBackupService`. The daemon remains the only component that reads, quiesces, snapshots, or restores Mycel storage; applications should call the Admin API instead of copying a live data directory.

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
