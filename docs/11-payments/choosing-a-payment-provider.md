# Choosing a Payment Provider

Before writing a line of integration code, decide *who* processes your payments
and *what kind* of relationship you have with them. This choice affects your
fees, your compliance burden, how much tax paperwork you own, which markets you
can serve, and how much you can customize checkout. This page maps the landscape
and gives you a decision framework — including **when Stripe is not the right
choice.**

## First, the crucial distinction: processor vs. merchant of record

This is the decision that trips up the most people, especially sellers of
**digital goods and SaaS**.

### Payment processor / PSP (e.g., Stripe, PayPal, Adyen, Braintree, Square)
You are the **merchant of record** — the legal seller. The processor moves the
money, but **you** are responsible for:

- Registering for and remitting **sales tax / VAT / GST** wherever you have
  obligations,
- Consumer‑protection compliance,
- Chargebacks and disputes.

Fees are lower (commonly ~2.9% + a fixed fee for cards), but the **tax and
compliance work is yours.** Tools like **Stripe Tax** help *calculate* tax, but
you still register and file. See [e‑commerce law](../10-legal-and-compliance/ecommerce-law.md).

### Merchant of record (MoR) (e.g., Paddle, Lemon Squeezy, Polar, Gumroad, FastSpring)
The provider becomes the **legal seller of record.** They take on:

- **Sales tax / VAT / GST** — calculating, collecting, and **remitting** it
  worldwide, so you don't register in dozens of jurisdictions,
- Fraud and chargeback liability (largely),
- Billing compliance.

In exchange you pay a **higher fee** (often in the **~5%+** range vs. ~2.9% + 30¢).

> 💡 **The trade‑off in one line:** a **processor** is cheaper but you own global
> tax compliance; a **merchant of record** costs more but makes your tax and
> compliance headaches largely disappear. For a solo developer or small team
> selling **digital products or SaaS internationally**, an MoR can be worth the
> premium purely to avoid registering for VAT across the EU and tracking
> economic‑nexus thresholds across US states. For a business that already has tax
> infrastructure, or sells physical goods, a processor like Stripe is usually the
> better economic and control choice. See
> [e‑commerce law: tax](../10-legal-and-compliance/ecommerce-law.md).

## Related vocabulary you'll see

- **Gateway** — the piece that securely captures payment details and connects to
  processing. Historically a separate product; modern PSPs bundle it.
- **Processor** — moves transaction data between banks and networks.
- **Acquirer / merchant account** — the bank relationship that receives funds.
  The old model required you to obtain your own; PSPs pool this for you so you can
  start in minutes.
- **Aggregator** — a PSP that onboards you under its own master merchant account
  (how Stripe/PayPal let you start instantly, versus applying for a dedicated
  merchant account).

## The provider landscape (high level)

| Provider | Type | Best for | Notes |
|----------|------|----------|-------|
| **Stripe** | Processor/PSP | Developers, custom checkouts, SaaS, marketplaces | Deep API, strong docs, huge product surface (Billing, Connect, Tax, Radar…). The focus of this section. |
| **PayPal / Braintree** | Processor/PSP | Buyer trust, quick add‑on, PayPal balance users | Ubiquitous consumer brand; Braintree is its developer platform. |
| **Adyen** | Processor/PSP | Large enterprises, global scale | Enterprise‑grade, single platform for online + in‑person. |
| **Square** | Processor/PSP | In‑person + online retail, SMBs | Strong point‑of‑sale heritage. |
| **Paddle / Lemon Squeezy / Polar / FastSpring** | **Merchant of record** | Digital goods & SaaS wanting tax handled | Higher fees; they own tax/VAT and much of compliance. |
| **Gumroad** | MoR‑style | Creators selling digital products | Simple, creator‑focused. |
| Regional/bank gateways | Processor/gateway | Specific markets/banks | Varies widely. |

*(Availability, features, and fees change — verify against each provider's
current site.)*

## Why this section focuses on Stripe

Stripe is the most common choice for developers building custom web payments,
because it offers:

- A well‑designed, well‑documented **API** and strong developer tooling.
- A broad **product suite** covering one‑off payments, subscriptions,
  marketplaces, invoicing, tax, and fraud — so you can grow without switching
  platforms.
- **Fast onboarding** (aggregator model) and support for many payment methods and
  countries.
- Sensible **security and PCI** defaults (hosted fields keep you in the easiest
  scope). See [PCI compliance](pci-compliance.md).

The **concepts** here (authorization/capture, webhooks as source of truth,
idempotency, PCI scope, SCA, reconciliation) apply to *every* provider — only the
specific APIs differ. Learn them once and they transfer.

## When Stripe is *not* the best choice

Be honest about fit:

- **You're a small/solo seller of digital goods or SaaS and dread global tax** →
  a **merchant of record** (Paddle, Lemon Squeezy, …) may save you far more in
  compliance pain than it costs in fees.
- **Your customers strongly prefer a specific method/brand** (e.g., PayPal
  balance, or a regional method Stripe doesn't cover well in your market) → offer
  what they'll actually use. See
  [payment methods](how-online-payments-work.md).
- **You need only a one‑off "pay me" link and no code** → a no‑code tool or a
  Stripe **Payment Link** may be all you need (still Stripe, but zero
  integration). See [integrating Stripe](stripe-integration.md).
- **Stripe isn't available or well‑supported in your country** — availability and
  supported payout countries vary; check before committing.
- **You're at large enterprise scale** with complex needs → evaluate Adyen and
  others on IC+ pricing, in‑person, and global acquiring.

## A decision framework

Ask, in order:

1. **Do I want to own global tax/compliance?** No, and I sell digital/SaaS →
   strongly consider a **merchant of record**. Yes, or I have tax support →
   **processor/PSP**.
2. **How much checkout control do I need?** None (no‑code link) → Payment
   Links/hosted. Standard hosted checkout → Checkout. Fully custom UI → the
   Payment Element. (All are Stripe options — see
   [integrating Stripe](stripe-integration.md).)
3. **What do my customers pay with, and where are they?** Match methods and
   supported countries to your audience.
4. **What will I need in 12–24 months?** Subscriptions? A marketplace paying out
   to third parties? Invoicing? Favor a platform that covers your roadmap so you
   don't re‑integrate later.
5. **Total cost of ownership**, not just headline rate — integration effort,
   maintenance, tax handling, dispute tooling, and add‑on product fees. See
   [budgeting & scoping](../01-planning-and-strategy/budgeting-and-scoping.md).

> ✅ **Do:** Pick based on tax model, customer methods, control needs, and your
> roadmap — not just the advertised percentage.
> ❌ **Don't:** Assume "Stripe" is automatically right; for global digital‑goods
> sellers especially, the merchant‑of‑record question can dominate everything
> else.

Once you've chosen Stripe (as the rest of this section assumes), continue to the
[Stripe overview](stripe-overview.md).
