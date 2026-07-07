---
id: preferences
version: 1.0.0
confidence: 0.90
success_rate: 0.83
last_updated: 2026-06-29
tags:
  - preferences
  - workflow
  - template
---

# User Preferences

## Purpose

This document records individual and team preferences for development workflows,
tools, and communication. Preferences are not rules — they guide how the team works
efficiently together while respecting individual differences.

---

## How to Use This Template

Replace bracketed placeholders with your team's actual preferences. For team
preferences, reach consensus. For individual preferences, prefix with the person's
name or handle.

---

## Editor & IDE Preferences

| Setting | Preference | Notes |
|---------|------------|-------|
| Primary Editor | [e.g., VS Code / IntelliJ / Vim / Neovim / Emacs] | Shared configuration in repo |
| Code Formatter | [e.g., Prettier / black / gofmt / rustfmt] | On-save formatting preferred |
| Key Mappings | [e.g., VS Code default / Vim / Emacs] | |
| Theme | [e.g., Dark / Light / Custom] | |
| Font | [e.g., Fira Code / JetBrains Mono / Source Code Pro] | With ligatures: [Yes / No] |
| Extensions | [List essential extensions] | |
| Editor Config | [Path to shared config files] | |

## Testing Preferences

| Aspect | Preference |
|--------|------------|
| Test Framework | [e.g., Vitest / Jest / PyTest / JUnit / RSpec] |
| Test Runner | [e.g., CLI / IDE integration / Watch mode] |
| Assertion Style | [e.g., should / expect / assert] |
| Mock Library | [e.g., Mockito / unittest.mock / sinon / Moq] |
| Test Naming Convention | [e.g., describe/it / test_* / camelCase] |
| Prefer | [Unit tests > Integration tests > E2E tests] |
| Coverage Tool | [e.g., c8 / Istanbul / Coverage.py / JaCoCo] |
| Minimum Coverage | [Percentage before merge] |

## Commit & Version Control

| Aspect | Preference |
|--------|------------|
| Commit Style | [e.g., Conventional Commits / Gitmoji / Free form] |
| Branch Naming | [e.g., feature/description, fix/issue-number] |
| Branch Strategy | [e.g., GitHub Flow / Git Flow / Trunk-Based] |
| Commit Granularity | [e.g., One commit per logical change / Squash merge] |
| PR Title Format | [e.g., "type(scope): description"] |
| PR Size Limit | [e.g., 400 lines changed max] |
| Sign-off Required | [Yes / No] |

## Communication Preferences

| Channel | Preference | Response Time Expectation |
|---------|------------|--------------------------|
| Code Reviews | [Inline PR comments / Pair review] | Within 24 hours |
| Urgent Issues | [Slack / Teams / PagerDuty] | Within 30 minutes |
| Questions | [Slack / Discord / GitHub Discussions] | Within 4 hours |
| Meetings | [Async-first / Sync standups] | |
| Documentation | [In-code / Wiki / ADRs] | |

## Workflow Preferences

| Aspect | Preference |
|--------|------------|
| Development Method | [Agile / Scrum / Kanban / Waterfall] |
| Sprint Length | [e.g., 1 week / 2 weeks / None] |
| Standup Time | [e.g., 10:00 AM daily / Async via Slack] |
| Retrospective Cadence | [e.g., End of every sprint / Monthly] |
| Pair Programming | [Encouraged / Optional / Not used] |
| Work Hours | [Core hours: 10AM-3PM / Flexible] |

## Build & CI Preferences

| Aspect | Preference |
|--------|------------|
| Build System | [e.g., Webpack / Vite / Gradle / Maven / Make] |
| CI Provider | [e.g., GitHub Actions / GitLab CI / Jenkins / CircleCI] |
| CI Speed Target | [e.g., Full pipeline < 10 minutes] |
| Pre-commit Hooks | [e.g., lint, format, type-check, test affected] |
| Release Cadence | [e.g., Weekly / Bi-weekly / Continuous] |

---

*Preferences can change. Update this document when the team agrees on a new workflow
or tool. Individual preferences are annotated with names.*
