# Incident Response

An incident is any unplanned disruption or security event — the site is down, a
breach is suspected, data is corrupted, a deploy went wrong. Incidents *will*
happen. What separates a manageable event from a disaster is having a **calm,
prepared plan** rather than improvising under pressure at 2 a.m.

## Prepare before you need it

The time to write your incident plan is *before* an incident. Decide in advance:

- **Roles** — who leads the response? Who communicates? Who has the access needed
  to fix things?
- **Contacts** — an up‑to‑date list, including out‑of‑hours reach and key vendors
  (host, DNS, security).
- **Access** — responders can actually get into the systems (and you're not
  locked out — see [secrets management](../07-security/secrets-management.md)).
- **Runbooks** — step‑by‑step guides for common scenarios (site down, cert
  expired, restore from backup, suspected breach). See
  [documentation](../03-development-best-practices/documentation.md).
- **Severity levels** — how you classify and prioritize incidents.

## The response lifecycle

A widely‑used model, adaptable to any size of team:

### 1. Detect
Become aware of the incident — ideally via [monitoring/alerts](monitoring-and-uptime.md)
rather than a customer complaint.

### 2. Assess & triage
- What's affected, how badly, and how many users?
- Is **personal data** involved? (This changes your legal obligations — see
  below. ⚖️)
- Assign severity and mobilize the right people.

### 3. Contain
Limit the damage. For a security incident that may mean isolating affected
systems, revoking compromised credentials, or taking something offline.

> 🔒 **Preserve evidence** during a suspected breach (logs, system state) before
> wiping and rebuilding — you may need it to understand scope and to meet legal
> obligations.

### 4. Eradicate & recover
Remove the cause (patch the vulnerability, remove malicious code, fix the bug),
then restore normal operation — often from a known‑good
[backup](backups-and-disaster-recovery.md) or a rollback to the previous
release. **Verify** the problem is truly gone before declaring recovery.

### 5. Communicate
Keep stakeholders informed throughout — internal team, affected users, and (where
required) regulators. Honest, timely communication protects trust; silence and
cover‑ups destroy it.

### 6. Review (post‑mortem)
After the dust settles, run a **blameless post‑mortem**: what happened, why, how
you responded, and what will prevent recurrence. The goal is *learning and
improvement*, not blame. Turn findings into concrete fixes (a new monitor, a
patched process, a runbook update).

## Security breaches: legal obligations

> ⚖️ **Legal note — read this before you need it:** If personal data is
> compromised, **data‑protection laws impose mandatory breach‑notification
> duties, often on tight deadlines:**
>
> - **GDPR (EU/UK):** notify the relevant supervisory authority **within 72
>   hours** of becoming aware of a personal‑data breach that poses a risk to
>   individuals, and notify **affected individuals** without undue delay if the
>   risk is high.
> - **US state laws:** most US states have their own breach‑notification laws
>   with their own timelines and requirements.
> - **Sector rules** (health, finance, etc.) may impose additional obligations.
>
> Know *in advance* who decides on notification, who drafts it, and which
> authorities/users must be told. Missing these deadlines can compound a breach
> with regulatory penalties. See
> [GDPR](../10-legal-and-compliance/gdpr.md) and
> [privacy policy](../10-legal-and-compliance/privacy-policy.md).

## Communicating well during an incident

> ✅ **Do:**
> - Acknowledge promptly; don't wait for perfect information.
> - Be honest about what you know, what you don't, and what you're doing.
> - Give a realistic next‑update time and keep it.
> - For breaches, follow legal notification requirements and be straight with
>   affected users.

> ❌ **Don't:**
> - Go silent and hope people don't notice.
> - Minimize, spin, or cover up — it destroys trust and can worsen legal
>   exposure.
> - Speculate publicly about cause before you know.

## A minimal incident plan (even for small sites)

Even a one‑person operation should have:

- A way to **know** when the site is down (monitoring + alerts).
- A **runbook** for the top few scenarios (site down, restore from backup, cert
  expired).
- Tested **backups** and a rollback path.
- A short list of **who to contact** (host, DNS, and — for breaches — whom to ask
  about legal obligations).

Preparation converts panic into procedure. That's the whole point.
