# Budgeting & Scoping

Most website budgets are wrong in the same way: they account for the **build**
and forget the **life**. A website is a product you operate, not a project you
finish. Budget for both.

## The two budgets

### 1. Build budget (one‑time)
- Discovery, planning, and IA.
- Design (UX, visual, design system).
- Content creation (writing, photography, licensing — see
  [copyright & IP](../10-legal-and-compliance/copyright-and-ip.md)).
- Development and integration.
- Testing (functional, accessibility, performance, security).
- Launch.

### 2. Run budget (recurring) — the one people forget
- **Hosting and services** (servers, CDN, email, third‑party APIs).
- **Domain renewal** and TLS (often free, but track it).
- **Maintenance**: dependency and platform updates, security patching.
- **Monitoring & backups** tooling.
- **Content updates** and small enhancements.
- **Support / incident response** capacity.
- **Periodic compliance review** (laws change).

> ✅ **Do:** Present clients with a build cost *and* a monthly/annual run cost.
> A site with no maintenance budget is a liability waiting to happen.

## Why maintenance can't be optional

An unmaintained site doesn't stay still — it decays:

- Dependencies develop known vulnerabilities that are actively exploited.
- Certificates and domains expire, causing sudden outages.
- Browsers and platforms change, breaking features.
- Content goes stale; links rot.
- Laws change, making policies non‑compliant.

Skipping maintenance doesn't save money; it defers a larger, less predictable
cost (a breach, an outage, a legal problem) to a worse time. See
[Maintenance & Operations](../09-maintenance/README.md).

## Estimation techniques

- **Break work down** to tasks small enough to estimate with confidence.
- Use **ranges**, not false precision ("3–5 days," not "4 days").
- Add **contingency** (commonly 15–25%) for the unknowns you can't see yet.
- Estimate **non‑functional work** explicitly: accessibility, performance,
  security, and testing are *work*, not free by‑products.
- Beware the **planning fallacy** — humans systematically underestimate. Compare
  against how long similar past work actually took.

## Scope management

Scope creep — the quiet accumulation of "small" additions — is the top killer of
timelines and budgets.

> ✅ **Do:**
> - Write down what's **in and out** of scope (the "Won't" list from
>   [requirements](requirements-gathering.md) is your friend).
> - Handle changes through a lightweight **change process**: assess impact on
>   time/cost, get agreement, then proceed.
> - Protect a **minimum viable launch**; push nice‑to‑haves to a later phase.

> ❌ **Don't:** Absorb "just one more small thing" silently. Small things
> compound, and unpriced work breeds resentment on both sides.

## Contracts protect everyone

For client work, a written agreement should cover:

- Scope, deliverables, and acceptance criteria.
- Payment schedule and what happens on changes.
- **Ownership of code, content, and accounts** on final payment.
- **Maintenance terms** (or an explicit statement that maintenance is separate).
- **Liability** for security, compliance, and downtime.
- Third‑party costs (licenses, fonts, stock, services) and who pays them.

> ⚖️ **Legal note:** Ambiguity about ownership and maintenance is the source of
> most freelance/agency disputes. Nail it down in writing before work starts.
> See [roles & responsibilities](../00-getting-started/roles-and-responsibilities.md)
> and [licensing](../10-legal-and-compliance/licensing.md).

## A realistic mental model

> The build is the *down payment*. Hosting, maintenance, and compliance are the
> *mortgage*. Budget for the mortgage, or don't buy the house.
