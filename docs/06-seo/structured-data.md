# Structured Data

Structured data is machine‑readable markup that explicitly tells search engines
what your content *means* — that this is a recipe, that's a product with a price,
this is an event on a date. It helps engines understand your pages and can earn
**rich results** (star ratings, FAQs, event details) that stand out in search.

## Why it helps

- **Comprehension** — you remove ambiguity about what the content represents.
- **Rich results** — eligible pages can get enhanced listings (ratings,
  images, prices, FAQ accordions), improving visibility and click‑through.
- **Voice & AI surfaces** — structured data helps machines extract precise
  answers.

It doesn't directly boost ranking, but better understanding and richer listings
often lead to more clicks.

## Schema.org and formats

- **Schema.org** is the shared vocabulary search engines support (types like
  `Article`, `Product`, `Organization`, `LocalBusiness`, `Event`, `Recipe`,
  `FAQPage`, `BreadcrumbList`, `Review`).
- **JSON‑LD** is the recommended format — a block of structured data in the page
  head, separate from your visible markup, so it's easy to add and maintain.
  (Microdata and RDFa are older, inline alternatives.)

## Common, high‑value types

| Type | Use for |
|------|---------|
| `Organization` / `LocalBusiness` | Company/brand info, contact, location, hours |
| `WebSite` + `SearchAction` | Site name and search box in results |
| `BreadcrumbList` | Breadcrumb trails in results |
| `Article` / `BlogPosting` | News and blog content |
| `Product` + `Offer` | E‑commerce items with price/availability |
| `Review` / `AggregateRating` | Ratings (with genuine reviews only) |
| `FAQPage` | Q&A content |
| `Event` | Dates, venue, tickets |

## Rules of the road

> ✅ **Do:**
> - Mark up content that is **actually on the page** and visible to users.
> - Use the most specific applicable type.
> - **Validate your markup** with the **Rich Results Test** (checks Google
>   rich‑result eligibility) and/or the **Schema.org Validator** (checks the
>   markup against the vocabulary, engine‑agnostic), then monitor the
>   **Enhancements** reports in [Search Console](search-console.md) for
>   errors on your live pages.
> - Keep it accurate and in sync with the visible content.

> ❌ **Don't:**
> - Mark up content that **isn't visible** to users, or that misrepresents the
>   page — search engines treat this as spam and may issue manual penalties.
> - Fake reviews or ratings. ⚖️ Beyond violating search guidelines, fabricated
>   or undisclosed reviews can breach **consumer‑protection and advertising
>   laws** (e.g., FTC rules, EU consumer directives). See
>   [e‑commerce law](../10-legal-and-compliance/ecommerce-law.md).

## Keep it maintainable

Structured data can drift out of sync with the page (a price changes, an event
passes). Generate it from the same source as your visible content where
possible, and include it in periodic
[content](../02-design-and-ux/content-strategy.md) and
[maintenance](../09-maintenance/README.md) reviews so it doesn't become
inaccurate — inaccurate structured data is worse than none.

## Where to learn the specifics

Refer to the official **Schema.org** documentation for vocabulary and each
search engine's structured‑data guidelines for which types earn rich results and
what properties they require. Requirements change, so check the current
guidance rather than relying on memory.
