---
id: debug-flow-v1
version: 1.0.0
confidence: 0.90
success_rate: 0.84
last_updated: 2026-06-29
tags:
  - prompt
  - debugging
  - troubleshooting
  - systematic
  - investigation
---

Follow this systematic debugging process. NO GUESSING -- every step must be evidence-based.

## Bug Report
- Symptom: {{symptom}}
- Environment: {{environment}}
- First observed: {{first_observed}}
- Impact: {{impact}}

## Step 1: Reproduce
- [ ] Create minimal reproduction scenario
- [ ] Document exact reproduction steps:
{{reproduction_steps}}
- [ ] Verify the bug exists in isolation (no confounding factors)

## Step 2: Isolate
- [ ] Identify the component/module where the bug manifests
- [ ] Narrow down to specific function/code block
- [ ] Determine if bug is in our code, dependency, or environment
- [ ] Binary search / bisect to find the failing change if applicable

### Current Hypothesis
{{current_hypothesis}}

### Evidence For
{{evidence_for}}

### Evidence Against
{{evidence_against}}

## Step 3: Investigate Root Cause
- [ ] Examine relevant code paths
- [ ] Check input values, state, and data flow
- [ ] Inspect logs and error messages
- [ ] Verify assumptions (do not assume -- prove each one)

### Investigation Log
| Step | Action Taken | Result |
|------|-------------|--------|
| 1    | {{action_1}} | {{result_1}} |
| 2    | {{action_2}} | {{result_2}} |

## Step 4: Hypothesize Fix
- [ ] Proposed fix: {{proposed_fix}}
- [ ] Does the fix address the root cause (not just symptoms)?
- [ ] What side effects could this fix introduce?
- [ ] Write a test that reproduces the bug first, then apply the fix

## Step 5: Implement Fix
- [ ] Apply the minimal change needed
- [ ] Ensure existing tests still pass
- [ ] Add regression test for this bug
- [ ] Update relevant documentation

## Step 6: Verify
- [ ] Bug is no longer reproducible
- [ ] Related functionality still works (sanity check)
- [ ] Performance impact assessed
- [ ] Edge cases covered

## Step 7: Document
- [ ] Root cause recorded in knowledge base
- [ ] Debugging process archived for future reference
- [ ] Related patterns documented if applicable
