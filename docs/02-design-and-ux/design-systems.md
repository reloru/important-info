# Design Systems

A design system is a shared, documented set of **reusable components,
patterns, and standards** that keep a product consistent and speed up building
it. Even a small site benefits from a lightweight version. Large or growing
sites can't stay coherent without one.

## Why bother

- **Consistency** — buttons, forms, spacing, and colors look and behave the same
  everywhere, which builds trust and reduces cognitive load for users.
- **Speed** — designers and developers assemble from ready‑made parts instead of
  reinventing each screen.
- **Maintainability** — fix or improve a component once, and it propagates.
- **Accessibility at scale** — bake accessibility into components once, and
  every use inherits it. ♿
- **Onboarding** — new team members have a single source of truth.

## Levels of a design system

From lightest to heaviest — pick what fits your project:

1. **Style guide** — documented colors, typography, spacing, logo usage, tone.
2. **Design tokens** — named, reusable values (e.g., `color-primary`,
   `space-4`, `font-size-lg`) stored centrally so design and code share one
   source of truth. Change the token, change everywhere.
3. **Component library** — reusable UI building blocks (buttons, inputs, cards,
   modals) with defined states and behavior.
4. **Pattern library** — larger recurring solutions (forms, navigation, search,
   pagination).
5. **Full design system** — all of the above, documented, versioned, and
   governed, often with usage guidelines and accessibility notes per component.

## Design tokens: the quiet superpower

Tokens decouple *decisions* from *values*. Instead of hard‑coding `#0055ff` in
fifty places, you reference `--color-primary`. Rebranding, theming (including
dark mode), and consistency all become tractable. Tokens are the bridge between
design tools and code.

## Component thinking

Build UIs from small, composable, well‑defined components. Each component should
have:

- A clear, single purpose.
- Defined **states** (default, hover, focus, active, disabled, error, loading,
  empty).
- Documented **props/variants** and when to use each.
- Built‑in **accessibility** (labels, roles, focus handling, keyboard support).
- Usage guidance ("use for the primary action; only one per view").

> ♿ **Accessibility note:** A component library is the best place to enforce
> accessibility. If your `Button`, `Input`, and `Modal` are accessible by
> construction, most of your site inherits it. Conversely, one inaccessible
> shared component multiplies the problem everywhere it's used.

## Governance

A design system is a living product, not a one‑time deliverable. Decide:

- Who owns it and approves changes?
- How are new components proposed and reviewed?
- How is it versioned and communicated when it changes?
- How do teams give feedback?

Without governance, systems drift back into inconsistency ("just this one
special button…") and lose their value.

## Don't over‑engineer

For a small brochure site, a one‑page style guide plus a handful of consistent,
accessible components is plenty. Match the investment to the project. The goal is
consistency and maintainability — not ceremony.

> ✅ **Do:** Start with tokens (color, type, spacing) and a few core components.
> Grow the system as real needs appear.
> ❌ **Don't:** Build an elaborate system for a five‑page site, or let one grow
> undocumented until nobody knows the "right" way to do anything.
