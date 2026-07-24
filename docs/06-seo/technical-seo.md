# Technical SEO

Technical SEO is the plumbing that lets search engines crawl and index your site
correctly. Get it wrong and even great content stays invisible. Most of it is
set‑once‑and‑maintain, but the cost of errors (a stray `noindex`, a broken
migration) can be severe.

## Crawlability & indexing

Search engines must be able to reach and read your pages.

- **`robots.txt`** — tells crawlers which paths they may or may not crawl. Useful
  for keeping crawlers out of admin or duplicate areas.
  > ❌ **Don't** use `robots.txt` to hide sensitive content — it's public and
  > only *requests* compliance. Use real access control. 🔒
  > ❌ **Don't** accidentally block your whole site (`Disallow: /`) — a classic,
  > catastrophic launch mistake.
- **`noindex`** — a meta tag/header that tells engines *not to index* a page.
  Powerful and dangerous: a `noindex` left over from a staging site can wipe you
  out of search. **Double‑check this at launch.**
- **XML sitemap** (`sitemap.xml`) — a machine‑readable list of your important
  URLs that helps engines discover them. Submit it in the search engine's
  webmaster tools — see [Search Console](search-console.md), which also reports
  whether the sitemap was read and how many of its URLs got indexed.
- **Internal linking** — pages with no links to them are hard to discover. A
  logical link structure helps crawling and spreads ranking signals.

## URLs

Stable, readable URLs are both a UX and an SEO asset. (See
[information architecture](../01-planning-and-strategy/information-architecture.md).)

- Readable and descriptive: `/services/web-maintenance` beats `/p?id=42`.
- Lowercase, hyphen‑separated words.
- Reflect site hierarchy.
- **Stable** — don't change them casually.

## Redirects & migrations

When URLs must change (a redesign, a restructure), preserve their value:

- Use **301 (permanent) redirects** from old URLs to their new equivalents.
  This passes ranking signals and keeps existing links working.
- Build a **redirect map** for any migration; test it before and after launch.
- Avoid **redirect chains** (A→B→C) — redirect straight to the final URL.
- ⚡ Redirects add latency; keep them minimal. See
  [Performance](../05-performance/README.md).

> ✅ **Do:** Treat "what happens to the old URLs?" as a first‑class question in
> any redesign. Silently dropping pages loses traffic and rankings.

## Canonicalization

Duplicate or near‑duplicate content (e.g., the same page reachable at multiple
URLs, or with tracking parameters) confuses engines about which to rank.

- Use a **canonical tag** (`<link rel="canonical">`) to point to the preferred
  version.
- Pick one **preferred domain** (e.g., `https://www.example.com` vs
  `https://example.com`) and redirect the other.
- Enforce **HTTPS** and a single trailing‑slash convention with redirects.

## HTTPS

Serving over **HTTPS** is a baseline ranking factor and a trust signal (browsers
label HTTP sites "Not secure"). Every site should be HTTPS‑only. See
[HTTPS & TLS](../07-security/https-and-tls.md).

## Mobile‑first indexing

Search engines predominantly index the **mobile** version of your site. If your
mobile experience is degraded or hides content, your rankings suffer. Build
responsively. See [responsive design](../02-design-and-ux/responsive-design.md).

## Core Web Vitals

Page experience — including [Core Web Vitals](../05-performance/core-web-vitals.md)
(loading, responsiveness, stability) — is part of ranking. Fast, stable pages
have an edge, especially between otherwise comparable results.

## Structured data

Marking up your content with schema helps engines understand it and can earn
rich results. See [structured data](structured-data.md).

## JavaScript & rendering

If content is rendered entirely client‑side with JavaScript, engines may see an
empty page or a delayed one. Prefer server‑side rendering or static generation
for content that must be indexed, or ensure your rendering approach is
crawler‑friendly. See
[choosing a tech stack](../01-planning-and-strategy/choosing-a-tech-stack.md).

## Verifying it all worked: Search Console

Everything above is something you *do to* your site; **Search Console is how you
confirm the search engine actually received it** — which pages got indexed, which
were rejected and why, whether your redirects and canonicals were honored, and
whether a leftover `noindex` slipped through. Set it up early and check it after
every launch or migration. See
[Search Console & webmaster tools](search-console.md).

## A pre‑launch technical‑SEO checklist

- [ ] No accidental site‑wide `Disallow` in `robots.txt`.
- [ ] No leftover `noindex` from staging.
- [ ] `sitemap.xml` present, correct, and submitted.
- [ ] Redirect map in place for any changed/old URLs (301s).
- [ ] Canonical tags and a single preferred domain.
- [ ] HTTPS enforced site‑wide.
- [ ] Titles and meta descriptions set (see [on‑page SEO](on-page-seo.md)).
- [ ] Mobile version has full content and works well.
- [ ] [Search Console](search-console.md) verified, sitemap submitted, alerts
      on; analytics configured with consent handling (see [analytics](analytics.md)).
