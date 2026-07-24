# The Website Life Cycle

Almost every website — a brochure site, a SaaS app, an online store — moves
through the same phases. Understanding the life cycle is the single most useful
mental model in this whole knowledge base, because it tells you *when* each
concern needs attention. Problems are cheap to fix early and expensive to fix
late.

```
┌──────────┐   ┌────────┐   ┌───────┐   ┌──────┐   ┌────────┐   ┌─────────────┐
│  PLAN    │──▶│ DESIGN │──▶│ BUILD │──▶│ TEST │──▶│ LAUNCH │──▶│  MAINTAIN   │
└──────────┘   └────────┘   └───────┘   └──────┘   └────────┘   └─────┬───────┘
      ▲                                                                │
      └────────────────────── iterate ────────────────────────────────┘
```

The last phase — **Maintain** — loops back to the first. A website is not a
project you finish; it's a product you operate.

---

## 1. Plan

Decide *what you're building and why* before touching a design tool or an
editor.

- Clarify goals, audience, and success metrics.
- Gather requirements and scope; agree on a budget and timeline.
- Design the information architecture (how content is organized).
- Choose the technology approach and hosting.
- **Scope legal obligations early**: Will you collect personal data? Sell
  online? Serve users in the EU/UK/California? These decisions change what you
  must build.

→ [Planning & Strategy](../01-planning-and-strategy/README.md)

## 2. Design

Turn requirements into an experience.

- User experience (UX) flows and wireframes.
- Visual design and a design system for consistency.
- Responsive layouts for every screen size.
- Content strategy: who writes it, in what voice, to what standard.
- **Accessibility is designed in here** — color contrast, focus order, and
  semantics are far cheaper to get right now than to retrofit.

→ [Design & UX](../02-design-and-ux/README.md) ·
  [Accessibility](../04-accessibility/README.md)

## 3. Build

Implement the design to a professional standard.

- Follow coding standards; use version control from commit one.
- Write semantic, accessible HTML.
- Bake in performance and security as you go, not afterward.
- Review code; document decisions.

→ [Development Best Practices](../03-development-best-practices/README.md)

## 4. Test

Verify it actually works — for everyone, everywhere.

- Functional testing (does it do what it should?).
- Accessibility testing (WCAG, keyboard, screen reader).
- Performance testing (Core Web Vitals, load).
- Cross‑browser / cross‑device testing.
- Security testing (dependencies, headers, common vulnerabilities).

→ [Testing](../03-development-best-practices/testing.md)

## 5. Launch

Go live deliberately, behind a checklist.

- Final pre‑launch review across all disciplines.
- DNS, TLS/SSL, redirects, and analytics configured.
- **Legal artifacts in place**: privacy policy, cookie consent, terms — before
  the first real user arrives, not after.
- Rollback plan ready in case something breaks.

→ [Pre‑launch checklist](../templates/pre-launch-checklist.md)

## 6. Maintain

The longest and most neglected phase. Sites rot without care.

- Monitoring and uptime alerts.
- Regular backups (tested, not just taken).
- Dependency and platform updates (security patches especially).
- Content updates and link rot.
- Incident response when something goes wrong.
- Periodic re‑review of legal compliance as laws and the site evolve.

→ [Maintenance & Operations](../09-maintenance/README.md)

---

## How cross‑cutting concerns thread through the life cycle

Some concerns aren't a single phase — they run through all of them. This is why
they get their own sections *and* inline callouts throughout the docs.

| Concern | Plan | Design | Build | Test | Launch | Maintain |
|---------|:----:|:------:|:-----:|:----:|:------:|:--------:|
| **Accessibility** | scope | design in | implement | audit | verify | regress‑test |
| **Performance** | budget | design for | optimize | measure | verify | monitor |
| **Security** | threat‑model | secure UX | secure code | pentest | harden | patch |
| **SEO** | keyword/IA | content plan | technical | audit | submit | monitor |
| **Legal** | identify obligations | consent UX | data handling | review | publish policies | re‑review |

The lesson: **the cheapest place to handle a concern is the leftmost column it
appears in.** Retrofitting accessibility, security, or privacy after launch is
where budgets and reputations get destroyed.
