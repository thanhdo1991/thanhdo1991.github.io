---
id: security-review
version: 2.0.0
confidence: 0.85
success_rate: 0.78
last_updated: 2026-06-29
tags:
  - quality
  - security
  - rigid
---

# Security Review

> Rigid skill. Systematic security review covering OWASP Top 10, dependency audit, SAST analysis, and threat modeling. Every finding must be triaged and addressed before production release.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "We're not a bank, nobody would attack us" | 60% of cyberattacks target small to medium businesses. Automated scanners don't discriminate. |
| "It's behind a VPN, it's safe" | VPNs protect the network, not the application. XSS, SQLi, and logic flaws work over VPN. |
| "We'll fix security issues later" | The cost to fix a vuln in production is 30-100x more than fixing it during development. |
| "Our devs know security best practices" | The average developer has 2 hours of security training per year. Knowledge gaps are systematic. |

## Process

### Phase 1: Threat Modeling
1. Identify assets: user data, credentials, tokens, PII, business logic.
2. Identify threat actors: anonymous users, authenticated users, insiders, third parties.
3. Map trust boundaries: where does data move from low-trust to high-trust zones? Every boundary is a control point.
4. Apply STRIDE per component: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege.

### Phase 2: OWASP Top 10 Review
Check each item against the codebase:
1. Broken Access Control: Are authorization checks present and correct? Can a user access another user's data by changing an ID?
2. Cryptographic Failures: Are secrets hardcoded? Is TLS enforced? Are passwords hashed with bcrypt/argon2?
3. Injection: Are all user inputs parameterized? Is there raw string concatenation in SQL, NoSQL, OS commands, or templates?
4. Insecure Design: Are there missing rate limits, missing access controls, or business logic flaws?
5. Security Misconfiguration: Are default credentials changed? Are debug endpoints exposed? Is CORS too permissive?
6. Vulnerable Components: Are dependencies up to date? Are there known CVEs?
7. Auth/SSO Failures: Are session tokens secure? Is MFA enforced where needed? Are passwords stored securely?
8. Integrity Failures: Are CI/CD pipelines secured? Are signed commits enforced?
9. Logging/Monitoring: Are security events logged? Is there an alert for repeated auth failures?
10. SSRF: Are URLs fetched from user input validated and restricted?

### Phase 3: Dependency Audit
1. Run `npm audit`, `pip audit`, `cargo audit`, or equivalent.
2. For each critical/high vulnerability: understand the impact, determine if it's reachable, and schedule a fix.
3. Check license compliance: are there GPL/AGPL dependencies in a proprietary codebase?

### Phase 4: SAST and Secrets Scanning
1. Run a SAST tool (SonarQube, Semgrep, CodeQL) on the codebase.
2. Run a secrets scanner (truffleHog, Gitleaks) on the repository history.
3. Remediate all true positives. Document and accept false positives.

## Red Flags (STOP Signals)

- Hardcoded secrets, API keys, or database credentials in source code.
- Any form of input concatenated into a SQL/NoSQL query or shell command.
- Missing authentication on any endpoint that returns user data.
- Authorization checks that use client-provided values (user ID from request body, not session).
- `eval()`, `exec()`, or equivalent in application code.

## No Exceptions

- Do not deploy code with known critical or high-severity vulnerabilities.
- Do not store secrets in source code. Use a secrets manager or environment variables.
- Do not roll your own cryptography. Use reviewed, standard libraries.
- Do not bypass authentication or authorization for "testing convenience."
