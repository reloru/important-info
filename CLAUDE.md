# CLAUDE.md — working memory for this repo

Context for future Claude sessions that isn't obvious from reading the docs.
Written for me (Claude), not primarily for humans. If a convention here ever
conflicts with what the docs actually do, the docs win — update this file.

## What this repo is

`reloru/important-info` is a **documentation-only knowledge base** about
**website development and maintenance**, focused on **best practices** and
**legal/compliance** — deliberately *not* granular code-level tutorials. No
application code. No build step. The deliverable is clear, correct, pedagogical
Markdown.

Audience: developers, freelancers/agencies, site owners, and learners. It's
meant to read either as a course (top to bottom, sections are numbered in
life-cycle order) or as a reference (jump to a topic).

## Layout & conventions (follow these when adding/editing)

- Content lives in `docs/NN-section/`, numbered 00–10 in website life-cycle
  order (Getting Started → Planning → Design → Dev → Accessibility →
  Performance → SEO → Security → Deployment → Maintenance → Legal), plus
  `docs/templates/`.
- **`docs/11-payments/`** sits *outside* the life-cycle numbering as a **feature
  deep-dive** (a capability, not a phase). It's OK to add more such feature
  sections (12+, e.g. email/notifications, i18n, search, auth-as-a-feature) the
  same way rather than forcing everything into the life-cycle metaphor. Payments
  leans more technical than the rest of the KB on purpose — that's appropriate
  for the topic; still keep architecture/best-practices over line-by-line code.
- **Every section folder has a `README.md` index** that links its pages. When
  you add a page, link it from that README (and, if broadly important, from the
  root `README.md` section table).
- File names: lowercase, hyphenated, one topic per file
  (`dependency-management.md`).
- **Callout vocabulary** used repo-wide (keep consistent):
  `✅ Do` / `❌ Don't`, `⚖️ Legal note`, `🔒 Security note`,
  `♿ Accessibility note`, `⚡ Performance note`, `💡 Tip`, `⚠️ Caution`.
  `⚠️` was in use in 7 places before it was documented; it's now listed in the
  root README and CONTRIBUTING too. Don't invent new ones.
- Use **relative links** between docs so navigation works on GitHub and in any
  future static-site generator.
- Page shape (pedagogical pattern to preserve): open with *why it matters* →
  *what to do* → an actionable **checklist or decision table**. Define important
  terms on first use; don't assume prior expertise.
- Typography: the docs use non-breaking hyphens/typographic dashes in many
  words (e.g. `e‑commerce`, `opt‑in`, `front‑load`). Match surrounding style;
  don't "correct" them.

## Editorial standards (the bar to hold)

- **Pedagogical, not encyclopedic-terse.** Teach and connect concepts; don't
  just define or point elsewhere. Pages should stand on their own *and* link
  where it genuinely adds value.
- **Terminology consistency:** website (one word), JavaScript, front end / back
  end (open compound), e‑commerce, email. Verified consistent as of the last
  pass.
- **Cross-references:** link where it adds context; avoid weak "see X ↔ see Y"
  see-saw loops where neither side adds information. Reciprocal links are fine
  when each direction carries distinct context (most here do).
- **The glossary (`docs/00-getting-started/glossary.md`) is comprehensive by
  design.** Each entry is self-contained (what it is AND why it matters).
  Redundancy with body pages is intentional and wanted — it's a standalone
  reference. If you introduce an important new term in the docs, add a glossary
  entry too.
- **Legal / privacy / security: accuracy over completeness.** Keep the repeated
  **"not legal advice"** framing intact. Distinguish established requirements
  from recommended practices from context-dependent guidance. Prefer linking to
  primary sources; note dates where guidance is time-sensitive.

## How to verify a change

Run the committed checker from the repo root. It replaced the ad-hoc heredocs
that used to live in this file — CI and humans now run the same code, so a CI
failure reproduces locally with the identical command:

```bash
python3 tools/check-docs.py
```

Stdlib only, no install, no network. It checks: relative links resolve,
`#anchors` match real headings, no orphaned pages, code fences balanced, table
row widths consistent. It skips `[BRACKETED]` template pseudo-links on purpose
and does not fetch external URLs.

`.github/workflows/docs-check.yml` runs it on every PR and on pushes to `main`
(`actions/checkout` is the only action used).

Still manual, worth doing when relevant:
- **Reciprocal-link graph** — flag A↔B pairs and eyeball for weak see-saws.
- **Acronym-defined-on-first-use** — high-risk acronyms (RUM, CMP, GPC, CSP,
  HSTS, RPO/RTO, IaC, SSRF, PCI DSS, E‑E‑A‑T, …) should have an expansion where
  used; the glossary backstops them.
- **External link liveness** — the checker doesn't fetch URLs. The repo now
  carries real citations (see below), so `curl -o /dev/null -w '%{http_code}'`
  over the extracted URL list is worth an occasional pass.


## Gotchas / do-not-break

- **Template `[PLACEHOLDER]` tokens are intentional.** `docs/templates/*.md`
  (privacy policy, ToS, cookie policy, incident report, a11y statement) are
  skeletons with `[BRACKETED]` fields for users to fill. Do **not** "fix" them.
  The link checker deliberately skips pseudo-links containing `[` for this
  reason (e.g. `[Cookie Policy]([COOKIE POLICY URL])`).
- Templates carry an explicit "skeleton, not a finished legal document — get
  professional review" warning. Keep it.
- **Font/asset privacy stance** taken across docs: self-host fonts/assets (the
  Google Fonts GDPR ruling is cited). Stay consistent if the topic comes up.
- **Search Console** has a dedicated page (`docs/06-seo/search-console.md`) and
  is wired into: SEO README, analytics, technical-seo (2 spots), structured-data,
  performance/core-web-vitals, maintenance-plan, and templates/pre-launch-checklist.
  If you touch SEO tooling, keep those references coherent.

## Environment & workflow (this remote setup)

- Remote/web execution; ephemeral container — **only what's committed & pushed
  survives.** This CLAUDE.md is the persistence mechanism for cross-session
  context.
- **GitHub via MCP tools** (`mcp__github__*`), not `gh` CLI. Search for them
  with ToolSearch (they're deferred). Every GitHub comment/PR body I author ends
  with the Claude Code attribution footer (server de-dupes it).
- Designated dev branch: `claude/website-dev-knowledge-base-86n12a`. **PR #1 is
  already merged into `main`.** A merged PR is finished — for new work, restart
  this branch from latest `main`
  (`git fetch origin main && git checkout -B claude/website-dev-knowledge-base-86n12a origin/main`),
  commit the fresh change, push, open a **new** draft PR, and (per the user's
  standing preference) merge it when done. Don't stack new commits on merged
  history or reuse the merged PR.
- Default user preference stated for this kind of task: **open a PR and merge it
  after finishing** — don't wait for approval unless the change is risky/ambiguous.
- Never put the model identifier in committed artifacts (commits, PRs, files) —
  chat replies only.

## Decisions already made (don't re-litigate without reason)

- **License:** docs under **CC BY 4.0** (`LICENSE`), plus an educational/
  no-warranty disclaimer.
- **Merge style:** PR #1 used a **merge commit** (to preserve the
  section-by-section build history on a fresh repo). Fine to squash small
  follow-ups.
- Structure is numbered-by-life-cycle on purpose (learnable in order). Don't
  re-architect without a reason; the user has affirmed the structure is good.
- Glossary redundancy is a feature, not a bug (see above).

## Backlog / good next steps (only if asked)

- ~~**CI:** add a GitHub Action that runs the link checker.~~ **Done** — see
  `tools/check-docs.py` + `.github/workflows/docs-check.yml`. markdownlint is
  still an option if line-length/style drift becomes a problem; it would need
  Node, which the repo otherwise doesn't.
- **Publish:** wire up a static-site generator (`.gitignore` already anticipates
  `_site/`, `dist/`, `node_modules/`, etc.); relative links + per-section READMEs
  are already SSG-friendly.
- **Depth:** sections are comprehensive but could go deeper where the user wants
  (e.g., more worked examples/workflows). Keep accuracy-over-padding for legal.
- Consider a top-level `CHANGELOG.md` if the KB starts versioning.

## Log of substantive work (append newest at top)

- **Content-gap pass on the non-legal sections.** The prior audit checked
  structure everywhere but read content closely only in legal/a11y/PCI/CWV. This
  pass read the rest. Method worth reusing: **grep the KB for topics a
  practitioner would expect**, then verify each apparent miss against the page
  that should own it — most "gaps" are wording mismatches. Also ran a **new
  check: glossary terms with no body-page coverage** (169 terms → 20 candidates
  → 2 real). Confirmed *not* gaps: redirects/migrations (technical-seo has a
  section), supply chain (dependency-management), AI-*generated* content
  (copyright-and-ip), monitoring/error tracking, Open Graph, CMS choice.
  - **Four new pages**, all cross-linked and in their section READMEs:
    `03/third-party-scripts.md` (the connective page between security,
    performance, privacy and PCI — inventory, SRI, CSP, consent gating,
    self-hosting; also gives the glossary's orphaned "third-party script" and
    "supply-chain attack" entries a home), `06/ai-crawlers-and-content-controls.md`,
    `10/data-retention.md`, `10/vendors-and-subprocessors.md`.
  - **Three in-place additions:** CORS + an SRI pointer in `security-headers.md`
    (CORS was absent from the page that should own it — note the framing that
    earned its place: it's the one security header that *grants* rather than
    restricts); **passkeys/WebAuthn** in `authentication-and-authorization.md`.
  - **Verified, don't re-derive:** WebAuthn L3 is a **W3C Recommendation
    (25 Aug 2026)**; robots.txt is **RFC 9309**; OpenAI tokens are GPTBot /
    OAI-SearchBot / ChatGPT-User / OAI-AdsBot; Anthropic's are ClaudeBot /
    Claude-SearchBot / Claude-User; **`Google-Extended` is NOT a crawler** (no
    separate UA string, control token only, no Search impact) — this is the fact
    most third-party articles get wrong. **`llms.txt` is a community convention,
    NOT a standard** — a marketing blog claimed a June 2026 W3C working draft
    standardizing it; **that draft does not exist in W3C's own listings and the
    claim was not repeated.** Real standards work is IETF **aipref**
    (`draft-ietf-aipref-vocab`, `draft-ietf-aipref-attach`, neither yet an RFC).
  - **Still open as feature-section candidates** (unchanged): full
    i18n/localization, transactional email/deliverability, on-site search.

- **Repo audit + fixes (this pass).** Ran structural checks (links, anchors,
  orphans, fences, tables, terminology, callouts, duplicate prose): **structure
  was clean** — 828 links resolved, no orphans, no duplicates, terminology
  consistent. The real findings were factual staleness and a **citation gap**.
  - **Three verified accuracy fixes**, each checked against the primary source in
    Sept 2026: (1) PCI page said "v4.0 is the current major version" — it's
    **v4.0.1**, and the **Jan-2025 SAQ A** (effective 31 Mar 2025) moved
    **6.4.3/11.6.1 out of the questionnaire and added a script-security
    *eligibility* criterion** — so page-integrity work is now part of qualifying
    for SAQ A, not optional polish; (2) CCPA revenue threshold is
    **$26,625,000** (eff. 1 Jan 2025, CPI-adjusted in odd years), plus a new
    section on the **2026 regs** (risk assessments from 1 Jan 2026, attestation
    by 1 Apr 2028; cyber audits 1 Apr 2028/2029/2030 by revenue; **ADMT**
    1 Jan 2027); (3) ADA **Title II** is a **final rule** (24 Apr 2024, WCAG 2.1
    AA) whose compliance dates were **extended** by an interim final rule
    effective 20 Apr 2026 to **26 Apr 2027 / 26 Apr 2028**.
  - **Citation gap closed on the high-stakes pages.** CONTRIBUTING principle 3
    requires authoritative sources for legal/security/standards claims, but the
    whole KB had only **3 external links**. Added verified **Primary sources**
    blocks (every URL curl-checked) to gdpr, ccpa-cpra, cookies-and-tracking,
    email-marketing-law, dmca, accessibility-law, wcag-overview, owasp-top-10,
    pci-compliance, core-web-vitals. wcag-overview and owasp-top-10 had *named*
    their authoritative source without linking it — fixed. **Pattern to follow:
    date-stamp the verification ("last verified September 2026") on any page
    carrying figures that move.**
  - **Automation:** `tools/check-docs.py` (stdlib only) now carries the link
    check *plus* anchor, orphan, fence, and table checks, and CI runs it. The
    heredoc in this file is gone — same code for CI and humans.
  - Also: documented `⚠️` as a real callout; wired forms-and-input-handling into
    the security README (it was only reachable from the dev section); expanded
    CSRF/SSRF on first use in two pages.

- **Pre-publish gap audit + SEO checklist + forms page.** Audited the KB for
  critical holes before wiring up an SSG. Finding: **no critical omission** — the
  core life-cycle/security/privacy/accessibility/performance/SEO/payments/legal is
  solid. Filled two real gaps: (1) `docs/templates/seo-checklist.md` (deeper SEO
  gate; overlap with pre-launch SEO block is intentional/OK per user); (2) new
  `docs/03-development-best-practices/forms-and-input-handling.md` covering
  server-side validation, spam/abuse (honeypot/time-trap/rate-limit/CAPTCHA),
  uploads, deliverability, privacy — the form-spam/rate-limit gap. Also added a
  brief `hreflang`/international-SEO note to technical-seo. Glossary: added
  hreflang, rate limiting, form spam protection. **Still non-critical but open as
  feature-section candidates if the user wants them: full i18n/localization
  (12+), transactional email/deliverability, on-site search.** KB is otherwise
  publish-ready.
- **Four checklist templates added** (`docs/templates/`): payments go-live,
  security hardening, privacy & compliance, and project handover & ownership.
  Each is a copy-ready, single-domain gate distinct from the broad pre-launch
  checklist; cross-linked from templates README, the pre-launch checklist, and
  their source sections (payments going-live, security README, legal README,
  roles/handover). Pattern for future checklists: keep them non-redundant with
  pre-launch (deeper/for a specific moment), link to source sections, note *when*
  to run them.
- **Payments section (new `docs/11-payments/`, focus: Stripe):** added a 10-file
  feature deep-dive — how online payments work, choosing a provider
  (processor vs. merchant-of-record), PCI/SAQ A, Stripe overview, integration
  (Checkout/Payment Element/Payment Links, PaymentIntent lifecycle, idempotency,
  "never trust the client"), webhooks & fulfillment (source of truth, signature
  verify, idempotent handling), subscriptions & billing (dunning, portal,
  auto-renew law), disputes/refunds/fraud (Radar, 3DS/SCA), and going-live/ops
  (Stripe CLI, payouts, reconciliation, tax). Verified a few volatile facts via
  web (Stripe now recommends **Checkout Sessions API + Payment Element** for most;
  standard US pricing commonly ~2.9%+30¢, hedged; SAQ A via hosted fields; MoR
  alternatives Paddle/Lemon Squeezy). Wired into e-commerce-law (2 spots), root
  README table+structure, and glossary (new Payments group). **Volatile Stripe
  specifics are deliberately hedged and point to docs.stripe.com as source of
  truth** — keep that stance; re-verify pricing/product names if you touch them.
- **CLAUDE.md added (PR #2, merged):** this file.
- **KB build-out + refinement (PR #1, merged):** created the full 11-section KB
  (79 docs) + templates; then a refinement pass adding the Search Console /
  webmaster-tools page and rewriting the glossary into a comprehensive
  terminology reference. Audited: links resolve, no placeholders/TODOs/orphans,
  consistent terminology.
