# On‑Page SEO

On‑page SEO is everything on the page itself that helps search engines (and
users) understand what it's about: the content, its structure, and the metadata
that describes it. Unlike tricks, on‑page SEO is mostly just *clear communication
done well* — which is why it overlaps so much with content and accessibility.

## Start with intent, not keywords

Modern search rewards content that genuinely answers what people are looking for
("search intent"). Understand the question behind the query, then answer it
better than the alternatives. Keyword research tells you *what people ask and how
they phrase it* — use it to shape genuinely useful content, not to stuff phrases.

> ❌ **Don't:** Keyword‑stuff (repeating a phrase unnaturally). It reads badly
> and search engines discount or penalize it.
> ✅ **Do:** Write naturally for humans, covering the topic thoroughly and using
> the words your audience actually uses.

## Title tags

The `<title>` is one of the most important on‑page signals and what usually shows
as the clickable headline in search results.

- Make each page's title **unique and descriptive**.
- Put the most important words near the front.
- Keep it a reasonable length so it isn't truncated (~50–60 characters is a
  common guideline).
- Reflect the page's actual content — don't bait‑and‑switch.

## Meta descriptions

The `<meta name="description">` doesn't directly affect ranking, but it's often
the snippet shown in results — so it affects **click‑through**.

- Write a compelling, accurate ~1–2 sentence summary.
- Make it unique per page.
- Include the page's value proposition; think of it as ad copy.

## Headings & structure

Headings (`<h1>`–`<h6>`) organize content for readers, screen readers, *and*
search engines.

- One clear **`<h1>`** describing the page.
- Logical, nested subheadings that outline the content (don't skip levels for
  looks). See [semantic HTML](../03-development-best-practices/semantic-html.md).
- Use headings to structure genuinely, not to game rankings.

This is a direct overlap with [accessibility](../04-accessibility/README.md) —
a good heading outline serves both.

## Content quality

- **Depth and usefulness** win. Thin, low‑value pages struggle.
- **Originality** — duplicate content competes with itself and with others.
- **Freshness** — keep important pages current (ties into
  [content strategy](../02-design-and-ux/content-strategy.md) and
  [maintenance](../09-maintenance/README.md)).
- **E‑E‑A‑T** — Experience, Expertise, Authoritativeness, Trustworthiness. Show
  who wrote it and why they're credible, especially for topics affecting health,
  finance, or safety.

## Links

- **Descriptive link text** — "read our maintenance guide," not "click here."
  Better for users, screen readers, *and* SEO (the link text describes the
  destination). ♿
- **Internal links** connect related content, help crawling, and distribute
  ranking signals — link generously and logically.
- **Outbound links** to quality sources can add value and credibility.
- ⚖️ For paid/sponsored or user‑generated links, use appropriate `rel` values
  (`sponsored`, `ugc`, `nofollow`) — misrepresenting paid links can violate
  search guidelines and advertising‑disclosure rules.

## Images

- **Descriptive alt text** (accessibility + image search + context). ♿
- Descriptive file names (`web-maintenance-checklist.jpg`, not `IMG_2381.jpg`).
- Optimized and appropriately sized (⚡ see
  [image optimization](../05-performance/image-and-asset-optimization.md)).

## Social/sharing metadata

Open Graph and similar tags control how pages appear when shared on social
platforms (title, description, image). They don't affect ranking directly but
improve click‑through and presentation when your content is shared.

## The through‑line

Almost every on‑page SEO best practice is also a **usability** or
**accessibility** best practice: clear titles, logical headings, descriptive
links, alt text, useful content. Do the fundamentals well and SEO largely takes
care of itself.
