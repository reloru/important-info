# ARIA & Semantics

**ARIA** (Accessible Rich Internet Applications) is a set of attributes that add
accessibility information to HTML — roles, states, and properties that assistive
technologies can read. It fills the gaps where native HTML can't express a
custom widget. Used well, it's essential. Used carelessly, it actively harms.

## The first rule of ARIA: don't use ARIA

The official guidance is blunt and correct: **if you can use a native HTML
element or attribute with the semantics and behavior you need, use it.** Native
elements come with accessibility, keyboard support, and states for free, and
they're far harder to get wrong.

```
<!-- ❌ Reinventing a button badly -->
<div role="button" tabindex="0" onclick="...">Save</div>

<!-- ✅ Just use a button -->
<button type="button">Save</button>
```

The `<div role="button">` version forces you to manually add keyboard handling,
focus, and Enter/Space activation — all of which the native `<button>` gives you
automatically, and which people routinely forget.

> ✅ **Do:** Reach for semantic HTML first. See
> [semantic HTML](../03-development-best-practices/semantic-html.md).
> ❌ **Don't:** Rebuild native controls out of `<div>`s and patch them with ARIA.

## What ARIA provides

- **Roles** — what a thing *is* (`role="tab"`, `role="dialog"`,
  `role="navigation"`). Use these for custom widgets HTML has no element for.
- **States** — the current condition (`aria-expanded="true"`,
  `aria-checked="false"`, `aria-disabled`).
- **Properties** — relationships and descriptions (`aria-label`,
  `aria-labelledby`, `aria-describedby`, `aria-controls`).

## Naming things: accessible names

Interactive elements need an **accessible name** so assistive tech can announce
them. In order of preference:

1. **Visible text content** (best — a `<button>Save</button>` names itself).
2. **`aria-labelledby`** — reference visible text elsewhere on the page.
3. **`aria-label`** — a string name when there's no visible text (e.g., an
   icon‑only button: `aria-label="Close"`).

> 💡 An icon‑only button with no text and no `aria-label` is announced as just
> "button" — useless. Always give icon buttons an accessible name.

## Live regions

For content that updates without a page reload (a form success message, a live
search count), `aria-live` tells screen readers to announce the change:

- `aria-live="polite"` — announce when the user is idle (most updates).
- `aria-live="assertive"` — interrupt immediately (urgent errors only).

## Common ARIA mistakes (that make things worse)

> ❌ **Don't:**
> - Add a `role` that contradicts the element (`<a role="button">` when you
>   mean a link, or vice versa).
> - Use `aria-label` on elements that don't take a name, or that already have
>   visible text (it can override and hide it).
> - Set ARIA states (like `aria-expanded`) and forget to *update* them in
>   JavaScript when the state actually changes — stale ARIA lies to users.
> - Sprinkle `role="presentation"`/`aria-hidden="true"` on things users need.
> - Put `aria-hidden="true"` on a focusable element — now it's reachable but
>   invisible to screen readers. Deeply confusing.

**Bad ARIA is worse than no ARIA**, because it misinforms the very users who
depend on it. No ARIA at least falls back to the (native) HTML semantics.

## The ARIA Authoring Practices Guide (APG)

For genuinely custom widgets — tabs, comboboxes, dialogs, tree views,
carousels — don't invent the pattern. The W3C **ARIA Authoring Practices Guide**
documents the expected roles, states, and keyboard interactions for each. Follow
it rather than guessing, or better yet, use a well‑tested, accessible component
library.

## Rules of thumb

1. Prefer native HTML.
2. Don't change native semantics unless you truly must.
3. All interactive ARIA controls must be keyboard‑operable.
4. Don't hide focusable elements from assistive tech.
5. Every interactive element needs an accessible name.
6. Keep ARIA **states in sync** with reality via your JavaScript.

Get these right and ARIA becomes the precision tool it's meant to be, rather
than a footgun.
