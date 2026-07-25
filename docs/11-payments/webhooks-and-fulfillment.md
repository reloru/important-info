# Webhooks & Fulfillment

This is the most important page in the section for **correctness**. Payments are
**asynchronous** — the real outcome often arrives *after* the customer leaves the
page, and some outcomes (a dispute, a failed subscription renewal, a delayed bank
payment) happen days later with no browser involved at all. **Webhooks** are how
Stripe tells your server what actually happened, and treating them as the **source
of truth** is what separates a reliable payment integration from a broken one.

## What webhooks are and why they're the source of truth

A **webhook** is an HTTP request Stripe sends to a URL on your server whenever
something happens in your account — a payment succeeded, a subscription renewed, a
dispute opened. Each carries an **Event** object describing what occurred.

Why you must rely on them rather than the browser:

- The customer might **close the tab** after paying but before any redirect
  completes. The payment still succeeded — your server needs to know.
- Client‑side success signals can be **spoofed, dropped, or interrupted**; you
  can't fulfill on trust. (See [never trust the client](stripe-integration.md).)
- Many events (**disputes, refunds, subscription renewals, delayed payment
  methods**) have **no browser context at all** — a webhook is the *only* way you
  hear about them.

> ✅ **The rule:** Confirm payments and drive fulfillment from **webhooks on your
> server**, not from client‑side redirects or callbacks. Use the browser result
> only for immediate UX ("thanks, we're processing your order").

## Verify every webhook's signature

Your webhook endpoint is a public URL — anyone could POST fake "payment
succeeded" events to it. So you **must verify** that each event genuinely came from
Stripe and wasn't tampered with.

Stripe signs every webhook with a **signing secret** (unique per endpoint). Your
handler must:

1. Read the raw request body and the `Stripe-Signature` header.
2. Use Stripe's library (with your endpoint's **signing secret**) to **verify the
   signature** before doing anything else.
3. Reject anything that fails verification.

> 🔒 **Do:**
> - **Verify the signature on every event** using the endpoint's signing secret.
> - Verify against the **raw, unparsed request body** (parsing/re‑serializing can
>   break signature checks).
> - Store the **signing secret** as a secret, like any credential. See
>   [secrets management](../07-security/secrets-management.md).
> ❌ **Don't:** Act on webhook data before verifying it, or expose an
> "process this order" endpoint that trusts unauthenticated input.

## Handle events idempotently (they can arrive more than once)

Stripe guarantees **at‑least‑once** delivery: to be reliable it may send the
**same event more than once**, and events can arrive **out of order**. If you
naively fulfill on every delivery, a customer could get **shipped twice** or
**credited twice**.

> ✅ **Make webhook handling idempotent:**
> - Every Event has a unique **`id`**. **Record processed event IDs** and **skip
>   duplicates** (e.g., an `INSERT ... ON CONFLICT DO NOTHING`, or a
>   processed‑events table checked before acting).
> - Make the fulfillment action itself idempotent — e.g., key the order by the
>   PaymentIntent/Checkout Session ID so "create order" is a no‑op if it already
>   exists.
> - Don't assume order of arrival; design so an out‑of‑order or repeated event is
>   harmless.

This mirrors the [idempotency](stripe-integration.md) you use on outbound
requests — both directions must tolerate retries.

## Respond fast, do work asynchronously

Stripe expects a **quick `2xx` response** to acknowledge receipt; if your endpoint
is slow or errors, Stripe **retries** the event (with backoff) — which is good for
resilience but bad if your slow synchronous work causes timeouts and duplicate
processing.

> ✅ **Do:** Acknowledge quickly (return `2xx`), and do heavy fulfillment work
> **asynchronously** (a queue/background job) keyed idempotently. Return a non‑2xx
> only when you genuinely want Stripe to **retry later** (e.g., a transient
> downstream failure).

## The events that matter (a starting map)

You subscribe only to the events you need. Common ones:

| Event | Meaning / typical action |
|-------|--------------------------|
| `checkout.session.completed` | A Checkout payment finished → **fulfill the order** |
| `payment_intent.succeeded` | A payment succeeded → fulfill / mark paid |
| `payment_intent.payment_failed` | A payment failed → notify / let them retry |
| `charge.refunded` | A refund was issued → update records/access |
| `charge.dispute.created` | A **chargeback** opened → gather evidence, maybe pause access ([disputes](disputes-refunds-and-fraud.md)) |
| `invoice.paid` | A subscription invoice was paid → extend access |
| `invoice.payment_failed` | Renewal failed → **dunning**/retry, warn customer ([subscriptions](subscriptions-and-billing.md)) |
| `customer.subscription.updated` / `.deleted` | Plan changed / canceled → adjust entitlements |

> 💡 For **Checkout**, `checkout.session.completed` is usually your main
> fulfillment trigger. For custom Payment Element flows,
> `payment_intent.succeeded` is. Pick one clear, idempotent fulfillment point per
> flow so you never fulfill twice.

## Fulfillment: do it exactly once

"Fulfillment" is whatever the customer paid for: ship the goods, grant access,
send the license/download, extend the subscription, send a receipt. The
requirements:

- **Trigger from the verified webhook**, not the browser.
- **Exactly once** — idempotent, so duplicate/replayed events don't double‑fulfill.
- **Verify the details server‑side** — confirm the amount, currency, and status
  match what you expect before granting value.
- **Record everything** — store the payment/session IDs against your order for
  [reconciliation](going-live-and-operations.md) and support.
- **Fail safe** — if fulfillment can't complete (inventory gone, downstream
  down), don't silently drop it: retry, alert, and reconcile.

## Reconciliation: your records vs. Stripe's

Your database and Stripe's should always agree on what was paid and fulfilled.
Drift happens (a missed webhook, a manual Dashboard refund, a bug), so
**reconcile**:

- Periodically compare your orders against Stripe's payments/payouts.
- Investigate mismatches (paid‑but‑not‑fulfilled is urgent; fulfilled‑but‑not‑paid
  is a leak).
- Keep an auditable link between each order and its Stripe objects.

More on this in [going live & operations](going-live-and-operations.md).

## Test webhooks before you trust them

Webhooks are easy to get subtly wrong, so test them explicitly:

- Use the **Stripe CLI** to forward events to your local server
  (`stripe listen --forward-to localhost:.../webhook`) and to **trigger** test
  events (`stripe trigger payment_intent.succeeded`).
- Test the **duplicate‑delivery** and **out‑of‑order** cases, not just the happy
  path.
- The Dashboard shows webhook **delivery attempts and failures** — monitor them.
  See [monitoring & uptime](../09-maintenance/monitoring-and-uptime.md).

## Reliability checklist

- [ ] Fulfillment is driven by **verified webhooks**, never the browser.
- [ ] Every event's **signature is verified** against the endpoint secret.
- [ ] Handling is **idempotent** (dedupe by event ID; fulfillment keyed to
      payment/session).
- [ ] Endpoint **responds `2xx` fast**; heavy work runs async and safe to retry.
- [ ] You handle **failure and dispute** events, not just success.
- [ ] **Reconciliation** catches drift between your records and Stripe.
- [ ] Webhook **delivery failures are monitored** and alert someone.
- [ ] Webhooks were **tested** (incl. duplicates/out‑of‑order) with the Stripe CLI.

Get webhooks right and your payments are trustworthy. Get them wrong and you'll
have phantom orders, double shipments, and angry customers. This is where to spend
your care.
