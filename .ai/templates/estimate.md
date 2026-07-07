---
id: template-estimate
version: 1.0.0
confidence: 0.95
success_rate: 0.89
last_updated: 2026-06-29
tags: [template, estimate, planning]
---

# Estimation Template

Use this template for Three-Point Estimation (PERT) to produce realistic effort forecasts.

## Task Information

- **Task:** [Name or short description]
- **Type:** [Feature / Bug / Refactor / Research / Process / Other]
- **Assumptions:** [List key assumptions underlying the estimate]
- **Dependencies:** [List blocking dependencies]

## Complexity Assessment

| Factor | Rating (1-5) | Notes |
|--------|-------------|-------|
| Technical complexity | [1-5] | [Rationale] |
| Domain knowledge required | [1-5] | [Rationale] |
| Unknowns / research needed | [1-5] | [Rationale] |
| Integration surface area | [1-5] | [Rationale] |
| Testing effort | [1-5] | [Rationale] |

**Overall Complexity:** [Low / Medium / High / Very High]

## Three-Point Estimate

| Estimate | Definition | Value (hours) |
|----------|-----------|---------------|
| **Optimistic (O)** | Best-case scenario, everything goes right | [hours] |
| **Most Likely (M)** | Normal scenario, typical hiccups | [hours] |
| **Pessimistic (P)** | Worst-case scenario, many things go wrong | [hours] |

## Calculated Values

| Metric | Formula | Value |
|--------|---------|-------|
| **Expected (E)** | (O + 4M + P) / 6 | [hours] |
| **Standard Deviation (SD)** | (P - O) / 6 | [hours] |
| **Variance (V)** | SD^2 | [hours] |
| **95% Confidence Range** | E +/- 2*SD | [hours] - [hours] |

## Confidence

- **Confidence Level:** [Low / Medium / High]
- **Rationale:** [Why this confidence level? What would increase it?]
- **Historical accuracy for similar tasks:** [X%]

## Breakdown

| Subtask | Est. Hours | Owner | Dependencies |
|---------|-----------|-------|-------------|
| [Subtask 1] | [h] | [Who] | [Dep] |
| [Subtask 2] | [h] | [Who] | [Dep] |
| [Subtask 3] | [h] | [Who] | [Dep] |
| **Total** | **[h]** | | |

## Risks

- **[Risk 1]:** [Impact if realized] — Mitigation: [Strategy]
- **[Risk 2]:** [Impact if realized] — Mitigation: [Strategy]
