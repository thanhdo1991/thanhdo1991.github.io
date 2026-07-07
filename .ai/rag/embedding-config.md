---
id: rag-embedding-config
version: 1.0.0
confidence: 0.90
success_rate: 0.88
last_updated: 2026-06-29
tags: [rag, embedding, configuration, vector]
---

# Embedding Configuration

Defines the embedding model, parameters, and configuration for vector generation and retrieval.

## Model Configuration

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Provider** | Anthropic / OpenAI / Local | Choose based on environment; local recommended for privacy |
| **Model** | `text-embedding-3-small` | Recommended for cost-effectiveness; `text-embedding-3-large` for higher accuracy |
| **Dimensions** | 1536 (small) / 3072 (large) | text-embedding-3-small = 1536, text-embedding-3-large = 3072 |
| **Max Input Tokens** | 8191 | Inputs exceeding this are truncated |
| **Distance Metric** | Cosine Similarity | Recommended for semantic search |

## Alternative Embedding Providers

| Provider | Model | Dimensions | Use Case |
|----------|-------|-----------|----------|
| OpenAI | text-embedding-3-small | 1536 | General purpose, cost-efficient |
| OpenAI | text-embedding-3-large | 3072 | High-accuracy retrieval |
| Sentence Transformers | all-MiniLM-L6-v2 | 384 | Local, offline capable |
| Sentence Transformers | all-mpnet-base-v2 | 768 | Local, better accuracy |
| Cohere | embed-english-v3.0 | 1024 | Enterprise, multilingual support |

## Chunking Strategy

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Chunk Size** | 512 tokens | Balances context and precision |
| **Chunk Overlap** | 64 tokens (12.5%) | Ensures no context loss at boundaries |
| **Chunking Method** | Recursive character split | Respects markdown boundaries (headers, paragraphs) |
| **Min Chunk Size** | 100 tokens | Avoids overly small fragments |

## Chunking Rules

1. **Prefer boundary breaks** at markdown headings (`##`, `###`) first.
2. **Fall back** to paragraph breaks (`\n\n`) if no heading within chunk_size.
3. **Fall back** to sentence breaks if no paragraph break.
4. **Never split** inline code, tables, or code blocks.
5. **Metadata** (frontmatter) is embedded separately as context for the document.
6. **Title + tags** are prepended to each chunk for context.

## Retrieval Parameters

| Parameter | Default | Range | Notes |
|-----------|---------|-------|-------|
| **Top-K** | 5 | 3-20 | Number of results returned |
| **Score Threshold** | 0.65 | 0.0-1.0 | Minimum similarity score |
| **MMR Lambda** | 0.3 | 0.0-1.0 | Diversity factor (0 = max relevance, 1 = max diversity) |
| **Max Source Distance** | 3 chunks | — | Maximum gap between chunks from same doc |

## Performance Recommendations

- **Batch size:** 20 documents per embedding call.
- **Cache:** Cache embeddings with a TTL of 24 hours.
- **Re-index** when the embed model changes (invalidate all vectors).
- **Dimension reduction:** Not recommended; use full dimensions for best accuracy.
