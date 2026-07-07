---
id: review-code
version: 2.0.0
confidence: 0.85
success_rate: 0.80
last_updated: 2026-06-29
tags:
  - core
  - review
  - rigid
---

# Review Code

> Rigid skill. Systematic code review with a strict hierarchy: correctness > style > performance > security. Follow the order; do not skip categories.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "I trust the author, this is a formality" | Even senior developers miss bugs. Four eyes catch more than two. |
| "I focus on style since correctness is obvious" | Style is cosmetic; correctness is functional. Style should be auto-formatted, not reviewed. |
| "The diff is small, I can skim it" | Small diffs can have large impact. A one-line change can introduce a SQL injection or an infinite loop. |
| "We'll catch it in QA" | A code review catch costs minutes; a QA catch costs days; a production catch costs customers. |

## Review Hierarchy

### 1. Correctness (Non-negotiable)
- Does the code do what the requirement says? Trace the requirement to the implementation.
- Check boundary conditions: empty collections, null values, off-by-one errors, type mismatches.
- Verify error handling: every fallible operation has appropriate error handling. No silent swallows.
- Check state mutations: are shared data structures mutated safely? Are there race conditions?
- Validate assumptions: does the code assume a certain order of operations, data format, or external state?

### 2. Style (After correctness)
- Does the code follow the project's formatting and naming conventions?
- Are names descriptive? A function name should describe what it does; a variable name should describe what it holds.
- Is the code readable? Would a new team member understand it without comments?
- Are comments necessary? Good code documents itself; comments should explain "why", not "what".

### 3. Performance (After style)
- Are there obvious N+1 queries or redundant computations?
- Are resources (connections, file handles, memory) properly released?
- Is caching appropriate and correctly implemented?
- Are hot paths identified and optimized (or at least not pessimized)?

### 4. Security (After performance)
- Are user inputs validated, sanitized, and escaped?
- Are there hardcoded secrets, tokens, or credentials?
- Does the code follow the principle of least privilege?
- Are there injection vectors (SQL, NoSQL, command, template, LDAP)?

## Red Flags (STOP Signals)

- Reviewer cannot trace the diff back to a specific requirement.
- The diff is > 400 lines. Request it be split.
- More style comments than correctness comments. The review is misprioritized.
- Any TODO or FIXME in production code. Either fix it or file a ticket.
- Tests are missing or only test the happy path.

## Systematic Review Process

1. Read the requirement or issue description.
2. Read the diff title and summary.
3. Review tests first: do they cover the requirement? Are they meaningful?
4. Review the implementation: follow the hierarchy above.
5. Classify each comment: [Correctness], [Style], [Performance], [Security], [Question].
6. For each comment, state: (a) what you see, (b) why it's a concern, (c) what the fix should be.
7. Final verdict: Approve, Changes Requested, or Comment (non-blocking suggestions).

## No Exceptions

- Do not approve a diff you have not read line by line.
- Do not skip test review. Tests are the specification.
- Do not use "LGTM" without substance. Every review must have at least one substantive comment or explicit statement of "no issues found."
- Do not review when tired, distracted, or rushed. Reschedule.
