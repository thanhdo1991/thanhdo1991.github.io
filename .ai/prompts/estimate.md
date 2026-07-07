---
id: estimate-v1
version: 1.0.0
confidence: 0.82
success_rate: 0.73
last_updated: 2026-06-29
tags:
  - prompt
  - estimation
  - planning
  - effort
  - project-management
---

Produce an effort estimate for the following work:

## Work Description
- Task: {{task_name}}
- Description: {{task_description}}
- Work type: {{work_type}} (new feature / bugfix / refactor / research / documentation)

## Decomposition
Break the work into granular, independently estimable units:

| Sub-task | Description | Complexity (S/M/L) | Estimated Hours | Confidence | Dependencies |
|----------|-------------|--------------------|----------------|------------|-------------|
| {{subtask_1}} | {{desc_1}} | {{complexity_1}} | {{hours_1}} | {{confidence_1}} | {{deps_1}} |
| {{subtask_2}} | {{desc_2}} | {{complexity_2}} | {{hours_2}} | {{confidence_2}} | {{deps_2}} |
| {{subtask_3}} | {{desc_3}} | {{complexity_3}} | {{hours_3}} | {{confidence_3}} | {{deps_3}} |

## Historical Benchmarking
Similar past tasks:
| Past Task | Actual Effort | Similarity | Notes |
|-----------|--------------|-----------|-------|
| {{past_task_1}} | {{actual_1}} | {{similarity_1}} | {{notes_1}} |
| {{past_task_2}} | {{actual_2}} | {{similarity_2}} | {{notes_2}} |

## Estimation Method
- Technique used: {{estimation_technique}} (e.g., PERT, Delphi, analogy, parametric)
- If PERT: Optimistic={{optimistic}}, Most Likely={{most_likely}}, Pessimistic={{pessimistic}}
- Expected (E) = {{expected_value}}
- Standard deviation: {{std_dev}}

## Confidence Intervals
- 50% confidence (P50): {{p50}} hours
- 75% confidence (P75): {{p75}} hours
- 90% confidence (P90): {{p90}} hours
- 95% confidence (P95): {{p95}} hours

## Risk Adjustments
- Risk factors that could increase effort: {{risk_factors}}
- Buffer added: {{buffer}} hours ({{buffer_percent}}%)
- Total estimate with buffer: {{total_with_buffer}}

## Recommendation
- Recommended estimate: {{recommended_estimate}}
- Confidence level: {{estimate_confidence}}
- Recommended approach to reduce uncertainty: {{uncertainty_reduction}}
