# OWASP Top 10

The **OWASP Top 10** is a widely‑referenced, regularly‑updated list of the most
critical web application security risks, published by the Open Worldwide
Application Security Project. It's the standard starting point for understanding
what goes wrong and how to prevent it. This page summarizes the categories and
their defenses at a conceptual level — always check the current official list for
the latest version and detail.

> This is an educational overview, not a substitute for a proper security review
> of your specific application. For higher‑risk apps, get a professional
> assessment.

## The categories (recent editions)

### 1. Broken Access Control
Users can act outside their intended permissions — viewing others' data,
accessing admin functions, changing records they shouldn't.
- **Defend:** Enforce authorization on the **server** for every request; deny by
  default; never rely on hiding UI or client‑side checks. Verify object‑level
  ownership ("is this *my* order?"). See
  [authorization](authentication-and-authorization.md).

### 2. Cryptographic Failures
Sensitive data exposed through weak or missing encryption.
- **Defend:** HTTPS everywhere; encrypt sensitive data at rest; use strong,
  modern algorithms; hash passwords with a strong, salted algorithm (never store
  plaintext); don't roll your own crypto. See [HTTPS & TLS](https-and-tls.md).

### 3. Injection (incl. SQL injection, XSS)
Untrusted input is interpreted as code or commands.
- **SQL injection:** use **parameterized queries / prepared statements** — never
  build queries by concatenating user input.
- **Cross‑site scripting (XSS):** **escape/encode output** by context; sanitize
  HTML; use a [Content Security Policy](security-headers.md).
- **General rule:** validate input, encode output, never trust either.

### 4. Insecure Design
Flaws baked into the architecture, not just the code.
- **Defend:** Threat‑model early; design with security in mind; establish secure
  patterns and reuse them. You can't patch your way out of a bad design.

### 5. Security Misconfiguration
Default credentials, unnecessary features enabled, verbose errors, open cloud
storage, missing hardening.
- **Defend:** Harden defaults; disable what you don't use; keep environments
  consistent; don't leak stack traces to users; review cloud/storage permissions.
  See [security headers](security-headers.md).

### 6. Vulnerable & Outdated Components
Using libraries, frameworks, plugins, or platforms with known vulnerabilities.
This is one of the **most common** real‑world causes of compromise.
- **Defend:** Inventory dependencies; scan for known vulnerabilities; update
  promptly; remove unused components. See
  [dependency management](../09-maintenance/dependency-management.md).

### 7. Identification & Authentication Failures
Weak login: guessable passwords, credential stuffing, poor session handling.
- **Defend:** Enforce strong credentials; offer/require MFA; rate‑limit and lock
  out brute force; manage sessions securely; protect password reset flows. See
  [authentication](authentication-and-authorization.md).

### 8. Software & Data Integrity Failures
Trusting code/updates/data without verifying integrity (e.g., compromised
dependencies or update channels — "supply chain" risks).
- **Defend:** Verify sources and signatures; lock dependency versions; secure
  your build/deploy pipeline. See [CI/CD](../08-deployment-and-devops/ci-cd.md).

### 9. Security Logging & Monitoring Failures
Without logging and alerting, breaches go unnoticed for a long time.
- **Defend:** Log security‑relevant events; monitor and alert on anomalies;
  protect and retain logs appropriately (mindful of privacy). See
  [monitoring](../09-maintenance/monitoring-and-uptime.md).

### 10. Server‑Side Request Forgery (SSRF)
The server is tricked into making requests to unintended destinations (e.g.,
internal systems).
- **Defend:** Validate and restrict outbound requests; use allow‑lists; isolate
  network segments.

## Cross‑cutting defenses (worth internalizing)

> ✅ **Do:**
> - **Validate input, encode output** — the antidote to most injection.
> - **Parameterize** every database query.
> - **Authorize on the server** for every action; deny by default.
> - **Keep everything patched.** The boring one that prevents the most breaches.
> - **HTTPS + security headers** on everything.
> - **Least privilege** for users, services, database accounts, and API keys.
> - **Log and monitor**; be ready to detect and respond.

> ❌ **Don't:**
> - Trust client‑side validation for security (it's for UX; attackers bypass
>   it).
> - Store passwords in plaintext or with weak hashing.
> - Expose secrets or verbose errors to users.
> - Assume "we're too small to be attacked" — bots don't discriminate.

## Keep current

The OWASP Top 10 is revised periodically and there are focused lists for APIs,
mobile, and more. Treat the official OWASP site as the source of truth, and
revisit it — the threat landscape shifts.
