---
id: performance-review
version: 2.0.0
confidence: 0.75
success_rate: 0.70
last_updated: 2026-06-29
tags:
  - quality
  - performance
  - flexible
---

# Performance Review

> Flexible skill. Systematic performance review covering benchmarks, profiling, query analysis, and resource management. Focus on measurable impact rather than micro-optimization.

## Overview

Performance reviews identify code that wastes CPU, memory, I/O, or network resources. The goal is not to optimize everything but to eliminate the few bottlenecks that matter: the 20% of code responsible for 80% of the execution time or resource consumption.

**Core Principle**: Measure before optimizing. Without profiling data, every performance guess is equally unreliable.

## Step-by-Step Process

### Phase 1: Define Performance Budget
1. Establish acceptable thresholds: P95 latency < 200ms, memory < 512MB, requests per second > 1000.
2. Identify critical paths: endpoints or operations that handle the most traffic.
3. Gather baseline measurements from production or load testing.

### Phase 2: Profile
1. CPU profiling: identify hot functions. Use flame graphs for visual analysis.
2. Memory profiling: find allocation hotspots, GC pressure, and memory leaks.
3. I/O profiling: database query latency, network round trips, file system operations.
4. Concurrency profiling: lock contention, thread pool saturation, async hot spots.

### Phase 3: Analyze Bottlenecks
- **N+1 Queries**: Look for queries in loops. Use eager loading, batching, or joins.
- **Redundant Computation**: Values computed repeatedly that could be cached or computed once.
- **Excessive Allocation**: Temporary objects created in hot paths. Object pooling or struct optimization.
- **Blocking Calls**: Synchronous I/O in async context, thread pool starvation.
- **Inefficient Algorithms**: O(n^2) where O(n log n) suffices, full table scans, unindexed queries.

### Phase 4: Optimize
1. Start with the highest-impact, lowest-risk change.
2. Apply one optimization at a time and measure the impact.
3. Verify that optimization does not change correctness.
4. Document the optimization and its measured impact.

## Common Mistakes

- **Premature optimization**: Optimizing code that runs once per hour or handles 10 requests per day. Profile first.
- **Micro-optimization**: Saving microseconds while ignoring millisecond-level database queries or network calls.
- **Optimizing without benchmarks**: A change that "feels faster" is not faster. Measure before and after.
- **Ignoring the GC**: In GC-managed languages, allocation patterns often matter more than algorithm efficiency.
- **Over-caching**: Caching adds complexity, stale data risks, and memory pressure. Cache only when measured benefit exists.

## Quality Gates

- [ ] Baseline measurements exist before any optimization.
- [ ] Each optimization is isolated and measured independently.
- [ ] Performance improvement is documented (before/after numbers).
- [ ] No change in correctness or API contract.
- [ ] Performance budget is defined and tracked in CI.
