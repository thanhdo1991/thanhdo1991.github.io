---
id: root-cause-v1
version: 1.0.0
confidence: 0.85
success_rate: 0.78
last_updated: 2026-06-29
tags:
  - prompt
  - analysis
  - debugging
  - root-cause
  - 5-whys
  - investigation
---

Perform a systematic Root Cause Analysis on the following issue:

Issue: {{issue_description}}
Environment: {{environment}}
Observed behavior: {{observed_behavior}}
Expected behavior: {{expected_behavior}}

Follow this process:

## 1. Reproduce the Issue
- Step-by-step reproduction instructions:
{{reproduction_steps}}
- Confirm the issue is consistently reproducible (Y/N):
- If intermittent, document frequency and conditions:

## 2. Gather Evidence
- Logs, stack traces, error messages:
{{evidence_logs}}
- Relevant code or configuration:
{{relevant_code}}
- Recent changes (deployments, config updates, code changes):
{{recent_changes}}

## 3. Five Whys Analysis
Start with the observed symptom and ask "why" iteratively:

Why 1: {{first_why}}
  Why 2: {{second_why}}
    Why 3: {{third_why}}
      Why 4: {{fourth_why}}
        Why 5 (Root Cause): {{root_cause}}

## 4. Causal Factors
List contributing factors that enabled the root cause to manifest:
- {{causal_factor_1}}
- {{causal_factor_2}}

## 5. Verify Root Cause
- Can we create a minimal test that reproduces the issue based on the proposed root cause?
- Does fixing the root cause (not just symptoms) prevent recurrence?
- Are there other issues that would also be resolved by this fix?

## 6. Action Items
- Immediate fix: {{immediate_fix}}
- Systemic prevention: {{systemic_prevention}}
- Monitoring/detection improvement: {{monitoring_improvement}}

## 7. Documentation
Update relevant knowledge base with:
- Root cause record
- Corrective actions taken
- Lessons learned
