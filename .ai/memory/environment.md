---
id: environment
version: 1.0.0
confidence: 0.95
success_rate: 0.88
last_updated: 2026-06-29
tags:
  - environment
  - configuration
  - devops
  - template
---

# Environment Configuration

## Purpose

Define the environments used throughout the development lifecycle and the process for
managing configuration across them. Consistent environments reduce "works on my
machine" issues and deployment surprises.

---

## Environment Overview

| Environment | Purpose | Deploy Method | URL / Endpoint | Who Has Access |
|-------------|---------|---------------|----------------|----------------|
| **Local Development** | Individual development and testing | Local run / Docker Compose | http://localhost:[port] | All developers |
| **Development / Dev** | Integration testing, shared environment | CI auto-deploy from `develop` | [url] | Development team |
| **Staging** | Pre-production validation, UAT | CI auto-deploy from `main` | [url] | Internal team + stakeholders |
| **Production** | Live user-facing system | Manual deploy with approval | [url] | Operations team |

---

## Local Development Setup

### Prerequisites

- [Language runtime] version [X.Y.Z]
- [Package manager] version [X.Y.Z]
- [Database] version [X.Y.Z]
- [Other tools as needed]

### Quick Start

```bash
# Clone the repository
git clone [repository-url]
cd [project-directory]

# Copy environment file
cp .env.example .env

# Install dependencies
[package-manager] install

# Start development services
[command to start dev environment]
```

### Recommended Tools

- **Container Runtime:** Docker (for local services like databases, queues)
- **API Client:** [Postman / Insomnia / HTTPie / curl]
- **Database GUI:** [TablePlus / DataGrip / DBeaver / pgAdmin]
- **Process Manager:** [nodemon / pm2 / foreman / supervisor]

## Environment Variables

### Required Variables

| Variable | Description | Local Value | Dev | Staging | Production |
|----------|-------------|-------------|-----|---------|------------|
| `DATABASE_URL` | Database connection string | Local postgres | Dev RDS | Stage RDS | Prod RDS |
| `API_KEY` | API authentication key | dev-key-xxx | [set] | [set] | [set via secrets] |
| `LOG_LEVEL` | Logging verbosity | debug | debug | info | warn |
| `PORT` | Application port | 3000 | 3000 | 3000 | 8080 |
| [Add more] | | | | | |

### Optional Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CACHE_TTL_SECONDS` | 300 | Cache expiration in seconds |
| `MAX_REQUEST_SIZE_MB` | 10 | Maximum allowed request body size |
| `RATE_LIMIT_REQUESTS` | 100 | Requests per window per IP |

## Secrets Management

### Principles

1. **Never commit secrets to version control.** Use environment variables or a
   secrets manager.
2. **Use `.env.example`** as a template with placeholder values. Commit this file.
3. **Keep actual `.env` files in `.gitignore`.**
4. **Rotate secrets** periodically and whenever a team member with access departs.
5. **Audit access** to production secrets quarterly.

### Secrets Storage

| Environment | Storage Method | Notes |
|-------------|---------------|-------|
| Local | `.env` file | Listed in `.gitignore` |
| Dev | [Vault / AWS Secrets Manager / GitHub Secrets / .env in CI] | |
| Staging | [Vault / AWS Secrets Manager / GitHub Secrets] | |
| Production | [Vault / AWS Secrets Manager / HashiCorp Vault] | Access requires approval |

## Configuration by Environment

Configuration that differs between environments should be:

1. **Environment variables** for values that change per deployment.
2. **Config files** (checked into version control) for values that are the same
   across environments but may be overridden by env vars.
3. **Feature flags** for toggling behavior without deployment.

### Config File Hierarchy

```
config/
  default.yaml         — Base config, all environments
  development.yaml     — Dev overrides
  staging.yaml         — Staging overrides
  production.yaml      — Production overrides
  local.yaml           — Local overrides (gitignored)
```

## Infrastructure as Code

| Resource | IaC Tool | Config Location |
|----------|----------|-----------------|
| Compute | [Terraform / Pulumi / CloudFormation] | [path to config] |
| Database | [Terraform / Pulumi / CloudFormation] | [path to config] |
| Networking | [Terraform / Pulumi / CloudFormation] | [path to config] |
| CI/CD Pipeline | [GitHub Actions / GitLab CI / Jenkinsfile] | [path to config] |

---

*Environment configurations must be kept in sync. Changes to production config should
first be validated in dev and staging.*
