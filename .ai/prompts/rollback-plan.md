---
id: rollback-plan-v1
version: 1.0.0
confidence: 0.86
success_rate: 0.79
last_updated: 2026-06-29
tags:
  - prompt
  - rollback
  - disaster-recovery
  - operations
  - contingency
  - recovery
---

Create a comprehensive rollback plan:

## Deployment/Change Information
- Change description: {{change_description}}
- Change ID/ticket: {{change_id}}
- Deployed at: {{deploy_time}}
- Deployed by: {{deployed_by}}
- Components affected: {{affected_components}}

## Rollback Triggers
Execute rollback if any of the following conditions are met:
- {{trigger_condition_1}}
- {{trigger_condition_2}}
- {{trigger_condition_3}}

## Pre-Rollback Checklist
Before initiating rollback, verify:
- [ ] Rollback decision approved by: {{approver}}
- [ ] Stakeholders notified: {{stakeholders_notified}}
- [ ] Current state snapshot captured (logs, metrics, data): {{state_snapshot}}
- [ ] Rollback script/binaries ready and verified: {{rollback_artifacts_ready}}
- [ ] Database backup verified: {{database_backup_verified}}
- [ ] Communication channel open for status updates: {{communication_channel}}

## Rollback Procedure

### Step 1: {{rollback_step_1_name}}
- Action: {{rollback_step_1_action}}
- Command/script: {{rollback_step_1_command}}
- Expected duration: {{rollback_step_1_duration}}
- Expected outcome: {{rollback_step_1_outcome}}

### Step 2: {{rollback_step_2_name}}
- Action: {{rollback_step_2_action}}
- Command/script: {{rollback_step_2_command}}
- Expected duration: {{rollback_step_2_duration}}
- Expected outcome: {{rollback_step_2_outcome}}

### Step 3: {{rollback_step_3_name}}
- Action: {{rollback_step_3_action}}
- Command/script: {{rollback_step_3_command}}
- Expected duration: {{rollback_step_3_duration}}
- Expected outcome: {{rollback_step_3_outcome}}

## Data Integrity Verification
After rollback, verify:
- [ ] Data consistency check: {{data_consistency_check}}
- [ ] Database integrity (no corruption, referential integrity): {{db_integrity_check}}
- [ ] Data volume matches pre-deployment baseline: {{data_volume_check}}
- [ ] Transaction logs consistent: {{transaction_log_check}}
- [ ] User data not lost or corrupted: {{user_data_check}}

## System Verification
- [ ] Application health endpoint returns healthy: {{health_check}}
- [ ] All services are running: {{service_status}}
- [ ] Core functionality verified:
  - {{core_check_1}}
  - {{core_check_2}}
- [ ] Performance metrics back to baseline: {{performance_check}}
- [ ] Error rates normal: {{error_rate_check}}

## Post-Rollback Actions
- [ ] Root cause investigation started: {{rca_started}}
- [ ] Incident report created: {{incident_report}}
- [ ] Communication sent to stakeholders: {{stakeholder_communication}}
- [ ] Blockers identified to prevent re-deployment of same issue: {{blockers_identified}}
- [ ] Lessons learned documented: {{lessons_learned}}
- [ ] Re-deploy plan (after fix): {{redeploy_plan}}
