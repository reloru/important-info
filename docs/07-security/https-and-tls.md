# HTTPS & TLS

HTTPS encrypts the connection between a user's browser and your server using
**TLS** (Transport Layer Security — the successor to SSL, though people still say
"SSL certificate"). It is the non‑negotiable baseline of web security. Every
site should be HTTPS‑only, no exceptions.

## Why HTTPS is mandatory now

- **Confidentiality** — nobody between the user and server (on public wifi, at an
  ISP, etc.) can read the traffic.
- **Integrity** — content can't be tampered with in transit (no injected ads or
  malware).
- **Authenticity** — the certificate proves users are talking to the real site,
  not an impostor.
- **Trust signals** — browsers mark HTTP sites "**Not secure**," which erodes
  confidence and conversions.
- **SEO** — HTTPS is a ranking signal. See
  [technical SEO](../06-seo/technical-seo.md).
- **Modern features** — many browser APIs (service workers, geolocation, etc.)
  *only* work over HTTPS.

There is no meaningful downside. Certificates are **free and automatable** (e.g.,
Let's Encrypt), and most hosting platforms provision and renew them for you.

## Getting and maintaining certificates

- Use automated issuance/renewal (ACME / Let's Encrypt, or your platform's
  built‑in TLS). Manual certificates expire and cause outages when forgotten.
- **Monitor expiry.** An expired certificate breaks the whole site with a scary
  browser warning. Add certificate expiry to your
  [monitoring](../09-maintenance/monitoring-and-uptime.md).
- Cover all hostnames you use (apex, `www`, subdomains) — mismatches trigger
  warnings.

> ⚠️ Expired certificates are one of the most common *self‑inflicted* outages.
> Automate renewal **and** monitor it — automation can silently fail too.

## Configure it properly

Enabling HTTPS isn't quite the whole job:

- **Redirect HTTP → HTTPS** so nobody lands on the insecure version.
- **HSTS** (`Strict-Transport-Security`) tells browsers to *only* use HTTPS for
  your domain going forward, preventing downgrade attacks. See
  [security headers](security-headers.md).
- **Avoid mixed content** — every resource (images, scripts, styles, fonts) must
  also load over HTTPS, or browsers block or warn about it.
- Use **modern TLS versions** (TLS 1.2/1.3) and disable obsolete protocols and
  weak ciphers.
- Consider **redirecting to a single canonical host** (e.g., `www` or apex, pick
  one) to keep certificates and SEO clean. See
  [technical SEO](../06-seo/technical-seo.md).

## Test your configuration

Use a reputable TLS testing service to check your certificate chain, protocol
versions, and cipher strength. Aim for a clean, modern configuration with no weak
or deprecated options.

## HTTPS is necessary, not sufficient

> 🔒 A padlock means the *connection* is encrypted — it does **not** mean the
> site is safe, honest, or free of vulnerabilities. Phishing sites use HTTPS
> too. HTTPS protects data *in transit*; you still need everything else in this
> section (input validation, auth, patching, headers). Don't let the padlock
> create false confidence.

## The one‑line takeaway

Serve **HTTPS everywhere**, redirect HTTP to it, enable HSTS, avoid mixed
content, use modern TLS, and **automate + monitor** certificate renewal. It's
cheap, it's expected, and going without it is indefensible.
