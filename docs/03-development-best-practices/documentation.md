# Documentation

Documentation is the message you send to the future — to the next maintainer,
the new hire, and forgetful future‑you. Websites live for years and change
hands; the code alone rarely explains *why* things are the way they are.
Undocumented projects become fragile mysteries nobody dares touch.

## What to document

Not everything, but the things that aren't obvious from the code:

- **README** — what the project is, how to set it up, run it, test it, and
  deploy it. The front door for anyone new.
- **Architecture overview** — the big picture: major components, how they fit,
  key decisions.
- **Setup / onboarding** — how to get a working local environment from scratch.
- **Deployment** — how the site is built and released; where it runs; how to
  roll back. See [Deployment & DevOps](../08-deployment-and-devops/README.md).
- **Operational runbooks** — how to respond to common incidents (site down,
  certificate expiring, backup restore). See
  [incident response](../09-maintenance/incident-response.md).
- **Decisions and their rationale** — *why* you chose this stack, this pattern,
  this trade‑off. This is the highest‑value, most‑often‑missing documentation.
- **Accounts and ownership** — an inventory of domains, hosting, services, and
  who controls them (store credentials in a secrets manager, not the doc).

## Document decisions, not just facts

The code shows *what* it does. Documentation should capture *why* — the context
and constraints that led to a choice. A lightweight **Architecture Decision
Record (ADR)** — a short note per significant decision (context, decision,
consequences) — is a cheap way to preserve reasoning that would otherwise be
lost.

> 💡 **Tip:** The question "why on earth is it done this way?" is the most
> expensive one in software. Good decision docs answer it before it's asked.

## Keep documentation close and current

> ✅ **Do:**
> - Keep docs **in the repo** alongside the code so they version together.
> - Update docs **in the same change** that changes the behavior.
> - Prefer a few accurate, maintained docs over many stale ones.
> - Write for the reader who knows *less* than you do right now.

> ❌ **Don't:**
> - Let docs drift out of date — wrong documentation is worse than none, because
>   it's trusted.
> - Document the obvious (`// loop over users`) while omitting the crucial (why
>   this retry limit, why this workaround).

## Documentation is a maintenance asset

Good documentation directly reduces maintenance risk and cost:

- Faster onboarding and handovers (critical when a project changes hands — see
  [roles & responsibilities](../00-getting-started/roles-and-responsibilities.md)).
- Faster, calmer incident response.
- Fewer "why is this here?" mysteries that lead to accidental breakage.

## Don't forget user‑facing documentation

If the site has features users need help with, they need docs too — help pages,
FAQs, tooltips. That's part of [content strategy](../02-design-and-ux/content-strategy.md)
and good [UX](../02-design-and-ux/ux-principles.md).

## The bare minimum

Even the smallest project deserves a README that answers: *What is this? How do
I run it? How do I deploy it? Who owns it?* If you write nothing else, write
that.
