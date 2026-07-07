---
id: workflow-task-lifecycle-001
version: 1.0.0
confidence: 0.85
success_rate: 0.80
last_updated: 2026-06-29
tags: [workflow, task-lifecycle, core]
---

# Task Lifecycle Workflow

Complete lifecycle for executing any task from input to compressed knowledge artifact.

## Flowchart

```
[Trigger Received] → [Recall: Find Context] → [Plan: Decompose Task]
    → [Execute: Do the Work] → [Review: Verify Output]
    → [Reflect: What Worked?] → [Extract: Save Learnings]
    → [Update: Apply Changes] → [Compress: Summarize]
    → [Done]
```

## Trigger

- New task is assigned or user issues a request.
- A recurring scheduled task fires (e.g., weekly sync).
- A sub-task is spawned from a parent workflow (e.g., feature workflow spawns a task-lifecycle for each step).

## Steps

### 1. Recall
- **Input**: Task description, user intent, environment state.
- **Process**: Search memory (decisions.md, patterns.md, past workflows) for relevant context. Identify similar past tasks and their outcomes.
- **Output**: Context summary with references to related knowledge.
- **Quality Gate**: Context must be non-empty. If no relevant memory found, flag as [First-time task] and proceed with defaults.

### 2. Plan
- **Input**: Context summary from Recall.
- **Process**: Decompose the task into atomic sub-steps. Estimate effort per step. Identify dependencies and risk areas. Write a brief execution plan (3-5 bullets max for simple tasks; full decomposition for complex ones).
- **Output**: Ordered step list with success criteria per step.
- **Quality Gate**: Each step must have a clear success criterion. No step should be too large to complete in a single session.

### 3. Execute
- **Input**: Plan from step 2.
- **Process**: Work through each sub-step in order. Use appropriate tools (edit, bash, search). Commit intermediate progress when a milestone is reached.
- **Output**: Completed work product (code changes, document, analysis, etc.).
- **Decision Point**: If execution hits an unexpected blocker, pause and escalate: [Blocker?] → [Attempt Unblock] → [Fail?] → [Return to Plan].
- **Quality Gate**: Each sub-step's success criterion must be verified before moving to the next.

### 4. Review
- **Input**: Work product from Execute.
- **Process**: Self-review the output against the plan's success criteria. Check for correctness, completeness, edge cases, and style/standards conformance.
- **Output**: Review verdict (Pass / Changes Requested / Rejected).
- **Decision Point**: [Review Verdict] → [Pass] → [Proceed] | [Changes Requested] → [Return to Execute] | [Rejected] → [Return to Plan].
- **Quality Gate**: All success criteria must be met. No known regressions introduced.

### 5. Reflect
- **Input**: Review verdict and execution notes.
- **Process**: Analyze what went well and what didn't. Identify process improvements for next time. Note any patterns worth remembering.
- **Output**: Reflection notes (2-5 sentences).
- **Quality Gate**: Reflection must identify at least one actionable improvement or confirm no improvement needed.

### 6. Extract
- **Input**: Reflection notes and work product.
- **Process**: Distill the task into reusable knowledge: patterns, decisions, gotchas, and code snippets worth saving. Format for memory storage.
- **Output**: Structured knowledge entry ready for memory update.
- **Quality Gate**: Entry must have a clear title, tags, and actionable content. No vague or generic statements.

### 7. Update
- **Input**: Knowledge entry from Extract.
- **Process**: Append/merge the entry into the appropriate memory files (decisions.md, patterns.md, skills). Update any stale references.
- **Output**: Updated memory files.
- **Quality Gate**: Memory files remain consistent (no duplicates, no contradictions). Verify by scanning the relevant section.

### 8. Compress
- **Input**: Complete task trace (plan, execution notes, review, reflections).
- **Process**: Produce a compressed summary: what was done, key decisions, result, and where the knowledge lives. This enables fast recall in future.
- **Output**: Compressed task record (max 5 sentences).
- **Quality Gate**: Summary is skimmable in under 10 seconds. Contains pointers to the full artifacts if needed.

## Output

- Completed task deliverables.
- Updated memory artifacts (decisions, patterns, skills).
- Compressed summary for future recall.
- (Optional) Updated Plans.md if the task was part of a larger initiative.
