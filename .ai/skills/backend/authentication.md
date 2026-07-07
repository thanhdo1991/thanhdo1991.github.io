---
id: authentication
version: 2.0.0
confidence: 0.85
success_rate: 0.82
last_updated: 2026-06-29
tags:
  - backend
  - authentication
  - security
  - rigid
---

# Authentication

> Rigid skill. Implement authentication securely: hash passwords with bcrypt/argon2, manage JWTs correctly, handle sessions safely, and never roll your own cryptography.

## Rationalization Table

| Common Excuse | Reality |
|---|---|
| "I'll just hash with MD5/SHA, it's fast" | Fast hashing = fast brute-forcing. Password hashing needs to be slow (bcrypt, argon2, scrypt). |
| "We don't need MFA, we have strong passwords" | Password reuse and phishing bypass strong passwords. MFA blocks 99.9% of account takeovers. |
| "I can write a JWT library, it's not that hard" | JWT has 10+ known vulnerabilities. Use a reviewed library. |
| "I'll roll my own encryption, it's more secure" | Custom crypto has never been audited. Standard libraries have hundreds of eyes on them. |

## Process

### Phase 1: Password Handling
1. Use bcrypt (cost factor >= 12) or argon2id (recommended for new projects).
2. Never store plaintext passwords. Never use unsalted hashes (MD5, SHA-1, SHA-256 directly).
3. Enforce password strength: minimum 8 characters, common password check.
4. Rate-limit login attempts: 5 attempts per email per 15 minutes.
5. Never tell the user which field is wrong on login. Always: "Invalid email or password."

### Phase 2: JWT Management
1. Use a reviewed JWT library. Never implement JWT parsing manually.
2. Validate: signature, expiration (`exp`), not-before (`nbf`), issuer (`iss`), audience (`aud`).
3. Use short-lived access tokens (15 minutes). Use refresh tokens (7 days, rotate on use).
4. Store access tokens in memory. Store refresh tokens in httpOnly, secure, SameSite cookies.
5. Implement token revocation: maintain a deny list for critical operations.

### Phase 3: Session Management
1. Generate session IDs with a cryptographically secure random generator.
2. Store sessions server-side (Redis, database). A stolen session cookie should be revocable.
3. Rotate session ID on privilege escalation (login, MFA verification).
4. Set session expiry: idle timeout (30 minutes), absolute timeout (24 hours).
5. Destroy sessions on logout (both client cookie and server-side session).

### Phase 4: MFA
1. Support TOTP (Time-based One-Time Password) as the primary MFA method.
2. Recovery codes: generate 8-10 single-use codes on MFA setup.
3. Require MFA for admin roles, password changes, and sensitive operations.
4. Rate-limit MFA verification: 3 attempts per 5 minutes.

## Red Flags (STOP Signals)

- Passwords stored with MD5, SHA-1, or unsalted SHA-256. Immediate fix required.
- JWT without expiration validation. Tokens that never expire are a permanent backdoor.
- Custom encryption or hash implementations. Rolled-your-own crypto is always wrong.
- Missing rate limiting on login, signup, or password reset.
- Exposing user enumeration (different error messages for "user not found" vs "wrong password").

## No Exceptions

- Do not store passwords with anything other than bcrypt (cost >= 12) or argon2id.
- Do not implement your own cryptographic algorithms, token formats, or authentication protocols.
- Do not send passwords or tokens in URLs or logs.
- Do not disable CSRF protection for cookie-based authentication.
- Do not skip MFA for admin accounts or sensitive operations.
