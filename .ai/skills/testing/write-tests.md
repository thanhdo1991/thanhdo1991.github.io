---
id: write-tests
version: 2.1.0
confidence: 0.95
success_rate: 0.90
last_updated: 2026-06-29
tags:
  - testing
  - tdd
  - rigid
---

# Write Tests

> Rigid skill. TDD-first approach: RED -> GREEN -> REFACTOR. Tests are specification, not documentation. No production code without a failing test first.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "I'll write tests after the code works" | Tests written after code validate what the code does, not what it should do. They document bugs as features. |
| "This is too simple to test" | Simple code has simple tests. If it's too simple to test, it's too simple to break, so it costs nothing to test. |
| "Test after = documentation, test first = specification" | Tests written first define the contract. Tests written last only record the implementation. |
| "We don't have time to write tests" | Untested code takes 2-5x longer to debug in production. You don't have time NOT to write tests. |
| "The test just tests the mock, not the real thing" | You're mocking too deep. Test at the right abstraction level. |

## The TDD Cycle

### RED (Write a Failing Test)
1. Understand the requirement as a specific behavior.
2. Write the simplest test that expresses that behavior.
3. The test should fail for the right reason: the feature doesn't exist yet.
4. Run only the new test to confirm it fails.

### GREEN (Make It Pass)
1. Write the minimal code to make the test pass.
2. Do not write code that is not tested. If the test doesn't force you to write that line, don't write it.
3. Use the simplest implementation that works: return a constant first, then generalize.

### REFACTOR (Clean Up)
1. Remove duplication between test and production code.
2. Improve names: test names should read as sentences describing expected behavior.
3. Extract setup logic into fixtures or factories.
4. Run the full suite to confirm nothing broke.

## Test Structure Rules

- One behavior per test. A test should have one arrange, one act, one assert.
- Test names follow the pattern: `[method]_[scenario]_[expected_result]` or a full sentence.
- Arrange comments for complex setup, Act comments for the trigger, Assert comments only if the assertion is non-obvious.
- Use factories or builders over raw constructors. Tests should not break when constructors change.

## Red Flags (STOP Signals)

- A test file with no assertions or only one assertion for the entire file.
- Tests that share mutable state (test order dependency).
- Tests that rely on external services without mocking or contract testing.
- `sleep()` calls in tests. Use polling with timeouts or dependency injection instead.
- Tests that pass without asserting anything. Every test must have at least one explicit assertion.

## No Exceptions

- Do not write production code without a failing test first. No exceptions.
- Do not skip the RED phase. Writing a passing test first means the test might not test anything.
- Do not commit untested code. If a feature cannot be tested, it must be refactored until it can.
- Do not use `skip` or `only` on tests that stay in the codebase longer than one session.
