# Caching & CDNs

The fastest request is the one you never make. **Caching** stores copies of
content so it doesn't have to be regenerated or re‑downloaded, and a **CDN**
serves that content from a location near each user. Together they're among the
highest‑leverage performance (and resilience) tools available.

## Layers of caching

Caching happens at several levels, each saving work at a different point:

1. **Browser cache** — the user's browser stores assets locally, so repeat
   visits don't re‑download them.
2. **CDN / edge cache** — copies stored at servers around the world, close to
   users.
3. **Server / application cache** — the server stores results (rendered pages,
   query results) to avoid recomputing them.
4. **Database cache** — frequently used query results kept in fast memory.

## Browser caching with HTTP headers

The server tells browsers how long to keep assets via headers:

- **`Cache-Control`** — the main control (e.g., `max-age`, `public`/`private`,
  `no-store`, `immutable`).
- **`ETag` / `Last-Modified`** — let the browser revalidate ("has this changed?")
  cheaply.

The classic strategy:

- **Static assets** (CSS, JS, images) → cache for a **long time**, and use
  **fingerprinted filenames** (e.g., `app.9f3a2c.js`) so a new version has a new
  URL. This gives you long caching *and* instant updates when content changes.
- **HTML** → cache **short** or revalidate, since it changes and points to the
  fingerprinted assets.

> 💡 **Cache busting:** Because fingerprinted filenames change when content
> changes, you can cache them "forever" without users getting stale files. This
> is the standard way to get aggressive caching safely.

## Content Delivery Networks (CDNs)

A CDN is a distributed network of servers that cache and serve your content from
the edge — physically near each visitor.

**Benefits:**

- **Speed** — shorter distance means lower latency; content is already cached at
  the edge.
- **Scalability** — the CDN absorbs traffic spikes your origin server couldn't.
- **Resilience** — cached content can keep serving even if your origin has
  trouble.
- 🔒 **Security** — most CDNs add DDoS protection, a web application firewall
  (WAF), and TLS termination. See [Security](../07-security/README.md).

**Good to know:**

- CDNs are ideal for **static assets** and cacheable pages; dynamic,
  personalized content needs care (don't cache someone's account page for
  everyone).
- Configure **cache invalidation/purging** so you can push urgent updates.
- Modern static/Jamstack hosting is essentially "CDN‑first" by default. See
  [choosing a tech stack](../01-planning-and-strategy/choosing-a-tech-stack.md).

## Server & application caching

For dynamic sites, caching on the server avoids repeating expensive work:

- **Page/fragment caching** — store rendered output and reuse it.
- **Object/query caching** — keep results of costly database queries in memory
  (e.g., Redis/Memcached).
- **Reverse proxy caching** — a proxy in front of the app serving cached
  responses.

The trade‑off is always **freshness vs. speed** — cache longer for speed, but
have a clear way to invalidate when data changes.

## Cache invalidation: the hard part

"There are only two hard things in computer science: cache invalidation and
naming things." Stale caches serve outdated content; that's the price of speed.
Design an invalidation strategy from the start:

- Fingerprint static assets (auto‑invalidates on change).
- Purge CDN caches on deploy or content update.
- Set sensible TTLs matched to how often content actually changes.
- Keep truly dynamic/personalized responses out of shared caches.

## Don't cache the wrong things

> 🔒 **Security note:** Never let shared caches (CDN, proxy) store
> **personalized or sensitive** responses — an account page, an authenticated
> API response — or one user could be served another's data. Mark such responses
> `Cache-Control: private, no-store` and scope caching rules carefully.

## Putting it together

A typical fast, resilient setup: static assets fingerprinted and cached long at
the browser and CDN; HTML cached short or at the edge with quick revalidation;
the origin protected behind the CDN; and the application caching expensive
computations server‑side. Measure the effect against your
[performance budget](performance-budgets.md).
