# Roles & Responsibilities

Websites are built by teams — even a "team of one" wears several hats. Knowing
the roles helps you scope work, assign accountability, and avoid the gaps where
important things (like backups or a privacy policy) fall through the cracks.

## Common roles

| Role | Responsible for | Cares most about |
|------|-----------------|------------------|
| **Product owner / client** | Goals, priorities, budget, sign‑off | Business outcomes |
| **Project manager** | Scope, timeline, coordination | Delivery on time |
| **UX designer** | Flows, wireframes, usability | The user's experience |
| **Visual / UI designer** | Look, brand, design system | Consistency & polish |
| **Content strategist / copywriter** | Words, structure, tone | Clarity & SEO |
| **Front‑end developer** | Markup, styling, interactivity, accessibility | The browser experience |
| **Back‑end developer** | Data, business logic, APIs, auth | Correctness & security |
| **DevOps / SRE** | Deployment, infrastructure, monitoring | Reliability |
| **QA / tester** | Verifying it works for everyone | Quality gates |
| **Security specialist** | Threat modeling, hardening, review | Reducing risk |
| **Data protection officer (DPO)** | Privacy compliance (required for some orgs under GDPR) | Lawful data handling |
| **Legal counsel** | Contracts, policies, compliance advice | Managing liability |

In small projects one person may cover many of these. That's fine — but every
responsibility still needs an owner. The danger isn't wearing many hats; it's
assuming *someone else* is wearing one that nobody is.

## Accountability vs. responsibility

- **Responsible** = does the work.
- **Accountable** = answers for the outcome (only one per outcome).

For example, a developer may be *responsible* for implementing cookie consent,
but the site **owner is accountable** for the site's privacy compliance. This
distinction matters most in legal contexts.

> ⚖️ **Legal note:** Under data‑protection law (e.g., GDPR), the organization
> that decides *why and how* personal data is processed is the **data
> controller** and bears primary legal responsibility. A contractor or hosting
> provider acting on the controller's instructions is typically a **data
> processor**. Contracts should make this split explicit — see
> [Legal & Compliance](../10-legal-and-compliance/README.md).

## Who is liable when something goes wrong?

This is one of the most misunderstood areas, so address it *in writing before
work begins*:

- **Who owns the code and content** on delivery? (See
  [copyright & IP](../10-legal-and-compliance/copyright-and-ip.md).)
- **Who is responsible for maintenance and security patching** after launch? A
  site the freelancer built but nobody maintains is a liability with an unclear
  owner.
- **Who is liable if the site is breached** or found non‑compliant? Contracts
  and data‑processing agreements should allocate this.

> ✅ **Do:** Put maintenance, ownership, and liability terms in the contract or
> statement of work *before* the project starts. Silence here is where disputes
> come from.

## The "who maintains it?" gap

The single most common failure pattern: a site is launched, the build team moves
on, and **nobody owns ongoing maintenance**. Months later an unpatched
dependency is exploited, or the domain silently expires, or a law changes and
the privacy policy is now wrong.

Decide, explicitly, before launch:

- Who applies security updates, and how often?
- Who renews the domain and TLS certificate?
- Who monitors uptime and responds to incidents?
- Who reviews legal compliance as laws change?

→ See [Maintenance & Operations](../09-maintenance/README.md).
