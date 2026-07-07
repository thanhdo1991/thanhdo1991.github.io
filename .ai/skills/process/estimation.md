---
id: estimation
version: 2.0.0
confidence: 0.70
success_rate: 0.65
last_updated: 2026-06-29
tags:
  - process
  - estimation
  - planning
  - flexible
---

# Estimation

> Flexible skill. Produce reliable estimates by decomposing work, using historical data, accounting for uncertainty, and revisiting estimates as understanding improves.

## Overview

Estimation is predicting how long work will take. It is inherently uncertain, but systematic techniques produce more reliable estimates than intuition alone. The goal is not perfect accuracy (which is impossible) but actionable planning and risk management.

**Core Principle**: An estimate is a probability, not a promise. Communicate confidence levels, and revisit estimates as new information emerges.

## Step-by-Step Process

### Phase 1: Decompose the Work
1. Break the work into items that are < 2 days each.
2. Each item should have a clear definition of done: "What state is the code in when this item is complete?"
3. Identify dependencies: items that block other items, or items that can be parallelized.
4. Identify unknowns: tasks where you don't know the approach, the technology, or the constraints.

### Phase 2: Apply Historical Data
1. Look at similar past work. How long did it take? What went wrong?
2. If historical data is not available, use proxies: similar tasks, similar complexity, similar team.
3. Adjust for differences: new technology adds risk, familiar patterns reduce risk.

### Phase 3: Estimate with Confidence Intervals
1. Use three-point estimation:
   - **Optimistic (O)**: Everything goes perfectly. No interruptions, no surprises.
   - **Most Likely (M)**: Typical conditions. Normal interruptions, some unknowns.
   - **Pessimistic (P)**: Everything goes wrong. Major unknowns, blockers, rework.
2. Calculate expected time: `(O + 4M + P) / 6` (PERT weighted average).
3. Communicate the range, not the point: "2-4 days" not "3 days."

### Phase 4: Account for Risk
1. Identify risks that could increase the estimate:
   - Technical unknowns: unfamiliar library, new pattern.
   - Dependency risks: waiting on another team, external API.
   - Complexity risks: edge cases, performance requirements, scale.
2. Add a risk buffer: 20-50% depending on the number and severity of risks.
3. Separate the buffer from the base estimate. "Base estimate: 5 days. Risk buffer: 2 days."

### Phase 5: Review and Revisit
1. After each item is completed, compare actual time to estimated time.
2. Calibrate: are you consistently over or under? Adjust future estimates.
3. When new information changes the scope or approach, update the estimate.
4. Never use estimates as targets. An estimate is a prediction; a deadline is a commitment.

## Common Mistakes

- **Estimating in ideal developer hours**: Real hours include meetings, code reviews, context switches, and interrupts. Multiply by 1.5-2x.
- **Confusing estimate with commitment**: "3 days" said as an estimate becomes a deadline. Always communicate the range and confidence.
- **Anchoring bias**: The first number mentioned becomes the anchor. Avoid giving an estimate until you have decomposed and analyzed.
- **Not accounting for testing**: Testing, code review, and documentation typically add 30-50% to development time.
- **Optimism bias**: Humans consistently underestimate. Apply a calibration factor based on your historical performance.

## Quality Gates

- [ ] Work is decomposed into items smaller than 2 days.
- [ ] Each item has a clear definition of done.
- [ ] Estimate is expressed as a range (optimistic-pessimistic) or with a confidence level.
- [ ] Risks and assumptions are documented alongside the estimate.
- [ ] Historical calibration data is used or referenced.
