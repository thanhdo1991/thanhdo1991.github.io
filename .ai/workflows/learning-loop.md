---
id: workflow-learning-loop-001
version: 1.0.0
confidence: 0.85
success_rate: 0.78
last_updated: 2026-06-29
tags: [workflow, learning, improvement]
---

# Learning Loop Workflow

Continuous self-improvement cycle that extracts knowledge from experience and integrates it into permanent skills and memory.

## Flowchart

```
[Experience Event] → [Extract Knowledge] → [Validate: Accurate & Novel?]
    → [Yes] → [Update Skills/Memory] → [Verify Improvement]
    → [Compress for Recall] → [Index for Search]
    → [No] → [Discard / Flag as Low Confidence]
    → [End]
```

## Trigger

- A task is completed (post-task-lifecycle).
- A new pattern is observed across multiple tasks.
- The user explicitly shares knowledge or feedback.
- A recurring scheduled learning cycle (e.g., weekly sync retro).

## Steps

### 1. Extract Knowledge
- **Input**: Task output, review verdict, reflection notes, user feedback.
- **Process**: Identify novel information that was not previously in memory. Categorize into: (a) decision rationale, (b) reusable pattern, (c) tool/framework insight, (d) process improvement, (e) error/antipattern.
- **Output**: Raw knowledge entries with category tags and confidence estimate.
- **Quality Gate**: Each entry must be specific and falsifiable. No vague truisms or subjective opinions without supporting evidence.

### 2. Validate
- **Input**: Raw knowledge entries from step 1.
- **Process**: Cross-check against existing memory for accuracy and novelty. If the knowledge contradicts existing memory, flag for conflict resolution. If it duplicates existing knowledge, discard or merge.
- **Decision Point**: [Accurate & Novel?] → [Yes] → [Proceed to Update] | [No: Duplicate] → [Discard] | [No: Contradicts] → [Resolve Conflict] → [Update or Discard].
- **Output**: Validated knowledge entries ready for storage.
- **Quality Gate**: No validated entry duplicates existing memory. Contradictions are resolved (not ignored).

### 3. Update Skills/Memory
- **Input**: Validated entries.
- **Process**:
  - For **patterns**: append to patterns.md with usage examples.
  - For **decisions**: append to decisions.md with context and rationale.
  - For **skills**: update the relevant skill definition or create a new one.
  - For **process improvements**: update workflow definitions in .ai/workflows/.
- **Output**: Updated memory files and/or skill definitions.
- **Quality Gate**: Update is atomic (no partial writes). If a file gets too large (>500 lines), archive older entries and create an index.

### 4. Verify Improvement
- **Input**: Updated memory/skills.
- **Process**: Run a self-test to confirm the update does not degrade performance. For skills: simulate a simple scenario that uses the updated knowledge. For patterns: check that the pattern is self-consistent and has clear applicability conditions.
- **Output**: Verification result (pass/fail).
- **Decision Point**: [Verification Pass?] → [Yes] → [Proceed to Compress] | [No] → [Rollback Update] → [Log Verification Failure].
- **Quality Gate**: Verification must exercise the new knowledge in a realistic scenario. If automatable, run the relevant test suite.

### 5. Compress for Recall
- **Input**: Verified knowledge.
- **Process**: Distill to a compact form optimized for fast retrieval. Use consistent tagging. Add cross-references to related knowledge.
- **Output**: Compressed knowledge entry (1-3 sentences with tags).
- **Quality Gate**: Compressed form preserves all essential information. No lossy compression that changes meaning.

### 6. Index for Search
- **Input**: Compressed entries.
- **Process**: Update the knowledge index so the Recall step in task-lifecycle can find this knowledge efficiently. Add keywords, aliases, and relationship links.
- **Output**: Updated index.
- **Quality Gate**: Index can retrieve the entry using at least two different query formulations.

## Output

- Updated memory files (patterns.md, decisions.md).
- Updated or new skill definitions.
- Verified, compressed, indexed knowledge ready for future recall.
- Learning loop metrics (entries added, conflicts resolved, verifications passed/failed).
