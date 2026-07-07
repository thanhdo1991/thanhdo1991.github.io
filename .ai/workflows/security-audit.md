---
id: workflow-security-audit-001
version: 1.0.0
confidence: 0.82
success_rate: 0.75
last_updated: 2026-06-29
tags: [workflow, security, audit]
---

# Security Audit Workflow

Comprehensive security assessment covering threat modeling, static analysis, dependency scanning, and remediation tracking.

## Flowchart

```
[Audit Triggered] → [Threat Model: Identify Assets & Threats]
    → [Scan Dependencies] → [SAST: Static Analysis]
    → [Manual Pen Test (High-Risk Areas)] → [Analyze Results]
    → [Prioritize: Critical/High/Medium/Low]
    → [Blocking Findings?] → [Yes] → [Create Fix Tasks] → [Update & Re-verify]
    → [No] → [Report: Document Findings]
    → [Update Security Memory] → [Done]
```

## Trigger

- Scheduled recurring audit (e.g., monthly or per-release).
- New dependency with known vulnerabilities is introduced.
- Major architectural change that may affect security posture.
- Incident postmortem identifies systemic security gaps.
- Compliance requirement (e.g., SOC 2, PCI-DSS, GDPR review).

## Steps

### 1. Threat Model
- **Input**: System architecture, data flow diagrams, asset inventory.
- **Process**: Identify: (a) assets worth protecting (PII, credentials, IP), (b) threat actors and their capabilities, (c) attack vectors, (d) trust boundaries, (e) existing controls. Use STRIDE or similar framework per component.
- **Output**: Threat model document (assets, threats, controls, risk ratings).
- **Quality Gate**: Every critical data flow has an identified threat. No trust boundary crosses from lower to higher trust without a corresponding control. The model covers both external and insider threats.

### 2. Scan Dependencies
- **Input**: Lock files (package.json, requirements.txt, Cargo.toml, etc.), container images.
- **Process**: Run dependency vulnerability scanners (npm audit, cargo audit, grype, trivy, etc.). Cross-reference CVE database. Check for outdated or deprecated packages.
- **Output**: Dependency vulnerability report (package, version, CVE, severity, fix available).
- **Quality Gate**: All direct and transitive dependencies are scanned. Dev dependencies are included if they affect the build pipeline. False positives are noted but not ignored.

### 3. SAST (Static Analysis)
- **Input**: Full source code.
- **Process**: Run SAST tools (Semgrep, CodeQL, SonarQube, etc.) configured with security-focused rulesets. Focus on: injection flaws, XSS, insecure crypto, path traversal, hardcoded secrets, unsafe deserialization.
- **Output**: SAST findings (file, line, rule, severity, suggested fix).
- **Quality Gate**: SAST covers the entire codebase (not just changed files). Custom rules exist for project-specific patterns. Results are deduplicated.

### 4. Manual Penetration Test
- **Input**: Threat model, SAST results, high-risk areas.
- **Process**: For critical or high-risk components: manual testing of authentication, authorization, input validation, session management, and business logic flaws. Test common OWASP Top 10 scenarios. Only as deep as the risk warrants (full pentest for critical systems, spot-check for low-risk).
- **Output**: Manual test findings with reproduction steps.
- **Quality Gate**: Manual tests cover all trust boundaries identified in the threat model. Findings have reproducible PoC steps. If automated testing covered the area, manual testing validates the automation.

### 5. Analyze & Prioritize
- **Input**: All findings from steps 2-4.
- **Process**: Correlate findings across scanners. Deduplicate. Prioritize by CVSS score (or equivalent) combined with business impact and exploitability. Tag each finding: Critical, High, Medium, Low, Informational.
- **Output**: Prioritized findings list with combined score.
- **Quality Gate**: Prioritization considers both technical severity and business context. Duplicate findings across scanners are merged (not double-counted). Each finding has a recommended remediation.

### 6. Remediation Decision
- **Input**: Prioritized findings.
- **Process**: For each blocking finding (Critical/High): create a fix task. Determine if a hotfix is needed or if it can wait for the next release cycle. Assign owner and timeline.
- **Decision Point**: `[Blocking Findings?] → [Yes] → [Create fix tasks] → [Fix → Re-scan → Verify] | [No blocking findings] → [Log as known issues for next cycle]`.
- **Output**: Fix tasks with owners and deadlines. Known-issues log for non-blocking items.
- **Quality Gate**: Critical findings have a fix timeline within 48 hours. High findings within the current release cycle. Medium/Low are acknowledged with a planned cycle.

### 7. Report
- **Input**: All findings, remediation actions, verification results.
- **Process**: Compile the audit report: executive summary, finding details by severity, remediation status, metrics (findings found/fixed/remaining, scan coverage, time-to-fix). Include recommendations for systemic improvements.
- **Output**: Security audit report.
- **Quality Gate**: Executive summary is readable by non-technical stakeholders. Technical sections include enough detail for developers to act.

### 8. Update Security Memory
- **Input**: Audit report, fix details.
- **Process**: Update memory with: (a) recurring vulnerability patterns (update patterns.md), (b) security decisions made (update decisions.md), (c) new security checks added to workflows, (d) false positive patterns to reduce noise in future scans.
- **Output**: Updated memory artifacts.
- **Quality Gate**: Learnings from this audit feed into the next audit (reduced false positives, new custom rules, improved scanning configuration).

## Output

- Threat model document.
- Dependency scan report.
- SAST results.
- Manual penetration test findings (if applicable).
- Prioritized finding list with remediation status.
- Security audit report (executive + technical).
- Fix tasks for blocking findings.
- Updated security knowledge in memory.
