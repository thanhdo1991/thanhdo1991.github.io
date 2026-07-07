---
id: workflow-code-review-001
version: 1.0.0
confidence: 0.86
success_rate: 0.83
last_updated: 2026-06-29
tags: [workflow, code-review, quality]
---

# Code Review Workflow

Structured review process covering correctness, style, performance, security, and maintainability.

## Flowchart

```
[Review Requested] → [Fetch Diff] → [Understand Context]
    → [Review: Correctness] → [Review: Style & Conventions]
    → [Review: Performance] → [Review: Security]
    → [Compile Feedback] → [Blocking Issues?] → [Yes] → [Request Changes]
    → [No] → [Optional Suggestions?] → [Yes] → [Comment Suggestions]
    → [No] → [Approve]
    → [Done]
```

## Trigger

- A pull request or change set is submitted.
- Pre-commit hook requests a quick self-review pass.
- A dependency update needs verification.

## Steps

### 1. Fetch Diff
- **Input**: PR URL, commit range, or branch name.
- **Process**: Fetch the full diff. Identify changed files, added/removed lines. Determine diff size (small/medium/large). Review commit messages for narrative context.
- **Output**: Full diff with metadata (files changed, lines added/removed, commit messages).
- **Quality Gate**: Diff is complete and accurate. No merge conflicts or unrelated changes in the diff.

### 2. Understand Context
- **Input**: Diff and related artifacts (spec, issue, design doc).
- **Process**: Read the linked issue/task description. Understand why the change exists. Check if the change aligns with the stated requirements. Identify architectural impact.
- **Output**: Context summary: what the change does, why, and its scope of impact.
- **Quality Gate**: Reviewer can explain the change in their own words before reviewing specifics. If context is insufficient, request more information before proceeding.

### 3. Correctness Review
- **Process**: Read every changed line. Trace logical paths. Check for: off-by-one errors, null/undefined handling, incorrect assumptions about input data, race conditions, incorrect API usage, missing error handling.
- **Output**: List of correctness findings (blocking issues).
- **Quality Gate**: Each finding includes: (a) the exact code location, (b) why it's wrong, (c) the expected correct behavior, (d) severity (blocking vs. non-blocking).

### 4. Style & Conventions Review
- **Process**: Check alignment with project style guide. Verify: naming conventions (casing, verbosity), file organization, import ordering, consistent patterns with surrounding code. Lint warnings should be zero.
- **Output**: List of style findings (non-blocking suggestions unless flagrant).
- **Quality Gate**: Style comments are tagged as non-blocking. Lint can auto-fix — prefer running the linter over manual style nits.

### 5. Performance Review
- **Process**: Identify: N+1 queries, unnecessary re-renders, large object copies, memory leaks (e.g., unsubscribed observers), synchronous I/O in hot paths, expensive operations in loops.
- **Output**: List of performance findings with potential impact (low/medium/high).
- **Quality Gate**: Performance findings include before/after expectations. Trivial micro-optimizations are skipped unless they appear in a hot path.

### 6. Security Review
- **Process**: Check for: injection vulnerabilities (SQL, XSS, command injection), insecure data handling, hardcoded secrets, insufficient authorization checks, exposed internal endpoints, insecure deserialization.
- **Output**: List of security findings (always blocking in production code).
- **Quality Gate**: Any security finding is treated as blocking. If uncertain about a security implication, escalate rather than ignore.

### 7. Compile Feedback
- **Input**: Findings from all review dimensions.
- **Process**: Categorize each finding: (a) blocking — must fix before merge, (b) non-blocking — important but can be deferred, (c) suggestion — nice to have. Write clear, constructive comments. For each blocking issue, explain the risk of not fixing it.
- **Output**: Organized review feedback with verdict (Approve / Approve with Suggestions / Request Changes / Reject).
- **Decision Point**: `[Blocking Issues?] → [Yes] → [Request Changes] | [No, but non-blocking?] → [Comment Suggestions + Approve] | [No issues] → [Approve]`.
- **Quality Gate**: Feedback is respectful and constructive. Each comment is actionable (what to fix, not just that something is wrong). Blocking issues include the rationale.

### 8. Verify
- **Input**: Updated diff if author addressed feedback.
- **Process**: Confirm each blocking issue is resolved. Check that the resolution didn't introduce new issues. Re-review only the changed parts (not the entire diff).
- **Output**: Updated verdict after author response.
- **Quality Gate**: If diff changed significantly (>30% of lines), re-run the full review rather than spot-checking.

## Output

- Review verdict (Approve / Changes Requested / Reject).
- Categorized feedback with actionable comments.
- (Optional) Approval or blocking labels on the PR.
