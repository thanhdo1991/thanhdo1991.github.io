---
id: data-migration
version: 2.0.0
confidence: 0.80
success_rate: 0.78
last_updated: 2026-06-29
tags:
  - data
  - migration
  - rigid
---

# Data Migration

> Rigid skill. Migrate data safely: backup first, validate with dry-run, process in batches, and verify after each stage. Data loss is not an option.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "The script is simple, I can run it directly" | A missing WHERE clause, wrong join condition, or production data anomaly can destroy or corrupt thousands of records. |
| "We have backups, we can restore if it fails" | Restoring a multi-terabyte database takes hours. The cost of restore is higher than the cost of caution. |
| "I tested on a copy of the data" | If the copy was not an exact replica (sampled, anonymized, truncated), the test is not valid. |
| "We'll fix any issues manually after" | Manual fixes at scale are error-prone, not audited, and often make the problem worse. |

## Process

### Phase 1: Plan
1. Understand the source schema and data format.
2. Understand the target schema and data format (if different).
3. Define the transformation rules: column mapping, type conversion, default values, deduplication.
4. Estimate the data volume: number of records, total size, expected duration.
5. Define rollback strategy: keep the source data intact until the migration is verified.

### Phase 2: Backup
1. Take a full backup of the source data. Verify the backup is restorable.
2. For production: take the backup immediately before starting the migration.
3. Store the backup in a separate location from the production database.

### Phase 3: Dry-Run
1. Run the migration script in a staging environment with production-like data volume.
2. Validate: record counts match, no nulls in required fields, no orphaned references.
3. Check performance: does the migration complete within the maintenance window?
4. Dry-run must succeed three consecutive times before production.

### Phase 4: Batch Migration
1. Process data in batches (recommended: 1000-10000 records per batch).
2. Each batch is a transaction. If one batch fails, the previous batches are committed.
3. Log each batch: records processed, duration, errors encountered.
4. Monitor system resources (CPU, memory, disk I/O, replication lag).

### Phase 5: Verify
1. Compare record counts: source vs target. They must match.
2. Spot-check random records for data integrity (field-by-field comparison).
3. Run application-level integrity checks: can the application read, display, and update migrated data?
4. Run the verification from the application's perspective, not just SQL queries.

## Red Flags (STOP Signals)

- Running a migration without a validated backup.
- Skip dry-run phase. Dry-run is not optional.
- Migrations that modify source data before full verification of the target.
- Single transaction processing all records (risk of rollback of millions of records).
- No rollback plan. If the migration goes wrong, how do you recover?

## No Exceptions

- Do not run a data migration without a complete, verified backup.
- Do not skip the dry-run. Test the full migration process on staging with production-like data.
- Do not modify source data until the target has been fully verified.
- Do not process the entire dataset in a single transaction.
