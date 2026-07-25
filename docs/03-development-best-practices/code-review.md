# Code Review

Code review is the practice of having someone other than the author examine a
change before it's merged. It's one of the most cost‑effective quality practices
there is — it catches bugs, spreads knowledge, and keeps a codebase coherent.

## What review is for

- **Catch defects** early, when they're cheap to fix.
- **Share knowledge** — reviewers learn the code; authors learn from feedback;
  the "bus factor" improves (fewer areas only one person understands).
- **Maintain consistency** with standards and architecture.
- **Catch cross‑cutting issues** — security, accessibility, performance — that
  the author may have overlooked.
- **Create a second set of eyes on risk** before it reaches users.

## What reviewers should look for

- **Correctness** — does it do what it claims? Any edge cases missed?
- **Security** 🔒 — input validation, authz checks, no secrets committed, no
  injection risks. See [Security](../07-security/README.md).
- **Accessibility** ♿ — semantic markup, labels, keyboard support for new UI.
- **Performance** ⚡ — obvious inefficiencies, heavy assets, N+1 queries.
- **Readability & maintainability** — will the next person understand this?
- **Tests** — are there tests for the change, especially for bug fixes?
- **Scope** — is the change focused, or has unrelated stuff crept in?

## How to review well (as a reviewer)

> ✅ **Do:**
> - Review promptly — a stalled review blocks the author and the work.
> - Be specific and kind; critique the code, not the person.
> - Explain the *why* behind suggestions; link to standards/docs.
> - Distinguish **blocking** issues from **nits** and preferences (label them).
> - Ask questions rather than issuing decrees when you're unsure.
> - Approve when it's good enough — perfection is not the bar; "better and safe"
>   is.

> ❌ **Don't:**
> - Rubber‑stamp ("LGTM") without actually reading it.
> - Bikeshed over formatting that a tool should handle (automate it instead —
>   see [coding standards](coding-standards.md)).
> - Make it about ego or gatekeeping.

## How to be reviewed well (as an author)

> ✅ **Do:**
> - Keep changes **small and focused** — huge PRs get shallow reviews.
> - Write a clear description: what changed, why, and how to test it.
> - Self‑review first; catch the obvious stuff before a human does.
> - Respond to feedback graciously; assume good intent.

> ❌ **Don't:**
> - Take feedback personally. Review improves the work, not judges the author.
> - Bundle ten unrelated changes into one review.

## Keep reviews small

The strongest predictor of a *useful* review is a *small* change. Beyond a few
hundred lines, reviewer attention and defect‑finding drop sharply. Break big work
into reviewable pieces.

## Automate the mechanical parts

Let machines handle what machines are good at, so humans focus on judgment:

- Formatting and linting → automated (see [coding standards](coding-standards.md)).
- Tests, builds, and security scans → run in **CI** on every PR (see
  [CI/CD](../08-deployment-and-devops/ci-cd.md)).
- Humans review design, correctness, security reasoning, and clarity.

## Reviews as a teaching tool

Beyond catching bugs, review is where a team's standards and knowledge actually
propagate. Treat it as collaborative learning, not a gate to argue past. Over
time it raises everyone's baseline.
