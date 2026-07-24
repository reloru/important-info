# Google Search Console & Webmaster Tools

If SEO is about helping search engines find, understand, and rank your content,
**Search Console is how you see what the search engine actually thinks of your
site** — which pages it has indexed, which queries you appear for, what's broken,
and whether you've been penalized. It is a free, official tool from Google, and
setting it up is one of the first things you should do for any site you care
about. This page also covers the family of free validation and diagnostic tools
that go with it, and the equivalent tool for Bing.

> **What is a "webmaster tool"?** Historically called "Google Webmaster Tools,"
> this class of tool is a dashboard a *site owner* uses to communicate with a
> search engine and see how the engine sees their site — distinct from
> *analytics*, which measures what *users* do once they arrive. You need both;
> they answer different questions. See [analytics](analytics.md).

## Google Search Console (GSC)

Search Console is the authoritative, first‑party view of your site's presence in
Google Search. Unlike third‑party SEO tools that *estimate*, GSC shows you
Google's own data about your site.

### Why it's essential

- It's **free and first‑party** — the real data, straight from Google.
- It **alerts you to problems**: indexing errors, security issues, manual
  penalties, and mobile‑usability problems.
- It shows the **actual search queries** bringing people to your site.
- It's **privacy‑friendly** — aggregated, no cookies on your site, no consent
  burden (contrast with page‑level [analytics](analytics.md)). ⚖️
- It's a core part of ongoing [maintenance](../09-maintenance/maintenance-plan.md)
  — the place you notice a traffic drop or an indexing problem before it becomes
  a crisis.

### Setup & verification

Before Google will show you a site's private data, you must **prove you own
it** ("verify" the property). Common verification methods:

- **DNS record** — add a TXT record to your domain's DNS. This verifies a
  **Domain property** (all subdomains and both `http`/`https` at once) and is the
  most robust method. See [DNS, domains & SSL](../08-deployment-and-devops/domains-dns-ssl.md).
- **HTML file upload** — upload a specific file to your site's root.
- **HTML meta tag** — add a verification `<meta>` tag to your homepage's
  `<head>`.
- **Google Analytics or Tag Manager** — if you already use them with the right
  permissions.

> 💡 **Property types:** A **Domain property** (DNS‑verified) covers every
> subdomain and protocol — usually what you want. A **URL‑prefix property**
> covers only one exact prefix (e.g., `https://www.example.com/`). If you use a
> URL‑prefix property, be consistent about `www`/non‑`www` and `http`/`https` so
> your data isn't split across properties. See
> [technical SEO: canonicalization](technical-seo.md).

### Submitting your sitemap

Once verified, submit your **XML sitemap** (`sitemap.xml`) under the **Sitemaps**
report. This tells Google where your important URLs are and helps it discover
them faster. GSC then reports whether the sitemap was read successfully and how
many of its URLs are indexed. (Submitting a sitemap *helps* discovery; it does
not *guarantee* indexing.) See
[technical SEO: sitemaps](technical-seo.md).

### URL Inspection tool

The **URL Inspection** tool tells you, for any single URL on your site:

- Whether it's **indexed**, and if not, **why not**.
- When Google last crawled it and what it saw.
- Whether it's **mobile‑friendly** and eligible for any **rich results**.
- Any indexing or structured‑data issues on that specific page.

You can also **"Request indexing"** after publishing or updating a page to nudge
Google to recrawl it sooner — useful, though not instant or guaranteed.

### Indexing & coverage diagnostics

The **Pages** report (formerly "Index Coverage") shows how many of your pages are
**indexed** vs. **not indexed**, grouped by reason. Common "not indexed"
reasons and what they usually mean:

- **"Excluded by 'noindex' tag"** — the page tells Google not to index it. ⚠️ A
  leftover `noindex` from staging is a classic, catastrophic cause of missing
  pages — see [technical SEO](technical-seo.md).
- **"Blocked by robots.txt"** — crawling is disallowed.
- **"Crawled – currently not indexed" / "Discovered – currently not indexed"** —
  Google knows about the page but chose not to (or hasn't yet) index it, often a
  sign the content is thin or low‑priority.
- **"Duplicate, Google chose a different canonical"** — Google indexed a
  different URL it considers canonical. See
  [technical SEO: canonicalization](technical-seo.md).
- **Server errors (5xx) / not found (404)** — the page failed to load when
  crawled.

Reviewing this report periodically is how you catch pages silently dropping out
of Google's index.

### Search performance (Performance report)

The **Performance report** is GSC's most‑used feature. It shows, for real Google
searches:

- **Impressions** — how often your pages appeared in results.
- **Clicks** — how often people clicked through.
- **CTR (click‑through rate)** — clicks ÷ impressions.
- **Average position** — where your pages ranked.

You can break this down by **query**, **page**, **country**, **device**, and
**search appearance**, and compare date ranges. This reveals what people actually
search to find you, which pages underperform their impressions (a title/meta
opportunity — see [on‑page SEO](on-page-seo.md)), and where rankings are rising
or slipping.

### Core Web Vitals & Page Experience

GSC includes a **Core Web Vitals report** based on **field data** (real Chrome
users, via the Chrome User Experience Report). It groups your URLs into **Good /
Needs improvement / Poor** for LCP, INP, and CLS, on mobile and desktop. This is
the same field data that feeds Google's page‑experience ranking signals, so it's
the authoritative place to see how real users experience your site's performance.
For the metrics themselves and how to fix them, see
[Core Web Vitals](../05-performance/core-web-vitals.md); to diagnose a specific
URL, use PageSpeed Insights (below).

### Enhancements & rich results

If you use [structured data](structured-data.md), GSC's **Enhancements** reports
show which rich‑result types Google detected (e.g., FAQs, products, breadcrumbs),
plus any validation errors or warnings — and let you validate a fix.

### Manual actions & security issues

Two reports you hope stay empty, but must check:

- **Manual actions** — a *human reviewer at Google* has penalized your site for
  violating spam guidelines (e.g., unnatural links, cloaking, thin/spammy
  content, [misused structured data](structured-data.md)). A manual action can
  bury or remove your site from results. If you get one, GSC explains it; you
  fix the issue and submit a **reconsideration request**.
- **Security issues** — Google detected malware, hacked content, or social
  engineering on your site. This is both an SEO emergency and a
  [security incident](../09-maintenance/incident-response.md) — investigate and
  remediate immediately. 🔒

> 💡 A **manual action** (human penalty) is different from an **algorithmic**
> ranking drop (no penalty, just the ranking systems valuing your pages less).
> Only manual actions appear in that report; a sudden drop with an empty Manual
> Actions report points to an algorithm update or a technical problem instead.

### Removals

The **Removals** tool temporarily hides a URL from Google results (about six
months) — useful in an urgent situation (e.g., sensitive content accidentally
published). It's a stopgap: to remove content *permanently* you must delete it
and return a 404/410, or block indexing with `noindex`.

## Search Console in ongoing maintenance

Search Console isn't a set‑and‑forget setup task — it's a monitoring surface you
should check on a regular cadence, and it belongs in your
[maintenance plan](../09-maintenance/maintenance-plan.md):

- **Enable email alerts** so Google notifies you of new indexing errors, manual
  actions, and security issues.
- **Monthly:** skim the Performance report for traffic changes; check the Pages
  report for new indexing errors.
- **After any launch, migration, or redesign:** submit the updated sitemap,
  spot‑check key URLs with URL Inspection, and watch coverage for fallout from
  changed URLs (confirm your [redirects](technical-seo.md) worked).
- **Immediately** on any manual‑action or security alert.

## Supporting validation & diagnostic tools

A family of free, official tools complements Search Console. Reach for these when
building or debugging specific things:

| Tool | Use it to… | Related page |
|------|-----------|--------------|
| **PageSpeed Insights** | Diagnose a single URL's performance, combining **lab** data (Lighthouse) and **field** data (real users), with specific fix suggestions | [Core Web Vitals](../05-performance/core-web-vitals.md) |
| **Lighthouse** (in Chrome DevTools) | Run local, repeatable lab audits for performance, accessibility, SEO, and best practices | [performance budgets](../05-performance/performance-budgets.md) |
| **Rich Results Test** | Check whether a page (or pasted code) is eligible for Google rich results and see structured‑data errors | [structured data](structured-data.md) |
| **Schema.org Validator** | Validate structured‑data markup against the Schema.org vocabulary (search‑engine‑agnostic) | [structured data](structured-data.md) |
| **Mobile‑Friendly / mobile usability checks** | Confirm a page works well on mobile (mobile‑first indexing) | [responsive design](../02-design-and-ux/responsive-design.md) |

> **A note on the AMP Test:** **AMP** (Accelerated Mobile Pages) is a framework
> for stripped‑down, fast‑loading mobile pages, and Google historically offered
> an **AMP Test** to validate them. AMP has faded in importance — Google removed
> the AMP requirement for its "Top Stories" carousel, and most sites no longer
> need it now that [Core Web Vitals](../05-performance/core-web-vitals.md) reward
> fast pages regardless of framework. If you maintain AMP pages, validate them
> with the relevant AMP validation tooling; if you're starting fresh, you almost
> certainly don't need AMP.

> 💡 **Lab vs. field data, again:** Search Console's Core Web Vitals report and
> PageSpeed Insights' "field" section show what *real users* experienced (what
> Google ranks on); Lighthouse and PageSpeed's "lab" section run a controlled
> test (great for debugging and catching regressions). Use field data to know
> the real state, lab data to diagnose and prevent regressions. See
> [Core Web Vitals](../05-performance/core-web-vitals.md).

## Bing Webmaster Tools

**Bing Webmaster Tools** is Microsoft's equivalent of Search Console for the Bing
search engine (which also powers some other engines and, increasingly, matters
for AI‑assistant answers). It offers similar features: verification, sitemap
submission, URL inspection, search‑performance reports, and diagnostics — and it
can **import your settings directly from Google Search Console** to save setup
time.

> **Priority:** For most sites, Google holds the dominant share of search
> traffic, so **Google Search Console is the priority**. Bing Webmaster Tools is
> worth setting up too — it's free, quick to import, and captures the Bing/AI
> audience you'd otherwise be blind to — but treat it as **secondary**, not a
> replacement for GSC. Weigh how much of your audience actually uses Bing before
> investing significant time in it.

## The takeaway

Set up **Google Search Console** (DNS‑verified domain property), submit your
sitemap, enable alerts, and make its Performance and Pages reports part of your
[maintenance routine](../09-maintenance/maintenance-plan.md). Keep the validation
tools — PageSpeed Insights, Rich Results Test, Schema.org Validator — in your
back pocket for building and debugging. Add **Bing Webmaster Tools** as a quick,
lower‑priority extra. Together they give you the search engine's own view of your
site, which no amount of guessing can replace.
