# Authentication & Authorization

Two related but distinct ideas that are constantly confused:

- **Authentication (authn)** — *Who are you?* Verifying identity (login).
- **Authorization (authz)** — *What are you allowed to do?* Enforcing
  permissions.

Both appear in the [OWASP Top 10](owasp-top-10.md) because both are frequently
broken. Getting them right protects your users' accounts and data.

## Authentication: verifying identity

### Passwords, done right
If you handle passwords yourself:

- **Never store them in plaintext or with weak hashing.** Use a strong,
  purpose‑built password hashing algorithm (e.g., bcrypt, scrypt, Argon2) with a
  unique salt per password. 🔒
- **Allow strong passwords** — encourage length over arbitrary complexity rules;
  support passphrases; don't cap length too low; allow password managers (don't
  block paste).
- **Check against known breached passwords** where feasible, and don't force
  frequent arbitrary rotation (modern guidance discourages it).

### Passkeys: the direction of travel
A **passkey** is a public‑key credential stored on the user's device or in their
password manager, created and used through the **Web Authentication API
(WebAuthn)** — a W3C Recommendation. The user authenticates locally (biometric,
device PIN), and the device proves possession of a private key to your server.
Nothing reusable is transmitted.

Why this matters more than a better password policy:

- **There is no shared secret to steal.** Your server stores only a public key,
  so a database breach yields nothing an attacker can replay.
- **Phishing‑resistant by construction.** The credential is **scoped to your
  origin** and simply won't produce a signature for a look‑alike domain. This is
  the property passwords and one‑time codes cannot provide — a user can be
  tricked into typing those into the wrong site; they cannot be tricked into
  this.
- **No credential stuffing**, because there's nothing reused across sites.

In the specification's terms, a passkey is a *client‑side discoverable
credential*: discoverable means the authenticator can offer it without your
server first identifying the user, which is what enables a sign‑in with no
username step at all.

> ✅ **Do:** Offer passkeys for new builds, and let existing users add one
> alongside their password. Support **multiple credentials per account** —
> people have more than one device, and a user with exactly one passkey and no
> recovery path is a lockout waiting to happen.
> ❌ **Don't:** Treat a passkey as a second factor bolted onto a password. It
> replaces the password; adding a second prompt for both gives users the cost of
> both and the benefit of neither.

> ⚠️ **Account recovery becomes the weak point.** Once the password is gone, the
> attacker's cheapest route is your reset flow — so an emailed "recover my
> account" link that bypasses the passkey quietly re‑introduces every phishing
> risk you just removed. Design recovery as deliberately as you design sign‑in.

### Multi‑factor authentication (MFA)
Requiring a second factor (an authenticator app, a hardware key, a code) makes
stolen passwords far less useful.

> ✅ **Do:** Offer MFA to users and **require it for admin/privileged accounts.**
> This is one of the highest‑value protections you can add.

### Protect the login and reset flows
- **Rate‑limit** and add lockout/backoff to resist brute‑force and credential
  stuffing.
- Make the **password reset** flow secure (time‑limited, single‑use tokens; no
  account enumeration that reveals which emails exist).
- Send security‑relevant notifications (new logins, password changes).

### Consider delegating auth
Building secure authentication is hard and easy to get subtly wrong. Using a
reputable identity provider or well‑maintained auth library/service (OAuth/OpenID
Connect, a managed auth platform) can be safer than rolling your own — provided
you configure it correctly.

### Sessions
- Use secure, **`HttpOnly`**, **`Secure`**, and appropriately **`SameSite`**
  cookies for session tokens. See [security headers](security-headers.md).
- Expire sessions sensibly; provide logout; regenerate session IDs on login to
  prevent fixation.
- Protect against **CSRF** (cross‑site request forgery) with tokens and/or
  `SameSite` cookies.

## Authorization: enforcing permissions

### Enforce on the server, always
> 🔒 The single most important rule: **authorization must be enforced on the
> server for every request.** Hiding a button or a menu item is a UX nicety, not
> security — an attacker just calls the endpoint directly.

### Deny by default
Grant access explicitly; deny everything else. New endpoints should be locked
down until deliberately opened.

### Check ownership (object‑level authorization)
"Broken access control" often means a user can access *another user's* object by
changing an ID in the URL (e.g., `/orders/1002` → `/orders/1003`). Always verify
that the current user is allowed to access *that specific* resource — not just
that they're logged in. This is one of the most common and damaging web
vulnerabilities.

### Least privilege
Give users, admins, services, database accounts, and API keys the **minimum**
permissions they need. A compromised low‑privilege account does less damage.

### Roles and scopes
Use clear roles/permissions (RBAC) or scopes to structure access. Keep the model
simple enough to reason about — overly complex permission systems hide bugs.

## Admin access is a special risk

Admin accounts and dashboards are prime targets:

- Require **MFA** for all admin access.
- Restrict admin interfaces (e.g., by network/IP where feasible).
- Log admin actions for accountability. See
  [monitoring](../09-maintenance/monitoring-and-uptime.md).
- Remove access promptly when someone leaves (offboarding).

## Privacy overlap

> ⚖️ **Legal note:** Accounts hold personal data, so authn/authz is also a
> data‑protection concern. Users have rights to access and delete their data;
> your auth system must support verifying identity for those requests without
> creating new risks. See [GDPR](../10-legal-and-compliance/gdpr.md) and
> [privacy policy](../10-legal-and-compliance/privacy-policy.md).

## Summary

Authenticate strongly (passkeys where you can, good password hashing and MFA
where you can't, protected flows either way), authorize strictly (server‑side,
deny‑by‑default, ownership checks, least privilege), and treat admin access as
high‑risk. When in doubt, lean on well‑tested libraries and providers rather than
inventing your own.

## Primary sources

- [Web Authentication: An API for accessing Public Key Credentials, Level 3](https://www.w3.org/TR/webauthn-3/)
  — the WebAuthn specification (W3C Recommendation, 25 August 2026), including
  the definition of a discoverable credential / passkey.
- [MDN — Web Authentication API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API)
  — the practical implementation guide.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — current
  guidance on password storage, session management, and authentication flows.
