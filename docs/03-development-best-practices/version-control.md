# Version Control

Version control tracks every change to your code over time, lets multiple people
collaborate without overwriting each other, and gives you a safety net to undo
mistakes. **Git** is the near‑universal standard. Using it well — from the first
commit — is non‑negotiable professional practice.

## Why it's essential

- **History** — see what changed, when, by whom, and *why*.
- **Undo** — revert to any previous working state.
- **Collaboration** — many people work in parallel and merge their work.
- **Branching** — develop features and fixes in isolation, then integrate.
- **Accountability & review** — changes are reviewable before they land.
- **Deployment** — modern deploys are driven off version control. See
  [CI/CD](../08-deployment-and-devops/ci-cd.md).

> ❌ **Don't:** Edit files directly on the production server. It's untracked,
> unreviewable, and unrecoverable when it breaks. Changes should flow from
> version control to production, not the other way around.

## Core concepts

- **Repository (repo)** — the project and its full history.
- **Commit** — a saved snapshot of changes with a message explaining them.
- **Branch** — an independent line of development.
- **Merge** — combining one branch's changes into another.
- **Remote** — a shared copy (e.g., on GitHub/GitLab) that the team syncs with.
- **Pull request / merge request** — a proposed change, reviewed before merging.

## Commit well

> ✅ **Do:**
> - Make **small, focused commits** — one logical change each.
> - Write **clear commit messages**: a concise summary line, then a body
>   explaining *why* if it's not obvious.
> - Commit working states; don't commit broken code to shared branches.

> ❌ **Don't:**
> - Bundle unrelated changes into one giant commit.
> - Write messages like "fix," "stuff," or "asdf."

A common message convention:

```
Short imperative summary (≤ ~50 chars)

Optional body explaining the motivation and context — the *why*, not
the *what* (the diff already shows the what). Wrap at ~72 chars.
```

## Branching strategies

Pick one that fits your team size and release cadence:

- **Trunk‑based** — everyone integrates into `main` frequently behind short‑lived
  branches. Simple; pairs well with continuous delivery.
- **GitHub Flow** — branch off `main`, open a pull request, review, merge,
  deploy. Great for web projects.
- **Git Flow** — more elaborate, with long‑lived `develop`/`release` branches.
  Suits scheduled releases; often overkill for websites.

Whatever you choose, keep branches **short‑lived** to avoid painful merges.

## Never commit secrets

> 🔒 **Security note:** **Never commit passwords, API keys, tokens, or
> credentials.** Git history is forever — even a deleted secret remains in the
> history and must be *rotated*, not just removed. Use a `.gitignore` for env
> files, store secrets in environment variables or a secrets manager, and
> consider automated secret scanning. See
> [secrets management](../07-security/secrets-management.md).

## `.gitignore`

Exclude things that shouldn't be tracked: dependencies (`node_modules/`), build
output, local env files, editor/OS cruft, and anything sensitive. A clean repo
is easier to work with and safer.

## Tags and releases

Use **tags** to mark released versions (often with semantic versioning:
`v1.4.2`). This makes it easy to know exactly what's deployed and to roll back to
a known‑good point. See [environments](../08-deployment-and-devops/environments.md).

## Backups are not version control (and vice versa)

Version control protects your *code's* history; it is not a substitute for
backing up your *data* (databases, user uploads). Both are needed. See
[backups & disaster recovery](../09-maintenance/backups-and-disaster-recovery.md).
