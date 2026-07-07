---
id: workflow-refactoring-001
version: 1.0.0
confidence: 0.84
success_rate: 0.79
last_updated: 2026-06-29
tags: [workflow, refactoring, quality]
---

# Refactoring Workflow

Safe, incremental process for improving code structure without changing external behavior.

## Flowchart

```
[Refactoring Need Identified] → [Analyze Code: Understand Current Structure]
    → [Identify Smells] → [Plan Target Structure]
    → [Ensure Test Coverage] → [Coverage Adequate?] → [No] → [Write Characterization Tests]
    → [Yes] → [Refactor: One Change at a Time]
    → [Run Tests] → [Pass?] → [No] → [Revert Last Change] → [Try Different Approach]
    → [Yes] → [More Refactors?] → [Yes] → [Next Atomic Refactor]
    → [No] → [Final Verification] → [Commit]
    → [Done]
```

## Trigger

- Code complexity makes future changes difficult.
- Repeated patterns of bugs in a module (smell concentration).
- Duplicate code identified during reviews.
- Architectural drift from the intended design.
- Performance analysis reveals structural bottlenecks.
- Preparing a module for a new feature (make the change easy, then make the easy change).

## Steps

### 1. Analyze Code
- **Input**: Target module or code area.
- **Process**: Read and understand the current structure. Map dependencies, data flow, and control flow. Measure complexity (cyclomatic, cognitive). Identify the boundaries of the refactoring target.
- **Output**: Code analysis summary (structure diagram, complexity metrics, dependency map).
- **Quality Gate**: Analysis covers all entry points and side effects of the target code. Implicit dependencies (global state, shared mutable data) are identified, not just explicit ones.

### 2. Identify Smells
- **Input**: Code analysis.
- **Process**: Identify specific code smells: duplication, long methods, large classes, excessive parameters, feature envy, shotgun surgery, primitive obsession, inappropriate intimacy, lazy class, speculative generality.
- **Output**: List of code smells with location and severity.
- **Quality Gate**: Each smell is grounded in a concrete problem (not just "I don't like this style"). Smells are prioritized by the value of fixing them. Cosmetic-only changes are deprioritized.

### 3. Plan Target Structure
- **Input**: Code smells, desired design principles.
- **Process**: Design the target structure after refactoring. For each smell, determine the refactoring technique: Extract Method, Rename, Move Field, Replace Conditional with Polymorphism, Extract Class, etc. Ensure the target structure aligns with project patterns.
- **Output**: Refactoring plan: ordered list of atomic refactorings with target structure description.
- **Quality Gate**: Each atomic refactoring preserves behavior. The plan has a clear stopping point. The target structure is consistent with the rest of the codebase.

### 4. Ensure Test Coverage
- **Input**: Plan and current test suite.
- **Process**: Check test coverage of the target code paths. If coverage is insufficient, write characterization tests that capture current behavior (these tests document "what it does now" before changes).
- **Decision Point**: `[Coverage Adequate?] → [Yes] → [Proceed] | [No] → [Write characterization tests] → [Proceed]`.
- **Output**: Test suite that covers all behavior paths of the target code.
- **Quality Gate**: Characterization tests pass before any refactoring begins. They explicitly test edge cases and error paths.

### 5. Refactor (Atomic)
- **Input**: Refactoring plan, test suite.
- **Process**: Apply exactly one refactoring from the plan. Keep the change minimal and behavior-preserving. Use IDE automation (rename, extract method, etc.) where available. Do not mix refactoring with feature work.
- **Output**: Single atomic code change.
- **Quality Gate**: Only one logical refactoring per change. No feature additions or bug fixes mixed in. The change can be described in one sentence.

### 6. Run Tests
- **Input**: Atomic change, test suite.
- **Process**: Run the full test suite (not just the affected tests). Verify no regressions.
- **Decision Point**: `[Tests Pass?] → [Yes] → [More refactors?] → [Yes: Next atomic refactor] | [No: Commit] | [No] → [Revert change] → [Try different approach]`.
- **Output**: Green test suite.
- **Quality Gate**: Full suite passes. If the refactoring was behavior-preserving, the same tests should pass with the same results.

### 7. Repeat
- **Input**: Remaining items in the refactoring plan.
- **Process**: Continue the atomic-refactor → test loop until all planned refactorings are applied.
- **Decision Point**: `[More Refactors Planned?] → [Yes] → [Continue loop] | [No] → [Final verification]`.
- **Output**: All planned changes applied with passing tests.
- **Quality Gate**: Each iteration is independent. If an iteration's tests fail, the change is reverted (not fixed in place — that would mix changes).

### 8. Final Verification
- **Input**: All changes applied, all tests passing.
- **Process**: Run a broader verification: integration tests, build, lint. Check that the public API surface is unchanged (unless API changes were part of the plan). Review the complete diff for consistency.
- **Output**: Verification result.
- **Quality Gate**: No behavior changes. No API breaks unless planned. Build artifacts (if any) are identical before/after (or at least functionally equivalent).

### 9. Commit
- **Input**: Verified changes.
- **Process**: Squash all atomic refactoring commits into one commit per refactoring session. Write a descriptive commit message that explains what was refactored and why (the goal), not just listing the techniques used.
- **Output**: Single commit with all refactoring changes.
- **Quality Gate**: Commit message follows conventional commits format. Message explains the motivation (e.g., "Reduce coupling in payment module to enable pluggable providers") not just the mechanism.

## Output

- Refactored code with improved structure.
- (Optional) Improved test coverage via characterization tests.
- Updated patterns.md if new structural patterns emerged.
- Commit with clear refactoring narrative.
