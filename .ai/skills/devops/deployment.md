---
id: deployment
version: 2.0.0
confidence: 0.85
success_rate: 0.82
last_updated: 2026-06-29
tags:
  - devops
  - deployment
  - rigid
---

# Deployment

> Rigid skill. Safe, repeatable deployments with backup, health checks, rollback plan, and gradual rollout. Every deployment is a procedure, not a script.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "It's a small change, just push it" | Small changes cause production incidents every day. Deployment rigor is not proportional to diff size. |
| "We can fix forward if something goes wrong" | Fix-forward assumes the issue is simple and immediately understood. Complex failures require rollback. |
| "The tests passed, it will be fine" | Tests cover known scenarios. Production data, traffic patterns, and concurrency are unknown unknowns. |
| "Rolling back is complicated, let's not" | Every deployment without a rollback plan is a bet with the service's availability. |

## Process

### Phase 1: Pre-Deployment Checklist
1. Are all tests passing on the target branch? Check CI status.
2. Is the deployment artifact built from the exact commit being deployed?
3. Is the database migration backward-compatible and ready?
4. Is the rollback plan documented and reviewed?
5. Is the team notified of the deployment window?

### Phase 2: Backup
1. If the deployment involves a database migration: take a backup first.
2. Backup configuration files, environment variables, and secrets if they are changing.
3. Verify the backup is restorable (checksum, restore test).

### Phase 3: Gradual Rollout
1. **Staging**: Deploy to staging. Run smoke tests.
2. **Canary**: Deploy to 1-5% of production instances. Monitor error rates, latency, and resource usage for 5-15 minutes.
3. **Expansion**: Increase to 25%, 50%, then 100%. Monitor after each step.
4. **Full rollout**: All instances running the new version.

### Phase 4: Health Check Verification
After each rollout step, verify:
- Application health endpoint returns 200.
- Error rate is not elevated (compare to pre-deployment baseline).
- Latency P50, P95, P99 are within thresholds.
- Database connection pool is not exhausted.
- Background jobs are processing normally.

### Phase 5: Rollback Procedure
1. If any health check fails at any stage: **rollback immediately**.
2. Rollback process: deploy the previous artifact. Revert the database migration if applicable.
3. After rollback: run health checks to confirm the service is healthy.
4. Post-mortem: what went wrong? What should the fix be?

## Red Flags (STOP Signals)

- Deployment during peak traffic hours without emergency approval.
- No documented rollback procedure.
- Skipping canary or staging environments.
- Manual steps that are not scripted or documented.
- Deploying on a Friday afternoon.

## No Exceptions

- Do not deploy without a rollback plan. Written, reviewed, and tested.
- Do not skip health checks. Every deployment must verify the application is healthy after deploy.
- Do not deploy database schema changes and application code changes simultaneously. Decouple them: schema change first, then application deploy.
- Do not deploy if any CI stage is failing. A failing CI means unknown risk.
