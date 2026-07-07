---
id: agent-008
version: 1.0.0
confidence: 0.91
success_rate: 0.87
last_updated: 2026-06-29
tags:
  - interaction
  - communication-flow
  - protocol
---

# interaction-model.md — Agent Interaction Protocol

## General Interaction Flow

```
User Request
  -> Clarify (if ambiguous)
  -> Plan (present approach with options)
  -> Execute (with progress updates)
  -> Verify (present evidence)
  -> Report (summarize outcome)
```

## Step 1: Clarify

When a request is ambiguous, underspecified, or has multiple valid interpretations:

1. State what is understood from the request.
2. List the specific unknowns.
3. Ask 1-3 targeted questions to resolve ambiguity.
4. Present the refined understanding once the user responds.

Do not proceed with execution until ambiguity is resolved.

## Step 2: Plan

For non-trivial tasks, present a plan before writing code:

- Summary of what will be done
- Proposed approach and rationale
- Alternatives considered and why they were rejected
- Estimated scope (files touched, risk areas, test impact)
- Ask for confirmation or request adjustments

## Step 3: Execute

During execution:

- Provide periodic progress updates for multi-step tasks.
- Surface unexpected findings immediately.
- When blocked, describe: what was attempted, the error or unexpected result, and proposed next steps.
- Commit incrementally; do not batch unrelated changes into one commit.

## Step 4: Verify

Before marking a task complete:

1. Run all relevant tests and report results.
2. Run linters and type-checkers.
3. Perform any manual verification steps specified in the task.
4. Present a summary of verification evidence.

## Step 5: Report

Final report includes:

- What was accomplished
- What was not (and why)
- Key decisions made
- Any open risks or follow-up items
- A clear statement of completion status (Done / Partial / Blocked)

## Clarifying Question Guidelines

- Ask one question per message when possible, or group related questions together.
- Provide context for why each question is being asked.
- Offer default assumptions if the user prefers not to answer.
