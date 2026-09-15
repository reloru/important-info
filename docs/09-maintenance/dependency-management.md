# Dependency Management

Modern websites are built on layers of external code: frameworks, libraries,
plugins, themes, the CMS core, the runtime, and the OS. Every one of those is a
**dependency you must keep updated**, because vulnerabilities are discovered in
them constantly. Outdated components are one of the most common causes of website
compromise — and one of the most preventable.

## Why this is the quiet #1 risk

When a vulnerability is disclosed in a popular library or plugin, attackers begin
scanning for sites still running the old version *within hours*. A site that
isn't updated is a sitting target. The fix is almost always "update the
dependency" — the hard part is having a process that ensures you actually do,
promptly.

This maps directly to
[OWASP: Vulnerable & Outdated Components](../07-security/owasp-top-10.md).

## Know what you depend on

You can't secure what you don't know you're running.

- Maintain an **inventory** of dependencies and their versions (your package
  manifest/lockfile does much of this automatically).
- Include the **whole stack**: app libraries, CMS core, plugins/themes, runtime
  (language version), server OS, and infrastructure components.
- Watch **transitive dependencies** — the dependencies of your dependencies —
  which often outnumber your direct ones.

## Automate detection

- Use **dependency/vulnerability scanning** (e.g., built‑in scanners on your code
  host, or dedicated tools) to alert you when a dependency has a known
  vulnerability.
- Enable **automated update PRs** (bots that open pull requests to bump versions)
  so updates are surfaced and testable, not forgotten.
- Wire scans into **CI** so problems are visible on every change. See
  [CI/CD](../08-deployment-and-devops/ci-cd.md).

## Update safely

> ✅ **Do:**
> - Prioritize **security updates** — apply critical ones fast, outside the
>   normal cycle if needed.
> - Test updates in **staging** before production. See
>   [environments](../08-deployment-and-devops/environments.md).
> - **Back up before** significant upgrades so you can roll back. See
>   [backups](backups-and-disaster-recovery.md).
> - Read **changelogs/release notes** for breaking changes.
> - Use **lockfiles** to pin exact versions for reproducible builds.
> - Update **regularly and incrementally** — small, frequent updates are far
>   easier and safer than rare, giant ones.

> ❌ **Don't:**
> - Ignore update notifications until a breach forces the issue.
> - Blindly auto‑merge major version bumps without testing.
> - Add dependencies casually — every one is a maintenance and security
>   liability (see below).

## Fewer dependencies, less risk

Every dependency is code you didn't write, running with your app's privileges,
that someone must keep patched.

> ✅ **Do:** Evaluate before adding: Is it actively maintained? Widely used?
> Reasonably sized? Do you really need it, or can a few lines of your own do the
> job? Prefer well‑maintained, popular libraries with healthy communities.

Abandoned dependencies are especially dangerous — no maintainer means no security
fixes. Periodically check whether anything you rely on is **unmaintained or
end‑of‑life**, and plan replacements.

## Plugins and CMS platforms deserve extra caution

> 🔒 For CMS‑based sites (e.g., WordPress), **plugins and themes are the leading
> source of vulnerabilities.** Install only what you need, only from reputable
> sources, keep them all updated, and **remove** deactivated/unused ones (they're
> still on the server and still exploitable). A CMS is a standing commitment to
> patching.

> 💡 Package dependencies are only half the supply chain. Scripts loaded at
> runtime from a third‑party URL aren't in your lockfile at all, and the vendor
> can change them without a release. See
> [third‑party scripts](../03-development-best-practices/third-party-scripts.md).

## Supply‑chain awareness

Attackers sometimes compromise the dependency itself (a hijacked package, a
malicious update). Mitigations:

- Pin versions with lockfiles and review updates.
- Verify sources; be wary of typosquatted package names.
- Limit what your build pipeline and dependencies can access (see
  [CI/CD security](../08-deployment-and-devops/ci-cd.md) and
  [OWASP: integrity failures](../07-security/owasp-top-10.md)).

## Make it routine

Fold dependency management into your
[maintenance plan](maintenance-plan.md): continuous scanning and alerts, prompt
security patches, a regular routine‑update cadence in staging, and periodic audits
for end‑of‑life components. Boring and regular beats dramatic and reactive.
