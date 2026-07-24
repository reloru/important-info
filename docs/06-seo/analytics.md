# Analytics & Measurement

You can't improve what you don't measure. Analytics tells you what people do on
your site — which pages they find, where they drop off, what converts — so you
can make informed decisions instead of guessing. But analytics also means
**collecting data about people**, which brings privacy law squarely into play.

## What to measure

Focus on metrics tied to your goals, not vanity numbers:

- **Acquisition** — how people find you (search, direct, referral, social).
- **Behavior** — which pages they visit, how they move through the site, where
  they leave.
- **Conversions** — the actions that matter (sign‑ups, purchases, contacts).
- **Performance** — real‑user [Core Web Vitals](../05-performance/core-web-vitals.md).
- **Search performance** — impressions, clicks, and queries (via a search
  engine's webmaster/console tools) — invaluable and privacy‑friendly.

> ✅ **Do:** Define your key questions first, then choose metrics that answer
> them. A dashboard full of numbers nobody acts on is noise.

## Tools

- **Search Console / webmaster tools** — how you appear in search; index
  coverage; queries. Essential and low‑privacy‑impact.
- **Web analytics platforms** — general‑purpose analytics (page views, journeys,
  conversions).
- **Privacy‑friendly analytics** — tools designed to avoid personal data and
  cookies (often cookieless, aggregated). Increasingly popular precisely because
  they sidestep much of the legal burden below.
- **Real‑user monitoring (RUM)** — field performance data.

## Analytics is a privacy matter

> ⚖️ **Legal note:** Most analytics involves processing personal data (IP
> addresses, identifiers, behavior) and often uses cookies or similar
> technologies. That triggers real legal obligations:
>
> - **Consent for non‑essential tracking.** Under EU/UK rules (the ePrivacy
>   "cookie law" plus GDPR), analytics/marketing cookies and similar trackers
>   generally require **prior, informed, opt‑in consent** — you must not load
>   them until the user agrees. See
>   [cookies & tracking](../10-legal-and-compliance/cookies-and-tracking.md).
> - **Disclosure.** Your [privacy policy](../10-legal-and-compliance/privacy-policy.md)
>   must say what you collect, why, and with whom you share it.
> - **International transfers.** Some analytics tools send data to other
>   countries; EU regulators have challenged certain configurations of common
>   US‑based analytics. See [GDPR](../10-legal-and-compliance/gdpr.md).
> - **US state laws** (e.g., CCPA/CPRA) give users rights to opt out of certain
>   "sharing" for cross‑context advertising. See
>   [CCPA/CPRA](../10-legal-and-compliance/ccpa-cpra.md).

## Practical, compliant analytics

> ✅ **Do:**
> - Prefer **privacy‑friendly, cookieless** analytics where it meets your needs
>   — it reduces both legal burden and consent friction.
> - If you use consent‑gated analytics, **don't load it before consent**, and
>   honor opt‑outs.
> - **Anonymize/minimize** where you can (e.g., truncate IPs, avoid collecting
>   more than you need — data minimization is a GDPR principle).
> - Disclose everything in your privacy and cookie policies.
> - Respect **Global Privacy Control / Do Not Track** signals where legally
>   required.

> ❌ **Don't:**
> - Drop tracking scripts before consent and hope nobody notices — regulators
>   and browser tooling do notice, and fines have followed.
> - Collect personal data "just in case." If you don't need it, don't collect
>   it. Every field you store is a liability.

## From data to decisions

Analytics is only useful if it changes what you do:

- Look for **drop‑off points** in key journeys and fix the friction (a UX win —
  see [UX principles](../02-design-and-ux/ux-principles.md)).
- Find **high‑exit pages** and improve their content or performance.
- Run experiments to test changes rather than arguing about opinions.
- Feed findings back into the [maintenance plan](../09-maintenance/maintenance-plan.md).

> 💡 The best analytics setup is the **minimum** that answers your real
> questions — less data to protect, fewer consent hurdles, and clearer signal.
