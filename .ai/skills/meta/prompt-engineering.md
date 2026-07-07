---
id: prompt-engineering
version: 2.0.0
confidence: 0.80
success_rate: 0.75
last_updated: 2026-06-29
tags:
  - meta
  - prompts
  - llm
  - flexible
---

# Prompt Engineering

> Flexible skill. Write effective prompts for LLMs using system prompts, few-shot examples, chain-of-thought, and structured output specifications. Adapt technique to task complexity.

## Overview

Prompt engineering is the practice of designing inputs to language models to produce reliable, accurate, and useful outputs. A well-crafted prompt is specific, structured, and constrained. A poorly crafted prompt is vague, open-ended, and produces unreliable results.

**Core Principle**: A prompt is a specification, not a question. The more precisely you define the task, the format, and the constraints, the more reliable the output.

## Step-by-Step Process

### Phase 1: Define the Task
1. Specify the task in one sentence: "Summarize this article in 3 bullet points."
2. Define the output format: "JSON with fields: title, summary, key_points."
3. Define constraints: "Maximum 100 words.", "Use technical language.", "Assume the reader is a senior engineer."
4. Define success criteria: "The summary must be factually accurate and include all key claims."

### Phase 2: Choose the Technique
- **Zero-shot**: Simple tasks the model already understands. "Translate to French: Hello."
- **Few-shot**: Provide 2-3 examples of input-output pairs. Best for format transfer or classification.
- **Chain-of-thought**: "Let's think step by step." Best for reasoning, math, or multi-step problems.
- **Structured output**: Schema + examples. Best when output must be parsed programmatically.

### Phase 3: Write the System Prompt
1. Set the role: "You are a senior software engineer reviewing a pull request."
2. Set the rules: "Follow the review hierarchy: correctness > style > performance > security."
3. Set constraints: "Do not suggest changes without explaining why."
4. Set tone: "Be direct and constructive."

### Phase 4: Iterate and Test
1. Run the prompt with representative inputs.
2. Evaluate the output against success criteria.
3. Refine: add constraints for failure cases, adjust examples for edge cases.
4. Version the prompt for tracking changes.

## Common Mistakes

- **Over-specifying**: Too many constraints create contradictions. The model satisfies some and violates others.
- **Under-specifying**: Vague prompts produce unpredictable outputs. "Write code" without language, framework, or style guidance.
- **Assuming the model knows the context**: The model does not know your project, codebase, or conventions. Provide context in the prompt.
- **No output format**: Free-form responses are hard to parse and inconsistent. Always specify the format.
- **Prompt injection**: User input in prompts should be isolated and sanitized to prevent injection attacks.

## Quality Gates

- [ ] Task is specified in a single, unambiguous sentence.
- [ ] Output format is explicitly defined with examples if non-trivial.
- [ ] Constraints are specific and measurable.
- [ ] Prompt has been tested with at least 3 representative inputs.
- [ ] Prompt handles edge cases gracefully (unexpected input, missing context).
