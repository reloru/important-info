# Integrating Stripe

This is the practical "how do I actually take a payment" page. Stripe offers
several integration approaches along a spectrum from **no code** to **fully
custom**, and picking the right one saves enormous effort. Then there are a few
principles — the **PaymentIntent lifecycle**, **idempotency**, and **never trust
the client** — that apply no matter which approach you choose.

> Exact code differs by language/SDK and changes over time; follow
> [docs.stripe.com](https://docs.stripe.com) for current snippets. This page
> teaches the architecture and the decisions.

## The integration options (least to most custom)

### 1. Payment Links — no code
Stripe generates a **shareable URL** (or QR) for a product/price. You create it in
the Dashboard or via API, share it, and Stripe hosts the entire checkout. **Zero
integration.**

- ✅ Fastest possible way to get paid; great for a single product, a donation, an
  invoice, a quick sale.
- ❌ Little control over flow; not suited to a dynamic cart or bespoke UX.

### 2. Stripe Checkout — prebuilt, hosted or embedded
Stripe hosts a **prebuilt, optimized payment page** (redirect to Stripe, or embed
it in your site). You create a **Checkout Session** on your server describing what
you're selling, and Stripe handles the payment UI, payment‑method selection, 3D
Secure, and more.

- ✅ Secure by default (**SAQ A** — see [PCI compliance](pci-compliance.md)),
  low‑maintenance, supports many payment methods, tax, discounts, shipping, and
  subscriptions with little code. **Stripe recommends the Checkout Sessions API
  for most integrations.**
- ❌ Less pixel‑level control than building your own (though it's customizable and
  can be embedded).
- **Best default for most sites.**

### 3. The Payment Element — custom checkout on your page
The **Payment Element** is a prebuilt, embeddable UI component (part of Stripe
**Elements**) that renders card and other payment‑method inputs — using **hosted
fields** — directly in your own page and design. Stripe now recommends building
with the **Payment Element together with the Checkout Sessions API** for custom
checkouts, which keeps much of Checkout's built‑in power while letting you control
the UI.

- ✅ Your look and flow; still **SAQ A** (card data goes straight to Stripe via
  the element's hosted fields); one element renders many payment methods and can
  show the right ones per customer automatically.
- ❌ More to build and maintain than hosted Checkout.
- **Choose when you need checkout on your own page/brand.**

### 4. The Payment Intents API directly — lowest level
You can drive the **Payment Intents API** yourself for fully bespoke flows. It's
the most flexible and the **most code and maintenance** — only reach for it when
the higher‑level options genuinely can't do what you need.

> ✅ **Do:** Start at the **highest level that meets your needs** — Payment Links
> or Checkout for most, the Payment Element when you need custom UI, the raw API
> only when you must.
> ❌ **Don't:** Hand‑roll a low‑level integration for a use case Checkout already
> solves — you'll re‑implement (and under‑test) authentication, payment methods,
> and edge cases Stripe handles for you.

## The PaymentIntent lifecycle (the heart of it)

Whatever the UI, a card payment is ultimately tracked by a **PaymentIntent** that
moves through states. Understanding this prevents a whole class of bugs.

```
create PaymentIntent (server, with amount + currency)
        │
        ▼
requires_payment_method ──▶ requires_confirmation ──▶ requires_action (e.g. 3D Secure)
        │                                                     │
        └───────────────────────────┬─────────────────────────┘
                                     ▼
                               processing
                                     │
                                     ▼
                     succeeded   OR   requires_payment_method (failed → retry)
```

The essential flow:

1. **Server** creates a PaymentIntent with the **amount and currency** (and
   options). This returns a **client secret**.
2. **Client** uses Stripe.js + the client secret to collect payment details and
   **confirm** the payment — Stripe handles any required **authentication (3D
   Secure/SCA)** inline. See [SCA/3D Secure](disputes-refunds-and-fraud.md).
3. The PaymentIntent ends in **`succeeded`** (or fails and can be retried with a
   new payment method).
4. Your **server** learns the true outcome via a **webhook**
   (`payment_intent.succeeded`), and only *then* fulfills the order. (Checkout
   wraps most of steps 1–3 for you and emits `checkout.session.completed`.) See
   [webhooks & fulfillment](webhooks-and-fulfillment.md).

> 💡 **Amounts are in the smallest currency unit.** Stripe expects integer minor
> units — **$10.00 is `1000`** (cents), ¥1000 is `1000` (yen has no minor unit).
> Getting this wrong means charging 100× too much or too little. Always compute
> amounts on the **server** from trusted data.

## The golden rule: never trust the client

The browser is controlled by the user (and potentially an attacker). **Never let
the client decide what happens on your server.**

> ❌ **Don't:**
> - Trust a **price or amount sent from the browser** — an attacker can change it.
>   Compute the charge **server‑side** from your own product/price data (or use
>   Checkout with server‑created line items).
> - Treat a **client‑side "success"** (a redirect, a JS callback) as proof of
>   payment and fulfill on that basis. Redirects can be spoofed, dropped, or
>   interrupted.
> - Expose your **secret key** to the browser (only the publishable key belongs
>   client‑side). See [secrets management](../07-security/secrets-management.md).

> ✅ **Do:**
> - Create PaymentIntents/Checkout Sessions on the **server** with amounts you
>   control.
> - Confirm real success **server‑side via webhooks**, and fulfill from there.
> - Re‑verify the amount/status server‑side before granting anything of value.

This single principle prevents the most common and damaging payment bugs.

## Idempotency: safe retries

Networks fail and users double‑click. If a "create charge" request times out, did
it succeed? Retrying blindly could **charge twice.** Stripe solves this with
**idempotency keys**: attach a unique key to a request, and if it's retried with
the same key, Stripe returns the **original result** instead of performing the
action again.

> ✅ **Do:** Send an **idempotency key** on payment‑creating requests (e.g., a
> UUID per checkout attempt) so retries are safe. Also make your **webhook
> handling idempotent** (the same event can arrive more than once) — see
> [webhooks & fulfillment](webhooks-and-fulfillment.md).

## Saving cards for later & repeat customers

To charge a returning customer or set up a subscription, save the payment method
to a **Customer** (via a PaymentIntent with the right setup, or a **SetupIntent**
if you're not charging now). You then reference the stored **PaymentMethod token**
— never the raw card. See [subscriptions & billing](subscriptions-and-billing.md).

## A practical starter recipe (most sites)

1. Model your catalog as **Products/Prices** (in Stripe or your own DB).
2. On "checkout," your **server** creates a **Checkout Session** (or a
   PaymentIntent + Payment Element) with the correct **amounts computed
   server‑side** and an **idempotency key**.
3. The customer pays via Stripe's hosted fields (**SAQ A**).
4. Your **webhook** receives `checkout.session.completed` /
   `payment_intent.succeeded`, you **verify and fulfill exactly once**, and record
   the order.
5. Handle the unhappy paths — declines, retries, refunds, disputes — per the rest
   of this section.

Next, the page that makes all of this *reliable*:
[webhooks & fulfillment](webhooks-and-fulfillment.md).
