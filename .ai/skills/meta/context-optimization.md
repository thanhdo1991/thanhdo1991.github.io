---
id: context-optimization
version: 2.0.0
confidence: 0.75
success_rate: 0.70
last_updated: 2026-06-29
tags:
  - meta
  - context
  - llm
  - flexible
---

# Context Optimization

> Flexible skill. Manage LLM context window effectively: know what to include, what to summarize, what to compress, and what to evict. Optimize for signal, not size.

## Overview

LLMs have limited context windows. Every token in the context consumes capacity that could be used for more relevant information. Context optimization is the practice of selecting, compressing, and structuring information to maximize the useful signal within the available window.

**Core Principle**: Context is a scarce resource. Every token should earn its place. If it doesn't help the model produce a better output, remove it.

## Step-by-Step Process

### Phase 1: Identify Context Sources
1. **High priority**: Current task description, code diff, error messages, relevant documentation.
2. **Medium priority**: Project structure, key conventions, recent decisions, related code.
3. **Low priority**: Historical context, tangential docs, verbose logs, unrelated modules.
4. **Evict first**: Large dependency files, verbose comments, outdated context, duplicated information.

### Phase 2: Structure the Context
1. Put the most important information first (primacy bias).
2. Use clear separators: `=== CODE ===`, `=== TASK ===`, `=== CONSTRAINTS ===`.
3. Group related information together. Avoid interleaving unrelated context.
4. For code: include only the relevant function or module, not the entire file.

### Phase 3: Compression Techniques
1. **Summarize**: Replace verbose explanations with concise summaries.
2. **Truncate**: Remove boilerplate, repetitive patterns, and verbose comments.
3. **Reference**: Use file paths and line numbers instead of inline code.
4. **Schema-level**: Instead of 100 records, show the schema + 3 representative records.

### Phase 4: Recall and Reuse
1. Store resolved decisions in a decisions log. Retrieve when context is needed.
2. Store common patterns in patterns.md. Reference instead of explaining again.
3. Use a memory system or notes to persist context across sessions.
4. When context overflows: summarize the current session, save to memory, start fresh.

### Phase 5: Eviction Strategy
1. When approaching the context limit, ask: "What is the least valuable content in the context?"
2. Evict in order: verbose examples > tangential discussion > old error messages > redundant constraints.
3. If the entire context is valuable, summarize from the bottom: the oldest information is usually less relevant.
4. Never evict: the current task definition, active code diff, immediate error messages.

## Common Mistakes

- **Dumping entire files**: Including a 500-line file when only 10 lines are relevant wastes context.
- **Repeating information**: Re-stating the same constraint multiple times.
- **Preserving outdated context**: An error message that was resolved, a decision superseded.
- **Not using structured formats**: Plain text is harder to parse than bullet lists or code blocks.
- **Ignoring the 80/20 rule**: 80% of useful context comes from 20% of available information.

## Quality Gates

- [ ] Context starts with the most important information (task, active change, error).
- [ ] No full file dumps unless every line is relevant.
- [ ] Summarization or truncation is applied to verbose content.
- [ ] Structured formats (bullet lists, code blocks, separators) are used consistently.
- [ ] Context fits within the target model's effective window (leaving buffer for output).
