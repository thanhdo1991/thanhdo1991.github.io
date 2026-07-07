---
id: agent-007
version: 1.0.0
confidence: 0.92
success_rate: 0.90
last_updated: 2026-06-29
tags:
  - tools
  - capabilities
  - interfaces
---

# tools.md — Tool Categories & Capabilities

## File System Operations

- **Read** — retrieve file contents for analysis. Supports partial reads by offset and line count for large files.
- **Write** — create new files or overwrite existing ones. Full content replacement.
- **Edit** — apply targeted string replacements to existing files. Requires exact match of the replaced text.
- **Glob** — fast pattern matching to find files by name, extension, or path structure.
- **Grep** — content search across files using regular expressions. Supports multiline, case-insensitive, and context-line modes.

## Version Control

- **Status** — view working tree state, staged/unstaged changes.
- **Diff** — inspect changes before committing.
- **Commit** — record changes with structured messages.
- **Branch management** — create, switch, merge branches for isolated work.
- **Remote operations** — push, pull, fetch from remote repositories.

## Testing & Verification

- **Test execution** — run test suites by file, pattern, or tag.
- **Coverage analysis** — measure code coverage and identify untested paths.
- **Linting** — static analysis for code style and common errors.
- **Type checking** — verify type consistency across the codebase.

## Search & Discovery

- **Structural search** — locate files, directories, and code structures by name or pattern.
- **Content search** — find specific strings, patterns, or symbols across the codebase.
- **Dependency analysis** — trace import/require graphs and understand module relationships.

## Documentation

- **Inline help** — access tool-level usage information.
- **Formatting** — structured output in markdown, JSON, YAML, and other standard formats.
- **Logging** — record decisions, outcomes, and deviations for future reference.

## Tool Invocation Principles

- Select the simplest tool that achieves the goal.
- Chain tools sequentially when output feeds into the next step.
- Log tool results as evidence when they form part of a completion claim.
