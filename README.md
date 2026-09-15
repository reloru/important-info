# Website Development & Maintenance — Knowledge Base

A comprehensive, pedagogical reference for **building, running, and maintaining
websites well** — with a strong emphasis on **best practices** and the
**legal and compliance** obligations that come with putting a site on the
internet.

This is not a copy‑paste code library. It is a *decision and practice guide*:
the things a developer, agency, freelancer, or site owner should understand,
plan for, and get right — organized so you can learn the field from the ground
up or look up a specific topic when you need it.

> ⚖️ **Not legal advice.** The legal sections summarize widely applicable rules
> and common practice to help you ask the right questions. Laws vary by
> jurisdiction and change over time. For anything with real risk, consult a
> qualified attorney in the relevant jurisdiction. See
> [`docs/10-legal-and-compliance/README.md`](docs/10-legal-and-compliance/README.md).

---

## How to use this knowledge base

- **New to the field?** Read the sections in order — they follow the natural
  life cycle of a website, from planning to long‑term maintenance.
- **Looking for something specific?** Use the map below. Every section has its
  own `README.md` index.
- **Shipping a site right now?** Jump to the
  [pre‑launch checklist](docs/templates/pre-launch-checklist.md) and the
  [legal & compliance section](docs/10-legal-and-compliance/README.md).

See [`docs/00-getting-started/how-to-use-this-repo.md`](docs/00-getting-started/how-to-use-this-repo.md)
for more, and the [glossary](docs/00-getting-started/glossary.md) for terms.

---

## Table of contents

| # | Section | What it covers |
|---|---------|----------------|
| 00 | [Getting Started](docs/00-getting-started/README.md) | How to use this repo, the website life cycle, glossary |
| 01 | [Planning & Strategy](docs/01-planning-and-strategy/README.md) | Requirements, information architecture, choosing a stack, domains & hosting, budgeting |
| 02 | [Design & UX](docs/02-design-and-ux/README.md) | UX principles, responsive design, design systems, content strategy |
| 03 | [Development Best Practices](docs/03-development-best-practices/README.md) | Standards, version control, semantic HTML, testing, code review, docs |
| 04 | [Accessibility](docs/04-accessibility/README.md) | WCAG, ARIA, checklists, testing — and the law behind it |
| 05 | [Performance](docs/05-performance/README.md) | Core Web Vitals, asset optimization, caching & CDNs, budgets |
| 06 | [SEO](docs/06-seo/README.md) | Technical & on‑page SEO, structured data, Search Console & webmaster tools, analytics |
| 07 | [Security](docs/07-security/README.md) | OWASP Top 10, HTTPS/TLS, auth, secrets, headers |
| 08 | [Deployment & DevOps](docs/08-deployment-and-devops/README.md) | CI/CD, environments, infrastructure, DNS/SSL |
| 09 | [Maintenance & Operations](docs/09-maintenance/README.md) | Maintenance plans, dependencies, backups, monitoring, incident response |
| 10 | [Legal & Compliance](docs/10-legal-and-compliance/README.md) | Privacy, GDPR, CCPA/CPRA, cookies, ToS, accessibility law, IP, e‑commerce, email law |
| 11 | [Payments](docs/11-payments/README.md) | How online payments work, choosing a provider, PCI, Stripe (integration, webhooks, subscriptions, disputes, operations) |
| — | [Templates & Checklists](docs/templates/README.md) | Ready‑to‑adapt policies, checklists, and plans |

> Sections 00–10 follow the website life cycle in order; **11 · Payments** is a
> **feature deep‑dive** (a capability you add, not a life‑cycle phase) and leans
> more technical by necessity.

---

## The website life cycle at a glance

```
PLAN ──▶ DESIGN ──▶ BUILD ──▶ TEST ──▶ LAUNCH ──▶ MAINTAIN ──▶ (iterate)
  │         │          │        │         │           │
  │         │          │        │         │           └─ monitoring, backups,
  │         │          │        │         │              patching, content,
  │         │          │        │         │              incident response
  │         │          │        │         └─ pre-launch checks: legal, a11y,
  │         │          │        │            perf, SEO, security
  │         │          │        └─ functional, accessibility, performance,
  │         │          │           cross-browser, security testing
  │         │          └─ standards, version control, reviews
  │         └─ UX, responsive, design system, content
  └─ requirements, IA, stack, hosting, budget, legal scoping
```

Legal and accessibility obligations are **not a launch‑day afterthought** —
they thread through every phase. This knowledge base flags where.

---

## Repository structure

```
.
├── README.md                     ← you are here (master index)
├── CONTRIBUTING.md               ← how to add or update content
├── LICENSE                       ← content license (CC BY 4.0)
├── tools/check-docs.py           ← link/anchor/orphan checker (stdlib only)
├── .github/workflows/            ← CI: runs the checker on every PR
├── docs/
│   ├── 00-getting-started/
│   ├── 01-planning-and-strategy/
│   ├── 02-design-and-ux/
│   ├── 03-development-best-practices/
│   ├── 04-accessibility/
│   ├── 05-performance/
│   ├── 06-seo/
│   ├── 07-security/
│   ├── 08-deployment-and-devops/
│   ├── 09-maintenance/
│   ├── 10-legal-and-compliance/
│   ├── 11-payments/
│   └── templates/
```

---

## Conventions used in these docs

- **✅ Do / ❌ Don't** — quick best‑practice contrasts.
- **⚖️ Legal note** — where a practice intersects with the law.
- **🔒 Security note** / **♿ Accessibility note** / **⚡ Performance note** —
  cross‑cutting callouts.
- **💡 Tip** — a practical shortcut or rule of thumb.
- **⚠️ Caution** — a common trap that bites people in practice.
- **Checklists** are written so you can copy them into an issue or ticket.

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).
