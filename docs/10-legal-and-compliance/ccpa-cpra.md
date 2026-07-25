# CCPA / CPRA (US State Privacy Laws)

The **California Consumer Privacy Act (CCPA)**, as amended and expanded by the
**California Privacy Rights Act (CPRA)**, is the leading US state privacy law. It's
the American counterpart to [GDPR](gdpr.md) — different in structure and
thresholds, but similar in spirit: transparency, consumer rights, and
accountability. California is also the front of a **broader wave** of US state
privacy laws.

> ⚖️ Not legal advice. Thresholds and rules change and vary by state; confirm
> your obligations with a professional.

## Does it apply to you?

The CCPA/CPRA generally applies to **for‑profit businesses that handle California
residents' personal information and meet at least one threshold**, such as:

- annual gross revenue above a set amount (commonly cited around **$25 million**),
  **or**
- buying/selling/sharing the personal information of a large number of consumers
  (commonly cited around **100,000**), **or**
- deriving a significant share (e.g., 50%+) of revenue from selling/sharing
  personal information.

Thresholds are adjusted over time — check current figures. Many small sites fall
below them, but if you're a growing business handling lots of Californians' data,
take it seriously.

## Key concepts

- **Personal information** — broadly defined, including identifiers, internet
  activity, geolocation, inferences, and more.
- **Sale / sharing** — defined broadly. "**Sharing**" notably covers disclosing
  personal information for **cross‑context behavioral advertising**, even without
  money changing hands. This sweeps in a lot of common ad‑tech.
- **Sensitive personal information** — a special category (e.g., precise
  geolocation, race, health, financial account details) with extra rights.
- **Service provider / contractor** — roughly analogous to a GDPR processor;
  needs appropriate contracts.

## Consumer rights

California consumers have rights including:

- **Know / Access** — what personal information you collect, use, disclose, sell,
  or share.
- **Delete** — request deletion of their personal information.
- **Correct** — fix inaccurate personal information.
- **Opt out of sale/sharing** — including a required **"Do Not Sell or Share My
  Personal Information"** mechanism.
- **Limit use of sensitive personal information.**
- **Non‑discrimination** — you can't penalize consumers for exercising rights.

## What you generally must do

> ✅ **Do:**
> - Provide a clear **privacy policy** describing categories collected, purposes,
>   and consumer rights (see [privacy policy](privacy-policy.md)).
> - Offer accessible **rights‑request mechanisms** (and verify requesters'
>   identity).
> - If you "sell" or "share" personal information, provide an **opt‑out** — often
>   a **"Do Not Sell or Share My Personal Information"** link, and honor
>   browser‑level **opt‑out preference signals** (like Global Privacy Control).
> - Put **contracts** in place with service providers/contractors.
> - Give extra treatment to **sensitive personal information** and to **minors**
>   (opt‑in rules apply to selling/sharing data of those under 16).

> ❌ **Don't:**
> - Assume ad trackers/analytics fall outside "sharing" — cross‑context
>   behavioral advertising often counts, triggering opt‑out obligations.
> - Ignore **opt‑out preference signals** where required.
> - Discriminate against users who exercise their rights.

## GPC and opt‑out signals

The **Global Privacy Control (GPC)** is a browser signal that communicates a
user's opt‑out of sale/sharing. California requires businesses to treat it as a
valid opt‑out request. Build your consent/opt‑out tooling to recognize it. See
[cookies & tracking](cookies-and-tracking.md).

## The wider US landscape

California isn't alone — a **growing number of US states** have enacted their own
comprehensive privacy laws (Virginia, Colorado, Connecticut, Utah, Texas, and
more, with others following). They share themes (notice, access, deletion,
opt‑out of targeted advertising/sale) but differ in thresholds and details.

> 💡 **Practical approach:** Rather than chasing each state's specifics, build to
> a **high common baseline** — transparent privacy notice, honor opt‑outs
> (including GPC), support access/deletion/correction, minimize data, and secure
> it. That posture satisfies much of the overlapping US patchwork and aligns with
> [GDPR](gdpr.md) too.

## CCPA/CPRA vs. GDPR (quick contrast)

| | GDPR | CCPA/CPRA |
|---|------|-----------|
| Applies to | Anyone processing EU/UK data (no size threshold) | For‑profits meeting size/volume thresholds |
| Default for tracking | **Opt‑in** consent | **Opt‑out** of sale/sharing |
| Basis needed to process | Yes (lawful basis) | Not framed that way; focuses on notice + opt‑out |
| Core rights | Access, delete, correct, object, portability, etc. | Know, delete, correct, opt‑out, limit sensitive |

If you comply well with GDPR, you're much of the way toward US state laws — but
the **opt‑in vs. opt‑out** difference and the specific "Do Not Sell or Share"
mechanics matter, so don't assume they're identical.
