---
id: state-management
version: 2.0.0
confidence: 0.75
success_rate: 0.70
last_updated: 2026-06-29
tags:
  - frontend
  - state
  - patterns
  - flexible
---

# State Management

> Flexible skill. Choose and implement state management patterns based on application complexity. From local component state to global stores, use the right tool for the scope.

## Overview

State management is the discipline of managing application data, its transformations, and its synchronization with the UI. The goal is predictable, debuggable, and performant data flow. Start with the simplest approach and add complexity only when the current approach hurts.

**Core Principle**: State should live as close as possible to where it is used. Lift state up only when necessary; push state down when possible.

## Step-by-Step Process

### Phase 1: Classify State Types
1. **Local state**: Form inputs, toggle states, UI interactions. Use component state (useState, this.state).
2. **Shared state**: Data consumed by multiple sibling components. Lift state to the common parent.
3. **Global state**: Data consumed across the app (auth user, theme, language). Use context or a state library.
4. **Server state**: Data from API calls. Cache, synchronize, and invalidate. Use React Query, SWR, RTK Query.
5. **URL state**: Current page, filters, search query. Store in the URL. It's bookmarkable and shareable.

### Phase 2: Choose the Pattern
- **Lifting state**: Suitable for 2-3 related components. No library needed.
- **Context**: Suitable for "global" data that changes rarely (theme, locale, auth).
- **Redux/Zustand**: Suitable for complex global state with frequent updates and middleware needs.
- **React Query/SWR**: Always for server state. Do not duplicate server state in a global store.

### Phase 3: Implement Immutable Updates
1. Never mutate state directly. Create new objects/arrays for each update.
2. Use spread operators, `map`, `filter`, `slice` for immutable operations.
3. For deeply nested state: use Immer, or normalize the state shape.
4. Avoid copying large state trees unnecessarily. Use selectors for derived data.

### Phase 4: Side Effects
1. Side effects (API calls, timers, analytics) should be separate from state logic.
2. Use middleware (Redux Thunk/Saga, Zustand middleware) or hooks.
3. Side effects should be idempotent where possible.
4. Handle loading, error, and success states for every async operation.

## Common Mistakes

- **Everything in global state**: Local state in a global store causes unnecessary re-renders and coupling. Use the minimum scope.
- **Mutating state directly**: Direct mutation skips reactivity, making the UI out of sync with data.
- **Duplicating server state**: Server data in global store becomes stale. Use a caching layer instead.
- **Over-normalization**: Flattening state so aggressively that simple reads require complex selectors.
- **Ignoring stale data**: Without cache invalidation, users see outdated information. Always set a stale time or refetch strategy.

## Quality Gates

- [ ] State is classified by scope (local/shared/global/server/URL) before implementation.
- [ ] All state updates are immutable (no direct mutations).
- [ ] Server state is managed separately from UI state (no duplicating API responses in global store).
- [ ] Async operations have loading, error, and success states.
- [ ] Re-renders are scoped to components that consume the changed state (no parent re-renders).
