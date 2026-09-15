# Forms & Input Handling

Forms are where your site accepts input from the outside world — contact
messages, sign‑ups, searches, uploads, checkouts. That makes them simultaneously
a **usability** surface, a **security** boundary, and a **spam magnet.** Other
pages cover the pieces; this one ties them together into how to handle form
submissions **correctly and safely.** It complements
[form usability](../02-design-and-ux/ux-principles.md) (how forms should feel) and
[semantic HTML](semantic-html.md) (how to mark them up); here the focus is what
happens *after* the user hits submit.

## Validate in two places, for two different reasons

A recurring source of bugs and vulnerabilities is confusing these:

- **Client‑side validation is for UX.** Instant feedback ("that's not a valid
  email") makes forms pleasant. It is **not security** — anyone can bypass the
  browser and post directly to your endpoint.
- **Server‑side validation is for correctness and security.** The server must
  **re‑validate everything**, because it cannot trust anything the client sends.

> 🔒 **The rule:** validate on the client for a good experience, and **always
> re‑validate on the server** as the real gate. Never rely on the browser to
> enforce anything that matters. This is the same "never trust the client"
> principle behind [payments](../11-payments/stripe-integration.md) and
> [authorization](../07-security/authentication-and-authorization.md).

## Treat all input as hostile

Every field is untrusted until validated. This is the antidote to whole classes
of vulnerability (see [OWASP Top 10](../07-security/owasp-top-10.md)):

> ✅ **Do:**
> - **Validate** type, length, format, and range server‑side; reject or safely
>   handle anything unexpected.
> - **Use parameterized queries** for anything that touches a database (prevents
>   SQL injection).
> - **Encode/escape output** by context when displaying user input (prevents
>   cross‑site scripting, XSS) — especially critical for anything that echoes a
>   submission back, or stores it for later display.
> - **Protect state‑changing forms with CSRF tokens** (cross‑site request
>   forgery — a page an attacker controls making your logged‑in user submit your
>   form) and appropriate `SameSite` cookies. See
>   [security headers](../07-security/security-headers.md).

> ❌ **Don't:** Build queries by concatenating input, render user input as raw
> HTML, or assume "it's just a contact form, what could go wrong?" Contact forms
> are probed constantly.

## Spam & abuse: every public form will be attacked

Automated bots submit to public forms relentlessly — junking your inbox/database,
abusing "email a friend"/comment features to relay spam, and testing for
vulnerabilities. Layer defenses (no single one is perfect):

- **Honeypot field** — a hidden field real users never fill; bots often do.
  Silently discard submissions that fill it. Cheap, invisible, and effective
  against unsophisticated bots. (Keep it truly hidden *and* out of the
  accessibility tree — e.g., `aria-hidden` + off‑screen, not just `type=hidden`,
  and label it clearly as "leave blank" for the rare AT edge case. ♿)
- **Time trap** — reject submissions that arrive implausibly fast (bots submit in
  milliseconds).
- **Rate limiting** — cap submissions per IP/session/account over time to blunt
  floods, brute force, and [card testing](../11-payments/disputes-refunds-and-fraud.md).
  A basic, high‑value control that's currently easy to forget.
- **CAPTCHA / challenge** — a last resort when needed, because it adds friction
  and can harm accessibility. Prefer **low‑friction, privacy‑respecting**
  challenge services over classic "click all the traffic lights" puzzles, and
  ensure an accessible alternative exists. ♿⚖️ (Note: some challenge services
  are third‑party scripts that process user data — mind
  [privacy/consent](../10-legal-and-compliance/cookies-and-tracking.md).)
- **Server‑side moderation/filtering** for user‑generated content, plus the
  ability to review and remove.

> 💡 Start with the **invisible** defenses (honeypot, time trap, rate limiting) —
> they stop most bots with zero user friction. Add a visible CAPTCHA only if spam
> persists, and keep it accessible.

## File uploads: a special hazard

If a form accepts files, it's a high‑risk feature:

> 🔒 **Do:**
> - **Validate type and size** (allow‑list expected types; enforce limits).
> - **Don't trust the filename or declared content type**; verify the actual
>   content, and **never execute** uploaded files.
> - **Store uploads outside the web root** (or in object storage) and serve them
>   safely; consider **malware scanning**.
> - Watch for **server‑side request forgery (SSRF)** and parsing issues in
>   anything that processes uploads (image libraries, PDF parsers). See
>   [OWASP Top 10](../07-security/owasp-top-10.md).

## Where submissions go

A submission usually needs to be **stored**, **emailed**, or both — each has
pitfalls:

- **Email notifications** — sending mail from your app raises **deliverability**:
  authenticate your domain with **SPF, DKIM, and DMARC** so your mail is trusted
  and not spoofed, and prefer a reputable sending service over raw SMTP. See
  [DNS, domains & SSL](../08-deployment-and-devops/domains-dns-ssl.md). Never put
  unsanitized user input into email **headers** (header‑injection risk).
- **Storage** — persist only what you need, secure it, and remember it's often
  **personal data**. See privacy note below.
- **Reliability** — if a submission triggers important downstream work (an order,
  a ticket), make it **idempotent** and don't silently drop failures — queue,
  retry, and alert. This mirrors [webhook handling](../11-payments/webhooks-and-fulfillment.md).

## Accessibility & error handling

Handling errors well is both usability and accessibility:

> ♿ **Do:**
> - Return errors in **plain language**, tied to the specific field, and
>   **preserve** what the user already entered (never wipe the form).
> - Make errors **programmatically associated** with fields and announced to
>   assistive tech. See [Accessibility](../04-accessibility/README.md) and
>   [form usability](../02-design-and-ux/ux-principles.md).
> - Confirm success clearly.

## Privacy: forms are data collection

Every form that gathers personal data triggers privacy obligations:

> ⚖️ **Do:**
> - **Collect only what you need** (data minimization).
> - Explain use and link your [privacy policy](../10-legal-and-compliance/privacy-policy.md)
>   at the point of collection.
> - For newsletter/marketing sign‑ups, use proper **opt‑in consent** and an
>   unsubscribe path. See [email marketing law](../10-legal-and-compliance/email-marketing-law.md).
> - Don't log sensitive submitted data, and secure what you store. See
>   [GDPR](../10-legal-and-compliance/gdpr.md).

## Form handling checklist

- [ ] **Server‑side validation** re‑checks everything (client‑side is UX only).
- [ ] **Parameterized queries**; **output encoding**; **CSRF protection**.
- [ ] Invisible anti‑spam (**honeypot, time trap, rate limiting**) in place;
      CAPTCHA only if needed and **accessible**.
- [ ] File uploads (if any) **type/size‑validated**, stored safely, never
      executed, scanned if feasible.
- [ ] Email notifications: **SPF/DKIM/DMARC** set; no header injection;
      reputable sender.
- [ ] Errors are **accessible, field‑specific, plain‑language**, and preserve
      input.
- [ ] Only **necessary personal data** collected; privacy policy linked; consent
      for marketing.
- [ ] Important submissions handled **reliably** (idempotent, retried, monitored).

Forms look simple and are quietly one of the most attacked, most bug‑prone parts
of a site. Handle them with the same care you give payments and auth — the
principles are the same.
