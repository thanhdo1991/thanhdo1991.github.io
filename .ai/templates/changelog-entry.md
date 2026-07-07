---
id: template-changelog-entry
version: 1.0.0
confidence: 0.95
success_rate: 0.96
last_updated: 2026-06-29
tags: [template, changelog, versioning]
---

# Changelog Entry Template

Follows [Keep a Changelog](https://keepachangelog.com/) convention with Semantic Versioning.

## Version Format

`[MAJOR].[MINOR].[PATCH]` — YYYY-MM-DD

- **MAJOR:** Breaking change (incompatible API/schema change)
- **MINOR:** Backward-compatible new functionality
- **PATCH:** Backward-compatible bug fix

## Entry Structure

```markdown
## [X.Y.Z] — YYYY-MM-DD

### Added
- [New feature or capability] ([#issue])
- [Another new feature]

### Changed
- [Change in existing behavior] ([#issue])
- [Performance improvement or refactor]

### Deprecated
- [Feature to be removed in future] ([#issue])

### Removed
- [Feature removed] ([#issue])

### Fixed
- [Bug fix] ([#issue])

### Security
- [Vulnerability fix] ([#issue])
```

## Category Guidelines

| Category | When to Use |
|----------|-------------|
| Added | New features, files, capabilities |
| Changed | Modifications to existing functionality |
| Deprecated | Features marked for future removal |
| Removed | Features removed in this version |
| Fixed | Bug fixes, error corrections |
| Security | Vulnerability patches, hardening |

## Example

```markdown
## [1.2.0] — 2026-06-15

### Added
- Reflection skill for post-task analysis
- Failure analysis template

### Changed
- Increased embedding chunk size from 512 to 1024 tokens

### Fixed
- Frontmatter validation regex for multi-word tags
```
