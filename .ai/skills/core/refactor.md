---
id: refactor
version: 2.0.0
confidence: 0.85
success_rate: 0.82
last_updated: 2026-06-29
tags:
  - core
  - refactoring
  - flexible
---

# Refactor

> Flexible skill. Safe, incremental refactoring that changes structure without changing behavior. Each step must be verifiable and reversible.

## Overview

Refactoring is the disciplined technique of restructuring existing code without altering its external behavior. The goal is to improve readability, maintainability, and performance characteristics while keeping the system running at all times.

**Core Principle**: Change structure without changing behavior. If behavior changes, it's not refactoring; it's rewriting.

## Step-by-Step Process

### Phase 1: Analyze Dependencies
1. Map the dependencies of the code to be refactored: what depends on it, and what does it depend on?
2. Identify the public contract: which functions, classes, or modules are used externally?
3. Check for implicit dependencies: shared mutable state, global variables, import-time side effects.
4. Document the current contract. This is your behavior baseline.

### Phase 2: Establish Test Coverage
1. Ensure the code under refactoring has adequate test coverage. Minimum: every public function has a test.
2. If coverage is insufficient, write characterization tests first: tests that capture the current behavior (even if buggy).
3. Run the tests. Confirm they pass on the current code.

### Phase 3: Small Steps
1. Identify the smallest possible change that moves toward the target structure.
2. Make the change.
3. Run the tests. If red, revert or fix.

### Phase 4: Verify After Each Step
1. Run lint and type checking.
2. Run the full test suite.
3. Run the application and smoke-test the affected area.
4. Commit the small step before proceeding to the next.

### Phase 5: Clean Up
1. Remove dead code, unused imports, and obsolete comments.
2. Rename variables and functions to match the new structure.
3. Update any external documentation or API specs affected by the refactoring.

## Common Mistakes

- **Refactoring and fixing bugs in the same change**: Each change should do one thing. Mixing refactoring with behavior changes makes both untestable and unreviewable.
- **Big bang refactoring**: Large refactors touch thousands of lines, break for days, and often get abandoned. The only safe refactor is one you can undo in one revert.
- **Refactoring without tests**: Without a test harness, you cannot distinguish between "it works" and "it passes the one case I manually tested."
- **Premature refactoring**: Code that works and is never touched again doesn't need refactoring. Focus on code that changes frequently.
- **Changing public APIs without deprecation**: Internal refactoring should not break callers. Deprecate before removing.

## Quality Gates

- [ ] Test coverage >= 80% on the refactored code (or characterization tests written).
- [ ] Each step committed independently with a clear message.
- [ ] Zero test regressions after the full sequence.
- [ ] No behavior changes introduced (verified by test suite).
- [ ] Dead code and unused imports removed.
