---
id: coding-style
version: 1.0.0
confidence: 0.95
success_rate: 0.88
last_updated: 2026-06-29
tags:
  - style
  - coding-standards
  - template
---

# Coding Style Guide

## Language-Agnostic Rules

These rules apply regardless of programming language. Language-specific additions
may be layered on top in a separate file.

---

## Formatting

- **Indentation:** 2 spaces per level (language standard overrides: e.g., Python uses
  4 spaces as per PEP 8). Never use literal tab characters.
- **Max Line Length:** 100 characters. For function signatures or long strings,
  break at natural boundaries and indent continuations by one level.
- **Blank Lines:**
  - One blank line between methods/functions.
  - Two blank lines between top-level declarations (classes, modules).
  - No trailing whitespace on any line.
- **Braces:** K&R style (opening brace on the same line) for most languages.
  Allman style (opening brace on its own line) is acceptable where idiomatic.
- **Trailing Commas:** Use trailing commas in multi-line lists, objects, and
  function parameters. This produces cleaner diffs when adding items.

## Naming (see also conventions.md)

- **Be descriptive but concise.** `getUserById` is good. `getUserByIdFromDatabaseAndReturn` is not.
- **Avoid Hungarian notation** unless the language idiom requires it.
- **Avoid single-letter variable names** except for:
  - Loop counters (`i`, `j`, `k`)
  - Generic type parameters (`T`, `K`, `V`)
  - Mathematical coordinates (`x`, `y`, `z`)
- **Boolean variables** should read as statements: `isEmpty`, `hasChildren`, `isValid`.

## Code Organization

### Functions

- A function should perform exactly **one** identifiable task.
- **Short functions** (under 20 lines) are preferred. Extract helper functions
  liberally — even a 3-line helper can clarify intent.
- **Parameters:** Aim for 2 or fewer parameters. Use an options object for 3+.
- **Return types:** Always declare a return type where the language supports it.
- **Pure functions** are preferred over mutating functions. Return new values
  instead of modifying inputs.

### Conditionals

- Prefer **positive** conditionals: `if (isActive)` over `if (!isInactive)`.
- **Ternary operators** are acceptable for simple binary assignments. Avoid nesting
  ternaries — that is a code smell.
- **Guard clauses** return early for invalid or edge-case inputs. This flattens the
  happy path and reduces nesting.

```
// Good: guard clause
function processOrder(order) {
  if (!order.isValid()) return { error: 'Invalid order' };
  // happy path continues here...
}
```

### Composition Over Inheritance

- Prefer composing behavior through small, focused interfaces rather than deep
  class hierarchies.
- Use inheritance only for true "is-a" relationships where the subtype truly
  substitutes for the base type.
- **Favor interfaces and traits** to share behavior across unrelated types.

### Error Handling

- Return or throw explicit error types, not generic errors.
- Handle errors at the appropriate level — don't catch an error unless you can
  meaningfully handle or augment it.
- Avoid empty catch blocks. If you must suppress an error, document why.

### State & Mutation

- **Minimize mutable state.** Prefer `const` / `final` / `val` over `let` / `var`.
- Keep mutation local to a function. Avoid mutating arguments or global state.
- **Immutability** simplifies reasoning about code. Use immutable data structures
  where available.

## Comments

- Code should be **self-documenting** — clean names and structure reduce the need
  for comments.
- Comments should explain **why**, not **what**. The code already says what it does.
- **Legal headers** (copyright, license) go at the top of the file.
- **Magic numbers** must be named constants, not literals.

---

## Formatting Enforcement

Use an automated formatter (Prettier, gofmt, rustfmt, black, etc.) configured to
match this style. Integrate formatting into the pre-commit hook and CI pipeline.

---

*This guide evolves. Changes require team consensus and should be reflected in the
formatter configuration.*
