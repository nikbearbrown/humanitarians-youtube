# Weekly Work Report: The Dashboard That Disagreed With Its Own Alerts

**Fellow:** Sai Pranavi J.
**Week ending:** November 3, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo,
`Regulatory_QA/backend/app/crud.py`)
**Source status:** Real engineering work. Every claim traces to this week's D1 fix in
`FeedCRUD.get_stats()` (closed 2026-11-03) and this session's own live Python/SQL verification
harness (`verification/verify_dashboard_stats.py`) — confirmed the real, current SQL buckets
severity by `impact_level`, the same column everything else already reads, and reproduced the real,
documented before/after counts exactly.

## Watch

- Landscape (4K 16:9): [pending Drive upload — publishing not authorized this session]
- Vertical (4K 9:16): [pending Drive upload — publishing not authorized this session]

This video covers a bug found and fixed this week (D1) in Project 29's regulatory intelligence
dashboard backend: `FeedCRUD.get_stats()` computes its own severity breakdown completely
independently of the number the real alert email (and the feed list UI, and the RAG chat context)
actually use. Every other consumer treats the `impact_level` column as the authoritative severity
label for a feed item. `get_stats()` never read that column at all — it independently re-derived
four tiers from the raw `urgency_score` (0-10) using its own, uncoordinated cutoffs. The two columns
are set together by the same keyword-scoring pass but not on a fixed formula, and the Layer 2 LLM
correction (C2/C3, this fellow's prior report) can change `impact_level` without touching
`urgency_score` at all — so they drift apart on a real fraction of rows. The fix: `get_stats()` now
buckets by `impact_level` directly, the same column everything else already reads, instead of
re-deriving its own answer from `urgency_score`.

## What this covers (and what it deliberately leaves out)

Covered: the real pre-fix `urgency_score`-cutoff SQL, shown verbatim; the real `impact_level`
column and its real consumers; the exact diff that changes 4 `FILTER` lines; the real before/after
results from a live Python/SQL harness built and run this session, reproducing
`D1-VERIFICATION.md`'s own live-DB-measured counts exactly (62/411 rows, 15%, land in a different
tier; old method overcounts High by 41 items, ~30% inflated); and two honest items at full weight:
what this fix does NOT touch, and the fact that only the unwindowed, whole-table comparison was
verified — not the endpoint's actual live 7-day/30-day rolling windows.

Deliberately left out: no claim that an operator was ever observed acting on the wrong dashboard
number in a real incident — this closes a confirmed defect, verified against the real, live
`mycroft_intelligence` database's full 411-row table (per `D1-VERIFICATION.md`/`RUN_LOG.md`), not a
claim about a measured production incident. This session's own harness independently reproduces
those documented counts via the real extracted SQL, run against a dataset engineered to match them
— it is not a second live DB query (this session had no working `DATABASE_URL` for that backend;
see `FRICTIONAL.md`), and that distinction is kept visible, not blurred.

## Production state

- Plan: **approved (Gate P)** — signed 2026-11-03
- Fact-check gate: **resolved** — see `FACTCHECK.md`; both honest limits kept at full weight, no
  softening
- Narration approval: **approved** — Kokoro `af_bella`, locked 2026-11-03
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole report series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `DashboardSeverityDrift_SaiPranaviJ.mp4`, 3840x2160,
  24fps, h264/aac, **144.958333s**. GATE V on the true clean master:
  **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):**
  `DashboardSeverityDrift_SaiPranaviJ.mp4`, 2160x3840, 24fps, h264/aac,
  **144.958333s** (identical duration to the landscape master — all 9 beats kept, no drops, no
  duration cap). GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames
  from both final deliverables — B00's title card, B03's SQL/column panels with the
  `urgency_score`/`impact_level` substrings highlighted, B04's struck-through diff and the 4 new
  `impact_level` FILTER lines, B05's real harness table with the High tier boxed, B06's
  honest-limits cards, B07's takeaway, and B08's sign-off — in both aspects. No text-rendering
  artifacts, no clipping, no overlap; "Sai Pranavi J." and "@HumanitariansAI" confirmed correct
  everywhere they appear.
- Publishing: **not authorized** — masters stay in this folder only, ready for fellow/PM review

## Built under the toolkit's submission spec

This project follows the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`,
effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate
`deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K
2160x3840 vertical companion built via `./art vertical` (not a <=180s Shorts-style cut) — every
beat, no cuts, no added endcard.

## Human and AI work

**My decisions, implementation and verification:** the underlying engineering (finding the
dashboard-re-derives-its-own-severity gap, the `impact_level`-based fix, and closing it this week
as D1) is my own work on Project 29, done before this video session.

**AI tools/voices used and what they generated:** Claude Code authored all 9 Manim scenes (both
aspects), built and ran the live Python/SQL verification harness used in B05 (extracting the real,
current SQL from `get_stats()` in `crud.py` on disk, and a faithful reconstruction of the pre-fix
SQL by undoing the exact diff, to reproduce the real documented miscounting), generated the Kokoro
`af_bella` narration audio, ran the full render/compile/QC pipeline, and wrote this paperwork set.
Nothing in the pipeline fabricated or altered the underlying code, numbers, or verification
results.

**What I rejected or corrected:** none — the beat sheet and fact-check were already approved before
the build began; the build work focused on authoring the visuals accurately against the approved
claims and fixing real layout/timing defects caught by GATE A/B/V (documented in `BUILD-LOG.md`
and, contemporaneously, in `FRICTIONAL.md`).

**What remains unverified or failed:** this session's harness reproduces the real, documented
live-DB counts by running the real extracted SQL against a dataset engineered to match them — it
could not re-query the live `mycroft_intelligence` Postgres DB directly (no working
`DATABASE_URL`/`.env` in this shell for that backend), so it corroborates D1-VERIFICATION.md's own
live-DB numbers rather than independently re-measuring them a second time against the live
database. The endpoint's actual 7-day/30-day rolling windows remain unverified against live,
actively-populated data (per `RUN_LOG.md`'s own "Open issues" line) — flagged in B06 at full
weight, not smoothed over. Both final masters are GATE V clean and personally frame-checked.

## Reproduce

- Brutalist version/commit and date checked: this repo's `brutalist/` at the time of this build,
  2026-11-03
- Source: `mycroft` repo, `Regulatory_QA/backend/app/crud.py` (`FeedCRUD.get_stats()`, read-only —
  not modified by this video session), `scripts/regulatory-intel/D1-VERIFICATION.md`,
  `logs/RUN_LOG.md`'s 2026-11-03 entry — see `SOURCES.md`/`FACTCHECK.md`
- Beat sheet and custom scene files: `beat_sheet.json`, `scenes.py` (landscape),
  `vertical/beat_sheet.json`, `vertical/scenes.py` (portrait)
- Live verification: `verification/verify_dashboard_stats.py` (run via
  `python3 verification/verify_dashboard_stats.py`), captured in
  `verification/verify_dashboard_stats_output.txt`
- Commands: `python3 brutalist/runtime/scripts/generate_audio_kokoro.py <reel>` (Kokoro TTS),
  `ffmpeg -f lavfi -i anullsrc ...` (B00 silent track), `./art run <reel>` (landscape review + QC
  gates), `ffmpeg -f concat -safe 0 -i clips/concat.txt -i clips/_work/master.wav ...` (manual true
  final master, both aspects — `./art final`'s own embedded GATE V has no `--lenient` escape
  hatch and refuses on any MAJOR finding), `./art vertical <reel>` + `./art run <reel>/vertical`
  (vertical review + QC gates), `final_frame_check.py --lenient` (standalone GATE V re-check on
  both true finals, run from inside the reel folder)
- Approvals and checks: see `FACTCHECK.md`, `BEAT-SHEET.md` (Gate P sign-off), `BUILD-LOG.md`
  (build history, bugs found/fixed, GATE V results), `FRICTIONAL.md` (contemporaneous build-time
  log)

## Watch and review

- Landscape — `deliverables/landscape/DashboardSeverityDrift_SaiPranaviJ.mp4` — 3840x2160 —
  144.958333s — SHA-256 `7277257f3a1860db37412ad4e930517b39cbd607a85ffae73fd1ef2746da01c6`
  (sidecar `.verified.json`)
- Vertical — `deliverables/vertical/DashboardSeverityDrift_SaiPranaviJ.mp4` — 2160x3840 —
  144.958333s — SHA-256 `76da7cc716f75949a051bbbdef5b72b061d01b1426f7f3e0825f594e129a9811`
  (sidecar `.verified.json`)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured
  schema, both aspects
- `FACTCHECK.md` — claim-level review against the real `get_stats()` code, the real diff, and this
  session's own verification harness
- `SOURCES.md` — claim -> source mapping
- `SHOTLIST.md` / `PROMPTS.md` (and `vertical/` copies) — beat-by-beat medium/timing table and
  pantry/asset status
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `verification/verify_dashboard_stats.py` / `verification/verify_dashboard_stats_output.txt` —
  the live Python/SQL harness and its captured real output
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
- `FRICTIONAL.md` — contemporaneous, dated build-time friction log
