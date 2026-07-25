# Contributing to the Knowledge Base

Thanks for helping keep this reference accurate and useful. This repo is
documentation, not application code, so the "build" is really about clear
writing and correct information.

## Principles

1. **Pedagogical first.** Explain *why*, not just *what*. Assume a smart reader
   who is new to the specific topic. Define jargon on first use.
2. **Best practices over trends.** Prefer durable, well‑established guidance.
   When something is contested or fast‑moving, say so.
3. **Cite when it matters.** Legal, security, and standards claims should point
   to an authoritative source (a law, an official spec, a recognized body).
4. **Practical.** Favor checklists, decision tables, and concrete examples over
   abstract prose.
5. **Honest about scope.** This is educational material. The legal sections are
   **not legal advice** — keep that framing intact.

## Structure & naming

- Content lives under `docs/` in numbered sections that follow the website
  life cycle.
- Each section folder has a `README.md` that indexes its files.
- File names are lowercase, hyphenated, and descriptive:
  `dependency-management.md`, not `deps.md`.
- Keep one topic per file. If a file grows past a few screens, consider
  splitting it and linking.

## Style guide

- Write in Markdown (GitHub‑flavored).
- Use `#` for the page title (one per file), then `##`/`###` for structure.
- Wrap prose at a sensible width; don't hard‑wrap tables or code.
- Use the shared callout conventions:
  - `> ✅ **Do:**` / `> ❌ **Don't:**`
  - `> ⚖️ **Legal note:**`
  - `> 🔒 **Security note:**` / `> ♿ **Accessibility note:**` / `> ⚡ **Performance note:**`
- Prefer relative links between docs so navigation works on GitHub and in
  static‑site generators.
- Keep line‑level code snippets minimal and illustrative — this repo is about
  practice and policy, not a code library.

## Adding a new topic

1. Pick the right section (or propose a new one in your PR description).
2. Create `docs/NN-section/your-topic.md` with a clear title and intro.
3. Add a link to it from that section's `README.md`.
4. If it's broadly important, add it to the root `README.md` map.
5. Open a pull request describing what you added and why.

## Updating legal content

Laws change. When you touch anything in `docs/10-legal-and-compliance/`:

- Note the **date** of the guidance where relevant.
- Prefer linking to primary sources (the statute, the regulator's site).
- Do **not** turn summaries into definitive legal advice — keep the disclaimer.

## Review

Every change goes through a pull request. Reviewers check for accuracy,
clarity, correct linking, and consistent style.
