# Secrets Management

Secrets are the credentials that unlock your systems: API keys, database
passwords, tokens, encryption keys, third‑party service credentials. Leaked
secrets are a leading cause of breaches — and they leak in boringly predictable
ways. Managing them well is basic hygiene with outsized impact.

## The cardinal rule

> 🔒 **Never commit secrets to version control.** Not "temporarily," not "in a
> private repo," not "I'll remove it later." Git history is permanent — a secret
> committed once and later deleted **still exists in the history** and must be
> treated as compromised. See
> [version control](../03-development-best-practices/version-control.md).

Public code hosting is continuously scanned by bots looking for committed keys.
An AWS key pushed to a public repo can be found and abused within *minutes*.

## Where secrets should live

- **Environment variables** — inject secrets at runtime via the environment, not
  in code. Keep local ones in an `.env` file that is **git‑ignored**.
- **Secrets managers / vaults** — dedicated services (e.g., cloud secret
  managers, HashiCorp Vault, platform "secrets" features) that store, encrypt,
  access‑control, and audit secrets.
- **Platform secret stores** — most hosting/CI platforms provide encrypted
  secret storage for deployments. Use them instead of hard‑coding.

> ❌ **Don't:** Paste secrets into code, config files in the repo, front‑end
> JavaScript (anything sent to the browser is public!), Slack messages,
> screenshots, or a shared spreadsheet of plaintext passwords.

## Front‑end secrets are not secret

Anything shipped to the browser can be read by anyone. "Hiding" an API key in
front‑end JavaScript does not protect it. If a key must stay secret, it belongs
on the **server**, which proxies the request. Use keys designed for public use
(with strict scoping/referrer restrictions) only where the vendor intends it.

## Good practices

> ✅ **Do:**
> - **Least privilege** — scope each key/credential to only what it needs.
> - **Rotate** secrets periodically and immediately after any suspected
>   exposure or staff departure.
> - **Separate secrets per environment** — dev, staging, and production should
>   never share credentials. See
>   [environments](../08-deployment-and-devops/environments.md).
> - **Audit access** — know who and what can read each secret.
> - **Use secret scanning** in CI and on your repos to catch accidental commits.
> - **Revoke** unused credentials.

## If a secret leaks

Treat it as compromised, even if the exposure was brief:

1. **Rotate/revoke it immediately** — generate a new one and invalidate the old.
2. **Assess the blast radius** — what could that secret access? Check logs for
   misuse.
3. **Remove it from history** if it was committed (and still rotate — removal
   alone is not enough).
4. **Follow your [incident response](../09-maintenance/incident-response.md)
   process**, including any breach‑notification obligations if personal data was
   at risk. ⚖️

## Credentials for the team

Human passwords need managing too:

- Use a **password manager** for shared and personal credentials — never
  plaintext lists.
- Enable **MFA** everywhere it's offered (registrar, hosting, DNS, email, CI,
  cloud). See [authentication](authentication-and-authorization.md).
- Maintain an **account inventory** (who controls what) and an **offboarding**
  process to revoke access when people leave. See
  [domains & hosting](../01-planning-and-strategy/domains-and-hosting.md).

## The takeaway

Keep secrets out of code and out of the browser, store them in environment
variables or a proper secrets manager, scope and rotate them, separate them by
environment, and be ready to rotate fast if one leaks. This one discipline
prevents a large share of avoidable breaches.
