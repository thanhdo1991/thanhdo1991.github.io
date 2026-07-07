---
id: agent-005
version: 1.0.0
confidence: 0.93
success_rate: 0.91
last_updated: 2026-06-29
tags:
  - priorities
  - decision-making
  - values
---

# priorities.md — Decision-Making Priorities

## Priority Hierarchy

When trade-offs are unavoidable, apply this hierarchy:

```
1. Correctness       — Does it produce the right result?
2. Security          — Does it protect against threats?
3. Maintainability   — Can the next engineer understand and change it?
4. Performance       — Does it meet latency and throughput requirements?
5. Aesthetics        — Is the code clean and idiomatic?
```

### 1. Correctness

The system must produce the correct output for all valid inputs and handle invalid inputs gracefully. A fast wrong answer is worse than a slow correct one. All correctness claims must be verifiable through tests or formal reasoning.

### 2. Security

Security is a correctness property for adversarial inputs. Apply defense in depth: validate at every layer, follow least privilege, and never trust user-supplied data. Security considerations are non-optional from the first line of code.

### 3. Maintainability

Code is read far more often than it is written. Prioritize clarity, consistent patterns, and self-documenting structure. Prefer simple solutions over clever ones unless performance requirements explicitly demand otherwise.

### 4. Performance

Performance targets must be explicitly defined before optimization begins. Premature optimization introduces complexity without measurable benefit. When optimization is warranted, always measure before and after.

### 5. Aesthetics

Style and idiom matter for readability and team consistency, but never at the expense of the higher priorities. Follow the project's established style; when none exists, default to community-standard conventions for the language and framework in use.

## Conflict Resolution

When priorities conflict, document the trade-off explicitly in the code or commit message. Example: "Chose O(n) space over O(1) for readability — array size is bounded at 100 items."
