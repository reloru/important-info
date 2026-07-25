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

Authenticate strongly (good password hashing, MFA, protected flows), authorize
strictly (server‑side, deny‑by‑default, ownership checks, least privilege), and
treat admin access as high‑risk. When in doubt, lean on well‑tested libraries and
providers rather than inventing your own.
