---
id: obs-success-rate-log
version: 1.0.0
confidence: 0.90
success_rate: 0.89
last_updated: 2026-06-29
tags: [observability, success-rate, tracking, metrics]
---

# Success Rate Log

Defines how success_rate is logged, tracked, updated, and aggregated across the framework.

## What Success Rate Measures

Success rate is a float between 0.0 and 1.0 representing the proportion of successful outcomes when a skill, template, or knowledge artifact is applied.

## Per-Skill Tracking

Each skill tracks its own success rate independently:

```yaml
skill_stats:
  skill_id: recall
  total_invocations: 42
  successful: 38
  failed: 4
  success_rate: 0.9048
  rolling_window: 20
  window_successes: 18
  window_failures: 2
  window_success_rate: 0.90
  last_updated: 2026-06-29
```

### Success Criteria for Skills

| Skill | Success Definition |
|-------|-------------------|
| recall | Relevant memories retrieved and applied correctly |
| plan | Plan followed without major deviations; task completed |
| reflect | Actionable insights captured; confidence calibrated |
| learn | Knowledge correctly extracted and saved |
| improve | Skill measurably better after update |
| review | Issues found before they reached production |
| compress | Knowledge condensed without losing critical info |
| index | All valid files indexed without errors |
| debug | Root cause identified and fix verified |
| estimate | Actual effort within 20% of estimate |

## Rolling Window

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Window type | Sliding time + event count | Combines recency and volume |
| Default window | Last 20 invocations | Smooths noise while reflecting recent performance |
| Minimum data points | 5 | Below this, window = total invocations |
| Window reset | Never | Accumulates for trend analysis |

## Update Frequency

| Trigger | Update | Scope |
|---------|--------|-------|
| After each skill invocation | Immediate | Per-skill counter |
| After each `reflect` | Immediate | Task-level |
| On framework startup | Load from persisted file | Global cache |
| On cron schedule (daily) | Aggregate and persist | All records |

## Aggregation

### By Skill
```
success_rate_by_skill = successful_count / total_invocations
window_success_rate = window_successes / (window_successes + window_failures)
```

### By Content Type
```
type_success_rate = sum(successful over type) / sum(total over type)
```

### Global
```
global_success_rate = sum(all successful) / sum(all total)
```

### Trend
```
trend = current_window_rate - previous_window_rate
Positive trend = improving, negative trend = degrading
```

## Persistence

Data is stored in `.ai/observability/success-rate-data.json`:

```json
{
  "skills": {
    "recall": { "total": 42, "successful": 38, "failed": 4, "window": [1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1] },
    "reflect": { "total": 30, "successful": 28, "failed": 2, "window": [1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1] }
  },
  "last_updated": "2026-06-29T12:00:00Z"
}
```

## Reporting

Success rate data is surfaced via the status command (e.g., `/status`):

```
Global success rate: 0.89 (89.2%)
--- Per Skill ---
recall:   38/42  (90.5%) — trending up
reflect:  28/30  (93.3%) — steady
plan:     25/30  (83.3%) — trending down
```
