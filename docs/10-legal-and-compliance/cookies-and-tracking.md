# Cookies & Tracking

Cookies and similar technologies (local storage, pixels, fingerprinting, SDKs)
are how sites remember users and track behavior. They're also one of the most
heavily regulated and most commonly **mishandled** areas of website law. Getting
consent wrong is a frequent, well‑publicized source of fines and complaints.

> ⚖️ Not legal advice. The rules differ by jurisdiction; this explains the common
> requirements and how to implement them defensibly.

## Types of cookies (by purpose)

- **Strictly necessary / essential** — required for the site to function (session,
  security, load balancing, remembering cart contents). Generally **do not
  require consent**.
- **Functional / preferences** — remember choices (language, region). Often need
  consent.
- **Analytics / performance** — measure usage. Generally **non‑essential →
  consent required** (in the EU/UK).
- **Advertising / targeting** — track across sites for ads. **Consent required**,
  and also implicate "sale/sharing" under [CCPA/CPRA](ccpa-cpra.md).

The key legal line is **essential vs. non‑essential**. Non‑essential trackers are
where consent obligations bite.

## The EU/UK rule: prior opt‑in consent

Under the **ePrivacy Directive** (the "cookie law") plus [GDPR](gdpr.md), storing
or reading non‑essential cookies/trackers requires **prior, informed, opt‑in
consent**. In practice:

> ✅ **Do:**
> - **Don't set non‑essential cookies/trackers until the user consents.** This is
>   the part most sites get wrong — the tracker must not fire on page load.
> - Make **"Accept" and "Reject" equally easy** — a one‑click reject at the same
>   level as accept.
> - Get **granular** consent (separate toggles for analytics vs. advertising,
>   etc.).
> - Make it **easy to withdraw** consent later (a persistent way to change cookie
>   settings).
> - **Record** consents (what, when).
> - Explain each category in your [privacy policy](privacy-policy.md) or a
>   dedicated cookie policy.

> ❌ **Don't:**
> - Use **pre‑ticked boxes** or treat continued browsing as consent — not valid.
> - Fire analytics/ads **before** consent and hope nobody checks — regulators and
>   automated audits do check, and enforcement has followed.
> - Use **dark patterns**: a giant "Accept all" with a buried, multi‑click
>   "reject." Regulators and the EU treat manipulative consent banners as
>   non‑compliant. See [UX principles: dark patterns](../02-design-and-ux/ux-principles.md).
> - Make access conditional on accepting non‑essential cookies ("cookie walls")
>   where prohibited.

## The US approach: notice + opt‑out

The US (via [CCPA/CPRA](ccpa-cpra.md) and other state laws) generally uses an
**opt‑out** model for the "sale/sharing" of data, rather than EU‑style opt‑in.
Key points:

- Provide notice and, where you "sell"/"share" data (which includes much
  cross‑context ad tracking), an **opt‑out** (e.g., "Do Not Sell or Share My
  Personal Information").
- Honor **Global Privacy Control (GPC)** browser signals where required.

## Consent management platforms (CMPs)

A **CMP** is tooling (a banner + preference center + logging) that manages
consent. A good CMP will:

- Block non‑essential scripts until consent is given.
- Offer granular categories and easy accept/reject.
- Store and log consent, and let users change it later.
- Recognize opt‑out signals like GPC.

> 💡 Choosing a CMP is easier than configuring it correctly. The common failure
> is a CMP that shows a banner but still **loads trackers before consent** — test
> this. Use your browser's dev tools to confirm nothing non‑essential fires
> before you click "accept."

## Third‑party scripts are the usual culprits

Analytics, ad tags, social embeds, chat widgets, A/B tools, and even **remote
fonts** can set cookies or transmit personal data (like IP addresses) to third
parties.

> ⚖️ A well‑known example: a German court found that loading **Google Fonts from
> Google's servers** transmitted users' IP addresses without consent, violating
> GDPR. **Self‑hosting** fonts and other assets avoids this (and is often faster —
> ⚡ see [image & asset optimization](../05-performance/image-and-asset-optimization.md)).

Audit every third‑party script for what it loads and where it sends data. Load
only what you need, and gate the non‑essential ones behind consent.

## Reduce the burden: collect less, track less

The simplest compliance strategy is to **need less consent**:

- Prefer **privacy‑friendly, cookieless analytics** that avoid personal data. See
  [analytics](../06-seo/analytics.md).
- **Self‑host** assets to avoid third‑party data leakage.
- Remove trackers you don't actually use.

Fewer trackers means fewer consent hurdles, less legal risk, faster pages, and
more trust. This is a case where the compliant path is also the better‑engineered
one.

## Implementation checklist

- [ ] Inventory every cookie/tracker and classify essential vs. non‑essential.
- [ ] Block non‑essential ones until consent (EU/UK) or provide opt‑out (US).
- [ ] Banner offers **equal, easy** accept and reject; granular categories.
- [ ] Users can **withdraw/change** consent anytime.
- [ ] **Record** consents; honor **GPC**/opt‑out signals where required.
- [ ] Cookie/privacy policy explains each category. See
      [privacy policy](privacy-policy.md).
- [ ] **Test** that nothing non‑essential fires before consent.
- [ ] Reconsider whether you can drop trackers entirely.

> 💡 The engineering side of this — inventorying vendor scripts, gating them on
> consent, and verifying nothing fires before the user answers — is in
> [third‑party scripts](../03-development-best-practices/third-party-scripts.md).

## Primary sources

- [Directive 2002/58/EC (ePrivacy Directive), on EUR‑Lex](https://eur-lex.europa.eu/eli/dir/2002/58/oj)
  — Article 5(3) is the "cookie law" storage‑and‑access rule.
- [Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
  — supplies the consent standard the ePrivacy rule relies on.
- [European Data Protection Board](https://edpb.europa.eu/edpb_en) — guidelines on
  consent and on dark patterns in consent interfaces.
- [California Privacy Protection Agency](https://cppa.ca.gov/regulations/) and
  [Global Privacy Control](https://globalprivacycontrol.org/) — the US opt‑out
  side, including the GPC signal specification.
