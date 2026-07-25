# SEO Checklist

A copy‑ready SEO gate for **launch and periodic audits**. It deliberately overlaps
with the SEO block of the broad [pre‑launch checklist](pre-launch-checklist.md) but
goes deeper and is reusable as a standalone SEO review (quarterly is a good
cadence — see the [maintenance plan](../09-maintenance/maintenance-plan.md)). For
the reasoning behind each item, follow the links into the
[SEO section](../06-seo/README.md).

> SEO has no guaranteed rankings and no legitimate shortcuts — this checklist is
> about not getting in a search engine's way and giving it what it needs to
> understand you. Durable SEO is mostly good, fast, accessible, useful content.

## Crawlability & indexing
- [ ] **`robots.txt`** correct — **no accidental `Disallow: /`** (a whole‑site
      block). See [technical SEO](../06-seo/technical-seo.md).
- [ ] **No leftover `noindex`** from staging on pages that should be indexed
      (critical — verify with URL Inspection).
- [ ] **XML sitemap** present, accurate, and **submitted** in
      [Search Console](../06-seo/search-console.md).
- [ ] Important pages are **internally linked** (nothing orphaned/undiscoverable).
- [ ] Content that must rank isn't hidden behind **client‑side‑only rendering**
      (prefer SSR/SSG for indexable content).

## URLs, redirects & canonicalization
- [ ] URLs are **readable, lowercase, hyphenated**, and reflect hierarchy; stable
      (not changed casually). See [information architecture](../01-planning-and-strategy/information-architecture.md).
- [ ] **301 redirects** map every old/changed URL to its best equivalent (for any
      redesign/migration); **no redirect chains**.
- [ ] **Canonical tags** set; a **single preferred domain** (www vs. apex) and
      HTTPS enforced with redirects.

## On‑page
- [ ] **Unique, descriptive `<title>`** per page (important words first, sensible
      length). See [on‑page SEO](../06-seo/on-page-seo.md).
- [ ] **Unique meta description** per page (compelling — affects click‑through).
- [ ] **One `<h1>`**; logical, nested heading outline (no skipped levels for
      looks). See [semantic HTML](../03-development-best-practices/semantic-html.md).
- [ ] Content is **genuinely useful**, original, and matches **search intent**; no
      keyword stuffing; **E‑E‑A‑T** signals (author/credibility) where relevant.
- [ ] **Descriptive link text** (not "click here") and descriptive image
      **filenames + alt text** (helps SEO *and* accessibility ♿).
- [ ] Paid/sponsored/UGC links use appropriate `rel` values. ⚖️

## Structured data & rich results
- [ ] Relevant **Schema.org** markup (JSON‑LD) for your content type, matching
      **visible** page content (no spammy/hidden markup). See
      [structured data](../06-seo/structured-data.md).
- [ ] Validated with the **Rich Results Test** / **Schema.org Validator**; monitor
      the **Enhancements** reports in Search Console.

## Social/sharing metadata
- [ ] **Open Graph** (and equivalent) tags — title, description, image — so shared
      links render well.
- [ ] A **favicon** and appropriate touch/app icons are set.

## Performance & mobile (page experience)
- [ ] **Core Web Vitals** within targets (LCP, INP, CLS). See
      [Core Web Vitals](../05-performance/core-web-vitals.md).
- [ ] **Mobile version has full content** and works well (mobile‑first indexing).
      See [responsive design](../02-design-and-ux/responsive-design.md).
- [ ] **HTTPS** everywhere (a baseline ranking + trust signal). See
      [HTTPS & TLS](../07-security/https-and-tls.md).

## International (only if you serve multiple languages/regions)
- [ ] **`hreflang`** annotations connect equivalent pages across languages/regions
      so the right version is served and they don't compete. See
      [technical SEO](../06-seo/technical-seo.md).
- [ ] A consistent URL strategy for locales (subdirectory/subdomain/ccTLD) and
      correct `lang` attributes.

## Measurement & monitoring
- [ ] **[Search Console](../06-seo/search-console.md)** verified; sitemap
      submitted; **email alerts on** (indexing errors, manual actions, security
      issues).
- [ ] **Analytics** configured with consent handling (see
      [analytics](../06-seo/analytics.md)); privacy‑friendly where possible. ⚖️
- [ ] Ongoing: watch the **Performance** report for traffic/query shifts and the
      **Pages** report for new indexing errors; fix **broken links / 404s**. See
      [content updates](../09-maintenance/content-updates.md).

---

> Run this at launch and revisit it periodically — content, links, and rankings
> drift, and technical regressions (a stray `noindex`, a broken migration) are
> easy to ship. Pair with the broad [pre‑launch checklist](pre-launch-checklist.md)
> at launch.
