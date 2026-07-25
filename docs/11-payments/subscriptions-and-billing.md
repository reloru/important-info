# Subscriptions & Billing

Recurring revenue is a different beast from one‑off payments. You're not just
charging once — you're managing an ongoing relationship with **renewals, plan
changes, failed payments, trials, and cancellations**, each with its own edge
cases and legal rules. Stripe's **Billing** product handles the machinery; this
page covers the concepts and the pitfalls, including the **consumer‑protection
rules** that make some "clever" subscription designs illegal.

> Follow [docs.stripe.com/billing](https://docs.stripe.com/billing) for exact
> APIs; this page is the durable model and the practices around it.

## The building blocks

- **Product** — the thing you sell ("Pro Plan").
- **Price** — how much and how often ("$20/month", "$200/year"). A Product can
  have several Prices (monthly/annual, currencies, tiers).
- **Customer** — the subscriber, with attached payment method(s).
- **Subscription** — links a Customer to one or more recurring Prices and drives
  billing over time.
- **Invoice** — generated each billing cycle (and for changes); Stripe attempts
  payment against the Customer's saved method.

## The subscription lifecycle (and its states)

A subscription moves through states you must handle — don't assume it's always
"active":

- **trialing** — in a free trial (if offered).
- **active** — paid and current.
- **past_due** — a renewal payment failed; Stripe is retrying (see **dunning**).
- **canceled** — ended (by the customer, you, or after failed retries).
- **unpaid / incomplete** — payment couldn't be collected/confirmed.

Your app grants or revokes access based on these states — and you learn about
transitions via **webhooks** (`customer.subscription.updated`,
`invoice.paid`, `invoice.payment_failed`, etc.). See
[webhooks & fulfillment](webhooks-and-fulfillment.md). **Entitlement should follow
the subscription state Stripe reports**, not a value you set once and forget.

## Trials

Free trials boost sign‑ups but need care:

- Decide whether to **collect a payment method up front** (higher conversion to
  paid, but more friction) or not (lower friction, more churn at conversion).
- Warn users **before** a trial converts to a paid charge — increasingly a legal
  expectation (see below).
- Handle the case where the saved card **fails at conversion.**

## Proration, upgrades, and downgrades

When a customer changes plans mid‑cycle, **proration** adjusts the charge for the
unused/extra time:

- **Upgrade mid‑cycle** — typically charge the prorated difference now (or add it
  to the next invoice).
- **Downgrade** — often credit the difference or apply the change at period end.
- Decide your policy deliberately (immediate vs. end‑of‑period changes) and make
  it clear to customers. Stripe can compute proration for you, but the **policy**
  is yours.

## Usage‑based / metered billing

For "pay for what you use" pricing (API calls, seats, GB), Stripe supports
**usage/metered billing**: you report usage and Stripe bills accordingly at the
cycle. Considerations:

- **Report usage reliably and idempotently** (don't double‑count).
- Give customers **visibility** into their usage to avoid bill shock.
- Reconcile reported usage against your own metering.

## Dunning: recovering failed payments

Cards expire, get declined, or hit limits, so **renewal payments fail routinely**.
**Dunning** is the process of recovering them:

- Stripe **retries** failed payments on a schedule (**smart retries**) and can
  email customers to update their card.
- Configure how many retries and what happens at the end (mark unpaid, cancel,
  restrict access).
- **Communicate**: prompt the customer to fix their payment method. This directly
  affects revenue — involuntary churn from failed payments is often larger than
  voluntary churn.
- React to `invoice.payment_failed` and related events in your app. See
  [webhooks & fulfillment](webhooks-and-fulfillment.md).

## The customer portal

Stripe's **Customer Portal** is a prebuilt, hosted page where subscribers can
update payment methods, change plans, view invoices, and **cancel** — without you
building any of it. Using it saves work *and* helps you meet the "easy
cancellation" requirements below.

## Handling cancellations

- Decide **cancel‑immediately vs. cancel‑at‑period‑end** (usually the latter —
  the customer keeps access through what they paid for).
- Revoke entitlements when the subscription actually ends (via the webhook), not
  the moment they click cancel (unless immediate).
- Consider a **win‑back**/feedback step — but **do not** make canceling hard (see
  legal note).

## ⚖️ The legal rules you cannot design around

Subscriptions are heavily regulated because of past abuse. These are **legal
requirements** in many places, not just good manners:

> ⚖️ **Do:**
> - **Disclose recurring terms clearly** *before* purchase — the amount,
>   frequency, and that it **auto‑renews.** See
>   [e‑commerce law](../10-legal-and-compliance/ecommerce-law.md).
> - Make **cancellation at least as easy as sign‑up** — "click‑to‑cancel" style
>   rules are spreading (US FTC, EU, and others), and burying cancellation is
>   increasingly **unlawful.** The Customer Portal helps here.
> - Send **renewal reminders / trial‑ending notices** where required (some
>   jurisdictions mandate advance notice before charging).
> - Get **explicit consent** for the recurring charge; no pre‑checked "auto‑renew"
>   traps (a [dark pattern](../02-design-and-ux/ux-principles.md)).
> - Provide clear **receipts** and an accessible billing history.

> ⚖️ **Don't:**
> - Hide the recurring nature, make cancellation a phone‑only maze, or keep
>   charging after a cancellation request.
> - Forget that **marketing emails** to subscribers still follow email law
>   (consent, unsubscribe) — see
>   [email marketing law](../10-legal-and-compliance/email-marketing-law.md).

These rules also intersect with your [terms of service](../10-legal-and-compliance/terms-of-service.md)
and [privacy policy](../10-legal-and-compliance/privacy-policy.md).

## Tax on subscriptions

Recurring charges have the same **sales tax / VAT** obligations as any sale — and
they recur, so getting tax right matters at scale. **Stripe Tax** can calculate it
per invoice, but as a processor **you're still the merchant of record** and
responsible for registering and remitting (unless you use a
[merchant of record](choosing-a-payment-provider.md)). See
[going live & operations](going-live-and-operations.md) and
[e‑commerce law](../10-legal-and-compliance/ecommerce-law.md).

## Subscriptions checklist

- [ ] Recurring price, frequency, and **auto‑renewal disclosed before purchase.**
- [ ] **Explicit consent** to recurring charges; no pre‑checked traps.
- [ ] **Cancellation is as easy as sign‑up** (Customer Portal or equivalent).
- [ ] **Trial‑ending / renewal reminders** sent where required.
- [ ] App **entitlements follow subscription state** via webhooks (active,
      past_due, canceled…).
- [ ] **Dunning** configured; failed‑payment recovery and customer prompts in
      place.
- [ ] **Proration policy** for upgrades/downgrades decided and communicated.
- [ ] **Tax** handled (Stripe Tax or MoR), and receipts/invoices provided.
- [ ] Metered usage (if any) reported **idempotently** and reconciled.

Next: the things that go wrong after a charge —
[disputes, refunds & fraud](disputes-refunds-and-fraud.md).
