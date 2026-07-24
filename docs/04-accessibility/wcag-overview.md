# WCAG Overview

The **Web Content Accessibility Guidelines (WCAG)** are the internationally
recognized standard for web accessibility, published by the W3C. When a law,
contract, or organization says "make it accessible," they almost always mean
"conform to WCAG." Knowing its structure lets you target a concrete, testable
bar.

## Versions

- **WCAG 2.0** (2008) — the long‑standing baseline referenced by many laws.
- **WCAG 2.1** (2018) — added mobile, low‑vision, and cognitive criteria.
- **WCAG 2.2** (2023) — current; added more criteria (e.g., focus appearance,
  dragging alternatives, accessible authentication).
- **WCAG 3.0** — a future, substantially different model, still in draft. Don't
  target it yet.

> 💡 Target **WCAG 2.2 Level AA** for new work — it's the current best practice
> and what most modern legal frameworks are converging on. It's backward‑
> compatible with 2.1 and 2.0 AA.

## The four principles: POUR

Every guideline rolls up to one of four principles. Content must be:

### Perceivable
Users must be able to perceive the information.
- Text alternatives for non‑text content (**alt text** for images).
- Captions and transcripts for audio/video.
- Don't rely on **color alone** to convey meaning.
- Sufficient **color contrast** (see below).
- Content adapts (reflows, resizes) without loss.

### Operable
Users must be able to operate the interface.
- Everything works by **keyboard**, in a logical order.
- **Visible focus** indicator showing where you are.
- Enough **time** to read and use content.
- No content that **flashes** in a way that can trigger seizures.
- Clear ways to **navigate** and find content (headings, landmarks, skip links).
- Adequately sized **touch targets**.

### Understandable
Users must be able to understand the content and interface.
- **Readable, predictable** content and behavior.
- Consistent navigation and identification.
- **Input assistance**: clear labels, instructions, and error messages that say
  how to fix the problem.

### Robust
Content must work reliably across browsers and assistive technologies.
- Valid, well‑formed markup.
- Correct name, role, and value for UI components (this is where
  [semantic HTML](../03-development-best-practices/semantic-html.md) and
  [ARIA](aria-and-semantics.md) come in).

## Conformance levels

Each success criterion is rated **A**, **AA**, or **AAA**:

| Level | Meaning | Practical use |
|-------|---------|---------------|
| **A** | Minimum — essential barriers removed | Necessary but not sufficient |
| **AA** | Addresses the major, common barriers | **The standard target**; what laws typically require |
| **AAA** | Highest — enhanced | Admirable; often impractical site‑wide |

Aim for **AA** across the board. Adopt AAA criteria where feasible and
impactful, but AAA is generally not required or expected for a whole site.

## A few concrete AA requirements to remember

- **Contrast:** normal text at least **4.5:1** against its background; large text
  at least **3:1**; UI components and meaningful graphics at least **3:1**.
- **Text resize:** usable up to **200%** zoom without loss of content/function.
- **Reflow:** usable at narrow widths without horizontal scrolling (ties into
  [responsive design](../02-design-and-ux/responsive-design.md)).
- **Keyboard:** all functionality available without a mouse, no keyboard traps.
- **Labels:** every form control has a programmatically associated label.
- **Focus visible:** the keyboard focus indicator is clearly visible.

## WCAG is a floor, not a ceiling

Conforming to WCAG doesn't guarantee a genuinely good experience for disabled
users — it's the measurable minimum. **Testing with real assistive‑technology
users** reveals problems no checklist catches. See
[testing accessibility](testing-accessibility.md).

## Where to go next

- The practical [accessibility checklist](accessibility-checklist.md).
- The legal backdrop in [accessibility law](../10-legal-and-compliance/accessibility-law.md).
- Authoritative source: the W3C Web Accessibility Initiative (WAI) and the WCAG
  Quick Reference.
