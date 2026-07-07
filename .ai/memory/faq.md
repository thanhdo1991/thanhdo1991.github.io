---
id: faq
version: 1.0.0
confidence: 0.95
success_rate: 0.90
last_updated: 2026-06-29
tags:
  - faq
  - knowledge-base
  - template
---

# Frequently Asked Questions

## Purpose

A living FAQ document that accumulates answers to common questions about the project.
When a question is asked more than once, document the answer here. This saves time,
reduces interruptions, and helps new team members ramp up faster.

---

## Project Setup & Onboarding

### Q: How do I set up the project locally?

**A:** See the README for quick-start instructions. In summary:
1. Clone the repository and run `[setup command]` to install dependencies.
2. Copy `.env.example` to `.env` and fill in your local values.
3. Start required services (database, cache, etc.) using `[command]`.
4. Run `[command]` to verify everything works.
If you encounter issues, check troubleshooting below or ask in `[channel]`.

### Q: What tools do I need to install?

**A:** Required: [language runtime], [package manager], [database client].
Recommended: [editor], [API client], [Docker]. See environment.md for full details.

### Q: How long should local setup take?

**A:** Typically 15-30 minutes for first-time setup. If it takes longer, the setup
documentation may be outdated — please open an issue or update the docs.

---

## Workflow

### Q: What branch should I base my work on?

**A:** Always branch from `[default-branch]`. Feature branches use the prefix
`[feature/description]`; bug fixes use `[fix/description]`.

### Q: How do I name my commits?

**A:** We use [Conventional Commits / descriptive format]. Example:
`[type(scope): description]`. See conventions.md or preferences.md for details.

### Q: How large should a pull request be?

**A:** Aim for under 400 lines changed. If your PR exceeds this, consider splitting
it into logical chunks. Large PRs are harder to review and more likely to contain
defects.

### Q: Who should review my PR?

**A:** At least one person with context on the affected code area. Use GitHub's
auto-assign or tag relevant teammates. The `[CODEOWNERS]` file will suggest
appropriate reviewers.

---

## Architecture & Design

### Q: Why did we choose [technology X] over [technology Y]?

**A:** See ADR-[number] for the full rationale. The short version: [technology X]
was chosen because [brief reason]. If you believe the context has changed, consider
proposing a new ADR.

### Q: Can I introduce a new design pattern?

**A:** Yes, but please check patterns.md first to see if an existing pattern fits.
If introducing a new pattern, document it in patterns.md and consider whether an
ADR is warranted for significant architectural impact.

### Q: How do I handle cross-cutting concerns like logging or authentication?

**A:** Use the existing middleware / decorator infrastructure in the shared module.
Do not add logging or auth logic to individual services. If you need a new
cross-cutting capability, discuss with the team first.

---

## Testing

### Q: What should I test?

**A:** All public APIs, all business logic branches, all error paths, and all
boundary conditions. See quality-rules.md for coverage thresholds. If you are
unsure, write a test — more tests are almost always better than fewer.

### Q: How do I run a subset of tests?

**A:** Use the `--filter` or `--test-path-pattern` flag: `[command] --filter [pattern]`.
See the testing tool's documentation for advanced filtering.

### Q: My test is flaky. What should I do?

**A:** Flaky tests undermine trust in the test suite. Identify the root cause
(non-determinism, shared state, timing) and fix it. If the fix is non-trivial,
quarantine the test with `@quarantine` / `[skip]` and create an issue. Flaky tests
must be resolved within 48 hours.

---

## Build & Deploy

### Q: How do I build for production?

**A:** Run `[build command]`. This produces optimized artifacts in the `[dist/]`
directory. See the README or environment.md for details.

### Q: How do I deploy to staging / production?

**A:** Staging deploys automatically when code is merged to `[branch]`. Production
deploys require a manual approval step. See the deployment runbook in `[location]`.

### Q: The build failed in CI but works locally. What now?

**A:** Common causes: environment differences, missing lockfile updates, platform-
specific behavior. Check CI logs for the exact error. If the issue is environment-
related, ensure your local setup matches the CI environment (see environment.md).

---

## Troubleshooting

### Q: I get error [X] when running locally. What does it mean?

**A:** [Error X] is usually caused by [common cause]. Try:
1. [Step 1]
2. [Step 2]
3. [Step 3]
If none of these help, check the project's issues tracker or ask in `[channel]`.

### Q: The database migration failed. How do I roll back?

**A:** Run `[rollback command]`. If the automatic rollback fails, follow the manual
rollback procedure in `[location]`.

---

*Add questions and answers as they arise. Questions asked more than once are
prioritized for inclusion here.*
