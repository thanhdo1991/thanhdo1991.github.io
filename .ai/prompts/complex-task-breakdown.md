---
id: complex-task-breakdown-v1
version: 1.0.0
confidence: 0.84
success_rate: 0.76
last_updated: 2026-06-29
tags:
  - prompt
  - planning
  - decomposition
  - complex-task
  - architecture
  - multi-domain
---

Decompose this complex task into a structured execution plan organized by domain.

## Task Overview
- Title: {{task_title}}
- Description: {{task_description}}
- Strategic context: {{strategic_context}}
- Success criteria: {{success_criteria}}

## Domain Decomposition
Split the task by domain/area of expertise:

### Domain 1: {{domain_1_name}}
- Owner skill: {{domain_1_skill}}
- Work packages:
  - {{work_package_1_1}}: {{wp_1_1_description}}
  - {{work_package_1_2}}: {{wp_1_2_description}}
- Acceptance criteria: {{domain_1_ac}}
- Estimated effort: {{domain_1_effort}}

### Domain 2: {{domain_2_name}}
- Owner skill: {{domain_2_skill}}
- Work packages:
  - {{work_package_2_1}}: {{wp_2_1_description}}
  - {{work_package_2_2}}: {{wp_2_2_description}}
- Acceptance criteria: {{domain_2_ac}}
- Estimated effort: {{domain_2_effort}}

## Interface Definitions
Define the contracts between domains:

### Interface: {{interface_1_name}}
- Between: {{interface_1_source}} and {{interface_1_target}}
- Data exchanged: {{interface_1_data}}
- Protocol/format: {{interface_1_protocol}}
- Error handling: {{interface_1_error_handling}}

### Interface: {{interface_2_name}}
- Between: {{interface_2_source}} and {{interface_2_target}}
- Data exchanged: {{interface_2_data}}
- Protocol/format: {{interface_2_protocol}}
- Error handling: {{interface_2_error_handling}}

## Execution Sequence

### Phase 1: Foundation (Day {{phase_1_start}} - {{phase_1_end}})
- {{phase_1_task_1}}
- {{phase_1_task_2}}
- Milestone: {{phase_1_milestone}}

### Phase 2: Core Implementation (Day {{phase_2_start}} - {{phase_2_end}})
- {{phase_2_task_1}}
- {{phase_2_task_2}}
- Milestone: {{phase_2_milestone}}

### Phase 3: Integration and Testing (Day {{phase_3_start}} - {{phase_3_end}})
- {{phase_3_task_1}}
- {{phase_3_task_2}}
- Milestone: {{phase_3_milestone}}

### Phase 4: Polish and Deploy (Day {{phase_4_start}} - {{phase_4_end}})
- {{phase_4_task_1}}
- {{phase_4_task_2}}
- Milestone: {{phase_4_milestone}}

## Coordination Plan
- Communication cadence: {{communication_cadence}}
- Sync points: {{sync_points}}
- Dependency tracking: {{dependency_tracking}}
- Review gates: {{review_gates}}
