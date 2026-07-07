---
id: conventions
version: 1.0.0
confidence: 0.95
success_rate: 0.92
last_updated: 2026-06-29
tags:
  - conventions
  - template
  - coding-standards
---

# Coding Conventions

## Purpose

Consistent conventions reduce cognitive load during code review, make the codebase
predictable, and help new contributors ramp up faster. These conventions apply to all
code in the project unless explicitly overridden by a language-specific style guide.

---

## Naming Conventions

| Element | Convention | Example | Notes |
|---------|------------|---------|-------|
| Files & Directories | kebab-case | `user-service.ts` | Use plural for directories: `services/` |
| Classes / Types | PascalCase | `UserService`, `OrderStatus` | Nouns or noun phrases |
| Functions / Methods | camelCase | `getUserById()`, `formatDate()` | Verbs or verb phrases |
| Variables | camelCase | `userList`, `isActive` | Meaningful, not abbreviated |
| Constants | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT` | Only for true compile-time constants |
| Private Members | underscore prefix | `_internalValue` | Optional, language-dependent |
| Interfaces | Prefix `I` or no prefix | `UserRepository` | Be consistent across the project |
| Booleans | Prefix with `is`, `has`, `can` | `isEnabled`, `hasPermission` | Improves readability in conditionals |

## File Organization

```
[module]/
  __init__.py          — Public API exports (if applicable)
  [entity].py          — Domain entities / models
  [entity].service.py  — Business logic
  [entity].repository.py — Data access
  [entity].controller.py — API / presentation
  [entity].test.py     — Tests (co-located or in tests/ directory)
```

- **One primary concept per file.** A file should export one class, function, or
  module that is the reason the file exists. Group closely related helpers in the same
  file.
- **Maximum file length:** 500 lines. If a file grows beyond this, extract
  functionality into sub-modules.
- **Cohesion over convenience:** Group code by domain concept, not by technical layer.
  Put user-related code together rather than all controllers in one folder.

## Import Order

1. Standard library imports
2. Third-party library imports
3. Internal / project imports
4. Relative imports within module

Within each group, sort alphabetically. Separate groups with a blank line.

## Comments & Documentation

- **Public APIs** must have a docstring or JSDoc block describing purpose, parameters,
  return value, and exceptions.
- **Implementation comments** explain *why*, not *what* — the code should already
  express *what* clearly.
- **TODO comments** must include a ticket or issue reference: `// TODO(#123): ...`
- **No commented-out code.** Delete it. If you need it later, use version control.

## Error Handling

- Use explicit exception types — never catch a generic `Exception` unless rethrowing
  after logging.
- Validate inputs at the boundary of every public function. Fail fast with clear
  messages.
- Wrap external library calls in a thin adapter layer so library-specific exceptions
  don't leak into domain code.
- Log at the appropriate level: ERROR for unrecoverable failures, WARN for
  recoverable issues, INFO for lifecycle events, DEBUG for diagnostic detail.

## Code Structure

- Keep functions short — ideally under 20 lines, never over 50.
- A function should do one thing and do it well. If it has "and" in the name, split
  it.
- Prefer early returns over nested if-else chains.
- Limit nesting to 3 levels maximum. Extract inner blocks into named functions.
- Reduce cyclomatic complexity: avoid switch statements with many cases; use
  polymorphism or a lookup table instead.

---

*Conventions evolve. Propose changes via a pull request to this file and discuss with
the team before committing.*
