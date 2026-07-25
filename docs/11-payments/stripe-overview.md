# Stripe Overview

Stripe is a large platform, and the breadth can be overwhelming at first. This
page gives you the lay of the land — the **products** you might use, the **core
API objects** you'll actually work with, and the operational basics (**keys,
test vs. live mode, the Dashboard**) — so the integration pages that follow make
sense.

> Stripe evolves quickly and its docs are excellent and authoritative. Treat
> **[docs.stripe.com](https://docs.stripe.com)** as the source of truth for exact
> API shapes and current recommendations; this page teaches the durable concepts.

## Stripe's product suite (what exists, and when you'd reach for it)

You don't need most of these on day one, but knowing they exist prevents you from
re‑inventing them or switching platforms later:

| Product | What it does | Reach for it when… |
|---------|--------------|--------------------|
| **Payments** (core) | One‑off payments via PaymentIntents | You need to charge a card |
| **Checkout** | Prebuilt, hosted or embedded payment page | You want a fast, secure, low‑maintenance checkout |
| **Payment Links** | Shareable no‑code payment URLs | You want to get paid with zero integration |
| **Elements / Payment Element** | UI components to build a custom checkout | You need checkout on your own page/design |
| **Billing** | Subscriptions, invoicing, recurring revenue | You sell subscriptions or recurring plans |
| **Invoicing** | Send hosted invoices | You bill customers directly |
| **Connect** | Pay out to third parties (marketplaces/platforms) | You run a marketplace or platform paying sellers |
| **Radar** | Fraud detection and rules | You need fraud protection (often on by default) |
| **Tax** | Automatic sales tax / VAT calculation | You must calculate tax at checkout |
| **Terminal** | In‑person card payments | You take payments at a physical point of sale |
| **Financial Connections** | Link customer bank accounts | You need bank data / bank payments |
| **Radar/Sigma/Reporting** | Analytics and SQL over your data | You need custom reporting |
| **Issuing** | Create/manage your own cards | You issue cards (advanced) |

For most websites, the core is **Payments + Checkout (or the Payment Element)**,
plus **Billing** if you do subscriptions, **Tax** if you owe tax, and **Radar**
for fraud. The rest you add as needed.

## Core API objects (the vocabulary you'll live in)

These are the objects you'll create and react to. Understanding them is more
important than memorizing API calls.

- **PaymentIntent** — represents the intent to collect a payment and **tracks its
  lifecycle** through authentication, authorization, and capture. The modern
  foundation of a Stripe payment. It handles required steps like 3D Secure
  automatically. (See [integrating Stripe](stripe-integration.md).)
- **SetupIntent** — like a PaymentIntent but for **saving a payment method for
  later** without charging now (e.g., to set up a subscription or file‑on‑card).
- **PaymentMethod** — a customer's specific way to pay (a card, a wallet, a bank
  account), represented as a **token** — never the raw card number.
- **Customer** — a saved record of a buyer, to which you can attach payment
  methods, subscriptions, and invoices for repeat business.
- **Charge** — a record of a completed charge (older‑style; PaymentIntents
  supersede direct charge creation but Charges still appear in the data model).
- **Product** and **Price** — what you sell and how much/how often it costs
  (Prices can be one‑time or recurring). Used by Checkout and Billing.
- **Subscription** — a recurring billing relationship between a Customer and one
  or more Prices. (See [subscriptions & billing](subscriptions-and-billing.md).)
- **Invoice** — an itemized bill, generated for subscriptions or sent manually.
- **Checkout Session** — represents one visit to a Stripe Checkout page; you
  create it server‑side and redirect/embed it. (See
  [integrating Stripe](stripe-integration.md).)
- **Refund** — reverses a payment, fully or partially. (See
  [disputes, refunds & fraud](disputes-refunds-and-fraud.md).)
- **Dispute** — a chargeback initiated by the cardholder's bank.
- **Event** — an object describing something that happened in your account,
  delivered to you via **webhooks**. The backbone of reliable integrations. (See
  [webhooks & fulfillment](webhooks-and-fulfillment.md).)
- **Balance** and **Payout** — your available funds and their transfer to your
  bank. (See [going live & operations](going-live-and-operations.md).)

> 💡 **A mental model:** you describe *what you want* (a PaymentIntent, a
> Checkout Session, a Subscription); Stripe drives it through the messy real‑world
> steps (authentication, retries, bank responses); and it tells you *what
> happened* by emitting **Events** to your webhook. Your backend's job is mostly
> **creating intents** and **reacting to events**.

## Keys, test mode, and live mode

- **API keys** authenticate your requests. Each account has:
  - A **publishable key** (safe to expose in the browser; used by Stripe.js to
    tokenize card data client‑side).
  - A **secret key** (server‑only; can do anything on your account). 🔒 **Never**
    expose the secret key in front‑end code, commit it to version control, or
    log it. Store it in an env var / secret manager. See
    [secrets management](../07-security/secrets-management.md).
  - A **webhook signing secret** (per endpoint; used to verify events are really
    from Stripe). See [webhooks & fulfillment](webhooks-and-fulfillment.md).
- **Test mode vs. live mode** — Stripe gives you **separate keys and data** for
  testing and production. In **test mode** you use test cards and no real money
  moves; in **live mode** everything is real. They're effectively parallel
  worlds — objects created in test don't exist in live. **Do all development and
  automated testing in test mode.** See
  [going live & operations](going-live-and-operations.md) and
  [environments](../08-deployment-and-devops/environments.md).
- **Restricted keys** — you can create keys scoped to only certain permissions;
  use them to apply **least privilege** for specific services. See
  [authentication & authorization](../07-security/authentication-and-authorization.md).

> ✅ **Do:** Keep test and live keys in **separate environment configuration**,
> matching your dev/staging/production
> [environments](../08-deployment-and-devops/environments.md). A live secret key
> in the wrong place is a serious incident.

## The Stripe Dashboard

The **Dashboard** is Stripe's web UI, and much more than a settings page — it's an
operational tool you'll use daily:

- View payments, customers, subscriptions, disputes, and payouts.
- Issue **refunds** and respond to **disputes**.
- Configure products/prices, **webhooks**, tax, Radar rules, and branding.
- Complete your **PCI SAQ** and account/identity verification.
- Toggle between **test and live** data.

> 🔒 The Dashboard controls real money and sensitive data — protect it with
> **MFA** and **least‑privilege team roles**, and remove access promptly when
> people leave. See [authentication & authorization](../07-security/authentication-and-authorization.md).

## The Stripe CLI (for developers)

The **Stripe CLI** is a command‑line tool for development: it can trigger test
events, **forward webhooks to your local machine**, tail logs, and make test API
calls. It's invaluable for building and testing webhook handlers locally — see
[webhooks & fulfillment](webhooks-and-fulfillment.md) and
[going live & operations](going-live-and-operations.md).

With the map in hand, continue to the practical
[integration patterns](stripe-integration.md).
