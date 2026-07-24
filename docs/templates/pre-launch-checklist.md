# Pre‑Launch Checklist

A cross‑discipline gate to run **before** a site goes live. Copy it into an issue
and check items off. Adapt to your project's scale — a brochure site skips some
of this, an e‑commerce app needs all of it and more. Each area links to the
relevant guidance.

## Content & functionality
- [ ] All pages present; no placeholder/"lorem ipsum" content left.
- [ ] Spelling and grammar reviewed.
- [ ] All links work (internal and external); no dead links.
- [ ] Forms submit correctly and send to the right place.
- [ ] Error, empty, and loading states behave correctly.
- [ ] Search, filters, and interactive features work.
- [ ] Contact details and business info are correct.
- [ ] 404 (and other error) pages are helpful and on‑brand.

## Cross‑browser & device
- [ ] Tested on current major browsers.
- [ ] Tested on real mobile devices (small + large), tablet, desktop.
- [ ] Tested both orientations and at 200% zoom.
  See [responsive design](../02-design-and-ux/responsive-design.md).

## Accessibility ♿
- [ ] Automated scan (axe/Lighthouse/WAVE) — no critical issues.
- [ ] Keyboard‑only walkthrough of key journeys passes.
- [ ] Screen‑reader check of key pages passes.
- [ ] Color contrast meets WCAG AA; nothing relies on color alone.
- [ ] Images have appropriate alt text; forms have labels.
- [ ] Accessibility statement published (if applicable).
  See [accessibility checklist](../04-accessibility/accessibility-checklist.md).

## Performance ⚡
- [ ] Core Web Vitals within targets (LCP, INP, CLS).
- [ ] Images optimized, right‑sized, and lazy‑loaded (except hero/LCP).
- [ ] CSS/JS minified; unused code removed.
- [ ] Caching and CDN configured.
- [ ] Meets the performance budget.
  See [Performance](../05-performance/README.md).

## SEO
- [ ] Unique, descriptive `<title>` and meta description per page.
- [ ] Logical heading structure.
- [ ] `sitemap.xml` present and submitted; `robots.txt` correct.
- [ ] **No leftover `noindex` from staging** (critical!).
- [ ] **No accidental `Disallow: /`** in robots.txt (critical!).
- [ ] 301 redirects in place for any old/changed URLs.
- [ ] Canonical tags and single preferred domain set.
- [ ] Analytics / Search Console configured (with consent handling).
  See [technical SEO](../06-seo/technical-seo.md).

## Security 🔒
- [ ] HTTPS enforced everywhere; HTTP redirects to HTTPS.
- [ ] TLS certificate valid, covers all hostnames, and auto‑renews.
- [ ] Security headers set (HSTS, CSP, nosniff, frame protection, etc.).
- [ ] No secrets in the codebase or front‑end; secrets in a proper store.
- [ ] Dependencies updated; no known critical vulnerabilities.
- [ ] Admin interfaces protected (MFA, restricted access).
- [ ] Default credentials changed; verbose errors disabled in production.
- [ ] Input validation and parameterized queries in place.
  See [Security](../07-security/README.md).

## Legal & compliance ⚖️
- [ ] **Privacy policy** published and linked (footer + collection points).
- [ ] **Cookie/tracking consent** implemented; non‑essential trackers blocked
      until consent (EU/UK) / opt‑out provided (US).
- [ ] **No non‑essential trackers fire before consent** (verify in dev tools).
- [ ] **Terms of Service** published (esp. for accounts/e‑commerce/UGC).
- [ ] All images, fonts, and media are **properly licensed**; records kept.
- [ ] E‑commerce: pricing, taxes/fees, shipping, returns, and cancellation
      rights disclosed; checkout free of dark patterns.
- [ ] Email sign‑ups use proper consent and unsubscribe.
- [ ] Breach‑response and data‑subject‑request processes ready.
  See [Legal & Compliance](../10-legal-and-compliance/README.md).

## Infrastructure & operations
- [ ] Hosting sized and configured for expected traffic.
- [ ] Domain registered/renewed and owned by the right party; auto‑renew on.
- [ ] DNS records correct; TTLs sensible for the cutover.
- [ ] **Backups configured and a restore has been tested.**
- [ ] Monitoring and alerting live (uptime, errors, cert/domain expiry).
- [ ] Deploy pipeline works; **rollback path tested.**
- [ ] Staging removed from search indexing / access.
  See [Deployment](../08-deployment-and-devops/README.md) and
  [Maintenance](../09-maintenance/README.md).

## Ownership & handover
- [ ] Client/owner controls their own accounts (domain, hosting, DNS,
      analytics).
- [ ] Documentation delivered (setup, deploy, runbooks).
- [ ] Maintenance responsibility assigned and agreed.
  See [roles & responsibilities](../00-getting-started/roles-and-responsibilities.md).

## Launch day
- [ ] Deploy during a low‑traffic window with people available.
- [ ] Verify the live site end‑to‑end after deploy (HTTPS, key journeys, forms).
- [ ] Confirm analytics and monitoring are receiving data.
- [ ] Watch error/uptime dashboards for the first hours.
- [ ] Rollback plan ready if something's wrong.

> 💡 Don't treat launch as the finish line. The moment it's live, the
> [maintenance phase](../09-maintenance/README.md) begins.
