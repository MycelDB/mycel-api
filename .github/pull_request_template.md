## Summary

<!-- What changed and why? -->

## API compatibility

- [ ] This change is additive/backward compatible.
- [ ] This change may be breaking and has maintainer approval.
- [ ] Removed fields reserve both field numbers and names.
- [ ] Field numbers are not reused.
- [ ] Streaming, pagination, authorization, concurrency, and idempotency semantics are documented where relevant.

## Repository boundaries

- [ ] No generated protobuf/gRPC bindings are committed.
- [ ] No daemon implementation code is added.
- [ ] No SDK helper/convenience code is added.
- [ ] New `.proto` files include `// SPDX-License-Identifier: Apache-2.0`.
- [ ] Language-specific generation options were not added to proto files.

## Validation

- [ ] `make test` passes.
- [ ] Breaking-change check was run when compatibility may be affected: `make breaking BREAKING_AGAINST=<baseline>`.

## Notes

<!-- Migration notes, downstream SDK impact, or follow-up work. -->
