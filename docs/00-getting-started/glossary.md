# Glossary

Plain‑language definitions of terms used throughout this knowledge base. Terms
are grouped loosely by area. When a term has a dedicated page, it links there.

## General web

- **Client / server** — The *client* is the user's browser; the *server* is the
  machine that sends it pages and data.
- **Front end / back end** — Front end is what runs in the browser (HTML, CSS,
  JavaScript). Back end is what runs on the server (application logic, database).
- **Static vs. dynamic site** — A *static* site serves pre‑built files; a
  *dynamic* site generates pages on request, often from a database.
- **CMS (Content Management System)** — Software (e.g., WordPress) that lets
  non‑developers create and edit content.
- **Framework** — A reusable foundation for building sites/apps (e.g., React,
  Django, Rails).
- **API (Application Programming Interface)** — A defined way for programs to
  talk to each other, often over HTTP.

## Infrastructure & delivery

- **DNS (Domain Name System)** — The internet's address book; translates a
  domain like `example.com` into a server IP address.
- **Hosting** — Where your site's files and services run. Can be shared,
  virtual private server (VPS), cloud, serverless, or a managed platform.
- **CDN (Content Delivery Network)** — A geographically distributed cache that
  serves content from a location near each user for speed and resilience.
- **TLS/SSL** — The encryption that makes `https://` secure. "SSL certificate"
  is the common (if technically dated) name for the certificate that enables it.
- **Environment** — A copy of the site for a purpose: *development*, *staging*
  (a production‑like rehearsal), *production* (the live site).

## Quality & compliance

- **WCAG (Web Content Accessibility Guidelines)** — The international standard
  for web accessibility. See [Accessibility](../04-accessibility/README.md).
- **ARIA (Accessible Rich Internet Applications)** — Attributes that add
  accessibility semantics to HTML when native elements aren't enough.
- **Core Web Vitals** — Google's key performance metrics (LCP, INP, CLS). See
  [Performance](../05-performance/README.md).
- **SEO (Search Engine Optimization)** — Practices that help search engines
  find, understand, and rank your content.
- **OWASP** — The Open Worldwide Application Security Project; publishes the
  well‑known "Top 10" web security risks.

## Legal & privacy

- **PII (Personally Identifiable Information)** — Data that identifies a person
  (name, email, IP address, etc.). "Personal data" is the broader legal term.
- **Data controller / processor** — Under GDPR, the *controller* decides why and
  how personal data is used; the *processor* acts on the controller's behalf.
- **GDPR** — The EU's General Data Protection Regulation. See
  [gdpr.md](../10-legal-and-compliance/gdpr.md).
- **CCPA / CPRA** — California's consumer privacy laws. See
  [ccpa-cpra.md](../10-legal-and-compliance/ccpa-cpra.md).
- **Consent** — A user's freely given, informed agreement — the legal basis for
  many kinds of tracking and data use.
- **ToS / T&C** — Terms of Service / Terms & Conditions: the contract between a
  site and its users.
- **DPA (Data Processing Agreement)** — A contract governing how a processor
  handles personal data on a controller's behalf.

## Development & operations

- **Version control / Git** — Tools that track changes to code over time and let
  teams collaborate. See [version control](../03-development-best-practices/version-control.md).
- **CI/CD** — Continuous Integration / Continuous Delivery: automated building,
  testing, and deploying. See [ci-cd.md](../08-deployment-and-devops/ci-cd.md).
- **Dependency** — External code your project relies on (a library, package, or
  plugin). Dependencies must be kept updated for security.
- **Backup** — A recoverable copy of your data/site. Only a *tested* backup
  counts. See [backups](../09-maintenance/backups-and-disaster-recovery.md).
- **Uptime / SLA** — Uptime is the % of time a site is available; an SLA
  (Service Level Agreement) is a promise about it.
- **Incident** — An unplanned disruption or security event. See
  [incident response](../09-maintenance/incident-response.md).

## Performance & caching

- **LCP / INP / CLS** — Largest Contentful Paint (loading), Interaction to Next
  Paint (responsiveness), Cumulative Layout Shift (visual stability).
- **Caching** — Storing a copy of content so it doesn't have to be regenerated
  or refetched. Happens in browsers, CDNs, and servers.
- **Lazy loading** — Deferring the loading of off‑screen assets until they're
  needed.
- **Minification / bundling** — Shrinking and combining code files to reduce
  what the browser must download.

*Missing a term? Add it — see [CONTRIBUTING.md](../../CONTRIBUTING.md).*
