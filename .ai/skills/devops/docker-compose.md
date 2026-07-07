---
id: docker-compose
version: 2.0.0
confidence: 0.80
success_rate: 0.75
last_updated: 2026-06-29
tags:
  - devops
  - docker
  - compose
  - flexible
---

# Docker Compose

> Flexible skill. Design Docker Compose configurations for local development, testing, and production-adjacent environments. Cover multi-stage builds, volumes, networking, and service orchestration.

## Overview

Docker Compose defines and runs multi-container Docker applications. A well-crafted Compose file ensures that all developers and environments share the same service topology, network configuration, and volume mounts, eliminating "works on my machine" issues.

**Core Principle**: The Compose file should be the source of truth for the local development environment. If a new developer needs manual steps, the Compose file is incomplete.

## Step-by-Step Process

### Phase 1: Service Design
1. Identify each service in the application: web server, database, cache, message queue, worker.
2. For each service, define:
   - Base image and version. Pin to specific versions, never `latest`.
   - Port mappings: host port to container port.
   - Environment variables: which are required, which have defaults, which are secrets.
   - Health checks: every service should define how to know it's ready.

### Phase 2: Multi-Stage Builds
1. Define a `development` stage: mounts source code as a volume for hot reload.
2. Define a `build` stage: runs tests, linters, and compiles the application.
3. Define a `production` stage: minimal image with compiled artifacts only.
4. Leverage Docker layer caching: copy `package.json`/`requirements.txt` first, then source code.

### Phase 3: Networking
1. Define a custom network for inter-service communication. Avoid `network_mode: host`.
2. Use service names as hostnames (e.g., `http://api:3000`).
3. Expose only the ports that are needed externally. Internal ports do not need `ports:` mapping.

### Phase 4: Volumes and Data
1. Use named volumes for persistent data (databases, caches). Anonymous volumes are hard to manage.
2. Use bind mounts for development (source code, hot reload configs).
3. Define a volume for package manager caches (npm, pip, maven) to speed up rebuilds.

### Phase 5: Orchestration
1. Define service dependencies with `depends_on` and health checks.
2. Use `wait-for-it` or `depends_on` condition for startup ordering.
3. Define resource limits: memory and CPU constraints prevent one service from starving others.
4. Use `.env` files for environment-specific overrides.

## Common Mistakes

- **Using `latest` tag**: Builds are non-deterministic. Always pin to a specific version or SHA.
- **Exposing every port**: Only the entry point service needs host port mapping. Other services talk via the internal network.
- **No health checks**: If you can't tell if a service is healthy, you can't orchestrate startup order or detect failures.
- **Ignoring resource limits**: Without limits, a memory leak in one service can OOM the entire dev environment.
- **Committing secrets to version control**: Use `.env.example` and add `.env` to `.gitignore`. Never commit real secrets.

## Quality Gates

- [ ] All services have pinned image versions.
- [ ] Health checks defined for every service.
- [ ] Startup ordering defined via `depends_on` with health conditions.
- [ ] Sensible resource limits set for all services.
- [ ] `docker compose up --build` starts the full stack without errors.
- [ ] `.env.example` documents all required environment variables.
