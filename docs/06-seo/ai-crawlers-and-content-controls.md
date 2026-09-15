# AI Crawlers & Content Controls

Search crawlers have visited your site for decades under a well‑understood
bargain: you let them index your content, they send you visitors. **AI crawlers
break that bargain's symmetry.** Some still send traffic; others read your
content to train a model, or to answer a user's question directly — in which case
the visitor may never arrive at all.

This page is about the controls you actually have, what each one does, and the
honest limits of all of them. It's a companion to
[technical SEO](technical-seo.md), which covers ordinary crawling and indexing.

> ⚖️ Not legal advice. Whether AI training on public web content is lawful is
> **genuinely unsettled** and is being litigated in several jurisdictions.
> Nothing here resolves that; it describes the technical signals available and
> how to use them deliberately. See
> [copyright & IP](../10-legal-and-compliance/copyright-and-ip.md).

## First, decide what you actually want

This is a business and editorial decision before it's a technical one, and the
answer is not the same for every site.

| Your situation | Typical stance |
|---|---|
| **You sell content** (publisher, courses, research) | Restrict training; often allow AI search so you still get cited |
| **You sell a product or service** | Usually allow everything — being in AI answers is discovery |
| **Documentation for your own product** | Allow freely; you *want* assistants to answer accurately about you |
| **You host user‑generated content** | Consider what you promised contributors; your terms may constrain you |

Note the axis that matters most: **training is not the same as retrieval.**
Providers now ship separate agents for separate purposes, which means "block AI"
is rarely the right instruction — it usually means "block training but stay
answerable."

## robots.txt: the main control

`robots.txt` is a real standard — **RFC 9309**, the Robots Exclusion Protocol —
and it remains the primary mechanism. AI vendors document their tokens and, for
the major ones, state that they honor it.

What the significant tokens are, per each vendor's own documentation:

| Token | Operator | Purpose |
|---|---|---|
| `GPTBot` | OpenAI | Crawls content that may be used to train foundation models |
| `OAI-SearchBot` | OpenAI | Surfaces sites in ChatGPT's search features |
| `ChatGPT-User` | OpenAI | Fetches triggered by a user's action in ChatGPT |
| `OAI-AdsBot` | OpenAI | Validates the safety of pages submitted as ads |
| `ClaudeBot` | Anthropic | Collects web content that may contribute to training |
| `Claude-SearchBot` | Anthropic | Improves search result quality |
| `Claude-User` | Anthropic | Fetches on behalf of a user's question |
| `Google-Extended` | Google | **Not a crawler** — see the trap below |

> ⚠️ **`Google-Extended` is a control token, not a crawler.** It has no separate
> user‑agent string of its own; Google crawls with its existing agents and uses
> this token purely as a robots.txt control over whether crawled content may be
> used for Gemini training and grounding. Per Google, it **does not affect
> inclusion in Google Search and is not a ranking signal.** So disallowing it
> costs you nothing in Search — and blocking `Googlebot` when you meant
> `Google-Extended` costs you everything.

A stance of "stay discoverable, decline training" looks like this:

```
# Decline model training
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

# Remain answerable and citable
User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /
```

> ✅ **Do:** Name tokens explicitly, keep the file under version control, and
> re‑check it after any platform migration — a stray site‑wide `Disallow` is one
> of the most damaging and most common SEO self‑inflicted wounds. See
> [technical SEO](technical-seo.md).
> ❌ **Don't:** Assume a blanket `User-agent: *` block is wise. It hits search
> engines too, and the vendor tokens you actually meant to stop are the ones that
> need naming.

## The honest limits

Be clear‑eyed about what `robots.txt` is and isn't:

- **It's a request, not an enforcement mechanism.** RFC 9309 defines how
  compliant crawlers should behave. Nothing stops a non‑compliant one, and a
  user agent string can claim to be anything.
- **It doesn't protect anything.** `robots.txt` is public, and listing a path
  advertises it. Never use it to hide sensitive content — that needs
  [authentication](../07-security/authentication-and-authorization.md).
- **It's prospective.** Disallowing training today does nothing about content
  already collected.
- **User‑triggered fetches may not be covered.** When a person pastes your URL
  into an assistant, that fetch is arguably on the user's behalf rather than a
  crawl, and vendors treat those agents differently.

If you need enforcement rather than a request, you're looking at authentication,
rate limiting, or bot‑management at the CDN — see
[forms & input handling](../03-development-best-practices/forms-and-input-handling.md)
for the rate‑limiting side, and your CDN's own tooling for the rest.

## llms.txt: useful, but know what it is

**`llms.txt`** is a proposed convention — a Markdown file at your domain root
that points assistants at clean, structured versions of your key pages, so they
can find the good content without wading through navigation and layout.

Its status matters more than its mechanics: **it is a community convention, not
an adopted standard.** No major AI provider has committed to consistently
fetching it, and support is inconsistent. It has, however, seen real adoption in
one specific niche — **developer documentation**, where coding assistants
pointed at a docs site do look for it.

> 💡 The honest recommendation: if you publish **technical documentation**,
> `llms.txt` is cheap and plausibly useful. Otherwise treat it as optional and
> speculative. It is also **not a permission mechanism** — it helps a cooperative
> agent read you efficiently; it expresses no restriction and enforces nothing.
> Don't mistake it for a control.

## What's actually being standardized

The real standards work is at the **IETF**, in the **AI Preferences (aipref)
working group**, chartered to standardize building blocks for expressing
preferences about how content is collected and used for AI. Two standards‑track
drafts are in progress:

- `draft-ietf-aipref-vocab` — a vocabulary for expressing AI preferences.
- `draft-ietf-aipref-attach` — how to attach those preferences to content, via
  mechanisms such as HTTP headers and well‑known URIs.

Neither has been published as an RFC yet. This is the space to watch: a
vendor‑neutral vocabulary would replace today's arrangement, where every
provider invents its own token and you maintain a list by hand.

## Tie it to your terms

> ⚖️ Your robots.txt expresses a preference; your **terms of service** and the
> **licence on your content** express a legal position. They should not
> contradict each other. If your site permits reuse under a permissive licence,
> a training block is a mixed message. If your terms restrict automated
> collection, say so there as well as in robots.txt. See
> [terms of service](../10-legal-and-compliance/terms-of-service.md),
> [copyright & IP](../10-legal-and-compliance/copyright-and-ip.md), and
> [licensing](../10-legal-and-compliance/licensing.md).

## Checklist

- [ ] A deliberate, written **stance** on AI training vs. AI search exists.
- [ ] `robots.txt` names vendor tokens **explicitly**, not just `*`.
- [ ] `Google-Extended` is handled — and **not** confused with `Googlebot`.
- [ ] Training and search agents are distinguished, not lumped together.
- [ ] Nothing sensitive is "protected" by `robots.txt` alone.
- [ ] Terms of service and content licensing are **consistent** with the stance.
- [ ] Server logs are checked periodically for which agents actually visit.
- [ ] The vendor token list is re‑checked on a schedule — these change.

## Primary sources

- [RFC 9309 — Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html)
  — the standard behind `robots.txt`.
- [OpenAI — bots and crawlers](https://developers.openai.com/api/docs/bots) —
  authoritative token list and the purpose of each.
- [Anthropic — does Anthropic crawl the web, and how can site owners block the crawler?](https://privacy.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
  — ClaudeBot, Claude‑SearchBot, Claude‑User, and their robots.txt handling.
- [Google — common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
  — including that `Google-Extended` is a control token with no separate agent
  string and no Search impact.
- [IETF AI Preferences (aipref) working group](https://datatracker.ietf.org/wg/aipref/about/)
  and [`draft-ietf-aipref-vocab`](https://datatracker.ietf.org/doc/draft-ietf-aipref-vocab/)
  — the standards‑track effort.
- [llmstxt.org](https://llmstxt.org/) — the `llms.txt` proposal itself.

*Vendor tokens and draft statuses were verified against these sources in
**September 2026**. This area moves fast — re‑check before relying on a token
name or a standard's status.*
