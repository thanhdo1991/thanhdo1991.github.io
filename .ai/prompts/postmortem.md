---
id: postmortem-v1
version: 1.0.0
confidence: 0.89
success_rate: 0.82
last_updated: 2026-06-29
tags:
  - prompt
  - postmortem
  - incident
  - retrospective
  - learning
  - blameless
---

Conduct an incident postmortem:

## Incident Overview
- Incident title: {{incident_title}}
- Incident ID: {{incident_id}}
- Date: {{incident_date}}
- Duration: {{incident_duration}}
- Severity: {{severity}} (P0/Critical / P1/Major / P2/Minor / P3/Cosmetic)
- Reported by: {{reported_by}}
- Reported via: {{reported_via}}

## Timeline
| Time (UTC) | Event | Action Taken |
|------------|-------|-------------|
| {{time_1}} | {{event_1}} | {{action_1}} |
| {{time_2}} | {{event_2}} | {{action_2}} |
| {{time_3}} | {{event_3}} | {{action_3}} |
| {{time_4}} | {{event_4}} | {{action_4}} |

## Impact
- Users affected: {{users_affected_count}} ({{users_affected_description}})
- Services affected: {{services_affected}}
- Data loss/corruption: {{data_loss}}
- Financial impact: {{financial_impact}}
- Reputational impact: {{reputational_impact}}
- SLA breach: {{sla_breach}} (Y/N - details: {{sla_details}})

## Root Cause
{{root_cause_description}}

### Contributing Factors
- {{contributing_factor_1}}
- {{contributing_factor_2}}

### Trigger
{{trigger_event_description}}

## Detection
- How was the issue first detected? {{detection_method}}
- Time from introduction to detection: {{time_to_detection}}
- Time from detection to mitigation: {{time_to_mitigation}}
- Could detection have been faster? {{detection_improvement}}

## Resolution
- What resolved the incident? {{resolution_description}}
- Was the fix permanent or temporary? {{fix_permanence}}
- Verification steps: {{verification_steps}}

## What Went Well
{{what_went_well}}

## What Went Wrong
{{what_went_wrong}}

## Where We Got Lucky
{{where_we_got_lucky}}

## Action Items

### Immediate (within 24 hours)
- [ ] {{immediate_action_1}} | Owner: {{immediate_owner_1}} | Due: {{immediate_due_1}}
- [ ] {{immediate_action_2}} | Owner: {{immediate_owner_2}} | Due: {{immediate_due_2}}

### Short-term (within 1 week)
- [ ] {{short_term_action_1}} | Owner: {{short_term_owner_1}} | Due: {{short_term_due_1}}
- [ ] {{short_term_action_2}} | Owner: {{short_term_owner_2}} | Due: {{short_term_due_2}}

### Long-term (within 1 month)
- [ ] {{long_term_action_1}} | Owner: {{long_term_owner_1}} | Due: {{long_term_due_1}}
- [ ] {{long_term_action_2}} | Owner: {{long_term_owner_2}} | Due: {{long_term_due_2}}

## Prevention Plan
- Systemic fix: {{systemic_fix}}
- Monitoring improvements: {{monitoring_improvements}}
- Testing improvements: {{testing_improvements}}
- Documentation updates: {{documentation_updates}}
- Process changes: {{process_changes}}

## Blameless Statement
This postmortem is a blameless analysis. The goal is to learn and improve our systems and processes, not to assign fault. All contributors acted in good faith with the information available at the time.

## Knowledge Integration
- [ ] Root cause and resolution documented in knowledge base
- [ ] Runbook updated for this scenario
- [ ] Monitoring alert thresholds adjusted if needed
- [ ] Related skills updated
- [ ] Postmortem shared with team
