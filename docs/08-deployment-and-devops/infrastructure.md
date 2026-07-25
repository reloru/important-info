# Infrastructure

Infrastructure is the underlying compute, storage, networking, and services your
site runs on. You don't always manage it directly — managed platforms handle much
of it for you — but understanding the options and principles helps you choose
well and operate reliably.

## The spectrum of "how much do I manage?"

From most to least hands‑on:

| Model | You manage | Provider manages | Trade‑off |
|-------|-----------|------------------|-----------|
| **Self‑managed servers / IaaS** | OS, runtime, app, scaling | Hardware, network | Max control, max responsibility |
| **Containers (e.g., Docker/Kubernetes)** | App + container config, sometimes orchestration | Underlying hosts | Portable, consistent; complex |
| **PaaS (platform as a service)** | Your app | OS, runtime, scaling | Less ops burden; some constraints |
| **Serverless / functions** | Your code | Everything else, scaling | Minimal ops; per‑request pricing, cold starts |
| **Static hosting + CDN** | Your built files | Serving, scaling, TLS | Simplest, cheapest for static; needs services for dynamic bits |

There's no single "best" — match the model to your site's complexity, team
skills, and budget. See
[choosing a tech stack](../01-planning-and-strategy/choosing-a-tech-stack.md).

## Containers, briefly

**Containers** package an app with its dependencies so it runs the same
everywhere — solving "works on my machine." They make environments consistent and
deployments portable. **Orchestration** (like Kubernetes) manages many containers
at scale but adds significant complexity; most small‑to‑medium sites don't need
it, and reaching for it prematurely is a common form of over‑engineering.

## Infrastructure as Code (IaC)

Rather than clicking around a console to set things up (which is
unrepeatable and undocumented), **define infrastructure in code** (e.g.,
Terraform, CloudFormation, Pulumi, or platform config files).

Benefits:

- **Repeatable & consistent** — spin up identical environments on demand.
- **Version‑controlled** — changes are reviewed and tracked like any code. See
  [version control](../03-development-best-practices/version-control.md).
- **Documented by definition** — the code *is* the documentation of your setup.
- **Recoverable** — rebuild from scratch after a disaster. See
  [disaster recovery](../09-maintenance/backups-and-disaster-recovery.md).

> ✅ **Do:** Prefer declarative, version‑controlled infrastructure over manual
> console changes, especially as complexity grows.

## Reliability & scaling considerations

- **Scalability** — can it handle traffic growth and spikes? Vertical (bigger
  server) vs. horizontal (more servers) scaling; auto‑scaling where supported.
- **Redundancy** — avoid single points of failure for anything critical.
- **Backups** — of data *and* configuration. See
  [backups](../09-maintenance/backups-and-disaster-recovery.md).
- **Monitoring** — know the health of your infrastructure. See
  [monitoring](../09-maintenance/monitoring-and-uptime.md).

## Security of infrastructure

> 🔒 **Security note:**
> - **Least privilege** for infrastructure access and service accounts.
> - **Network controls** — firewalls, private networks, security groups; expose
>   only what must be public.
> - **Patch** the OS and platform components (or choose managed options that do
>   it for you). Unpatched infrastructure is a top breach vector. See
>   [dependency management](../09-maintenance/dependency-management.md).
> - **Review cloud storage/service permissions** — misconfigured public buckets
>   are a recurring cause of data leaks (see
>   [OWASP: security misconfiguration](../07-security/owasp-top-10.md)).

## Cost awareness

Cloud and serverless bills can surprise you — usage‑based pricing scales with
traffic (and with mistakes, like a runaway process or an attack).

> ✅ **Do:** Set **budgets and billing alerts.** Understand what drives cost.
> Factor infrastructure into your
> [run budget](../01-planning-and-strategy/budgeting-and-scoping.md).

## Data residency & jurisdiction

> ⚖️ **Legal note:** *Where* your infrastructure physically lives can have legal
> consequences — data‑protection laws restrict international transfers of
> personal data, and some contracts or regulations require data to stay in a
> specific region. Choose regions deliberately. See
> [GDPR](../10-legal-and-compliance/gdpr.md).

## Keep it as simple as the problem allows

The best infrastructure is the simplest one that meets your reliability and scale
needs. Every layer you add is another thing to secure, patch, monitor, and pay
for. Start simple; add complexity only when a real need justifies it.
