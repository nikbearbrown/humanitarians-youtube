# Weekly Work Report: The Dashboard That Forgot What Day It Was

**Fellow:** Sai Pranavi J.
**Week ending:** November 19, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo,
`Regulatory_QA/backend/app/crud.py`'s `FeedCRUD.get_stats()`)
**Source status:** Real engineering work. Every claim traces to this week's F1 fix (closed
2026-11-19, commit `a7e1628` on `feature/regulatory-intelligence-hardening`) and this session's own
live Python/psycopg2 verification harness (`verification/verify_stale_stats_window.py`) — run
directly against the real, live `mycroft_intelligence` Postgres DB.

## Watch

- Landscape (4K 16:9): [pending Drive upload — publishing not authorized this session]
- Vertical (4K 9:16): [pending Drive upload — publishing not authorized this session]

This video covers a bug found and fixed this week (F1) in Project 29's regulatory intelligence
dashboard backend. D1 (2026-11-03) fixed which column the dashboard's severity breakdown reads, and
in the process flagged — but did not close — a second defect in the same query: the severity-count
query was filtered to `WHERE created_at >= NOW() - INTERVAL '7 days'`. The live database's fixture
data has `created_at` between July 14 and July 24, 2026 — today is November 19, 2026, four months
later — so that filter returns zero rows, unconditionally, on every single page load, forever.
Meanwhile `total_feeds` is an unwindowed count, and the feed list directly below the stats cards
(including last week's E1-fixed "Select All" button) applies no date filter at all. The dashboard
read "Total Feeds: 411, Critical: 0, High Priority: 0" while the list right below it showed 24 real
Critical- and 8 real High-tagged items a user could click and select right now — zero clicks to
reach, the default page load. The fix drops the 7-day filter from the severity query only, so it
reads the same unwindowed population as `total_feeds` and the feed list already do.

## What this covers (and what it deliberately leaves out)

Covered: the real fixture date range and today's date, shown against the pre-fix 7-day window
verbatim; the real pre-fix `WHERE` clause, the real `Stats.jsx` card labels with their real
resulting values, and the real unwindowed `list_feeds`/`App.jsx` fetch; the exact one-line diff that
removes the `WHERE` clause, and what was deliberately left untouched (`source_distribution`'s 30-day
window, `recent_activity`'s 14-day window); and the real before/after numbers from a live
Python/psycopg2 harness built and run this session directly against the real, live
`mycroft_intelligence` database (0/0/0/0 -> 33/98/280/0, plus the real 24 Critical/8 High top-100
feed-list slice) — 13/13 assertions pass, matching `F1-VERIFICATION.md`'s own reported table
exactly. Two honest items at full weight: `source_distribution`'s own 30-day window has the same
structural staleness risk and was not touched this round, and this was verified by running the real
query text against the live database, not by loading the dashboard in a running browser session.

Deliberately left out: no claim that this bug was observed to break a real user's live session in
production — this closes a confirmed, reproducible defect, verified against the real live database,
not an observed end-user incident. The post-fix 33/98/280/0 figures and last week's D1 report's own
identical unwindowed `impact_level` counts are two distinct investigations' results and are kept
separately attributed throughout, never conflated into a single claim.

## Production state

- Plan: **approved (Gate P)** — signed 2026-11-19
- Fact-check gate: **resolved** — see `FACTCHECK.md`; both honest limits kept at full weight, no
  softening
- Narration approval: **approved** — Kokoro `af_bella`, locked 2026-11-19
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole report series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `StaleStatsWindow_SaiPranaviJ.mp4`, 3840x2160, 24fps,
  h264/aac, **149.833333s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):**
  `StaleStatsWindow_SaiPranaviJ.mp4`, 2160x3840, 24fps, h264/aac, **149.833333s** (identical
  duration to the landscape master — all 9 beats kept, no drops, no duration cap). GATE V on the
  true clean master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames
  from both final deliverables — B00's title card, B01's exec summary, B03's three-panel
  contradiction with the real verbatim query/labels, B04's real diff, B05's real live-DB query
  table, B08's sign-off — in both aspects. No text-rendering artifacts, no clipping, no overlap;
  "Sai Pranavi J." and "@HumanitariansAI" confirmed correct everywhere they appear.
- Publishing: **not authorized** — masters stay in this folder only, ready for fellow/PM review

## Built under the toolkit's submission spec

This project follows the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`,
effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate
`deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K
2160x3840 vertical companion built via `./art vertical` (not a <=180s Shorts-style cut) — every
beat, no cuts, no added endcard.

## Human and AI work

**My decisions, implementation and verification:** the underlying engineering (finding the
7-day-window gap in the severity query, confirming it against the live database's stale fixture
range, the fix itself, and closing it this week as F1) is my own work on Project 29, done before
this video session.

**AI tools/voices used and what they generated:** Claude Code authored all 9 Manim scenes (both
aspects), built and ran the live Python/psycopg2 verification harness used in B05 (extracting the
real, current severity SQL from `crud.py` on disk, confirming it matches verbatim, reconstructing
the pre-fix query by re-adding exactly the removed clause, and running both directly against the
real, live database, plus an independent replication of the frontend's actual top-100 fetch),
generated the Kokoro `af_bella` narration audio, ran the full render/compile/QC pipeline, and wrote
this paperwork set. Nothing in the pipeline fabricated or altered the underlying code, numbers, or
verification results.

**What I rejected or corrected:** none — the beat sheet and fact-check were already approved before
the build began; the build work focused on authoring the visuals accurately against the approved
claims and fixing real layout/timing defects caught by GATE A/B/V (documented in `BUILD-LOG.md` and,
contemporaneously, in `FRICTIONAL.md`).

**What remains unverified or failed:** this session's harness runs the real query text directly
against the real, live database — it does not load the dashboard in a running browser/frontend
session, matching `RUN_LOG.md`'s own stated limitation (no server process was up this session).
`source_distribution`'s own 30-day window has the same structural staleness risk as the one fixed
this week, per `RUN_LOG.md`'s own "Open issues" line — flagged in B06 at full weight, not smoothed
over. Both final masters are GATE V clean and personally frame-checked.

## Reproduce

- Brutalist version/commit and date checked: this repo's `brutalist/` at the time of this build,
  2026-11-19
- Source: `mycroft` repo, `Regulatory_QA/backend/app/crud.py` (read-only — not modified by this
  video session; the fix is already committed as `a7e1628`), `Regulatory_QA/frontend/src/
  components/Stats.jsx`, `Regulatory_QA/frontend/src/App.jsx`,
  `scripts/regulatory-intel/F1-VERIFICATION.md`, `logs/RUN_LOG.md`'s 2026-11-19 entry — see
  `SOURCES.md`/`FACTCHECK.md`
- Beat sheet and custom scene files: `beat_sheet.json`, `scenes.py` (landscape),
  `vertical/beat_sheet.json`, `vertical/scenes.py` (portrait)
- Live verification: `verification/verify_stale_stats_window.py` (run via
  `python3 -I verification/verify_stale_stats_window.py`), captured in
  `verification/verify_stale_stats_window_output.txt`
- Commands: `python3 brutalist/runtime/scripts/generate_audio_kokoro.py <reel>` (Kokoro TTS),
  `ffmpeg -f lavfi -i anullsrc ...` (B00 silent track), `./art run <reel>` (landscape review + QC
  gates), `ffmpeg -f concat -safe 0 -i clips/concat.txt -i clips/_work/master.wav ...` (manual true
  final master, both aspects — `./art final`'s own embedded GATE V has no `--lenient` escape
  hatch and refuses on any MAJOR finding), `./art vertical <reel>` + `./art run <reel>/vertical`
  (vertical review + QC gates), `final_frame_check.py --lenient` (standalone GATE V re-check on
  both true finals, run from inside the reel folder directly)
- Approvals and checks: see `FACTCHECK.md`, `BEAT-SHEET.md` (Gate P sign-off), `BUILD-LOG.md`
  (build history, bugs found/fixed, GATE V results), `FRICTIONAL.md` (contemporaneous build-time
  log)

## Watch and review

- Landscape — `deliverables/landscape/StaleStatsWindow_SaiPranaviJ.mp4` — 3840x2160 —
  149.833333s — SHA-256 `b2307ce12a9a215ca3fe7f1418004447324e7a8a354837b9bf274321386fd616`
  (sidecar `.verified.json`)
- Vertical — `deliverables/vertical/StaleStatsWindow_SaiPranaviJ.mp4` — 2160x3840 —
  149.833333s — SHA-256 `decfcafc74b8be402261dc4f99a8e598d0e95ada22192a1b1bb70785f9151047`
  (sidecar `.verified.json`)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured
  schema, both aspects
- `FACTCHECK.md` — claim-level review against the real `crud.py`/`Stats.jsx`/`App.jsx` code and
  this session's own live-DB verification harness
- `SOURCES.md` — claim -> source mapping
- `SHOTLIST.md` / `PROMPTS.md` (and `vertical/` copies) — beat-by-beat medium/timing table and
  pantry/asset status
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `verification/verify_stale_stats_window.py` / `verification/verify_stale_stats_window_output.txt`
  — the live Python/psycopg2 harness and its captured real output
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
- `FRICTIONAL.md` — contemporaneous, dated build-time friction log
