# Testing Accessibility

You can't know a site is accessible without testing it — and testing well means
combining automated tools with human, hands‑on checks. Automated tools alone
give a false sense of security: they reliably catch only a **minority** of real
accessibility barriers.

## The layered approach

Think of accessibility testing as layers, each catching what the others miss:

1. **Automated scanning** — fast, catches obvious/common issues.
2. **Manual keyboard testing** — catches interaction and focus problems.
3. **Screen‑reader testing** — catches what things actually sound like.
4. **Zoom/reflow and visual checks** — catches low‑vision issues.
5. **Real user testing** — catches everything the above miss.

## 1. Automated tools

Good for scale and regression‑catching, especially in CI:

- **axe** (browser extension and library) — the widely‑used engine behind many
  tools; excellent signal‑to‑noise.
- **Lighthouse** (built into Chrome DevTools) — includes an accessibility audit.
- **WAVE** — visual, in‑page annotations of issues.
- **Pa11y** — command‑line, good for automation.

> ✅ **Do:** Run an automated check in CI so regressions are caught on every
> change. See [CI/CD](../08-deployment-and-devops/ci-cd.md).
> ❌ **Don't:** Treat a green automated score as "accessible." Tools can't judge
> whether alt text is *meaningful*, whether focus order makes *sense*, or
> whether a custom widget is actually usable.

## 2. Keyboard testing

Unplug your mouse (metaphorically) and navigate a key journey:

- `Tab` / `Shift+Tab` move forward/back — is the order logical?
- Can you **reach and operate everything** (links, buttons, menus, forms,
  modals)?
- Is the **focus indicator always visible**?
- Any **keyboard traps** (focus you can't escape)?
- Do custom widgets respond to expected keys (Enter/Space, arrows, Esc)?
- Does a **skip link** let you bypass repetitive navigation?

This single test surfaces a large share of serious problems and takes minutes.

## 3. Screen‑reader testing

Listen to your page. You don't need to be an expert to catch big problems:

- **VoiceOver** (built into macOS/iOS), **NVDA** (free, Windows), **TalkBack**
  (Android), or **JAWS** (Windows, commercial).
- Navigate by headings, landmarks, and links — does the structure make sense?
- Are images announced meaningfully (or is decoration read aloud as noise)?
- Are form fields announced with their labels, required state, and errors?
- Are icon‑only buttons named, or just "button"?
- Do dynamic updates get announced (see
  [live regions](aria-and-semantics.md))?

Testing with more than one screen reader/browser pairing is ideal, since
behavior varies.

## 4. Visual / low‑vision checks

- Zoom the browser to **200%** (and beyond) — is everything still usable, with
  no content lost or overlapping?
- Check at mobile/narrow widths for **reflow** (no horizontal scrolling).
- Verify **color contrast** with a contrast checker.
- Simulate **color blindness** to confirm nothing relies on color alone.
- Respect `prefers-reduced-motion`.

## 5. Testing with real users

The gold standard: watch **people who actually use assistive technology** try to
complete real tasks. They'll find issues no checklist or tool predicts, and
they'll tell you what's merely *technically compliant* versus *genuinely
usable*. If you can involve disabled users (paid, respectfully) at any point,
do — especially for complex applications.

## Bake it into the process

Accessibility testing shouldn't be a one‑time pre‑launch scramble:

- Add automated checks to **CI**.
- Include accessibility in your **[code review](../03-development-best-practices/code-review.md)**
  and **[definition of done](../03-development-best-practices/testing.md)**.
- Re‑test after significant changes — accessibility regresses just like anything
  else.
- Schedule periodic audits as part of
  [maintenance](../09-maintenance/README.md).

> ⚖️ **Legal note:** Keeping records of your accessibility testing and
> remediation demonstrates good‑faith effort — useful if compliance is ever
> questioned. Many organizations also publish an **accessibility statement**
> describing their conformance and how to report problems. See
> [accessibility law](../10-legal-and-compliance/accessibility-law.md).
