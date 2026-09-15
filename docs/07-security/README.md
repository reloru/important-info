# 07 · Security

Security is about protecting your site, your data, and — most importantly —
**your users** from harm. A breach can mean stolen data, defaced pages,
ransomware, legal liability, and destroyed trust. Most real‑world compromises
don't come from sophisticated attacks; they come from **unpatched software, weak
credentials, and predictable mistakes.**

## The mindset

- **Security is a process, not a product.** You don't "add security" at the end;
  you build securely and maintain it continuously.
- **Defense in depth.** Assume any single control can fail; layer them so one
  failure isn't a catastrophe.
- **Least privilege.** Give every user, service, and key the *minimum* access it
  needs — no more.
- **Never trust input.** Treat all data from users, URLs, and third parties as
  potentially hostile until validated.
- **Assume you'll be targeted.** Automated bots probe every site constantly.
  Being small is not protection.

## In this section

- **[OWASP Top 10](owasp-top-10.md)** — the most common, impactful web
  vulnerabilities and how to avoid them.
- **[HTTPS & TLS](https-and-tls.md)** — encrypting traffic (non‑negotiable).
- **[Authentication & authorization](authentication-and-authorization.md)** —
  verifying who users are and what they may do.
- **[Secrets management](secrets-management.md)** — keeping keys and credentials
  out of harm's way.
- **[Security headers](security-headers.md)** — browser‑level protections you
  get almost for free.

Forms are where most user input enters your site, so the practical companion to
this section lives in the development chapter:
**[forms & input handling](../03-development-best-practices/forms-and-input-handling.md)**
— server‑side validation, spam and abuse controls, file uploads, and rate limiting.

## The highest‑value basics

If you do nothing else, do these:

1. **Serve HTTPS everywhere.** See [HTTPS & TLS](https-and-tls.md).
2. **Keep everything updated.** Patch the OS, framework, CMS, plugins, and
   dependencies promptly — this prevents the majority of compromises. See
   [dependency management](../09-maintenance/dependency-management.md).
3. **Use strong, unique credentials + MFA** on every account.
4. **Validate and sanitize all input**; use parameterized queries. See
   [OWASP Top 10](owasp-top-10.md) and
   [forms & input handling](../03-development-best-practices/forms-and-input-handling.md).
5. **Never commit secrets.** See [secrets management](secrets-management.md).
6. **Back up** — and test restores — so you can recover. See
   [backups](../09-maintenance/backups-and-disaster-recovery.md).
7. **Apply security headers.** See [security headers](security-headers.md).

For a copy‑ready audit of all of this and more — to run before launch and
periodically after — use the
[security hardening checklist](../templates/security-hardening-checklist.md).

## Security and the law are intertwined

> ⚖️ **Legal note:** Data‑protection laws require you to protect personal data
> with "appropriate technical and organizational measures," and many
> jurisdictions have **mandatory breach‑notification** rules with tight
> deadlines (e.g., GDPR's 72 hours). A security failure is often also a legal
> event. See [GDPR](../10-legal-and-compliance/gdpr.md) and
> [incident response](../09-maintenance/incident-response.md).

Security is not a specialist afterthought — it's woven through development,
deployment, and maintenance. Every section of this knowledge base touches it.
