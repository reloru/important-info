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
  `♿ Accessibility note`, `⚡ Performance note`, `💡 Tip`.
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

## How to verify a change (there is no CI yet)

No test/build/lint. The one automated check that matters is the **internal link
checker**. Run it from the repo root before committing:

```bash
python3 - <<'PY'
import os, re
md=[]
for root,dirs,files in os.walk('.'):
    if root.startswith('./.git'): continue
    for f in files:
        if f.endswith('.md'): md.append(os.path.join(root,f))
lr=re.compile(r'\[[^\]]+\]\(([^)]+)\)')
broken=[]; checked=0
for p in md:
    b=os.path.dirname(p)
    for m in lr.finditer(open(p).read()):
        t=m.group(1).strip()
        if t.startswith(('http://','https://','mailto:','#','tel:')): continue
        fp=t.split('#')[0]
        if not fp or '[' in fp: continue  # skip intentional template placeholder pseudo-links
        checked+=1
        if not os.path.exists(os.path.normpath(os.path.join(b,fp))):
            broken.append((p,t))
print(f"checked {checked} links;", "ALL OK" if not broken else broken)
PY
```

Also worth re-running when relevant (scripts are ad hoc, not committed):
- **Orphan check** — every content page should be linked from some other page
  (root/section READMEs count). Last pass: no orphans.
- **Reciprocal-link graph** — flag A↔B pairs and eyeball for weak see-saws.
- **Acronym-defined-on-first-use** — high-risk acronyms (RUM, CMP, GPC, CSP,
  HSTS, RPO/RTO, IaC, SSRF, PCI DSS, E‑E‑A‑T, …) should have an expansion where
  used; the glossary backstops them.

A link-check GitHub Action would be a good future addition (see backlog).

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

- **CI:** add a GitHub Action that runs the link checker (and maybe markdownlint)
  on PRs — the natural first automation for a docs repo.
- **Publish:** wire up a static-site generator (`.gitignore` already anticipates
  `_site/`, `dist/`, `node_modules/`, etc.); relative links + per-section READMEs
  are already SSG-friendly.
- **Depth:** sections are comprehensive but could go deeper where the user wants
  (e.g., more worked examples/workflows). Keep accuracy-over-padding for legal.
- Consider a top-level `CHANGELOG.md` if the KB starts versioning.

## Log of substantive work (append newest at top)

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
