# Testing

Testing is how you find problems before your users do. "It works on my machine"
is not testing. A website needs several *kinds* of testing, each catching
different classes of problem, ideally automated so they run every time.

## The kinds of testing a website needs

### Functional / behavioral
Does the site do what it's supposed to?

- **Unit tests** — small pieces of logic in isolation (fast, numerous).
- **Integration tests** — parts working together (e.g., form → API → database).
- **End‑to‑end (E2E) tests** — real user journeys through the actual UI (e.g.,
  "sign up, log in, place an order"). Slower but high‑confidence.

A common guideline (the "testing pyramid"): many fast unit tests, fewer
integration tests, and a small number of critical E2E tests.

### Cross‑browser and cross‑device
Your site must work across the browsers and devices your audience uses. Test on
real devices and current versions of major browsers, not just your own setup.
See [responsive design](../02-design-and-ux/responsive-design.md).

### Accessibility testing ♿
Automated tools catch a portion of issues; the rest require manual testing.

- **Automated** (e.g., axe, Lighthouse, WAVE) — catches many contrast, missing
  label, and structure issues. Necessary but *not sufficient* — automation finds
  only a minority of real accessibility barriers.
- **Keyboard** — can you reach and operate everything with only a keyboard, in a
  logical order, with visible focus?
- **Screen reader** — does the page make sense read aloud?
- **Zoom/reflow** — usable at 200%+ zoom.

See [testing accessibility](../04-accessibility/testing-accessibility.md).

### Performance testing ⚡
Measure real‑world loading and responsiveness:

- Lab tools (e.g., Lighthouse, WebPageTest) for controlled measurement.
- Core Web Vitals (LCP, INP, CLS) — see [Performance](../05-performance/README.md).
- Load/stress testing for expected (and peak) traffic if relevant.

### Security testing 🔒
- Automated dependency scanning for known vulnerabilities.
- Static analysis and security linters.
- For higher‑risk apps, penetration testing.
See [Security](../07-security/README.md).

## Automate it

Manual testing doesn't scale and gets skipped under deadline pressure. Automate
what you can and run it in **CI** on every change, so regressions are caught
immediately. See [CI/CD](../08-deployment-and-devops/ci-cd.md).

> ✅ **Do:**
> - Add a test when you fix a bug, so it can't silently return (regression
>   test).
> - Test the unhappy paths: invalid input, empty states, network failure,
>   permissions.
> - Keep tests fast and reliable — flaky tests get ignored, defeating the
>   purpose.

> ❌ **Don't:**
> - Chase 100% coverage as a vanity metric; test what matters and what's risky.
> - Rely only on automated accessibility tools — they miss most real issues.
> - Ship "small changes" untested. Small changes cause plenty of outages.

## Test environments

Do serious testing in a **staging** environment that mirrors production, using
production‑like (but not real personal) data. Never test destructive operations
against live data. See [environments](../08-deployment-and-devops/environments.md).

> ⚖️ **Legal note:** Don't use real customers' personal data in test/staging
> environments casually — it expands where sensitive data lives and your
> exposure if it leaks. Use synthetic or properly anonymized data. See
> [GDPR](../10-legal-and-compliance/gdpr.md).

## What "done" means

A change is done when it works, is tested, passes review, and doesn't regress
accessibility, performance, or security. "It renders on my screen" is the
beginning of testing, not the end.
