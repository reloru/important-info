# Performance Budgets

A performance budget is a set of **limits you commit to** — maximum page weight,
maximum load time, target metric thresholds — that you measure against
continuously. Without a budget, performance quietly erodes: every new feature,
script, and image adds weight until the site is slow and nobody knows exactly
when it happened.

## Why budgets work

- They make performance a **shared, explicit goal**, not an afterthought.
- They turn a vague "let's keep it fast" into a **measurable gate**.
- They catch **regressions early**, when they're cheap to fix.
- They force **trade‑off conversations**: "this new widget adds 300KB — what
  comes out to make room?"

## Kinds of budgets

Set budgets in whichever terms your team can act on:

- **Metric budgets** — target [Core Web Vitals](core-web-vitals.md) thresholds
  (e.g., LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1).
- **Quantity budgets** — total page weight (e.g., ≤ 1 MB), number of requests,
  amount of JavaScript (e.g., ≤ 150 KB compressed), number of fonts.
- **Rule/score budgets** — e.g., a minimum Lighthouse performance score, or "no
  render‑blocking resources."

Metric budgets reflect user experience best; quantity budgets are easy to
enforce automatically. Use both.

## Setting sensible numbers

- Base targets on your **users' real conditions** — a mid‑range phone on a
  throttled connection, not your dev machine.
- Anchor to **Core Web Vitals "good" thresholds** as a baseline.
- Look at **competitors/analogues** — being meaningfully faster is an advantage.
- Be realistic but firm. A budget nobody can hit gets ignored; one with no teeth
  is decoration.

## Enforce it automatically

A budget only works if it's checked continuously:

- Run **Lighthouse (CI)** or similar on every pull request; fail the build if a
  budget is exceeded.
- Track **field data** (real‑user monitoring) over time to catch real‑world
  regressions.
- Surface results where the team sees them (PR checks, dashboards).

See [CI/CD](../08-deployment-and-devops/ci-cd.md) and
[testing](../03-development-best-practices/testing.md).

> ✅ **Do:** Treat a budget breach like a failing test — investigate before
> merging.
> ❌ **Don't:** Let "just this once" exceptions pile up. Each one becomes the new
> normal.

## When you must exceed a budget

Sometimes a genuinely valuable feature costs more than the budget allows. That's
a decision to make **consciously**, not by accident:

- Quantify the cost and the benefit.
- Look for offsets (remove something else, lazy‑load it, defer it).
- If you raise the budget, do it deliberately and record why.

## Budgets as a maintenance tool

Performance, like accessibility and security, **regresses over time** if
unmonitored. A budget with automated enforcement is what keeps a fast site fast
through years of changes. Fold periodic performance review into your
[maintenance plan](../09-maintenance/maintenance-plan.md).
