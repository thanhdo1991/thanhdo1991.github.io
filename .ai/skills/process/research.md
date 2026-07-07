---
id: research
version: 2.0.0
confidence: 0.75
success_rate: 0.70
last_updated: 2026-06-29
tags:
  - process
  - research
  - investigation
  - flexible
---

# Research

> Flexible skill. Conduct systematic technical research: formulate the question, search efficiently, evaluate sources critically, synthesize findings, and make a decision.

## Overview

Technical research is the process of finding, evaluating, and applying information to solve a problem. Whether evaluating a library, debugging a system, or learning a new technology, a structured research approach saves time and produces better decisions.

**Core Principle**: The goal of research is a decision, not infinite knowledge. Stop researching when you have enough information to make an informed decision.

## Step-by-Step Process

### Phase 1: Define the Question
1. Write the research question as a specific, answerable statement.
   - Bad: "How do we improve performance?"
   - Good: "What is the most effective caching strategy for reducing P95 API latency below 200ms?"
2. Define the scope: what is in bounds, what is out of bounds.
3. Define success criteria: what does a satisfactory answer look like?
4. Estimate timebox: how long will you research before making a decision?

### Phase 2: Search
1. Start with the official documentation. It is the most authoritative source.
2. Search for community knowledge: blog posts, Stack Overflow, GitHub issues, Reddit.
3. Search for benchmarks or case studies if performance is a concern.
4. Use multiple search engines and perspectives. Confirmation bias is real.

### Phase 3: Evaluate Sources
1. Check the date: is the information current? Technology evolves quickly.
2. Check the authority: is the source official, well-known, or reputable?
3. Check for bias: is the author selling a product or promoting a specific solution?
4. Cross-reference: do multiple independent sources agree?
5. Verify: can you reproduce the results or claims in your environment?

### Phase 4: Synthesize
1. List the options identified, with pros and cons for each.
2. Compare against the success criteria defined in Phase 1.
3. Identify unknowns or risks that require further investigation.
4. Make a recommendation. A research outcome without a recommendation is incomplete.

### Phase 5: Document and Decide
1. Document the research: question, options evaluated, evidence, recommendation.
2. Share with stakeholders for input.
3. Make the decision. If the decision is "no decision yet," define what additional information is needed.

## Common Mistakes

- **Analysis paralysis**: Researching beyond the point of diminishing returns. Set a timebox and stick to it.
- **Confirmation bias**: Only looking for evidence that supports your preferred solution. Actively seek counterarguments.
- **Trusting outdated information**: A blog post from 2019 about best practices may be wrong or obsolete.
- **No defined success criteria**: If you don't know what "done" looks like, you'll never finish researching.
- **Not documenting the outcome**: Research done but not shared is research wasted. Document the decision and rationale.

## Quality Gates

- [ ] Research question is specific and scoped.
- [ ] Multiple independent sources were consulted.
- [ ] Sources are current (within the relevant timeframe for the topic).
- [ ] A recommendation is made with supporting evidence.
- [ ] Research is documented and shared with the team.
