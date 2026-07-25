# Semantic HTML

Semantic HTML means using HTML elements **for their meaning**, not just their
appearance — a `<button>` for a button, a `<nav>` for navigation, headings in
order. It's the single highest‑leverage practice in front‑end development
because it improves accessibility, SEO, robustness, and maintainability *all at
once*, usually for free.

## Why semantics matter

The browser, search engines, and assistive technologies all read your HTML to
understand the page. When you use the right element, they get that meaning
automatically:

- **Accessibility** — screen readers announce a real `<button>` as a button and
  let users navigate by headings and landmarks. A `<div onclick>` gives them
  nothing. ♿
- **SEO** — search engines use headings and structure to understand your
  content. See [on‑page SEO](../06-seo/on-page-seo.md).
- **Robustness** — native elements come with built‑in keyboard support, focus
  behavior, and states you'd otherwise have to reimplement (badly).
- **Maintainability** — meaningful markup is easier to read and style.

## Use the right element

| Instead of… | Use… |
|-------------|------|
| `<div class="button" onclick>` | `<button>` |
| `<div class="heading">` | `<h1>`–`<h6>` (in order) |
| `<span>` links styled to look clickable | `<a href>` |
| `<div>` soup for structure | `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` |
| A `<table>` for page layout | CSS Grid/Flexbox (tables are for tabular data) |
| Manual "required" asterisks only | `<input required>` + a visible indicator |

## Landmarks and document structure

Structural elements create **landmarks** that let assistive‑tech users jump
around the page:

- `<header>` — introductory content / site header.
- `<nav>` — major navigation blocks.
- `<main>` — the primary content (one per page).
- `<section>` / `<article>` — thematic groupings / self‑contained content.
- `<aside>` — tangential content.
- `<footer>` — footer content.

## Headings form an outline

Use headings to convey hierarchy, not size:

- One clear main heading (`<h1>`) describing the page.
- Nested subheadings (`<h2>`, `<h3>`…) in logical order — don't skip levels for
  visual effect.
- Style size with CSS, not by choosing the "biggest‑looking" heading tag.

> ♿ Screen‑reader users frequently navigate by heading. A logical heading
> outline is one of the most impactful accessibility wins there is.

## Forms deserve real semantics

- Associate every input with a `<label>` (via `for`/`id` or wrapping).
- Use appropriate `type`s (`email`, `tel`, `number`, `date`) — they trigger the
  right mobile keyboards and built‑in validation.
- Group related fields with `<fieldset>` and `<legend>`.
- Mark required fields with the `required` attribute *and* a visible indicator.

Native form markup and its built‑in validation are for structure and UX — the
security and spam handling of what gets submitted is covered in
[forms & input handling](forms-and-input-handling.md).

## When native isn't enough: ARIA (carefully)

Sometimes you build components HTML doesn't natively provide (a custom combobox,
a tab panel). That's where **ARIA** adds semantics — but the first rule of ARIA
is *don't use ARIA if a native element will do*. Native elements are more robust
and less error‑prone. See [ARIA & semantics](../04-accessibility/aria-and-semantics.md).

> ✅ **Do:** Reach for the native element first, every time.
> ❌ **Don't:** Rebuild a `<button>` or `<select>` out of `<div>`s and then bolt
> on ARIA to fake what you threw away.

## The payoff

Semantic HTML is the rare practice with almost no downside. It costs nothing
extra to write, and it pays off in accessibility, SEO, resilience, and
maintainability simultaneously. Make it your default.
