---
id: workflow-research-001
version: 1.0.0
confidence: 0.82
success_rate: 0.77
last_updated: 2026-06-29
tags: [workflow, research, knowledge]
---

# Research Workflow

Systematic process for answering questions, gathering information, and synthesizing knowledge from multiple sources.

## Flowchart

```
[Research Question] → [Define Scope] → [Gather Sources]
    → [Analyze Sources] → [Enough Info?] → [No] → [Refine Search] → [Gather More]
    → [Yes] → [Synthesize Findings]
    → [Validate: Cross-check Claims] → [Pass?] → [No] → [Re-analyze Contradictions]
    → [Yes] → [Store Knowledge] → [Done]
```

## Trigger

- An open-ended question needs investigation.
- A decision requires supporting evidence.
- A technology/tool needs evaluation.
- A bug's root cause is unclear and requires domain research.
- Pre-requisite to any planning activity (research-backed planning).

## Steps

### 1. Define Scope
- **Input**: Raw research question, context.
- **Process**: Refine the question into a precise, answerable form. Define boundaries (what's in scope, what's out). Identify key sub-questions. Set a depth target (quick overview vs. exhaustive analysis).
- **Output**: Scoped research question with success criteria (what "done" looks like).
- **Quality Gate**: The question is specific enough to be answered in a defined number of sources. Success criteria are clear (e.g., "I can explain X in 3 sentences" or "I have pros/cons for options A, B, C").

### 2. Gather Sources
- **Input**: Scoped question.
- **Process**: Search across: (a) internal memory and past workflows, (b) project documentation and codebase, (c) web search, (d) official documentation, (e) community resources. Prioritize primary/official sources over secondary. Collect diverse perspectives.
- **Output**: Curated list of sources with relevance scores.
- **Decision Point**: [Source Quality?] → [Primary/Authoritative] → [High weight] | [Secondary/Community] → [Low weight, cross-check] | [Unreliable] → [Discard].
- **Quality Gate**: At least 3 independent sources for any factual claim. No source is older than the relevance window for the topic. For technology evaluation, at least one source is official documentation.

### 3. Analyze Sources
- **Input**: Curated sources.
- **Process**: Read each source. Extract key facts, data points, arguments, and quotes. Note contradictions between sources. Assess the reliability of each source for the specific claim.
- **Output**: Annotated notes per source with extracted claims and confidence ratings.
- **Quality Gate**: Each source is read completely (not cherry-picked). Conflicting claims are noted, not ignored. Analysis distinguishes between fact and opinion.

### 4. Sufficiency Check
- **Input**: Annotated notes.
- **Process**: Assess whether the gathered information is sufficient to answer the research question with confidence. If gaps remain, identify what's missing.
- **Decision Point**: [Enough Info?] → [Yes] → [Proceed to Synthesize] | [No, missing key data] → [Refine search terms] → [Gather more sources] | [No, contradictions unresolved] → [Deep-dive on conflicting claims].
- **Output**: Go/no-go decision on synthesis phase.
- **Quality Gate**: Decision is explicit. If proceeding despite gaps, document what's unknown.

### 5. Synthesize Findings
- **Input**: Annotated notes, sufficiency decision.
- **Process**: Organize findings into a coherent answer. Structure by sub-questions. Identify the most supported conclusion. Flag remaining uncertainties. Format for the intended audience.
- **Output**: Synthesis document (structured answer with supporting evidence).
- **Quality Gate**: Synthesis directly answers the scoped question. Each claim is traceable to its source. Uncertainties and confidence levels are clearly communicated.

### 6. Validate Claims
- **Input**: Synthesis document.
- **Process**: Cross-check every factual claim against at least one other source. Test code examples. Verify version-specific information. Check for recency (stale information).
- **Output**: Validation report (verified claims, unverifiable claims, corrections).
- **Decision Point**: [All Key Claims Verified?] → [Yes] → [Store Knowledge] | [No, contradictions remain] → [Re-analyze contradictions or flag as uncertain].
- **Quality Gate**: No unverified factual claim is presented as fact. Uncertain claims are explicitly labeled as such.

### 7. Store Knowledge
- **Input**: Validated synthesis.
- **Process**: Format the synthesis for memory storage. Add contextual tags, related topics, and retrieval keywords. If the research produced actionable decisions or patterns, update decisions.md and patterns.md accordingly.
- **Output**: Stored knowledge entry.
- **Quality Gate**: Entry is findable by the original research question and by related concepts. Entry includes a summary section for quick recall.

## Output

- Research synthesis (structured answer).
- Source list with annotations.
- Confidence assessment per key claim.
- Updated memory (relevant patterns, decisions).
- (Optional) Recommendation if the research was decision-oriented.
