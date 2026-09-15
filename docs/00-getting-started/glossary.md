# Glossary

A comprehensive, self-contained reference for the terminology used across this
knowledge base. Each entry explains **what the term means and why it matters** —
enough to build a working mental model, not just expand an acronym. Entries are
intentionally standalone: you shouldn't have to read another page to understand a
definition, though most link to fuller treatment where it exists.

Terms are grouped by area. Use your browser's find (Ctrl/Cmd‑F) to jump to one.

> This glossary is meant to *reinforce* the main documentation, not replace it.
> Individual pages still define important terms where they're introduced; this
> page gathers them in one place so the whole vocabulary is learnable at a
> glance.

---

## Web fundamentals & architecture

- **Client / server** — The **client** is the program requesting content (usually
  the user's web browser); the **server** is the machine that receives requests
  and sends back pages and data. Nearly all web activity is a conversation
  between the two. *Why it matters:* where code runs (client vs. server) has huge
  security and performance consequences — e.g., anything on the client is visible
  to the user, so secrets belong on the server.
- **Front end / back end** — The **front end** is everything running in the
  browser (HTML, CSS, JavaScript) that the user sees and interacts with. The
  **back end** is the server‑side application logic, databases, and APIs the user
  never sees directly. *Why it matters:* the two have different skills, risks, and
  failure modes; "full‑stack" means working across both.
- **HTML / CSS / JavaScript** — The three core browser languages: **HTML**
  structures content (headings, links, forms), **CSS** styles its appearance
  (layout, color, type), and **JavaScript** adds behavior and interactivity.
  *Why it matters:* keeping structure, style, and behavior in their proper layers
  makes sites more robust, accessible, and maintainable.
- **Semantic HTML** — Using HTML elements according to their **meaning** (a
  `<button>` for a button, `<nav>` for navigation) rather than generic `<div>`s
  styled to look right. *Why it matters:* it improves accessibility, SEO, and
  resilience simultaneously, usually for free. See
  [semantic HTML](../03-development-best-practices/semantic-html.md).
- **Static vs. dynamic site** — A **static** site serves pre‑built files that look
  the same to everyone; a **dynamic** site generates pages on request, often
  personalized and drawn from a database. *Why it matters:* static sites are
  faster, cheaper, and safer; dynamic sites are more flexible. The choice shapes
  cost, security, and hosting.
- **Static site generator (SSG) / Jamstack** — Tooling that pre‑builds a site into
  static files (optionally adding dynamic features via APIs/serverless), typically
  served from a CDN. *Why it matters:* it combines much of static's speed and
  safety with dynamic capabilities. See
  [choosing a tech stack](../01-planning-and-strategy/choosing-a-tech-stack.md).
- **Rendering (SSR / CSR / SSG)** — *Where and when* HTML is produced:
  **server‑side rendering** builds each page on the server per request;
  **client‑side rendering** ships mostly‑empty HTML that JavaScript fills in in
  the browser; **static site generation** builds pages ahead of time. *Why it
  matters:* client‑side‑only rendering can hide content from search engines and
  slow the first paint. See [technical SEO](../06-seo/technical-seo.md).
- **CMS (Content Management System)** — Software (e.g., WordPress, Drupal) that
  separates content from code and lets non‑developers create and edit it through
  an admin interface. *Why it matters:* it empowers editors but is a standing
  **security and maintenance commitment** — most CMS breaches come from unpatched
  plugins. See [dependency management](../09-maintenance/dependency-management.md).
- **Headless CMS** — A CMS that manages content and exposes it via an API, leaving
  presentation to a separate front end. *Why it matters:* it pairs editor‑friendly
  content management with modern static/Jamstack front ends.
- **Framework / library** — Reusable, third‑party code you build on: a
  **framework** provides an overall structure you plug into (e.g., Django, Rails,
  React); a **library** is a focused tool you call as needed. *Why it matters:*
  they accelerate building but every one is a dependency someone must understand
  and keep patched for years.
- **API (Application Programming Interface)** — A defined contract that lets
  programs talk to each other, commonly over HTTP. *Why it matters:* APIs are how
  front ends, back ends, and third‑party services integrate — and each is an
  attack surface that must enforce its own security.
- **Progressive enhancement** — Building a baseline experience that works
  everywhere, then layering on enhancements for capable browsers. *Why it
  matters:* it keeps sites usable and accessible even when JavaScript fails or a
  device is limited.

## Infrastructure, hosting & delivery

- **Domain / registrar** — A **domain** (e.g., `example.com`) is the human‑readable
  address you *rent* through a **registrar** and renew periodically. *Why it
  matters:* the owner should control the registrar account; a lapsed domain causes
  a total, sudden outage. See [domains & hosting](../01-planning-and-strategy/domains-and-hosting.md).
- **DNS (Domain Name System)** — The internet's address book, translating a domain
  name into the server IP address behind it. *Why it matters:* DNS is a single
  point of failure for the whole site, and misconfiguration or expiry takes
  everything down at once. See [DNS, domains & SSL](../08-deployment-and-devops/domains-dns-ssl.md).
- **DNS records (A, AAAA, CNAME, MX, TXT, NS, CAA)** — The individual entries that
  point a domain at services: **A/AAAA** map to IP addresses, **CNAME** aliases one
  name to another, **MX** routes email, **TXT** holds verification and email‑auth
  data, **NS** names the authoritative servers, **CAA** limits who may issue
  certificates. *Why it matters:* knowing which record does what makes migrations
  and email setup far less error‑prone.
- **SPF / DKIM / DMARC** — Email‑authentication DNS records that prove mail from
  your domain is legitimate and make spoofing harder. *Why it matters:* they
  protect your deliverability and reputation, and matter for
  [email marketing](../10-legal-and-compliance/email-marketing-law.md).
- **Hosting** — Where your site's files and services actually run — options range
  from shared hosting and VPS to cloud (IaaS), managed platforms (PaaS),
  serverless, and static+CDN. *Why it matters:* the model determines how much you
  must operate, secure, and pay for. See [infrastructure](../08-deployment-and-devops/infrastructure.md).
- **CDN (Content Delivery Network)** — A geographically distributed network of
  caching servers that serve content from a location near each user. *Why it
  matters:* it improves speed, absorbs traffic spikes, adds resilience, and often
  provides TLS and DDoS protection. See [caching & CDNs](../05-performance/caching-and-cdn.md).
- **TLS / SSL** — **Transport Layer Security** (the modern successor to SSL) is the
  encryption that powers `https://`. An **SSL/TLS certificate** proves a site's
  identity and enables the encryption. *Why it matters:* HTTPS is now the baseline
  for security, trust, SEO, and modern browser features. See
  [HTTPS & TLS](../07-security/https-and-tls.md).
- **HTTPS** — HTTP carried over TLS, so the connection is encrypted,
  tamper‑resistant, and authenticated. *Why it matters:* browsers flag non‑HTTPS
  sites as "Not secure"; every site should be HTTPS‑only.
- **HSTS (HTTP Strict Transport Security)** — A response header instructing
  browsers to only ever use HTTPS for your domain. *Why it matters:* it prevents
  downgrade attacks. See [security headers](../07-security/security-headers.md).
- **Environment (development / staging / production)** — A separate copy of the
  site for a purpose: **development** (where you build), **staging** (a
  production‑like rehearsal for testing), **production** (the live site). *Why it
  matters:* proving changes in staging before production is how you ship safely.
  See [environments](../08-deployment-and-devops/environments.md).
- **Infrastructure as Code (IaC)** — Defining servers, networks, and services in
  version‑controlled code (e.g., Terraform) rather than clicking around a console.
  *Why it matters:* it makes setups repeatable, reviewable, documented, and
  recoverable after a disaster.
- **Container** — A package of an application with its dependencies so it runs
  identically everywhere, solving "works on my machine." **Orchestration** (e.g.,
  Kubernetes) manages many containers at scale. *Why it matters:* containers bring
  consistency, but orchestration adds complexity most small sites don't need.
- **Serverless / PaaS / IaaS** — Cloud service models by how much you manage:
  **IaaS** gives raw infrastructure you run; **PaaS** manages the platform so you
  bring only your app; **serverless** runs your code on demand with no servers to
  manage. *Why it matters:* moving up the stack trades control for less
  operational burden.
- **Data residency** — Where data physically lives geographically. *Why it
  matters:* data‑protection laws restrict international transfers, so region choice
  can be a legal decision. See [GDPR](../10-legal-and-compliance/gdpr.md).

## Planning, UX & design

- **Requirements (functional / non‑functional)** — **Functional** requirements
  describe *what the system does*; **non‑functional** describe *how well* (speed,
  accessibility, security, uptime). *Why it matters:* the non‑functional ones are
  most often forgotten and cause the worst late surprises. See
  [requirements gathering](../01-planning-and-strategy/requirements-gathering.md).
- **Information architecture (IA)** — The practice of organizing and labeling
  content so people can find things and know where they are (sitemaps,
  navigation, taxonomy, URL structure). *Why it matters:* bad IA is why users
  can't find the contact page; fixing it after launch means broken links and lost
  SEO. See [information architecture](../01-planning-and-strategy/information-architecture.md).
- **Sitemap (planning vs. XML)** — A **planning sitemap** is a diagram of a site's
  pages and hierarchy; an **XML sitemap** (`sitemap.xml`) is a machine‑readable
  list of URLs submitted to search engines. *Why it matters:* they're different
  artifacts for different audiences (humans planning vs. crawlers indexing).
- **Wireframe** — A low‑fidelity layout sketch showing structure and content
  priority before visual design. *Why it matters:* it's cheap to iterate on
  structure before committing to visuals.
- **UX vs. UI** — **UX (user experience)** is how a site *works* — flows, clarity,
  findability; **UI (user interface)** is how it *looks and feels* — layout, color,
  components. *Why it matters:* great UI on bad UX is lipstick on a maze; get the
  experience right first. See [UX principles](../02-design-and-ux/ux-principles.md).
- **Usability heuristics** — Well‑established rules of thumb (e.g., Nielsen's ten)
  for spotting usability problems, like "keep users informed of system status."
  *Why it matters:* they turn "this feels off" into specific, fixable issues.
- **Design system** — A documented, reusable set of components, patterns, and
  standards that keep a product consistent and faster to build. *Why it matters:*
  it enforces consistency and lets you build accessibility in once and inherit it
  everywhere. See [design systems](../02-design-and-ux/design-systems.md).
- **Design tokens** — Named, central values for design decisions (e.g.,
  `color-primary`, `space-4`) shared by design and code. *Why it matters:* change
  the token, change everywhere — the key to theming, dark mode, and consistency.
- **Component library** — A collection of reusable, well‑defined UI building blocks
  (buttons, inputs, modals) with defined states and behavior. *Why it matters:* one
  accessible, well‑built component benefits every place it's used (and one bad one
  spreads the same way).
- **Content strategy** — Planning what content you need, who creates and maintains
  it, and to what standard. *Why it matters:* content is what users come for, yet
  it's routinely treated as a last‑minute afterthought that breaks the design.
- **Dark pattern (deceptive design)** — An interface trick that manipulates users
  into unintended actions (pre‑checked consent, hidden costs, hard‑to‑find
  cancellation). *Why it matters:* beyond eroding trust, many are now **illegal**
  under privacy and consumer law. See
  [UX principles](../02-design-and-ux/ux-principles.md).
- **MoSCoW** — A prioritization scheme: **Must, Should, Could, Won't (this time).**
  *Why it matters:* the explicit "Won't" list is the most valuable tool for
  managing scope and expectations.
- **User story** — A requirement framed from the user's view: "As a [role], I want
  [goal] so that [benefit]." *Why it matters:* it keeps focus on outcomes rather
  than features.
- **MVP (Minimum Viable Product)** — The smallest version that delivers real value
  and can launch. *Why it matters:* protecting the MVP keeps scope from ballooning
  and gets you to real feedback sooner.
- **Scope creep** — The quiet accumulation of "small" additions that blow up
  timelines and budgets. *Why it matters:* it's the top killer of web projects;
  managing it requires a written scope and a change process.
- **Total cost of ownership (TCO)** — The full lifetime cost of a site, including
  hosting, maintenance, updates, and compliance — not just the build. *Why it
  matters:* a cheap build with expensive upkeep can cost more overall. See
  [budgeting & scoping](../01-planning-and-strategy/budgeting-and-scoping.md).

## Accessibility

- **Web accessibility (a11y)** — Designing and building so that people with
  disabilities (and everyone else) can use your site. *Why it matters:* it's an
  ethical baseline, an increasingly common legal requirement, and it overlaps with
  good UX and SEO. See [Accessibility](../04-accessibility/README.md).
- **WCAG (Web Content Accessibility Guidelines)** — The international standard for
  web accessibility, structured around four principles (**POUR**: Perceivable,
  Operable, Understandable, Robust) and three conformance levels (**A, AA, AAA**).
  *Why it matters:* "make it accessible" almost always means "conform to WCAG,"
  usually **Level AA**. See [WCAG overview](../04-accessibility/wcag-overview.md).
- **Conformance level (A / AA / AAA)** — WCAG's tiers of stringency: **A** removes
  essential barriers, **AA** addresses the major common ones (the standard target),
  **AAA** is enhanced and often impractical site‑wide. *Why it matters:* laws and
  contracts typically require **AA**.
- **ARIA (Accessible Rich Internet Applications)** — HTML attributes (roles,
  states, properties) that convey accessibility information for custom widgets when
  native HTML can't. *Why it matters:* the first rule is "don't use ARIA if native
  HTML will do" — bad ARIA is worse than none. See
  [ARIA & semantics](../04-accessibility/aria-and-semantics.md).
- **Assistive technology (AT)** — Tools people use to access content, such as
  **screen readers** (which read the page aloud), magnifiers, and switch devices.
  *Why it matters:* your HTML semantics are what AT relies on to convey meaning.
- **Screen reader** — Software (e.g., NVDA, VoiceOver, JAWS) that reads a page
  aloud and lets users navigate by headings, landmarks, and links. *Why it
  matters:* testing with one reveals problems no automated tool catches.
- **Alt text (alternative text)** — A text description of a meaningful image, read
  by screen readers and shown if the image fails to load (decorative images get
  empty `alt=""`). *Why it matters:* it's both an accessibility requirement and an
  SEO signal.
- **Keyboard navigation / focus** — Operating a site using only the keyboard, with
  a visible **focus indicator** showing which element is active. *Why it matters:*
  many users can't use a mouse; keyboard operability is a core WCAG requirement and
  a quick test that finds many bugs.
- **Landmark** — A structural region of a page (`header`, `nav`, `main`, `footer`)
  that lets assistive‑tech users jump around. *Why it matters:* landmarks plus a
  logical heading outline are among the highest‑impact accessibility wins.
- **Skip link** — A "skip to main content" link that lets keyboard users bypass
  repeated navigation. *Why it matters:* without it, keyboard users must tab
  through the whole menu on every page.
- **Color contrast** — The luminance difference between text and its background,
  measured as a ratio (WCAG AA wants at least **4.5:1** for normal text). *Why it
  matters:* low contrast excludes users with low vision and fails common legal
  standards.
- **Accessibility statement** — A public page describing your conformance, known
  limitations, and how to report barriers. *Why it matters:* some laws require it,
  and it demonstrates good‑faith effort. See
  [accessibility law](../10-legal-and-compliance/accessibility-law.md).
- **Accessibility overlay** — A third‑party widget claiming to auto‑fix
  accessibility. *Why it matters:* overlays are widely criticized as ineffective
  and have **not** reliably prevented lawsuits — there's no substitute for building
  accessibly.

## Performance

- **Core Web Vitals** — Google's user‑centric performance metrics: **LCP** (Largest
  Contentful Paint — loading), **INP** (Interaction to Next Paint —
  responsiveness), and **CLS** (Cumulative Layout Shift — visual stability). *Why
  it matters:* they measure real experience and feed search ranking. See
  [Core Web Vitals](../05-performance/core-web-vitals.md).
- **LCP / INP / CLS** — **LCP** = time until the largest content element renders
  (good ≤ 2.5s); **INP** = how quickly the page responds to interactions (good ≤
  200ms); **CLS** = how much the layout unexpectedly shifts (good ≤ 0.1). *Why it
  matters:* they're the concrete targets to optimize toward.
- **Lab data vs. field data** — **Lab** data comes from a controlled test on a
  simulated device (great for debugging and catching regressions); **field** data
  comes from real users' sessions (what Google actually ranks on). *Why it
  matters:* the two often differ; you need both. See
  [Core Web Vitals](../05-performance/core-web-vitals.md).
- **RUM (Real‑User Monitoring)** — Collecting performance data from real visitors
  over time. *Why it matters:* it reflects the true spread of devices and networks,
  unlike a single lab run.
- **Lighthouse / PageSpeed Insights** — Free Google tools that audit a page's
  performance (and more): **Lighthouse** runs lab audits locally; **PageSpeed
  Insights** combines lab and field data with suggestions. *Why it matters:* they
  turn "it feels slow" into specific, prioritized fixes. See
  [Search Console & webmaster tools](../06-seo/search-console.md).
- **Caching** — Storing a copy of content so it needn't be regenerated or
  refetched, at layers from the browser to the CDN to the server. *Why it
  matters:* the fastest request is the one you never make — caching is a top
  performance and resilience lever. See [caching & CDNs](../05-performance/caching-and-cdn.md).
- **Cache busting / fingerprinting** — Giving a file a content‑based name (e.g.,
  `app.9f3a2c.js`) so it can be cached "forever" yet updates instantly when its
  contents change. *Why it matters:* it lets you cache aggressively without serving
  stale files.
- **Lazy loading** — Deferring the loading of off‑screen assets until they're
  needed (e.g., `loading="lazy"` on below‑the‑fold images). *Why it matters:* it
  cuts initial page weight — but never lazy‑load the LCP image.
- **Minification / bundling / compression** — **Minification** strips whitespace
  and comments from code; **bundling** combines files; **compression** (gzip/
  Brotli) shrinks what's sent over the wire. *Why it matters:* together they reduce
  bytes and requests the browser must handle.
- **Code splitting** — Breaking a JavaScript bundle so each page loads only the
  code it needs. *Why it matters:* JavaScript is the most expensive asset per byte,
  and shipping less of it improves responsiveness (INP).
- **Render‑blocking resource** — CSS or JavaScript that must load before the
  browser can display the page. *Why it matters:* render‑blockers delay the first
  paint and hurt LCP; defer or inline‑critical them.
- **Responsive images (`srcset` / `sizes`)** — Markup that lets the browser pick an
  appropriately sized image per device. *Why it matters:* it stops phones
  downloading desktop‑sized images — usually the biggest, easiest performance win.
- **Performance budget** — A committed limit (page weight, metric thresholds) you
  measure against continuously. *Why it matters:* without one, performance quietly
  erodes with every added feature. See [performance budgets](../05-performance/performance-budgets.md).
- **Third‑party script** — Externally hosted code you embed (analytics, chat, ads,
  embeds). *Why it matters:* you don't control its size, speed, or privacy
  behavior — often the worst performance and consent offenders.

## SEO

- **SEO (Search Engine Optimization)** — Practices that help search engines find,
  understand, and rank your content. *Why it matters:* much of good SEO is simply
  good web development; there are no legitimate shortcuts. See [SEO](../06-seo/README.md).
- **Crawling / indexing / ranking** — The three things search engines do:
  **crawl** (discover pages), **index** (understand and store them), and **rank**
  (order them for a query). *Why it matters:* SEO is about not blocking the first
  two and earning the third by being useful.
- **`robots.txt`** — A file that requests which paths crawlers may or may not
  crawl. *Why it matters:* a stray `Disallow: /` can hide your whole site — and it
  is *not* a security control (it's public and advisory).
- **`noindex`** — A tag/header telling search engines not to index a page. *Why it
  matters:* a leftover `noindex` from staging is a classic, catastrophic way to
  vanish from search. See [technical SEO](../06-seo/technical-seo.md).
- **XML sitemap** — A machine‑readable list of your important URLs submitted to
  search engines. *Why it matters:* it speeds discovery (though it doesn't
  guarantee indexing).
- **Canonicalization / canonical tag** — Telling search engines which URL is the
  preferred version when the same content is reachable at several URLs
  (`<link rel="canonical">`). *Why it matters:* it prevents duplicate content from
  splitting or confusing your rankings.
- **301 redirect** — A permanent redirect from an old URL to a new one that passes
  ranking signals and keeps links working. *Why it matters:* it's how you change or
  retire URLs without losing traffic — essential for any migration.
- **Title tag / meta description** — The `<title>` is the clickable headline in
  results and a strong ranking signal; the meta description is the snippet beneath
  it (affects click‑through, not ranking). *Why it matters:* they're cheap,
  per‑page wins for visibility and clicks. See [on‑page SEO](../06-seo/on-page-seo.md).
- **Structured data / schema / rich results** — Machine‑readable markup (using the
  **Schema.org** vocabulary, usually as **JSON‑LD**) that tells engines what your
  content *means* and can earn enhanced **rich results** (ratings, FAQs). *Why it
  matters:* it improves comprehension and can boost click‑through — but faking it
  invites penalties. See [structured data](../06-seo/structured-data.md).
- **Search Console / webmaster tools** — A free, first‑party dashboard (Google
  Search Console; Bing Webmaster Tools) showing how a search engine sees your site
  — indexing, queries, errors, penalties. *Why it matters:* it's the authoritative
  view no third‑party tool can match, and a core maintenance surface. See
  [Search Console](../06-seo/search-console.md).
- **Manual action** — A penalty applied by a *human reviewer* at a search engine
  for violating guidelines, surfaced in Search Console. *Why it matters:* it can
  bury or remove your site; it's distinct from an algorithmic ranking drop (which
  isn't a penalty).
- **E‑E‑A‑T** — Google's quality lens: **Experience, Expertise, Authoritativeness,
  Trustworthiness.** *Why it matters:* it especially affects "your money or your
  life" topics (health, finance, safety), where credibility signals matter most.
- **Search intent** — The actual goal behind a query. *Why it matters:* modern
  search rewards content that answers the intent, not pages stuffed with keywords.
- **Keyword research** — Learning what terms your audience searches and how they
  phrase them. *Why it matters:* it shapes genuinely useful content — as input to
  writing, not as phrases to cram in.
- **Open Graph** — Metadata tags controlling how a page appears when shared on
  social platforms (title, description, image). *Why it matters:* it improves
  click‑through and presentation of shared links.
- **Link rot** — The steady breakage of links over time as pages move or
  disappear. *Why it matters:* dead links erode trust and SEO; catching them is an
  ongoing maintenance task. See [content updates](../09-maintenance/content-updates.md).
- **Backlink** — A link from another site to yours. *Why it matters:* genuine,
  earned links are a ranking signal; buying spammy ones invites penalties.
- **`hreflang`** — Annotations that tell search engines how the language/region
  versions of a page relate. *Why it matters:* on multilingual/multi‑region sites
  they serve the right version to each user and stop the versions competing as
  duplicates. See [technical SEO](../06-seo/technical-seo.md).

## Security

- **OWASP Top 10** — A widely referenced list of the most critical web application
  security risks, from the Open Worldwide Application Security Project. *Why it
  matters:* it's the standard starting point for understanding what goes wrong and
  how to prevent it. See [OWASP Top 10](../07-security/owasp-top-10.md).
- **Defense in depth** — Layering multiple security controls so no single failure
  is catastrophic. *Why it matters:* any one control can fail; layers contain the
  damage.
- **Least privilege** — Granting every user, service, and key the minimum access it
  needs. *Why it matters:* it limits how much damage a compromised account or key
  can do.
- **Authentication vs. authorization** — **Authentication (authn)** verifies *who
  you are* (login); **authorization (authz)** enforces *what you may do*
  (permissions). *Why it matters:* both are commonly broken, and authorization must
  be enforced on the **server** for every request. See
  [authentication & authorization](../07-security/authentication-and-authorization.md).
- **Broken access control** — When users can act outside their permissions (e.g.,
  viewing another user's record by changing an ID). *Why it matters:* it's one of
  the most common and damaging web vulnerabilities — always verify object
  ownership.
- **Injection (SQL injection, XSS)** — Attacks where untrusted input is
  interpreted as code: **SQL injection** manipulates database queries; **XSS
  (cross‑site scripting)** injects malicious scripts into pages. *Why it matters:*
  the fix is foundational — validate input, use parameterized queries, and encode
  output.
- **CSRF (Cross‑Site Request Forgery)** — Tricking a logged‑in user's browser into
  making an unwanted request. *Why it matters:* it's defended with anti‑CSRF tokens
  and `SameSite` cookies.
- **CORS (Cross‑Origin Resource Sharing)** — HTTP headers by which a server tells
  the browser which *other* origins may read its responses, relaxing the default
  same‑origin policy. *Why it matters:* it's the one security header that **grants**
  access rather than restricting it, so misconfiguring it (a wildcard with
  credentials, or blindly reflecting the `Origin` header) opens your API to every
  site on the internet. It also protects browsers only — it is not server‑side
  access control. See [security headers](../07-security/security-headers.md).
- **Preflight request** — An automatic `OPTIONS` request a browser sends before a
  non‑simple cross‑origin request, asking the server whether the real request is
  allowed. *Why it matters:* a missing or wrong preflight response is the usual
  cause of a cross‑origin call that works in one tool and fails in the browser.
- **SRI (Subresource Integrity)** — An `integrity` attribute holding a
  cryptographic hash of a script or stylesheet, which the browser verifies before
  running it. *Why it matters:* it's the defence against a third‑party file being
  altered after you linked to it; on a mismatch the browser refuses to load the
  resource. Requires the `crossorigin` attribute for cross‑origin files. See
  [third‑party scripts](../03-development-best-practices/third-party-scripts.md).
- **Passkey** — A public‑key credential stored on a user's device or password
  manager and used via **WebAuthn** instead of a password. *Why it matters:* there
  is no shared secret to steal, and because the credential is scoped to your
  origin it is **phishing‑resistant by construction** — a property passwords and
  one‑time codes cannot offer. See
  [authentication & authorization](../07-security/authentication-and-authorization.md).
- **WebAuthn (Web Authentication API)** — The W3C standard browser API for
  creating and using public‑key credentials, the mechanism behind passkeys. *Why
  it matters:* it's the specification your library or identity provider
  implements, and the vocabulary ("discoverable credential", "relying party") you
  will meet in their documentation.
- **Magecart** — The class of attack in which a compromised third‑party script
  skims card or credential data from a page. *Why it matters:* the victim site
  isn't breached itself — it merely linked to something that later turned
  hostile, which is why script inventory and integrity checking matter on payment
  and login pages. See [PCI compliance](../11-payments/pci-compliance.md).
- **Rate limiting** — Capping how many requests/actions a client can make in a
  time window. *Why it matters:* it blunts brute‑force logins, form spam, API
  abuse, and payment card‑testing — a cheap, high‑value control that's easy to
  forget. See [forms & input handling](../03-development-best-practices/forms-and-input-handling.md).
- **Form spam protection (honeypot / CAPTCHA)** — Techniques to stop bots
  submitting public forms: a **honeypot** is a hidden field real users leave
  blank; a **CAPTCHA** is a human‑verification challenge. *Why it matters:* every
  public form is attacked constantly; invisible defenses (honeypot, time trap,
  rate limiting) stop most bots without the friction/accessibility cost of a
  CAPTCHA. See [forms & input handling](../03-development-best-practices/forms-and-input-handling.md).
- **MFA (Multi‑Factor Authentication)** — Requiring a second factor (an app code, a
  hardware key) beyond a password. *Why it matters:* it makes stolen passwords far
  less useful and is one of the highest‑value protections — especially for admins.
- **Password hashing / salt** — Storing passwords as irreversible **hashes**
  (using bcrypt/scrypt/Argon2) with a unique **salt** per password, never as
  plaintext. *Why it matters:* it limits the damage if your database is stolen.
- **Encryption at rest / in transit** — Protecting data while **stored** (at rest)
  and while **moving** over the network (in transit, via TLS). *Why it matters:*
  both are needed; HTTPS covers transit, but stored sensitive data needs its own
  protection.
- **Secret** — A credential that unlocks systems: API keys, database passwords,
  tokens. *Why it matters:* leaked secrets are a leading breach cause; never commit
  them to version control or ship them to the browser. See
  [secrets management](../07-security/secrets-management.md).
- **Secrets manager / vault** — A dedicated service that stores, encrypts,
  access‑controls, and audits secrets. *Why it matters:* it's the safe alternative
  to hard‑coding credentials or keeping plaintext lists.
- **Security headers (CSP, HSTS, etc.)** — HTTP response headers that switch on
  browser protections (Content‑Security‑Policy against XSS, HSTS forcing HTTPS,
  and others). *Why it matters:* they mitigate whole classes of attack for little
  effort. See [security headers](../07-security/security-headers.md).
- **CSP (Content Security Policy)** — A header controlling which sources of
  scripts, styles, etc. the browser may load. *Why it matters:* it's a strong
  defense against XSS, though it takes care to configure without breaking things.
- **SSRF (Server‑Side Request Forgery)** — Tricking the server into making requests
  to unintended destinations (e.g., internal systems). *Why it matters:* it can
  expose internal infrastructure; restrict and validate outbound requests.
- **Supply‑chain attack** — Compromise via a dependency or its update channel
  rather than your own code. *Why it matters:* trusted components can turn
  malicious; pin versions, verify sources, and limit build‑pipeline access.
- **Threat modeling** — Systematically identifying what could go wrong and how to
  defend against it, early in design. *Why it matters:* you can't patch your way
  out of an insecure design.
- **Penetration testing (pentest)** — Authorized simulated attacks to find
  vulnerabilities before real attackers do. *Why it matters:* higher‑risk apps need
  it to validate their defenses.
- **PCI DSS (Payment Card Industry Data Security Standard)** — Security
  requirements for handling payment‑card data. *Why it matters:* using a reputable
  processor so you never touch raw card data dramatically shrinks your obligations.
  See [PCI compliance](../11-payments/pci-compliance.md).

## Development practices

- **Version control / Git** — Tools that track every change to code over time and
  let teams collaborate. **Git** is the standard. *Why it matters:* it gives you
  history, undo, collaboration, and the foundation for modern deployment. See
  [version control](../03-development-best-practices/version-control.md).
- **Commit / branch / merge / pull request** — Git building blocks: a **commit** is
  a saved snapshot with a message; a **branch** is an independent line of work; a
  **merge** combines branches; a **pull request (PR)** proposes a change for review
  before merging. *Why it matters:* they enable parallel work and reviewable
  changes.
- **Coding standards** — Agreed conventions for formatting and naming, ideally
  enforced by tools. *Why it matters:* consistency lets a team read and change code
  without friction — the specific rules matter less than following the same ones.
- **Linter / formatter** — A **linter** flags likely bugs and style issues; a
  **formatter** rewrites code to a consistent style automatically. *Why it
  matters:* they end style debates and catch problems before review. See
  [coding standards](../03-development-best-practices/coding-standards.md).
- **Code review** — Having someone examine a change before it's merged. *Why it
  matters:* it catches defects early, spreads knowledge, and keeps a codebase
  coherent — most effective on small, focused changes. See
  [code review](../03-development-best-practices/code-review.md).
- **Testing (unit / integration / E2E)** — **Unit** tests check small pieces in
  isolation; **integration** tests check parts working together; **end‑to‑end**
  tests exercise real user journeys through the UI. *Why it matters:* each catches
  different bugs; automate them so regressions are caught every time. See
  [testing](../03-development-best-practices/testing.md).
- **Regression** — A bug that reappears or a feature that breaks after a change.
  *Why it matters:* adding a test when you fix a bug stops it silently returning.
- **ADR (Architecture Decision Record)** — A short note capturing a significant
  decision, its context, and consequences. *Why it matters:* it preserves the
  *why* behind choices — the most expensive knowledge to lose. See
  [documentation](../03-development-best-practices/documentation.md).
- **CI/CD (Continuous Integration / Continuous Delivery‑Deployment)** — Automating
  build, test, and release so every change is verified and shipping is a
  push‑button (or automatic) step. *Why it matters:* it catches problems early and
  makes frequent, safe releases — including fast security patches — possible. See
  [CI/CD](../08-deployment-and-devops/ci-cd.md).
- **Feature flag** — A switch that turns a feature on or off independently of
  deploying its code. *Why it matters:* it decouples releasing from deploying and
  enables safe, gradual rollouts.

## Maintenance & operations

- **Dependency** — External code your project relies on (a library, package, or
  plugin), including the dependencies of your dependencies. *Why it matters:*
  outdated components are a top breach cause, so every dependency is a maintenance
  and security commitment. See [dependency management](../09-maintenance/dependency-management.md).
- **Backup** — A recoverable copy of your data and site. *Why it matters:* only a
  **tested** backup counts — an untested one is a hope, not a safety net. See
  [backups & disaster recovery](../09-maintenance/backups-and-disaster-recovery.md).
- **3‑2‑1 rule** — Keep **3** copies of data, on **2** types of media, with **1**
  off‑site. *Why it matters:* it survives the failure of any single system,
  location, or provider.
- **Disaster recovery (DR)** — The whole plan for restoring service after a serious
  failure — backups plus process, roles, and targets. *Why it matters:* backups are
  a component; DR is the strategy that actually gets you back online.
- **RPO / RTO** — **Recovery Point Objective** = how much data loss is acceptable
  (drives backup frequency); **Recovery Time Objective** = how fast you must be
  back online (drives restore readiness). *Why it matters:* they translate "how
  important is this site?" into concrete backup and DR investment.
- **Monitoring / observability** — Continuously watching a site's health so you
  learn about problems before users do. *Why it matters:* an unmonitored site can be
  down or breached for hours unnoticed. See [monitoring & uptime](../09-maintenance/monitoring-and-uptime.md).
- **Uptime / SLA / SLO** — **Uptime** is the percent of time a site is available;
  an **SLA (Service Level Agreement)** is a promise about it; an **SLO** is an
  internal target. *Why it matters:* "99.9%" still means ~8.8 hours of downtime a
  year — know what you're promising and relying on.
- **Alert fatigue** — When too many noisy alerts cause people to ignore them all.
  *Why it matters:* an ignored alert is worse than none; alerts must be actionable.
- **Logging** — Recording security‑ and operations‑relevant events for debugging
  and investigation. *Why it matters:* without logs, breaches and outages are far
  harder to understand — but logs can contain personal data and need protection.
- **Incident** — An unplanned disruption or security event (site down, breach,
  corruption). *Why it matters:* incidents will happen; preparation converts panic
  into procedure. See [incident response](../09-maintenance/incident-response.md).
- **Incident response** — The prepared plan for handling incidents: detect, assess,
  contain, eradicate, recover, communicate, review. *Why it matters:* the plan must
  exist *before* the incident — including who decides on breach notification.
- **Post‑mortem** — A blameless review after an incident: what happened, why, and
  what will prevent recurrence. *Why it matters:* it turns a bad event into
  systemic improvement rather than blame.
- **Runbook** — A step‑by‑step guide for handling a specific operational scenario
  (restore from backup, cert expired). *Why it matters:* it lets responders act
  calmly and correctly under pressure.

## Legal, privacy & compliance

> ⚖️ These are plain‑language orientations, **not legal advice**. Laws vary by
> jurisdiction and change; see [Legal & Compliance](../10-legal-and-compliance/README.md).

- **Personal data / PII** — Any information relating to an identifiable person —
  names, emails, **IP addresses**, device and cookie IDs, location, and more.
  "**PII** (Personally Identifiable Information)" is the common US term; "personal
  data" is the broader legal one. *Why it matters:* if you collect it (and almost
  every site does), data‑protection law applies.
- **Data controller / processor** — Under GDPR, the **controller** decides *why and
  how* personal data is processed (usually the site owner, who bears primary
  responsibility); the **processor** acts on the controller's instructions (e.g.,
  your host or analytics vendor). *Why it matters:* contracts should make this
  split explicit, since it allocates legal responsibility.
- **GDPR (General Data Protection Regulation)** — The EU/UK data‑protection law,
  notable for broad reach (it can apply to non‑EU sites with EU users) and large
  fines. *Why it matters:* it requires a lawful basis, transparency, data‑subject
  rights, and 72‑hour breach notification. See [GDPR](../10-legal-and-compliance/gdpr.md).
- **CCPA / CPRA** — California's consumer privacy laws (the leading US state
  regime), and a model for a wider wave of state laws. *Why it matters:* they
  emphasize notice and an **opt‑out** of "sale/sharing," which includes much ad
  tracking. See [CCPA/CPRA](../10-legal-and-compliance/ccpa-cpra.md).
- **Lawful basis** — Under GDPR, the legal justification required for each
  processing activity (consent, contract, legitimate interests, etc.). *Why it
  matters:* you can't process personal data without one — for marketing trackers
  it's generally consent.
- **Consent (opt‑in / opt‑out)** — A user's freely given, informed agreement.
  **Opt‑in** requires action *before* processing (the EU model for trackers);
  **opt‑out** lets processing happen until the user objects (closer to the US
  model). *Why it matters:* using the wrong model — or firing trackers before
  opt‑in — is a common, fined mistake.
- **Cookie (essential vs. non‑essential)** — A small file storing data in the
  browser. **Essential** cookies are needed for the site to function (no consent
  required); **non‑essential** ones (analytics, advertising) generally require
  consent in the EU/UK. *Why it matters:* the essential/non‑essential line is where
  consent obligations bite. See [cookies & tracking](../10-legal-and-compliance/cookies-and-tracking.md).
- **ePrivacy Directive ("cookie law")** — The EU rule (alongside GDPR) requiring
  consent before storing/reading non‑essential cookies and trackers. *Why it
  matters:* it's why the trackers must not fire until the user agrees.
- **Consent Management Platform (CMP)** — Tooling that shows a consent banner,
  blocks non‑essential scripts until consent, records choices, and lets users
  change them. *Why it matters:* a common failure is a CMP that displays a banner
  but still loads trackers before consent — test it.
- **GPC / Do Not Track** — Browser signals communicating a user's opt‑out
  preference. **Global Privacy Control (GPC)** must be honored as a valid opt‑out
  in California. *Why it matters:* ignoring required opt‑out signals is
  non‑compliant.
- **Privacy policy** — A public document disclosing what personal data you collect,
  why, who you share it with, and users' rights. *Why it matters:* it's legally
  required in most places and must match your **actual** practices. See
  [privacy policy](../10-legal-and-compliance/privacy-policy.md).
- **Terms of Service (ToS / T&C)** — The contract between a site and its users.
  *Why it matters:* how users agree (**clickwrap** with an explicit "I agree" vs.
  **browsewrap** footer link) strongly affects enforceability. See
  [terms of service](../10-legal-and-compliance/terms-of-service.md).
- **DPA (Data Processing Agreement)** — A contract governing how a processor
  handles personal data for a controller. *Why it matters:* GDPR requires one with
  vendors that process personal data on your behalf.
- **DPO (Data Protection Officer)** — A designated privacy‑compliance role that
  some organizations must appoint under GDPR. *Why it matters:* it's a formal
  accountability requirement for higher‑risk processing.
- **Breach notification** — The legal duty to report certain personal‑data breaches
  to regulators (GDPR: within **72 hours**) and sometimes to affected individuals.
  *Why it matters:* missing the deadline compounds a breach with penalties — plan
  it into [incident response](../09-maintenance/incident-response.md).
- **Data minimization** — Collecting and keeping only the personal data you
  actually need. *Why it matters:* it's a GDPR principle and the simplest way to
  cut risk — every field you store is a liability.
- **Copyright** — Automatic legal protection for original creative works (text,
  images, code) the moment they're created. *Why it matters:* assume anything you
  find is copyrighted and off‑limits without a license — "I found it online" is not
  a defense. See [copyright & IP](../10-legal-and-compliance/copyright-and-ip.md).
- **Trademark** — Protection for brand identifiers (names, logos, slogans) that
  identify a source of goods/services. *Why it matters:* check for conflicts before
  choosing a business/domain name to avoid a forced, costly rebrand.
- **License (permissive / copyleft)** — The terms under which you may use someone's
  code or content. **Permissive** (MIT, Apache) allows almost anything with
  attribution; **copyleft** (GPL, and **AGPL** even for network services) can
  require you to release your own source. *Why it matters:* "open source" is not
  obligation‑free, and AGPL can surprise proprietary projects. See
  [licensing](../10-legal-and-compliance/licensing.md).
- **Creative Commons (CC)** — A family of content licenses (BY, NC, ND, SA, CC0)
  with specific conditions like required attribution. *Why it matters:* using a
  CC‑licensed asset without meeting its conditions is a license violation.
- **Work made for hire** — A US concept where the hiring party is deemed the author
  of a work. *Why it matters:* it does **not** automatically cover independent
  contractors — client contracts need an explicit ownership/assignment clause.
- **DMCA (Digital Millennium Copyright Act)** — US law known for **notice‑and‑
  takedown** and a **safe harbor** protecting services that host user content and
  follow the rules. *Why it matters:* it's both your remedy when others copy you
  and your obligation when you host user content. See [DMCA](../10-legal-and-compliance/dmca.md).
- **CAN‑SPAM / CASL** — Email‑marketing laws: US **CAN‑SPAM** (opt‑out model,
  strict on honesty and unsubscribe) and Canada's **CASL** (strict opt‑in). *Why it
  matters:* they govern consent, sender identity, and unsubscribe, with real
  per‑message penalties. See [email marketing law](../10-legal-and-compliance/email-marketing-law.md).
- **ADA / Section 508 / EAA / AODA** — Accessibility laws: US **ADA** (applied to
  websites) and **Section 508** (federal); EU **European Accessibility Act**
  (broad private‑sector, from 2025); Ontario's **AODA**. *Why it matters:* they
  make WCAG‑level accessibility a legal requirement for many sites. See
  [accessibility law](../10-legal-and-compliance/accessibility-law.md).
- **Right of withdrawal / cooling‑off** — In the EU/UK, a consumer's right to cancel
  most online purchases within **14 days**. *Why it matters:* you must inform buyers
  of it, and failing to do so extends the window. See [e‑commerce law](../10-legal-and-compliance/ecommerce-law.md).
- **Economic nexus (sales tax) / VAT** — Rules requiring you to collect sales tax
  (US, based on sales thresholds per state) or **VAT** (EU, often by the customer's
  country) on online sales. *Why it matters:* getting tax wrong creates real
  liability; use tax tooling and professional advice.

- **Data retention** — The period you keep personal data before deleting or
  anonymising it. *Why it matters:* GDPR's **storage limitation** principle sets
  no numbers but requires you to justify the period you chose, and data you no
  longer need is pure liability. See [data retention](../10-legal-and-compliance/data-retention.md).
- **Subprocessor** — A processor engaged by *your* processor — your email
  platform's cloud host, your helpdesk's transcription service. *Why it matters:*
  your data reaches them but your contract doesn't, so this chain is where most
  site owners' unexamined exposure sits; processors must get your authorisation
  before engaging one and must tell you about changes. See
  [vendors & subprocessors](../10-legal-and-compliance/vendors-and-subprocessors.md).
- **DPA (Data Processing Agreement)** — The written contract required between a
  controller and a processor handling personal data on their behalf. *Why it
  matters:* GDPR Article 28 specifies what it must cover, and for many platforms
  accepting it is a **separate step** people skip.
- **AI crawler** — An automated agent that reads web content for model training,
  for AI search, or on a user's behalf. *Why it matters:* these are distinct
  purposes with distinct user‑agent tokens, so "block AI" is rarely the right
  instruction — most sites want to decline training while staying citable. See
  [AI crawlers & content controls](../06-seo/ai-crawlers-and-content-controls.md).
- **llms.txt** — A proposed Markdown file at a site's root pointing AI assistants
  at clean versions of key pages. *Why it matters:* it is a **community
  convention, not an adopted standard**, with inconsistent vendor support and no
  ability to express restrictions — useful for developer documentation, not a
  permission mechanism.

## Payments

- **Payment Service Provider (PSP) / payment processor** — A service (e.g.,
  Stripe, PayPal) that lets you accept payments, bundling the gateway,
  processing, and bank relationship. *Why it matters:* a modern PSP lets you start
  accepting cards in minutes without contracting a gateway, processor, and
  merchant account separately. See [Payments](../11-payments/README.md).
- **Payment gateway** — The component that securely captures payment details and
  connects them to processing. *Why it matters:* it's the piece that keeps card
  data off your servers (via hosted fields); modern PSPs include it.
- **Acquirer / issuer** — The **acquirer** (acquiring bank) receives the
  merchant's funds; the **issuer** (issuing bank) issued the customer's card and
  approves or declines the payment. *Why it matters:* they're the two banks whose
  back‑and‑forth authorizes and settles every card payment.
- **Merchant of record (MoR)** — The entity that is the **legal seller** of a
  transaction and owns tax and compliance for it. With a processor like Stripe,
  **you** are the MoR (you handle tax); services like Paddle or Lemon Squeezy
  **become** the MoR and handle sales tax/VAT for you at a higher fee. *Why it
  matters:* it's the key decision for global digital‑goods/SaaS sellers who'd
  rather not register for tax worldwide. See
  [choosing a payment provider](../11-payments/choosing-a-payment-provider.md).
- **Authorization / capture / settlement / payout** — The four stages of a card
  payment: **authorization** (the issuer approves and holds funds), **capture**
  (you instruct collection), **settlement** (banks/networks actually move the
  money over days), **payout** (the PSP transfers your balance, minus fees, to
  your bank). *Why it matters:* they're distinct and asynchronous — "authorized"
  is not "paid," and payouts lag sales. See
  [how online payments work](../11-payments/how-online-payments-work.md).
- **PaymentIntent** — Stripe's object representing a payment and tracking its
  lifecycle (including authentication like 3D Secure). *Why it matters:* it's the
  modern foundation of a Stripe payment and why SCA "just works." See
  [integrating Stripe](../11-payments/stripe-integration.md).
- **Tokenization** — Replacing sensitive card data with a non‑sensitive **token**
  that references it. *Why it matters:* you store and reuse the token, never the
  card number — the basis of PCI‑light integrations and saved cards.
- **Idempotency key** — A unique value attached to a request so that retrying it
  performs the action only once. *Why it matters:* it makes payment creation safe
  to retry after timeouts/double‑clicks so customers aren't charged twice; webhook
  handling needs the same idempotency. See
  [integrating Stripe](../11-payments/stripe-integration.md).
- **Webhook** — An HTTP callback a service sends your server when an event occurs.
  *Why it matters:* for payments, webhooks are the **source of truth** — you
  confirm success and fulfill orders from verified webhooks, not from the browser.
  See [webhooks & fulfillment](../11-payments/webhooks-and-fulfillment.md).
- **3D Secure (3DS) / Strong Customer Authentication (SCA)** — An extra
  authentication step (a bank prompt/code/biometrics) on a card payment. **SCA**
  (under the EU/UK **PSD2** law) legally requires it for many online payments.
  *Why it matters:* it reduces fraud and shifts liability, and is mandatory for
  European customers — Stripe's PaymentIntents flows handle it automatically. See
  [disputes, refunds & fraud](../11-payments/disputes-refunds-and-fraud.md).
- **Chargeback / dispute** — When a cardholder asks their bank to reverse a charge.
  *Why it matters:* it costs you the sale plus a (usually non‑refundable) fee, and
  a high dispute ratio can threaten your ability to accept cards at all.
- **Dunning** — The process of recovering failed recurring payments (retries +
  customer prompts to update their card). *Why it matters:* failed‑payment
  ("involuntary") churn is often larger than voluntary churn; good dunning
  directly protects subscription revenue. See
  [subscriptions & billing](../11-payments/subscriptions-and-billing.md).
- **Reconciliation** — Confirming your records, the PSP's records, and your bank
  all agree on what was paid, refunded, and paid out. *Why it matters:* it catches
  missed webhooks, bugs, and fraud — non‑negotiable for anything handling money.
  See [going live & operations](../11-payments/going-live-and-operations.md).

---

*Missing a term, or found one explained better on its page? Improvements welcome —
see [CONTRIBUTING.md](../../CONTRIBUTING.md).*
