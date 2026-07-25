# DNS, Domains & SSL (Operations)

This page covers the operational side of making a domain resolve to your site
securely — the plumbing that, when it fails, takes the *whole site* down at once.
For the strategic side (choosing and owning a domain), see
[domains & hosting](../01-planning-and-strategy/domains-and-hosting.md).

## How a request finds your site

1. A user types `example.com`.
2. **DNS** translates that name into your server/CDN's IP address.
3. The browser connects and negotiates **TLS** (HTTPS) using your certificate.
4. Your server (or CDN edge) responds with the page.

Every link in that chain is a potential point of failure — and several fail
*silently until they don't*.

## DNS records you'll actually use

| Record | Purpose |
|--------|---------|
| **A** | Points a name to an IPv4 address |
| **AAAA** | Points a name to an IPv6 address |
| **CNAME** | Aliases one name to another (e.g., `www` → apex or a platform host) |
| **MX** | Where email for the domain is delivered |
| **TXT** | Verification and email auth (SPF, DKIM, DMARC) |
| **NS** | Which nameservers are authoritative for the domain |
| **CAA** | Restricts which certificate authorities may issue certs for the domain |

### TTL and propagation
DNS records have a **TTL** (time to live) that controls how long they're cached.
Changes take time to "propagate" as caches expire. Before a planned migration,
**lower the TTL** ahead of time so the cutover is fast; raise it again once
stable.

## Common DNS operations

- **Pointing the domain** at your host/CDN (A/AAAA or CNAME).
- **`www` vs. apex** — decide on one canonical host and redirect the other; keep
  it consistent for SEO and certificates. See
  [technical SEO](../06-seo/technical-seo.md).
- **Email authentication** — set **SPF**, **DKIM**, and **DMARC** so your
  domain's email is trusted and harder to spoof. Protects deliverability and
  your reputation.
- **Subdomains** — for staging, apps, docs, etc. Keep non‑public ones protected.

## TLS/SSL certificates in operation

- **Automate issuance and renewal** (ACME / Let's Encrypt or your platform's
  built‑in TLS). Manual certs get forgotten and expire.
- **Cover every hostname** you serve (apex, `www`, subdomains) — mismatches
  trigger browser warnings.
- **Redirect HTTP → HTTPS** and enable **HSTS**. See
  [HTTPS & TLS](../07-security/https-and-tls.md) and
  [security headers](../07-security/security-headers.md).
- Use **CAA records** to limit which authorities can issue certificates for your
  domain — a small anti‑misissuance safeguard.

## The silent‑outage checklist

The most painful outages come from things that expire or lapse with no code
change at all. Guard against them:

- [ ] **Domain auto‑renew** enabled; billing and contact details current.
- [ ] **TLS certificate auto‑renew** working — *and monitored* (automation fails
      too).
- [ ] **Certificate expiry monitoring** with alerts well before expiry.
- [ ] **Domain expiry monitoring** / calendar reminders.
- [ ] **Registrar and DNS account** secured with MFA and recorded ownership. See
      [secrets management](../07-security/secrets-management.md).
- [ ] **DNS provider** reliability considered (it's a single point of failure).

> ⚠️ An expired domain or certificate is a total, sudden, embarrassing outage —
> and one of the most common. Monitor both. See
> [monitoring & uptime](../09-maintenance/monitoring-and-uptime.md).

## Plan migrations carefully

Changing hosts or DNS providers is delicate:

- Lower TTLs in advance.
- Set up and verify the new destination **before** switching.
- Keep the old destination live until propagation completes and you've
  confirmed the new one works.
- Have a **rollback** (revert the DNS change) ready.
- Watch for certificate and mixed‑content issues on the new host.

Done carefully, DNS/TLS operations are invisible. Done carelessly, they're the
cause of your worst outages — so treat them with the same rigor as code changes.
