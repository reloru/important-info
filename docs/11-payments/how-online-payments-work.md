# How Online Payments Work

Before integrating any payment provider, you need a mental model of what actually
happens when someone types their card number and clicks "Pay." It's more involved
than it looks — several institutions coordinate in seconds — and understanding it
explains *why* the tools and rules in the rest of this section exist. This page
assumes no prior knowledge.

## The players

A single card payment involves a surprising cast:

- **Cardholder** — your customer, paying with a card (or wallet, or bank).
- **Merchant** — you, the business getting paid.
- **Payment gateway** — the software that securely captures payment details and
  passes them to be processed. (Modern platforms like Stripe bundle this in.)
- **Payment processor** — moves the transaction data between the parties and the
  card networks.
- **Acquirer (acquiring bank / merchant bank)** — the bank that holds the
  merchant's account and receives the funds. (Stripe abstracts this away for you.)
- **Card networks (schemes)** — Visa, Mastercard, American Express, etc. They run
  the rails, set rules, and route transactions between banks.
- **Issuer (issuing bank)** — the customer's bank that issued their card and
  ultimately approves or declines the payment and bills the customer.

> 💡 **What a modern PSP hides for you.** A **Payment Service Provider (PSP)** like
> Stripe or PayPal rolls the gateway, processing, and acquiring relationship into
> one product. Instead of separately contracting a gateway, a processor, and a
> merchant account (the old, painful way), you sign up once and it handles the
> chain. That convenience is a big part of why platforms like Stripe dominate. See
> [choosing a payment provider](choosing-a-payment-provider.md).

## The money flow: authorization → capture → settlement → payout

This is the single most important sequence to understand. These are **distinct
steps**, and conflating them causes real bugs.

### 1. Authorization
When the customer pays, the request travels from the gateway → processor → card
network → **issuing bank**, which checks the card is valid and has funds/credit,
runs fraud and authentication checks (see
[SCA/3D Secure](disputes-refunds-and-fraud.md)), and returns an **approve** or
**decline**. On approval, the amount is typically **held** (reserved) on the
customer's card but **not yet moved**.

### 2. Capture
**Capture** is the instruction to actually collect the authorized amount. Two
common patterns:

- **Auto‑capture (immediate)** — authorize and capture in one step. Right for
  most e‑commerce where you charge at purchase.
- **Manual/delayed capture** — authorize now, capture later (e.g., capture only
  when you ship, or capture a final amount for a hotel/rental). Authorizations
  **expire** if not captured within a window (often ~7 days for cards), so you
  can't hold indefinitely.

> A payment can be **authorized but never captured** (you let the hold expire or
> cancel it) — no money moves. This is why "authorized" ≠ "paid."

### 3. Settlement (clearing)
Behind the scenes, the card networks and banks **settle** the captured
transactions — the actual transfer of funds between the issuing and acquiring
banks — usually in batches over the following days. This is why money isn't
instantly in your bank even after a "successful" payment.

### 4. Payout
Your PSP accumulates your settled funds as a **balance** and **pays out** to your
bank account on a schedule (e.g., daily or every few days, often on a rolling
delay), **minus fees** and minus any amounts held back for risk. See
[going live & operations](going-live-and-operations.md) for payouts and
reconciliation.

```
Customer pays
   │
   ▼
AUTHORIZE ──(approve/decline by issuer)──▶ funds held on card
   │
   ▼
CAPTURE ────────────────────────────────▶ collection instructed
   │
   ▼
SETTLEMENT ─(networks + banks, over days)─▶ funds transferred to acquirer
   │
   ▼
PAYOUT ──(PSP → your bank, minus fees)───▶ money in your account
```

## Fees: what you actually pay

Card payments are not free, and the fee structure has layers:

- **Interchange** — set by the card networks, paid to the *issuing* bank. Varies
  by card type (rewards/corporate cards cost more), region, and whether the card
  is present.
- **Scheme/network fees** — the networks' own cut.
- **Processor/PSP markup** — your provider's margin on top.

Most developer PSPs simplify this into **blended pricing** — one flat rate
regardless of the underlying card — while larger merchants may use
**interchange‑plus (IC+)**, which passes through the true interchange plus a fixed
markup (often cheaper at scale, but more complex).

> 💡 **Rule of thumb for Stripe's standard online card pricing:** commonly around
> **2.9% + a small fixed fee (e.g. 30¢) per successful card charge** in the US,
> with **no monthly or setup fee** — but rates vary by country, card, and payment
> method, and change over time. **Always check the provider's current pricing
> page.** Extra fees may apply for currency conversion, certain payment methods,
> chargebacks, and add‑on products (Tax, Billing, Radar, etc.).

Failed payments generally aren't charged, but **refunds usually don't return the
original processing fee**, and **disputes/chargebacks carry their own fee** — see
[disputes, refunds & fraud](disputes-refunds-and-fraud.md).

## Payment methods beyond cards

"Payments" is broader than credit cards, and offering the methods your customers
prefer directly lifts conversion:

- **Credit/debit cards** — the baseline, globally.
- **Digital wallets** — Apple Pay, Google Pay, etc. Fast, secure (tokenized),
  and boost mobile conversion; usually easy to enable through a PSP.
- **Bank debits / transfers** — ACH (US), SEPA (EU), iDEAL, Bacs, etc. Lower fees
  but often slower and with different failure/refund behavior.
- **"Buy now, pay later" (BNPL)** — Klarna, Afterpay/Clearpay, Affirm.
- **Regional methods** — hugely important for international sales (e.g., iDEAL in
  the Netherlands, Bancontact in Belgium, Alipay/WeChat Pay in China, Pix in
  Brazil). Missing the locally dominant method can mean missing the market.

> 💡 Modern PSPs let you enable many methods with little extra work (Stripe's
> Payment Element can show the relevant methods per customer automatically — see
> [integrating Stripe](stripe-integration.md)). Each method, though, has its own
> settlement timing, fees, dispute rules, and refund behavior — don't assume all
> methods behave like cards.

## Card‑present vs. card‑not‑present

- **Card‑not‑present (CNP)** — online/e‑commerce, where the card isn't physically
  present. Higher fraud risk, so authentication (like 3D Secure) and fraud tools
  matter more.
- **Card‑present** — in person, via a physical terminal (e.g., Stripe Terminal).
  Lower fraud risk and different fee/PCI handling.

This section focuses on **card‑not‑present** web payments.

## Why this matters for your build

Every design decision downstream follows from this model:

- Because card data flows to the **processor, not your server**, you use hosted
  fields to stay out of PCI scope. See [PCI compliance](pci-compliance.md).
- Because **authorization, capture, and settlement are separate and asynchronous**,
  you confirm real success on your **server via webhooks**, not from the browser.
  See [webhooks & fulfillment](webhooks-and-fulfillment.md).
- Because **payouts lag and fees apply**, you need **reconciliation** and clear
  accounting. See [going live & operations](going-live-and-operations.md).
- Because **things go wrong after payment** (declines, refunds, disputes), you
  build for the unhappy paths from the start. See
  [disputes, refunds & fraud](disputes-refunds-and-fraud.md).

With this model in hand, the rest of the section is about doing each step well.
