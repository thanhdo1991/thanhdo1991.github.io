---
id: changelog-management
version: 2.0.0
confidence: 0.85
success_rate: 0.80
last_updated: 2026-06-29
tags:
  - process
  - changelog
  - release
  - rigid
---

# Changelog Management

> Rigid skill. Maintain a changelog following the Keep a Changelog format. Every release must be documented with the correct type (Added, Changed, Fixed, Removed) and linked to relevant issues.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "The git log is our changelog" | Git logs contain WIP commits, merge messages, and rebase artifacts. They are not user-facing. |
| "We'll write the changelog at release time" | Writing at release time means important changes are forgotten. Write as you go. |
| "Changelogs are for open source projects" | Every project benefits from a changelog: onboarding, debugging, release planning. |
| "No one reads changelogs anyway" | Developers, operations, QA, and product managers all read changelogs. |

## Process

### Phase 1: Follow Keep a Changelog Format
1. The changelog file is named `CHANGELOG.md` in the repository root.
2. Use the format: version number, release date, categorized sections.

### Phase 2: Categorize Every Change
- **Added**: New features, new endpoints, new configuration options.
- **Changed**: Changes to existing functionality, performance improvements, dependency updates.
- **Deprecated**: Features that will be removed in the future. Includes migration path.
- **Removed**: Features that were removed. Includes breaking change notice.
- **Fixed**: Bug fixes. Reference the issue or ticket number.
- **Security**: Vulnerability fixes. Reference the CVE or advisory.

### Phase 3: Write Entries as You Go
1. Update the `[Unreleased]` section with every PR or significant commit.
2. Each entry starts with a verb in past tense: Added, Fixed, Changed.
3. Reference the issue or PR number.
4. Write for the reader: what do they need to know about this change?

### Phase 4: Release Preparation
1. Before a release, move `[Unreleased]` entries to a new version section.
2. Add the release date and version number.
3. Review for completeness: every PR merged should have a changelog entry.
4. Flag breaking changes with a "BREAKING" prefix.

### Phase 5: Maintain Consistency
1. Use a changelog linter or CI check to enforce format compliance.
2. Include changelog review in the PR review checklist.

## Red Flags (STOP Signals)

- No changelog file exists in the repository.
- Changelog not updated alongside code changes.
- Unreleased section is empty when commits have been made.
- No issue or PR references in changelog entries.
- Breaking changes not explicitly marked.

## No Exceptions

- Do not release without updating the changelog.
- Do not write vague changelog entries: "Fixed bugs" is not acceptable.
- Do not skip the Unreleased section. Every PR must add an Unreleased entry.
- Do not remove or retroactively edit published changelog entries.
