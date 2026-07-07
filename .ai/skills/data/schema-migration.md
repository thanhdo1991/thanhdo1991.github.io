---
id: schema-migration
version: 2.0.0
confidence: 0.85
success_rate: 0.80
last_updated: 2026-06-29
tags:
  - data
  - migration
  - rigid
---

# Schema Migration

> Rigid skill. Safe, backward-compatible database schema migrations with rollback plans. Every migration must be testable on staging before production.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "I'll just manually ALTER TABLE in production" | No rollback, no review, no audit trail. Manual changes bypass every safety control. |
| "It's just adding a column, no risk" | Adding a NOT NULL column without a default locks the table and requires downtime. |
| "We'll fix the rollback later" | If the rollback isn't written, the migration can't be rolled back. All forward, no exit. |
| "Staging is close enough to production" | Differences in data volume, distribution, and access patterns cause staging to miss production issues. |

## Process

### Phase 1: Design Migration
1. Make every change backward-compatible:
   - Add columns as nullable or with a default. NOT NULL comes in a separate migration.
   - Rename by adding a new column, migrating data, then dropping the old.
   - Remove columns by first deploying code that stops reading them.
2. Write both `up` and `down` scripts. The `down` script must restore the previous state with complete data.

### Phase 2: Review
1. Check that no existing queries break with the intermediate schema state.
2. Verify the migration handles existing data correctly (fills defaults, transforms values).
3. Check lock impact: `ALTER TABLE` may lock the table. Use `pt-online-schema-change` or `gh-ost` for large tables.

### Phase 3: Test on Staging
1. Run the migration on a staging environment with production-like data volume.
2. Verify data integrity before and after the migration.
3. Run the application against the migrated schema and confirm all features work.
4. Test the rollback on staging: run `down`, confirm the schema and data return to the original state.

### Phase 4: Run in Production
1. Take a backup immediately before the migration.
2. Run the migration during low-traffic hours.
3. Monitor database performance, lock wait times, and replication lag.
4. After migration: run a data integrity check and verify application health.

## Red Flags (STOP Signals)

- Migrations without a `down` script. Every migration must be reversible.
- NOT NULL columns added without a default value for existing rows.
- Renaming tables or columns without a migration plan that handles the intermediate state.
- Data transformations in a schema-only migration. Separate schema changes from data changes.
- Running a migration without a recent backup.

## No Exceptions

- Do not run un-reviewed migrations in production. Every migration requires at minimum one peer review.
- Do not skip staging testing for any schema change that affects existing data.
- Do not combine multiple schema changes in a single migration. One logical change per migration file.
- Do not modify a committed migration. Apply a new migration to fix it.
