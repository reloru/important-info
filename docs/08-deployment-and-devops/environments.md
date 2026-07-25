# Environments

An **environment** is a complete, separate copy of your site set up for a
specific purpose. Keeping development, testing, and live systems apart is
fundamental to shipping safely — it's how you try changes without risking real
users or real data.

## The standard environments

### Development (local)
Where developers write and run code on their own machines. Fast iteration; broken
states are fine; uses fake/sample data.

### Staging (a.k.a. test / pre‑production)
A **production‑like** environment for final testing and stakeholder review. It
should mirror production as closely as practical — same platform, configuration,
and similar data — so that "works on staging" reliably predicts "works in
production."

### Production
The **live** site real users interact with. Changes reach here only after passing
through the earlier environments. Treat it with care.

Some teams add more (QA, UAT, demo, per‑feature preview environments), but
dev → staging → production is the essential spine.

## Why separation matters

> ✅ **Do:**
> - Test every change in **staging before production.**
> - Keep configuration and secrets **separate per environment.** See
>   [secrets management](../07-security/secrets-management.md).
> - Make staging as **production‑like** as you can afford — big differences hide
>   bugs until they hit real users.

> ❌ **Don't:**
> - Test directly in production.
> - Share databases or credentials across environments.
> - Let staging drift far from production ("it worked in staging" becomes
>   meaningless).

## Configuration per environment

The same code should run in every environment, with **only configuration
differing** (database URLs, API endpoints, keys, feature flags). Keep config out
of the code and inject it per environment via environment variables or a config
service. This is a core principle of maintainable deployments.

## Data in non‑production environments

> ⚖️ **Legal note:** Be careful with data in staging/test. Using **real
> customers' personal data** outside production multiplies where sensitive data
> lives and your exposure if it leaks — and can itself breach data‑protection
> rules. Prefer **synthetic** or properly **anonymized** data for testing. If
> you must use production data, protect it to the same standard as production
> and minimize it. See [GDPR](../10-legal-and-compliance/gdpr.md) and
> [testing](../03-development-best-practices/testing.md).

Also keep non‑production environments from being **publicly discoverable and
indexed**:

- Protect staging behind authentication or IP restrictions.
- Prevent search engines from indexing it (but remember to remove any `noindex`
  before that code reaches production — a classic launch bug!). See
  [technical SEO](../06-seo/technical-seo.md).

## Environments and releases

- Use [version control](../03-development-best-practices/version-control.md) tags
  or release markers so you know exactly what's deployed where.
- Promote a **specific, tested build** from staging to production — don't rebuild
  separately for prod, which could introduce differences.
- Keep the ability to **roll back** production to the previous known‑good
  release. See [CI/CD](ci-cd.md).

## Right‑sizing for small projects

A tiny brochure site may not need a full staging server — but it should at least
have a way to preview changes before they go live (many static/managed hosts
offer free preview/deploy‑preview environments per change). The principle holds
at every scale: **prove it somewhere safe before it's live.**
