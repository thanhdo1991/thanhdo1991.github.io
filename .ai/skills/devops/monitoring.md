---
id: monitoring
version: 2.0.0
confidence: 0.75
success_rate: 0.70
last_updated: 2026-06-29
tags:
  - devops
  - monitoring
  - observability
  - flexible
---

# Monitoring

> Flexible skill. Design and implement monitoring covering logs, metrics, traces, alerts, and dashboards. Observability is not tooling; it is the ability to understand the system's internal state from its outputs.

## Overview

Monitoring is the practice of collecting, analyzing, and acting on data about your system's behavior. Good monitoring tells you what is happening (logs), what is slow or failing (metrics), and why (traces). The goal is to reduce time-to-detection and time-to-understanding of production issues.

**Core Principle**: Monitor what you would want to know during an incident, not what is easy to measure. If you can't measure it, you can't improve it.

## Step-by-Step Process

### Phase 1: Define Signals
1. **Latency**: Response times for critical endpoints. Track P50, P95, P99.
2. **Traffic**: Requests per second, active users, connections.
3. **Errors**: HTTP 5xx, application exceptions, failed jobs.
4. **Saturation**: CPU, memory, disk I/O, connection pool usage, queue depth.
5. **Business**: Orders placed, users registered, payments processed.

### Phase 2: Logging Strategy
1. All logs are structured JSON. No free-text log messages that can't be parsed.
2. Every log line includes: timestamp, service name, environment, correlation ID, log level.
3. Levels: DEBUG (development), INFO (normal operation), WARN (potential issue), ERROR (failure), FATAL (service down).
4. No sensitive data in logs: PII, passwords, tokens, credit card numbers.

### Phase 3: Metrics Collection
1. Use RED method for request-driven services: Rate (requests/sec), Errors (failed requests/sec), Duration (latency distribution).
2. Use USE method for resources: Utilization, Saturation, Errors.
3. Define SLIs (Service Level Indicators) and SLOs (Service Level Objectives).
4. Collect metrics every 10-15 seconds. Longer intervals miss spikes.

### Phase 4: Alerting
1. Every alert must have a runbook: what to check, who to contact, how to respond.
2. Alert on symptoms (user-facing errors, high latency), not causes (high CPU).
3. No alert fatigue: every page should require human action. If no action is needed, it's a notification, not an alert.
4. Use escalation policies: first responder -> team lead -> on-call manager.

### Phase 5: Dashboards
1. Create dashboards per audience: engineering (detailed), operations (summary), management (business).
2. Every dashboard has a clear title and purpose. No "miscellaneous" dashboards.
3. Show trend lines, not just current values. A single number is noise; a trend is signal.

## Common Mistakes

- **Monitoring everything without context**: Collecting data without knowing what's normal creates noise. Define baselines first.
- **Dashboards without purpose**: If looking at a dashboard doesn't tell you whether the system is healthy, it's decoration.
- **Alerting on every metric**: Alerts that fire constantly are ignored. Alert on user impact, not infrastructure noise.
- **No alert runbooks**: An alert that goes off at 3 AM with no runbook is a panic, not a procedure.
- **Logging only in error paths**: Log the happy path too. Knowing what normally happens helps identify anomalies.

## Quality Gates

- [ ] Every service has at least latency, error rate, and request rate metrics.
- [ ] All production logs are structured and searchable in a centralized system.
- [ ] Every alert has a runbook linked in the alert notification.
- [ ] Dashboard shows service health at a glance (green/yellow/red).
- [ ] No PII or secrets in any log output (verified by scan).
