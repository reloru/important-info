# Accessibility Checklist

A practical, actionable checklist for building and reviewing accessible pages.
It won't replace [full WCAG 2.2 AA](wcag-overview.md) or real user testing, but
it catches the great majority of common barriers. Copy it into your PR template
or QA ticket.

## Structure & semantics

- [ ] Page uses **semantic HTML** (`<header>`, `<nav>`, `<main>`, `<footer>`,
      real `<button>`/`<a>`). See
      [semantic HTML](../03-development-best-practices/semantic-html.md).
- [ ] One `<h1>` per page; headings nest logically (no skipped levels).
- [ ] Landmarks let users jump to major regions.
- [ ] A **"skip to main content"** link is available for keyboard users.
- [ ] Page has a descriptive, unique `<title>`.
- [ ] The page's language is set (`<html lang="…">`).
- [ ] Reading/DOM order matches the visual order.

## Text & readability

- [ ] Body text contrast is at least **4.5:1** (3:1 for large text). 
- [ ] UI components and meaningful icons have at least **3:1** contrast.
- [ ] Text can be resized to **200%** without breaking layout or losing content.
- [ ] Content **reflows** at narrow widths without horizontal scrolling.
- [ ] Line length, spacing, and size are comfortable to read.

## Color & visuals

- [ ] Meaning is **never conveyed by color alone** (use text/icons/patterns
      too).
- [ ] Links are distinguishable from body text (not by color alone).
- [ ] No content flashes more than **three times per second** (seizure risk).

## Images & media

- [ ] Meaningful images have descriptive **alt text**; decorative images have
      empty `alt=""`.
- [ ] Complex images (charts) have a longer text description.
- [ ] Videos have **captions**; audio has **transcripts**.
- [ ] Media does **not autoplay** with sound; users control playback.

## Keyboard & focus

- [ ] Everything is reachable and operable with the **keyboard alone**.
- [ ] **Tab order** is logical.
- [ ] The **focus indicator** is clearly visible on every interactive element.
- [ ] No **keyboard traps** (you can always tab away).
- [ ] Custom widgets support expected keys (Enter/Space to activate, arrows for
      menus, Esc to close).
- [ ] Focus is managed sensibly for modals/dialogs (moves in, is trapped inside
      while open, returns on close).

## Forms

- [ ] Every input has a **visible, associated `<label>`** (placeholders are not
      labels).
- [ ] Required fields are indicated clearly (not by color alone).
- [ ] Errors are announced, described in plain language, and tied to the field.
- [ ] Instructions/format hints are provided before the input.
- [ ] Related controls are grouped (`<fieldset>`/`<legend>`).
- [ ] Inputs use appropriate `type`s and `autocomplete` values.

## Interactive components

- [ ] Custom components expose correct **name, role, and value** (via native
      elements or [ARIA](aria-and-semantics.md)).
- [ ] Touch/click targets are large enough (~44×44px) and well spaced.
- [ ] Drag/hover‑only actions have an accessible alternative.
- [ ] Time limits are avoidable, adjustable, or can be extended.

## Motion & preferences

- [ ] Respect `prefers-reduced-motion` for animations and transitions.
- [ ] Parallax and large motion effects can be reduced/disabled.

## Verify

- [ ] Run an **automated scan** (axe / Lighthouse / WAVE) — zero critical
      issues. (Remember: automation finds only a minority of problems.)
- [ ] **Keyboard‑only** walk‑through of key journeys.
- [ ] **Screen‑reader** check of key pages.
- [ ] Test at **200% zoom** and at mobile widths.

See [testing accessibility](testing-accessibility.md) for how to do the verify
steps well.

---

> ✅ **Do:** Treat this list as a gate, not a wish list — accessibility bugs are
> bugs.
> ⚖️ **Legal note:** Many jurisdictions require accessibility by law; a checklist
> pass materially reduces both barriers and legal risk. See
> [accessibility law](../10-legal-and-compliance/accessibility-law.md).
