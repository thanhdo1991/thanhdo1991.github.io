---
id: integration-testing
version: 2.0.0
confidence: 0.80
success_rate: 0.75
last_updated: 2026-06-29
tags:
  - testing
  - integration
  - flexible
---

# Integration Testing

> Flexible skill. Plan, write, and maintain integration tests that validate your system's components work together. Cover boundaries, contracts, and data flow without duplicating unit tests.

## Overview

Integration tests verify that your application's components interact correctly. They sit between unit tests (fast, isolated) and end-to-end tests (slow, realistic). A well-designed integration test covers the boundaries between units: database queries, API calls, message queues, and file I/O.

**Core Principle**: Test the boundary, not the internal logic. Unit tests cover internal correctness; integration tests cover inter-component communication.

## Step-by-Step Process

### Phase 1: Identify Integration Points
1. List every boundary in the system: database, cache, message broker, external API, file system, environment variables.
2. Prioritize by risk: boundaries that change frequently, have complex contracts, or are maintained by different teams.
3. For each boundary, define the contract: expected inputs, outputs, error responses, and state changes.

### Phase 2: Choose Mocking Strategy
- **Real instance**: Use Testcontainers or Docker for databases, caches, queues. Best fidelity, slowest.
- **In-memory substitute**: SQLite for PostgreSQL, in-memory Redis, fake S3. Good balance of speed and realism.
- **Mocked at interface**: Mock the boundary interface. Fastest, but tests the mock, not the real integration.
- **Rule**: Use real instances for data-critical integrations (database, main API). Use mocks for external third-party APIs you don't control.

### Phase 3: Write Tests
1. Set up the real or substitute dependency.
2. Seed test data that represents realistic production scenarios.
3. Execute the operation that crosses the boundary.
4. Verify the state change on both sides of the boundary.
5. Clean up: reset or tear down the dependency state.

### Phase 4: Contract Testing
1. For each API or service dependency, define a contract test that verifies the provider meets the consumer's expectations.
2. Run contract tests in CI. A contract failure blocks deployment.
3. Use tools like Pact or Spring Cloud Contract for consumer-driven contracts.

## Common Mistakes

- **Duplicating unit tests**: Integration tests should not test the same logic as unit tests. They test connectivity, data format, and contract compliance.
- **Leaking state between tests**: Tests that depend on previous test's state are flaky. Reset data between each test.
- **Too slow to run regularly**: If integration tests take > 5 minutes, split them: fast ones run on every commit, slow ones run nightly.
- **No test for failure modes**: What happens when the database is unreachable? The cache is full? The API returns a 500? Every integration point should have a failure test.
- **Hardcoded connection strings**: Use environment variables or configuration files. No test should require manual setup.

## Quality Gates

- [ ] Every integration point has at least one happy-path test and one failure-mode test.
- [ ] Tests clean up all test data after execution (no cross-test contamination).
- [ ] Integration tests run automatically in CI.
- [ ] No external service dependency is required to run tests locally (use containers or mocks).
- [ ] Test data is realistic: similar volume, variation, and edge cases to production.
