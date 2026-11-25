# Admin usage metric names

`mycel.admin.v1.UsageMetric.name`, `GetUsageRequest.metric_names`,
`ListUsageRequest.metric_names`, and `UsageLimit.metric_name` use stable string
metric identifiers. Adding a new metric identifier does not require a protobuf
field or enum change, but the metric name, unit, authority, quota safety, and
formula are part of the public API contract.

Usage snapshots separate quota-safe logical metrics from diagnostic/physical
observations. Clients must not treat diagnostic metrics as billing or hard-limit
inputs unless a later API contract explicitly changes their safety metadata.

## Quota-safe graph metrics

| Metric | Unit | Authority | Quota-safe | Hard-limit eligible | Formula |
| --- | --- | --- | --- | --- | --- |
| `graph.node_count` | `USAGE_UNIT_COUNT` | `USAGE_AUTHORITY_RAFT_COMMITTED_EXACT` | yes | yes | Count committed, non-deleted graph nodes owned by the requested scope. |
| `graph.edge_count` | `USAGE_UNIT_COUNT` | `USAGE_AUTHORITY_RAFT_COMMITTED_EXACT` | yes | yes | Count committed, non-deleted graph edges owned by the requested scope. |
| `graph.logical_bytes` | `USAGE_UNIT_BYTES` | `USAGE_AUTHORITY_RAFT_COMMITTED_EXACT` | yes | no | Sum UTF-8 bytes of scalar values inside committed node `payload` maps owned by the requested scope. |

`graph.logical_bytes` counts payload content, not graph storage overhead:

- string scalar values count their UTF-8 byte length;
- numeric and boolean scalar values count the byte length of their deterministic
  text representation;
- `null` values count as zero;
- arrays and nested maps recurse into their values;
- payload map keys and JSON structural syntax do not count;
- labels/tags, properties, metadata, edge payloads, blob payload bytes, indexes,
  WAL bytes, and physical graph-store overhead do not count.

## Quota-safe blob metrics

| Metric | Unit | Authority | Quota-safe | Hard-limit eligible | Formula |
| --- | --- | --- | --- | --- | --- |
| `blob.active_count` | `USAGE_UNIT_COUNT` | `USAGE_AUTHORITY_RAFT_COMMITTED_EXACT` | yes | yes | Count committed active blob metadata descriptors owned by the requested scope. |
| `blob.active_logical_bytes` | `USAGE_UNIT_BYTES` | `USAGE_AUTHORITY_RAFT_COMMITTED_EXACT` | yes | yes | Sum committed payload byte sizes from active blob metadata descriptors owned by the requested scope. |
| `blob.local_active_count` | `USAGE_UNIT_COUNT` | `USAGE_AUTHORITY_RAFT_COMMITTED_EXACT` | yes | yes | Count active blob descriptors whose payload backend is local filesystem. |
| `blob.local_active_logical_bytes` | `USAGE_UNIT_BYTES` | `USAGE_AUTHORITY_RAFT_COMMITTED_EXACT` | yes | yes | Sum active payload byte sizes for local-filesystem blob descriptors. |
| `blob.object_store_active_count` | `USAGE_UNIT_COUNT` | `USAGE_AUTHORITY_RAFT_COMMITTED_EXACT` | yes | yes | Count active blob descriptors whose payload backend is object-store/S3-compatible. |
| `blob.object_store_active_logical_bytes` | `USAGE_UNIT_BYTES` | `USAGE_AUTHORITY_RAFT_COMMITTED_EXACT` | yes | yes | Sum active payload byte sizes for object-store-backed blob descriptors. |
| `blob.pending_delete_count` | `USAGE_UNIT_COUNT` | `USAGE_AUTHORITY_RAFT_COMMITTED_EXACT` | yes | no | Count committed blob descriptors or tombstones in an explicit Mycel pending-delete state. |
| `blob.pending_delete_logical_bytes` | `USAGE_UNIT_BYTES` | `USAGE_AUTHORITY_RAFT_COMMITTED_EXACT` | yes | no | Sum payload byte sizes for committed pending-delete descriptors/tombstones. |

## Diagnostic physical metrics

Diagnostic metric names, including `diagnostic.local_graph_store_bytes`, are
observations of local physical or derived storage. They are reported with
`quota_safe=false` and `hard_limit_eligible=false`. They may include filesystem
layout, storage-class overhead, indexes, WAL/checkpoint effects, compression, or
other implementation details, so clients should display them as operational
diagnostics rather than quota/product usage.
