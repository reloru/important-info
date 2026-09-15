# Data Retention

Most privacy work focuses on what you collect and how you protect it. Retention
is the neglected third question: **how long do you keep it, and what actually
happens when that time is up?**

It's neglected because storage is cheap and deleting feels like losing something.
But data you no longer need is pure liability — it can still be breached,
subpoenaed, mis‑used, or requested by the person it describes. **The safest data
is the data you don't have.**

> ⚖️ Not legal advice. Retention periods depend on your jurisdiction, sector, and
> the specific purpose. Some periods are legally mandated minimums; others are
> maximums. Confirm yours.

## The rule you're working to

Under GDPR this is **storage limitation** — one of the core principles: personal
data must be kept "no longer than is necessary for the purposes for which it is
processed." US state laws increasingly express the same idea as a
data‑minimisation duty.

Note what the principle does *not* say. It sets no numbers. There is no
"GDPR retention period," and any vendor who tells you there is a universal answer
is guessing. What it requires is that you can **justify** the period you chose —
which means the period has to be a decision someone made, not a default nobody
reviewed.

> ✅ **Do:** Set a period **per purpose**, write down the reasoning, and review
> it periodically.
> ❌ **Don't:** Keep everything "in case it's useful later." That is precisely
> the reasoning the principle exists to rule out.

## Building a retention schedule

A retention schedule is a table. It does not need to be elaborate to be a large
improvement on nothing.

| Data | Purpose | Period | Basis for the period | Then what? |
|---|---|---|---|---|
| Contact‑form submissions | Answer the enquiry | 12 months | Enough for follow‑up; enquiries go cold | Delete |
| Customer orders | Fulfil, support, and meet tax/accounting duties | Per statutory accounting period | **Legal obligation** — often the longest clock on your site | Delete or archive |
| Account data | Operate the account | Life of account + short grace period | Lets users reactivate; limits indefinite holding | Delete |
| Marketing list | Send what they opted into | Until opt‑out, plus engagement review | Consent isn't perpetual in practice | Delete on opt‑out |
| Server / access logs | Security and debugging | Weeks to months | Long enough to investigate an incident | Rotate and delete |
| Analytics | Understand usage | Vendor‑configurable | Aggregates rarely need raw retention | Aggregate, then delete |
| Backups | Recovery | Your backup rotation | See the tension below | Expire with the rotation |

The important column is the fourth one. "Because that's the default" is not a
basis; "our accountant requires this period" is.

> 💡 **Tax and accounting rules usually set your longest retention clock**, and
> they're a *legal obligation* rather than a preference — which also means a
> deletion request generally can't override them. This is the most common
> legitimate reason to keep data after someone asks you to delete it, and your
> [privacy policy](privacy-policy.md) should say so.

## Deletion is harder than it looks

Writing "we delete after 12 months" is easy. Making it true is the work.

Personal data spreads. Before you promise deletion, find out where a given
person's data actually lives:

- the primary database, and any **replicas** or read copies;
- **search indexes** and caches;
- **logs** — application, access, and error logs often contain emails or IPs;
- **exports**: the CSV someone downloaded, the spreadsheet in shared storage;
- **email**: your support inbox is a personal‑data store nobody thinks about;
- **third‑party vendors** — your CRM, email platform, analytics, helpdesk. See
  [vendors & subprocessors](vendors-and-subprocessors.md);
- **backups.**

> ⚠️ **Backups are the classic conflict**, and there's a defensible answer.
> Selectively deleting one person's records from historical backups is usually
> impractical and can compromise the backups' integrity. The widely accepted
> approach is: delete from live systems immediately, let backups **expire
> naturally** on their documented rotation, ensure the deletion is **re‑applied
> if a backup is ever restored**, and don't use backup data for anything but
> recovery. Document that as your position. See
> [backups & disaster recovery](../09-maintenance/backups-and-disaster-recovery.md).

## Automate it, or it won't happen

Manual deletion scheduled for "sometime next quarter" does not occur.

> ✅ **Do:** Implement retention as a **scheduled job** that runs on its own.
> Configure retention settings in the third‑party tools that offer them —
> analytics, logging, and helpdesk platforms usually do. Alert on failure, the
> same as any other scheduled job. See
> [monitoring & uptime](../09-maintenance/monitoring-and-uptime.md).

Consider whether you need deletion at all, or whether **anonymisation** serves
the purpose. Genuinely anonymised data — where no individual can be
re‑identified, by you or anyone else — falls outside data‑protection rules, so
you can keep the analytical value without the liability. The bar is high:
pseudonymised data, where a key still exists somewhere, is **still personal
data**.

## Retention and deletion requests

Retention interacts directly with the rights you have to honour:

- A **deletion request** is much easier to fulfil when you already know where
  data lives — the same map serves both.
- An **access request** must cover everything you hold, including the copies
  above. Shorter retention means less to find.
- **Don't over‑delete under pressure**: if a legal obligation requires you to
  keep something, keep it and explain why.

See [GDPR](gdpr.md) and [CCPA/CPRA](ccpa-cpra.md).

## Checklist

- [ ] A **retention schedule** exists, per data type and purpose.
- [ ] Each period has a **written justification**, not a default.
- [ ] Statutory minimums (tax, accounting, sector rules) are identified.
- [ ] You know **everywhere** each data type lives, including logs and vendors.
- [ ] Deletion is **automated** and monitored, not a manual reminder.
- [ ] The backup position is documented and consistently applied.
- [ ] Vendor‑side retention settings are configured, not left at defaults.
- [ ] The [privacy policy](privacy-policy.md) reflects the real periods.
- [ ] The schedule is reviewed on a cycle — see
      [maintenance plan](../09-maintenance/maintenance-plan.md).

## Primary sources

- [ICO — Principle (e): Storage limitation](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/)
  — the clearest regulator guidance on justifying retention periods.
- [Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
  — Article 5(1)(e) states the storage‑limitation principle.
