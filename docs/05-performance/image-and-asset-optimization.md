# Image & Asset Optimization

Images are typically the **largest chunk of bytes** on a web page, which makes
image optimization the single highest‑return performance task for most sites.
Fonts, CSS, and JavaScript matter too. This page covers getting all of them lean.

## Images: the biggest win

### Right format
- **AVIF / WebP** — modern formats with excellent compression; prefer them, with
  a fallback for older browsers.
- **JPEG** — fine for photos when modern formats aren't available.
- **PNG** — for images needing transparency or sharp edges (but often larger).
- **SVG** — for logos, icons, and simple graphics; scales perfectly and is tiny.
- **Video instead of GIF** — animated GIFs are enormous; a muted, looping video
  is far smaller.

### Right size
Don't ship a 4000px image to display it at 400px.

- Resize images to the largest size they'll actually be displayed.
- Use **responsive images** (`srcset` and `sizes`) so each device downloads an
  appropriately sized version — a phone gets a small image, a desktop a large
  one. Ties into [responsive design](../02-design-and-ux/responsive-design.md).

### Compress
- Compress images (lossy where acceptable) — you can often cut file size
  dramatically with no visible quality loss.
- Automate compression in your build so nobody has to remember.

### Lazy‑load off‑screen images
- Add `loading="lazy"` to images below the fold so they load only when needed.
- **Don't** lazy‑load the LCP/hero image — that delays your
  [LCP](core-web-vitals.md). Load it eagerly (and consider preloading it).

### Prevent layout shift
- Always set **width and height** (or CSS `aspect-ratio`) on images so the
  browser reserves space and the page doesn't jump. This directly improves
  [CLS](core-web-vitals.md).

### Accessibility
> ♿ Every meaningful image needs descriptive **alt text**; decorative images get
> `alt=""`. This is both an accessibility requirement and an SEO signal. See
> [Accessibility](../04-accessibility/README.md).

## Fonts

Web fonts are a common, sneaky performance cost:

- **Limit** the number of families, weights, and styles — each is a download.
- Use **modern formats** (WOFF2) and **subset** fonts to the characters you
  need.
- Set **`font-display: swap`** (or an equivalent strategy) so text is visible
  while the font loads, rather than invisible.
- **Preload** critical fonts to reduce delay.
- Consider **system fonts** when brand allows — zero download.
- Beware layout shift when a web font replaces the fallback (contributes to
  [CLS](core-web-vitals.md)).

> ⚖️ **Legal note:** Loading fonts from a third‑party service can transmit user
> IP addresses to that provider — which has been treated as personal‑data
> processing under GDPR (a German court fined a site owner over Google Fonts
> loaded remotely). **Self‑hosting fonts** avoids this and is often faster too.
> See [cookies & tracking](../10-legal-and-compliance/cookies-and-tracking.md).

## CSS & JavaScript

- **Minify** CSS and JS (strip whitespace/comments) and **compress** transfer
  (gzip/Brotli — usually handled by the server/CDN).
- **Remove unused code** — dead CSS and JS still cost bytes and parse time.
- **Split code** so pages load only the JavaScript they need, not the whole app.
- **Defer non‑critical JavaScript** (`defer`/`async`, or load on interaction) so
  it doesn't block rendering.
- **Avoid render‑blocking resources** in the critical path; inline only truly
  critical CSS.
- **JavaScript is the most expensive asset per byte** — it must be downloaded,
  parsed, compiled, and executed, and it hurts [INP](core-web-vitals.md). Ship
  less of it.

## Third‑party scripts: the hidden tax

Analytics, chat widgets, ad tags, A/B testing, and social embeds are often the
worst offenders — you don't control their size or speed, and they can block your
page and harm privacy.

> ✅ **Do:** Audit every third‑party script. Load only what you need, defer it,
> and remove anything unused.
> ⚖️ Third‑party scripts also raise **privacy** questions (they can set cookies
> and send data externally) — see
> [cookies & tracking](../10-legal-and-compliance/cookies-and-tracking.md).

## Other assets

- Serve everything over HTTP/2 or HTTP/3 for efficient multiplexing.
- Cache aggressively with good headers and a CDN — see
  [caching & CDNs](caching-and-cdn.md).
- Preconnect/preload key resources; prefetch likely next navigations.

## The workflow

Bake optimization into the **build pipeline** so it happens automatically —
compressing images, minifying code, generating responsive variants. Manual
optimization gets skipped; automated optimization is reliable. Then measure the
result against your [performance budget](performance-budgets.md).
