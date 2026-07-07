---
id: code-review-prompt-v1
version: 1.0.0
confidence: 0.91
success_rate: 0.86
last_updated: 2026-06-29
tags:
  - prompt
  - code-review
  - quality
  - best-practices
  - peer-review
---

Review the following code changes:

## Change Information
- Repository: {{repository}}
- Branch/PR: {{branch_or_pr}}
- Author: {{author}}
- Description: {{change_description}}
- Files changed: {{files_changed}}

## Diff to Review
```
{{diff_content}}
```

## Review Focus Areas

### Correctness
- [ ] Does the code correctly implement the intended behavior?
- [ ] Are all code paths covered (success, error, edge cases)?
- [ ] Are there any off-by-one, null pointer, or type errors?
- [ ] Is state management correct (immutability, transactions, locking)?

### Design and Architecture
- [ ] Does the change follow established patterns and conventions?
- [ ] Is the code appropriately abstracted and modular?
- [ ] Are there coupling or cohesion concerns?
- [ ] Does the change introduce unnecessary complexity?

### Style and Readability
- [ ] Follows project coding standards (linting, formatting)?
- [ ] Variable and function names are descriptive?
- [ ] Comments are meaningful and explain rationale?
- [ ] Is the code easy to follow and maintain?

### Security
- [ ] Input validation and output encoding in place?
- [ ] Proper authentication/authorization checks?
- [ ] No hardcoded secrets, tokens, or credentials?
- [ ] Safe handling of file I/O, network requests, and user data?

### Performance
- [ ] Loops and algorithms have reasonable complexity?
- [ ] Database queries are efficient (no N+1, proper indexing)?
- [ ] Memory usage is appropriate (no leaks, unnecessary allocation)?
- [ ] Caching used where beneficial?

### Testing
- [ ] Are there tests for the new code?
- [ ] Do tests cover positive and negative cases?
- [ ] Are tests deterministic and isolated?
- [ ] Is there a regression test if this is a bug fix?

## Feedback Summary

### Critical (must fix)
{{critical_issues}}

### Major (should fix)
{{major_issues}}

### Minor (consider)
{{minor_issues}}

### Praise
{{praise_items}}

## Overall Verdict
- {{verdict}} (Approve / Request Changes / Comment)
- {{summary_comment}}
