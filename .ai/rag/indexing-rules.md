---
id: rag-indexing-rules
version: 1.0.0
confidence: 0.90
success_rate: 0.87
last_updated: 2026-06-29
tags: [rag, indexing, rules, update-frequency]
---

# Indexing Rules

Defines what gets indexed, what is skipped, update frequency, and conflict resolution strategy.

## What Gets Indexed

| Content Type | Directory | Index? | Priority |
|-------------|-----------|--------|----------|
| Reflections | `.ai/reflections/` | Yes | High |
| Decisions (ADRs) | `.ai/decisions/` | Yes | High |
| Failure analyses | `.ai/failures/` | Yes | Medium |
| Patterns | `.ai/patterns/` | Yes | High |
| Skills | `.ai/skills/` | Yes | High |
| Changelog entries | `.ai/changelog/` | Yes | Low |
| Meeting notes | `.ai/meetings/` | Yes | Low |
| Templates | `.ai/templates/` | No | — |
| Configuration | `.ai/rag/`, `.ai/observability/` | No | — |
| Shell scripts | `.ai/lib/` | No | — |
| Commands | `.claude/commands/` | No | — |

## Exclusions

Files matching these patterns are always excluded:

1. **Binary files:** `*.png`, `*.jpg`, `*.gif`, `*.ico`, `*.pdf`, `*.zip`
2. **Generated outputs:** `*.log`, `*.tmp`, `*.lock`
3. **Version control:** Any file in `.git/`
4. **Templates directory** (indexed by reference only)
5. **Config directory** (not indexed)
6. **Files without valid frontmatter** (logged as warning)

## Indexing Triggers

| Trigger | Action | Scope |
|---------|--------|-------|
| New file created | Index immediately | Single file |
| File modified | Re-index on next sync | Single file |
| File deleted | Remove from index | Single file |
| Periodic full sync | Run daily or periodic index command | Full collection |
| Embedding model changed | Re-index ALL documents | Full collection |

## Update Frequency

| Sync Type | Frequency | Method |
|-----------|-----------|--------|
| Individual file | On write (via watcher/hook) | Incremental, append-only |
| Bulk sync | Daily or on-demand | Full scan, dedup by checksum |
| Full re-index | When model changes | Drop and rebuild |

## Conflict Resolution

| Conflict Scenario | Resolution Strategy |
|-------------------|-------------------|
| Same checksum exists | Skip (no change) |
| Same ID, different checksum | Update in-place |
| Same content in different file | Allow (both indexed, different source_path) |
| Same file path, different content | Replace with latest |
| Corrupt embedding | Skip, log warning, retry on next sync |

## Indexing Pipeline

```
File change detected
       ↓
[1] Read file content
       ↓
[2] Parse YAML frontmatter
       ↓
[3] Validate frontmatter (reject if invalid)
       ↓
[4] Compute checksum (SHA256)
       ↓
[5] Check for existing checksum → skip if unchanged
       ↓
[6] Chunk content (per chunking rules)
       ↓
[7] Generate embeddings for each chunk
       ↓
[8] Store in vector DB with metadata
       ↓
[9] Update file index manifest
```

## Index Integrity Checks

- Run `validate-frontmatter.sh` before every bulk index.
- Verify checksum matches content before re-indexing.
- Log all errors to `.ai/observability/index-errors.log`.
- Maintain a manifest file at `.ai/rag/.index-manifest.json`.
