# 11 · Payments (with a focus on Stripe)

Accepting money online is one of the highest‑stakes things a website can do. Get
it right and it's almost invisible; get it wrong and you face lost sales, angry
customers, fraud, fines, frozen funds, or leaked card data. This section is a
practical, fairly exhaustive guide to taking payments on the web — the concepts,
the decisions, and a deep, hands‑on focus on **Stripe**, the most popular
developer‑oriented payment platform.

> This section sits **outside the numbered life‑cycle** (00–10) as a
> **feature deep‑dive**: payments is a capability you add to a site, not a phase
> every site goes through. It leans more technical than the rest of the KB
> because integrating payments genuinely requires it — but it stays focused on
> architecture, best practices, security, and compliance rather than
> line‑by‑line code (which belongs in the provider's own docs).

> ⚖️🔒 **Read this first.** Payments touch **security** (card data, secrets),
> **legal/compliance** (PCI DSS, SCA, tax, consumer rights), and **operations**
> (reconciliation, disputes, payouts) all at once. Nothing here is legal,
> financial, or PCI‑audit advice, and payment platforms and rules change — always
> confirm specifics against the provider's current official documentation and,
> where money and liability are real, a qualified professional.

## Why payments deserve their own section

- **You are handling other people's money and card data.** Mistakes have direct
  financial and legal consequences, not just a broken page.
- **The "happy path" is the easy 20%.** The hard, essential 80% is everything
  around it: failed payments, refunds, disputes, fraud, webhooks, reconciliation,
  tax, and recurring billing.
- **It's a trust surface.** A clunky, scary, or broken checkout kills conversions
  faster than almost anything else. See [UX principles](../02-design-and-ux/ux-principles.md).
- **Compliance is mandatory, not optional** — PCI DSS for card data, Strong
  Customer Authentication in Europe, sales tax/VAT, and consumer‑protection
  rules. See [e‑commerce law](../10-legal-and-compliance/ecommerce-law.md).

## In this section

Read top to bottom if payments are new to you — each page builds on the last.

1. **[How online payments work](how-online-payments-work.md)** — the ecosystem,
   the players, the money flow (authorization → capture → settlement → payout),
   fees, and payment methods. Start here.
2. **[Choosing a payment provider](choosing-a-payment-provider.md)** — processor
   vs. gateway vs. **merchant of record**; the landscape (Stripe, PayPal, Adyen,
   Paddle, Lemon Squeezy…); and when *not* to use Stripe.
3. **[PCI compliance](pci-compliance.md)** — what PCI DSS requires, and how to
   stay in the easiest scope (**SAQ A**) by never touching raw card data.
4. **[Stripe overview](stripe-overview.md)** — Stripe's products, the core API
   objects, keys, test vs. live mode, and the Dashboard.
5. **[Integrating Stripe](stripe-integration.md)** — Payment Links vs. Checkout
   vs. the Payment Element; the PaymentIntent lifecycle; idempotency; and the
   golden rule: **never trust the client**.
6. **[Webhooks & fulfillment](webhooks-and-fulfillment.md)** — why webhooks are
   the source of truth, verifying signatures, idempotent handling, and reliably
   fulfilling orders. The most important page for correctness.
7. **[Subscriptions & billing](subscriptions-and-billing.md)** — recurring
   payments, trials, proration, failed‑payment recovery (dunning), the customer
   portal, and the legal rules around auto‑renewal.
8. **[Disputes, refunds & fraud](disputes-refunds-and-fraud.md)** — chargebacks,
   refunds, fraud prevention (Radar), and 3D Secure / Strong Customer
   Authentication.
9. **[Going live & operations](going-live-and-operations.md)** — testing with the
   Stripe CLI, the go‑live checklist, payouts, reconciliation, reporting, tax
   (Stripe Tax), and monitoring.

## The mental model in one paragraph

When a customer pays, their card details go **directly to your payment provider**
(never to your server), the provider asks the customer's bank to **authorize** the
amount, you **capture** it, the money is **settled** by the card networks and
banks, and days later the provider **pays out** the balance (minus fees) to your
bank account. Your job is to (1) collect payment details securely without touching
raw card data, (2) confirm success on your **server** via **webhooks** rather than
trusting the browser, (3) **fulfill** the order exactly once, and (4) handle
everything that can go wrong afterward — declines, refunds, disputes, fraud, and
recurring‑billing failures. Everything in this section is a detailed expansion of
that sentence.

## How this connects to the rest of the KB

- **Security** — API keys and webhook secrets are high‑value credentials; card
  data must never touch your servers. See [Security](../07-security/README.md)
  and [secrets management](../07-security/secrets-management.md).
- **Legal** — PCI, SCA, tax, refunds, and auto‑renewal rules. See
  [e‑commerce law](../10-legal-and-compliance/ecommerce-law.md) and
  [terms of service](../10-legal-and-compliance/terms-of-service.md).
- **Maintenance/ops** — payments need monitoring, reconciliation, and incident
  response like any critical system. See
  [monitoring & uptime](../09-maintenance/monitoring-and-uptime.md) and
  [incident response](../09-maintenance/incident-response.md).
- **Terminology** — payments terms are collected in the
  [glossary](../00-getting-started/glossary.md).
