---
id: workflow-incident-response-001
version: 1.0.0
confidence: 0.84
success_rate: 0.78
last_updated: 2026-06-29
tags: [workflow, incident, operations]
---

# Incident Response Workflow

Structured process for detecting, triaging, mitigating, and learning from incidents.

## Flowchart

```
[Incident Detected] → [Triage: Assess Severity]
    → [Sev1: Critical] → [Immediate Response: Pager/Alert Team]
    → [Sev2: High] → [Respond Within SLA]
    → [Sev3+: Low] → [Schedule for Normal Hours]
    → [Mitigate: Stop the Bleeding]
    → [Root Cause Analysis] → [Implement Permanent Fix]
    → [Verify Fix] → [Postmortem: Write Incident Report]
    → [Update: Memory + Playbooks + Monitoring]
    → [Done]
```

## Trigger

- Monitoring alert fires (error rate spike, latency spike, disk full, etc.).
- User reports a production outage or severe degradation.
- Security incident is discovered.
- CI/CD pipeline fails in a way that blocks all deployments.
- Dependency service outage affects availability.

## Steps

### 1. Detect
- **Input**: Alert, user report, monitoring dashboard anomaly.
- **Process**: Confirm the incident is real (not a false alarm). Capture the initial state: time, affected component, impact scope (users, features, regions), error signatures.
- **Output**: Incident confirmed with initial impact assessment.
- **Quality Gate**: Detection within the monitoring SLO (e.g., alert fires within 5 minutes of anomaly). False alarms are identified quickly to avoid wasting response time.

### 2. Triage Severity
- **Input**: Initial impact assessment.
- **Process**: Classify severity using a predefined matrix:
  - **Sev1 (Critical)**: Complete service outage, data loss, security breach. All users affected. No workaround.
  - **Sev2 (High)**: Major feature degraded. Significant subset of users affected. Workaround is partial or painful.
  - **Sev3 (Medium)**: Minor feature degraded. Small subset of users affected. Workaround exists.
  - **Sev4 (Low)**: Cosmetic issue. No functional impact. Single user affected.
- **Output**: Severity classification with rationale.
- **Decision Point**: `[Sev1?] → [Immediate response: assemble team, page on-call, start war room] | [Sev2?] → [Respond within SLA (e.g., 1 hour)] | [Sev3+?] → [Log for next business day]`.
- **Quality Gate**: Severity is based on actual user impact, not just technical symptoms. Over-classification (calling everything Sev1) is as bad as under-classification. Err on the side of higher severity initially — it can be downgraded later.

### 3. Mitigate
- **Input**: Severity classification, incident context.
- **Process**: Take immediate action to reduce or eliminate user impact. Options: rollback the recent deployment, feature flag off the problematic feature, scale up resources, block malicious traffic, restart service, fail over to redundant infrastructure. Mitigation is NOT fixing the root cause — it's stopping the bleeding.
- **Output**: Incident mitigated (users no longer impacted).
- **Quality Gate**: Mitigation is confirmed by monitoring (error rate back to baseline, traffic restored, etc.). The mitigation action is documented (what was done, by whom, at what time). If the mitigation has side effects (e.g., feature flag disables a feature), those are communicated.

### 4. Root Cause Analysis
- **Input**: Incident timeline, logs, metrics, deployment history, code changes.
- **Process**: Investigate the root cause. Use the 5 Whys technique. Distinguish between trigger (the event that started it) and root cause (the systemic issue that allowed it). Consider: code change, configuration change, infrastructure failure, dependency failure, human error, process gap.
- **Output**: Root cause statement with evidence.
- **Quality Gate**: Root cause is supported by evidence (logs, metrics, code review). Multiple hypotheses were considered and eliminated. The root cause is systemic enough that fixing it prevents similar incidents.

### 5. Implement Permanent Fix
- **Input**: Root cause statement.
- **Process**: Design and implement a fix that addresses the root cause, not just the symptom. Apply the bugfix workflow (see bugfix.md). Ensure the fix includes monitoring improvements to detect recurrence faster.
- **Output**: Code/configuration fix.
- **Quality Gate**: Fix is tested in a non-production environment. Fix includes a regression test (see bugfix.md step 6). Fix does not rely on the mitigation (feature flags, rollback) remaining in place.

### 6. Verify Fix
- **Input**: Fix deployed to production (or staging for non-critical).
- **Process**: Confirm the fix resolves the issue. Run the original reproduction scenario. Monitor the relevant metrics for the incident duration window. Confirm the mitigation can be reverted (e.g., feature flag turned back on).
- **Output**: Verification result.
- **Quality Gate**: Same monitoring signals that detected the incident are green. The mitigation is removed only after the fix is confirmed effective. If the fix doesn't work, revert and go back to analysis.

### 7. Postmortem
- **Input**: Full incident timeline, root cause, fix, mitigation actions, communications.
- **Process**: Write a blameless postmortem report covering: (a) summary, (b) timeline, (c) impact, (d) root cause, (e) mitigation, (f) fix, (g) what went well, (h) what went wrong, (i) action items with owners. Focus on systemic improvements, not individual blame.
- **Output**: Postmortem document.
- **Quality Gate**: Postmortem is written within 48 hours of incident resolution (or agreed timeline). Action items are specific, measurable, and have owners. No blame language. The postmortem is shared with the team.

### 8. Update
- **Input**: Postmortem, action items.
- **Process**: Update memory with the incident pattern (patterns.md). Update the incident response playbook if gaps were found. Update monitoring and alerting based on lessons learned. Create tracking tasks for action items.
- **Output**: Updated memory, playbooks, monitoring configuration.
- **Quality Gate**: Action items are tracked (not just documented). Monitoring coverage is improved if the incident was detected by user report rather than by monitoring. The playbook is updated if the response revealed gaps.

## Output

- Incidents mitigated and resolved.
- Root cause analysis.
- Permanent fix deployed.
- Postmortem document.
- Action items with owners.
- Updated memory and playbooks.
