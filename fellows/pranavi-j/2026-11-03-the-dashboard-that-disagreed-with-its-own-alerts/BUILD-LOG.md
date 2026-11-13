# BUILD-LOG — The Dashboard That Disagreed With Its Own Alerts

## 2026-11-03 — Research and verification

**Gate P:** Beat sheet approved 2026-11-03. **FACTCHECK:** resolved same day — all claims traced to
the real, current `Regulatory_QA/backend/app/crud.py` (`FeedCRUD.get_stats()`, read-only, not
modified this session), `scripts/regulatory-intel/D1-VERIFICATION.md`,
`/Users/pranavijs/mycroft/logs/RUN_LOG.md`'s 2026-11-03 entry, and this session's own live Python/
SQL verification harness (`verification/verify_dashboard_stats.py`,
`verification/verify_dashboard_stats_output.txt`): the real, current SQL (post-fix) reproduces
D1-VERIFICATION.md's own reported counts exactly (Critical 33 / High 98 / Medium 280 / Low 0), and
a reconstruction of the pre-fix SQL (built by undoing the exact documented diff) reproduces the old
counts exactly (Critical 32 / High 139 / Medium 240 / Low 0) — 62 of 411 rows (15%) land in a
different tier, old method overcounting High by 41 items (~30% inflated). All 13 harness assertions
pass. See `FACTCHECK.md` and `SOURCES.md` for the full claim-by-claim trace. See `FRICTIONAL.md` for
the real, dated build-time snags (including the attempt to query the live DB directly, which hit a
missing-`DATABASE_URL` settings-chain wall, and the pivot to the extract-and-reconstruct harness
pattern).

Confirmed via `git -C /Users/pranavijs/mycroft status --short` before and after this project's
research/verification work: identical pre-existing, unrelated diffs both times (`logs/RUN_LOG.md`,
two unrelated `package-lock.json` files, and `Regulatory_QA/backend/app/crud.py` itself — all from
the real D1 engineering work already done before this video session) plus the untracked
`D1-VERIFICATION.md`. This session made no changes to the `mycroft` repo.

## 2026-11-03 — Full build (both aspects)

**Audio:** Kokoro `af_bella`, all 9 beats. B01-B08 generated via `generate_audio_kokoro.py`
(measured durations: B01 14.28s, B02 17.95s, B03 24.12s, B04 17.88s, B05 24.55s, B06 29.11s,
B07 11.28s, B08 1.51s). B00 is a real silent mp3 (`ffmpeg anullsrc`, requested 4.05s, measured
4.10s — mp3 frame-boundary rounding, used the real measured value) with `audio_policy: "silence"`
set explicitly per `build_safety.py`'s silent-required-audio gate. Total measured runtime 144.78s
audio.

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (Pango/Cairo
small-font-size-artifact workaround), copied from this fellow's closest sibling
(`2026-10-27-the-correction-that-never-reached-the-email/scenes.py`) for visual consistency. B03
shows the real pre-fix `urgency_score` cutoff SQL, verbatim, next to the real `impact_level` column
every other consumer (alert email, feed list UI, RAG chat context) already reads, with the
`urgency_score`/`impact_level` substrings isolated via Manim `Text` character-index slicing (no
re-creation, no paraphrase) and boxed crimson/sage. B04 shows the real diff adding the 4
`impact_level`-based `FILTER` lines (struck-through before, added after, exactly as in
`D1-VERIFICATION.md`'s "The fix"). B05 shows the real before/after harness results (Critical 32->33,
High 139->98, Medium 240->280, Low 0->0; 62/411, 15%; High overcounted 41/~30%) from this session's
own run. B06 shows both honest limits as separate full-weight cards.

**Timing verification before rendering:** wrote a standalone AST-based checker (parses every
`run_time=`/`self.wait()` literal per `Scene` class and sums it against each beat's measured
`actual_duration_s`, kept in the session scratchpad, not part of this project folder — same
checker pattern this fellow's sibling reels documented building). All 9 landscape scenes matched
their measured durations exactly on the first pass. The first vertical draft had one real
arithmetic slip in `B05_HarnessTable` (summed 24.85s against a measured 24.55s target); fixed by
reducing the final `self.wait()` remainder by 0.3s — see `FRICTIONAL.md` for the root cause.

**GATE A (pre-flight):** all 9 landscape scenes and all 9 vertical scenes individually checked via
`static_scene_check.py --class <Name>` — clean, 0 warn/error on the first pass for every scene, both
aspects. GATE A did catch one real bug mid-build, though not on the first pass: see "GATE V" below,
`B03`'s highlight fix attempt 2 (Manim's `.chars` property) hard-failed GATE A's render-free stub
(`TypeError: 'function' object is not subscriptable`) because that stub doesn't implement `.chars` —
correctly blocking an approach that, while valid against real Manim, was incompatible with this
toolkit's own pre-flight check.

**GATE B / GATE V (landscape) — real defects found and fixed:**
- `B05_HarnessTable`: GATE V on the true final master (never the review slate, which carries the
  documented burn-in-overlay false positive — `frames=18 BLOCKER=18 MAJOR=0` on every sampled
  frame, confirmed via extracted-frame inspection) found a real `underfill`: content filled only
  50% of the safe area (min 55%) at both sampled points. Root cause: the scene pinned its title to
  the top edge and chained every other element below it via `next_to()`, clustering everything in
  the top ~45% of the frame. Fixed by enlarging the tile/type sizes AND restructuring the whole
  beat (title through closing caption) into one `VGroup(...).arrange(DOWN, ...).move_to(ORIGIN)`,
  vertically centered rather than top-anchored — applied the same fix proactively to
  `vertical/scenes.py`'s own B05 before ever rendering it.
- `B03_OneQueryOneColumn`: a real correctness bug caught by personal frame inspection, not by any
  automated gate (GATE A/B/V only check layout/overlap/fill, not whether a highlighted substring is
  the RIGHT substring) — the crimson "urgency_score" highlight box landed 1-2 characters late
  (boxing "rgency_score >=" instead of "urgency_score"), because the scene sliced the `Text`
  mobject directly by python string index, and Manim's `Text` doesn't give whitespace its own
  submobject, so the index silently drifts once any space precedes the slice. Took three attempts
  to fix correctly (full narrative, including the GATE-A-incompatible `.chars` attempt, in
  `FRICTIONAL.md`): the final fix uses Manim's own `t2c={needle: color}` constructor parameter
  (correct against real Manim, and GATE-A-safe since the toolkit's render-free stub silently
  ignores unrecognized kwargs) and boxes the WHOLE line instead of just the substring, since there
  is no cheap GATE-A-safe way to get a sub-mobject handle for just the `t2c`-colored span.
All of the above are genuine measured/observed defects (re-confirmed by extracting and personally
viewing the actual frames), not false positives.

**Landscape final:** 3840x2160, 24fps, h264/aac, 144.958333s. `final_frame_check.py --lenient` on
the true final master: **0 BLOCKER, 0 MAJOR.** Confirmed via `ffprobe`. Personally re-inspected
spot-check frames across the full timeline (B00 title, B03's fixed highlight, B04's diff, B05's
re-centered harness table, B06's honest-limit cards) directly from the shipped deliverable before
moving on to the vertical build.

**`vertical/scenes.py`:** genuine hand-authored portrait redesign for all 9 beats (rendered at true
2160x3840 / `3840p24` internally), same `T()` helper plus the portrait `config.frame_width` patch
(copied verbatim from this fellow's sibling reels' documented fix). B02's 2-tile row, B03's
code-panel/column-readers row, and B06's 2-card row each became stacked columns; B05's 4
side-by-side tier tiles were redesigned as ONE compact table-style panel (header + 4 rows) rather
than a literal vertical stack of 4 bordered tiles, to fit the same measured beat duration's worth of
content inside this frame's narrower safe area. The landscape build's B05 centering fix and B03
`t2c` highlight fix were both applied to this file proactively, before ever rendering it.

**`./art vertical`:** scaffolded `vertical/beat_sheet.json`, correctly reusing the hand-authored
`vertical/scenes.py` and the parent's audio (byte-for-byte, via `vertical/mp3/`). First
`./art run vertical --height 3840` pass: GATE B failed on `B02_DashboardVsEmailHook` — 2 real WARNs
(title top edge at y=3.48, zinger bottom edge at y=-3.48, both just outside the +/-3.4 safe
half-height once centered at the original `buff=0.7`). Fixed by tightening the top-level arrange
buff to 0.55. Re-ran: GATE B clean, all 9 beats slotted. Review-slate GATE V reported the same
known burn-in false positive (`BLOCKER=18 MAJOR=0`) as the landscape pass — not trusted at face
value. Built the true final vertical master manually and ran
`final_frame_check.py vertical --mp4 deliverables/vertical/DashboardSeverityDrift_SaiPranaviJ.mp4
--lenient`: **BLOCKER=0, MAJOR=0** — clean on the first true-master pass (the B05-centering and B03
`t2c` fixes, applied proactively before this aspect's first render, meant neither of the landscape
build's two defects needed rediscovering here).

**Vertical final:** 2160x3840, 24fps, h264/aac, 144.958333s — **identical duration to the landscape
master** (same timeline, every beat kept, nothing dropped, via `./art vertical` — no cap, no
rewritten outro, no added endcard). `final_frame_check.py --lenient` on the true final master:
**0 BLOCKER, 0 MAJOR.**

Both final masters were personally re-inspected frame-by-frame (B00's title card, B02's
dashboard-vs-email tiles, B03's corrected "urgency_score" highlight with real spacing intact, B04's
struck-through diff and the 4 new `impact_level` FILTER lines, B05's re-centered/redesigned harness
table, B06's honest-limit cards, B07's takeaway, and B08's sign-off) directly from the shipped
deliverables, in both aspects, before considering this project done — no text-rendering artifacts,
no clipping, no overlap; "Sai Pranavi J." (never the full surname) and "@HumanitariansAI" confirmed
correct everywhere they appear.

**Deliverables:**
- `deliverables/landscape/DashboardSeverityDrift_SaiPranaviJ.mp4` (+ `.verified.json`, SHA-256
  `7277257f3a1860db37412ad4e930517b39cbd607a85ffae73fd1ef2746da01c6`)
- `deliverables/vertical/DashboardSeverityDrift_SaiPranaviJ.mp4` (+ `.verified.json`, SHA-256
  `76da7cc716f75949a051bbbdef5b72b061d01b1426f7f3e0825f594e129a9811`)

## Summary — final gate results

| Aspect | Resolution | Duration | GATE V (true final master) |
|---|---|---|---|
| Landscape | 3840x2160 @ 24fps | 144.958333s | 0 BLOCKER, 0 MAJOR |
| Vertical | 2160x3840 @ 24fps | 144.958333s | 0 BLOCKER, 0 MAJOR |

No persistent/unavoidable MAJOR findings remain on either true final master — both are fully
clean. Three real bugs were found and fixed this build (landscape B05 underfill, vertical B02
safe-area overflow, landscape/vertical-shared B03 substring-highlight indexing defect — the last
took three attempts; full narrative in `FRICTIONAL.md`), all confirmed genuine via extracted-frame
inspection, none dismissed as false positives without that inspection.

Publishing not authorized. Nothing inside `brutalist/` was modified; nothing inside
`/Users/pranavijs/mycroft` was modified (confirmed via `git status --short` before and after this
session — only pre-existing, unrelated changes from before this session were present both times).
