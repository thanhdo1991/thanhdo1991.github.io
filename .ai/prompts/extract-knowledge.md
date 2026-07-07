---
id: extract-knowledge-v1
version: 1.0.0
confidence: 0.87
success_rate: 0.80
last_updated: 2026-06-29
tags:
  - prompt
  - knowledge-extraction
  - learning
  - skill-update
  - experience-capture
---

Extract knowledge from the following experience:

## Experience Summary
- Task/context: {{task_context}}
- What happened: {{what_happened}}
- Outcome: {{outcome}}
- Surprises encountered: {{surprises}}

## Knowledge Extraction

### What was learned?
{{learned_content}}

### Pattern Identified
- Pattern type (success/failure/reusable): {{pattern_type}}
- Pattern description: {{pattern_description}}
- Conditions for applicability: {{applicability_conditions}}

### Skill Update Required
- Skill to update: {{skill_name}}
- Current confidence: {{current_confidence}}
- New confidence: {{new_confidence}}
- Rationale for change: {{rationale}}

### New Decision Record Needed?
- Does this experience warrant a new decision record? {{needs_decision_record}}
- If yes, summary: {{decision_summary}}

### Reusable Artifacts
- Code snippets, templates, or configurations worth preserving:
{{reusable_artifacts}}

### Knowledge Distribution
- Who else should know about this? {{share_with}}
- Best channel for sharing: {{share_channel}}

## Storage
Store this in the knowledge base under:
- Category: {{knowledge_category}}
- Tags: {{knowledge_tags}}
- Retention priority (1-5): {{retention_priority}}

## Save Knowledge
After filling in the template above, persist this knowledge:
1. Generate a slug from the pattern/category name
2. Save to: `.ai/memory/{{knowledge_category}}/{{date}}-{{slug}}.md`
3. Apply the YAML frontmatter pattern from templates/ or existing memory files
4. If a skill update is required, also update the relevant skill file in `.ai/skills/`:
   - Bump the version field
   - Adjust confidence based on outcome
   - Update success_rate if applicable
