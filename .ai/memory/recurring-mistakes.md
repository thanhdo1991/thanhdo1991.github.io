---
id: recurring-mistakes
version: 1.0.0
confidence: 0.90
success_rate: 0.85
last_updated: 2026-06-29
tags:
  - mistakes
  - learning
  - anti-patterns
  - template
---

# Recurring Mistakes

## Purpose

A living catalog of mistakes that have recurred in the project. Documenting the root
cause, symptoms, and prevention strategy helps the entire team avoid repeating them.

---

## How to Use This Document

When you catch a bug during review, or when an incident post-mortem identifies a
preventable mistake, add it here. Tag each entry with the relevant category so we can
spot patterns over time.

---

## Categories

### Logic & Correctness

| Mistake | Root Cause | Prevention | Status |
|---------|------------|------------|--------|
| Off-by-one errors in loop boundaries | Rushing edge-case analysis | Use inclusive/exclusive notation in comments; write boundary tests first | Active |
| Incorrect null/undefined handling | Assuming a value is always present | Use strict type checking; enforce optional/Maybe patterns | Active |
| Swapping parameters in function calls | Similar parameter types | Use named arguments / parameter objects for 3+ params | Active |
| [Add your own] | | | |

### Performance

| Mistake | Root Cause | Prevention | Status |
|---------|------------|------------|--------|
| N+1 queries in ORM code | Lazy loading without awareness | Audit all loops that access relations; eager-load explicitly | Active |
| Missing pagination on list endpoints | Assuming small datasets | Default every list endpoint to paginated | Active |
| Inefficient loop nesting | Not considering algorithmic complexity | Discuss algorithmic approach in review for loops over large data | Active |
| Unbounded memory growth | Accumulating data without cleanup | Profile memory usage in staging before release | Active |
| [Add your own] | | | |

### Security

| Mistake | Root Cause | Prevention | Status |
|---------|------------|------------|--------|
| Logging sensitive data | Debugging with full-context logging | Mandatory log review before merge; automated PII scanner | Active |
| Insufficient input validation | Trusting internal service calls | Validate at every system boundary regardless of caller | Active |
| Hardcoded secrets in config files | Convenience during development | Pre-commit hook scans for secrets; gitleaks/trufflehog in CI | Active |
| Permissive CORS settings | Debugging from multiple origins | Set strict CORS policy in production; environment-specific config | Active |
| [Add your own] | | | |

### Testing

| Mistake | Root Cause | Prevention | Status |
|---------|------------|------------|--------|
| Testing implementation, not behavior | Tying tests to internal structure | Test through public interfaces; avoid mocking internals | Active |
| Flaky tests due to shared state | Tests modifying shared fixtures | Use fresh fixtures per test; parallel test isolation | Active |
| Missing edge case tests | Happy-path-only thinking | Write test cases for empty, null, max, and error conditions first | Active |
| [Add your own] | | | |

### Process & Communication

| Mistake | Root Cause | Prevention | Status |
|---------|------------|------------|--------|
| Merging without review | Pressure to ship quickly | Branch protection rules; mandatory CI checks | Active |
| Scope creep in pull requests | Combining unrelated changes | One logical change per PR; split large PRs | Active |
| Undocumented design decisions | Verbal agreements not recorded | "If it wasn't recorded, it didn't happen" — use ADRs | Active |
| [Add your own] | | | |

---

## How to Add a New Entry

```
### [Mistake Name]

- **Category:** [Logic / Performance / Security / Testing / Process]
- **Date first observed:** YYYY-MM-DD
- **Symptoms:** [How does this manifest?]
- **Root cause:** [What led to the mistake?]
- **Impact:** [What was the cost? Time lost, bugs shipped, etc.]
- **Prevention strategy:** [Process, tool, or practice change]
- **Status:** [Active / Mitigated / Resolved]
- **Related incidents:** [Links to PRs, issues, or post-mortems]
```

---

*Review this document quarterly to identify top patterns and prioritize systemic fixes.*
