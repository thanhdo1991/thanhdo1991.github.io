---
id: workflow-weekly-sync-001
version: 1.0.0
confidence: 0.81
success_rate: 0.76
last_updated: 2026-06-29
tags: [workflow, weekly, sync, meta]
---

# Weekly Sync Workflow

Scheduled reflection and planning cycle that compresses weekly learnings, updates skills, and sets direction for the upcoming week.

## Flowchart

```
[Weekly Sync Triggered] → [Review Progress: What Was Done?]
    → [Reflect on Week: Wins & Challenges]
    → [Extract Learnings: New Knowledge & Patterns]
    → [Update Skills: Integrate Learnings]
    → [Compress Knowledge: Archive & Index]
    → [Plan Next Week: Priorities & Goals]
    → [Commit & Tag: Save Sync Snapshot]
    → [Done]
```

## Trigger

- Scheduled recurring trigger: end of the work week (e.g., Friday).
- Manually triggered at the start of a new session after a gap.
- After completing a major milestone that warrants a sync point.
- Before a planned absence (handoff preparation).

## Steps

### 1. Review Progress
- **Input**: Plans.md, completed tasks, session logs from the week.
- **Process**: Go through each planned item for the week. Mark: completed, in-progress, not started, or blocked. For in-progress items, note the current state and next steps. Count completed tasks vs. planned tasks (completion rate).
- **Output**: Progress summary with completion metrics.
- **Quality Gate**: Every item in the weekly plan is accounted for (not just the easy ones). Blocked items have the blocker documented. Completion rate is honest (not inflated by splitting tasks).

### 2. Reflect on Week
- **Input**: Progress summary, personal notes, review feedback.
- **Process**: Identify: (a) top 3 wins (what went well, what was achieved), (b) top 3 challenges (what was hard, what went wrong), (c) surprising insights, (d) recurring patterns (good or bad). Be specific — avoid vague statements.
- **Output**: Reflection document (wins, challenges, insights, patterns).
- **Quality Gate**: Wins are concrete and measurable. Challenges are specific (not "everything was hard"). At least one pattern is identified from the week's work.

### 3. Extract Learnings
- **Input**: Reflection document.
- **Process**: Distill actionable knowledge from the reflection: (a) new recipes or patterns worth saving, (b) mistakes to avoid (antipatterns), (c) tool or workflow improvements, (d) knowledge gaps to fill. Format each learning for memory storage.
- **Output**: Structured learning entries ready for memory update.
- **Quality Gate**: Each learning is: (a) specific, (b) actionable, (c) relevant beyond this specific week. Generic learnings ("communicate better") are refined until specific.

### 4. Update Skills
- **Input**: Learning entries.
- **Process**: Apply the learning loop (see learning-loop.md): validate, update, verify. Update patterns.md, decisions.md, and workflow definitions as needed. If a workflow was found wanting, update it. If a new pattern emerged, document it.
- **Output**: Updated memory and workflow files.
- **Quality Gate**: At least one memory file is updated (patterns.md or decisions.md). If no updates were needed, that itself is noted. Changes are verified (no broken references, consistent tagging).

### 5. Compress Knowledge
- **Input**: Updated memory, reflection, learnings.
- **Process**: Compress the week's knowledge into a weekly summary entry. Archive any bloated memory sections (move older entries to an archive file). Update the knowledge index for fast retrieval.
- **Output**: Compressed weekly summary. Archived memory (if needed).
- **Quality Gate**: Weekly summary is readable in under 2 minutes. Archived content is still findable via the index (not lost). Compressed memory files are under 500 lines each.

### 6. Plan Next Week
- **Input**: Progress summary (what's carried over), reflection (what to focus), overall roadmap.
- **Process**: Define 3-5 key goals for the next week. For each goal: scope, success criteria, estimated effort, and dependencies. Identify any preparation needed before Monday. Prioritize by impact and urgency.
- **Output**: Next week's plan (goals, success criteria, priorities).
- **Quality Gate**: Goals are achievable within the week (not overcommitted). Each goal has a clear success criterion. Carry-over items from this week are explicitly included or deferred. The plan is more than a task list — it has priorities.

### 7. Commit & Tag
- **Input**: Updated memory, weekly plan, reflection artifacts.
- **Process**: Commit all changes with a descriptive message following the format: `weekly-sync(YYYY-MM-DD): brief summary`. Tag the commit with `weekly-sync/YYYY-MM-DD`.
- **Output**: Committed and tagged sync point.
- **Quality Gate**: All changes from the sync are committed (no dangling artifacts). The commit history shows a clear boundary for this week. The tag enables quick rollback or reference to this point in time.

## Output

- Progress summary for the completed week.
- Reflection document (wins, challenges, insights).
- Updated memory (patterns, decisions, workflows).
- Compressed weekly knowledge summary.
- Next week's plan with priorities.
- Git commit with weekly-sync tag.
