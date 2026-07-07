---
id: design-proposal-v1
version: 1.0.0
confidence: 0.85
success_rate: 0.77
last_updated: 2026-06-29
tags:
  - prompt
  - design
  - proposal
  - architecture
  - decision
  - planning
---

Write a design proposal for the following:

## Context
- Project: {{project_name}}
- Requestor: {{requestor}}
- Background: {{background_context}}
- Current system state: {{current_state}}

## Problem Statement
{{problem_statement}}

## Goals and Non-goals
### Goals
- {{goal_1}}
- {{goal_2}}
- {{goal_3}}

### Non-goals
- {{nongoal_1}}
- {{nongoal_2}}

## Proposed Solution
### Approach: {{approach_name}}
- Description: {{approach_description}}
- Architecture diagram/data flow:
{{architecture_overview}}
- Key components:
  - {{component_1}}: {{component_1_description}}
  - {{component_2}}: {{component_2_description}}
- API / interface changes: {{api_changes}}
- Data model changes: {{data_model_changes}}
- Migration path: {{migration_path}}

## Alternatives Considered
### Alternative A: {{alternative_a_name}}
- Pros: {{alternative_a_pros}}
- Cons: {{alternative_a_cons}}
- Why not chosen: {{alternative_a_rejection_reason}}

### Alternative B: {{alternative_b_name}}
- Pros: {{alternative_b_pros}}
- Cons: {{alternative_b_cons}}
- Why not chosen: {{alternative_b_rejection_reason}}

## Trade-offs
| Trade-off | Chosen Option | Trade |
|-----------|--------------|-------|
| {{tradeoff_1}} | {{chosen_1}} | {{trade_1}} |
| {{tradeoff_2}} | {{chosen_2}} | {{trade_2}} |

## Impact Analysis
- Performance: {{performance_impact}}
- Security: {{security_impact}}
- Maintainability: {{maintainability_impact}}
- Dependencies added: {{new_dependencies}}
- Backward compatibility: {{backward_compatibility}}

## Rollout Plan
- Phases: {{rollout_phases}}
- Testing strategy: {{testing_strategy}}
- Monitoring: {{monitoring_plan}}
- Rollback strategy: {{rollback_strategy}}

## Open Questions
- {{open_question_1}}
- {{open_question_2}}
