# Disputes, Refunds & Fraud

The happy path — customer pays, you fulfill — is the easy part. A real payment
system has to handle what comes after and around it: **refunds** you issue,
**disputes (chargebacks)** customers initiate through their bank, and **fraud** you
must prevent. This page covers all three, plus **3D Secure / Strong Customer
Authentication**, which sits at the intersection of fraud prevention and law.

## Refunds

A **refund** returns money to the customer for a payment you already captured.

- Refunds can be **full or partial**, and you can issue them from the Dashboard or
  the API. A `charge.refunded` **webhook** lets your app react (revoke access,
  update records). See [webhooks & fulfillment](webhooks-and-fulfillment.md).
- **Processing fees are usually not returned** to you on a refund — you refund the
  customer's full amount but eat the original fee. Factor this into your policy.
- Refunds take **days** to appear on the customer's statement (bank‑dependent) —
  set expectations to reduce "where's my money?" support tickets.
- Refunding is often **cheaper and better than losing a dispute** (see below) — a
  goodwill refund avoids dispute fees and protects your dispute ratio.

> ⚖️ **Legal note:** Your **refund/returns policy** must be clearly disclosed, and
> in some places consumers have **statutory** cancellation/refund rights (e.g., the
> EU/UK **14‑day** cooling‑off for many online purchases). You must honor
> whatever policy you publish and any mandatory rights. See
> [e‑commerce law](../10-legal-and-compliance/ecommerce-law.md).

## Disputes (chargebacks)

A **dispute** — commonly a **chargeback** — happens when a cardholder asks *their
bank* to reverse a charge (claiming fraud, "item not received," "not as
described," duplicate, etc.). This is initiated **outside** your site, through the
card network, and it's adversarial.

### What happens
1. The cardholder disputes the charge with their bank.
2. The funds are **withdrawn from you**, and Stripe charges a **dispute fee**
   (often **non‑refundable even if you win**).
3. You get a `charge.dispute.created` **webhook** and a window to **submit
   evidence** (receipts, delivery/tracking, communications, your terms, proof of
   access).
4. The **issuing bank decides.** You either win (funds returned, fee usually kept
   by Stripe) or lose (funds and fee gone).

### Why disputes are dangerous
- They cost the **sale + a fee + your time**, win or lose.
- A **high dispute ratio** can lead card networks to place you in monitoring
  programs, raise your costs, or ultimately **jeopardize your ability to accept
  cards.** Keeping disputes low is a business‑survival issue, not just accounting.

### Reducing and handling disputes
> ✅ **Do:**
> - Use a **clear, recognizable billing descriptor** so customers recognize the
>   charge on their statement (unrecognized charges → "fraud" disputes).
> - Deliver good **service and communication**; make refunds and cancellation
>   easy so people don't go to their bank instead (see
>   [subscriptions](subscriptions-and-billing.md)).
> - Keep **evidence**: order records, delivery/tracking, access logs, agreed
>   terms, and customer correspondence — so you can respond to disputes.
> - **Respond promptly** to dispute events with strong evidence.
> - **Prevent fraud** up front (below) — fraudulent charges become disputes.
> - Consider a **proactive refund** when a dispute is likely and you'd lose anyway.

> ❌ **Don't:** Ignore dispute webhooks or the evidence deadline — a no‑response is
> an automatic loss.

## Fraud prevention (and Stripe Radar)

Online (card‑not‑present) payments attract fraud: stolen cards, **card testing**
(bots trying many numbers), and account takeover. Fraudulent payments hurt twice —
you can lose the goods **and** get a chargeback and fee.

- **Stripe Radar** is Stripe's fraud tool: machine‑learning risk scoring plus
  **rules** you can configure (block/allow/review based on risk, country,
  mismatch, velocity, etc.). It's built into payments (with advanced features as
  an add‑on).
- **Card testing** — attackers hammering your payment endpoint with many card
  numbers — is common; watch for spikes of tiny or failed charges and use
  Radar/rate‑limiting to blunt it. It can also run up fees. See
  [monitoring & uptime](../09-maintenance/monitoring-and-uptime.md).
- Layer other signals where appropriate: address/postal (AVS) and CVC checks,
  velocity limits, and manual review for high‑risk orders.

> ✅ **Do:** Turn on fraud protection from day one, monitor for card‑testing
> spikes, and tune rules to your risk tolerance (too strict blocks real
> customers; too loose invites fraud).
> ❌ **Don't:** Leave a raw payment/charge endpoint unprotected — bots will find
> it.

## 3D Secure & Strong Customer Authentication (SCA)

**3D Secure (3DS)** is an extra authentication step where the customer verifies a
payment with their bank (a prompt, a code, biometrics). It **shifts liability** for
fraud on authenticated transactions from you to the bank and reduces fraud.

- In the **EU/EEA and UK**, **Strong Customer Authentication (SCA)** — under
  **PSD2** — **legally requires** additional authentication (like 3DS) for many
  online card payments, with some exemptions. Non‑compliant payments get
  **declined** by the bank.
- **Stripe handles this for you** when you use PaymentIntents/Checkout/the Payment
  Element: it triggers 3D Secure when needed (the PaymentIntent enters a
  `requires_action` state and Stripe.js walks the customer through it). This is a
  major reason to use the modern PaymentIntents‑based flows rather than legacy
  charge creation. See [integrating Stripe](stripe-integration.md).

> ⚖️ **Legal + practical note:** SCA is both a **compliance requirement** (EU/UK)
> and a **fraud‑reduction/liability‑shift** benefit. Using Stripe's recommended
> integrations keeps you compliant without hand‑rolling authentication — but if
> you sell to European customers, confirm your flow actually performs SCA.

## After a payment: keep records

Everything here depends on good records — order details, fulfillment/access logs,
delivery proof, communications, and the link to the Stripe payment. They're your
evidence in disputes, your basis for refunds, and your audit trail for
[reconciliation](going-live-and-operations.md). Treat payment data as sensitive
personal data under [privacy law](../10-legal-and-compliance/gdpr.md) — keep only
what you need, secure it, and don't store card details yourself (store
[tokens](stripe-integration.md)).

## Checklist

- [ ] Clear **refund/returns policy**, honored, with mandatory consumer rights
      respected.
- [ ] **Recognizable billing descriptor** set to cut "unrecognized charge"
      disputes.
- [ ] **Dispute webhooks** handled; evidence gathered and submitted before
      deadlines.
- [ ] **Fraud protection (Radar)** enabled and tuned; **card‑testing** monitored.
- [ ] **3D Secure / SCA** performed for EU/UK customers (via Stripe's
      PaymentIntents flows).
- [ ] **Dispute ratio** monitored — kept low to protect your ability to accept
      cards.
- [ ] Payment records retained securely for evidence and reconciliation.

Finally, the operational side of running payments day to day:
[going live & operations](going-live-and-operations.md).
