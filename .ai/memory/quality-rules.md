---
id: quality-rules
version: 1.0.0
confidence: 0.95
success_rate: 0.87
last_updated: 2026-06-29
tags:
  - quality
  - testing
  - code-review
  - template
---

# Quality Rules

## Purpose

Define objective, measurable quality standards for the project. These rules are
enforced through automated checks and code review. Meeting these standards is a
prerequisite for merging any change.

---

## Test Coverage

| Criterion | Minimum | Stretch Target | Notes |
|-----------|---------|----------------|-------|
| Line Coverage | 80% | 90% | Measured per module, not aggregate |
| Branch Coverage | 70% | 85% | Every branch in conditionals exercised |
| Critical Path Coverage | 100% | 100% | Auth, payments, data integrity paths |
| Public API Coverage | 90% | 100% | All public functions have at least one test |

- Coverage below the minimum **blocks the merge**.
- Exemptions must be documented with a comment and approved in code review.
- Focus on meaningful coverage — testing the right things matters more than hitting
  a percentage.

## Test Quality

- **No flaky tests.** A test that fails intermittently must be fixed or quarantined
  within 48 hours.
- **Tests must be deterministic.** No reliance on wall clock, random data without a
  seed, or external services without a controlled mock.
- **Test readability** matters as much as production code. Use descriptive test
  names structured as: `[UnitOfWork_StateUnderTest_ExpectedBehavior]`.
- **One assertion per test concept.** It is acceptable to have multiple assertions
  in a single test as long as they all verify the same logical outcome.

## Code Review Standards

### Required Before Merge

- All tests pass (CI green).
- No new warnings (linter, compiler, type checker).
- Coverage meets the above thresholds.
- At least one reviewer has approved.
- No unresolved review threads.

### Review Checklist

Reviewers should verify:
1. **Correctness:** Does the code do what it claims? Are edge cases handled?
2. **Design:** Does it fit the architecture? Is it consistent with patterns in use?
3. **Readability:** Can another team member understand it without an explanation?
4. **Security:** Are inputs validated? Are secrets handled properly? Are there
   injection vectors?
5. **Performance:** Are there obvious inefficiencies? N+1 queries? Unnecessary
   allocations?
6. **Test Coverage:** Are new features tested? Are changes adequately tested?

## Performance Benchmarks

| Operation | P50 Target | P95 Target | Measurement Method |
|-----------|------------|------------|--------------------|
| API Response (simple) | < 50ms | < 200ms | Load test with 100 req/s |
| API Response (complex) | < 200ms | < 500ms | Load test with 50 req/s |
| Database Query (indexed) | < 10ms | < 50ms | Profiling in staging |
| Database Query (complex) | < 100ms | < 300ms | Profiling in staging |
| Page Load (server-rendered) | < 500ms | < 2s | Browser timing API |
| Batch Job (1k records) | < 5s | < 15s | CI benchmark job |

Regressions of more than 20% require investigation before merge.

## Security Rules

- **No secrets in code.** API keys, passwords, and tokens must use environment
  variables or a secrets manager.
- **Input validation** on every external boundary. Use allowlists, not blocklists.
- **Dependency scanning** runs in CI. Critical or high-severity vulnerabilities
  block the build.
- **Authentication** is required for every endpoint that handles user data.
- **Rate limiting** must be applied to all public endpoints.
- **Logging** must never include PII, passwords, tokens, or other sensitive data.

## Static Analysis

| Check | Tool | Enforced In |
|-------|------|-------------|
| Linting | [linter name] | Pre-commit + CI |
| Type Checking | [type checker] | CI |
| Security Scan | [SAST tool] | CI |
| Dependency Audit | [audit tool] | CI (daily) |
| Complexity | [complexity tool] | CI (warning only) |

---

*Update this document as quality standards evolve. All changes require team consensus.*
