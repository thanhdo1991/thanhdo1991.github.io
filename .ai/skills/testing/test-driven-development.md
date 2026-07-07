---
id: test-driven-development
version: 2.1.0
confidence: 0.95
success_rate: 0.88
last_updated: 2026-06-29
tags:
  - testing
  - tdd
  - rigid
---

# Test-Driven Development

> Rigid skill. Full TDD discipline: no production code without a failing test. The RED-GREEN-REFACTOR cycle is non-negotiable.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "This is too simple to test" | If it's simple, the test is simple. Write a one-line assertion. |
| "I'll test after the feature is done" | "Test after" means "test the happy path and call it done." Edge cases are forgotten. |
| "The test would be too complex to write first" | The test complexity reveals design complexity. If the test is hard to write, the design needs improvement. |
| "TDD slows me down" | TDD adds 10-15% to initial development. It saves 30-50% in debugging. Net positive by day 2. |
| "I'll test later, I promise" | "Later" never comes. Code moves to production, then to "don't touch, it works." |

## The TDD Cycle

### RED Phase
1. Write a test for the next behavior you want to implement.
2. The test must fail for the expected reason (test subject not found, method missing, wrong result).
3. Do not proceed until you see the test fail. A test that passes without implementation may be invalid.
4. Write only enough test to force the next production code.

### GREEN Phase
1. Write the minimal production code to make the test pass.
2. Duplication and ugliness are permitted. The goal is a passing test, not elegant code.
3. Do not add functionality that is not covered by a test.
4. Run the full suite. All tests pass.

### REFACTOR Phase
1. Remove duplication. Apply design patterns. Improve names.
2. Tests provide the safety net. If a refactoring breaks a test, you caught it early.
3. Run the full suite after each refactoring step.
4. Return to RED for the next behavior.

## Test Design Principles

- **FIRST**: Fast, Isolated, Repeatable, Self-validating, Timely.
- **Arrange-Act-Assert**: Structure every test in three clear sections.
- **One concept per test**: If a test has multiple assertions, it tests multiple behaviors.
- **Tests as documentation**: A new team member should understand the system by reading tests.

## Red Flags (STOP Signals)

- "This is too simple to test" or "This doesn't need a test."
- Skipping the RED phase and writing code first.
- A commit with production code but no test changes.
- Tests that share state or depend on a specific execution order.
- Tests that require external services running locally (database, cache, API).

## No Exceptions

- No production code without a failing test first. Period.
- No skipping the RED phase. Every cycle starts with a failing test.
- No committing a test that can pass without the corresponding production code.
- No committing production code that doesn't have a test. Untested code is technical debt with interest.
