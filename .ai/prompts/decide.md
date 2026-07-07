---
id: decide-v1
version: 1.0.0
confidence: 0.86
success_rate: 0.80
last_updated: 2026-06-29
tags:
  - prompt
  - decision
  - trade-off-analysis
  - strategy
  - evaluation
---

Make a structured decision on the following:

## Decision Context
- Decision to make: {{decision_question}}
- Context/background: {{background}}
- Deadline: {{deadline}}
- Decision maker: {{decision_maker}}

## Options

### Option A: {{option_a_name}}
- Description: {{option_a_description}}
- Effort: {{option_a_effort}}
- Risk level: {{option_a_risk}}
- Key benefit: {{option_a_benefit}}
- Key drawback: {{option_a_drawback}}

### Option B: {{option_b_name}}
- Description: {{option_b_description}}
- Effort: {{option_b_effort}}
- Risk level: {{option_b_risk}}
- Key benefit: {{option_b_benefit}}
- Key drawback: {{option_b_drawback}}

### Option C: {{option_c_name}}
- Description: {{option_c_description}}
- Effort: {{option_c_effort}}
- Risk level: {{option_c_risk}}
- Key benefit: {{option_c_benefit}}
- Key drawback: {{option_c_drawback}}

## Evaluation Criteria
| Criterion | Weight (1-5) | Option A | Option B | Option C |
|-----------|-------------|----------|----------|----------|
| {{criterion_1}} | {{weight_1}} | {{a_score_1}} | {{b_score_1}} | {{c_score_1}} |
| {{criterion_2}} | {{weight_2}} | {{a_score_2}} | {{b_score_2}} | {{c_score_2}} |
| {{criterion_3}} | {{weight_3}} | {{a_score_3}} | {{b_score_3}} | {{c_score_3}} |

## Trade-off Analysis
- Must-have requirements: {{must_have}}
- Nice-to-have: {{nice_to_have}}
- Deal-breakers: {{deal_breakers}}

## Recommendation
- Recommended option: {{recommended_option}}
- Rationale: {{rationale}}
- Confidence in recommendation: {{confidence_level}}

## Implementation
- Next steps: {{next_steps}}
- Success criteria for this decision: {{success_criteria}}
- Review date: {{review_date}}
