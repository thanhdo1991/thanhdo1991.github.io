---
id: team-roles
version: 1.0.0
confidence: 0.95
success_rate: 0.85
last_updated: 2026-06-29
tags:
  - team
  - roles
  - process
  - template
---

# Team Roles & Responsibilities

## Purpose

Clearly defined roles reduce ambiguity, prevent duplication of effort, and ensure
every critical responsibility has an owner. This document describes each role on
the team, its primary responsibilities, and who currently fills it.

---

## Current Team

| Role | Person | Backup | Since |
|------|--------|--------|-------|
| [Role] | @name | @name | YYYY-MM-DD |
| [Role] | @name | @name | YYYY-MM-DD |

---

## Role Descriptions

### Developer / Engineer

- **Primary:** Write production code that meets the team's quality standards.
- **Secondary:** Write tests, review teammates' code, contribute to technical
  discussions, maintain documentation for code they own.
- **Accountable for:** Correctness, test coverage, code quality, performance of
  assigned work.
- **Decision scope:** Implementation details within accepted architecture.

### Senior / Lead Developer

- **Primary:** Guide technical direction, make architectural decisions, mentor
  developers.
- **Secondary:** Design reviews, code reviews, sprint planning input, cross-team
  coordination.
- **Accountable for:** Overall code quality, architecture integrity, technical debt
  management.
- **Decision scope:** Architecture, technology choices, coding standards, trade-offs.

### Tech Lead / Architect

- **Primary:** Own the technical vision and roadmap. Ensure the architecture supports
  current and future requirements.
- **Secondary:** Evaluate technologies, define patterns, conduct architecture reviews,
  document ADRs.
- **Accountable for:** Architectural fitness, scalability, security posture, platform
  stability.
- **Decision scope:** System architecture, technology stack, cross-cutting concerns,
  final escalation for technical disputes.

### Reviewer

- **Primary:** Validate that changes meet quality, security, and architecture standards
  before merging.
- **Secondary:** Share knowledge through review comments, identify systemic issues,
  mentor through feedback.
- **Accountable for:** Catching defects, verifying test coverage, enforcing standards.
- **Decision scope:** Approve or request changes on pull requests within their
  expertise area.

### QA / Test Engineer

- **Primary:** Design and execute test strategies beyond unit tests — integration,
  e2e, performance, and exploratory testing.
- **Secondary:** Maintain test infrastructure, report bugs with clear reproduction
  steps, advocate for testability in design.
- **Accountable for:** Overall product quality, test environment health, regression
  detection.
- **Decision scope:** Testing priorities, test automation strategy, quality gates.

### DevOps / Platform Engineer

- **Primary:** Build and maintain CI/CD pipelines, infrastructure, monitoring, and
  deployment automation.
- **Secondary:** Incident response, capacity planning, cost optimization, security
  hardening.
- **Accountable for:** Deployment reliability, infrastructure uptime, build speed,
  incident response.
- **Decision scope:** Infrastructure, CI/CD tooling, observability, deployment
  strategy.

### Product Manager / Owner

- **Primary:** Define and prioritize features based on business value and user needs.
- **Secondary:** Maintain backlog, write user stories, accept completed work, gather
  stakeholder feedback.
- **Accountable for:** Product roadmap, priority decisions, stakeholder communication.
- **Decision scope:** What to build and when. Not how to build it.

### Scrum Master / Project Manager

- **Primary:** Facilitate ceremonies, remove blockers, protect team from external
  interruptions.
- **Secondary:** Track progress, improve team processes, ensure communication flows.
- **Accountable for:** Process efficiency, team health, impediment removal.
- **Decision scope:** Process, ceremonies, metrics.

---

## RACI Matrix (Responsible, Accountable, Consulted, Informed)

| Activity | Dev | Lead | QA | DevOps | PM |
|----------|-----|------|----|--------|----|
| Feature Implementation | R | A | C | I | C |
| Code Review | R | A | I | - | - |
| Architecture Decision | C | R/A | C | C | I |
| Test Strategy | C | A | R | I | - |
| Deployment | I | C | I | R/A | I |
| Incident Response | C | C | I | R/A | I |
| Backlog Prioritization | I | C | I | I | R/A |
| Release Decision | I | C | C | I | R/A |

**R** = Responsible (does the work), **A** = Accountable (owns the outcome),
**C** = Consulted (gives input), **I** = Informed (receives updates).

---

## On-Call & Escalation

| Tier | Role | Response Time | Coverage |
|------|------|---------------|----------|
| Tier 1 | DevOps / Platform Engineer | < 5 minutes | Business hours |
| Tier 2 | Senior Developer | < 15 minutes | Business hours |
| Tier 3 | Tech Lead / Architect | < 30 minutes | As needed |
| Escalation | Engineering Manager | < 1 hour | As needed |

---

*Roles should adapt as the team grows. Review this document quarterly and update as
needed.*
