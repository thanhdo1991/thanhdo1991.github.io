---
id: agent-010
version: 1.0.0
confidence: 0.90
success_rate: 0.86
last_updated: 2026-06-29
tags:
  - context
  - memory
  - optimization
---

# context-window.md — Context Management Strategy

## Context Window Constraints

The agent operates within a fixed-size context window. As conversation length increases, older information is at risk of being evicted or compressed, which can degrade decision quality. This document defines the strategy for managing context effectively.

## Strategy Overview

```
Recall -> Act -> Compress -> Store -> Next Task
```

## 1. Recall Before Acting

Before any significant operation, load:
- Project structure overview (key directories, config files, stack)
- Active constraints (from `constraints.md` and `rules.md`)
- Recent decisions from the decision log
- Relevant patterns from prior work

This ensures the agent operates with full awareness of the current state, even when pieces of prior context have aged out.

## 2. Structured Context Organization

Use a consistent structure within the context to minimize search overhead:

- **Task definition** — what is being done, why, and what success looks like
- **Active constraints** — loaded from rules/constraints at task start
- **Current state** — where in the Plan -> Execute -> Verify cycle the task is
- **Evidence log** — key outputs, test results, and verification data produced during the task

## 3. Compression Techniques

After completing a task or reaching a checkpoint:

- Summarize detailed discussions into concise decision records.
- Replace verbose tool output with structured summaries (pass/fail counts, key errors).
- Archive full logs to external files when they exceed useful context density.
- Remove resolved sub-tasks from the active plan.

## 4. Template Usage

Use structured templates for consistent output that is easy to scan and compress:

- **Decision records**: Context -> Options -> Rationale -> Outcome
- **Task summaries**: Goal -> Approach -> Result -> Verification
- **Error reports**: Observed -> Expected -> Diagnosis -> Resolution

Templates reduce the tokens needed for structure, leaving more capacity for content.

## 5. Handoff Preparation

When context pressure is high and a task spans multiple sessions:
- Write a concise checkpoint summary to a handoff file.
- Include: task state, next action, known risks, and verification status.
- Reference the handoff file explicitly at the start of the next session.

## 6. Continuous Improvement

Track context utilization over time:
- Log instances where context loss caused a mistake or rework.
- Adjust compression thresholds based on observed failure patterns.
- Refine the recall checklist as new information categories prove important.
