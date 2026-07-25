# Choosing a Technology Stack

The "stack" is the set of technologies your site is built and run on. The best
stack is rarely the newest or the one with the most buzz — it's the one that
fits your **content, team, budget, and maintenance capacity**.

## Start from the requirements, not the technology

Ask what the site actually needs to do:

- Is content mostly **static** (marketing pages, docs) or **dynamic**
  (accounts, personalization, transactions)?
- **Who edits content** — developers, or non‑technical staff who need a CMS?
- What's the expected **scale and traffic**?
- What **skills** does the team already have (and can maintain long‑term)?
- What's the **budget** — for build *and* for ongoing maintenance?
- Any hard **compliance or hosting** constraints (e.g., data residency)?

## The main approaches

### 1. Site builders (Wix, Squarespace, Shopify, etc.)
Hosted, all‑in‑one platforms.

- ✅ Fast to launch, low technical skill needed, maintenance handled for you.
- ❌ Limited flexibility, ongoing subscription, potential lock‑in, less control
  over performance/SEO details and data.
- **Good for:** small businesses, simple sites, non‑technical owners, quick
  stores.

### 2. Content Management Systems (WordPress, Drupal, etc.)
Software that separates content from presentation, with an admin UI.

- ✅ Non‑developers can edit; huge ecosystem of themes/plugins; flexible.
- ❌ Plugins are a **security and maintenance burden**; needs hosting and
  regular updates; can become slow if unmanaged.
- **Good for:** content‑heavy sites, blogs, sites edited by non‑developers.
- 🔒 **Security note:** The majority of CMS compromises trace to outdated core,
  themes, or plugins. A CMS is a *commitment to patching*. See
  [dependency management](../09-maintenance/dependency-management.md).

### 3. Static site generators & the "Jamstack" (Hugo, Eleventy, Astro, Next.js static export, etc.)
Pre‑build pages into static files, often served from a CDN, with dynamic bits
added via APIs/serverless functions.

- ✅ Very fast, cheap to host, small attack surface, scales trivially.
- ❌ Requires a build step and developer involvement; dynamic features need
  extra services.
- **Good for:** docs, blogs, marketing sites, anything content‑driven where
  editors are comfortable with a workflow (or a headless CMS is added).

### 4. Custom application (a web framework — React/Vue on the front, Django/Rails/Node/Laravel/etc. on the back)
Bespoke code for bespoke needs.

- ✅ Maximum flexibility and control; fits complex, unique requirements.
- ❌ Highest cost to build and maintain; you own all the responsibility for
  security, performance, and updates.
- **Good for:** SaaS products, web apps, complex transactional systems.

## Decision cheat‑sheet

| If you need… | Consider |
|--------------|----------|
| A simple site, live this week, minimal upkeep | Site builder |
| Non‑technical editors + flexibility | CMS (well‑maintained) or headless CMS + static |
| Speed, security, low hosting cost, content‑driven | Static site generator / Jamstack |
| Complex logic, accounts, unique workflows | Custom application |

## Beware "resume‑driven development"

Choosing a technology because it's trendy or good for your résumé — rather than
because it fits the problem — is a classic, costly mistake. Every dependency and
framework you adopt is something *someone must understand and maintain for
years*.

> ✅ **Do:** Favor boring, well‑documented, widely‑used technology with a healthy
> community and a clear update path.
> ❌ **Don't:** Pick a stack no one on the maintenance team can support, or one
> whose ecosystem is abandoned.

## Total cost of ownership, not just build cost

A cheaper build with expensive maintenance can cost more overall. Weigh:

- Hosting and service subscriptions.
- Update/patching effort (especially for plugin‑heavy CMSes).
- Specialist skills needed to maintain it.
- Lock‑in and the cost of migrating away later.

Record *why* you chose the stack. That reasoning is gold when someone
re‑evaluates it in two years. See [budgeting & scoping](budgeting-and-scoping.md)
and [Deployment & DevOps](../08-deployment-and-devops/README.md).
