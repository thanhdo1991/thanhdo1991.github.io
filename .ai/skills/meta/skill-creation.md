---
id: skill-creation
version: 2.1.0
confidence: 0.88
success_rate: 0.83
last_updated: 2026-06-29
tags:
  - meta
  - skills
  - rigid
  - auto-create
---

# Skill Creation

> Rigid skill. Create and improve skills using TDD: write the test first, watch it fail, write the skill, watch it pass, refactor. Skills are code and must be tested.

## When to Create
Skills are created in two ways:
1. **Auto-creation** (during `/recall`) — triggered when no existing skill matches the task domain
2. **Manual creation** — when you identify a repeated pattern worth formalizing

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "I'll just write the skill, the structure is clear" | Without a test, you have no way to verify the skill works or to detect regressions. |
| "Skills are documentation, not code" | Skills are executable knowledge. An untested skill is an assumption, not a tool. |
| "Testing a skill is meta-overhead" | If the skill is used more than once, the test pays for itself. Self-improving systems require feedback loops. |
| "I know what the skill should contain" | Write the test first and discover what you don't know. The test forces clarity. |

## Process

### Phase 1: Identify the Need
1. What task does this skill automate or guide?
2. Who is the audience? What is their context and skill level?
3. What outcome does the skill produce?

### Phase 2: Write the Test First
1. Define the test scenario: input or situation -> expected skill behavior -> expected output.
2. The test checks:
   - Skill structure: frontmatter is valid, required sections exist.
   - Content quality: no placeholder text, no contradictions.
   - Behavior: given a simulated scenario, does the skill produce the correct guidance?
3. Run the test. It must fail. A test that passes without a skill is a useless test.

### Phase 3: Write the Skill
1. Follow the template:
   - YAML frontmatter with id, version, confidence, success_rate, tags.
   - Description line with skill type (rigid/flexible) and summary.
   - For rigid skills: rationalization table, red flags, no exceptions.
   - For flexible skills: overview, process, common mistakes, quality gates.
2. **Auto-created skills** (from `/recall` gap detection) go to `.ai/skills/user/<category>/<name>.md`
3. **Manually created skills** go to `.ai/skills/<category>/<name>.md`
4. Write production-grade content. No placeholder text.
5. Ensure the skill is self-contained: the reader should not need external references.

### Phase 4: Watch It Pass
1. Run the test against the completed skill.
2. If the test fails, fix the skill until it passes.
3. If the test passes but the skill is wrong, fix the test and the skill.

### Phase 5: Refactor
1. Review the skill for clarity, conciseness, and correctness.
2. Check for contradictions between sections.
3. Update the version number.
4. Verify the skill works in practice by using it on a real task.

## Red Flags (STOP Signals)

- A skill without a corresponding test file.
- Skills with placeholder text ("TODO", "FIXME", "TBD").
- Confidence or success_rate not set or set to 1.0 (unrealistic).
- Frontmatter missing required fields (version, last_updated, confidence).
- Skills that are too vague to produce actionable guidance.

## No Exceptions

- Do not commit a skill without a passing test.
- Do not write the skill before writing the test. TDD applies to skill creation.
- Do not skip the refactor phase. Every skill can be improved.
- Do not leave placeholder text in any committed skill file.
