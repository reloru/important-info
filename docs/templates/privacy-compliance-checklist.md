# Privacy & Compliance Checklist

A copy‑ready checklist for the **data‑protection and privacy** obligations that
apply to almost every site that collects any personal data. Run it when you build
data flows, before launch, and on your **annual** compliance review (see the
[maintenance plan](../09-maintenance/maintenance-plan.md)). It consolidates the
[Legal & Compliance section](../10-legal-and-compliance/README.md) into actionable
items.

> ⚖️ **Not legal advice.** This helps you ask the right questions; laws vary by
> jurisdiction and change. For real risk, consult a qualified professional. Which
> items apply depends on where your users are and what you do — adapt accordingly.

## 1. Know your data (the foundation)
- [ ] **Map what personal data you collect** — categories, sources (forms,
      analytics, cookies, third parties), where it flows, and who can access it.
      ("Personal data" is broad: names, emails, **IP addresses**, device/cookie
      IDs, location.) See [GDPR](../10-legal-and-compliance/gdpr.md).
- [ ] **Identify which laws apply** based on your users (EU/UK → GDPR;
      California/other US states → CCPA/CPRA & peers) and activities.
- [ ] **Data minimization** — collect and keep only what you actually need; every
      extra field is a liability.
- [ ] **Retention** — defined periods (or criteria); a way to delete data when no
      longer needed (including in [backups](../09-maintenance/backups-and-disaster-recovery.md)).

## 2. Lawful basis & transparency
- [ ] Each processing purpose has a **lawful basis** (GDPR: consent, contract,
      legitimate interests, etc.). See [GDPR](../10-legal-and-compliance/gdpr.md).
- [ ] A **privacy policy** is published, **accurate to your real practices**, in
      plain language, and linked prominently (footer + collection points). See
      [privacy policy](../10-legal-and-compliance/privacy-policy.md) and the
      [template](privacy-policy-template.md).
- [ ] Special rules handled if relevant: **children's** data (COPPA / GDPR age of
      consent) and **special‑category** (sensitive) data.

## 3. Cookies & tracking
- [ ] Every cookie/tracker **inventoried** and classified **essential vs.
      non‑essential**. See [cookies & tracking](../10-legal-and-compliance/cookies-and-tracking.md).
- [ ] **EU/UK:** non‑essential cookies/trackers **do not load before opt‑in
      consent**; accept and reject are **equally easy**; consent is granular and
      withdrawable; consents recorded. **Verify nothing fires before consent** (dev
      tools).
- [ ] **US:** notice provided; **opt‑out** of sale/sharing where applicable;
      recognized signals (**GPC**) honored.
- [ ] No **dark patterns** in the consent UI. See
      [UX: dark patterns](../02-design-and-ux/ux-principles.md).
- [ ] A **cookie policy** is published and matches the inventory. See the
      [template](cookie-policy-template.md).
- [ ] Third‑party scripts/assets audited; **self‑host fonts/assets** where feasible
      to avoid leaking user data (e.g. the Google Fonts GDPR ruling).

## 4. Data subject / consumer rights
- [ ] Processes exist to **fulfill rights** within legal timeframes — access,
      correction, deletion, objection/opt‑out, portability (scope depends on the
      law).
- [ ] A clear, working **contact/mechanism** for requests, with **identity
      verification** that doesn't create new risk.
- [ ] Right to **opt out of marketing** honored; marketing email follows consent +
      unsubscribe rules. See [email marketing law](../10-legal-and-compliance/email-marketing-law.md).

## 5. Vendors & transfers
- [ ] **Data Processing Agreements (DPAs)** in place with processors (hosting,
      analytics, email, payments) that handle personal data for you.
- [ ] **International transfers** use a valid mechanism (adequacy, SCCs); hosting
      **region/data residency** chosen deliberately. See
      [infrastructure](../08-deployment-and-devops/infrastructure.md).
- [ ] Payment/card data handled by a compliant processor; you store **tokens, not
      cards**. See [PCI compliance](../11-payments/pci-compliance.md).

## 6. Security & breach readiness
- [ ] Personal data protected with appropriate measures (encryption, access
      control) — run the [security hardening checklist](security-hardening-checklist.md). 🔒
- [ ] **Breach‑response plan** ready, including **notification duties** (⚖️ GDPR:
      supervisory authority within **72h**; affected individuals if high risk; US
      state and sector rules too). See
      [incident response](../09-maintenance/incident-response.md).
- [ ] Records/documentation of compliance measures kept (demonstrates good faith;
      GDPR **accountability**).

## 7. Governance & review
- [ ] A **DPO** appointed if required; an **EU/UK representative** if a non‑EU/UK
      controller in scope.
- [ ] Compliance **re‑reviewed at least annually** and whenever data practices or
      laws change (see [maintenance plan](../09-maintenance/maintenance-plan.md)).
- [ ] Terms of service consistent with the privacy policy and actual practices. See
      [terms of service](../10-legal-and-compliance/terms-of-service.md).

---

> The recurring theme: **collect less, secure it, be transparent, and be ready to
> act on requests and incidents.** Doing those four things well covers most of what
> overlapping privacy laws require.
