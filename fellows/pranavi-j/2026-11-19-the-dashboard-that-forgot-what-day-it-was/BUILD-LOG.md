# BUILD-LOG — The Dashboard That Forgot What Day It Was

## 2026-11-19 — Research and verification

**Gate P:** Beat sheet approved 2026-11-19. **FACTCHECK:** resolved same day — all claims traced to
the real, current `Regulatory_QA/backend/app/crud.py` (read-only, not modified this session, since
the fix is already committed as `a7e1628` on `feature/regulatory-intelligence-hardening`),
`Regulatory_QA/frontend/src/components/Stats.jsx`, `Regulatory_QA/frontend/src/App.jsx`,
`scripts/regulatory-intel/F1-VERIFICATION.md`, `/Users/pranavijs/mycroft/logs/RUN_LOG.md`'s
2026-11-19 entry, and this session's own live Python/psycopg2 verification harness
(`verification/verify_stale_stats_window.py`, `verification/verify_stale_stats_window_output.txt`):
the real, current severity-count SQL (confirmed to match verbatim, exactly once) and a faithful
reconstruction of the pre-fix query (re-adding exactly the removed `WHERE` clause) were run
UNCHANGED directly against the real, live `mycroft_intelligence` Postgres DB (411 rows,
`localhost:5431`) — 13/13 assertions pass, reproducing `F1-VERIFICATION.md`'s own reported numbers
exactly (0/0/0/0 -> 33/98/280/0; 24 Critical / 8 High in the real top-100 feed-list slice). See
`FACTCHECK.md` and `SOURCES.md` for the full claim-by-claim trace. See `FRICTIONAL.md` for the
real, dated build-time snags.

Confirmed via `git -C /Users/pranavijs/mycroft status --short` before and after this project's
research/verification work: identical pre-existing, unrelated diffs both times (two unrelated
`package-lock.json` files, from other, unrelated Project 29 components) — no changes to `crud.py`,
`Stats.jsx`, `App.jsx`, or `logs/RUN_LOG.md`. This session made no changes to the `mycroft` repo and
ran no `git add`/`commit`/`push` there.

## 2026-11-19 — Full build (both aspects)

**Audio:** Kokoro `af_bella`, all 9 beats. B01-B08 generated via `generate_audio_kokoro.py`
(measured durations: B01 16.512s, B02 17.640s, B03 24.168s, B04 24.840s, B05 25.368s, B06 25.488s,
B07 10.056s, B08 1.512s). B00 is a real silent mp3 (`ffmpeg anullsrc`, requested 4.05s, measured
4.104s — mp3 frame-boundary rounding, used the real measured value) with `audio_policy: "silence"`
set explicitly per `build_safety.py`'s silent-required-audio gate. Total measured runtime 149.69s
audio.

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (Pango/Cairo
small-font-size-artifact workaround), palette/helpers copied from this fellow's two closest
siblings (`2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts/scenes.py`,
`2026-11-12-the-button-that-broke-every-next-question/scenes.py`) for visual consistency. B02
contrasts the real fixture `created_at` range against today's date and the pre-fix 7-day window —
the arithmetic that guarantees zero rows. B03 shows, verbatim, the real pre-fix `WHERE` clause, the
real `Stats.jsx` card labels with their real resulting values, and the real unwindowed
`list_feeds`/`App.jsx` fetch — three stacked panels, since the bug is a contradiction between two
panels on the same page. B04 shows the real one-line diff (just the `WHERE` clause removed) plus
what was deliberately left alone. B05 shows the real before/after numbers from this session's own
live Postgres run. B06 shows both honest limits as separate full-weight cards.

**Timing verification before rendering:** wrote a standalone AST-based checker (parses every
`run_time=`/`self.wait()` literal per `Scene` class and sums it against each beat's measured
`actual_duration_s`, kept in the session scratchpad, not part of this project folder — same checker
pattern this fellow's sibling reels documented building). All 9 landscape scenes matched their
measured durations to within 4ms on the first pass — no arithmetic slip this build.

**GATE A (pre-flight):** all 9 landscape scenes and all 9 vertical scenes individually checked via
`static_scene_check.py --class <Name>` — clean, 0 warn/error for every scene, both aspects.

**GATE B / GATE V (landscape) — real defects found and fixed:**
- First `./art run` pass: GATE B (strict) found 1 real layout warning on `B02_StaleWindowHook` — its
  3-tile row (fixture date range / today / pre-fix window) was wide enough that the leftmost tile's
  text bled past the safe area's left edge (`layout_audit.md`'s own reported box:
  `[-6.31, -0.72, -3.19, -0.17]`, safe half-width 6.3). Confirmed genuine directly from the reported
  bounding box. Fixed by narrowing each tile (width 4.3->3.9, buff 0.45->0.3) and adding an explicit
  `fit(tiles, 12.0)` floor on the whole row. Re-ran `static_scene_check.py`: clean. Re-rendered.
  Second `./art run` pass: GATE B clean on all 9 beats.
- Review-slate GATE V: reported the documented burn-in-timestamp-overlay false positive
  (`frames=18 BLOCKER=18 MAJOR=0`, every frame flagged `edge-bleed`) — not trusted at face value.
  Built the true final master manually (`ffmpeg -f concat -safe 0 -i clips/concat.txt -i
  clips/_work/master.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -c:a
  aac -shortest deliverables/landscape/StaleStatsWindow_SaiPranaviJ.mp4`) and ran
  `final_frame_check.py . --mp4 deliverables/landscape/StaleStatsWindow_SaiPranaviJ.mp4 --lenient`
  from inside the reel folder.
- First true-master GATE V pass: **BLOCKER=0, MAJOR=2** — both `underfill` findings on
  `B04_OneLineFix` (content fills only 41% of the safe area, min 55%). Extracted and visually
  inspected the flagged frame before fixing anything — confirmed a real defect: the diff panel and
  the two "kept" cards were correctly centered but every element was sized too modestly relative to
  the safe width. Fixed by enlarging every font size in that beat and adding a minimum panel-width
  floor (11.4, not just content-width + padding) — the same systemic fix this fellow's sibling
  reels' own B05 underfill used. Deleted the stale `manim/B04.mp4`/`clips/B04.mp4` before
  re-rendering (stale-clips-cache gotcha). Re-ran, re-checked.
- Final true-master GATE V re-check: **BLOCKER=0, MAJOR=0**. Landscape master confirmed 3840x2160,
  24fps, 149.833333s via `ffprobe`.

**`vertical/scenes.py`:** genuine hand-authored portrait redesign for all 9 beats (rendered at true
2160x3840 / `3840p24` internally), same `T()` helper plus the portrait `config.frame_width` patch —
**verified actually applied at runtime, not just described in the docstring**, the single most
recurring toolkit bug across prior weeks' builds per the house known-bugs list. B02's 3-tile row,
B03's code-panel/stats-panel/list-panel row, and B06's 2-card row each became stacked columns;
B05's row-table became a single compact stacked-rows panel rather than side-by-side tiles.

**`./art vertical`:** scaffolded `vertical/beat_sheet.json`, correctly reusing the hand-authored
`vertical/scenes.py` and the parent's audio (byte-for-byte, via `vertical/mp3/`). The command's own
printed "ONDA CHECK BLOCKED"/"needs native portrait scene916" warnings turned out to be a generic
message `shorts.py` prints for every beat regardless of lane — confirmed harmless by checking the
actual written `vertical/beat_sheet.json` (every beat still `shot.type: GRAPHIC` with the correct
`manim.scene`) before treating it as a real blocker.

**GATE B (vertical) — a real defect found and fixed:** first `./art run .../vertical --height 3840`
pass: GATE B (strict) found 1 real layout warning on `B03_TwoPanelsDisagree` — its closing caption
bled past the portrait safe bottom edge (`layout_audit.md`'s own reported box:
`[-1.21, -3.44, ...]` / `[-1.18, -3.69, ...]`, safe half-height 3.4). The stack's 5.6 height cap
left no margin below it for the caption, once the title's real height was accounted for. Fixed by
tightening the cap to 3.9 and the caption gap/font slightly. Re-rendered: GATE B clean on all 9
beats. The fact that only this one beat was flagged (not all 9 failing underfill at 5-10% fill, the
documented systemic signature of a missing `frame_width` patch) confirmed the portrait patch was
live and working correctly this build.

**GATE V (vertical, true final master) — 3 real defects across 3 beats, all found and fixed:**
review-slate GATE V again reported the documented false positive (`frames=18 BLOCKER=18 MAJOR=0`) —
not trusted; built the true vertical master the same manual way and ran the standalone lenient
check from inside `vertical/`. First true-master pass: **BLOCKER=2, MAJOR=4**.
1. `B01_ExecSummary`: 2 BLOCKER `edge-bleed` (top/bottom). Root cause: an unsafe `7.2` height cap on
   the centered block — the real portrait title-safe budget is +/-3.4y (6.8 total), not the 8.0
   frame hard-edge, so 7.2 left no margin. The rendered frame looked fine inside this beat's own
   decorative gold frame (itself drawn taller than the real pixel-safe-area GATE V checks) — a real
   gap between "looks fine in its own decorative frame" and "inside the real safe area," confirmed
   by extracting and inspecting both flagged frames before fixing anything. Fixed by tightening the
   cap to 6.5 (and proactively applied the identical fix to `B02_StaleWindowHook`, which used the
   same unsafe value but hadn't tripped the gate this pass).
2. `B03_TwoPanelsDisagree`: 2 MAJOR `underfill` (52% fill, just under the 55% minimum). Root cause:
   `title.to_edge(UP)` had pinned the title near the top independently of the stack/caption below
   it, leaving the whole bottom half of the frame empty — the same top-anchoring defect this
   fellow's sibling reels' own B05 lesson warns against, re-introduced here instead of avoided
   proactively. Fixed by restructuring the beat to build title+stack+caption as one group and
   centering that whole group on `ORIGIN` (deferring the `Write(title)` animation until after the
   full layout was computed), plus enlarging the code/stats/list panel fonts for better fill.
3. `B08_BrandOutro`: 2 MAJOR `underfill` (43% fill). Root cause: modest fonts and tight buffs left
   most of the tall portrait frame empty. Fixed by enlarging every font size and wrapping two lines
   across more lines each (using vertical space, not just horizontal).

Deleted the stale `vertical/manim/{B01,B02,B03,B08}.mp4` and `vertical/clips/{...}.mp4` before
re-rendering. Re-ran the AST timing checker against the edited `vertical/scenes.py` first — all 9
scenes still matched their measured durations (none of these fixes touched any `run_time=`/
`self.wait()` value, only layout/sizing) — before spending render time. Final true-master GATE V
re-check: **BLOCKER=0, MAJOR=0**. Vertical master confirmed 2160x3840, 24fps, 149.833333s via
`ffprobe` — identical duration to the landscape master (every beat kept, nothing dropped, via
`./art vertical` — no cap, no rewritten outro, no added endcard).

Both final masters were personally re-inspected frame-by-frame (B00's title card, B01's exec
summary, B03's three-panel contradiction with the real verbatim query/labels, B04's real diff,
B05's real live-DB query table, B08's sign-off) directly from the shipped deliverables, in both
aspects, before considering this project done — no text-rendering artifacts, no clipping, no
overlap; "Sai Pranavi J." (never the full surname) and "@HumanitariansAI" confirmed correct
everywhere they appear.

**Deliverables:**
- `deliverables/landscape/StaleStatsWindow_SaiPranaviJ.mp4` (+ `.verified.json`, SHA-256
  `b2307ce12a9a215ca3fe7f1418004447324e7a8a354837b9bf274321386fd616`)
- `deliverables/vertical/StaleStatsWindow_SaiPranaviJ.mp4` (+ `.verified.json`, SHA-256
  `decfcafc74b8be402261dc4f99a8e598d0e95ada22192a1b1bb70785f9151047`)

## Summary — final gate results

| Aspect | Resolution | Duration | GATE V (true final master) |
|---|---|---|---|
| Landscape | 3840x2160 @ 24fps | 149.833333s | 0 BLOCKER, 0 MAJOR |
| Vertical | 2160x3840 @ 24fps | 149.833333s | 0 BLOCKER, 0 MAJOR |

No persistent/unavoidable MAJOR findings remain on either true final master — both are fully
clean. Real defects found and fixed this build: landscape B02 edge-bleed, landscape B04 underfill,
vertical B03 edge-bleed (GATE B, pre-render), vertical B01/B02 unsafe height-cap edge-bleed risk,
vertical B03 underfill (top-anchoring), vertical B08 underfill — all confirmed genuine via
extracted-frame inspection or direct bounding-box review, full narrative in `FRICTIONAL.md`.

Publishing not authorized. Nothing inside `brutalist/` was modified; nothing inside
`/Users/pranavijs/mycroft` was modified (confirmed via `git status --short` before and after this
session — only pre-existing, unrelated changes from before this session were present both times).
