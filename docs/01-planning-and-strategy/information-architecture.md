# Information Architecture (IA)

Information architecture is the practice of **organizing and labeling content**
so people can find what they need and understand where they are. Good IA is
invisible; bad IA is the reason users can't find the contact page and give up.

## Why IA comes before design

You can't design a page well until you know what pages exist and how they
relate. IA is the skeleton; visual design is the skin. Deciding structure late
means expensive rework — and, after launch, broken URLs and lost SEO.

## Core concepts

- **Sitemap** — a hierarchical map of all pages and their relationships. (This is
  the *planning* sitemap, distinct from the `sitemap.xml` you give search
  engines — see [SEO](../06-seo/README.md).)
- **Navigation** — the menus and links that expose the structure. Primary
  (global), secondary (section), utility (login, search), and footer nav each
  play a role.
- **Taxonomy** — the categories, tags, and labels used to classify content.
- **URL structure** — readable, stable, logical paths (`/services/web-design`
  beats `/page?id=42`).
- **Labeling** — the words used for sections and links. Use the *users'*
  vocabulary, not internal jargon.

## Techniques

- **Card sorting** — give users content items and ask them to group and name
  them. Reveals how *they* expect things organized, not how you do.
- **Tree testing** — give users a text‑only version of your navigation and ask
  them to find things. Tests findability without visual design confounds.
- **Content inventory & audit** — list every existing page (for redesigns) and
  decide keep / merge / cut / rewrite.

## Principles of good IA

> ✅ **Do:**
> - Keep hierarchy shallow — aim for any page reachable in ~3 clicks.
> - Use clear, consistent, user‑centered labels.
> - Group related content; don't scatter it.
> - Provide multiple paths (nav, search, related links) to important content.
> - Design breadcrumbs for deep sections so users always know where they are.

> ❌ **Don't:**
> - Bury key pages (contact, pricing) deep in menus.
> - Use clever‑but‑ambiguous labels ("Solutions" that could mean anything).
> - Create orphan pages with no navigation path to them.
> - Change URLs casually after launch — it breaks links and rankings.

## URLs are part of IA — and they're forever

Once a URL is public, people and search engines rely on it. Choose URLs you can
live with:

- Lowercase, hyphen‑separated words: `/blog/website-maintenance-guide`.
- Reflect hierarchy: `/docs/security/https`.
- Avoid volatile elements (dates you'll regret, IDs, session tokens).
- Avoid stuffing keywords or making them needlessly deep.

> 💡 **Tip:** If you *must* change a URL later, add a **301 redirect** from the
> old one to the new one so links and SEO value are preserved. Plan a redirect
> map for any redesign of an existing site. (See
> [technical SEO](../06-seo/technical-seo.md).)

## IA and accessibility

Good IA is also an accessibility feature. Logical heading structure, consistent
navigation, descriptive link text, and breadcrumbs all help users of assistive
technology orient themselves. (See [Accessibility](../04-accessibility/README.md).)

## Deliverables

- A **sitemap diagram** everyone can review.
- A **URL scheme** for new pages (and a redirect map for old ones).
- A **navigation model** (what appears in each menu).
- A **labeling/taxonomy list** for categories and tags.

These feed directly into design and content work.
