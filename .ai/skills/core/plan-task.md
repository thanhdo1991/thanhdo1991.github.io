---
id: plan-task
version: 2.0.0
confidence: 0.85
success_rate: 0.82
last_updated: 2026-06-29
tags:
  - core
  - planning
  - rigid
  - breakdown
---

# Plan Task

> Rigid skill. A systematic, step-by-step approach to breaking down any task into actionable, sequenced, and estimatable work items. No skipping steps.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "I know what to do, I don't need to write it down" | Writing exposes hidden assumptions and dependencies. Studies show written plans reduce rework by 30-50%. |
| "Plans become obsolete immediately anyway" | The value is in the thinking, not the document. Planning surfaces edge cases before they become bugs. |
| "We need to move fast, planning is slow" | An hour of planning saves 3-10 hours of debugging. Speed without direction is just chaos. |
| "It's a simple task, a mental plan is enough" | Simple tasks become complex when context is lost during handoff or interruption. |

## Process

### 1. Analyze the Request
- Read the task description twice. Identify nouns (entities), verbs (actions), and constraints (time, resources, compatibility).
- List open questions. Get answers before proceeding.
- State the goal in one sentence: "This task aims to [measurable outcome]."

### 2. Decompose
- Break the goal into deliverables: "To achieve [goal], I need [A], [B], [C]."
- For each deliverable, identify:
  - **Input**: What data or state is needed?
  - **Process**: What transformation occurs?
  - **Output**: What artifact or state change results?
- Stop when each item is a single, focused change (typically < 50 lines of code or < 2 hours of work).

### 3. Estimate
- Assign a t-shirt size to each item: S (< 30 min), M (< 2 hr), L (< 4 hr), XL (> 4 hr).
- Flag XL items: they must be split or you must explain why they can't be.
- Add a risk multiplier: 1.5x for items touching unfamiliar code, 2x for items requiring cross-team coordination.

### 4. Sequence
- Identify dependency chains. A → B means B needs A's output.
- Parallelize independent items.
- Place high-risk items early (fail fast).
- Place high-value items first (deliver early).

### 5. Validate the Plan
- Walk through each item's output and verify it feeds into the next item.
- Check for orphan work: items whose output is not consumed by any other item or the goal.
- Confirm the plan answers: "How do I know when this is done?"

## Red Flags (STOP Signals)

- Any item you cannot explain in one sentence to a peer.
- The decomposition is a flat list of files; real plans have dependencies and flow.
- Estimate variance > 2x between comparable items without explanation.
- No clear exit criterion for any item.

## No Exceptions

- Do not start coding until the plan is written and validated.
- Do not skip the analysis step. Undefined constraints are the #1 cause of rework.
- Do not merge items because they "seem related." If they can be sequenced, they should be separate.
- Do not plan more than one day of work in detail; leave future items as placeholders.
