---
id: workflow-onboarding-001
version: 1.0.0
confidence: 0.80
success_rate: 0.75
last_updated: 2026-06-29
tags: [workflow, onboarding, setup]
---

# Onboarding Workflow

Systematic process for new agents or contributors to understand the codebase, tooling, and workflows before contributing.

## Flowchart

```
[Onboarding Start] → [Clone Repo] → [Setup Environment]
    → [Run Tests: Verify Environment] → [Tests Pass?] → [No] → [Fix Environment Issues]
    → [Yes] → [Learn Architecture: Key Files & Patterns]
    → [Learn Workflows: .ai/workflows/ Overview]
    → [First Task: Simple Contribution] → [Review: Guided Review]
    → [Retro: Reflect on First Experience]
    → [Done: Ready for Independent Work]
```

## Trigger

- New agent instance starts for the first time on this project.
- New human contributor joins the team.
- Project is re-initialized after a long hiatus.
- Environment has changed significantly (new toolchain, migration).

## Steps

### 1. Clone Repo
- **Input**: Repository URL, access credentials (if needed).
- **Process**: Clone the repository. Verify the clone is complete and on the correct branch. Read the project README and CLAUDE.md (if present).
- **Output**: Local copy of the repository.
- **Quality Gate**: Clone is clean (no errors, no missing LFS objects). README is readable. CLAUDE.md exists and is reviewed.

### 2. Setup Environment
- **Input**: Project configuration files (package.json, Cargo.toml, Dockerfile, etc.).
- **Process**: Install dependencies (npm install, cargo build, pip install, etc.). Set up any required services (database, cache, queues). Configure environment variables from example files. Install pre-commit hooks if applicable.
- **Output**: Fully configured development environment.
- **Quality Gate**: All dependency installations complete without errors. Required services are running. Environment variables are configured correctly (no placeholder values left).

### 3. Run Tests
- **Input**: Configured environment.
- **Process**: Run the test suite. Verify all tests pass. If tests fail, diagnose whether the issue is environment-specific or pre-existing.
- **Decision Point**: `[Tests Pass?] → [Yes] → [Proceed to Architecture] | [No: Environment issue] → [Fix environment] → [Re-run tests] | [No: Pre-existing failure] → [Note known failures → Proceed]`.
- **Output**: Green test suite (or documented known failures).
- **Quality Gate**: At least the core test suite passes. If known failures exist, they are documented with references (e.g., issue tracker links). The on-boarder understands which tests are expected to pass.

### 4. Learn Architecture
- **Input**: Codebase, architecture docs (if any).
- **Process**: Review: (a) directory structure, (b) key files (entry points, core modules, config), (c) data flow (request-response cycle, data pipeline), (d) key patterns used (repository pattern, MVC, event-driven, etc.), (e) technology stack and why each component was chosen.
- **Output**: Architecture understanding verified (can explain the system in own words).
- **Quality Gate**: Can answer: What does each top-level directory contain? What is the request flow from entry to response? Where does business logic live? Where are tests for a given module?

### 5. Learn Workflows
- **Input**: Files in `.ai/workflows/`.
- **Process**: Read each workflow file. Understand: what triggers each workflow, the step sequence, decision points, quality gates, and expected outputs. Pay special attention to: task-lifecycle (the meta-workflow), learning-loop (how the system improves), and code-review (quality standards).
- **Output**: Workflow understanding (can identify which workflow applies to a given situation).
- **Quality Gate**: Can answer: Which workflow handles a new feature? What do you do when you encounter a bug? What happens after a task is completed? How are quality gates enforced?

### 6. First Task
- **Input**: Simple, well-scoped task (e.g., documentation fix, small bug, easy feature).
- **Process**: Execute the task using the appropriate workflow. Follow all steps and quality gates. The task is intentionally simple to build confidence in the workflow process.
- **Output**: Completed first task with all artifacts (code, tests, memory updates).
- **Quality Gate**: The correct workflow was identified and followed. All quality gates in the workflow were passed. The on-boarder can explain which workflow they used and why.

### 7. Review
- **Input**: First task output.
- **Process**: Guided code review of the first task. Focus on both the code quality and adherence to workflows. Provide constructive feedback on process as well as product.
- **Output**: Review feedback and approval.
- **Quality Gate**: Review is educational, not gatekeeping. The on-boarder understands any feedback and can apply it going forward. If the review identifies workflow gaps (workflows that didn't handle the situation), update the workflows.

### 8. Retro
- **Input**: Onboarding experience, first task experience.
- **Process**: Reflect on: (a) what was unclear in the documentation, (b) what was missing from the setup, (c) which workflows were helpful, (d) which workflows were confusing, (e) improvements to the onboarding process itself.
- **Output**: Onboarding retro notes, improvements to onboarding workflow.
- **Quality Gate**: At least one improvement to the onboarding process is identified and captured as an action item. The on-boarder feels confident to work independently.

## Output

- Fully set up development environment.
- Verified test suite.
- Architecture and workflow understanding.
- Completed first task.
- Onboarding feedback for process improvement.
- Ready-to-contribute agent or developer.
