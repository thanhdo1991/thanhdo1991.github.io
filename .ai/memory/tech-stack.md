---
id: tech-stack
version: 1.0.0
confidence: 0.95
success_rate: 0.90
last_updated: 2026-06-29
tags:
  - tech-stack
  - template
  - infrastructure
---

# Tech Stack

## Purpose

This document catalogs the technologies used in the project. Keeping an accurate tech
stack record helps with onboarding, dependency audits, upgrade planning, and ensuring
all team members agree on the tools.

---

## Technology Categories

### Programming Languages

| Language | Version | Usage | Status |
|----------|---------|-------|--------|
| [Language] | [X.Y] | [Primary / Scripting / Glue] | [Active / Deprecated / Evaluation] |
| [Language] | [X.Y] | [Testing / Build / DSL] | [Active / Deprecated / Evaluation] |

### Frameworks & Runtimes

| Framework | Version | Purpose | Status |
|-----------|---------|---------|--------|
| [Framework] | [X.Y] | [Web / CLI / Desktop / Mobile] | [Active / Deprecated] |
| [Runtime] | [X.Y] | [Node / JVM / .NET / Python / Go] | [Active / Deprecated] |

### Databases & Storage

| System | Version | Role | Status |
|--------|---------|------|--------|
| [Database] | [X.Y] | [Primary / Cache / Queue / Analytics] | [Active / Deprecated] |
| [Object Store] | [X.Y] | [File storage / Backups / Artifacts] | [Active / Deprecated] |

### Infrastructure & DevOps

| Tool | Version | Purpose | Status |
|------|---------|---------|--------|
| [Container Runtime] | [X.Y] | [Docker / containerd] | [Active / Deprecated] |
| [Orchestrator] | [X.Y] | [Kubernetes / Nomad / Swarm] | [Active / Deprecated] |
| [CI/CD] | [--] | [GitHub Actions / GitLab CI / Jenkins] | [Active / Deprecated] |
| [IaC] | [X.Y] | [Terraform / Pulumi / CloudFormation] | [Active / Deprecated] |

### Observability

| Tool | Purpose | Status |
|------|---------|--------|
| [Logging] | [Structured log aggregation] | [Active / Planned] |
| [Metrics] | [Time-series monitoring] | [Active / Planned] |
| [Tracing] | [Distributed request tracing] | [Active / Planned] |
| [Alerting] | [Incident notification] | [Active / Planned] |

### Testing

| Tool | Scope | Status |
|------|-------|--------|
| [Test Framework] | [Unit / Integration / E2E] | [Active / Deprecated] |
| [Mock Library] | [Test doubles] | [Active / Deprecated] |
| [Coverage Tool] | [Code coverage reporting] | [Active / Deprecated] |

---

## Version Policy

- **LTS releases** are preferred for runtime dependencies.
- Dependencies are **pinned to exact versions** (not ranges) in production.
- **Major version upgrades** require an ADR and thorough testing.
- **Deprecated technologies** should be migrated within two release cycles.

---

## Evaluation Criteria for New Technologies

1. **Community Health:** Active maintenance, responsive to issues, reasonable release
   cadence.
2. **License Compatibility:** Must be compatible with the project's license.
3. **Learning Curve:** Team should be able to reach productive use within one week.
4. **Interoperability:** Must integrate cleanly with existing stack.
5. **Performance:** Must meet the project's performance benchmarks (see
   quality-rules.md).
6. **Security Posture:** No known critical vulnerabilities. Active security
   disclosure process.

---

*Update this document when adopting or deprecating a technology.*
