# Third-party notices and dependency license inventory

This repository is licensed under the Apache License, Version 2.0. It contains MycelDB protobuf API definitions and currently declares no third-party protobuf module dependencies in `buf.yaml`.

Tracked issue: MycelDB/mycel-api#2

## Inventory

The generated inventory is committed at:

```text
docs/legal/dependency-license-inventory.tsv
```

Current inventory status: no third-party dependencies are declared by this API-only repository.

## Covered ecosystems

- Protobuf API sources under `api/proto`.
- Buf configuration in `buf.yaml`.

CI actions and locally installed developer tools are not redistributed as part of this repository and are not included in the committed dependency inventory.

## Notice handling

- Keep upstream copyright, license, and NOTICE files intact if third-party protobuf definitions or generated material are added later.
- Do not remove license headers from generated code or copied third-party source.
- API source releases should keep this notice document and inventory in the repository and release source archives.
- This inventory is a release-hygiene aid and is not legal advice.

## Regeneration

Run:

```sh
python3 scripts/generate-license-inventory.py
```

The script currently verifies that `buf.yaml` has no external `deps` entries and rewrites the inventory header. If external protobuf dependencies are added later, extend the script and this document to record their package names, versions, licenses, and notice requirements.
