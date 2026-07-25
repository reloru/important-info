# Maintenance Plan

A maintenance plan turns "we should keep the site healthy" into a concrete,
recurring, owned schedule. Without one, maintenance happens reactively — i.e.,
after something has already broken. This page gives you a ready‑to‑adapt cadence.

See also the copy‑ready
[maintenance checklist template](../templates/maintenance-checklist.md).

## Assign owners first

Every recurring task needs a named owner and a defined frequency. "Everyone's
responsibility" is nobody's. Record who owns:

- Security patching and dependency updates.
- Backups and restore testing.
- Monitoring and alert response.
- Domain and certificate renewals.
- Content accuracy and link checking.
- Legal/compliance review.

See [roles & responsibilities](../00-getting-started/roles-and-responsibilities.md).

## A recurring cadence

### Continuous / automated
- **Uptime & error monitoring** with alerts (see
  [monitoring](monitoring-and-uptime.md)).
- **Automated backups** (see [backups](backups-and-disaster-recovery.md)).
- **CI checks** on every change (see [CI/CD](../08-deployment-and-devops/ci-cd.md)).
- **Security/dependency scanning** alerts.

### Weekly
- [ ] Review monitoring/error alerts and act on anomalies.
- [ ] Apply **critical security updates** promptly (don't wait for the monthly
      cycle for urgent ones). See
      [dependency management](dependency-management.md).
- [ ] Confirm backups are running and check for failures.
- [ ] Triage any user‑reported issues.

### Monthly
- [ ] Apply routine dependency/platform/plugin/CMS updates (in staging first).
- [ ] **Test a backup restore** (at least periodically — a backup you've never
      restored is a hope, not a backup).
- [ ] Review performance vs. your
      [budget](../05-performance/performance-budgets.md); check Core Web Vitals.
- [ ] Check for broken links and 404s.
- [ ] Review security alerts and access (who still needs access?).
- [ ] Review [Search Console](../06-seo/search-console.md) — the Performance
      report for traffic changes and the Pages report for new indexing errors,
      manual actions, or security issues.
- [ ] Review analytics for issues and opportunities (see
      [analytics](../06-seo/analytics.md)).

### Quarterly
- [ ] Full **dependency audit** and larger version upgrades, planned.
- [ ] **Accessibility re‑check** of key pages (see
      [testing accessibility](../04-accessibility/testing-accessibility.md)).
- [ ] **Security review** (headers, configs, unused accounts/keys, cert config).
- [ ] Content audit: accuracy, freshness, dead links, outdated info (see
      [content updates](content-updates.md)).
- [ ] Verify **disaster‑recovery** plan and run a restore drill.

### Annually
- [ ] **Legal/compliance review** — privacy policy, cookie banner, terms,
      accessibility statement still accurate as laws and the site have changed.
      ⚖️ See [Legal & Compliance](../10-legal-and-compliance/README.md).
- [ ] Confirm **domain and certificate** renewals and ownership are in order.
- [ ] Review the tech stack and dependencies for anything **end‑of‑life** or
      unmaintained.
- [ ] Revisit hosting/infrastructure fit and cost.
- [ ] Review the maintenance plan itself.

## Handle updates safely

> ✅ **Do:**
> - Apply updates in **staging** first, test, then promote to production. See
>   [environments](../08-deployment-and-devops/environments.md).
> - **Back up before** major updates so you can roll back.
> - Read changelogs for **breaking changes** and security notes.
> - Keep **critical security patches** on a fast track — apply them quickly,
>   even outside the normal cycle.

> ❌ **Don't:**
> - Apply big updates directly to production and hope.
> - Let updates pile up until a giant, risky, all‑at‑once upgrade is needed.

## Track everything

Keep a simple record of what was done and when: updates applied, backups tested,
issues found and fixed, reviews completed. This creates accountability, aids
[incident response](incident-response.md), and — for legal/accessibility —
demonstrates diligence. ⚖️

## Right‑size the plan

A small brochure site needs a lighter version of this than a busy e‑commerce
app — but *every* site needs **security updates, working backups, uptime
monitoring, and renewal tracking** at minimum. Scale the rest to the site's risk
and complexity.
