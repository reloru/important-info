# 09 · Maintenance & Operations

This is the phase everyone underestimates and the one where most real‑world sites
fail. A website is **not a project you finish** — it's a product you operate.
Launch is the *start* of a site's life, not the end. Neglected sites don't stay
still; they rot: dependencies grow vulnerable, certificates expire, content goes
stale, and small problems become emergencies.

## Why maintenance is non‑negotiable

An unmaintained website accumulates risk silently:

- **Security** — unpatched software is the #1 cause of compromise. Vulnerabilities
  are discovered constantly; a site frozen in time becomes more exploitable every
  month.
- **Availability** — expired domains/certificates and unmonitored failures cause
  sudden outages.
- **Correctness** — browsers, platforms, and integrations change and break old
  code.
- **Trust & SEO** — stale content, dead links, and errors erode both.
- **Compliance** — laws change; a policy that was fine last year may not be now.

> The cheapest maintenance is regular and boring. The most expensive is the
> emergency you get when you skip it.

## In this section

- **[Maintenance plan](maintenance-plan.md)** — a recurring schedule of what to
  do and when.
- **[Dependency management](dependency-management.md)** — keeping software
  updated safely.
- **[Backups & disaster recovery](backups-and-disaster-recovery.md)** — being
  able to recover from anything.
- **[Monitoring & uptime](monitoring-and-uptime.md)** — knowing there's a problem
  before your users tell you.
- **[Incident response](incident-response.md)** — a calm, prepared plan for when
  things go wrong.
- **[Content updates](content-updates.md)** — keeping the site accurate and
  fresh.

## The maintenance mindset

> ✅ **Do:**
> - Treat maintenance as a **funded, scheduled, owned** responsibility — not an
>   afterthought.
> - **Assign an owner** for every ongoing task (patching, backups, renewals,
>   monitoring, content). See
>   [roles & responsibilities](../00-getting-started/roles-and-responsibilities.md).
> - **Automate** the repetitive parts (updates, backups, monitoring, cert
>   renewal).
> - **Test your recovery**, not just your backups.

> ❌ **Don't:**
> - Launch and walk away.
> - Assume "it's working, so leave it alone" — working today ≠ safe tomorrow.
> - Skip updates because "if it ain't broke." Security‑wise, it's often already
>   broken; you just don't know yet.

## Budget for it

Maintenance has a real, recurring cost. It belongs in the budget from day one —
see [budgeting & scoping](../01-planning-and-strategy/budgeting-and-scoping.md).
A site with no maintenance budget is an incident waiting for a date.
