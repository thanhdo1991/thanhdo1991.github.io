---
id: improve-skill-v1
version: 1.0.0
confidence: 0.83
success_rate: 0.75
last_updated: 2026-06-29
tags:
  - prompt
  - skill-improvement
  - meta-learning
  - optimization
  - self-evolution
---

Review and improve the following skill:

## Skill Profile
- Skill name: {{skill_name}}
- Current version: {{current_version}}
- Current confidence: {{current_confidence}}
- Current success rate: {{success_rate}}
- Usage count: {{usage_count}}

## Usage Analysis
### Recent Usage
| Date | Task | Outcome | Confidence Delta |
|------|------|---------|-----------------|
| {{date_1}} | {{task_1}} | {{outcome_1}} | {{delta_1}} |
| {{date_2}} | {{task_2}} | {{outcome_2}} | {{delta_2}} |

### Common Failure Patterns
- {{failure_pattern_1}}
- {{failure_pattern_2}}

### Knowledge Gaps
- {{knowledge_gap_1}}
- {{knowledge_gap_2}}

## Gap Analysis
- What should the skill handle that it currently does not?
- {{missing_capability_1}}
- {{missing_capability_2}}
- Where does the skill produce suboptimal results?
- {{weakness_1}}
- {{weakness_2}}

## Improvement Proposals

### Improvement 1: {{improvement_1_name}}
- Description: {{improvement_1_description}}
- Expected impact: {{improvement_1_impact}}
- Implementation effort: {{improvement_1_effort}}
- Priority: {{improvement_1_priority}}

### Improvement 2: {{improvement_2_name}}
- Description: {{improvement_2_description}}
- Expected impact: {{improvement_2_impact}}
- Implementation effort: {{improvement_2_effort}}
- Priority: {{improvement_2_priority}}

## Metrics
- Target confidence after improvements: {{target_confidence}}
- Target success rate: {{target_success_rate}}
- Review period: {{review_period}}

## Implementation Plan
- Changes to skill prompt: {{prompt_changes}}
- Changes to related skills: {{related_skill_changes}}
- New knowledge required: {{new_knowledge_required}}
- Testing/validation plan: {{validation_plan}}

## Apply Changes
After completing the analysis and obtaining approval, execute the improvements:

1. **Update the skill file** at `.ai/skills/{{skill_path}}`:
   - Apply the approved prompt/process changes
   - Bump version (e.g., 2.0.0 → 2.1.0)
   - Adjust `confidence` based on usage data
   - Update `success_rate` with latest outcomes
   - Set `last_updated` to current date

2. **Generate a changelog entry** in the skill's changelog section or in `.ai/observability/changelog.md` under "Changed" or "Fixed":
   - Record what changed and why
   - Include before/after confidence values

3. **Update related skills** if the implementation plan specifies changes to them

4. **Save extracted knowledge** using the extract-knowledge prompt flow

5. **Verify** the updated skill produces correct behavior on a test case
