# Responsive Design

People visit websites on phones, tablets, laptops, desktops, TVs, and more —
across a huge range of screen sizes, input methods, and network conditions. A
responsive site adapts to all of them from a single codebase. This is now the
baseline expectation, not a feature.

## Mobile‑first thinking

Design for the smallest screen first, then enhance for larger ones. This
discipline forces you to prioritize content and actions, because there's no room
for clutter. Scaling *up* from a focused mobile design is easier than cramming a
desktop design *down*.

Mobile‑first is also a business reality: for most sites, **the majority of
traffic is mobile**, and search engines predominantly index the mobile version
of your site.

## The building blocks

- **Fluid layouts** — use relative units (%, `rem`, `fr`, `vw`) and modern CSS
  layout (Flexbox, Grid) so content reflows naturally instead of being pinned to
  fixed pixel widths.
- **Flexible media** — images and video scale within their containers
  (`max-width: 100%`), and you serve appropriately sized images per device.
- **Breakpoints** — points where the layout changes to suit the available space.
  Choose them based on where *your content* breaks, not specific device models
  (which change every year).
- **The viewport meta tag** — `<meta name="viewport" content="width=device-width,
  initial-scale=1">` tells mobile browsers to render at the device's width.
  Without it, mobile layouts break.

## Design for touch and other inputs

- **Touch targets** should be comfortably large (~44×44px minimum) and spaced so
  users don't hit the wrong thing.
- Don't rely on **hover** — it doesn't exist on touch. Ensure everything is
  reachable by tap and keyboard. ♿
- Consider **thumb reach** — primary actions within easy reach on large phones.

## Content and performance implications

Responsive isn't only about layout:

- ⚡ **Serve right‑sized images.** A phone shouldn't download a 3000px desktop
  hero. Use responsive images (`srcset`/`sizes`) and modern formats. See
  [image & asset optimization](../05-performance/image-and-asset-optimization.md).
- Prioritize content order for small screens — what matters most goes first.
- Beware heavy assets on mobile networks; test on real, throttled connections.

## Testing responsiveness

> ✅ **Do:**
> - Test on **real devices**, not only the browser's device emulator.
> - Test the full range: small phone, large phone, tablet, laptop, wide desktop.
> - Test both orientations (portrait/landscape).
> - Test with the browser/text zoomed to 200% — content must remain usable
>   (this is also a WCAG requirement — ♿).
> - Test with a slow, throttled network.

> ❌ **Don't:**
> - Hide important content on mobile just because it's inconvenient — mobile
>   users deserve the full site.
> - Assume the desktop layout "will just work" small. It won't.
> - Design fixed‑width elements that force horizontal scrolling.

## Responsive ≠ separate mobile site

Maintaining a separate `m.example.com` site is an outdated pattern that doubles
maintenance and fragments SEO. A single responsive site is the standard modern
approach.

## Accessibility and responsiveness overlap

Zoom, reflow, large targets, and content that works at any size are both
responsive‑design and accessibility concerns. Building responsively well gets
you much of the way toward WCAG's reflow and resize requirements. See
[Accessibility](../04-accessibility/README.md).
