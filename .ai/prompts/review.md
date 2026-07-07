---
id: review
version: 1.0.0
confidence: 0.85
success_rate: 0.82
last_updated: 2026-06-29
tags: [prompt, review, quality]
---

# Review

Run a structured review of completed work. Delegates to the review-check prompt for detailed analysis.

## Usage
Use this prompt to trigger a self-review after completing a task. For the full review checklist covering correctness, security, performance, and edge cases, use **review-check.md**.

## Process
1. Load the work item (diff, files, or description)
2. Open `prompts/review-check.md` and follow the checklist
3. Categorize findings by severity (Critical/Major/Minor)
4. Provide an overall verdict and recommendations

## Template
Reviewing: {{work_description}}
Files: {{files_changed}}
Focus: {{review_focus}}
