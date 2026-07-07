---
id: rag-chroma-schema
version: 1.0.0
confidence: 0.85
success_rate: 0.83
last_updated: 2026-06-29
tags: [rag, chroma, schema, vector-db]
---

# Chroma DB Schema

Specific configuration for Chroma DB as the vector database backend.

## Collection Configuration

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Collection Name** | `{{PROJECT_NAME}}_framework_knowledge` | Replace PROJECT_NAME with your project |
| **Distance Function** | `cosine` | Options: cosine, l2, ip (inner product) |
| **Metadata Store** | SQLite (embedded) | Chroma default |
| **Persistence** | `./.chroma/` | Directory relative to project root |

## Collection Metadata

```python
collection_metadata = {
    "hnsw:space": "cosine",
    "hnsw:construction_ef": 200,    # Build time accuracy vs speed
    "hnsw:M": 32,                    # Max number of connections per layer
    "hnsw:search_ef": 100,           # Search depth (higher = slower but more accurate)
    "description": "{{PROJECT_NAME}} self-improving framework knowledge base",
    "version": "1.0.0",
    "created": "2026-06-29",
}
```

## Chroma-Specific Metadata Filters

All frontmatter fields are stored as Chroma metadata. These can be used in `where` filters:

```python
# Filter by content type
collection.query(
    query_embeddings=[embedding],
    where={"content_type": "reflection"}
)

# Filter by confidence threshold
collection.query(
    query_embeddings=[embedding],
    where={"confidence": {"$gte": 0.8}}
)

# Filter by multiple tags (any match)
collection.query(
    query_embeddings=[embedding],
    where={"tags": {"$contains": "debugging"}}
)

# Compound filter
collection.query(
    query_embeddings=[embedding],
    where={
        "$and": [
            {"content_type": "decision"},
            {"confidence": {"$gte": 0.85}},
            {"tags": {"$contains": "architecture"}}
        ]
    }
)
```

## Query Templates

### Template 1: Recall relevant knowledge before task

```python
def recall_before_task(task_description, task_tags, limit=5):
    return collection.query(
        query_texts=[task_description],
        n_results=limit,
        where={
            "$and": [
                {"content_type": {"$in": ["reflection", "decision", "pattern", "failure"]}},
                {"confidence": {"$gte": 0.6}}
            ]
        }
    )
```

### Template 2: Find related failures

```python
def find_related_failures(context, limit=3):
    return collection.query(
        query_texts=[context],
        n_results=limit,
        where={"content_type": "failure"}
    )
```

### Template 3: Skill retrieval

```python
def find_relevant_skills(query, confidence_min=0.7):
    return collection.query(
        query_texts=[query],
        n_results=3,
        where={
            "$and": [
                {"content_type": "skill"},
                {"confidence": {"$gte": confidence_min}}
            ]
        }
    )
```

## Chroma Client Configuration

```python
import chromadb

# Persistent client (recommended)
client = chromadb.PersistentClient(
    path="./.chroma",
    settings=chromadb.Settings(
        anonymized_telemetry=False,
        allow_reset=True,  # Only for development
    )
)

# Get or create collection
collection = client.get_or_create_collection(
    name="{{PROJECT_NAME}}_framework_knowledge",
    metadata=collection_metadata
)
```

## Batch Insert Pattern

```python
def batch_insert(records, batch_size=20):
    """Insert records with metadata in batches."""
    for i in range(0, len(records), batch_size):
        batch = records[i:i+batch_size]
        collection.add(
            ids=[r["id"] for r in batch],
            embeddings=[r["embedding"] for r in batch],
            metadatas=[r["metadata"] for r in batch],
            documents=[r["content"] for r in batch],
        )
```

## Limitations

1. **Max metadata size:** 4096 bytes per record. Keep metadata lean.
2. **Max document size:** Effective limit is ~200K tokens per document.
3. **No full-text search within Chroma** — combine with SQLite FTS5 for hybrid search.
4. **No built-in document versioning** — implement via checksum in metadata.
