# Requirements Gathering

Requirements gathering is the process of turning a vague wish ("we need a new
website") into a concrete, agreed, testable description of what will be built.
Done well, it prevents scope creep, disputes, and rebuilds.

## Functional vs. non‑functional requirements

- **Functional requirements** describe *what the system does*: "Users can reset
  their password by email." "Admins can publish blog posts."
- **Non‑functional requirements** describe *how well it does it*: performance,
  accessibility, security, uptime, browser support, legal compliance.

Non‑functional requirements are the ones most often forgotten — and the ones
that cause the worst late surprises. Write them down explicitly:

- "Pages must reach Largest Contentful Paint under 2.5s on a mid‑range mobile
  device on 4G." (See [Performance](../05-performance/README.md).)
- "The site must conform to WCAG 2.2 Level AA." (See
  [Accessibility](../04-accessibility/README.md).)
- "The site must support the two most recent versions of major browsers."
- "Personal data handling must comply with GDPR." (See
  [Legal & Compliance](../10-legal-and-compliance/README.md).)

## Techniques for gathering requirements

- **Stakeholder interviews** — talk to everyone who has a stake: owners, users,
  content editors, support, legal.
- **User stories** — "As a [role], I want [goal] so that [benefit]." Keeps focus
  on outcomes, not features.
- **Job stories** — "When [situation], I want to [motivation], so I can
  [expected outcome]." Emphasizes context.
- **Competitive/analog review** — what do comparable sites do well or badly?
- **Content inventory** — for redesigns, catalog what exists before deciding
  what to keep, cut, or rewrite.

## Prioritization: MoSCoW

Not everything can be in v1. Prioritize explicitly:

| Priority | Meaning |
|----------|---------|
| **Must** | Launch is meaningless without it |
| **Should** | Important but launch can survive a short delay |
| **Could** | Nice to have if time/budget allow |
| **Won't (this time)** | Explicitly out of scope — record it so it isn't assumed |

The **"Won't"** column is the most valuable one for managing expectations.

## Turning requirements into acceptance criteria

A requirement isn't done until you can *test* whether it's met. Pair each with
acceptance criteria:

> **Requirement:** Users can subscribe to a newsletter.
> **Acceptance criteria:**
> - A valid email address is accepted and stored.
> - An invalid email shows an inline, accessible error.
> - The user gives explicit consent before being subscribed (⚖️ required in many
>   jurisdictions — see [email law](../10-legal-and-compliance/email-marketing-law.md)).
> - A confirmation is shown; a double opt‑in email is sent.

## Common requirements people forget

- **Accessibility** target (WCAG level and version).
- **Performance** budgets.
- **Browser/device support** matrix.
- **Legal artifacts**: privacy policy, cookie consent, terms, e‑commerce
  disclosures.
- **Analytics & consent** — what you'll measure and how you'll get permission.
- **SEO** basics: URL structure, redirects from any old site, metadata.
- **Maintenance**: who updates content and dependencies after launch.
- **Backups & recovery** expectations.
- **Content ownership & licensing** for text, images, and fonts (see
  [copyright & IP](../10-legal-and-compliance/copyright-and-ip.md)).

## Output: a requirements document

Capture the result somewhere durable and shared — a document, a wiki, or issues
in a tracker. It should include goals, audiences, functional and non‑functional
requirements, prioritization, acceptance criteria, and what's explicitly out of
scope. This becomes the reference everyone points to when "wait, was that in
scope?" comes up — and it always comes up.
