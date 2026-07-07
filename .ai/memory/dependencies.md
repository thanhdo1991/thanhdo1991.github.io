---
id: dependencies
version: 1.0.0
confidence: 0.95
success_rate: 0.88
last_updated: 2026-06-29
tags:
  - dependencies
  - maintenance
  - security
  - template
---

# Dependency Management

## Purpose

Dependencies are a source of functionality, risk, and maintenance burden. This
document defines how the project manages its dependencies — tracking, updating,
auditing, and retiring them.

---

## Dependency Inventory

Maintain a current inventory of all dependencies. This can be generated from lock
files or package manifests, but the following summary should be kept here:

### Runtime Dependencies

| Package | Version | Purpose | License | Risk Level | Last Audited |
|---------|---------|---------|---------|------------|--------------|
| [package] | [version] | [what it does] | [MIT / Apache / GPL] | [Low / Medium / High] | YYYY-MM-DD |
| [package] | [version] | [what it does] | [MIT / Apache / GPL] | [Low / Medium / High] | YYYY-MM-DD |

### Development Dependencies

| Package | Version | Purpose | License | Risk Level | Last Audited |
|---------|---------|---------|---------|------------|--------------|
| [package] | [version] | [testing / linting / build] | [MIT / Apache / GPL] | [Low / Medium / High] | YYYY-MM-DD |
| [package] | [version] | [testing / linting / build] | [MIT / Apache / GPL] | [Low / Medium / High] | YYYY-MM-DD |

---

## Update Policy

### Cadence

| Update Type | Frequency | Process |
|-------------|-----------|---------|
| **Security patches** | As soon as available | Automated PR with priority review |
| **Minor / patch updates** | Weekly (batched) | Automated PR, pass CI, merge |
| **Major version upgrades** | Quarterly review + as needed | Requires ADR, manual testing, team review |
| **Deprecated packages** | Within 2 release cycles | Plan migration, create ADR, execute |

### Rules

- All dependencies **must be pinned** to exact versions in production builds.
- **Lock files** (package-lock.json, yarn.lock, Cargo.lock, go.sum, Gemfile.lock,
  poetry.lock, etc.) are committed to version control.
- **Peer dependencies** must be compatible with the project's primary dependency
  versions. Verify compatibility on upgrade.
- **Transitive dependencies** are included in security scanning. A vulnerability in a
  transitive dependency is treated the same as a direct one.

## Security Auditing

| Tool | Scope | Schedule | Action on Finding |
|------|-------|----------|-------------------|
| [SAST tool] | Runtime dependencies | Every CI run | Block merge for critical/high |
| [SAST tool] | Dev dependencies | Every CI run | Block merge for critical/high |
| [Dependency graph] | All | Continuous (GitHub/Dependabot) | Automated PRs |
| [Manual audit] | High-risk deps | Quarterly | Document in dependencies.md |

### Severity Response Times

| Severity | Response Time | Fix Time |
|----------|---------------|----------|
| Critical | Immediate | Within 24 hours |
| High | Within 24 hours | Within 1 week |
| Medium | Within 1 week | Within 1 month |
| Low | Next release cycle | Next release cycle |

## Adding a New Dependency

Before adding a new dependency, answer these questions in the PR description:

1. **Is it necessary?** Can we implement this functionality with existing code?
2. **Is it well-maintained?** Recent releases, responsive maintainers, community size.
3. **Is the license compatible?** Check against the project's license.
4. **Is it secure?** Any known vulnerabilities? Security disclosure process?
5. **What is the bundle/install size impact?** Is the size justified?
6. **Is there a simpler alternative?** Fewer features but simpler integration?

## Removing a Dependency

1. Ensure all usages are migrated away.
2. Remove the package and clean up configuration.
3. Run the full test suite to verify nothing is broken.
4. Update the dependency inventory in this file.
5. Consider writing a brief ADR if the dependency was significant.

---

## Tools & Automation

| Function | Tool | Configuration |
|----------|------|---------------|
| Version updates | [Dependabot / Renovate / Snyk] | [config file path] |
| Security scanning | [npm audit / cargo audit / pip-audit / trivy] | [config file path] |
| License compliance | [FOSSA / License Finder] | [config file path] |
| Size analysis | [bundlephobia / webpack-bundle-analyzer] | [config file path] |

---

*Keep this document current. An outdated dependency inventory is worse than none.*
