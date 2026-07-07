---
id: api-integration
version: 2.0.0
confidence: 0.80
success_rate: 0.76
last_updated: 2026-06-29
tags:
  - frontend
  - api
  - integration
  - flexible
---

# API Integration

> Flexible skill. Integrate frontend applications with backend APIs reliably. Cover error handling, loading states, caching, retry logic, and optimistic updates.

## Overview

API integration is the bridge between the frontend and backend. A robust integration handles network failures, slow responses, stale data, and race conditions. The user should never see a blank screen, a spinner that runs forever, or inconsistent data.

**Core Principle**: Treat the API as an unreliable resource. Every call can fail, every response can be delayed, and every cache can be stale. Design for failure.

## Step-by-Step Process

### Phase 1: Define API Client
1. Create a single API client instance with base URL, headers, and authentication.
2. Use interceptors for:
   - Adding auth tokens to requests.
   - Refreshing expired tokens on 401 responses.
   - Logging request/response timing.
   - Transforming error responses to standardized error objects.
3. Set reasonable timeouts (default 10s for reads, 30s for mutations).

### Phase 2: Error Handling
1. Categorize errors:
   - **Network error**: No internet, DNS failure, connection refused.
   - **Client error**: 4xx responses (bad request, unauthorized, not found).
   - **Server error**: 5xx responses (internal error, service unavailable).
   - **Timeout**: Request exceeded the timeout limit.
2. For each category, define user-facing messaging and recovery actions:
   - Network: "No internet connection. Retrying..." with retry button.
   - 4xx: Display the server's error message (or a generic one).
   - 5xx: "Something went wrong. Please try again." with auto-retry.
3. Never show raw API error messages to users. Parse and sanitize.

### Phase 3: Loading States
1. Every API call has a loading state. Show a skeleton, spinner, or progress indicator.
2. Avoid showing a spinner for every interaction:
   - Initial load: skeleton screen (preferred) or spinner.
   - Refresh: keep showing stale data with an indicator that refresh is happening.
   - Mutation: show the new data optimistically or show a brief progress indicator.
3. Handle race conditions: if request A completes after request B, use AbortController or request deduplication.

### Phase 4: Caching Strategy
1. Define cache duration per endpoint type:
   - Static data (config, lists of options): cache for 5-60 minutes.
   - User-specific data (profile, orders): cache for 30-300 seconds.
   - Real-time data (notifications, status): stale-while-revalidate, or don't cache.
2. Invalidate the cache after mutations. Re-fetch affected data.
3. Use stale-while-revalidate: show cached data immediately, refresh in the background.

### Phase 5: Retry and Resilience
1. Automatic retry for transient failures: 3 retries with exponential backoff.
2. Do not retry on 4xx errors (client mistake). Only retry 5xx, network errors, and timeouts.
3. Implement a circuit breaker: if the API returns 5xx 10 times in a minute, stop calling for 30 seconds.

## Common Mistakes

- **Not handling loading state**: The user sees nothing while the API call is in progress. Always show a loading indicator.
- **Not handling errors**: An unhandled API error crashes the page or leaves the user with a permanent spinner.
- **Ignoring race conditions**: Component unmounts before the API response arrives, causing a "setState on unmounted component" warning or stale data.
- **No retry logic**: A transient network failure fails the user's action permanently. Retry automatically.
- **Overfetching in loops**: An API call inside `useEffect` that runs on every render or a loop that fetches multiple endpoints sequentially.

## Quality Gates

- [ ] All API calls have loading, error, and success state handling.
- [ ] Network errors show a user-friendly message with retry action.
- [ ] Race conditions are handled (AbortController on unmount, deduplication).
- [ ] Retry logic is implemented for transient failures with exponential backoff.
- [ ] Cache strategy is defined and documented per endpoint category.
