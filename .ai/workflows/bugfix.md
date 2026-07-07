---
id: workflow-bugfix-001
version: 1.0.0
confidence: 0.88
success_rate: 0.82
last_updated: 2026-06-29
tags: [workflow, bugfix, debugging]
---

# Bugfix Workflow

Systematic process for reproducing, diagnosing, fixing, and learning from bugs.

## Flowchart

```
[Bug Report] → [Reproduce: Confirm Bug]
    → [Known Bug?] → [Yes] → [Quick Fix: Apply Known Solution] → [Verify Fix]
    → [No] → [Isolate: Minimize Scope]
    → [Root Cause Analysis] → [Identify Cause]
    → [Implement Fix] → [Write Regression Test]
    → [Verify Fix + No Regression] → [Update Memory]
    → [Done]
```

## Trigger

- User reports a bug (unexpected behavior, error, crash).
- CI pipeline detects a test failure.
- Monitoring alerts on a production anomaly.
- Security scan reports a vulnerability.

## Steps

### 1. Reproduce
- **Input**: Bug report, error message, stack trace, failing test.
- **Process**: Attempt to reproduce the bug with the given inputs. If reproduction steps are incomplete, gather more information. Confirm the bug exists and is not a user error or environment issue.
- **Output**: Reliable reproduction steps (minimal, deterministic).
- **Quality Gate**: Bug is reproduced at least twice in a clean environment. Steps are precise enough for another developer to reproduce.

### 2. Known Bug Check
- **Input**: Reproduction steps from step 1.
- **Process**: Search memory (patterns.md, decisions.md, past issues) for matching bug signature. Cross-reference error messages, stack trace patterns, and affected components.
- **Decision Point**: [Known Bug?] → [Yes] → [Apply known fix from memory] → [Skip to Verify] | [No] → [Proceed to Isolate].
- **Output**: Classification (known vs. unknown) and, if known, reference to the stored fix.
- **Quality Gate**: Search is thorough (multiple query formulations). False negatives (thinking it's unknown when it's known) are worse than false positives here.

### 3. Isolate
- **Input**: Unknown bug with reproduction steps.
- **Process**: Use binary search / divide-and-conquer to narrow the scope. Strip away unrelated code. Create a minimal reproduction that isolates the bug to the smallest possible code region.
- **Output**: Minimal reproduction (smallest input, smallest code path that triggers the bug).
- **Quality Gate**: The minimal reproduction should be as simple as possible but no simpler. At minimum, the affected function/module is identified.

### 4. Root Cause Analysis
- **Input**: Minimal reproduction from step 3.
- **Process**: Trace execution from input through the minimal path. Identify the exact line/code path where behavior diverges from expected. Determine why the code behaves that way (logic error, race condition, edge case, API change, etc.).
- **Output**: Root cause statement (e.g., "Function X returns null when input Y is negative because Z was not initialized").
- **Quality Gate**: Root cause is precise enough that a fix can be designed without speculation. If the root cause is uncertain, add instrumentation and gather more data.

### 5. Implement Fix
- **Input**: Root cause statement.
- **Process**: Design the minimal change that corrects the behavior without side effects. Consider edge cases the fix might introduce. Write the fix.
- **Output**: Code change (diff).
- **Quality Gate**: Fix is minimal (smallest change that corrects the issue). Fix does not introduce new bugs (checked via static analysis). Fix follows project conventions.

### 6. Write Regression Test
- **Input**: Root cause statement and minimal reproduction.
- **Process**: Write a test that fails before the fix and passes after. Ensure the test covers the exact bug scenario plus any related edge cases.
- **Output**: Regression test(s).
- **Quality Gate**: Test fails against the unfixed code. Test is added to the appropriate test suite. Coverage of the bug path is confirmed.

### 7. Verify Fix
- **Input**: Fix and regression test.
- **Process**: Run the full test suite (unit, integration, affected e2e). Verify the original reproduction steps no longer trigger the bug. Check for any regressions.
- **Output**: Verification result (pass/fail).
- **Decision Point**: [All Tests Pass?] → [Yes] → [Proceed to Update Memory] | [No] → [Return to Root Cause or Fix].
- **Quality Gate**: Full test suite passes. No new warnings or lint errors. If production, verify the fix in a staging environment.

### 8. Update Memory
- **Input**: Root cause, fix, test, verification result.
- **Process**: Store the bug signature and fix in memory (patterns.md — antipatterns section, decisions.md). Tag for future retrieval.
- **Output**: Updated memory entries.
- **Quality Gate**: The stored knowledge includes: (a) symptom/error signature, (b) root cause, (c) fix applied, (d) test reference. A future occurrence should be retrievable by error message or symptom.

## Output

- Bug fix (code change).
- Regression test(s).
- Root cause documentation.
- Updated memory for future recall.
- (Optional) If severity warrants: incident report.
