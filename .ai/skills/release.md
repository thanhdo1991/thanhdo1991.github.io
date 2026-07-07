---
id: release
version: 2.0.0
confidence: 0.85
success_rate: 0.82
last_updated: 2026-06-29
tags: [skill, process, devops, release]
---

# Release

Software release management and deployment coordination.

## Overview
The release process covers version bumping, changelog updates, build, staging verification, production deployment, and post-release monitoring.

## Related Skills
- **[process/changelog-management.md](process/changelog-management.md)** — Changelog format and maintenance
- **[devops/deployment.md](devops/deployment.md)** — Deployment strategies and rollback
- **[devops/ci-cd-setup.md](devops/ci-cd-setup.md)** — CI/CD pipeline configuration

## Key Principles
1. **Automate everything** — Manual steps introduce errors
2. **Changelog first** — Document changes before tagging
3. **Staging parity** — Test in staging that mirrors production
4. **Rollback ready** — Every release must have a tested rollback plan
5. **Semantic versioning** — Follow semver for dependency communication

## Quality Gates
- [ ] All tests pass (unit + integration + e2e)
- [ ] Changelog updated with all changes
- [ ] Version bumped per semver
- [ ] Staging deployment verified
- [ ] Rollback plan confirmed
- [ ] Release notes reviewed
- [ ] Database migrations backward-compatible
