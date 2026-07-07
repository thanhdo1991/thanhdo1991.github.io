---
id: review-check-v1
version: 1.0.0
confidence: 0.92
success_rate: 0.88
last_updated: 2026-06-29
tags:
  - prompt
  - review
  - checklist
  - quality
  - qa
  - verification
---

Perform a comprehensive self-review on the following work:

## Work Item
- Description: {{work_description}}
- Files changed: {{files_changed}}
- Type (feature/bugfix/refactor/docs): {{work_type}}

## Review Checklist

### Value
- [ ] Does the implementation match the requirements/specification?
- [ ] Are all acceptance criteria met?
- [ ] Is there any scope creep or unnecessary functionality?

### Correctness
- [ ] Does the logic handle all specified inputs correctly?
- [ ] Are error conditions properly handled?
- [ ] Are there any race conditions or timing issues?
- [ ] Is state management consistent and correct?

### Edge Cases
- [ ] Empty/null/zero inputs handled?
- [ ] Boundary values tested?
- [ ] Resource exhaustion scenarios considered?
- [ ] Network/IO failures handled gracefully?
- [ ] Concurrent access considered?

### Security
- [ ] Input validation and sanitization in place?
- [ ] Injection vulnerabilities (XSS, SQLi, command injection) addressed?
- [ ] Authentication/authorization checks correct?
- [ ] Sensitive data (secrets, PII) not exposed in logs/output?
- [ ] Dependencies checked for known vulnerabilities?

### Performance
- [ ] Time complexity appropriate for expected data volumes?
- [ ] Memory usage reviewed for leaks or excessive allocation?
- [ ] Database queries optimized (N+1, missing indexes)?
- [ ] Caching opportunities identified?
- [ ] Resource cleanup guaranteed (closeable objects, transactions)?

### Maintainability
- [ ] Code follows project style and conventions?
- [ ] Functions/methods have single responsibility?
- [ ] Naming is clear and descriptive?
- [ ] Comments explain why, not what?
- [ ] Documentation updated (README, API docs, inline docs)?
- [ ] No dead code, commented-out code, or TODOs left unresolved?

### Test Coverage
- [ ] Unit tests cover core logic including edge cases?
- [ ] Integration tests cover key interaction points?
- [ ] Tests are deterministic and isolated?
- [ ] Test coverage for bug fixes (regression tests)?
- [ ] Performance tests for critical paths?

### Logging and Observability
- [ ] Appropriate logging levels used (error/warn/info/debug)?
- [ ] Log messages include sufficient context for debugging?
- [ ] Metrics/tracing added for critical operations?
- [ ] No sensitive data in log messages?

## Overall Assessment
- Issues found: {{issues_found}}
- Severity (critical/major/minor/none): {{severity}}
- Recommendation: {{recommendation}}
