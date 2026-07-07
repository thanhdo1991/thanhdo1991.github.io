---
id: database-design
version: 2.0.0
confidence: 0.80
success_rate: 0.75
last_updated: 2026-06-29
tags:
  - data
  - database
  - schema
  - flexible
---

# Database Design

> Flexible skill. Design database schemas that are normalized, performant, and maintainable. Cover indexing strategy, migration planning, and naming conventions.

## Overview

Database design shapes how data is stored, queried, and evolved over the lifetime of an application. Good design minimizes data redundancy, ensures consistency, and enables efficient querying. The design must balance normalization (reducing duplication) with denormalization (improving read performance).

**Core Principle**: Design for consistency first, then optimize for performance. Data that is duplicate but correct is fixable; data that is inconsistent is untrustworthy.

## Step-by-Step Process

### Phase 1: Conceptual Model
1. Identify entities (nouns in the domain: User, Order, Product, etc.).
2. Define relationships: one-to-one, one-to-many, many-to-many.
3. Identify attributes for each entity and their data types.
4. Define business rules and constraints (unique, not-null, check, foreign key).

### Phase 2: Normalization
1. 1NF: Each column contains atomic values. No arrays or JSON blobs for related data.
2. 2NF: Every non-key column depends on the entire primary key (relevant for composite keys).
3. 3NF: Every non-key column depends only on the primary key. No transitive dependencies.
4. Evaluate: does the query pattern justify denormalization? Only denormalize when measured.

### Phase 3: Primary Key Strategy
1. Prefer auto-increment integers or UUIDs. Both are valid; choose based on:
   - Auto-increment: faster, smaller index, sequential. Risk: enumeration attacks, migration conflicts.
   - UUID: globally unique, merge-friendly. Risk: larger index, slower inserts, fragmentation.
2. Avoid natural keys (email, SSN) as primary keys. They change or may be reused.
3. Use composite keys only for junction tables or natural hierarchies.

### Phase 4: Indexing Strategy
1. Index primary keys and foreign keys (automatic in most databases).
2. Index columns used in WHERE, JOIN, ORDER BY, and GROUP BY clauses.
3. For composite indexes: order columns by selectivity (most selective first).
4. Avoid over-indexing: each index slows writes by N + 1 operations.
5. Use partial indexes for filtered queries, covering indexes for frequent queries.

## Common Mistakes

- **Storing denormalized data too early**: Optimize for read patterns only after measuring. Premature denormalization creates sync nightmares.
- **No foreign key constraints**: The application will have bugs. Foreign keys are the last line of defense for referential integrity.
- **Missing created_at/updated_at**: Every table needs timestamps for debugging, auditing, and replication.
- **Using strings for dates**: Always use the database's native date/time types. String comparison is wrong, slow, and unmaintainable.
- **Not planning for deletion**: Soft delete adds complexity. Hard delete breaks referential integrity. Plan the deletion strategy upfront.

## Quality Gates

- [ ] Entity definitions capture the domain language, not table/column names.
- [ ] Tables have a primary key, created_at, and updated_at columns.
- [ ] Foreign keys are defined for all relationships (no orphaned references).
- [ ] Indexes exist for all foreign keys and common query patterns.
- [ ] Column types match the data domain (DOB as date, not string; price as decimal, not float).
