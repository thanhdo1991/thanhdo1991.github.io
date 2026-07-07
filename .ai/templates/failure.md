---
id: template-failure
version: 1.0.0
confidence: 0.95
success_rate: 0.91
last_updated: 2026-06-29
tags: [template, failure, analysis, learning]
---

# Failure Analysis Template

Use this template to analyze failures, incidents, or unexpected negative outcomes. The goal is systematic improvement, not blame.

## Incident Summary

- **Date:** 2026-06-29
- **Task/Project:** [Name]
- **Severity:** [Critical / Major / Minor / Cosmetic]
- **Impact:** [What was the blast radius? Who was affected?]

## What Failed?

[Describe what happened in concrete terms. Include timestamps, inputs, outputs, and observable behavior.]

## Expected vs Actual

| Aspect | Expected | Actual |
|--------|----------|--------|
| Behavior | [...] | [...] |
| Performance | [...] | [...] |
| Output | [...] | [...] |
| Time | [...] | [...] |

## Root Cause Analysis

**Immediate Cause:** [The direct trigger]

**Contributing Factors:**
1. [Factor 1] — [how it contributed]
2. [Factor 2] — [how it contributed]

**Root Cause:** [The fundamental issue — use 5 Whys or causal chain analysis]

## Timeline

| Time | Event |
|------|-------|
| T0 | [First deviation] |
| T1 | [Detection] |
| T2 | [Response started] |
| T3 | [Mitigation applied] |
| T4 | [Resolution] |

## Fix Applied

- **What:** [Description of the fix]
- **Verification:** [How the fix was confirmed]
- **Side effects:** [Any unintended consequences]

## Prevention

- **Process change:** [What process needs to change?]
- **Tooling:** [What tool/automation would catch this?]
- **Monitoring:** [What alert should exist?]
- **Training:** [What knowledge gap was exposed?]

## Lessons Learned

- [Lesson 1]
- [Lesson 2]

## Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [Action] | [Who] | [When] |
