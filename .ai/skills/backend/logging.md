---
id: logging
version: 2.0.0
confidence: 0.80
success_rate: 0.76
last_updated: 2026-06-29
tags:
  - backend
  - logging
  - observability
  - flexible
---

# Logging

> Flexible skill. Implement structured logging with appropriate levels, correlation IDs, and sensitive data filtering. Logs are the primary tool for debugging production issues.

## Overview

Logging is the practice of recording application events in a structured, searchable format. Good logs enable debugging, monitoring, auditing, and compliance. Bad logs are noise that buries real signals.

**Core Principle**: Log what you need to debug an issue, not everything that happens. Every log line should have a clear purpose and be actionable.

## Step-by-Step Process

### Phase 1: Choose a Logging Framework
1. Use a structured logging library (pino, winston, structlog, slog, logrus).
2. Output JSON format by default. JSON is parsable, searchable, and indexable.
3. Configure the logger once at the application entry point. Use dependency injection to pass it.
4. Never use `console.log` or `print`. Route all output through the logging framework.

### Phase 2: Define Log Levels
- **TRACE**: Detailed debugging information. Not enabled in production.
- **DEBUG**: Information useful during development. May be enabled temporarily in production for specific services.
- **INFO**: Normal application events. User signup, order placed, scheduled job completed.
- **WARN**: Potential issues that don't require immediate action. Deprecated API called, retryable failure, high memory usage.
- **ERROR**: Recoverable errors. Failed operation that the application handled gracefully.
- **FATAL**: Unrecoverable errors. Application cannot continue. Triggers immediate escalation.

### Phase 3: Structured Fields
Every log line should include:
- `timestamp`: ISO 8601 with timezone.
- `level`: The log level.
- `service`: The service or application name.
- `environment`: dev, staging, production.
- `correlation_id`: Link related log lines across services.
- `message`: Human-readable description.
- `operation`: What was happening (HTTP method + path, job name, function).
- `duration_ms`: How long the operation took.
- `error`: Error details if applicable.

### Phase 4: Sensitive Data Filtering
1. Define patterns for sensitive data: email, phone, SSN, credit card, password, token.
2. Redact these fields before logging. Use a redaction library or middleware.
3. Never log request/response bodies that contain PII. Log structure, not content.
4. Test log output in staging to confirm no sensitive data leaks.

### Phase 5: Correlation IDs
1. Generate a correlation ID at the first entry point (HTTP request, message, scheduled job).
2. Pass the correlation ID through all downstream calls (database queries, API calls, background jobs).
3. Include the correlation ID in all logs. This enables end-to-end request tracing.
4. Return the correlation ID in API error responses so users can reference it.

## Common Mistakes

- **Logging too much**: Every log statement has a cost. In high-traffic services, excessive logging causes performance degradation and high storage costs.
- **Not logging enough in error paths**: When something fails, you need context: what operation, what inputs, what state. Log it.
- **Logging sensitive data**: Passwords, tokens, and PII in logs are compliance violations. Redact before logging.
- **Unstructured messages**: "User 123 saved" is useless at scale. Include structured fields.
- **No correlation IDs**: Without a correlation ID, you cannot connect related log entries across services.

## Quality Gates

- [ ] All logs are structured JSON with consistent field names.
- [ ] Log levels are used correctly.
- [ ] Correlation IDs are generated at entry points and passed through the request lifecycle.
- [ ] Sensitive data is redacted from all log output (verified by automated scan).
- [ ] Log sampling or rate limiting is in place for high-traffic services.
