# Monitoring & Uptime

Monitoring is how you find out about problems **before your users do** (or at
least the moment they do). A site without monitoring can be down, broken, or
under attack for hours before anyone notices — usually via an angry email. Good
monitoring turns silent failures into prompt alerts.

## What to monitor

### Availability (uptime)
Is the site up and responding? An external service that checks your site from
outside on a schedule and alerts you when it can't reach it. Check key pages, not
just the homepage.

### Errors
Are users hitting failures? Track server errors (5xx), client errors (spikes in
4xx), and application exceptions. **Error tracking** tools capture and group
exceptions with the context to debug them.

### Performance
Is it fast? Track response times and real‑user
[Core Web Vitals](../05-performance/core-web-vitals.md) over time. A gradual
slowdown is a problem you want to catch before it becomes an outage. See
[performance budgets](../05-performance/performance-budgets.md).

### Certificates & domains
> ⚠️ Monitor **TLS certificate expiry** and **domain expiry** with alerts well in
> advance. These cause sudden, total, entirely‑avoidable outages. See
> [DNS, domains & SSL](../08-deployment-and-devops/domains-dns-ssl.md).

### Security signals
Watch for anomalies: spikes in failed logins, unusual traffic, unexpected file
changes, or admin actions. Ties into
[OWASP: logging & monitoring](../07-security/owasp-top-10.md).

### Infrastructure
Server/resource health (CPU, memory, disk, database) so you catch capacity
problems before they cause failures. **Disk filling up** is a classic silent
killer.

### Backups & jobs
Alert on **backup failures** and other scheduled jobs — a backup that quietly
stops running is discovered at the worst possible moment. See
[backups](backups-and-disaster-recovery.md).

## Alerting: make it actionable

Monitoring is only useful if the right person is told, promptly, when something's
wrong.

> ✅ **Do:**
> - Route alerts to a channel/person who will actually see and act on them.
> - Set thresholds that catch real problems.
> - Include enough context to start diagnosing.
> - Define severity levels and who responds to each.

> ❌ **Don't:**
> - Create so many noisy alerts that people tune them out ("alert fatigue"). An
>   ignored alert is worse than none.
> - Alert on things nobody will act on.

## Logs

Logs are your record of what happened — essential for debugging and for
investigating incidents.

- Log **security‑relevant events** (logins, admin actions, access failures).
- **Centralize** logs so you can search across systems.
- **Protect** logs (they can contain sensitive data) and set sensible retention.
- ⚖️ Be mindful of **privacy** — don't log more personal data than you need, and
  account for logs in your data‑protection practices. See
  [GDPR](../10-legal-and-compliance/gdpr.md).

## Synthetic vs. real‑user monitoring

- **Synthetic** — scripted checks that probe your site on a schedule from
  outside. Great for uptime and catching outages fast.
- **Real‑user monitoring (RUM)** — data from actual visitors' sessions. Great for
  understanding real‑world performance and errors across devices/networks.

Use both: synthetic to know *that* something's down, RUM to understand what your
users actually experience.

## Uptime, SLAs, and expectations

- **Uptime** is the percentage of time the site is available (99.9% ≈ ~8.8 hours
  of downtime per year; 99.99% ≈ ~53 minutes).
- An **SLA** (Service Level Agreement) is a commitment about it — relevant if you
  promise availability to clients/customers, or rely on a provider's promise.
- Know your providers' SLAs and design redundancy for anything you can't afford
  to have fail.

## Close the loop

Monitoring feeds [incident response](incident-response.md): an alert kicks off
your response process. After an incident, review whether monitoring caught it in
time — if not, add the check that would have. Over time, your monitoring should
get better at catching the things that actually go wrong.

> The goal: **you find out first, and you find out early.** Everything else in
> operations depends on that.
