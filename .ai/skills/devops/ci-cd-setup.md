---
id: ci-cd-setup
version: 2.0.0
confidence: 0.80
success_rate: 0.76
last_updated: 2026-06-29
tags:
  - devops
  - cicd
  - pipeline
  - flexible
---

# CI/CD Setup

> Flexible skill. Design and implement CI/CD pipelines with lint, test, build, and deploy stages. Each stage must provide fast feedback and clear failure signals.

## Overview

A CI/CD pipeline automates the process from code commit to production deployment. Done well, it provides fast, reliable feedback to developers and enables frequent, safe deployments. Done poorly, it becomes a bottleneck that everyone tries to bypass.

**Core Principle**: Each stage should catch a specific class of errors and fail fast. If a failure takes 20 minutes to discover, the pipeline is too slow. Pipeline health is product health.

## Step-by-Step Process

### Phase 1: Pipeline Architecture
Define stages in order of speed and value:
1. **Lint**: Syntax and style checking (< 1 minute). Catches formatting, unused imports, type errors.
2. **Unit Tests**: Fast, isolated tests (< 5 minutes). Catches logic errors.
3. **Build**: Compile or bundle the application (< 5 minutes). Catches compilation errors.
4. **Integration Tests**: Tests against real dependencies (< 10 minutes). Catches contract errors.
5. **Security Scan**: Dependency audit and SAST (< 5 minutes). Catches vulnerabilities.
6. **Deploy**: Push to environment (varies). Staged: staging -> canary -> production.

### Phase 2: Stage Configuration
For each stage, define:
- **Trigger**: push to branch, PR creation, merge to main, scheduled.
- **Cache**: dependency caches (npm, pip, maven) to speed up subsequent runs.
- **Parallelism**: independent stages run in parallel (lint + unit tests + security scan).
- **Retention**: how long artifacts, logs, and reports are kept.

### Phase 3: Failure Handling
1. **Fail fast**: If lint fails, stop the pipeline. Don't waste resources on later stages.
2. **Status**: Every pipeline run should produce a clear status: passing, failed, or unstable.
3. **Notifications**: Failed stages notify the committer and the team channel.
4. **Flaky detection**: Track test flakiness. Flaky tests should be quarantined, not ignored.

### Phase 4: Deployment Strategy
1. **Staging**: Deploy every merge to staging. Run integration tests.
2. **Canary**: Deploy to a subset of instances or users. Monitor error rates.
3. **Production**: Full rollout with automated rollback if error rate exceeds threshold.
4. **Rollback**: One-click rollback to the previous version. Test the rollback procedure.

## Common Mistakes

- **Pipeline too slow**: A 30-minute pipeline encourages developers to push without running tests locally. Optimize the pipeline to provide feedback under 10 minutes.
- **Hardcoded secrets in pipeline config**: Use the CI platform's secrets management. Never put tokens, keys, or passwords in YAML files.
- **Building in deploy stage**: Build once, deploy the same artifact everywhere. Rebuilding in each environment produces different artifacts.
- **Skipping tests to speed up CI**: If tests are skipped, the pipeline doesn't validate correctness. Speed up the tests instead.
- **No pipeline for infrastructure**: Infrastructure changes should go through the same pipeline as application changes.

## Quality Gates

- [ ] Pipeline completes in < 10 minutes for a typical commit.
- [ ] Every stage has a clear success/failure criterion.
- [ ] Secrets are managed via platform secrets, not in code.
- [ ] Deploy stage uses the same artifact built in the build stage.
- [ ] Rollback is tested and documented.
- [ ] Pipeline status is visible to the entire team.
