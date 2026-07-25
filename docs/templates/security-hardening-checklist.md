# Security Hardening Checklist

A copy‑ready security audit you can run **before launch and periodically after**
(quarterly is a good cadence — see the [maintenance plan](../09-maintenance/maintenance-plan.md)).
It's deeper and more security‑specific than the security block in the broad
[pre‑launch checklist](pre-launch-checklist.md). For the reasoning behind each
item, follow the links into the [Security section](../07-security/README.md).

> 🔒 This reduces risk; it does not guarantee security. For higher‑risk apps
> (payments, accounts, sensitive data), add a professional review / penetration
> test. Nothing here is a substitute for building securely from the start.

## Transport & headers
- [ ] **HTTPS everywhere**; HTTP redirects to HTTPS; valid, auto‑renewing certs
      covering all hostnames. See [HTTPS & TLS](../07-security/https-and-tls.md).
- [ ] **HSTS** enabled (consider `preload` once all subdomains are HTTPS).
- [ ] **Content‑Security‑Policy** in place (built up via report‑only first);
      `X‑Content‑Type‑Options: nosniff`; clickjacking protection
      (`frame-ancestors`/`X‑Frame‑Options`); sensible `Referrer‑Policy`;
      `Permissions‑Policy` disabling unused features. See
      [security headers](../07-security/security-headers.md).
- [ ] No **mixed content**; modern TLS versions only; weak ciphers disabled.

## Authentication
- [ ] Passwords stored with a strong, salted hash (bcrypt/scrypt/Argon2) —
      **never** plaintext. See
      [authentication & authorization](../07-security/authentication-and-authorization.md).
- [ ] **MFA** offered to users and **required for admin/privileged** accounts.
- [ ] Login/reset flows **rate‑limited**; no account enumeration; reset tokens
      time‑limited and single‑use.
- [ ] Sessions use **`Secure` + `HttpOnly` + `SameSite`** cookies; sessions expire;
      IDs regenerate on login; logout works.
- [ ] **CSRF** protection on state‑changing requests.

## Authorization
- [ ] Authorization enforced on the **server for every request** (UI hiding is not
      security).
- [ ] **Deny by default**; new endpoints locked down until deliberately opened.
- [ ] **Object‑level ownership** verified (can a user reach *another* user's record
      by changing an ID?).
- [ ] **Least privilege** for users, admins, service accounts, DB accounts, and API
      keys.

## Input, output & data
- [ ] **Input validated**, **output encoded** per context (defense against XSS).
- [ ] **Parameterized queries** everywhere (no string‑concatenated SQL).
- [ ] Sensitive data **encrypted at rest**; only necessary data collected/retained
      (data minimization — ⚖️ see [privacy & compliance checklist](privacy-compliance-checklist.md)).
- [ ] File uploads validated (type/size) and stored safely; SSRF‑prone outbound
      requests restricted/allow‑listed. See [OWASP Top 10](../07-security/owasp-top-10.md).

## Secrets
- [ ] **No secrets in code, front‑end, or version control**; stored in env/secret
      manager. See [secrets management](../07-security/secrets-management.md).
- [ ] **Secret scanning** enabled on repos/CI; leaked secrets **rotated** (not just
      deleted).
- [ ] Secrets **separated per environment**; unused credentials revoked; rotation
      on staff departure.

## Dependencies & supply chain
- [ ] **Dependency/vulnerability scanning** enabled; **critical patches applied
      promptly**. See [dependency management](../09-maintenance/dependency-management.md).
- [ ] Lockfiles pin versions; update sources verified; unused/abandoned
      dependencies removed.
- [ ] CI/CD pipeline access limited; third‑party build actions pinned and trusted.
      See [CI/CD](../08-deployment-and-devops/ci-cd.md).

## Configuration & infrastructure
- [ ] Default credentials changed; unnecessary features/ports disabled.
- [ ] **Verbose errors/stack traces disabled** in production; version‑revealing
      headers minimized.
- [ ] Cloud storage/service permissions reviewed (no accidentally public buckets).
- [ ] Admin interfaces restricted (network/IP where feasible) and MFA‑protected.
- [ ] OS/platform components patched (or a managed option handles it).

## Detection & response
- [ ] **Security‑relevant events logged** (logins, admin actions, access failures);
      logs centralized, protected, and privacy‑aware. See
      [monitoring & uptime](../09-maintenance/monitoring-and-uptime.md).
- [ ] **Alerting** on anomalies (failed‑login spikes, unusual traffic).
- [ ] **Backups** exist, follow 3‑2‑1, include an offline/immutable copy, and a
      **restore has been tested**. See
      [backups & disaster recovery](../09-maintenance/backups-and-disaster-recovery.md).
- [ ] **Incident‑response plan** ready, including **breach‑notification** duties
      (⚖️ GDPR 72h and others). See
      [incident response](../09-maintenance/incident-response.md).

---

> Run this **periodically**, not just once — security regresses as code,
> dependencies, and threats change. Record what you checked and when (useful for
> diligence and audits).
