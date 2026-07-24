# 03 · Development Best Practices

This section is about *how to build well* — the professional habits that make a
codebase reliable, maintainable, and safe to change. It is deliberately **not** a
language tutorial or a code library. It's the practices that apply regardless of
your stack.

## Why practices matter more than cleverness

Code is read far more often than it's written, and websites are maintained for
years by people who weren't there at the start. The goal isn't the cleverest
solution; it's the one the next person (often future‑you) can understand, trust,
and safely modify.

## In this section

- **[Coding standards](coding-standards.md)** — consistency, readability, and
  the tools that enforce them.
- **[Version control](version-control.md)** — using Git well: branches,
  commits, and collaboration.
- **[Semantic HTML](semantic-html.md)** — the foundation of accessible,
  robust, SEO‑friendly pages.
- **[Testing](testing.md)** — the kinds of testing a website needs and when.
- **[Code review](code-review.md)** — catching problems and sharing knowledge.
- **[Documentation](documentation.md)** — writing down what future maintainers
  need.

## The short version

> ✅ **Do:**
> - Use version control from the first commit; never edit production directly.
> - Follow a consistent style, enforced by automated tools.
> - Write semantic, accessible HTML as the default.
> - Build in security and performance as you go, not as a cleanup phase.
> - Test before you ship; review before you merge.
> - Document the *why*, not just the *what*.

> ❌ **Don't:**
> - Copy‑paste solutions you don't understand (especially security‑sensitive
>   ones).
> - Leave secrets, credentials, or API keys in code. (🔒 See
>   [secrets management](../07-security/secrets-management.md).)
> - Ship without testing "because it's a small change."

## Cross‑cutting

Security ([07](../07-security/README.md)), accessibility
([04](../04-accessibility/README.md)), and performance
([05](../05-performance/README.md)) are development concerns woven through every
practice here — not separate phases you get to later.
