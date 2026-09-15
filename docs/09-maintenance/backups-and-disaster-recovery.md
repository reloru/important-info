# Backups & Disaster Recovery

Backups are your last line of defense against disaster — hardware failure,
ransomware, a botched deploy, a hack, a fat‑fingered `DROP TABLE`, or a provider
outage. The crucial, frequently‑ignored truth: **a backup you haven't tested
restoring is not a backup — it's a hope.**

## Backups vs. disaster recovery

- **Backup** — a recoverable copy of your data and site.
- **Disaster recovery (DR)** — the whole plan for getting back to operation after
  a serious failure: backups *plus* the process, roles, and targets for
  restoring service.

Backups are a component; DR is the strategy.

## What to back up

- **Databases** — usually the crown jewels (user data, content, orders).
- **User‑uploaded files / media** — often stored outside the database.
- **Application code** — via [version control](../03-development-best-practices/version-control.md)
  (but note: code in Git ≠ your data backed up).
- **Configuration & infrastructure** — ideally as
  [infrastructure as code](../08-deployment-and-devops/infrastructure.md).
- **Secrets/credentials** — securely, so a rebuild is possible (in a secrets
  manager, not a plaintext file). See
  [secrets management](../07-security/secrets-management.md).

> ⚖️ **Legal note:** Backups hold personal data, which makes them part of your
> retention and deletion story — including the practical tension between a
> deletion request and a historical backup. See
> [data retention](../10-legal-and-compliance/data-retention.md).

## The 3‑2‑1 rule

A durable, widely‑used backup strategy:

- **3** copies of your data,
- on **2** different types of media/storage,
- with **1** copy **off‑site** (a different location/provider).

This survives the failure of any single system, location, or provider.

## Make backups resilient to attack

> 🔒 **Security note:** Ransomware and attackers deliberately target backups. Keep
> at least one copy **offline or immutable** (write‑once, or with delete
> protection) and **separated** from production credentials, so a compromise of
> your live system can't also destroy your backups. Backups that an attacker can
> reach and delete are little protection.

## Automate and verify

> ✅ **Do:**
> - **Automate** backups on a schedule — manual backups get skipped.
> - Match **frequency** to how much data you can afford to lose (see RPO below).
> - **Monitor** backup jobs and alert on failures — silent backup failure is a
>   nasty surprise at the worst moment.
> - **Test restores regularly** — actually restore to a scratch environment and
>   confirm the data is complete and usable. This is the step everyone skips and
>   everyone regrets.
> - **Retain** multiple points in time (so you can go back *before* a
>   slow‑burning corruption or breach, not just to yesterday).

> ❌ **Don't:**
> - Assume your host backs you up. **Verify** what they back up, how often, how
>   long they keep it, and whether *you* can restore it. See
>   [domains & hosting](../01-planning-and-strategy/domains-and-hosting.md).
> - Store backups only in the same place as production.
> - Trust a backup you've never restored.

## Two numbers that define your DR plan

- **RPO (Recovery Point Objective)** — how much data loss is acceptable? (Drives
  backup *frequency*. RPO of 1 hour → back up at least hourly.)
- **RTO (Recovery Time Objective)** — how quickly must you be back online? (Drives
  how *ready* your restore process must be.)

Decide these deliberately based on the site's importance; they tell you how much
to invest.

## Write the recovery runbook

When disaster strikes, you don't want to be improvising. Document, in advance:

- Where backups are and how to access them.
- **Step‑by‑step restore instructions** (tested, so you know they work).
- Who is responsible and how to reach them.
- How to rebuild infrastructure if needed.
- How to communicate status to stakeholders/users.

Keep it with your [incident response](incident-response.md) plan.

## Privacy note for backups

> ⚖️ **Legal note:** Backups contain personal data, so they're subject to
> data‑protection rules too — secure them, control access, and account for them
> in retention and deletion practices. (Handling data‑subject deletion requests
> across backups is a known nuance — document your approach.) See
> [GDPR](../10-legal-and-compliance/gdpr.md).

## The bottom line

Automate backups, follow 3‑2‑1, keep a copy attackers can't reach, define your
RPO/RTO, and — above all — **test that you can actually restore.** The worst time
to discover your backups don't work is during the disaster they were meant to
save you from.
