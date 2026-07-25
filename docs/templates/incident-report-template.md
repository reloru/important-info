# Incident Report Template

Use this to document an incident and its post‑mortem. The goal is **learning and
prevention, not blame.** Keep completed reports somewhere the team can reference
them. For the process, see
[incident response](../09-maintenance/incident-response.md).

---

## Incident summary

- **Incident ID / title:** `[SHORT NAME]`
- **Date/time detected:** `[YYYY-MM-DD HH:MM TZ]`
- **Date/time resolved:** `[YYYY-MM-DD HH:MM TZ]`
- **Duration:** `[e.g., 2h 14m]`
- **Severity:** `[Critical / High / Medium / Low]`
- **Incident lead:** `[NAME]`
- **Systems affected:** `[e.g., checkout, main site, database]`
- **User impact:** `[who was affected and how; approx. how many]`
- **Personal data involved?** `[Yes / No / Unknown]` ⚖️ *(If yes, see the
  breach‑notification note below.)*

## Timeline

| Time | Event |
|------|-------|
| `[HH:MM]` | `[e.g., monitoring alert fired: 5xx spike]` |
| `[HH:MM]` | `[e.g., on-call acknowledged, began investigation]` |
| `[HH:MM]` | `[e.g., root cause identified]` |
| `[HH:MM]` | `[e.g., fix deployed / rolled back]` |
| `[HH:MM]` | `[e.g., service confirmed restored]` |

## What happened

`[Plain-language narrative of the incident from detection to resolution.]`

## Root cause

`[The underlying cause — not just the symptom. What actually went wrong, and why
did it reach production?]`

## Detection

- **How was it detected?** `[monitoring alert / user report / other]`
- **Could it have been detected sooner?** `[yes/no + how]`

## Response & resolution

- **What was done to contain it?** `[…]`
- **What resolved it?** `[fix / rollback / restore from backup / etc.]`
- **What went well?** `[…]`
- **What was difficult or slow?** `[…]`

## Impact assessment

- **Availability:** `[downtime, degraded features]`
- **Data:** `[any loss, corruption, or exposure]`
- **Users/customers:** `[who, how many, what they experienced]`
- **Business/reputation:** `[…]`

## Data breach considerations ⚖️

*(Complete only if personal data may have been exposed.)*
- **Data types potentially affected:** `[…]`
- **Number of individuals potentially affected:** `[…]`
- **Notification obligations assessed?** `[Yes/No]` — *GDPR may require notifying
  the supervisory authority within 72 hours and, for high‑risk breaches,
  affected individuals; US state laws and sector rules may also apply. See
  [GDPR](../10-legal-and-compliance/gdpr.md).*
- **Notifications made:** `[authority / individuals / when]`
- **Who approved the notification decision:** `[NAME/ROLE]`

## Action items (prevention)

| Action | Owner | Due | Status |
|--------|-------|-----|--------|
| `[e.g., add monitor for X]` | `[NAME]` | `[date]` | `[open]` |
| `[e.g., patch dependency Y]` | `[NAME]` | `[date]` | `[open]` |
| `[e.g., update runbook]` | `[NAME]` | `[date]` | `[open]` |

## Lessons learned

`[What will we do differently? What systemic improvement prevents this class of
problem, not just this instance?]`

---

> Blameless principle: focus on **systems and processes**, not individuals.
> People make mistakes; resilient systems make those mistakes hard to make and
> easy to recover from.
