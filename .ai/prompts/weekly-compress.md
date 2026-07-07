---
id: weekly-compress-v1
version: 1.0.0
confidence: 0.84
success_rate: 0.76
last_updated: 2026-06-29
tags:
  - prompt
  - knowledge-compression
  - maintenance
  - cleanup
  - knowledge-management
---

Perform weekly knowledge compression and cleanup.

## Period
- Week ending: {{week_ending}}
- Total learnings/records created: {{total_records}}

## Summarization
For each category, summarize key learnings and identify what to retain:

### Technical Learnings
Raw entries:
{{technical_entries}}

Compressed summary:
{{technical_summary}}

Key patterns identified:
{{technical_patterns}}

### Process Improvements
Raw entries:
{{process_entries}}

Compressed summary:
{{process_summary}}

### Decision Records
Raw entries:
{{decision_entries}}

Compressed summary:
{{decision_summary}}

### Skill Updates
Changes made this week:
{{skill_changes}}

Pending updates:
{{pending_skill_updates}}

## Cleanup Actions
- [ ] Consolidate duplicate or overlapping knowledge entries
- [ ] Archive outdated information (add archival tag, move to cold storage)
- [ ] Remove entries with retention_priority below {{retention_threshold}}
- [ ] Merge related decision records
- [ ] Update skill confidence scores based on weekly performance data

## Knowledge Base Health
- Total entries: {{total_entries}}
- Entries marked for archival: {{archival_entries}}
- Entries removed: {{removed_entries}}
- New entries this week: {{new_entries}}

## Documentation Updates
- Documents needing updates: {{docs_to_update}}
- Missing documentation identified: {{missing_docs}}

## Next Week Focus
- Areas needing deeper knowledge: {{areas_of_focus}}
- Skills to prioritize: {{skills_to_prioritize}}
