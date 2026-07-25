# Accessibility Law

Web accessibility isn't only an ethical and quality issue — in a growing number
of jurisdictions it's a **legal requirement**, and inaccessible sites have
generated a large and rising volume of lawsuits, complaints, and regulatory
action. This page covers the legal landscape; for how to actually build
accessibly, see [Accessibility](../04-accessibility/README.md).

> ⚖️ Not legal advice. Accessibility law is jurisdiction‑specific and evolving;
> consult a professional about your obligations and risk.

## The common thread: WCAG is the de‑facto standard

Across most of these laws, conformance is measured against the
**[Web Content Accessibility Guidelines (WCAG)](../04-accessibility/wcag-overview.md)**,
typically **Level AA** (currently 2.1 or 2.2). Even where a statute doesn't name
WCAG explicitly, courts and regulators use it as the benchmark. **Building to
WCAG 2.2 AA is the single best way to reduce legal risk.**

## United States

### Americans with Disabilities Act (ADA)
The ADA prohibits discrimination against people with disabilities. Courts have
widely applied it to websites — particularly for businesses considered "places of
public accommodation." There has been a **flood of ADA web‑accessibility
lawsuits and demand letters**. While the ADA doesn't (yet) codify a specific
technical standard for private sites in all contexts, **WCAG AA is the practical
benchmark** used in settlements and rulings. (Note: the DOJ has moved to require
WCAG for state/local government sites under ADA Title II.)

### Section 508
Requires **US federal agencies** (and often their contractors and recipients of
federal funds) to make their electronic and information technology accessible,
aligned with WCAG. If you build for government, this likely applies.

## European Union

### European Accessibility Act (EAA)
A major expansion: the EAA extends accessibility requirements to a **broad range
of private‑sector** products and services — including e‑commerce, banking,
transport, e‑books, and more — with obligations applying from **June 2025**. It
effectively makes WCAG‑level accessibility mandatory for many private businesses
serving EU consumers. If you sell to or serve EU consumers, take this seriously.

### Web Accessibility Directive
Requires **public sector bodies'** websites and mobile apps in the EU to be
accessible (to the EN 301 549 standard, which incorporates WCAG).

## United Kingdom
The **Equality Act 2010** requires reasonable adjustments so disabled people
aren't disadvantaged, applied to websites; public sector bodies have specific
accessibility regulations (aligned with WCAG AA).

## Canada
- **AODA** (Accessibility for Ontarians with Disabilities Act) requires WCAG‑level
  accessibility for many Ontario organizations.
- The **Accessible Canada Act** covers federally regulated entities.

## Elsewhere
Many other countries (Australia's DDA, Israel, and others) have accessibility
requirements, frequently referencing WCAG. The global direction is clearly toward
*more* enforceable accessibility obligations, not fewer.

## What this means for you

> ✅ **Do:**
> - **Target [WCAG 2.2 AA](../04-accessibility/wcag-overview.md)** across your
>   site. It's the standard that satisfies most legal frameworks.
> - Build accessibility in from **design and development**, not as a retrofit —
>   it's cheaper and more defensible. See
>   [Accessibility](../04-accessibility/README.md).
> - **Test** with automated tools *and* manual/assistive‑tech methods, and
>   **keep records** of your testing and remediation — evidence of good‑faith
>   effort matters. See
>   [testing accessibility](../04-accessibility/testing-accessibility.md).
> - Publish an **accessibility statement** describing your conformance, known
>   limitations, and how users can report problems and get help. (Some laws
>   require one.)
> - Provide an **accessible way to contact you** about barriers, and respond.

> ❌ **Don't:**
> - Assume you're "too small" to be a target — small businesses receive demand
>   letters and lawsuits too.
> - Rely solely on an **"accessibility overlay" widget.** These third‑party
>   overlays are widely criticized by accessibility experts and disability
>   advocates as ineffective, and they have **not reliably prevented
>   litigation** — some overlay users have still been sued. There is no
>   quick‑fix plugin substitute for actually building accessibly.

## The bottom line

Accessibility is shifting from "best practice" to "legal baseline" worldwide.
The good news: the compliant path is the same as the good‑engineering path —
semantic HTML, sufficient contrast, keyboard support, text alternatives, and
real testing. Build to WCAG AA, document your efforts, offer a way to report
problems, and you dramatically reduce both barriers *and* legal risk.
