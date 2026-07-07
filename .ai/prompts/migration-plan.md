---
id: migration-plan-v1
version: 1.0.0
confidence: 0.85
success_rate: 0.77
last_updated: 2026-06-29
tags:
  - prompt
  - migration
  - planning
  - deployment
  - operations
  - transition
---

Create a detailed migration plan:

## Migration Overview
- Title: {{migration_title}}
- Reason for migration: {{migration_reason}}
- Requestor: {{requestor}}
- Owner: {{owner}}

## Current State (As-Is)
- Current system/version: {{current_system}}
- Architecture overview: {{current_architecture}}
- Data volume: {{current_data_volume}}
- Dependencies: {{current_dependencies}}
- Known limitations: {{current_limitations}}

## Target State (To-Be)
- Target system/version: {{target_system}}
- Architecture overview: {{target_architecture}}
- Key improvements: {{target_improvements}}
- New dependencies: {{new_dependencies}}

## Migration Steps

### Pre-Migration
- [ ] {{pre_step_1}}
- [ ] {{pre_step_2}}
- [ ] Communication plan: {{communication_plan}}

### Step 1: {{step_1_name}}
- Description: {{step_1_description}}
- Duration estimate: {{step_1_duration}}
- Success criteria: {{step_1_criteria}}
- Rollback step: {{step_1_rollback}}

### Step 2: {{step_2_name}}
- Description: {{step_2_description}}
- Duration estimate: {{step_2_duration}}
- Success criteria: {{step_2_criteria}}
- Rollback step: {{step_2_rollback}}

### Step 3: {{step_3_name}}
- Description: {{step_3_description}}
- Duration estimate: {{step_3_duration}}
- Success criteria: {{step_3_criteria}}
- Rollback step: {{step_3_rollback}}

### Post-Migration
- [ ] {{post_step_1}}
- [ ] {{post_step_2}}
- [ ] Verification period: {{verification_period}}

## Rollback Plan
- Trigger conditions: {{rollback_triggers}}
- Rollback procedure: {{rollback_procedure}}
- Rollback duration estimate: {{rollback_duration}}
- Data integrity check post-rollback: {{data_integrity_check}}

## Validation
- Performance benchmarks: {{performance_benchmarks}}
- Functional tests: {{functional_tests}}
- Data integrity checks: {{data_integrity_checks}}
- Smoke tests: {{smoke_tests}}
- Monitoring dashboards: {{monitoring_dashboards}}

## Risk Assessment
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| {{risk_1}} | {{prob_1}} | {{impact_1}} | {{mitigation_1}} |
| {{risk_2}} | {{prob_2}} | {{impact_2}} | {{mitigation_2}} |

## Communication
- Stakeholders: {{stakeholders}}
- Status updates: {{status_updates}}
- Escalation path: {{escalation_path}}
