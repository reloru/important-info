# Going Live & Operations

Building a payment flow is only half the job; **running it** is the other half.
This page covers testing your integration thoroughly, the go‑live checklist, and
the ongoing operational realities — **payouts, reconciliation, reporting, tax, and
monitoring** — that keep a payment system trustworthy after launch. Payments are a
critical system and deserve the same operational discipline as the rest of
[maintenance & operations](../09-maintenance/README.md).

## Test thoroughly in test mode first

Stripe's **test mode** is a full parallel environment (separate keys and data)
where **no real money moves.** Do all development and automated testing there.

- **Test cards** — Stripe provides card numbers that simulate specific outcomes:
  success, decline, insufficient funds, `requires_action` (3D Secure), disputes,
  and more. Test the **failure paths**, not just success.
- **The Stripe CLI** — forward webhooks to your local server
  (`stripe listen --forward-to localhost:…/webhook`) and **trigger** events
  (`stripe trigger payment_intent.succeeded`) so you can build and test handlers
  locally. See [webhooks & fulfillment](webhooks-and-fulfillment.md).
- **Test the unhappy paths explicitly**: declines and retries, 3D Secure prompts,
  refunds, disputes, duplicate/out‑of‑order webhooks, subscription renewal
  failures (dunning), and cancellation. These are where real bugs hide. See
  [testing](../03-development-best-practices/testing.md).
- Map test/live keys to your **dev/staging/production**
  [environments](../08-deployment-and-devops/environments.md) so you never cross
  streams.

> ✅ **Do:** Treat the payment flow like any other critical feature — automated
> tests around your server logic and webhook handling, run in
> [CI](../08-deployment-and-devops/ci-cd.md).

## Activating your account (going live)

Before live mode works, Stripe must **verify your business** — identity,
bank/payout details, and business information (a **KYC**, "know your customer,"
requirement that payment providers are legally obligated to perform).

> 💡 Start account activation **early** — verification can take time, and you
> can't receive payouts until it's done. Keep your business and bank details
> accurate; mismatches delay payouts.

## Go‑live checklist

*(A fuller, copy‑ready version is the
[payments go‑live checklist template](../templates/payments-go-live-checklist.md) —
paste it into a ticket.)*

- [ ] Business **activated/verified**; payout bank account confirmed.
- [ ] **Live API keys** in production config; **test keys** in dev/staging —
      separated per [environment](../08-deployment-and-devops/environments.md).
- [ ] **Secret key & webhook signing secret** stored in a secret manager, **never**
      in the front end or version control. See
      [secrets management](../07-security/secrets-management.md).
- [ ] **Live webhook endpoint** configured, signature‑verified, and reachable over
      HTTPS; delivery monitored. See [webhooks](webhooks-and-fulfillment.md).
- [ ] Checkout and site are **HTTPS‑only**; payment pages use **hosted fields**
      (**SAQ A**) with a protective **CSP**. See [PCI compliance](pci-compliance.md).
- [ ] **Amounts computed server‑side**; **idempotency keys** on payment creation.
- [ ] **Fraud protection (Radar)** on; **3D Secure/SCA** working for EU/UK. See
      [disputes & fraud](disputes-refunds-and-fraud.md).
- [ ] **Refund, dispute, and subscription** flows implemented and tested.
- [ ] **Tax** handled (Stripe Tax or a [merchant of record](choosing-a-payment-provider.md)).
- [ ] **Receipts**, refund policy, terms, and privacy policy in place. See
      [e‑commerce law](../10-legal-and-compliance/ecommerce-law.md).
- [ ] Dashboard access uses **MFA** and least privilege.
- [ ] **Monitoring & alerts** on payment failures, webhook failures, and fraud
      spikes. See [monitoring & uptime](../09-maintenance/monitoring-and-uptime.md).
- [ ] Do a **small real transaction** (and refund it) in live mode as a final
      smoke test.

This complements the general [pre‑launch checklist](../templates/pre-launch-checklist.md).

## Payouts

- Your captured funds accumulate as your Stripe **balance**, then **pay out** to
  your bank on a schedule (e.g., daily/weekly, often on a rolling delay — new
  accounts may have a longer initial hold).
- Payouts are **net of fees**, refunds, and any disputed amounts, so a payout
  rarely equals a day's gross sales — this is normal and matters for accounting.
- Stripe may hold a **reserve** for risk, especially early or for higher‑risk
  businesses.
- Negative balances (lots of refunds/disputes) can be **debited** from your bank —
  keep enough buffer.

## Reconciliation & bookkeeping

**Reconciliation** is confirming that your records, Stripe's records, and your bank
all agree. It's non‑negotiable for anything handling money.

> ✅ **Do:**
> - Link every **order** to its Stripe **payment/session ID**, and every **payout**
>   to the transactions it covers.
> - Regularly compare **your DB ↔ Stripe ↔ bank**; investigate mismatches
>   (paid‑but‑not‑fulfilled is urgent).
> - Account for **fees, refunds, disputes, and tax** separately — gross ≠ net.
> - Use Stripe's **reporting/exports** (and tools like Sigma for SQL, or your
>   accounting integration) to feed bookkeeping.
> - Keep records for the period your **tax/accounting** rules require.

Reconciliation catches missed webhooks, bugs, and fraud early — treat mismatches
as incidents. See [incident response](../09-maintenance/incident-response.md).

## Tax

As a processor, **you are the merchant of record and responsible for sales
tax/VAT/GST** where you have obligations:

- **Stripe Tax** can **calculate and collect** the right tax at checkout and help
  with reporting — but **you still register and remit** in the relevant
  jurisdictions.
- If global tax is too much to own, a **[merchant of record](choosing-a-payment-provider.md)**
  (Paddle, Lemon Squeezy, …) takes it over for a higher fee.
- Tax rules (US economic nexus, EU VAT, etc.) are complex and jurisdiction‑
  specific — get professional advice. See
  [e‑commerce law: tax](../10-legal-and-compliance/ecommerce-law.md).

## Monitoring & incident response for payments

Payments fail in ways that directly cost money, so monitor them like the critical
system they are:

- **Payment success/decline rates** — a sudden drop can mean a broken deploy, a
  key problem, or an outage. Alert on it.
- **Webhook delivery failures** — a silently failing endpoint means unfulfilled
  paid orders. See [webhooks](webhooks-and-fulfillment.md).
- **Fraud / card‑testing spikes** — bursts of tiny or failed charges.
- **Dispute ratio** — trending up threatens your account.
- **Payout failures** — bank/verification issues stopping your money.

Wire these into your [monitoring](../09-maintenance/monitoring-and-uptime.md) and
have an [incident‑response](../09-maintenance/incident-response.md) plan: a payment
outage is a revenue‑and‑trust emergency, and a payment **data** breach triggers
[breach‑notification](../10-legal-and-compliance/gdpr.md) duties.

## Keep it running: payments in ongoing maintenance

Fold payments into the [maintenance plan](../09-maintenance/maintenance-plan.md):

- Keep Stripe **libraries/SDKs and API version** current; read change/upgrade
  notes. See [dependency management](../09-maintenance/dependency-management.md).
- **Rotate keys** if exposed; review Dashboard access on a schedule. See
  [secrets management](../07-security/secrets-management.md).
- Watch for **expiring cards** on subscriptions (dunning) and update flows.
- **Re‑attest PCI** as required; revisit tax registrations as you grow into new
  jurisdictions.
- Periodically **reconcile** and review fraud rules and dispute trends.

Payments are never "done." Built carefully and operated with discipline, though,
they become the quiet, reliable engine of the business rather than a source of
emergencies.
