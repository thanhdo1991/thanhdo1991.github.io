---
id: run-tests
version: 2.0.0
confidence: 0.85
success_rate: 0.80
last_updated: 2026-06-29
tags:
  - testing
  - execution
  - flexible
---

# Run Tests

> Flexible skill. Run tests, interpret results, diagnose failures, and maintain a healthy test suite. Adapt the approach to the project's test pyramid and toolchain.

## Overview

Running tests is not simply executing a command and checking green. This skill covers selecting the right test scope, interpreting results accurately, diagnosing flaky or failed tests, and maintaining the health of the suite over time.

**Core Principle**: A test run is only useful if you trust its results. A flaky suite erodes trust faster than no tests at all.

## Step-by-Step Process

### Phase 1: Select Scope
1. Determine what to run: unit only, integration only, full suite, or affected tests only.
2. For CI: run the full suite. For development: start with affected tests, run full before commit.
3. Configure parallelization: split by file, by shard, or by test suite. Monitor for interference.

### Phase 2: Execute
1. Use the project's test runner with consistent flags (no silent failures, show full stack traces).
2. Set a timeout per test and per suite. Hanging tests block progress.
3. Collect output: pass/fail counts, coverage reports, failure stack traces, performance data.

### Phase 3: Interpret Results
1. Green: confirm coverage thresholds are met. Review warnings.
2. Red: identify the failing test(s). Determine if the failure is:
   - **Legitimate**: the code change introduced a regression.
   - **Flaky**: the test fails intermittently without code changes.
   - **Environmental**: CI infrastructure issue, port conflict, disk full.
   - **Pre-existing**: the test was already failing before your changes.

### Phase 4: Debug Failures
1. Reproduce the failure locally with the same test and seed.
2. Read the full stack trace. The cause is often 2-3 frames below the assertion line.
3. For flaky tests: isolate the shared state, timing dependency, or test order sensitivity.
4. For legitimate failures: follow the debug skill.

## Common Mistakes

- **Running tests in CI only**: Run tests locally before commit. CI feedback cycle is 5-30 minutes; local is 5-30 seconds.
- **Ignoring warnings**: A warning today is a failure tomorrow. Treat warnings as errors in CI.
- **Using `skip` to make CI pass**: Skipping tests hides regressions. File a ticket and set a deadline to fix.
- **Not snapshotting failures**: When a test fails, capture the inputs, expected output, and actual output before making changes.
- **Over-relying on coverage percentages**: 100% coverage with trivial tests is worse than 70% coverage with meaningful tests.

## Quality Gates

- [ ] Full test suite passes locally before push.
- [ ] No tests skipped without a linked ticket.
- [ ] Coverage meets project minimum (or no decrease from baseline).
- [ ] Flaky tests are quarantined and assigned an owner.
- [ ] CI test run completes under the team's threshold (typically < 10 minutes).
