---
id: error-handling
version: 2.0.0
confidence: 0.90
success_rate: 0.85
last_updated: 2026-06-29
tags:
  - backend
  - errors
  - rigid
---

# Error Handling

> Rigid skill. Systematic error handling that never swallows errors, never exposes internals, and provides structured, typed, and logged failure information. Every error is either handled or explicitly propagated.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "This error should never happen, I'll leave it unhandled" | Everything that can fail will fail in production. Write the handler now, before the pager call. |
| "I'll catch it at the top level" | A generic top-level catch turns all errors into 500 responses with no context. |
| "Empty catch block is fine for this edge case" | An empty catch is a bug. If the error is expected, handle it. If unexpected, log it. |
| "Errors are just for debugging" | Production errors are user-facing failures. They are the most important signals. |

## Process

### Phase 1: Define Error Types
1. Create typed error classes or discriminated unions:
   - `ValidationError`: input data doesn't meet constraints.
   - `AuthenticationError`: user is not authenticated.
   - `AuthorizationError`: user is not allowed to perform this action.
   - `NotFoundError`: the requested resource does not exist.
   - `ConflictError`: the request conflicts with current state.
   - `InternalError`: unexpected system failure.
2. Each error type has a code (machine-readable), message (human-readable), and details (context).

### Phase 2: Structured Error Handling
1. Use try/catch at boundary points: API handlers, message queue consumers, scheduled jobs.
2. In each catch:
   - Log the error with full context (operation, inputs, stack trace).
   - Convert to a user-facing error response (never expose internals).
   - Return or propagate to the caller.
3. Never catch and ignore. If you catch, you must log, handle, or rethrow.

### Phase 3: Error Propagation
1. Functions should either return the expected value or throw/return a typed error.
2. Use `Result` types or union types for expected failures.
3. Use exceptions for unexpected failures (programming errors, infrastructure failures).

### Phase 4: Global Error Handler
1. Framework middleware that catches all unhandled exceptions.
2. Log the error with a correlation ID.
3. Return a generic 500 response. Never expose stack traces, file paths, or internal state.
4. Monitor: all 500 errors are paged in production.

## Red Flags (STOP Signals)

- Empty catch blocks. They hide failures and make debugging impossible.
- Errors handled by logging and continuing. If the error doesn't change execution, why catch it?
- Stack traces in API responses. They expose internal code structure to attackers.
- `catch (e: any)` without type narrowing. You lose the ability to handle different error types.
- Catching and rethrowing without adding context. A wrapped error should include context.

## No Exceptions

- Do not swallow errors. Every catch block must log, handle, or rethrow.
- Do not expose internal errors to users. Stack traces, file paths, and SQL queries are internal.
- Do not use exceptions for expected application flow (validation, not-found). Use typed returns.
- Do not leave empty catch blocks in committed code. They are latent bugs.
