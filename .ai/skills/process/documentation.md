---
id: documentation
version: 2.0.0
confidence: 0.80
success_rate: 0.74
last_updated: 2026-06-29
tags:
  - process
  - documentation
  - writing
  - flexible
---

# Documentation

> Flexible skill. Write clear, maintainable documentation: README, API docs, architecture docs, and changelogs. Documentation is a product, not an afterthought.

## Overview

Documentation is the primary interface between your code and its users (including your future self). Good documentation answers questions before they are asked, reduces onboarding time, and prevents recurring issues. Documentation that is hard to maintain will become obsolete; documentation that is easy to maintain will stay relevant.

**Core Principle**: Write for the reader who has never seen the project before. Documentation is not a record of what you did; it is a guide for what someone else needs to know.

## Step-by-Step Process

### Phase 1: Identify Audience and Purpose
1. **README**: New developers evaluating or onboarding to the project. Quick start, prerequisites, basic usage.
2. **API docs**: Developers integrating with the API. Endpoints, requests, responses, errors, authentication.
3. **Architecture docs**: Developers maintaining or extending the system. Components, data flow, decisions, trade-offs.
4. **Changelog**: Anyone tracking what changed between versions. Follow Keep a Changelog format.

### Phase 2: Write the README
1. Project name and one-sentence description.
2. Prerequisites: language version, database, dependencies.
3. Quick start: copy-paste commands to get running in 2 minutes.
4. Configuration: environment variables, configuration files.
5. Development: how to run tests, linters, and the dev server.
6. Deployment: how to build and deploy (or link to deploy docs).

### Phase 3: Write Architecture Docs (ADR)
1. Record architecture decisions in ADR (Architecture Decision Record) format.
2. Each ADR contains: title, status, context, decision, consequences.
3. Keep ADRs in the repository at `docs/adr/NNNN-title.md`.
4. Review ADRs when revisiting the decision. Update status to "superseded" if replaced.

### Phase 4: Maintain Documentation
1. Treat documentation as code: review in PRs, test links, keep in version control.
2. Use `mkdocs`, `docusaurus`, or similar for multi-page documentation.
3. Add a "last reviewed" date to each document. Automate prompts for review.
4. Include a "Contributing" section that explains how documentation is updated.

## Common Mistakes

- **README only has setup instructions**: Setup is important, but README should also explain what the project does, how it works, and where to get help.
- **Outdated documentation**: Documentation that contradicts the code is worse than no documentation. Review and update with every significant change.
- **Documenting implementation details instead of concepts**: Code changes; concepts evolve slowly. Document the "why" and "what," not the "how."
- **No examples**: Examples are the most valuable part of documentation. Every API, function, or configuration should have a working example.
- **Writing for the author, not the reader**: Avoid internal jargon, implicit assumptions, and undocumented prerequisites. The reader does not have your context.

## Quality Gates

- [ ] README has a quick-start section that a new developer can follow in under 5 minutes.
- [ ] API documentation includes at least one example request and response per endpoint.
- [ ] Architecture decisions are documented as ADRs with status, context, decision, and consequences.
- [ ] Documentation is versioned alongside the code (same repository, same branch).
- [ ] All links in documentation are valid (checked by a link checker in CI).
