# Third‑Party Scripts

Every `<script src="https://someone-else.com/...">` on your page is a decision to
run **code you don't control, on your domain, with your users' data.** Analytics,
chat widgets, ad tags, A/B testing, heatmaps, fonts, embedded video, consent
banners — a typical site accumulates a dozen of them, usually one at a time,
usually without anyone deciding the total was acceptable.

This page is about treating that collection as something you **own and manage**
rather than something that happens to you. It's the connective tissue between
four sections that each see one face of the same problem: security, performance,
privacy, and payments.

## Why a third‑party script is different from your own code

A script loaded from another origin runs with the **same privileges as your own
JavaScript**. It can:

- read and modify **any content on the page**, including form fields;
- read **cookies** not marked `HttpOnly`, and anything in `localStorage`;
- **send data anywhere**, to any origin it likes;
- **change what it does at any time** — the vendor can ship new code to your
  site's users without telling you, because you linked to *their* URL, not a
  fixed artifact.

That last point is the one people miss. Your dependency review covered the
version of the library you installed. It did not cover the version the vendor
decides to serve tomorrow. See
[dependency management](../09-maintenance/dependency-management.md) for the
package side of this — the two are complementary, not the same problem.

> 🔒 **This is the Magecart attack class.** Attackers compromise a widely used
> third‑party script (or the vendor's CDN, or a sub‑dependency of the script) and
> use it to skim card numbers and credentials from checkout and login pages. The
> victim sites were not themselves breached; they had simply linked to something
> that later turned hostile.

## Decide before you add

The cheapest third‑party script is the one you never added.

> ✅ **Do:** Ask, for each one: What does it do that we need? Who owns it? What
> data does it get? What happens to the page if it's slow, or down, or wrong?
> Could we get 80% of the value from something self‑hosted?
> ❌ **Don't:** Add a tag because marketing asked, a tutorial included it, or it
> was free. Free scripts are paid for with your users' data and your page speed.

A useful discipline: **each script needs a named owner and a reason**, recorded
somewhere. Scripts with neither are the ones still running three years after the
campaign ended.

## Keep an inventory

You cannot manage what you haven't listed. Maintain a record of every
third‑party origin your pages load, with:

| Field | Why it matters |
|---|---|
| **Script / vendor** | Who to contact, and whose incident notices to read |
| **Pages it loads on** | Scope — especially whether it touches checkout or login |
| **Purpose & owner** | Lets you retire it when the reason expires |
| **Data it can access** | Drives your privacy notice and your consent categories |
| **Loading method** | `async`/`defer`/blocking, and whether it's gated on consent |

Your browser's dev‑tools network panel, sorted by domain, gives you the honest
current list — which is often longer than anyone expects, because **scripts load
other scripts.** A tag manager is one entry in your HTML and an unbounded number
of actual third parties at runtime.

> ⚠️ A tag manager moves the decision of "what runs on our site" from your
> deploy pipeline — where it gets reviewed — to a web console where it usually
> doesn't. That's convenient for marketing and a real governance gap. If you use
> one, put change control around it and review its container periodically.

## Pin what you can: Subresource Integrity

**Subresource Integrity (SRI)** lets the browser verify that a fetched file is
*exactly* the file you expected. You publish a cryptographic hash of the
resource's contents in an `integrity` attribute; the browser hashes what it
actually received and **refuses to run it on any mismatch**.

```html
<script src="https://cdn.example.com/widget.v3.js"
        integrity="sha384-[BASE64 HASH OF THAT EXACT FILE]"
        crossorigin="anonymous"></script>
```

You generate the hash from the file itself — most CDNs publish it alongside the
resource, and you can compute it locally from the downloaded file.

Details that trip people up:

- The hash algorithm must be **`sha256`, `sha384`, or `sha512`** — `sha384` is
  the common choice. You may list several hashes; the browser uses the strongest.
- **`crossorigin` is mandatory for cross‑origin resources.** SRI requires CORS,
  so the server must also send an appropriate `Access-Control-Allow-Origin`.
  Without `crossorigin`, a request carrying `integrity` **always fails.** See
  [CORS in security headers](../07-security/security-headers.md).
- SRI works on `<script>` and on `<link>` with `rel` of `stylesheet`, `preload`,
  or `modulepreload`.
- A mismatch is a **network error**: the script doesn't execute, the stylesheet
  doesn't apply. Make sure the page degrades sanely when that happens.

> ✅ **Do:** Use SRI for third‑party scripts pinned to a specific version.
> ❌ **Don't:** Expect SRI to work with a "latest" URL that the vendor updates in
> place — the hash will break on every vendor release. That tension is the point:
> **a URL whose contents can change under you is exactly the thing SRI is
> warning you about.** Prefer versioned URLs, or self‑host.

## Constrain what you can't pin: CSP

Where SRI can't apply (a vendor script that legitimately changes, or one that
loads further scripts), a **Content Security Policy** limits the damage by
restricting which origins may load and which may be connected to. `script-src`
controls what runs; `connect-src` controls where data can be sent — that second
one is what stops a compromised script from exfiltrating to an attacker's server.

Start in report‑only mode and use the violation reports to discover what your
page actually loads. See
[security headers](../07-security/security-headers.md).

## Self‑host where it's practical

Self‑hosting converts a live dependency into a versioned artifact you control:
you choose when it changes, SRI becomes trivially applicable, there's no
third‑party DNS/TLS/CDN in your critical path, and no third party learns your
users' IP addresses.

> ⚖️ **Legal note:** For **fonts and other assets, self‑hosting is this knowledge
> base's standing recommendation** — a German court found that embedding Google
> Fonts, which transmitted visitors' IP addresses to a third party without
> consent, infringed the visitor's rights. The same logic applies to any embedded
> asset that phones home. See [GDPR](../10-legal-and-compliance/gdpr.md) and
> [cookies & tracking](../10-legal-and-compliance/cookies-and-tracking.md).

The trade‑off is real: you take on hosting, updating, and patching what you
self‑host. For a small, stable library that's trivial. For a complex product
(a payment element, a live chat backend) it isn't an option — which is fine,
because those are exactly the cases where the vendor's own infrastructure is
doing something you genuinely can't replicate.

## The performance cost

> ⚡ Third‑party scripts are one of the most common causes of poor
> [Core Web Vitals](../05-performance/core-web-vitals.md). They compete for the
> main thread (hurting **INP**), can block rendering (hurting **LCP**), and often
> inject banners and embeds that push content around (hurting **CLS**).

> ✅ **Do:** Load non‑critical third parties with `async` or `defer`; reserve
> space for anything that injects UI; lazy‑load embeds (video, maps, social) so
> they cost nothing until the user wants them; set a budget for third‑party bytes
> and requests and hold it. See
> [performance budgets](../05-performance/performance-budgets.md).
> ❌ **Don't:** Let a third party be a **single point of failure**. A synchronous
> script from a vendor having a bad day can hang your page. Test what your site
> does when a third‑party origin is blocked or slow — browser dev tools can block
> a domain so you can see for yourself.

## The privacy cost

Most third‑party scripts see the user's IP address, user agent, page URL, and
whatever they choose to collect — which is usually more than you assumed.

> ⚖️ **Legal note:** In the EU/UK, non‑essential scripts that store or read
> information on the device generally require **prior opt‑in consent**, and they
> must not fire before the user consents. Under CCPA/CPRA, ad‑tech scripts often
> constitute "**sharing**" for cross‑context behavioral advertising, triggering
> opt‑out obligations. Your [privacy policy](../10-legal-and-compliance/privacy-policy.md)
> must reflect what these scripts actually do, and vendors handling personal data
> on your behalf need contracts — see
> [vendors & subprocessors](../10-legal-and-compliance/vendors-and-subprocessors.md).

A consent banner that loads tracking scripts before the user answers is not
compliance theatre — it's just non‑compliance. **Test it**: open the network
panel, load the page, answer nothing, and see what fired.

## Payment pages are a special case

> 🔒 On pages that take card details, third‑party scripts are not merely a risk
> — they're a **PCI DSS eligibility question.** The SAQ A published in January
> 2025 requires merchants to confirm their site is **not susceptible to script
> attacks**, and PCI DSS Requirements 6.4.3 and 11.6.1 cover managing payment‑page
> scripts and detecting unauthorized changes to them. An inventory plus change
> detection is the evidence. See [PCI compliance](../11-payments/pci-compliance.md).

The strongest position on a payment page is the smallest one: your payment
provider's hosted fields, and as close to nothing else as you can manage.

## Review them on a schedule

Third‑party scripts rot quietly. Add a periodic review to your
[maintenance plan](../09-maintenance/maintenance-plan.md):

- [ ] Re‑derive the live inventory from the network panel; compare to your record.
- [ ] **Remove what no longer has a purpose or an owner.** This is usually the
      single biggest win, and it's free.
- [ ] Confirm consent gating still works — test with consent refused.
- [ ] Check SRI hashes still match and versioned URLs haven't drifted.
- [ ] Re‑check your CSP still constrains `script-src` and `connect-src`.
- [ ] Verify payment and login pages carry the minimum set.
- [ ] Confirm each vendor still has a current contract and a known data scope.

## Primary sources

- [MDN — Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)
  and the [W3C SRI specification](https://www.w3.org/TR/SRI/) — the `integrity`
  attribute, supported elements, and the CORS requirement.
- [MDN — Cross‑Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
  — why `crossorigin` is needed alongside `integrity`.
- [PCI SSC — SAQ A updates](https://blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a)
  — the payment‑page script requirements referenced above.
