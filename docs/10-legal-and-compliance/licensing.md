# Licensing & Ownership

Two related topics that cause real disputes and real legal exposure: the
**licenses of the software you use** to build a site, and **who owns the site**
when you build it for someone else. Both are easy to get wrong quietly and
expensive to sort out later.

> ⚖️ Not legal advice. Software licensing and ownership terms have real legal
> effect; get professional review for anything significant.

## Software & open‑source licenses

Nearly every site is built on open‑source software (libraries, frameworks,
plugins, tools). Open source is free to use, but **not free of obligations** —
each component carries a license with terms you must honor. Ignoring them is a
license violation.

### Two broad families

- **Permissive** (e.g., MIT, BSD, Apache 2.0) — do almost anything, including use
  in commercial/closed products, usually just by **preserving the license and
  copyright notice**. Apache 2.0 also has an explicit patent grant. Low friction.
- **Copyleft** (e.g., GPL, LGPL, AGPL) — you may use and modify, but distributing
  (and for **AGPL**, even *providing it as a network service*) can require you to
  **release your source under the same license**. This can have serious
  implications for proprietary projects.

> ⚠️ **AGPL** is the one that surprises people: it can trigger source‑disclosure
> obligations for software offered over a network (like a web app), not only when
> you distribute binaries. Check the license of any AGPL‑licensed component before
> building a proprietary service on it.

### Good practice

> ✅ **Do:**
> - **Know the licenses** of your dependencies (tools can generate a license
>   inventory). See
>   [dependency management](../09-maintenance/dependency-management.md).
> - **Comply** with each: preserve notices, provide attribution, and meet any
>   source‑sharing obligations.
> - **Watch copyleft** (especially GPL/AGPL) in proprietary products.
> - **License your own code** deliberately — pick a license (or keep it
>   proprietary) on purpose.

> ❌ **Don't:**
> - Assume "open source" means "no obligations."
> - Mix incompatible licenses without checking.
> - Ship someone else's code stripped of its required notices.

## Content licenses

Beyond code, remember that images, fonts, media, and text each carry their own
licenses. That's covered in [copyright & IP](copyright-and-ip.md) — the same
principle applies: know the license, comply with it, keep records.

## Who owns the website? (Client work)

This is one of the biggest sources of freelance/agency disputes. By default, the
answer is often **not** what clients assume.

### The default surprises people
In many jurisdictions, absent a written agreement, **the creator (developer/
agency) may retain copyright** in the code and design they produce — even though
the client paid for it. The client may only have an implied license to use it.
That's frequently the opposite of what everyone assumed.

> ✅ **Do:** Put ownership **in writing** in the contract, before work starts:
> - Who owns the **code**, the **design**, and the **content** on final payment?
> - Is ownership **assigned/transferred** to the client, or is the client granted
>   a **license** (and if so, how broad)?
> - What about **pre‑existing/reusable components** the developer brings (often
>   licensed to the client, not assigned)?
> - What about **third‑party assets** (stock, fonts, plugins) — their licenses
>   pass to the client, but the developer's own license may be non‑transferable.

### Accounts and access
Ownership isn't just code. Make sure the **client owns and controls their own
accounts** — domain registrar, hosting, DNS, analytics, and platform logins — so
they're never held hostage. See
[domains & hosting](../01-planning-and-strategy/domains-and-hosting.md) and
[roles & responsibilities](../00-getting-started/roles-and-responsibilities.md).

### "Work made for hire" is not universal
The US concept of "work made for hire" (where the hiring party is deemed the
author) applies only in specific circumstances and **doesn't automatically cover
independent contractors** without the right written terms — and it isn't a
concept everywhere. Don't rely on it implicitly; use an explicit assignment
clause.

## Practical checklist

- [ ] Dependency **license inventory** exists and is reviewed.
- [ ] Copyleft (**GPL/AGPL**) obligations understood for any proprietary work.
- [ ] Your own code's license chosen deliberately.
- [ ] Client contract states **ownership/assignment** of code, design, and
      content on payment.
- [ ] Handling of **pre‑existing components** and **third‑party assets** spelled
      out.
- [ ] Client **owns their own accounts** (domain, hosting, DNS, analytics).
- [ ] All content licenses tracked (see
      [copyright & IP](copyright-and-ip.md)).

Getting licensing and ownership right is unglamorous paperwork that prevents the
most bitter and avoidable disputes in web work. Do it before you build, not after
the relationship sours.
