# Dead Links, Live Redirects.

**Fellow:** Rishabh Madani \
**Project:** Humanitarians AI site — link and route cleanup \
**Date:** 2026-08-14

## Subject

A corrections reel: what was broken on the site, and what fixed it. The sequel to
*Fellows Portal, Refactored.*, covering the eleven commits of 2026-08-10.

It opens on three kinds of rot — links that point nowhere, tool files that exist
twice, and a route nothing reaches. Two are harmless to fix. The third bites back:
consolidating five duplicate artifact files deletes the destinations of live
redirects in `next.config.mjs`, and `/gru.html` starts returning a 404 even though
nothing on the site ever linked to it.

The lesson is the transferable part: **a redirect is a reference.** A file with no
inbound links can still be load-bearing in the router, where a link crawler and a
`git grep` for hrefs both miss it. The fix is not a better delete — it is keeping
the files the redirects need and excluding them from the Tools listing instead,
where the duplicate was actually visible to a human.

It closes on the three project subdomains, served by a middleware rewrite so the
subdomain stays in the address bar rather than being thrown away by a redirect.

## How the Video Is Structured

Fifteen beats across four cycles, each a prompt to Claude followed by the real diff
it produced.

The reel carries **one** OUTPUT beat rather than one per cycle. Three results — the
crawl's findings, the redirect resolving again, the subdomain loading — were
demonstrations of claims no viewer would dispute, so they are stated in narration
instead of shown. The 404 is the exception and is not negotiable: it is the only
evidence for the reel's central claim, and without it the revision repairs a problem
the viewer never saw.

That beat is a native animation of the causal chain, not a screen recording —
`next.config.mjs` → the deleting commit → `GET /gru.html · 301 → 404`. No mocked-up
`curl` output appears on screen; inventing HTTP responses would be fabrication
dressed as evidence.

## How the Video Was Built

Built with the Brutalist workflow: a `beat_sheet.json` driving narration and timing,
Kokoro narration in the Pragmatist register (`af_bella`), and Remotion for every
beat. Narration is generated and measured first, so audio duration is the master
clock and each visual beat is cut to fit it.

Unlike the first reel, this one contains **no screen captures at all** — all fifteen
beats are machine-rendered at 3840x2160, so nothing in it is upscaled.

## The 9:16 Short

A 1:36 Shorts cut lives in `short/`. It keeps cycle 2 — the one that goes wrong —
because it is the only self-contained story in the reel with a hook, a turn and a
payoff: consolidate five duplicate files, discover they were redirect destinations,
watch it 404.

It honours the full spine — ask, code, and a genuine OUTPUT beat. Every beat is
re-rendered natively in portrait; nothing is centre-cropped.

## Files

- `README.md` — this file
- `beat_sheet.json` — narration, timing, and scene instructions (15 beats)
- `PEDAGOGY.md` — teaching-quality gate, signed before audio was generated
- `SOURCES.md` — commit-to-beat map, provenance, and the scope gap
- `STATUS.md` — per-beat fill state
- `ToDo.md` — outstanding human slots (none)
- `todo.json` — build support
- `short/` — the 9:16 Shorts cut: its own `beat_sheet.json` (6 beats) and
  `PEDAGOGY.md` gate

## Notes

- **Provenance, stated on air.** The redirect list that breaks was not written in
  this reel's commit range — it was authored four weeks earlier, by a different
  author, in the commit that built the AI+1 hub. That is the actual reason the
  delete looked safe, and the video says so. Omitting it would have made the mistake
  look more careless than it was.
- **Scope gap, chosen not overlooked.** This reel covers work done after the first
  video was *built*, not after its *content* ends. Twenty-six commits sit between
  the two reels and are covered by neither — six of mine from 2026-07-01
  (course, donate page, sorting) and twenty from 2026-07-15–21 (the AI+1 hub, and
  an earlier manual broken-link pass). Excluded as off-spine. Full table in
  `SOURCES.md`.
- **Primacy.** A manual site-wide broken-link pass happened three weeks before this
  one. The narration therefore claims only that this crawler is the first
  *automated* audit, never the first audit.
- **`scripts/check-links.mjs` is gitignored** in the app repo as local-only, so the
  script this video teaches is not currently there for a viewer to find. The
  `package.json` entry that invokes it is committed.
