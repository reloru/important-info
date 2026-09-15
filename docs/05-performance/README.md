# 05 · Performance

Performance is a feature, an accessibility issue, an SEO factor, and a
conversion driver all at once. Slow sites lose users, rank worse, and exclude
people on slower devices and networks. The good news: most performance wins come
from a handful of well‑understood practices.

## Why performance matters (with receipts)

- **Users leave.** Bounce rates climb sharply as load time grows; even a
  fraction of a second measurably affects engagement and conversions.
- **Search ranking.** Google uses Core Web Vitals as a ranking signal. See
  [SEO](../06-seo/README.md).
- **Accessibility & equity.** Not everyone has a flagship phone on fast
  fibre. Heavy sites exclude people on older devices and slower or metered
  connections. ♿
- **Cost.** Efficient sites use less bandwidth and compute.

## In this section

- **[Core Web Vitals](core-web-vitals.md)** — the metrics that matter most and
  what drives them.
- **[Image & asset optimization](image-and-asset-optimization.md)** — usually
  the biggest, easiest wins.
- **[Caching & CDNs](caching-and-cdn.md)** — serve less, serve it closer, serve
  it faster.
- **[Performance budgets](performance-budgets.md)** — set limits and hold the
  line.

## The 80/20 of web performance

Most sites can dramatically improve by doing a few things well:

1. **Optimize images** (right size, modern format, lazy‑load off‑screen ones) —
   images are typically the largest bytes on a page.
2. **Reduce and defer JavaScript** — JS is expensive to download, parse, and
   run, especially on mobile.
3. **Use a CDN and good caching** so repeat and distant visits are fast.
4. **Avoid layout shift** by reserving space for images, ads, and embeds.
5. **Load only what's needed**, when it's needed (lazy loading, code splitting).

## Measure, don't guess

Optimize based on data, not hunches. Use **lab** tools (Lighthouse, WebPageTest)
for controlled testing and **field** data (real‑user monitoring) for what actual
users experience — the two often differ. Test on a **mid‑range phone on a
throttled connection**, not your fast laptop on office wifi. See
[performance budgets](performance-budgets.md) and
[testing](../03-development-best-practices/testing.md).

> ✅ **Do:** Set a performance budget early and measure against it continuously.
> ❌ **Don't:** Add a huge hero video, five web fonts, and a dozen third‑party
> scripts, then wonder why the site is slow. Managing that last category has its
> own page: [third‑party scripts](../03-development-best-practices/third-party-scripts.md).
