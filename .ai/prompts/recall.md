---
id: recall-v1
version: 1.0.0
confidence: 0.9
success_rate: 0.85
last_updated: 2026-06-29
tags:
  - prompt
  - recall
  - knowledge-retrieval
  - memory
  - context-loading
---

Before working on {{task}}, recall relevant knowledge from {{memory_source}}. Focus on: {{aspects}}.

## How to Retrieve
Search/examine the following sources in order:
1. `.ai/memory/` — project knowledge, decisions, conventions, patterns
2. `.ai/skills/` — framework built-in skills (search by tags)
   - Built-in skills: `core/`, `testing/`, `quality/`, `data/`, `devops/`, `frontend/`, `backend/`, `process/`, `meta/`
   - User-created skills: `user/<category>/` (skills auto-created from previous tasks)
3. `.ai/prompts/` — applicable prompt templates for the task type
4. `.ai/workflows/` — relevant multi-step workflows
5. `.ai/templates/` — output format templates
6. Previous decision records and knowledge entries

For each source, read the matching files and synthesize their content into the summary format below. If no relevant content is found in a source, note that explicitly.

## Skill Gap Detection — Auto-Create New Skills
After searching all sources, **evaluate whether the existing skills cover the task**:

1. Did you find a skill file (in built-in or user/ subdirectory) with confidence ≥ 0.6 that directly matches this task domain?
2. If **YES** → note the skill name + confidence level. Use it.
3. If **NO** → **You must create a new skill immediately**:
   - Analyze the task: what domain-specific knowledge/process does it require?
   - Choose a skill name (kebab-case, e.g. `data-visualization`)
   - Pick the right subdirectory inside `user/`: `user/core/`, `user/testing/`, `user/frontend/`, `user/backend/`, `user/data/`, `user/devops/`, `user/process/`, `user/meta/`
   - Generate the skill file at `.ai/skills/user/<category>/<skill-name>.md` using this structure:
     ```yaml
     ---
     id: <skill-name>
     version: 1.0.0
     confidence: 0.70
     success_rate: 0.65
     last_updated: <today>
     tags: [<category>, <skill-name>]
     ---
     # <Skill Name>
     ## Overview
     [1-2 sentences — what this skill does and when to use it]
     ## Step-by-Step Process
     [3-5 phases covering the full workflow]
     ## Common Mistakes
     [2-3 typical errors and how to avoid them]
     ## Quality Gates
     [checklist of criteria for successful completion]
     ```
   - Record the creation in `.ai/observability/changelog.md` under "Added"
   - **Use the new skill** to execute the task

### When NOT to Auto-Create
- If an existing skill exists with confidence ≥ 0.6 → use it, don't duplicate
- If the task is trivial (one-step, no process needed) → no skill needed
- If unsure about the skill category → default to `process/`

## Content to Retrieve
1. Similar tasks completed previously and their outcomes
2. Known patterns, anti-patterns, and idiomatic approaches related to this domain
3. Relevant decisions, trade-offs, and rationales documented in the knowledge base
4. Common pitfalls and edge cases encountered in past related work
5. Skill-specific guidance and best practices applicable to this task

Format the recall as a structured summary with:
- Key insights (bullet points)
- Relevant past decisions (with links to decision records)
- Applicable skills and their confidence levels
- Potential risks to watch for during execution

For each insight, rate its relevance to the current task on a scale of 1-5 and indicate whether it has been verified or is still an assumption.
