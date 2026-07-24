# Maintenance Checklist

A copy‑ready recurring checklist. Assign an owner to each item, set reminders,
and scale to your site's risk. For the reasoning behind it, see the
[maintenance plan](../09-maintenance/maintenance-plan.md).

## Owners (fill in)

| Responsibility | Owner | Frequency |
|----------------|-------|-----------|
| Security patching / dependency updates | `[NAME]` | Weekly + as needed |
| Backups & restore testing | `[NAME]` | Automated + monthly test |
| Monitoring & alert response | `[NAME]` | Continuous |
| Domain / certificate renewals | `[NAME]` | Auto + monitored |
| Content accuracy & link checks | `[NAME]` | Monthly / quarterly |
| Legal / compliance review | `[NAME]` | Annually + on change |

## Continuous (automated)
- [ ] Uptime & error monitoring active with working alerts.
- [ ] Automated backups running; failure alerts on.
- [ ] CI checks (tests, lint, security scan) on every change.
- [ ] Dependency vulnerability alerts enabled.

## Weekly
- [ ] Review monitoring/error alerts; investigate anomalies.
- [ ] Apply **critical security updates** promptly.
- [ ] Confirm backups succeeded (check for failures).
- [ ] Triage user‑reported issues.

## Monthly
- [ ] Apply routine dependency/plugin/CMS/platform updates (staging → prod).
- [ ] **Test a backup restore** to a scratch environment.
- [ ] Check Core Web Vitals / performance vs. budget.
- [ ] Scan for broken links / 404s and fix.
- [ ] Review access: remove accounts/keys no longer needed.
- [ ] Skim analytics for issues and opportunities.

## Quarterly
- [ ] Full dependency audit; plan larger version upgrades.
- [ ] Accessibility re‑check of key pages (automated + keyboard + screen reader).
- [ ] Security review: headers, configs, unused accounts/keys, cert config.
- [ ] Content audit: accuracy, freshness, dead links, outdated info.
- [ ] Disaster‑recovery drill (restore + rebuild steps).

## Annually
- [ ] **Legal/compliance review**: privacy policy, cookie banner, terms,
      accessibility statement still accurate as laws + site changed. ⚖️
- [ ] Confirm domain + certificate renewals and correct ownership.
- [ ] Identify end‑of‑life / unmaintained dependencies; plan replacements.
- [ ] Revisit hosting/infrastructure fit and cost.
- [ ] Review this checklist and the maintenance plan itself.

## Before any significant update
- [ ] Read changelog/release notes for breaking changes and security notes.
- [ ] **Back up** first.
- [ ] Apply and test in **staging**.
- [ ] Promote to production with a **rollback** ready.

## Record of work (log)

| Date | Who | What was done | Notes / issues found |
|------|-----|---------------|----------------------|
| `[YYYY-MM-DD]` | `[NAME]` | `[e.g., applied security updates]` | `[…]` |

> Keeping this log demonstrates diligence (useful for legal/accessibility),
> speeds up [incident response](../09-maintenance/incident-response.md), and
> prevents things from silently slipping.
