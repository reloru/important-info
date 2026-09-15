# Security Headers

HTTP security headers are instructions your server sends with each response that
tell the browser to enable protective behaviors. They're among the
highest‑value, lowest‑effort security wins available — often just a few lines of
server or CDN configuration that harden every page at once.

## The key headers

### Strict-Transport-Security (HSTS)
Forces browsers to use **HTTPS only** for your domain, preventing downgrade and
cookie‑hijacking attacks.

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

> Add `preload` (and submit to the HSTS preload list) only once you're confident
> *all* subdomains are HTTPS — it's hard to undo. See
> [HTTPS & TLS](https-and-tls.md).

### Content-Security-Policy (CSP)
The most powerful (and most involved) header. It controls **which sources** of
scripts, styles, images, etc. the browser may load — a strong defense against
**cross‑site scripting (XSS)** and data injection.

- A good CSP blocks inline scripts and untrusted origins, so injected malicious
  scripts simply don't run.
- It takes effort to configure without breaking things — start in
  **report‑only** mode, watch violation reports, then enforce.
- Worth it for anything handling sensitive data or user accounts.

### X-Content-Type-Options
Stops browsers from "MIME‑sniffing" a response into a different content type
(which can be abused).

```
X-Content-Type-Options: nosniff
```

### X-Frame-Options / frame-ancestors
Prevents your pages from being embedded in others' `<iframe>`s
(**clickjacking**). Modern approach: use CSP's `frame-ancestors`; the older
header is `X-Frame-Options: DENY` (or `SAMEORIGIN`).

### Referrer-Policy
Controls how much referrer information is sent when users click away — a privacy
and information‑leak control.

```
Referrer-Policy: strict-origin-when-cross-origin
```

### Permissions-Policy
Lets you disable powerful browser features (camera, microphone, geolocation,
etc.) you don't use, reducing the attack surface and protecting users.

### Access-Control-Allow-Origin (CORS)
The odd one out. Every other header here **adds** a restriction; the CORS headers
**relax** one. Browsers block cross‑origin reads by default (the same‑origin
policy), and **Cross‑Origin Resource Sharing (CORS)** is how a server opts
specific other origins back in.

That inversion is why CORS is the header most often turned into a vulnerability:
misconfiguring the others weakens a defence, while misconfiguring this one
*grants access*.

```
Access-Control-Allow-Origin: https://app.example.com
Vary: Origin
```

Three rules worth internalising:

- **`*` and credentials cannot combine.** If a request carries cookies or HTTP
  auth, the wildcard is invalid — browsers reject the response outright. Name the
  exact origin and send `Access-Control-Allow-Credentials: true`.
- **Never reflect the `Origin` header blindly.** Echoing back whatever origin
  asked is functionally equivalent to allowing every site on the internet to read
  authenticated responses from your API. Validate against an **allow‑list** and
  echo only a match — and send `Vary: Origin` so caches don't serve one origin's
  response to another.
- **Preflights exist for a reason.** For anything beyond a simple request — a
  method other than GET/HEAD/POST, a custom header, an unusual `Content-Type` —
  the browser first sends an `OPTIONS` **preflight** and only proceeds if the
  server approves. `Access-Control-Max-Age` lets the browser cache that approval.

> ⚠️ CORS protects **browsers**, not servers. It governs what a browser will let
> a page *read* cross‑origin; it is not access control. A direct request from
> `curl` or a server ignores it entirely. Authorization still has to be enforced
> server‑side on every request — see
> [authentication & authorization](authentication-and-authorization.md).

> ✅ **Do:** Default to no CORS headers at all, and add a narrow allow‑list only
> where a real cross‑origin client needs one.
> ❌ **Don't:** Reach for `Access-Control-Allow-Origin: *` to make a console
> error go away. That error is usually telling you something true.

### A related control: Subresource Integrity
Headers govern what the browser *may* load. **Subresource Integrity (SRI)**
governs whether what arrived is what you expected — a hash in an `integrity`
attribute that the browser verifies before running a third‑party script or
stylesheet. It pairs with CORS (SRI requires it) and with CSP, and it's covered
with the rest of the third‑party problem in
[third‑party scripts](../03-development-best-practices/third-party-scripts.md).

## Cookie security attributes

Not headers per se, but set on cookies and just as important:

- **`Secure`** — only sent over HTTPS.
- **`HttpOnly`** — not readable by JavaScript (limits XSS damage to session
  cookies).
- **`SameSite`** — restricts cross‑site sending (helps prevent **cross‑site
  request forgery, CSRF**). Use `Lax` or `Strict` for session cookies.

See [authentication](authentication-and-authorization.md) for session handling.

## How to apply them

- Set headers at the **server, reverse proxy, or CDN** level so they apply
  everywhere consistently.
- Many platforms let you configure them in a config file or dashboard.
- **Test** with an online security‑headers scanner and your browser's dev tools.

> ✅ **Do:** Start with the easy wins (HSTS, `nosniff`, frame protection,
> `Referrer-Policy`, secure cookie flags), then invest in a proper **CSP**.
> ❌ **Don't:** Copy a strict CSP blindly and break your site — build it up
> incrementally using report‑only mode first.

## Don't forget the flip side: don't leak information

Hardening also means **not oversharing**:

- Remove or genericize headers that reveal exact software versions (they help
  attackers target known vulnerabilities).
- Don't expose verbose error messages or stack traces to users (a
  [security misconfiguration](owasp-top-10.md)).

## Why bother

Security headers are cheap insurance: a small configuration change that mitigates
whole classes of attack (XSS, clickjacking, protocol downgrade, CSRF) across your
entire site. There's rarely a good reason to skip the basic set. Include a
security‑headers check in your
[pre‑launch checklist](../templates/pre-launch-checklist.md) and periodic
[security reviews](../09-maintenance/maintenance-plan.md).
