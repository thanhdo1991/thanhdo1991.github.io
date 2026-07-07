---
id: rag-schema
version: 1.0.0
confidence: 0.95
success_rate: 0.92
last_updated: 2026-06-29
tags: [rag, schema, vector-db, database]
---

# RAG Schema Definition

This document defines the table structure, fields, and data types for the vector database used in the self-improving framework.

## Collection: `framework_knowledge`

Primary collection storing all indexed knowledge artifacts.

### Field Definitions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | UUID (v4) | Yes | Unique identifier for each record |
| `content` | Text | Yes | The main content body (markdown) |
| `content_type` | Enum | Yes | Type: reflection, decision, pattern, failure, skill, changelog, meeting, estimate |
| `source_file` | String | Yes | Relative path from `.ai/` to the source file |
| `source_path` | String | Yes | Full relative path including filename |
| `embedding` | Float[] | Yes | Vector embedding of the content |
| `created_at` | DateTime | Yes | Record creation timestamp |
| `updated_at` | DateTime | Yes | Last modification timestamp |
| `checksum` | String (SHA256) | Yes | Content hash for deduplication |
| `chunk_index` | Integer | No | Position of this chunk within the source document |
| `total_chunks` | Integer | No | Total number of chunks for the source document |

### Metadata Fields (stored alongside content)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | String | Yes | Title extracted from document |
| `tags` | String[] | Yes | Tags from frontmatter |
| `confidence` | Float [0-1] | Yes | Confidence score from frontmatter |
| `success_rate` | Float [0-1] | Yes | Success rate from frontmatter |
| `version` | String | Yes | Semantic version |
| `last_used` | DateTime | No | Last retrieval timestamp |
| `use_count` | Integer | No | Cumulative retrieval count |
| `related_ids` | String[] | No | IDs of related records |

### Collection: `framework_stats`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | UUID (v4) | Yes | Unique identifier |
| `metric_name` | String | Yes | Name of the metric |
| `metric_value` | Float | Yes | Current value |
| `window_size` | Integer | Yes | Rolling window for this metric |
| `recorded_at` | DateTime | Yes | When this data point was recorded |

### Indexes

| Index Name | Field(s) | Type |
|------------|----------|------|
| `idx_content_type` | content_type | B-tree |
| `idx_tags` | tags | GIN (array) |
| `idx_confidence` | confidence | B-tree |
| `idx_created_at` | created_at | B-tree |
| `idx_checksum` | checksum | Unique |
| `idx_embedding` | embedding | IVFFlat / HNSW |
