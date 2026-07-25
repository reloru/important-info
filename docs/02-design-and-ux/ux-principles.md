# UX Principles

Usability is not a matter of taste. Decades of research give us reliable
principles for designing interfaces people can actually use. You don't have to
memorize all of them, but you should recognize when you're violating one.

## Nielsen's 10 usability heuristics (the classics)

A durable, widely‑used checklist for spotting usability problems:

1. **Visibility of system status** — always keep users informed (loading states,
   confirmations, progress).
2. **Match between system and the real world** — use users' language and mental
   models, not internal jargon.
3. **User control and freedom** — provide clear exits, undo, and back.
4. **Consistency and standards** — follow platform and web conventions; don't
   make users relearn.
5. **Error prevention** — design so mistakes are hard to make in the first
   place.
6. **Recognition rather than recall** — show options; don't force users to
   remember things.
7. **Flexibility and efficiency of use** — accelerators for experts, simplicity
   for novices.
8. **Aesthetic and minimalist design** — every extra element competes for
   attention; cut ruthlessly.
9. **Help users recognize, diagnose, and recover from errors** — plain‑language
   messages that say what happened and how to fix it.
10. **Help and documentation** — available when needed, findable, task‑focused.

## How people actually behave

Design for real humans, not idealized ones:

- **People scan, they don't read.** They skim for what looks relevant. Use clear
  headings, short paragraphs, and meaningful links.
- **People satisfice.** They pick the first reasonable option, not the best one.
  Make the good path obvious.
- **Attention is scarce.** Every choice, field, and distraction has a cost.
- **Change is friction.** Familiar patterns reduce cognitive load; novelty for
  its own sake taxes users.

## Practical guidelines

> ✅ **Do:**
> - Make the primary action on each page obvious.
> - Write clear, specific link and button labels ("Download report," not "Click
>   here").
> - Show where the user is (breadcrumbs, active nav states).
> - Provide feedback for every action.
> - Design empty states, loading states, and error states — not just the happy
>   path.
> - Keep forms as short as possible; ask only for what you need.
> - Use progressive disclosure: reveal complexity only when needed.

> ❌ **Don't:**
> - Rely on color alone to convey meaning (fails for colorblind users — ♿).
> - Hide critical actions behind hover (fails on touch — and discoverability).
> - Use tiny tap targets (aim for at least ~44×44px).
> - Auto‑play audio/video with sound.
> - Trap users with no clear way back or out.

## Forms deserve special care

Forms are where users most often struggle and abandon:

- Label every field (visibly — placeholder text is not a label). ♿
- Group related fields; use a logical order.
- Validate inline and explain errors in plain language next to the field.
- Preserve entered data on error — never make users retype everything.
- Indicate required vs. optional clearly.
- Support autofill and password managers.

## Dark patterns: don't

**Dark patterns** are interface tricks that manipulate users into doing things
they didn't intend — pre‑checked consent boxes, hard‑to‑find unsubscribe links,
"confirmshaming," hidden costs, or making the "decline" option deliberately
obscure.

> ⚖️ **Legal note:** Beyond being unethical and corrosive to trust, many dark
> patterns are now **illegal**. GDPR requires consent to be freely given and as
> easy to withdraw as to give; the EU Digital Services Act and California's CPRA
> explicitly restrict manipulative "deceptive designs," and the US FTC has
> pursued companies over them. Designing an honest, symmetric choice isn't just
> nice — it's increasingly the law. See
> [cookies & tracking](../10-legal-and-compliance/cookies-and-tracking.md) and
> [GDPR](../10-legal-and-compliance/gdpr.md).

## Test with real users

The most reliable way to find usability problems is to **watch real people try
to use it.** Even five users, given realistic tasks, will surface the majority
of serious issues. You are not your user; your assumptions are hypotheses until
tested.
