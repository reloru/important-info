# CI/CD

**CI/CD** automates the path from a code change to a deployed site. It stands for
**Continuous Integration** and **Continuous Delivery/Deployment** — the practice
of building, testing, and releasing software automatically and frequently. It's
the backbone of modern, reliable web development.

## The two (or three) letters

- **Continuous Integration (CI)** — every change is automatically **built and
  tested** as soon as it's pushed. Problems are caught immediately, while the
  change is small and fresh in the author's mind.
- **Continuous Delivery (CD)** — every change that passes CI is automatically
  prepared for release, so deploying is a **push‑button** (or automatic) step.
- **Continuous Deployment** — goes further: passing changes deploy to production
  **automatically**, with no manual gate.

## What a pipeline typically does

On each push or pull request, the pipeline runs a sequence of stages, stopping if
any fails:

1. **Build** — compile/bundle the site.
2. **Lint & format check** — enforce [coding standards](../03-development-best-practices/coding-standards.md).
3. **Test** — unit, integration, and end‑to‑end tests. See
   [testing](../03-development-best-practices/testing.md).
4. **Security & dependency scan** — check for known vulnerabilities and, ideally,
   [secret leaks](../07-security/secrets-management.md).
5. **Accessibility & performance checks** — automated a11y scan and a
   [performance budget](../05-performance/performance-budgets.md) check (e.g.,
   Lighthouse CI).
6. **Deploy** — to staging automatically; to production on approval or
   automatically, depending on your model.

## Why it's worth it

- **Catch problems early** — a failing test blocks the merge, not the release.
- **Consistency** — every deploy follows the exact same steps; no "forgot to run
  the build" surprises.
- **Speed and confidence** — automated safety nets let you ship small changes
  often, which is *safer* than rare big releases.
- **Auditability** — a record of what was built, tested, and deployed, and when.
- **Faster security patching** — when you need to ship a fix, the pipeline makes
  it quick and safe.

## Deployment strategies (reducing risk)

- **Rollback‑ready releases** — always able to revert to the previous version
  fast. The simplest and most essential safety net.
- **Blue‑green** — run two production environments; switch traffic to the new one
  once it's verified; switch back instantly if needed.
- **Canary / phased rollout** — release to a small percentage of users first,
  watch for problems, then expand.
- **Feature flags** — deploy code "off," then turn features on (and off)
  independently of deployment. Great for decoupling release from deploy.

## Guard the pipeline itself

> 🔒 **Security note:** Your CI/CD system has access to production and to
> secrets, making it a high‑value target. Protect it:
> - Store credentials in the platform's **encrypted secrets** store, never in
>   the pipeline config. See
>   [secrets management](../07-security/secrets-management.md).
> - Limit who can change pipeline configuration and approve production deploys.
> - Be cautious with third‑party build actions/plugins — they run with your
>   pipeline's access (a supply‑chain risk — see
>   [OWASP Top 10](../07-security/owasp-top-10.md)).
> - Pin dependency and action versions.

## Start simple

You don't need an elaborate setup on day one. Even a minimal pipeline that
**runs your tests and linting on every pull request** and **deploys on merge** is
a huge step up from manual releases. Grow it as the project's needs grow.

> ✅ **Do:** Automate at least test + deploy from the start; add security,
> accessibility, and performance gates as you mature.
> ❌ **Don't:** Deploy by dragging files to a server. It's untracked,
> inconsistent, and unrepeatable.

Pair CI/CD with proper [environments](environments.md) so changes are proven in
staging before they reach real users.
