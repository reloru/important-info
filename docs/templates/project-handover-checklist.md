# Project Handover & Ownership Checklist

A copy‑ready checklist for **handing a website over** — from an agency/freelancer
to a client, between teams, or at the end of a build — and for making sure the
**"who owns and maintains this?" gap never opens.** This addresses one of the most
common and costly failure patterns in web work: a site launches, the builders move
on, and nobody actually owns the domain, the credentials, or the ongoing
maintenance. See
[roles & responsibilities](../00-getting-started/roles-and-responsibilities.md).

> Fill in owners and dates. Do this **before** the relationship or engagement ends
> — chasing a former contractor for the domain login months later is exactly what
> this prevents.

## 1. Accounts & ownership (the critical part)
- [ ] The **client/owner controls their own accounts** — registrar, hosting, DNS,
      CDN, analytics, email, payment provider, and any platform logins — under
      **their** billing and email, not the builder's. See
      [domains & hosting](../01-planning-and-strategy/domains-and-hosting.md).
- [ ] An **account inventory** exists: every service, who owns it, the login, the
      renewal date, and where credentials live.
- [ ] Credentials transferred via a **secure method** (a shared password manager /
      secret manager), **never** plaintext email/spreadsheet. See
      [secrets management](../07-security/secrets-management.md).
- [ ] **MFA** re‑enrolled under the owner's control (so recovery doesn't depend on
      the departing party's phone/email).
- [ ] Builder/contractor access **revoked** where it's no longer needed
      (offboarding); remaining access is intentional and documented.

## 2. Domain, DNS & certificates
- [ ] **Domain** in the owner's registrar account; **auto‑renew on**; billing +
      contact email current; registrar lock and WHOIS privacy set.
- [ ] **DNS** records documented and under the owner's control.
- [ ] **TLS certificate** auto‑renewing and **monitored** for expiry. See
      [DNS, domains & SSL](../08-deployment-and-devops/domains-dns-ssl.md).

## 3. Code, content & assets
- [ ] **Source code** repository transferred/accessible to the owner, with history.
      See [version control](../03-development-best-practices/version-control.md).
- [ ] **Ownership of code, design, and content** settled in writing (assignment or
      license) per the contract. See [licensing](../10-legal-and-compliance/licensing.md).
- [ ] **Third‑party asset licenses** (fonts, images, plugins, stock) documented and
      transferable — or the owner knows what they must license themselves. See
      [copyright & IP](../10-legal-and-compliance/copyright-and-ip.md).
- [ ] Any **pre‑existing/reusable components** and their license terms identified.

## 4. Documentation
- [ ] A **README / handover doc** covers: what the site is, how to run it locally,
      how to deploy, and how to roll back. See
      [documentation](../03-development-best-practices/documentation.md).
- [ ] **Architecture overview** and key **decisions/rationale** recorded.
- [ ] **Operational runbooks** for common scenarios (site down, cert expiry, restore
      from backup). See [incident response](../09-maintenance/incident-response.md).
- [ ] **Account inventory** (from §1) and environment/config notes included.

## 5. Operations & maintenance ownership
- [ ] **Backups** configured, and a **restore has been tested**; the owner knows how
      to recover. See [backups & disaster recovery](../09-maintenance/backups-and-disaster-recovery.md).
- [ ] **Monitoring & alerts** (uptime, errors, cert/domain expiry) route to someone
      who will act. See [monitoring & uptime](../09-maintenance/monitoring-and-uptime.md).
- [ ] **Who applies security patches**, and how often, is **explicitly assigned and
      agreed** — the single most common gap. See
      [dependency management](../09-maintenance/dependency-management.md).
- [ ] A **maintenance plan** (or a maintenance contract) is in place, funded, and
      owned. See [maintenance plan](../09-maintenance/maintenance-plan.md) and the
      [maintenance checklist](maintenance-checklist.md).

## 6. Legal & compliance continuity
- [ ] **Privacy policy, cookie consent, terms** are live, accurate, and the owner
      knows they must be **kept current** as laws/practices change. See
      [Legal & Compliance](../10-legal-and-compliance/README.md) and the
      [privacy & compliance checklist](privacy-compliance-checklist.md).
- [ ] For sites taking payments: payment account, tax setup, and the
      [payments go‑live checklist](payments-go-live-checklist.md) items are owned by
      the client.
- [ ] **Liability for maintenance, security, and compliance** after handover is
      clear in writing. See
      [budgeting & scoping](../01-planning-and-strategy/budgeting-and-scoping.md).

## 7. Final verification
- [ ] The owner has **successfully logged into** each critical account themselves.
- [ ] A short **walkthrough/training** delivered (how to edit content, deploy,
      respond to an alert).
- [ ] A named person **owns the site going forward** — accountability sits with one
      identifiable owner, not "the team."

---

> The test of a good handover: if the builder disappeared tomorrow, could the owner
> keep the site running, secure, and compliant? If any box above is unchecked, the
> answer is probably no.
