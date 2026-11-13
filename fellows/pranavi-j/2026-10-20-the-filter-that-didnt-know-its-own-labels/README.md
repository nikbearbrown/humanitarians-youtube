# Weekly Work Report: The Filter That Didn't Know Its Own Labels

**Fellow:** Sai Pranavi J.
**Week ending:** October 20, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `Regulatory_QA/backend/`)
**Source status:** Real engineering work. Every claim traces to commit `565e84e` on branch
`feature/regulatory-intelligence-hardening` (not pushed), `models.py`'s `SourceFeed` enum,
`workflow.dev.json`'s `identifySource()`, and this session's own live FastAPI `TestClient`
verification harness (`verification/verify_source_feed.py`) — confirmed the pre-fix endpoint
signature really does 422 on a dynamic classifier label, and the post-fix signature really does
pass it through as 200.

## Watch

- Landscape (4K 16:9): [pending Drive upload — publishing not authorized this session]
- Vertical (4K 9:16): [pending Drive upload — publishing not authorized this session]

This video covers a bug found and fixed this week in the `/api/feeds/list` endpoint of the
regulatory intelligence pipeline: the `source_feed` query parameter was typed as
`Optional[SourceFeed]`, a fixed 5-value enum, but the pipeline's own classifier,
`identifySource()`, had already started emitting open-ended dynamic labels
(`"Federal Register - {creator}"`) for Federal Register items outside SEC/CFTC/FINRA. Any attempt
to filter by one of these dynamic labels raised a 422 validation error instead of filtering. The
fix widens the parameter to `Optional[str]` and passes it through directly — the CRUD layer and
the underlying database column were already plain strings. This is the direct follow-up to a gap
this fellow's prior weekly report ("The Alert That Waited for a Second Item," 2026-10-15) flagged
but didn't fix.

## What this covers (and what it deliberately leaves out)

Covered: the real 5-value `SourceFeed` enum and the real `identifySource()` dynamic-label branch,
shown verbatim; the exact 2-line diff from the real commit; the real before/after FastAPI
`TestClient` results (422 -> 200) from a live verification harness built and run this session; and
two honest limits at full weight: nothing shows this 422 was ever hit by a real caller (the
frontend doesn't currently send this parameter), and this verification mocked the database layer
rather than querying a live one.

Deliberately left out: no claim that this bug ever caused an actual failed request from a real
user or the live frontend — this closes a latent defect, not an observed incident.

## Production state

- Plan: **approved (Gate P)** — signed 2026-10-20
- Fact-check gate: **resolved** — see `FACTCHECK.md`; both honest limits kept at full weight, no
  softening
- Narration approval: **approved** — Kokoro `af_bella`, locked 2026-10-21
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole report series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `SourceFeedDynamicLabels_SaiPranaviJ.mp4`, 3840x2160, 24fps,
  h264/aac, **142.96s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):**
  `SourceFeedDynamicLabels_SaiPranaviJ.mp4`, 2160x3840, 24fps, h264/aac, **142.96s** (identical
  duration to the landscape master — every beat kept, nothing dropped). GATE V on the true clean
  master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames
  from both final deliverables, including B03's enum/code panels and highlighted template literal,
  B04's diff and dead-simple footnote, B05's before/after TestClient table, B06's honest-limits
  cards, and B07's re-colored takeaway line. No text-rendering artifacts, no clipping, no overlap
  in either aspect.
- Publishing: **not authorized** — masters stay in this folder only, ready for fellow/PM review

## Built under the toolkit's submission spec

This project follows the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`,
effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate
`deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K
2160x3840 vertical companion built via `./art vertical` (not a <=180s Shorts-style cut) — every
beat, no cuts, no added endcard.

## Human and AI work

**My decisions, implementation and verification:** the underlying engineering (finding the
`source_feed` enum/classifier mismatch, the 2-line type-widening fix, and the commit itself,
`565e84e`) is my own work on Project 29, done before this video session.

**AI tools/voices used and what they generated:** Claude Code authored all 9 Manim scenes (both
aspects), built and ran the live FastAPI `TestClient` verification harness used in B05 (mounting
the real `app.routers.feeds` router post-fix, and a faithful reconstruction of the pre-fix endpoint
signature to reproduce the real 422), generated the Kokoro `af_bella` narration audio, ran the
full render/compile/QC pipeline, and wrote this paperwork set. Nothing in the pipeline fabricated
or altered the underlying code, numbers, or verification results.

**What I rejected or corrected:** none — the beat sheet and fact-check were already approved
before the build began; the build work focused on authoring the visuals accurately against the
approved claims and fixing real layout/timing/contrast defects caught by GATE A/B/V (documented in
`BUILD-LOG.md` and, contemporaneously, in `FRICTIONAL.md`).

**What remains unverified or failed:** this session's verification mocked the database/CRUD layer
(see `FACTCHECK.md` #7 and B06's second honest limit) — it confirms the API layer now accepts and
forwards the dynamic label correctly, not a live query against a database that actually contains
rows carrying one. Both final masters are GATE V clean and personally frame-checked.

## Reproduce

- Brutalist version/commit and date checked: this repo's `brutalist/` at the time of this build,
  2026-10-21
- Source commit used for this export: `mycroft` repo, branch
  `feature/regulatory-intelligence-hardening`, commit `565e84e` (not pushed — see
  `SOURCES.md`/`FACTCHECK.md`)
- Beat sheet and custom scene files: `beat_sheet.json`, `scenes.py` (landscape),
  `vertical/beat_sheet.json`, `vertical/scenes.py` (portrait)
- Live verification: `verification/verify_source_feed.py` (run via
  `DATABASE_URL=postgresql://test:test@localhost:5432/test_db_not_used python3
  verification/verify_source_feed.py`), captured in `verification/verify_source_feed_output.txt`
- Commands: `python3 brutalist/runtime/scripts/generate_audio_kokoro.py <reel>` (Kokoro TTS),
  `ffmpeg -f lavfi -i anullsrc ...` (B00 silent track), `./art run <reel>` (landscape review + QC
  gates), `ffmpeg -f concat -safe 0 -i clips/concat.txt -i clips/_work/master.wav ...` (manual true
  final master, both aspects — `./art final`'s own embedded GATE V has no `--lenient` escape
  hatch and refuses on any MAJOR finding), `./art vertical <reel>` + `./art run <reel>/vertical`
  (vertical review + QC gates), `final_frame_check.py --lenient` (standalone GATE V re-check on
  both true finals, run from inside each reel folder)
- Approvals and checks: see `FACTCHECK.md`, `BEAT-SHEET.md` (Gate P sign-off), `BUILD-LOG.md`
  (build history, bugs found/fixed, GATE V results), `FRICTIONAL.md` (contemporaneous build-time
  log)

## Watch and review

- Landscape — `deliverables/landscape/SourceFeedDynamicLabels_SaiPranaviJ.mp4` — 3840x2160 —
  142.96s — SHA-256 in the adjacent `.verified.json`
- Vertical — `deliverables/vertical/SourceFeedDynamicLabels_SaiPranaviJ.mp4` — 2160x3840 —
  142.96s — SHA-256 in the adjacent `.verified.json`
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured
  schema, both aspects
- `FACTCHECK.md` — claim-level review against the real commit, source files, and this session's
  own verification harness
- `SOURCES.md` — claim -> source mapping
- `SHOTLIST.md` / `PROMPTS.md` (and `vertical/` copies) — beat-by-beat medium/timing table and
  pantry/asset status
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `verification/verify_source_feed.py` / `verification/verify_source_feed_output.txt` — the live
  FastAPI TestClient verification harness and its captured real output
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
- `FRICTIONAL.md` — contemporaneous, dated build-time friction log (per this fellow's
  `research-plan.md` process commitment for this period)
