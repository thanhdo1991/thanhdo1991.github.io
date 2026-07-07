---
id: implement-feature
version: 2.1.0
confidence: 0.90
success_rate: 0.85
last_updated: 2026-06-29
tags:
  - core
  - implementation
  - flexible
  - tdd
---

# Implement Feature

> Flexible skill. Production-grade implementation flow using Test-Driven Development as the default approach. Adapt steps based on context but never skip the verification phase.

## Overview

This skill guides the end-to-end implementation of a feature: from understanding the requirement, through design and coding (with TDD), to verification. It balances rigor with practicality, allowing the developer to adjust the depth of testing and documentation to the feature's risk profile.

**Core Principle**: Write the test first. If you can't write the test, you don't understand the requirement well enough to write the code.

## Step-by-Step Process

### Phase 1: Understand and Design
1. Read the requirement and write a one-paragraph summary in your own words.
2. Identify the interface boundary: What inputs does this feature accept? What outputs does it produce? What side effects does it have?
3. Design the data flow as a simple ASCII diagram or list of transformations.
4. List edge cases: empty input, null values, boundary conditions, error states, concurrency.

### Phase 2: Test-First
1. Write the simplest failing test that describes the expected behavior.
2. Run it. Watch it fail (RED). Confirm the failure is for the expected reason.
3. Write the minimal code to pass the test (GREEN).
4. Refactor if needed (REFACTOR).
5. Repeat for the next behavior until the feature is complete.

### Phase 3: Integration
1. Wire the unit into the application (controller, route, component).
2. Write integration tests covering the happy path and at least two error paths.
3. Run the full test suite. All tests must pass.

### Phase 4: Verify
1. Run lint and type checking. Fix all issues.
2. Run the application and manually verify the feature works end-to-end.
3. Check error handling: What happens when the network fails? The database is down? The input is malicious?
4. Review the diff for accidental changes to unrelated code.

## Common Mistakes

- **Writing tests after code**: Tests written post-hoc validate what the code does, not what it should do. The test-first mind shift catches spec gaps early.
- **One giant test**: Tests should verify one behavior. A test named "test_feature" that asserts five things is five untestable scenarios.
- **Over-mocking**: Mock at the boundary, not internally. If you mock three layers deep, your test validates mocks, not reality.
- **Skipping edge cases**: Happy-path-only code breaks in production. Every conditional (if/switch/pattern match) needs a test for the branch you didn't take.
- **Gold-plating**: Building infrastructure the feature doesn't need. YAGNI applies to test infrastructure too.

## Quality Gates

- [ ] Every public function has at least one test (happy path + one error path).
- [ ] Test suite runs green with zero warnings.
- [ ] No TODO, FIXME, or debug logging in the diff.
- [ ] Feature works end-to-end in a dev run.
- [ ] Diff touches only files related to the feature (no incidental formatting changes).
