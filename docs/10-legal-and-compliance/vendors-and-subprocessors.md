# Vendors & Subprocessors

Almost nothing about a modern website is built by the people who own it. Hosting,
email delivery, analytics, payments, chat, CRM, error tracking, backups, the CDN
— each is a company holding some of your users' data on your behalf.

Data‑protection law is unambiguous about where responsibility sits: **you don't
outsource accountability.** If you decide why and how personal data is processed
you are the **controller**, and you remain answerable to your users for what your
vendors do with it — including vendors you didn't know you had.

> ⚖️ Not legal advice. Contract requirements and transfer rules vary by
> jurisdiction and change; this is the shape of the obligation, not a substitute
> for advice or for reading the contract.

## Controller, processor, subprocessor

Three roles, and the third is the one that surprises people:

- **Controller** — decides the *why* and *how*. Usually you, the site owner.
- **Processor** — processes on the controller's behalf, under instruction. Your
  host, your email platform, your analytics vendor.
- **Subprocessor** — a processor **your processor** engaged. Your email platform
  runs on someone else's cloud. Your helpdesk uses a separate transcription
  service. Your CDN has regional partners.

Your data reaches the subprocessor, but your contract is with the processor. That
chain is where most site owners' real exposure sits — not because it's
illegitimate, but because **it's invisible unless you go looking.**

> 💡 The practical test: if a vendor three layers down had a breach tomorrow,
> would you find out, and would you know whether your users were affected? If
> not, you have a chain you haven't mapped.

## What the contract has to do

Under GDPR, a controller must only use processors offering sufficient guarantees,
and the relationship must be governed by a **written contract** — commonly a
**Data Processing Agreement (DPA)**. Article 28 sets out what it must cover:

- the **subject matter, duration, nature and purpose** of the processing, the
  types of data, and the categories of data subject;
- that the processor acts **only on documented instructions** from you;
- **confidentiality** commitments from people processing the data;
- appropriate **security measures**;
- terms on **engaging subprocessors** (below);
- assistance with **data‑subject rights** and with breach notification;
- **deletion or return** of the data at the end of the contract;
- submitting to **audits** and making available the information needed to
  demonstrate compliance.

Most established vendors publish a standard DPA you can accept. **Read it rather
than assuming** — and note whether accepting it is a separate step, because for
many platforms it is.

## The subprocessor rules that matter

This is the part people skip:

- A processor **must not engage a subprocessor without your prior written
  authorisation** — either *specific* (you approve each one) or *general* (you
  approve the practice in advance).
- Under general authorisation, the processor must **tell you about intended
  changes** — additions or replacements — and give you a real chance to
  **object**.
- The processor must impose **equivalent protection** on the subprocessor,
  contractually. The obligations flow down; they don't dilute.
- The original processor generally **remains fully liable to you** for the
  subprocessor's performance.

> ✅ **Do:** Find each major vendor's **subprocessor list** — reputable ones
> publish it — and **subscribe to its change notifications** if offered. That
> subscription is the mechanism that makes the "chance to object" real rather
> than theoretical.
> ❌ **Don't:** Accept a DPA that lets the processor add subprocessors freely
> with no notice, if you have any negotiating position at all. For a small site
> using large platforms you usually don't — in which case at least *know* that's
> the deal you took.

## International transfers

> ⚖️ Sending EU/UK personal data outside the EEA requires a valid transfer
> mechanism — an **adequacy decision** for the destination country, **Standard
> Contractual Clauses**, or another recognised route. This is a live issue for
> website operators because so many default vendors are US‑based, and because
> the transfer can be invisible: a vendor in your own country may run on
> infrastructure elsewhere, or support it from a third region.

Ask where data is **stored**, and separately where it is **accessed from** —
support access from another jurisdiction is a transfer too. Many vendors offer
regional hosting; choosing the right region at signup is far easier than
migrating later. See
[infrastructure](../08-deployment-and-devops/infrastructure.md) and
[GDPR](gdpr.md).

## Assessing a vendor before you sign

Proportionate to the sensitivity of the data:

| Question | Why it matters |
|---|---|
| What data do they get, really? | Often more than the feature requires |
| Is there a **DPA**, and have you accepted it? | Frequently a separate click |
| Where is data stored and accessed from? | Transfer mechanism, data residency |
| Who are the **subprocessors**, and how are changes notified? | Your invisible chain |
| **Security posture** — certifications, track record, disclosure process? | You inherit their weaknesses |
| **Retention and deletion** — what happens at the end? | See [data retention](data-retention.md) |
| **Breach notification** — how fast, and to whom? | Your 72‑hour clock depends on theirs |
| **Exit** — can you export your data in a usable form? | Lock‑in is a risk, not just a cost |

> 🔒 **Security note:** A vendor is also an attack surface. Their compromise can
> become your incident — directly, through data they hold, or through code they
> serve to your pages. See
> [third‑party scripts](../03-development-best-practices/third-party-scripts.md)
> and [OWASP Top 10](../07-security/owasp-top-10.md).

## Keep a register

You need a current list. Record, per vendor: what it does, what personal data it
receives, DPA status and date, storage region, subprocessor‑list URL, breach
contact, and the internal owner.

This register is not busywork — it's what you reach for when you need to:

- answer an **access or deletion request** that spans systems;
- assess whether a vendor's breach affects **your** users;
- complete the **records of processing** many organisations must maintain;
- write a [privacy policy](privacy-policy.md) that's actually accurate;
- run a [privacy compliance check](../templates/privacy-compliance-checklist.md).

> ⚠️ Vendors accumulate exactly like [third‑party scripts](../03-development-best-practices/third-party-scripts.md)
> do: added for a reason, kept past it. A trial account from two years ago still
> holding a customer export is a live liability with no upside. **Offboard
> deliberately** — export what you need, confirm deletion, close the account,
> revoke the API keys. See
> [secrets management](../07-security/secrets-management.md).

## Checklist

- [ ] A **vendor register** exists and is current.
- [ ] Every vendor touching personal data has an **accepted DPA**.
- [ ] Subprocessor lists are known; change notifications subscribed where offered.
- [ ] **Transfer mechanisms** identified for data leaving the EEA/UK.
- [ ] Storage **and access** regions are known, not assumed.
- [ ] Breach‑notification paths are understood in both directions.
- [ ] Retention settings are configured vendor‑side — see
      [data retention](data-retention.md).
- [ ] The [privacy policy](privacy-policy.md) reflects the real vendor list.
- [ ] Unused vendors are **offboarded**, with data deleted and keys revoked.
- [ ] The register is reviewed on a cycle — see
      [maintenance plan](../09-maintenance/maintenance-plan.md).

## Primary sources

- [ICO — what needs to be included in the contract?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/what-needs-to-be-included-in-the-contract/)
  — the clearest breakdown of Article 28 terms, including the subprocessor
  authorisation and notification rules described above.
- [Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
  — Article 28 governs processors and subprocessors; Chapter V covers
  international transfers.
- [European Data Protection Board](https://edpb.europa.eu/edpb_en) — guidance on
  controller/processor roles and on transfer mechanisms.
