# Coding Standards

Coding standards are the agreed conventions that keep a codebase consistent and
readable. The specific rules matter less than the fact that everyone follows the
*same* ones. Consistency lets a team read and change code without friction.

## Why consistency beats preference

When every file follows the same conventions, you spend your attention on the
logic, not on decoding someone's personal style. Inconsistent code is slower to
read, harder to review, and more bug‑prone. Pick conventions and enforce them —
the choice of tabs vs. spaces matters far less than picking one.

## What standards cover

- **Formatting** — indentation, line length, spacing, quotes, braces.
- **Naming** — clear, consistent names for variables, functions, files, CSS
  classes.
- **File and folder structure** — predictable organization.
- **Comments and documentation** — when and how to explain code.
- **Language‑specific idioms** — the accepted "right way" in your stack.

## Readable code principles

> ✅ **Do:**
> - Use **descriptive names** that reveal intent (`unreadMessageCount`, not
>   `n`).
> - Keep functions **small and single‑purpose**.
> - Avoid deep nesting; prefer early returns.
> - Prefer **clarity over cleverness** — the clever one‑liner nobody understands
>   is a liability.
> - Remove dead code rather than commenting it out (version control remembers
>   it).
> - Handle errors explicitly; don't swallow them silently.

> ❌ **Don't:**
> - Leave commented‑out blocks and `TODO`s to rot.
> - Use "magic numbers" — name constants so their meaning is clear.
> - Copy‑paste blocks instead of factoring out shared logic (within reason —
>   don't over‑abstract either).

## Automate enforcement

Humans are inconsistent and reviewing style by hand is a waste of everyone's
time. Let tools do it:

- **Linters** (e.g., ESLint, Stylelint, RuboCop, Flake8) catch likely bugs and
  style violations.
- **Formatters** (e.g., Prettier, Black, gofmt) enforce formatting
  automatically, ending style debates.
- **EditorConfig** keeps basic settings consistent across editors.
- Run these in **pre‑commit hooks** and in **CI** so nothing inconsistent gets
  merged. See [CI/CD](../08-deployment-and-devops/ci-cd.md).

> 💡 **Tip:** Adopting an existing, well‑known style guide (for your language or
> framework) is usually smarter than inventing your own. Less bikeshedding, more
> building.

## Comments: explain *why*, not *what*

Good code says *what* it does; comments should say *why* it does it that way —
the context, the trade‑off, the non‑obvious constraint.

```
// BAD: increments the counter by one
count += 1;

// GOOD: retry budget is 3; the API rate-limits bursts above that
if (attempts < MAX_RETRIES) { ... }
```

Comments that merely restate the code go stale and add noise. Comments that
capture intent and gotchas are gold to the next maintainer.

## Consistency in CSS/markup, too

Front‑end code needs standards as much as back‑end code:

- A consistent CSS methodology (e.g., a naming convention or utility approach)
  prevents specificity wars and unmaintainable styles.
- Semantic, consistent HTML aids accessibility and SEO — see
  [semantic HTML](semantic-html.md).

## Standards are a team agreement

Write the standards down, keep them short, and revisit them occasionally. The
point isn't rigid rules for their own sake — it's shared expectations that let
the team move fast without stepping on each other.
