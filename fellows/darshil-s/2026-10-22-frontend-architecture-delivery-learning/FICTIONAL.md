# Frictional Log — 2026-10-22

**Learnings:** Vite resolves environment variables at build time, not runtime, so each environment needs its own build; single-page apps need a server-side fallback rule to serve `index.html` for unrecognized routes; serving compiled static assets through Nginx instead of Node keeps the runtime container minimal; Vitest + React Testing Library test behavior rather than implementation details; baking a version identifier into the build lets a running app report exactly what's live.

**Implemented work:** Learning-only week — no separate implementation video. Content was synthesized into the companion technical-learnings video rather than applied to the pipeline directly this week.
