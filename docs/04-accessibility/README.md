# 04 · Accessibility

Web accessibility means building sites that **everyone can use**, including
people with disabilities — visual, motor, auditory, cognitive, and situational.
It is both an ethical baseline and, increasingly, a **legal requirement**. And
it overlaps heavily with good UX, SEO, and solid engineering.

## Who benefits

Roughly one in six people worldwide lives with a significant disability, but
accessibility helps far more than that:

- Someone using a **screen reader** because they're blind.
- Someone using a **keyboard only** because of a motor impairment.
- Someone with **low vision** who zooms to 200%.
- Someone **colorblind** who can't rely on color alone.
- Someone with a **temporary** injury (a broken arm) or a **situational**
  limitation (bright sunlight, a noisy room, holding a baby).

Accessible design is better design for everyone.

## In this section

- **[WCAG overview](wcag-overview.md)** — the standard, its principles
  (POUR), and conformance levels.
- **[Accessibility checklist](accessibility-checklist.md)** — a practical,
  actionable list.
- **[ARIA & semantics](aria-and-semantics.md)** — when native HTML isn't enough,
  and how to use ARIA without making things worse.
- **[Testing accessibility](testing-accessibility.md)** — automated and manual
  methods.

## The law, in brief

> ⚖️ **Legal note:** Accessibility is legally required in many places. In the
> US, the **ADA** has been applied to websites (with WCAG used as the de‑facto
> standard) and **Section 508** covers federal contexts. In the EU, the **Web
> Accessibility Directive** (public sector) and the **European Accessibility
> Act** (broad, private‑sector obligations from June 2025) apply. The UK, Canada
> (AODA), Australia, and others have their own rules. Inaccessible sites have
> drawn a large and growing number of lawsuits and complaints. See
> [accessibility law](../10-legal-and-compliance/accessibility-law.md).

## The most important idea

Accessibility is **designed and built in**, not bolted on. It's dramatically
cheaper and better when considered from the start — in
[design](../02-design-and-ux/README.md) and in
[semantic HTML](../03-development-best-practices/semantic-html.md) — than
retrofitted after launch under legal pressure.

> ✅ **Do:** Start with semantic HTML, sufficient contrast, keyboard support, and
> text alternatives. That foundation gets you most of the way to WCAG AA.
