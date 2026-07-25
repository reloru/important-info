# 08 · Deployment & DevOps

Deployment is how your code becomes a live website; DevOps is the set of
practices that make deployment **reliable, repeatable, and low‑risk**. The goal
is boring deploys: you push a change, automation builds and tests it, and it goes
live safely — with a clear way to undo it if something's wrong.

## Why this matters

Manual, ad‑hoc deployment ("upload the files and pray") is where outages,
inconsistencies, and untracked changes come from. Good deployment practice turns
releases from stressful events into routine, safe operations — which means you
ship improvements and security fixes more often, not less.

## In this section

- **[CI/CD](ci-cd.md)** — automating build, test, and release.
- **[Environments](environments.md)** — dev, staging, and production, and why
  you need them.
- **[Infrastructure](infrastructure.md)** — where and how your site runs, and
  infrastructure as code.
- **[DNS, domains & SSL](domains-dns-ssl.md)** — the operational plumbing of
  making a domain resolve securely.

## Core principles

> ✅ **Do:**
> - **Automate deployments** so they're repeatable and human error is minimized.
> - **Deploy from version control**, never by editing production directly. See
>   [version control](../03-development-best-practices/version-control.md).
> - **Test in a staging environment** that mirrors production before releasing.
> - **Keep a rollback path** — always be able to get back to the last good
>   state quickly.
> - **Separate secrets and config per environment.** See
>   [secrets management](../07-security/secrets-management.md).
> - **Make deploys small and frequent** — small changes are easier to test and
>   safer to roll back than big-bang releases.

> ❌ **Don't:**
> - Edit live files on the server.
> - Deploy untested code to production "just this once."
> - Share credentials or data between environments.
> - Deploy on a Friday afternoon with no rollback plan. 😉

## Deployment is where security and reliability meet

The deployment pipeline is itself a security‑sensitive asset (it has access to
production and secrets) and the mechanism by which you ship patches. A healthy
pipeline is what lets you respond quickly when a vulnerability needs fixing. See
[Security](../07-security/README.md) and
[Maintenance & Operations](../09-maintenance/README.md).
