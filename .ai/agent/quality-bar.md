---
id: agent-009
version: 1.0.0
confidence: 0.96
success_rate: 0.93
last_updated: 2026-06-29
tags:
  - quality
  - standards
  - verification
---

# quality-bar.md — Quality Standards & Acceptance Criteria

## Minimum Quality Bar

No output is considered complete until it meets all of the following criteria.

### 1. No Silent Failures

- Every operation that can fail must have explicit error handling.
- Errors must be surfaced to the user, not swallowed in catch-all handlers.
- Log output must distinguish between expected states, warnings, and errors.

### 2. All Assertions Verified

- Every assumption that affects correctness must be expressed as an assertion or test.
- Assertions must be executable and run as part of the verification step.
- Inferred assertions (e.g., "this value is never null") must be documented until a test covers them.

### 3. Tests Must Pass

- The full test suite must pass before any change is committed.
- When existing tests are broken before the change, that must be disclosed and not conflated with the change's impact.
- New functionality must include at minimum one positive test (expected path) and one negative test (error/edge case).

### 4. Code Reviewed Before Commit

- Every change must be self-reviewed against the task scope before commit.
- The review must check: correctness, security, edge cases, naming consistency, and documentation.
- Review findings must be resolved (fixed or explicitly deferred with reason) before the change is committed.

### 5. No Debug Artifacts

- No console.log, print, dump, or debugger statements in committed code.
- No commented-out code blocks.
- No placeholder values, hardcoded credentials, or TODO markers without an associated tracked issue.

### 6. Documentation Completeness

- Public API surfaces must have doc comments describing purpose, parameters, and return values.
- Architectural changes must be reflected in relevant ADRs or design documents.
- Configuration changes must be documented in the appropriate configuration guide or README.
