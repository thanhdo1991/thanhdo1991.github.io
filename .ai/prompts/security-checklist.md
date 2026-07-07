---
id: security-checklist-v1
version: 1.0.0
confidence: 0.90
success_rate: 0.83
last_updated: 2026-06-29
tags:
  - prompt
  - security
  - checklist
  - owasp
  - audit
  - vulnerability
---

Perform a security review on the following:

## Scope
- Target: {{review_target}}
- Version/revision: {{version}}
- Review type: {{review_type}} (code review / architecture review / dependency audit / full assessment)

## OWASP Top 10 (2021) Checklist

### A01: Broken Access Control
- [ ] Proper authorization checks on all protected resources?
- [ ] Role-based access control correctly implemented?
- [ ] No IDOR (Insecure Direct Object References)?
- [ ] API endpoints enforce permissions, not just UI hiding?
- [ ] JWT/session tokens validated on every request?

### A02: Cryptographic Failures
- [ ] Data in transit encrypted (TLS 1.2+)?
- [ ] Data at rest encrypted with strong algorithms?
- [ ] No weak/legacy crypto algorithms used?
- [ ] Secrets, API keys, passwords stored securely (not in code)?
- [ ] Proper key management and rotation practices?

### A03: Injection
- [ ] SQL/NoSQL injection prevention (parameterized queries / ORM)?
- [ ] Command injection prevention (avoid shell execution, use exec APIs safely)?
- [ ] LDAP, XML, expression language injection checked?
- [ ] Input validation and sanitization at trust boundaries?

### A04: Insecure Design
- [ ] Threat modeling performed?
- [ ] Security requirements defined before implementation?
- [ ] Rate limiting on sensitive endpoints?
- [ ] Proper error handling (no stack traces exposed)?

### A05: Security Misconfiguration
- [ ] Default credentials changed?
- [ ] Unnecessary services/features disabled?
- [ ] CORS configured restrictively?
- [ ] Security headers set (CSP, HSTS, X-Frame-Options, X-Content-Type-Options)?
- [ ] Environment-specific configs not in version control?

### A06: Vulnerable and Outdated Components
- [ ] All dependencies scanned for known vulnerabilities?
- [ ] Dependency versions pinned (not floating)?
- [ ] Regular update/patch process in place?
- [ ] Transitive dependencies reviewed?

### A07: Identification and Authentication Failures
- [ ] Multi-factor authentication available where applicable?
- [ ] Session management secure (timeout, rotation, secure cookies)?
- [ ] Password policies enforced (strength, hashing algorithm like bcrypt/argon2)?
- [ ] Account lockout after failed attempts?
- [ ] No credential stuffing vulnerabilities?

### A08: Software and Data Integrity Failures
- [ ] CI/CD pipeline secure (no unauthorized changes)?
- [ ] Software supply chain security (signed commits, artifact verification)?
- [ ] Deserialization of untrusted data handled safely?

### A09: Security Logging and Monitoring Failures
- [ ] Security-relevant events logged (auth attempts, access violations, input validation failures)?
- [ ] Logs include sufficient context (timestamp, user, source IP, action)?
- [ ] No sensitive data in logs?
- [ ] Automated alerting on suspicious patterns?

### A10: Server-Side Request Forgery (SSRF)
- [ ] External URL validation and allowlisting?
- [ ] Internal network access restricted?
- [ ] URL parsing safe from bypass techniques?

## Additional Security Concerns

### Authentication and Authorization
- [ ] OAuth/OIDC flows implemented correctly?
- [ ] API key/token rotation policy defined?
- [ ] Principle of least privilege applied?

### Data Validation
- [ ] File upload validation (type, size, content)?
- [ ] Output encoding to prevent XSS?
- [ ] Proper content-type handling?

### Infrastructure
- [ ] Network segmentation (public/private subnets)?
- [ ] WAF rules configured?
- [ ] Backup and disaster recovery tested?
- [ ] Incident response plan documented?

## Findings Summary
| Severity | Count | Examples |
|----------|-------|---------|
| Critical | {{critical_count}} | {{critical_examples}} |
| High     | {{high_count}}     | {{high_examples}}     |
| Medium   | {{medium_count}}   | {{medium_examples}}   |
| Low      | {{low_count}}      | {{low_examples}}      |

## Recommendations
- {{recommendation_1}}
- {{recommendation_2}}
- {{recommendation_3}}
