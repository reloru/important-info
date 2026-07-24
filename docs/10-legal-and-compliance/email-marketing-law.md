# Email Marketing Law

If your site sends email — newsletters, promotions, order updates, drip
campaigns — you're subject to anti‑spam and marketing laws. These vary by country
but share common requirements around **consent, honesty, and easy unsubscribe.**
Violations carry real per‑message penalties and can get your domain blacklisted.

> ⚖️ Not legal advice. Rules differ by jurisdiction and by whether a message is
> "marketing" vs. "transactional." Confirm your obligations.

## The two big regimes

### CAN‑SPAM (United States) — opt‑out model
The US law governing commercial email. It doesn't require prior consent, but it
sets firm rules for commercial messages:

- **No false or misleading headers** — "From," "To," and routing must be accurate.
- **No deceptive subject lines** — they must reflect the content.
- **Identify the message as an ad** (where applicable).
- **Include a valid physical postal address.**
- **Provide a clear opt‑out** and **honor it promptly** (within 10 business days);
  you can't charge or require info beyond an email address to unsubscribe.
- You're responsible even if someone else sends on your behalf.

Penalties can be **substantial per email**, so mistakes scale fast.

### GDPR + ePrivacy (EU/UK) — opt‑in model
Stricter: marketing email generally requires **prior, opt‑in consent.**

- **Consent must be freely given, specific, informed** (no pre‑ticked boxes, no
  bundling into terms acceptance). See [GDPR](gdpr.md).
- **Easy withdrawal** — every message must let recipients unsubscribe easily, and
  you must honor it.
- **Identify the sender** and provide contact details.
- The recipient's email address is **personal data**, so all of GDPR applies to
  how you collect, store, and use your list.

### CASL (Canada) — strict opt‑in
Canada's anti‑spam law is among the strictest: it generally requires **express
consent** before sending commercial electronic messages, mandates **sender
identification**, and requires a working **unsubscribe** mechanism. Penalties are
significant.

Other countries (Australia's Spam Act, etc.) have their own rules — mostly
consent‑ and unsubscribe‑focused.

## The "soft opt‑in" nuance

Many regimes allow emailing **existing customers** about **similar products/
services** without fresh opt‑in consent — *if* you collected the address during a
sale, offered an opt‑out at collection, and offer one in every message. This is a
narrow exception; don't stretch it to cover cold marketing or unrelated products.

## Transactional vs. marketing email

- **Transactional** messages (order confirmations, password resets, shipping
  notices, account notices) are about a transaction the user initiated and are
  generally exempt from marketing‑consent rules.
- **Marketing** messages (promotions, newsletters, offers) trigger the consent/
  opt‑out rules above.

> ⚠️ **Don't smuggle marketing into transactional emails.** Adding promotional
> content to an order confirmation can turn it into a marketing message subject
> to the full rules. Keep them separate.

## Good practice everywhere

> ✅ **Do:**
> - Use **opt‑in** (ideally **double opt‑in**: confirm via a link) — it's the
>   safest global baseline, improves list quality, and aids consent records.
> - Keep **records of consent** — what, when, and how.
> - Put a **clear, one‑click‑style unsubscribe** in every marketing email and
>   process it **promptly**.
> - **Identify yourself** truthfully and include required details (e.g., postal
>   address for CAN‑SPAM).
> - **Authenticate your domain** (SPF, DKIM, DMARC) — improves deliverability and
>   prevents spoofing. See
>   [DNS, domains & SSL](../08-deployment-and-devops/domains-dns-ssl.md).
> - Segment by jurisdiction if your rules differ.

> ❌ **Don't:**
> - Buy or scrape email lists — a fast route to legal violations, spam
>   complaints, and blacklisting.
> - Use pre‑ticked consent boxes or bury consent in the terms.
> - Make unsubscribing hard, or keep emailing after someone opts out.
> - Use misleading subject lines or fake sender info.

## Consent ties back to the whole stack

Newsletter sign‑ups are a data‑collection point, so they intersect with:

- [Privacy policy](privacy-policy.md) — disclose what you do with the address.
- [GDPR](gdpr.md)/[CCPA/CPRA](ccpa-cpra.md) — it's personal data with rights
  attached (including the right to object to marketing).
- [UX](../02-design-and-ux/ux-principles.md) — an honest, clear sign‑up (no dark
  patterns).

## Checklist

- [ ] Marketing email uses **opt‑in consent** (double opt‑in recommended);
      consent is **recorded**.
- [ ] Every marketing message has an **easy unsubscribe**, honored promptly.
- [ ] Sender identity and required details (e.g., postal address) are present and
      truthful.
- [ ] Subject lines and headers are **accurate**.
- [ ] Marketing is kept **separate** from transactional email.
- [ ] Domain email **authentication** (SPF/DKIM/DMARC) is configured.
- [ ] List is **self‑collected**, never bought or scraped.
- [ ] Jurisdictional differences (CAN‑SPAM vs. GDPR vs. CASL) accounted for.
