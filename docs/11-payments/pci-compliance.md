# PCI Compliance

If you handle payment cards in any way, you're subject to **PCI DSS** — the
**Payment Card Industry Data Security Standard**. It sounds intimidating, but the
practical takeaway is simple and liberating: **if you never let raw card data
touch your servers, your compliance burden shrinks dramatically.** This page
explains what PCI DSS is, the scope levels, and how to stay in the easiest one.

> ⚖️🔒 Not PCI‑audit or legal advice. PCI DSS is a contractual security standard
> enforced by the card networks (via your acquirer/PSP), not a law — but
> non‑compliance can mean fines, higher fees, or losing the ability to accept
> cards, and a card‑data breach is catastrophic. Confirm your obligations with
> your provider; requirements evolve (**PCI DSS v4.0.1** is the current version,
> and v4.x's future‑dated requirements became mandatory on **31 March 2025**).

## What PCI DSS is

PCI DSS is a set of security requirements created by the major card networks
(Visa, Mastercard, Amex, Discover, JCB) for **any business that stores,
processes, or transmits cardholder data.** It covers things like network
security, encryption, access control, monitoring, and testing. Compliance is
required by your agreement with the card networks and your payment provider.

The **cardholder data** it most cares about includes the **Primary Account Number
(PAN)** — the card number itself — plus the expiry, cardholder name, and,
especially sensitive, the **CVV/security code** and full magnetic‑stripe/chip
data (which you may **never store** after authorization).

## The key insight: scope is everything

PCI's burden scales with **how much cardholder data your systems touch.** The
whole game is to **minimize scope** — ideally to *never handle raw card data at
all.* You do that by letting your payment provider's hosted, PCI‑validated
components collect the card details directly, so the sensitive data goes from the
customer's browser **straight to the provider**, bypassing your servers entirely.

> ✅ **Do:** Use your PSP's **hosted fields / hosted checkout** so raw card data
> never reaches your backend. This is the single most important PCI (and
> security) decision you'll make.
> ❌ **Don't:** Build your own card input that posts the PAN/CVV to your own
> server, log card numbers, or store CVVs. That drags you into the strictest,
> most expensive scope — and one bug becomes a breach.

## SAQ types: how you validate compliance

Smaller merchants validate compliance with a **Self‑Assessment Questionnaire
(SAQ)** — the type depends on *how you accept cards*:

| SAQ type | Applies when… | Burden |
|----------|---------------|--------|
| **SAQ A** | You **fully outsource** card handling to a PCI‑compliant third party — e.g., a hosted payment page or **hosted fields embedded via the provider's iframe/JS**. Card data never touches your systems. | **Smallest.** A short questionnaire. |
| **SAQ A‑EP** | Your site **directly affects** how card data is collected (e.g., you host the payment page but a third party processes), so your page's integrity matters more. | Larger. |
| **SAQ D** | You **store, process, or transmit** card data directly (custom card handling, storing PANs). | **Largest** — the full standard. |

*(There are other SAQ types for in‑person/terminal scenarios; the above are the
common web ones.)*

**The goal for most web businesses: qualify for SAQ A** by fully outsourcing card
capture.

### SAQ A now has a script‑security eligibility criterion

This is the part most "just use hosted fields" advice is out of date on. The SAQ A
published in **January 2025** (effective **31 March 2025**) changed what it takes
to *qualify*, not just what you attest to:

- PCI DSS Requirements **6.4.3** (managing payment‑page scripts) and **11.6.1**
  (detecting unauthorized changes to the payment page) were **removed from the
  SAQ A questionnaire itself**, along with Requirement 12.3.1's targeted risk
  analysis supporting 11.6.1.
- In their place, SAQ A added an **eligibility criterion**: the merchant confirms
  their site **is not susceptible to attacks from scripts** that could affect the
  e‑commerce system. The PCI SSC points to the techniques in 6.4.3 and 11.6.1 as
  the way to establish that — implemented by you *or* by a third party.
- Removing them from the SAQ **does not remove them from PCI DSS.** The underlying
  requirements still stand; SAQ A only changes how you report.

> 🔒 Practical effect: the page‑integrity work described under
> [remaining responsibilities](#beyond-card-capture-your-remaining-responsibilities)
> is no longer optional polish on top of SAQ A — it is part of the case that you
> belong in SAQ A at all. Script inventory, integrity checking, and a tight
> [Content Security Policy](../07-security/security-headers.md) are the evidence.

## How Stripe keeps you in SAQ A

Stripe's recommended integrations are designed precisely to keep you in the
lightest scope:

- **Stripe Checkout** (hosted or embedded) and **Stripe Elements / the Payment
  Element** use **hosted payment fields**: the card input is served from Stripe's
  own PCI‑validated infrastructure (via an iframe), so the customer's card data
  goes **directly to Stripe**, never to your server. This qualifies you for the
  simplest **SAQ A**.
- Stripe can **pre‑fill and guide your SAQ** in the Dashboard when you use these
  secure integrations, further reducing the paperwork.
- Even server‑side, you work with **tokens and IDs** (like a PaymentMethod or
  Customer ID), never the raw card number. See
  [integrating Stripe](stripe-integration.md).

> 💡 The reason "never touch the PAN" keeps recurring in this section is that it
> simultaneously (a) minimizes PCI scope, (b) removes the worst breach risk, and
> (c) is simply less code for you to write and secure. Good security and low
> compliance burden point the same way here.

## Beyond card capture: your remaining responsibilities

Using hosted fields dramatically reduces scope, but doesn't make you ignore
security entirely:

- **Serve checkout over HTTPS**, everywhere, with a valid certificate — required
  and non‑negotiable. See [HTTPS & TLS](../07-security/https-and-tls.md).
- **Protect your integrity**: keep dependencies patched and guard against script
  injection on payment pages (a tampered page could exfiltrate data before it
  reaches the iframe — the "Magecart" class of attack). A strong
  **Content Security Policy** helps. See
  [security headers](../07-security/security-headers.md) and
  [dependency management](../09-maintenance/dependency-management.md).
- **Guard your API keys and webhook secrets** — they're not card data, but
  they're high‑value credentials. See
  [secrets management](../07-security/secrets-management.md).
- **Don't store what you don't need.** If you need to charge a customer again,
  store the provider's **token/Customer ID**, never the card details yourself.
- **Maintain compliance over time** — complete your SAQ, keep integrations
  current, and re‑attest as required (often annually).

## PCI compliance checklist

- [ ] Card data is collected by the provider's **hosted fields/checkout** — it
      never hits your server (targeting **SAQ A**).
- [ ] You **never store** PANs or CVVs yourself; you store **tokens/IDs**.
- [ ] Checkout and the whole site are **HTTPS‑only** with valid certs.
- [ ] A **Content Security Policy** and patched dependencies protect page
      integrity against injected scripts — and you can **show** it, since this is
      now an SAQ A **eligibility** question, not just good practice.
- [ ] You have an **inventory of scripts** on the payment page and a way to detect
      unauthorized changes to them (PCI DSS 6.4.3 / 11.6.1). See
      [third‑party scripts](../03-development-best-practices/third-party-scripts.md).
- [ ] **API keys / webhook secrets** are stored securely (env/secret manager),
      never in the front end or version control.
- [ ] You've completed the provider‑guided **SAQ** and have a plan to re‑attest.
- [ ] Access to the payment Dashboard uses **MFA** and least privilege. See
      [authentication & authorization](../07-security/authentication-and-authorization.md).

Get PCI scope right once — by never touching raw card data — and it mostly takes
care of itself. Then move on to actually integrating Stripe:
[Stripe overview](stripe-overview.md).

## Primary sources

- [PCI SSC Document Library](https://www.pcisecuritystandards.org/document_library/)
  — the standard, the SAQs, and the attestation forms themselves.
- [Important Updates for Merchants Validating to SAQ A](https://blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a)
  — PCI SSC's own announcement of the January 2025 SAQ A changes described above.
- [Stripe: security & PCI guide](https://docs.stripe.com/security/guide) —
  provider‑specific guidance on which integrations map to which SAQ.

*Version/date‑sensitive material on this page was last verified against those
sources in **September 2026**. PCI DSS versions and SAQ eligibility change; check
the document library before relying on a date here.*
