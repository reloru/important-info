# E‑commerce Law

Selling online adds a layer of legal obligations on top of everything else in
this section — consumer‑protection rules, mandatory disclosures, tax collection,
payment‑data security, and more. These rules exist to protect buyers, and
regulators enforce them. If your site takes money, this page is for you.

> ⚖️ Not legal advice. E‑commerce rules are highly jurisdiction‑specific and
> depend on what you sell and to whom; get professional advice.

## Consumer protection: transparency is the theme

Consumer laws (strong in the EU/UK, meaningful in the US and elsewhere) broadly
require you to be **clear and honest** before and during a sale.

> ✅ **Do — disclose clearly, before purchase:**
> - **Who you are** — business identity and contact details.
> - **The product/service** — accurate description, key characteristics.
> - **The total price** — including taxes and, importantly, **all fees**. Hidden
>   or late‑revealed costs ("drip pricing") are unlawful in many places.
> - **Shipping/delivery** costs and timeframes.
> - **Payment terms.**
> - **Return, refund, and cancellation** rights and how to use them.

> ❌ **Don't:**
> - Use **dark patterns** at checkout — pre‑ticked add‑ons, fake urgency/scarcity,
>   hidden costs, "confirmshaming," or making cancellation hard. These are
>   increasingly **illegal** (EU consumer law, US FTC action, CPRA). See
>   [UX: dark patterns](../02-design-and-ux/ux-principles.md).
> - Misrepresent products, prices, or availability. Keep listings accurate — see
>   [content updates](../09-maintenance/content-updates.md).

## Right of withdrawal / cancellation

> ⚖️ In the **EU/UK**, consumers generally have a **"cooling‑off" right** to
> cancel most online purchases within **14 days** and get a refund, with limited
> exceptions (e.g., custom goods, some digital content once started with
> consent). You must **inform** consumers of this right — failing to do so can
> *extend* the cancellation window substantially. US rules differ (there's no
> blanket federal cooling‑off for online sales), so your refund policy and state
> rules govern — but you must honor whatever policy you publish.

Publish a clear **refund/returns policy** and follow it.

## The checkout must not trick users

The purchase step is heavily scrutinized:

- The button that creates a payment obligation must be **clearly labeled** (EU
  rules require wording like "Order with obligation to pay").
- Show the **final total** before the user commits.
- Get **explicit** agreement for any extras — no pre‑checked upsells.
- Make **terms** and policies available and require agreement where appropriate
  (clickwrap — see [terms of service](terms-of-service.md)).

## Payments & PCI DSS

> 🔒 Handling card data brings **PCI DSS** (Payment Card Industry Data Security
> Standard) obligations. The safest approach for most sites is to **never touch
> raw card data** — use a reputable payment processor (hosted checkout or
> tokenized fields) so card details go directly to the processor. This
> dramatically reduces your PCI scope and risk. Never store card numbers
> yourself unless you truly must and are properly certified. See
> [Security](../07-security/README.md).

For the full picture — how online payments work, choosing a provider (including
whether a **merchant of record** should own tax for you), integrating Stripe, PCI
scope, Strong Customer Authentication, disputes, and operations — see the
[**Payments** section](../11-payments/README.md).

## Tax

> ⚖️ **Sales tax / VAT / GST** on online sales is complex and location‑dependent:
> - **US:** post‑*Wayfair*, states can require **sales tax** collection based on
>   economic nexus (sales thresholds), even without a physical presence.
> - **EU:** **VAT** rules apply, including special rules for digital services and
>   cross‑border sales (e.g., charging VAT based on the customer's country, and
>   schemes like OSS/MOSS).
> - Thresholds, rates, and registration duties vary widely.
>
> This is an area to get **accounting/tax advice** and to use tax‑calculation
> tooling — getting it wrong creates real liability. Tools like **Stripe Tax**
> calculate and collect tax, but as a processor you still register and remit; a
> **merchant of record** can take over tax entirely for a higher fee. See
> [choosing a payment provider](../11-payments/choosing-a-payment-provider.md).

## Digital goods and subscriptions

- **Digital content/services** have their own consumer rules (e.g., disclosures,
  and effects on the withdrawal right once delivery/consumption begins).
- **Subscriptions / auto‑renewals** face specific rules in many places: clear
  disclosure of recurring charges, easy cancellation ("click to cancel" style
  requirements are spreading), and renewal reminders. Making cancellation harder
  than sign‑up is increasingly prohibited.

## Also applies to e‑commerce

Selling doesn't exempt you from the rest of this section — it adds to it:

- **Privacy** — you're processing customer personal data. See
  [GDPR](gdpr.md), [CCPA/CPRA](ccpa-cpra.md), and
  [privacy policy](privacy-policy.md).
- **Terms of Service** — your sales contract. See
  [terms of service](terms-of-service.md).
- **Email marketing** — order emails vs. marketing; consent and unsubscribe. See
  [email marketing law](email-marketing-law.md).
- **Accessibility** — the EAA specifically covers e‑commerce. See
  [accessibility law](accessibility-law.md).
- **Security** — you're a payment and data target. See
  [Security](../07-security/README.md).

## Checklist for selling online

- [ ] Business identity and contact details clearly shown.
- [ ] Accurate product descriptions and **all‑in pricing** (taxes + fees).
- [ ] Shipping, delivery, returns/refunds, and cancellation rights disclosed.
- [ ] Cooling‑off/withdrawal rights honored where they apply (e.g., EU/UK 14 days).
- [ ] Checkout free of dark patterns; payment‑obligation button clearly labeled.
- [ ] Payments handled via a reputable processor; **PCI scope minimized.** 🔒
- [ ] Sales **tax/VAT/GST** handled correctly (get advice/tooling).
- [ ] Subscriptions: clear recurring terms and **easy cancellation.**
- [ ] Privacy, terms, and security obligations met.
