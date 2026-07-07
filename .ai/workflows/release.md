---
id: workflow-release-001
version: 1.0.0
confidence: 0.85
success_rate: 0.80
last_updated: 2026-06-29
tags: [workflow, release, deployment]
---

# Release Workflow

End-to-end release process from changelog management through production deployment with rollback safety.

## Flowchart

```
[Release Decision] → [Update Changelog] → [Bump Version]
    → [Tag Commit] → [Build Artifacts] → [Run Full Test Suite]
    → [Tests Pass?] → [No] → [Fix Blockers] → [Rebuild]
    → [Yes] → [Deploy to Staging]
    → [Staging Verification: Smoke Tests + E2E]
    → [Staging Passes?] → [No] → [Rollback Staging] → [Fix & Rebuild]
    → [Yes] → [Deploy to Production]
    → [Production Verification: Health Checks + Monitoring]
    → [Production Healthy?] → [No] → [Rollback Production] → [Incident Response]
    → [Yes] → [Release Complete: Announce]
    → [Done]
```

## Trigger

- Feature complete for the planned release scope.
- Bugfix release is warranted (enough fixes accumulated or critical fix).
- Scheduled release date arrives.
- Hotfix for a production incident requires immediate release.

## Steps

### 1. Update Changelog
- **Input**: Release scope, merged PRs, commit log.
- **Process**: Review the unreleased section of CHANGELOG.md. Ensure all significant changes are documented. Categorize: Added, Changed, Deprecated, Removed, Fixed, Security. Check that entries are user-facing and meaningful (not internal refactoring noise).
- **Output**: Updated CHANGELOG.md with the new release version and date.
- **Quality Gate**: Every breaking change is clearly marked. No internal-only changes in the changelog. Format follows Keep a Changelog conventions.

### 2. Bump Version
- **Input**: Changelog, release type (major/minor/patch/hotfix).
- **Process**: Update version in all relevant files (package.json, Cargo.toml, version.py, etc.). Use semantic versioning. The version bump reflects the changelog content (major for breaking, minor for features, patch for fixes).
- **Output**: Version-bumped files, committed.
- **Quality Gate**: Version is consistent across all files. The version number matches the changelog section. Pre-release identifiers (alpha, beta, rc) are used appropriately.

### 3. Tag Commit
- **Input**: Version-bumped commit.
- **Process**: Create a signed git tag with the version number (e.g., v1.2.3). Push the tag to the remote. The tag message includes the changelog summary for that version.
- **Output**: Git tag (local + remote).
- **Quality Gate**: Tag is on the correct commit (the version bump commit). Tag format matches project convention. Tag is pushed to the remote.

### 4. Build & Test
- **Input**: Tagged codebase.
- **Process**: Build all artifacts (compiled code, Docker images, packages). Run the full test suite: unit, integration, e2e. Run security scans (see security-audit.md). Run lint and type checking.
- **Output**: Build artifacts, test results.
- **Decision Point**: `[All Tests Pass?] → [Yes] → [Proceed to Staging] | [No] → [Identify blocker] → [Fix → Rebuild → Retest]`.
- **Quality Gate**: Zero test failures. Zero lint errors. Security scan shows no Critical/High findings. Build is reproducible (same source produces same artifact).

### 5. Deploy to Staging
- **Input**: Verified build artifacts.
- **Process**: Deploy to the staging environment that mirrors production. Run smoke tests (critical user journeys). Run e2e tests against staging. Monitor staging logs and metrics for anomalies.
- **Output**: Running staging instance, smoke test results.
- **Decision Point**: `[Staging Passes?] → [Yes] → [Proceed to Production] | [No] → [Rollback staging] → [Root cause → Fix → Rebuild]`.
- **Quality Gate**: Staging smoke tests cover: login, core business flow, API health, database migration success (if applicable). No new errors in staging logs beyond expected baseline.

### 6. Deploy to Production
- **Input**: Verified build, staging approval.
- **Process**: Deploy using the project's deployment strategy (blue/green, canary, rolling update). Apply database migrations with care (backward-compatible first). Monitor deployment progress.
- **Output**: Production deployment.
- **Quality Gate**: Deployment is automated (not manual SSH). Migrations are reversible. If using canary: start with 1% traffic, ramp up on health signals.

### 7. Verify Production
- **Input**: Running production deployment.
- **Process**: Check health endpoints. Monitor error rates, latency, and traffic patterns for 15+ minutes. Verify critical user journeys in production. Check that monitoring and alerting are operational for the new version.
- **Output**: Production health report.
- **Decision Point**: `[Production Healthy?] → [Yes] → [Release complete] | [No: Errors spiking] → [Rollback] → [Incident response]`.
- **Quality Gate**: Error rate is at or below pre-deployment baseline. P99 latency is within SLO. Key business metrics (conversions, signups, etc.) are not degrading.

### 8. Announce
- **Input**: Successful release.
- **Process**: Post the release announcement in team channels. Update the relevant deployment status boards. If applicable, notify users (via changelog, in-app notification, or release notes).
- **Output**: Release announcement.
- **Quality Gate**: Announcement links to the changelog entry for the release. Known issues or limitations are communicated.

## Output

- Released version (tagged, deployed).
- Updated CHANGELOG.md.
- Deployment verification report.
- (Optional) Rollback incident record if deployment failed.
