# Domains & Hosting

Two foundational decisions: the **address** people type (the domain) and the
**place** the site actually runs (the hosting). Both have long‑term
consequences, and both have a few traps that catch people out.

## Domains

### Registering a domain
A domain (e.g., `example.com`) is *rented*, not bought — you register it through
a **registrar** for a period (usually 1–10 years) and renew it.

> ✅ **Do:**
> - Register the domain in the **client/owner's own account**, not the
>   agency's. The owner should control their own domain. This prevents the
>   all‑too‑common hostage situation when a relationship ends.
> - **Enable auto‑renew** and keep the payment method and contact email current.
>   Expired domains cause total, sudden outages — and can be snapped up by
>   others.
> - Turn on **registrar lock** (transfer lock) to prevent unauthorized
>   transfers.
> - Use **WHOIS privacy** where offered to reduce spam and exposure of personal
>   contact details.
> - Enable **two‑factor authentication** on the registrar account. Losing the
>   domain account is losing the domain.

> ❌ **Don't:** Let a single individual's personal email be the sole recovery
> contact for a business‑critical domain.

### Choosing a domain name
- Short, memorable, easy to spell and say aloud.
- Prefer `.com` for broad commercial reach, or a relevant country/topic TLD.
- ⚖️ **Legal note:** Check for **trademark conflicts** before committing — using
  a name that infringes an existing trademark can force a costly rename or
  worse. A quick trademark and existing‑use search is cheap insurance. See
  [copyright & IP](../10-legal-and-compliance/copyright-and-ip.md).

### DNS basics
DNS records connect your domain to services:

- **A / AAAA** — point the domain at a server's IPv4 / IPv6 address.
- **CNAME** — alias one name to another (e.g., `www` → the apex domain or a
  platform host).
- **MX** — where email for the domain is delivered.
- **TXT** — verification and email‑auth records (SPF, DKIM, DMARC).

> 💡 **Tip:** Set up **SPF, DKIM, and DMARC** so email from your domain is
> trusted and harder to spoof. It also protects your reputation from
> impersonation.

See [DNS, domains & SSL](../08-deployment-and-devops/domains-dns-ssl.md) for the
operational detail.

## Hosting

### Types of hosting

| Type | What it is | Good for | Watch out for |
|------|------------|----------|----------------|
| **Shared** | Many sites on one server | Cheap, small sites | "Noisy neighbors," limited control |
| **VPS** | A virtual slice of a server you control | More control, moderate scale | You manage/patch the OS |
| **Dedicated** | A whole physical server | High, predictable load | Cost; you manage everything |
| **Cloud (IaaS)** | On‑demand virtual infrastructure | Scaling, flexibility | Complexity, cost surprises |
| **Managed platform (PaaS)** | Platform handles infra (e.g., managed WordPress, app platforms) | Less ops burden | Some lock‑in, higher unit cost |
| **Serverless / static + CDN** | Functions and static files, no servers to manage | Static/Jamstack sites, spiky load | Cold starts, per‑request pricing |

### What to evaluate
- **Reliability / uptime** and the provider's track record.
- **Performance** — location of data centers relative to users; CDN options.
- **Scalability** — can it handle traffic spikes?
- **Support** — hours, channels, responsiveness.
- **Backups** — does the host take them, how often, and can *you* restore them?
  (Don't assume — verify. See
  [backups](../09-maintenance/backups-and-disaster-recovery.md).)
- **Security** — included TLS, firewalls, DDoS protection, isolation.
- ⚖️ **Data residency / jurisdiction** — where your data physically lives can
  have legal implications (e.g., GDPR international‑transfer rules). See
  [GDPR](../10-legal-and-compliance/gdpr.md).

### TLS/SSL is non‑negotiable
Every site should be served over **HTTPS**. Free, automated certificates (e.g.,
Let's Encrypt) make this easy and most platforms include it. HTTP‑only sites are
flagged as "Not secure," hurt SEO, and expose users. See
[HTTPS & TLS](../07-security/https-and-tls.md).

## Ownership: keep the keys

The recurring theme: **the site owner should control their own accounts** —
domain registrar, hosting, DNS, analytics, and any platform logins. Document
who has access to what. When a project changes hands, this is the difference
between a smooth transition and a crisis.

> ✅ **Do:** Maintain an inventory of all accounts, who owns them, renewal dates,
> and where credentials are stored (in a proper secrets manager, never a
> spreadsheet of plaintext passwords). See
> [secrets management](../07-security/secrets-management.md).
