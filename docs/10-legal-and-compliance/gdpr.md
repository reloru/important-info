# GDPR (EU / UK Data Protection)

The **General Data Protection Regulation (GDPR)** is the EU's data‑protection law
(the UK has its near‑identical **UK GDPR**). It's the most influential privacy law
in the world, it has genuine teeth (fines up to the greater of €20 million or 4%
of global annual turnover), and — crucially — **it can apply to you even if
you're not in the EU.**

> ⚖️ Not legal advice. GDPR is detailed and fact‑specific; this is an orientation.
> Get professional advice for your situation.

## Does it apply to you?

GDPR applies if you process the personal data of people **in the EU/UK** in
connection with:

- **offering goods or services** to them (even for free), or
- **monitoring their behavior** (e.g., tracking/analytics/advertising).

Note what's *not* required: you don't have to be located in the EU, and there's
no minimum company size. A small site anywhere that has EU visitors and uses
analytics or takes sign‑ups can be in scope. When in doubt, assume it may apply.

## Key concepts

- **Personal data** — any information relating to an identifiable person. Broad:
  names, emails, IP addresses, cookie IDs, location, etc.
- **Special category data** — extra‑sensitive data (health, race, religion,
  sexuality, biometrics, etc.) with stricter rules.
- **Data subject** — the individual the data is about.
- **Controller** — decides *why and how* data is processed (usually you, the site
  owner). Bears primary responsibility.
- **Processor** — processes data on the controller's behalf (e.g., your hosting or
  analytics vendor). Requires a **Data Processing Agreement (DPA)**.
- **Processing** — basically anything you do with data (collect, store, use,
  share, delete).

## The core principles (Article 5)

You must process personal data:

1. **Lawfully, fairly, transparently.**
2. For **specified, legitimate purposes** (purpose limitation).
3. **Minimally** — only what you need (data minimization).
4. **Accurately** — keep it correct and up to date.
5. With **storage limitation** — not longer than necessary.
6. With **integrity and confidentiality** — i.e., securely. See
   [Security](../07-security/README.md).

Plus **accountability** — you must be able to *demonstrate* compliance
(documentation matters).

## You need a lawful basis

Every processing activity needs one of six **lawful bases**:

1. **Consent** — freely given, specific, informed, unambiguous, opt‑in, and as
   easy to withdraw as to give.
2. **Contract** — necessary to perform a contract with the person.
3. **Legal obligation** — required by law.
4. **Vital interests** — to protect someone's life.
5. **Public task** — official functions.
6. **Legitimate interests** — your genuine interests, balanced against the
   person's rights (requires a balancing assessment; not usable by public
   authorities for their tasks).

> 💡 For **marketing cookies/analytics and tracking**, consent is generally the
> required basis (reinforced by the ePrivacy rules) — and it must be **prior,
> opt‑in** consent. See [cookies & tracking](cookies-and-tracking.md).

## Data subject rights

People have rights you must honor (usually within **one month**), including:

- **Access** — a copy of their data and info about its processing.
- **Rectification** — correct inaccurate data.
- **Erasure** ("right to be forgotten") — deletion in certain cases.
- **Restriction** — limit processing in certain cases.
- **Portability** — receive their data in a portable format.
- **Object** — to certain processing, including **direct marketing** (absolute
  right to opt out of marketing).
- **Rights regarding automated decision‑making**/profiling.

Your systems and processes must be able to *fulfil* these — including finding and
deleting a person's data (mind your [backups](../09-maintenance/backups-and-disaster-recovery.md)).

## Consent, done right

> ✅ **Do:** Make consent **opt‑in** (unticked boxes), **specific** (separate
> consents for separate purposes), **informed**, and **withdrawable easily**.
> Keep a record of what each person consented to and when.
> ❌ **Don't:** Use pre‑ticked boxes, bundle consent into terms acceptance, make
> "reject" harder than "accept," or treat silence/inactivity as consent. These
> are unlawful (and are [dark patterns](../02-design-and-ux/ux-principles.md)).

## Breach notification

> ⚖️ A personal‑data breach that risks individuals must be reported to the
> supervisory authority **within 72 hours** of becoming aware; high‑risk breaches
> also require notifying affected individuals without undue delay. Have this in
> your [incident response](../09-maintenance/incident-response.md) plan **before**
> you need it.

## Other obligations to know

- **Records of processing** — many organizations must maintain them.
- **DPAs with processors** — contracts with vendors that handle personal data on
  your behalf.
- **International transfers** — sending EU personal data outside the EEA requires
  a valid transfer mechanism (adequacy decision, Standard Contractual Clauses,
  etc.). This has affected use of some US‑based services; check your vendors and
  hosting regions. See [infrastructure](../08-deployment-and-devops/infrastructure.md).
- **Data Protection Impact Assessments (DPIAs)** — required for high‑risk
  processing.
- **DPO** — some organizations must appoint a Data Protection Officer.
- **EU/UK representative** — non‑EU/UK controllers in scope may need one.

## Practical starting checklist

- [ ] Map what personal data you collect, why, where it goes, and how long you
      keep it.
- [ ] Identify a **lawful basis** for each processing purpose.
- [ ] Publish an accurate, plain‑language
      [privacy policy](privacy-policy.md).
- [ ] Implement **opt‑in consent** for non‑essential cookies/tracking. See
      [cookies & tracking](cookies-and-tracking.md).
- [ ] Put **DPAs** in place with processors; check international transfers.
- [ ] Build processes to handle **data subject rights** requests.
- [ ] Secure the data ([Security](../07-security/README.md)) and prepare
      **breach response** ([incident response](../09-maintenance/incident-response.md)).
- [ ] **Minimize** — stop collecting data you don't need.
- [ ] Document everything and review it periodically.

GDPR rewards the habits this whole knowledge base encourages: collect less,
secure it, be transparent, and be ready to act on requests and incidents.

## Primary sources

- [Regulation (EU) 2016/679 (GDPR), full text on EUR‑Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
  — the regulation itself; Article 5 (principles), Article 6 (lawful bases),
  Articles 12–23 (rights), Articles 33–34 (breach notification).
- [European Data Protection Board](https://edpb.europa.eu/edpb_en) — guidelines
  and consistency opinions from the EU regulators collectively.
- [UK Information Commissioner's Office — UK GDPR guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/)
  — the most readable regulator guidance in English, and authoritative for the UK.

*Where this page states a hard figure — €20 million / 4%, one month, 72 hours —
it reflects the regulation text linked above. Regulator guidance on how those
apply does move; check the EDPB or your own supervisory authority.*
