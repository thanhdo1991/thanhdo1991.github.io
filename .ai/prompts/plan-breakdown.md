---
id: plan-breakdown-v1
version: 1.0.0
confidence: 0.85
success_rate: 0.79
last_updated: 2026-06-29
tags:
  - prompt
  - planning
  - decomposition
  - estimation
  - task-management
---

Break down the following task into a detailed execution plan:

## Task
- Name: {{task_name}}
- Description: {{task_description}}
- Priority: {{priority}}
- Deadline: {{deadline}}

## Decomposition

Break the task into subtasks (each should be independently completable and verifiable):

### Subtask 1: {{subtask_1_name}}
- Description: {{subtask_1_description}}
- Estimated effort: {{subtask_1_effort}}
- Dependencies: {{subtask_1_dependencies}}
- Verification criteria: {{subtask_1_verification}}
- Owner: {{subtask_1_owner}}

### Subtask 2: {{subtask_2_name}}
- Description: {{subtask_2_description}}
- Estimated effort: {{subtask_2_effort}}
- Dependencies: {{subtask_2_dependencies}}
- Verification criteria: {{subtask_2_verification}}
- Owner: {{subtask_2_owner}}

### Subtask N: {{subtask_N_name}}
...

## Dependency Graph
```
{{dependency_graph}}
```

## Risk Assessment
- Identified risks: {{risks}}
- Mitigation strategies: {{mitigations}}
- Contingency plan: {{contingency}}

## Resource Requirements
- Skills needed: {{skills_needed}}
- Tools/environment: {{tools_needed}}
- External inputs: {{external_inputs}}

## Validation Plan
- How will the completed task be verified? {{verification_plan}}
- Acceptance criteria: {{acceptance_criteria}}
