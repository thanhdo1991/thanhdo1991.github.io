---
id: agent-003
version: 1.0.0
confidence: 0.98
success_rate: 0.95
last_updated: 2026-06-29
tags:
  - rules
  - constraints
  - immutable
---

# rules.md — Immutable Operating Rules

These rules are non-negotiable. Violation constitutes a system failure and must be logged as such.

## Rule 1: Context Recall Before Action

Before starting any task, load relevant context: project structure, prior decisions, active constraints, and applicable patterns. Operating without context is not permitted.

## Rule 2: No Commit Without Review

Every change destined for version control must pass a structured review:
- Functional correctness verified
- Tests pass (or new tests written and passing)
- No debug artifacts, commented code, or placeholder values
- Diff reviewed against scope of work

## Rule 3: Always TDD (Test-Driven Development)

- Write failing tests before implementation code.
- Verify that tests pass after implementation.
- Refactor only with green test suite.
- Exception: exploratory spikes, which must be documented and discarded before production code.

## Rule 4: Verify Before Completion

Claims of completion must be backed by evidence:
- Automated test results
- Linting and type-checking output
- Manual verification steps (when automation is unavailable)
- A summary of what was verified and how

## Rule 5: Never Hallucinate

- Do not fabricate APIs, library functions, error messages, or behaviors.
- If uncertain about a fact, state the uncertainty and propose how to verify.
- If a specific version or parameter is unknown, mark it as `[VERIFY]` in output and resolve before claiming done.

## Rule 6: Auto-Create Skills When None Match

Before starting any task, the recall phase MUST check whether existing skills (both built-in `skills/<category>/` and user-created `skills/user/<category>/`) cover the task domain. If no skill with confidence ≥ 0.6 exists that matches:
- **Create a new skill file** under `skills/user/<category>/` (see `.ai/prompts/recall.md` — Skill Gap Detection section)
- Follow the standard skill template (frontmatter + process + quality gates)
- Record the creation in changelog
- Use the new skill to execute the task

This rule is immutable. Do not skip it because "I'll create the skill later" or "the task is simple."

## Rule 7: Log Deviations

When a rule cannot be followed (e.g., no test framework exists yet), log the deviation with justification and a plan to re-enable compliance.
