# Payments Go‑Live Checklist

A copy‑ready gate for launching payments (Stripe‑oriented, but most items apply to
any provider). Paste it into an issue and check items off before you take **real**
money. It expands the inline checklist in
[going live & operations](../11-payments/going-live-and-operations.md); for the
reasoning behind each item, follow the links into the
[Payments section](../11-payments/README.md).

> ⚖️🔒 Not legal, PCI‑audit, or financial advice. Payments touch security, law,
> and money at once — confirm specifics against your provider's current docs and,
> where liability is real, a professional. Adapt to your business (one‑off sales,
> subscriptions, marketplace, etc.) and delete what doesn't apply.

## 0. Decisions made before building
- [ ] **Provider chosen deliberately** — processor (you own tax) vs. **merchant of
      record** (they own tax). See
      [choosing a payment provider](../11-payments/choosing-a-payment-provider.md).
- [ ] **Integration approach chosen** — Payment Links (no‑code) / Checkout / Payment
      Element — at the highest level that meets your needs. See
      [integrating Stripe](../11-payments/stripe-integration.md).
- [ ] **Payment methods** to offer decided (cards, wallets, regional methods) for
      your audience/markets.

## 1. Account & keys
- [ ] Business **activated/verified** (KYC complete); **payout bank account**
      confirmed. (Start early — verification takes time.)
- [ ] **Live** API keys in production config; **test** keys in dev/staging —
      separated per [environment](../08-deployment-and-devops/environments.md).
- [ ] **Secret key** and **webhook signing secret** stored in env/secret manager —
      **never** in front‑end code or version control. See
      [secrets management](../07-security/secrets-management.md).
- [ ] **Restricted keys** used for scoped services (least privilege).
- [ ] Dashboard access uses **MFA** and least‑privilege roles; offboarding removes
      access. See [authentication & authorization](../07-security/authentication-and-authorization.md).

## 2. Security & PCI
- [ ] Card data collected only via the provider's **hosted fields/checkout** — it
      **never touches your server** (targeting **SAQ A**). See
      [PCI compliance](../11-payments/pci-compliance.md).
- [ ] You **never store** raw card numbers/CVVs; you store **tokens/IDs**.
- [ ] Checkout and the whole site are **HTTPS‑only** with valid certs. See
      [HTTPS & TLS](../07-security/https-and-tls.md).
- [ ] A **Content Security Policy** + patched dependencies protect payment pages
      from injected/skimming scripts. See
      [security headers](../07-security/security-headers.md).
- [ ] Provider‑guided **PCI SAQ** completed; plan to re‑attest.

## 3. Payment flow correctness
- [ ] **Amounts computed server‑side** from trusted data (never trust a
      browser‑supplied price), in the correct **minor units** (e.g. cents). See
      [integrating Stripe](../11-payments/stripe-integration.md).
- [ ] **Idempotency keys** on payment‑creating requests (safe retries).
- [ ] Success is confirmed **server‑side**, not from a client redirect/callback.

## 4. Webhooks & fulfillment
- [ ] **Live webhook endpoint** configured, reachable over HTTPS, and subscribed to
      the events you need. See [webhooks & fulfillment](../11-payments/webhooks-and-fulfillment.md).
- [ ] Every event's **signature is verified** against the endpoint secret (using the
      raw body).
- [ ] Handling is **idempotent** (dedupe by event ID; fulfillment keyed to the
      payment/session) — safe against duplicate & out‑of‑order delivery.
- [ ] Endpoint **responds 2xx fast**; heavy fulfillment runs async.
- [ ] **Fulfillment happens exactly once** from the verified webhook, with details
      re‑verified (amount/currency/status) before granting value.
- [ ] **Failure & dispute** events handled, not just success.

## 5. Subscriptions & billing (if applicable)
- [ ] App **entitlements follow subscription state** (active/past_due/canceled) via
      webhooks. See [subscriptions & billing](../11-payments/subscriptions-and-billing.md).
- [ ] **Dunning** (failed‑payment retries + customer prompts) configured.
- [ ] **Recurring terms & auto‑renewal disclosed before purchase**; explicit
      consent; **cancellation as easy as sign‑up** (e.g., Customer Portal).
- [ ] **Trial‑ending / renewal reminders** sent where required. ⚖️ See
      [e‑commerce law](../10-legal-and-compliance/ecommerce-law.md).
- [ ] Proration policy for upgrades/downgrades decided; metered usage (if any)
      reported idempotently.

## 6. Fraud, disputes & authentication
- [ ] **Fraud protection (Radar or equivalent)** enabled and tuned; **card‑testing**
      monitored. See [disputes, refunds & fraud](../11-payments/disputes-refunds-and-fraud.md).
- [ ] **3D Secure / SCA** performed for EU/UK customers (via PaymentIntents flows).
- [ ] Clear, **recognizable billing descriptor** set (cuts "unrecognized charge"
      disputes).
- [ ] **Dispute** evidence sources (orders, delivery, access logs, terms) captured;
      dispute webhooks handled before deadlines.
- [ ] **Refund** flow implemented; refund/returns policy honored (incl. mandatory
      consumer rights, e.g. EU/UK 14‑day). ⚖️

## 7. Tax, receipts & policies
- [ ] **Tax** handled — Stripe Tax (you register/remit) or a merchant of record.
      ⚖️ See [e‑commerce law: tax](../10-legal-and-compliance/ecommerce-law.md).
- [ ] **All‑in pricing** shown before commitment (taxes + fees); payment‑obligation
      button clearly labeled; no dark patterns at checkout.
- [ ] **Receipts** sent; **refund policy, terms, and privacy policy** in place and
      linked. See [terms of service](../10-legal-and-compliance/terms-of-service.md).

## 8. Testing
- [ ] Full flow tested in **test mode** with **test cards** — incl. declines,
      3D Secure, refunds, disputes, duplicate/out‑of‑order webhooks, and (if used)
      subscription renewal failure. See [testing](../03-development-best-practices/testing.md).
- [ ] Webhooks tested locally with the **Stripe CLI** (`stripe listen`,
      `stripe trigger`).
- [ ] Server payment logic covered by automated tests in
      [CI](../08-deployment-and-devops/ci-cd.md).

## 9. Launch & post‑launch ops
- [ ] Final **live smoke test**: a small real transaction, then refund it.
- [ ] **Monitoring & alerts** on payment success/decline rates, webhook delivery
      failures, fraud/card‑testing spikes, dispute ratio, and payout failures. See
      [monitoring & uptime](../09-maintenance/monitoring-and-uptime.md).
- [ ] **Reconciliation** process (your DB ↔ provider ↔ bank) scheduled; mismatches
      treated as incidents. See [incident response](../09-maintenance/incident-response.md).
- [ ] Payments folded into the [maintenance plan](../09-maintenance/maintenance-plan.md):
      keep SDKs/API version current, rotate keys if exposed, review access, watch
      expiring cards, re‑attest PCI, revisit tax registrations as you grow.

---

> This is a payments‑specific gate; run it **alongside** the broad
> [pre‑launch checklist](pre-launch-checklist.md), which covers the rest of the
> site.
