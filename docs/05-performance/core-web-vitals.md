# Core Web Vitals

Core Web Vitals are a set of real‑world, user‑centric performance metrics
defined by Google. They matter because they measure what users actually
*experience* — loading, responsiveness, and stability — and because they factor
into search ranking. They're the concrete targets to optimize toward.

## The three current metrics

### LCP — Largest Contentful Paint (loading)
How long until the **largest visible element** (usually the hero image or main
heading) renders. It answers: *"Does the page feel loaded?"*

- **Good:** ≤ **2.5 s** · Needs work: ≤ 4.0 s · Poor: > 4.0 s
- **Common causes of poor LCP:** slow server response, render‑blocking CSS/JS,
  large unoptimized images, slow web fonts.
- **Fixes:** optimize/preload the LCP image, improve server/hosting response,
  use a CDN, remove render‑blocking resources, cache aggressively.

### INP — Interaction to Next Paint (responsiveness)
How quickly the page **responds to user input** (taps, clicks, key presses)
across the whole visit. It answers: *"Does it react when I interact?"* (INP
replaced the older First Input Delay in 2024.)

- **Good:** ≤ **200 ms** · Needs work: ≤ 500 ms · Poor: > 500 ms
- **Common causes of poor INP:** heavy JavaScript blocking the main thread, big
  event handlers, too much work on interaction.
- **Fixes:** ship less JavaScript, break up long tasks, defer non‑critical work,
  avoid unnecessary re‑rendering.

### CLS — Cumulative Layout Shift (visual stability)
How much the page **jumps around** as it loads. It answers: *"Did the button
move just as I tapped it?"*

- **Good:** ≤ **0.1** · Needs work: ≤ 0.25 · Poor: > 0.25
- **Common causes of poor CLS:** images/embeds without dimensions, ads/banners
  injected above content, web fonts causing reflow, dynamically inserted content
  pushing things down.
- **Fixes:** always set width/height (or aspect‑ratio) on media; reserve space
  for ads/embeds; avoid inserting content above existing content; use
  `font-display` strategies that minimize shift.

## Lab vs. field data

- **Field (real‑user) data** — what actual visitors experienced, gathered from
  real sessions. This is what Google uses for ranking. It reflects the true
  spread of devices and networks.
- **Lab data** — a controlled test (e.g., Lighthouse) on a simulated device and
  network. Great for debugging and catching regressions, but a single lab run
  isn't the same as your real users' experience.

Use both: lab data to diagnose and prevent regressions, field data to know
what's really happening.

## Tools

- **PageSpeed Insights** — field + lab data for a URL.
- **Lighthouse** (Chrome DevTools) — lab audits, including a performance score.
- **Chrome DevTools Performance panel** — deep diagnosis of main‑thread work.
- **WebPageTest** — detailed, configurable lab testing.
- **Real‑user monitoring (RUM)** — collect Core Web Vitals from your live
  traffic over time.

## Priorities, in order

1. **LCP** — get meaningful content on screen fast (image optimization, hosting,
   caching, remove render‑blockers).
2. **CLS** — stop the page from jumping (dimensions on media, reserved space).
   Often the cheapest to fix.
3. **INP** — keep interactions snappy (reduce and defer JavaScript).

> ⚡ Core Web Vitals aren't just a Google scorecard — they're a proxy for a
> genuinely better experience. Optimizing them helps users, SEO, and conversions
> together. Set them as targets in your
> [performance budget](performance-budgets.md).
