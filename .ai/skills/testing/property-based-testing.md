---
id: property-based-testing
version: 2.0.0
confidence: 0.75
success_rate: 0.70
last_updated: 2026-06-29
tags:
  - testing
  - property-based
  - flexible
---

# Property-Based Testing

> Flexible skill. Use property-based testing to find edge cases that example-based tests miss. Know when to apply properties and when examples suffice.

## Overview

Property-based testing (PBT) generates hundreds or thousands of test cases from a property specification, finding edge cases that hand-written examples would miss. Rather than asserting specific input-output pairs, you assert invariants that must hold for all inputs.

**Core Principle**: Define the invariant, not the example. Let the computer find edge cases.

## Step-by-Step Process

### Phase 1: Identify Candidate Properties
Look for these property patterns:
- **Round-trip**: serialize(deserialize(x)) = x, or encrypt(decrypt(x)) = x
- **Idempotent**: sort(sort(x)) = sort(x), or deduplicate(deduplicate(x)) = deduplicate(x)
- **Commutative**: operation(A, B) = operation(B, A) for symmetric operations
- **Oracle**: compare against a known correct (if slower) implementation
- **Inductive**: define base case + step case (like a mathematical proof)
- **Invariant**: the output always satisfies a condition (e.g., sorted list is always same length)

### Phase 2: Define Generators
1. Start with the framework's built-in generators (integers, strings, collections).
2. Constrain generators to valid inputs: non-empty strings, positive integers, sorted lists.
3. Custom generators for domain types: email addresses, phone numbers, order objects.

### Phase 3: Write Property Tests
1. Assert the property, not the specific output.
2. Let the framework shrink failing cases to minimal reproduction.
3. Log the seed to reproduce failures deterministically.

### Phase 4: Integrate with Example Tests
1. Use PBT for validation logic, serialization, data transformations.
2. Use example tests for regression bugs and specific business rules.

## When to Use PBT vs Example-Based

| Scenario | Approach |
|---|---|
| Data serialization/deserialization | Property-based |
| Validation rules | Property-based |
| Sorting, filtering, deduplication | Property-based |
| Specific bug regression | Example-based |
| UI component rendering | Example-based |
| Integration with external API | Example-based |
| Business rule with fixed outputs | Example-based |

## Common Mistakes

- **Writing properties that always pass**: A property that can't fail is worse than no test. Use examples first to validate the property.
- **Overly complex generators**: If the generator is harder to maintain than the code, reconsider PBT.
- **Testing too broadly**: `for_all(any_integer())` generates values your code will never receive in production. Constrain to realistic domains.
- **Ignoring shrunk output**: The library finds minimal failing cases. Study them carefully; they reveal surprising assumptions.
- **PBT for everything**: Example tests are simpler to write and read. Use PBT where properties are natural and clear.

## Quality Gates

- [ ] Each property is accompanied by at least one ready-to-run example test.
- [ ] Generator constraints match production constraints (no illegal states generated).
- [ ] Shrinking produces minimal, human-readable counterexamples.
- [ ] Property tests run within the normal test suite budget (< 30s for a typical module).
- [ ] The seed is logged or recorded for any discovered failure.
