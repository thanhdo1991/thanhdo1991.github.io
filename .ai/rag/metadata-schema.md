---
id: rag-metadata-schema
version: 1.0.0
confidence: 0.95
success_rate: 0.93
last_updated: 2026-06-29
tags: [rag, metadata, schema, validation, indexing]
---

# Metadata Schema

Defines all frontmatter fields, validation rules, and indexing fields used across the framework.

## Common Frontmatter Fields (All Files)

| Field | Type | Required | Default | Validation |
|-------|------|----------|---------|------------|
| `id` | String | Yes | — | Must be kebab-case, max 64 chars, unique per content type |
| `version` | String (semver) | Yes | 1.0.0 | Must match `^\d+\.\d+\.\d+$` |
| `confidence` | Float | Yes | 0.50 | Range 0.0 — 1.0, step 0.01 |
| `success_rate` | Float | Yes | — | Range 0.0 — 1.0, only on templates and skills with tracked usage |
| `last_updated` | Date | Yes | — | Must match `^\d{4}-\d{2}-\d{2}$` |
| `tags` | String[] | Yes | — | Array of kebab-case strings, 1-10 tags, each 2-32 chars |

## Content-Type-Specific Fields

### Reflection
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `task_id` | String | Yes | References the task or plan item |
| `duration_minutes` | Integer | No | Actual time spent |

### Decision (ADR)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `status` | Enum | Yes | proposed, accepted, deprecated, superseded |
| `superseded_by` | String | No | ID of the decision that supersedes this one |

### Failure Analysis
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `severity` | Enum | Yes | critical, major, minor, cosmetic |
| `incident_date` | Date | Yes | Date of the incident |

### Pattern
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `category` | Enum | Yes | architectural, creational, structural, behavioral, idiomatic, anti-pattern |
| `scope` | Enum | Yes | component, module, system, cross-system |

### Skill
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `trigger_pattern` | String | Yes | Keyword or phrase that triggers this skill |
| `prerequisites` | String[] | No | Required tools or conditions |

### Changelog Entry
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `version` | String | Yes | Matching the version in filename |
| `release_date` | Date | Yes | Date of release |

## Validation Rules

1. **Required fields** must be present and non-empty.
2. **Confidence** must be a float between 0.0 and 1.0 inclusive.
3. **Success rate** must be a float between 0.0 and 1.0 inclusive.
4. **Tags** must be unique within the array (no duplicates).
5. **Dates** must be in ISO 8601 format (YYYY-MM-DD).
6. **ID** must be globally unique across all files of the same content type.
7. **Version** must follow strict semver with no leading `v`.

## Indexing Fields

These fields in frontmatter are indexed for RAG retrieval:

| Field | Index Strategy | Purpose |
|-------|---------------|---------|
| `id` | Primary key | Unique lookup |
| `tags` | Inverted index + filter | Content-type filtering |
| `confidence` | Range index | Quality filtering |
| `success_rate` | Range index | Proven-effectiveness filtering |
| `last_updated` | Range index | Recency filtering |
| `version` | Exact match | Version-specific queries |

## Example: Validated Frontmatter

```yaml
---
id: my-cool-resource
version: 1.2.3
confidence: 0.87
success_rate: 0.91
last_updated: 2026-06-29
tags: [reflection, debugging, python]
---
```
