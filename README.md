# Mycel API

Protocol contract and generated Go stubs for MycelDB daemon APIs.

Module path:

```text
github.com/myceldb/mycel-api
```

## Contents

- `api/proto/`: protobuf source definitions for Mycel Admin, Client, and Common APIs.
- `gen/go/`: committed generated Go protobuf/gRPC stubs.
- `buf.yaml`, `buf.gen.yaml`: Buf lint/generation configuration.

This repository intentionally does not contain daemon implementation code. Applications may import generated stubs directly, but most Go applications should prefer the higher-level `mycel-go-sdk` connector once available.

Admin backup control is part of this public API surface through `mycel.admin.v1.AdminBackupService`. The daemon remains the only component that reads, quiesces, snapshots, or restores Mycel storage; applications should call the Admin API instead of copying a live data directory.

## Go imports

Examples:

```go
clientv1 "github.com/myceldb/mycel-api/gen/go/mycel/client/v1"
adminv1 "github.com/myceldb/mycel-api/gen/go/mycel/admin/v1"
commonv1 "github.com/myceldb/mycel-api/gen/go/mycel/common/v1"
```

## Generate

```sh
go run github.com/bufbuild/buf/cmd/buf@v1.50.1 lint
go run github.com/bufbuild/buf/cmd/buf@v1.50.1 generate
go test ./...
```

Generated Go files are committed so downstream Go modules can consume this repository directly.
