---
id: dependency-audit
version: 2.0.0
confidence: 0.75
success_rate: 0.72
last_updated: 2026-06-29
tags:
  - quality
  - dependencies
  - flexible
---

# Dependency Audit

> Flexible skill. Systematically audit project dependencies for known vulnerabilities, license compliance, maintenance status, and drift. Run regularly, not just at release time.

## Overview

Every dependency is a risk: a security vulnerability, a license violation, a maintenance abandonment, or a breaking change. Regular audits keep these risks visible and manageable. The goal is not zero dependencies but conscious dependency management.

**Core Principle**: Every dependency you add is a maintainer you hire. Choose wisely, audit regularly, and remove when unused.

## Step-by-Step Process

### Phase 1: Inventory
1. List all direct and transitive dependencies for each ecosystem (npm, pip, maven, cargo, etc.).
2. Categorize each dependency by function: framework, utility, database driver, testing, build tool.
3. Identify unused dependencies: grep imports, check build output, use `depcheck` or equivalent.

### Phase 2: Vulnerability Scan
1. Run the ecosystem's vulnerability scanner: `npm audit`, `pip audit`, `cargo audit`, `mvn dependency-check`.
2. For each vulnerability:
   - Severity: critical, high, medium, low.
   - Reachability: is this code path used in the application?
   - Fix available: update to a patched version, or workaround exists?
3. Schedule remediation: critical within 48 hours, high within 1 week, medium next sprint.

### Phase 3: License Audit
1. Check licenses for each dependency against the project's license policy.
2. Flag copyleft licenses (GPL, AGPL, SSPL) in proprietary projects.
3. Flag "non-commercial" or "research only" licenses in commercial products.
4. Ensure all licenses are compatible with each other.

### Phase 4: Maintenance Assessment
For each critical dependency, evaluate:
- **Last release date**: Has it been over a year since the last release?
- **Response time**: How quickly do maintainers respond to issues and PRs?
- **Community health**: Are there active contributors? Is there a bus factor of 1?
- **Deprecation signals**: Is the README marked as unmaintained? Is there a recommended alternative?

### Phase 5: Remediation
1. Update vulnerable or outdated dependencies to safe versions.
2. Remove unused dependencies. Each removal reduces attack surface and build time.
3. For abandoned critical deps: fork and maintain internally, or find a maintained replacement.
4. Pin exact versions for production dependencies (avoid auto-update ranges).

## Common Mistakes

- **Ignoring transitive dependencies**: Your direct deps may be healthy, but their transitive deps may be vulnerable. Audit the full tree.
- **Auditing only at release**: Vulnerabilities are discovered daily. Audit monthly at minimum.
- **Blindly running update --all**: Each update should be intentional. Test each update independently.
- **Not documenting audit results**: Record what was checked, what was found, and what was fixed. Audit trails are required for compliance.
- **Removing a dep without checking all imports**: A grep might miss dynamic imports or indirect usage. Run the full test suite after removal.

## Quality Gates

- [ ] Dependency audit runs in CI on every commit (or weekly scheduled).
- [ ] Zero critical vulnerabilities without an approved exception.
- [ ] All dependency licenses are compatible with the project license.
- [ ] No dependency is more than one major version behind the latest stable.
- [ ] Unused dependencies are removed (confirmed by working build and tests).
