---
id: workflow-feature-001
version: 1.0.0
confidence: 0.83
success_rate: 0.76
last_updated: 2026-06-29
tags: [workflow, feature, development]
---

# Feature Workflow

End-to-end process for implementing new features with test-first methodology and quality gates.

## Flowchart

```
[Feature Request] → [Spec Review] → [Accept?] → [No] → [Reject / Send Back]
    → [Yes] → [Create Plan]
    → [TDD Loop: Write Test → Run → Fail] → [Implement to Pass]
    → [Refactor (if needed)] → [All Tests Pass?] → [No] → [Fix / Adjust]
    → [Yes] → [Code Review] → [Approved?] → [No] → [Address Feedback]
    → [Yes] → [Ship: Merge + Deploy]
    → [Done]
```

## Trigger

- User requests a new capability.
- Product spec or feature brief is provided.
- A spike/prototype is validated and greenlit for implementation.
- Derived from a higher-level roadmap item.

## Steps

### 1. Spec Review
- **Input**: Feature request, acceptance criteria, user stories, design docs.
- **Process**: Review the spec for clarity, completeness, and feasibility. Identify ambiguous requirements, missing acceptance criteria, and potential design gaps. Ask clarifying questions.
- **Output**: Reviewed spec with annotations (accepted, rejected, needs clarification). Updated acceptance criteria.
- **Decision Point**: [Spec Clear & Complete?] → [Yes] → [Accept] | [No: Needs Work] → [Send back with questions] | [No: Infeasible] → [Reject with rationale].
- **Quality Gate**: Every acceptance criterion is testable (measurable, observable, unambiguous). At least one person besides the author has reviewed the spec.

### 2. Plan
- **Input**: Approved spec.
- **Process**: Decompose the feature into implementation steps. Identify files to create/modify. Decide between TDD (Red-Green-Refactor) for each unit. Estimate effort. Identify dependencies.
- **Output**: Implementation plan with file list, step order, and effort estimates.
- **Quality Gate**: Plan identifies all files that need changes. Steps are ordered to minimize merge conflicts. Plan includes test files, not just implementation files.

### 3. TDD Loop (Red-Green-Refactor)
- **Input**: Implementation plan, feature spec, existing test suite.
- **Process**: For each unit:
  1. **Red**: Write a test that captures the desired behavior. Run it — it should fail.
  2. **Green**: Implement the minimum code to make the test pass.
  3. **Refactor**: Clean up code while keeping tests green.
- **Output**: Working code with passing tests for each unit.
- **Quality Gate**: Every Red step produces a failing test with a meaningful failure message. Every Green step is minimal (just enough to pass). No production code is written without a preceding failing test.

### 4. Code Review
- **Input**: Full feature implementation, all tests passing, diff of changes.
- **Process**: Apply the code review workflow (see code-review.md). Focus on correctness, test coverage, edge cases, and alignment with spec.
- **Decision Point**: [Review Approved?] → [Yes] → [Ready to Ship] | [Changes Requested] → [Address feedback → Re-run tests] | [Rejected] → [Major rework + re-review].
- **Quality Gate**: Test coverage >= 80% for new code. All existing tests still pass. No lint/type errors. Review was performed by someone who understands the domain.

### 5. Ship
- **Input**: Approved code, passing CI.
- **Process**: Merge to the target branch. Deploy to staging for final verification (if applicable). Deploy to production per release workflow (see release.md).
- **Output**: Merged code, deployed feature.
- **Quality Gate**: Post-deploy monitoring confirms the feature works as expected. Rollback plan exists.

## Output

- Feature implementation (code changes).
- Tests (unit, integration, as applicable).
- Updated documentation (if spec required it).
- Updated memory (new patterns, decisions made during implementation).
- (Optional) Feature flag configuration if phased rollout.
