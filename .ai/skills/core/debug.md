---
id: debug
version: 2.0.0
confidence: 0.90
success_rate: 0.88
last_updated: 2026-06-29
tags:
  - core
  - debug
  - rigid
---

# Debug

> Rigid skill. Systematic debugging through the reproduce-isolate-root-cause-fix-verify cycle. No guessing, no random changes, no superstition.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "I know what the bug is, let me just fix it" | Without reproduction, you cannot verify the fix. Without isolation, you may fix a symptom, not the cause. |
| "Let me try changing this and see if it helps" | Random changes create noise. You lose the ability to tell what fixed it and what broke something else. |
| "It works on my machine" | Environment differences are part of the root cause. Investigate systematically. |
| "This is a weird one-time glitch" | "Heisenbugs" are real, but assuming one-time is a trap. Log it, monitor it, or prove it's transient. |

## Process

### Step 1: Reproduce
- Write down the exact steps to reproduce the bug. If you can't reproduce it reliably, you can't fix it.
- Note the environment: OS version, browser, device, network conditions, database state.
- For intermittent bugs, add logging and reproduce under observation.
- If truly unreproducible after 30 minutes of effort, document the evidence and escalate.

### Step 2: Isolate
- Find the minimal input, minimal code path, and minimal configuration that triggers the bug.
- Use binary search: comment out half the code path, see if the bug persists. Narrow to the file, then the function, then the line.
- For data bugs: reduce the input data to the minimum dataset that reproduces the issue.
- Write a failing test that captures the bug behavior exactly.

### Step 3: Identify Root Cause
- Ask "why" five times. The first answer is usually a symptom, not a cause.
- Distinguish between:
  - **Proximate cause**: the line of code that produced the wrong output.
  - **Root cause**: why that line was wrong (misunderstood requirement, missed edge case, wrong assumption).
- Document the root cause before touching any code.

### Step 4: Fix
- Write the minimal change that addresses the root cause.
- Do not fix cosmetic issues or refactor unrelated code in the same change.
- Verify the fix against the failing test from Step 2.

### Step 5: Verify
- Run the reproduction steps. The bug must not appear.
- Run the full test suite. No regressions.
- Ask: "Could this root cause exist elsewhere?" Search for similar patterns.

## Red Flags (STOP Signals)

- You made a change but cannot articulate how it addresses the root cause.
- The bug disappeared without a clear fix. It's still latent.
- You changed more than 5 lines to fix a single bug.
- You found yourself saying "maybe" or "perhaps" about the root cause.

## No Exceptions

- Do not make changes until you have reproduced the bug in your environment.
- Do not fix a bug you cannot explain. A fix without understanding is a future regression.
- Do not deploy a fix that was only tested against the reproduction case; run the full suite.
