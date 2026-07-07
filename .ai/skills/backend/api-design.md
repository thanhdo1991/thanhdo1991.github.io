---
id: api-design
version: 2.1.0
confidence: 0.88
success_rate: 0.82
last_updated: 2026-06-30
tags:
  - backend
  - api
  - rest
  - graphql
  - flexible
---

# API Design

> Flexible skill. Design RESTful or GraphQL APIs that are consistent, discoverable, and evolvable. Cover resource naming, versioning, error responses, pagination, and documentation.

## Overview

A well-designed API is the contract between services and clients. Consistency in naming, status codes, error formats, and pagination reduces client integration time and prevents misunderstandings. A good API is predictable: given the pattern, the client can guess the next endpoint.

**Core Principle**: An API is a user interface for developers. Design it with the same care as a UI. Consistency, predictability, and clear error messages are features.

## Step-by-Step Process

### Phase 1: Resource Design
1. Identify the resources (nouns): User, Product, Order, Invoice.
2. Define relationships: User has Orders, Order has OrderItems.
3. Map to URL patterns:
   - Collection: `GET /api/v1/users`
   - Single: `GET /api/v1/users/:id`
   - Nested: `GET /api/v1/users/:id/orders`
   - Actions that don't fit CRUD: `POST /api/v1/orders/:id/cancel`
4. Use plural nouns for collections, singular for singletons.

### Phase 2: Request/Response Design
1. Use consistent casing: pick camelCase or snake_case per project convention.
2. Return the full resource on creation (`POST`) for client convenience.
3. Filtering: `GET /api/v1/users?role=admin&status=active`
4. Sorting: `GET /api/v1/users?sort=-created_at` (minus = descending)
5. Sparse fields: `GET /api/v1/users?fields=id,name,email`
6. Include related resources: `GET /api/v1/orders?include=items,user`

### Phase 3: Error Responses
1. Use HTTP status codes correctly:
   - 200: Success (GET, PATCH)
   - 201: Created (POST)
   - 204: No Content (DELETE success)
   - 400: Bad Request (validation error)
   - 401: Unauthenticated
   - 403: Unauthorized (authenticated but not allowed)
   - 404: Not Found
   - 409: Conflict (duplicate, version conflict)
   - 422: Unprocessable Entity (domain validation)
   - 429: Too Many Requests
   - 500: Internal Server Error
2. Standard error body: `{ error: { code: "VALIDATION_ERROR", message: "Email is required", details: [{ field: "email", reason: "required" }] } }`
3. Never expose stack traces or internal implementation details in error responses.

### Phase 4: Pagination
1. Use cursor-based pagination for lists that change frequently.
2. Use offset-based pagination for stable lists.
3. Response structure: `{ data: [...], meta: { total: 100, cursor: "abc123", has_more: true } }`

### Phase 5: Versioning
1. URL versioning: `/api/v1/`, `/api/v2/`. Simple, explicit, cacheable.
2. Support at least one previous version in production.
3. Deprecate with a Sunset header: `Sunset: Sat, 31 Dec 2026 23:59:59 GMT`

## Common Mistakes

- **Inconsistent naming**: Mixing camelCase and snake_case, or using different resource naming patterns.
- **Wrong HTTP methods**: Using POST for everything, or GET for mutations.
- **Exposing internal implementation**: Database IDs, internal column names, stack traces in error responses.
- **No pagination for lists**: Returning all records in one response breaks at scale.
- **Backward-incompatible changes without versioning**: Adding required fields, removing fields, or changing types is breaking.

## Quality Gates

- [ ] All endpoints follow consistent URL naming (plural nouns, kebab-case).
- [ ] HTTP status codes are used correctly.
- [ ] Error responses have a consistent structure with code, message, and optional details.
- [ ] All list endpoints support pagination with a default limit.
- [ ] Breaking changes are versioned. Deprecated versions have a Sunset header.
- [ ] API documentation is auto-generated from the spec (OpenAPI/Swagger).
