---
id: obs-confidence-tracking
version: 1.0.0
confidence: 0.90
success_rate: 0.88
last_updated: 2026-06-29
tags: [observability, confidence, tracking, metrics]
---

# Confidence Tracking

Defines how confidence scores are assessed, tracked, and updated over time across all framework artifacts.

## What Confidence Measures

Confidence represents the assessed reliability, accuracy, and trustworthiness of a piece of knowledge or a skill. It is a float between 0.0 (no confidence) and 1.0 (maximum confidence).

## Confidence Level Meanings

| Range | Label | Meaning |
|-------|-------|---------|
| 0.00 - 0.25 | **Speculative** | Untested, theoretical, newly created. Likely contains gaps. |
| 0.26 - 0.50 | **Tentative** | Partially validated but not yet proven reliable in practice. |
| 0.51 - 0.75 | **Moderate** | Tested multiple times with reasonable success. Reasonable to rely on. |
| 0.76 - 0.90 | **High** | Well-tested, consistently reliable. Trustworthy for decision-making. |
| 0.91 - 1.00 | **Established** | Extensively validated, widely used, minimal failure rate. Gold standard. |

## Initial Confidence Assignment

| Artifact Type | Default Initial Confidence | Rationale |
|--------------|---------------------------|-----------|
| New template | 0.95 | Best practices, production-grade from design |
| New skill | 0.70 | Untested in this environment |
| New reflection | 0.80 | Subjective but based on actual experience |
| New decision (ADR) | 0.75 | Well-reasoned but untested |
| New pattern | 0.85 | Based on established literature |
| New failure analysis | 0.90 | Root-caused with action items |
| AI-generated suggestions | 0.40 | Requires human validation |

## Update Rules

Confidence is updated under these conditions:

### After Successful Use (+)
- +0.05 if the artifact was used and produced correct/reliable results
- +0.10 if used in a high-stakes context and succeeded
- +0.02 if the artifact was retrieved by RAG and found useful

### After Failed Use (-)
- -0.15 if the artifact led to incorrect results or bad decisions
- -0.10 if the artifact was used but produced no measurable benefit

### By Human Validation
- +0.20 when a human explicitly reviews and approves
- -0.30 when a human explicitly marks as incorrect

## Decay Over Time

Confidence decays if an artifact is not used or updated:

| Time Since Last Update | Decay Amount | Notes |
|----------------------|-------------|-------|
| 30 days | -0.02 | Minimal decay |
| 90 days | -0.05 | Noticeable staleness |
| 180 days | -0.10 | Should prompt review |
| 365 days | -0.20 | Likely out of date |
| >365 days | -0.30 | Archive or re-validate |

**Decay floor:** Confidence will not decay below 0.10 automatically. Manual review is required below that threshold.

## Recording Process

Each confidence change is recorded as an event:

```yaml
confidence_event:
  artifact_id: reflection-20260629-001
  previous_confidence: 0.80
  new_confidence: 0.85
  delta: +0.05
  reason: "Successfully applied to task X with correct outcome"
  timestamp: 2026-06-29T14:30:00Z
  trigger: successful_use
```

## Aggregation

For aggregated confidence statistics across the framework:

- **Mean confidence:** Average across all indexed artifacts
- **Weighted confidence:** Weighted by use_count (more-used = more weight)
- **Confidence by content type:** Separate averages per type
- **Trend:** Weekly delta in mean confidence
