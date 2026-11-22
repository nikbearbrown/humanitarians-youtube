# Frictional log — The Dashboard That Forgot What Day It Was

Contemporaneous build-time log. Written as things happen, not reconstructed afterward.

## 2026-11-19

- **Start.** Reading `F1-VERIFICATION.md` and `RUN_LOG.md`'s 2026-11-19 entry for F1. This is a
  time-window defect, not a column-choice defect like D1 (2026-11-03) — different root cause,
  same `get_stats()` function, same dashboard. Framing this reel around "forgot what day it was"
  (hardcoded 7-day window vs. 4-months-stale fixture data) to keep it visually/tonally distinct
  from D1's "disagreed with its own alerts" (impact_level vs. urgency_score column mismatch).
- Read `crud.py`'s real `get_stats()` on disk directly — confirmed the already-committed fix
  (commit `a7e1628`, `feature/regulatory-intelligence-hardening`) is in place: the severity query
  has no `WHERE created_at` clause at all now, and the code comment above it explicitly says why
  (points at F1-VERIFICATION.md). `source_distribution` still has its 30-day window,
  `recent_activity` still has its 14-day window — both deliberately untouched, matching the
  verification doc.
- Confirmed read-only: `git -C /Users/pranavijs/mycroft status --short` shows only two unrelated
  `package-lock.json` diffs in Goal_Setting_System/Insider_Trading_System — nothing in
  Regulatory_QA, nothing touched by this video session. Branch is
  `feature/regulatory-intelligence-hardening`, `a7e1628` is HEAD-ish (confirmed via `git log
  --oneline -3`). This video build will not run any git command in the mycroft repo per the hard
  constraint.
- **Live DB reachable this week** (unlike D1's session, which had no working `DATABASE_URL` and
  fell back to a synthetic sqlite reconstruction — see
  `2026-11-03-.../verification/verify_dashboard_stats.py`'s own docstring). `PGPASSWORD=postgres
  psql -h localhost -p 5431 -U postgres -d mycroft_intelligence` connects cleanly. Wrote
  `verification/verify_stale_stats_window.py` to run the REAL pre-fix/post-fix query text
  directly against the live 411-row table via psycopg2, not a reconstruction. Ran it — all 13
  assertions pass, numbers match `F1-VERIFICATION.md` exactly: 0/0/0/0 -> 33/98/280/0. Also
  independently replicated `list_feeds()`'s actual ordering/limit (`ORDER BY created_at DESC,
  urgency_score DESC`, frontend's real `limit: 100` from `App.jsx`) against the live DB: top-100
  slice is 24 Critical / 8 High — matches the verification doc's claimed panel-vs-panel
  contradiction concretely, not just by inspecting query text.
- Confirmed `Stats.jsx`'s real on-screen label text verbatim for the hook/setup beats: "Total
  Feeds", "Critical", "High Priority", "Selected" (`StatCard` components) — these are the exact
  strings that will appear quoted on screen, not paraphrased.
- Also confirmed `list_feeds`'s real `ORDER BY created_at DESC, urgency_score DESC` clause and
  `App.jsx`'s real `feedsAPI.listFeeds({ limit: 100 })` call verbatim, and independently verified
  the frontend's real top-100 slice (24 Critical / 8 High) against the live DB directly (not just
  quoting `F1-VERIFICATION.md`'s claim) before writing it into any beat.

- Generated Kokoro `af_bella` audio for B01-B08 via `generate_audio_kokoro.py` — measured durations
  (B00 silent via `ffmpeg anullsrc`, requested 4.05s, measured 4.104s — same mp3 frame-boundary
  rounding this fellow's sibling reels documented, used the real measured value): B01 16.512s, B02
  17.640s, B03 24.168s, B04 24.840s, B05 25.368s, B06 25.488s, B07 10.056s, B08 1.512s. Wrote an
  AST-based timing checker (scratchpad, not part of this project folder) that sums every
  `run_time=`/`self.wait()` literal per Scene class and compares it to these measured durations —
  all 9 landscape scenes matched to within 4ms on the first pass.

- **Landscape GATE B (real defect):** first `./art run` pass failed GATE B (strict) on
  `B02_StaleWindowHook` — a real layout warning, not a false positive: the 3-tile row (fixture
  date range / today / pre-fix window) was wide enough that its leftmost tile's text bled past the
  safe area's left edge (`box=[-6.31, ...]`, safe half-width 6.3). Confirmed genuine directly from
  `layout_audit.md`'s own reported bounding box. Fixed by narrowing each tile (width 4.3->3.9, buff
  0.45->0.3) and adding an explicit `fit(tiles, 12.0)` floor on the whole row, rather than shrinking
  only the one offending tile. Re-rendered: GATE B clean.

- **Landscape GATE V on the review slate — expected false positive, not trusted at face value:**
  `[gate-v] frames=18 BLOCKER=18 MAJOR=0` — every single sampled frame flagged `edge-bleed`, the
  documented burn-in-timestamp-overlay false-positive signature this toolkit's known bugs describe.
  Built the true final master manually instead (`ffmpeg -f concat -safe 0 -i clips/concat.txt -i
  clips/_work/master.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -c:a
  aac -shortest deliverables/landscape/StaleStatsWindow_SaiPranaviJ.mp4`) and ran
  `final_frame_check.py . --mp4 deliverables/landscape/StaleStatsWindow_SaiPranaviJ.mp4 --lenient`
  from inside the reel folder, per the documented workaround (`./art final`'s own embedded GATE V
  has no `--lenient` escape hatch).

- **Landscape GATE V on the TRUE master — a real defect found and fixed:** first pass:
  `BLOCKER=0, MAJOR=2`, both `underfill` on `B04_OneLineFix` (41% safe-area fill, min 55%).
  Extracted and visually inspected the flagged frame before fixing anything — confirmed real: the
  diff panel and the two "kept" cards were centered correctly but sized far too modestly relative
  to the safe width, leaving a large empty band around them. Fixed by enlarging every font size in
  that beat (16->22 for the diff lines, 15->19 for the kept cards) and adding a minimum panel-width
  floor (11.4, not just content-width + padding) — the same systemic fix this fellow's sibling
  reels' own B05 underfill used. Deleted the stale `manim/B04.mp4` and `clips/B04.mp4` before
  re-rendering (per this toolkit's documented stale-clips-cache gotcha — a diagnostic re-render
  that doesn't show up in the next assembly is a stale cached clip, not a failed re-render). Second
  GATE V pass on the rebuilt true master: `BLOCKER=0, MAJOR=0`. Landscape master confirmed
  3840x2160, 24fps, 149.833333s via `ffprobe`.

- **Vertical `config.frame_width` patch — verified, not just copied as a comment:** before trusting
  this file's portrait math, confirmed `config.frame_width`/`config.frame_height` were actually
  being set to the portrait values at runtime (not just described in the module docstring) — the
  single most recurring toolkit bug across prior weeks' builds per the house known-bugs list.
  First `./art run .../vertical --height 3840` pass's GATE B result (only 2 localized warnings, not
  all 9 beats failing underfill at 5-10% fill) confirmed the patch was live and working, not the
  systemic "forgot to apply it" failure mode.

- **Vertical GATE B (real defect):** `B03_TwoPanelsDisagree`'s portrait redesign (code/stats/list
  panels stacked, then a caption below) failed GATE B — the caption bled past the bottom safe edge
  (`box=[..., -3.69]`, safe half-height 3.4). The stack's 5.6 height cap left no margin for the
  caption below it once the title's real height was accounted for. Fixed by tightening the cap to
  3.9 and the caption gap/font slightly. Re-rendered: GATE B clean.

- **Vertical GATE V on the review slate — same documented false positive:**
  `frames=18 BLOCKER=18 MAJOR=0`, identical signature to the landscape slate. Not trusted; built the
  true vertical master the same manual way (`vertical/clips/concat.txt` + `vertical/clips/_work/
  master.wav`) and ran the standalone lenient check from inside `vertical/`.

- **Vertical GATE V on the TRUE master — 3 real defects across 3 beats, all found and fixed:**
  first pass: `BLOCKER=2, MAJOR=4`.
  1. `B01_ExecSummary`: 2 BLOCKER `edge-bleed` (top/bottom). Root cause: an unsafe `7.2` height cap
     on the centered block — the real title-safe budget for portrait is +/-3.4y (6.8 total), not
     the 8.0 frame hard-edge, so 7.2 left no margin. Extracted and inspected both flagged frames;
     the rendered image looked fine inside this beat's own decorative gold frame, which is itself
     drawn taller than the pixel-safe-area GATE V actually checks — a real, non-obvious gap between
     "looks fine in the decorative frame" and "inside the real safe area." Fixed by tightening the
     cap to 6.5 (and proactively applied the same fix to `B02_StaleWindowHook`, which used the same
     unsafe 7.2 value but hadn't tripped the gate this pass).
  2. `B03_TwoPanelsDisagree`: 2 MAJOR `underfill` (52% fill, just under the 55% minimum).
     Root cause: `title.to_edge(UP)` had pinned the title near the top independently of the stack/
     caption below it, leaving the whole bottom half of the frame empty — the same top-anchoring
     defect this fellow's sibling reels' own B05 lesson warns against, re-introduced here in a new
     beat instead of being avoided proactively. Fixed by restructuring the beat to build
     title+stack+caption as one group and centering that whole group on `ORIGIN` (deferring the
     `Write(title)` animation until after the full layout was computed), plus enlarging the code/
     stats/list panel fonts (13->16) for better fill.
  3. `B08_BrandOutro`: 2 MAJOR `underfill` (43% fill). Root cause: modest fonts and tight buffs on a
     short 4-line block left most of the tall portrait frame empty. Fixed by enlarging every font
     size, wrapping "explained with Claude Code" and "in for Sai Pranavi J." across 2 lines each
     (more vertical space used, not just horizontal), and widening buffs between lines.
  Deleted the stale `vertical/manim/{B01,B02,B03,B08}.mp4` and `vertical/clips/{...}.mp4` before
  re-rendering. Re-ran the AST timing checker against the edited `vertical/scenes.py` first — all 9
  scenes still matched their measured durations (none of these fixes touched any `run_time=`/
  `self.wait()` value, only layout/sizing) — before spending render time. Second GATE V pass on the
  rebuilt true vertical master: `BLOCKER=0, MAJOR=0`. Vertical master confirmed 2160x3840, 24fps,
  149.833333s via `ffprobe` — identical duration to the landscape master (all 9 beats kept, no
  drops, via `./art vertical`).

- Personally re-inspected extracted frames from both final true masters (B00's title card, B01's
  exec summary, B03's three-panel contradiction with the real verbatim query/labels, B04's real
  diff, B05's real live-DB query table, B08's sign-off) in both aspects before considering this done
  — no text-rendering artifacts, no clipping, no overlap; "Sai Pranavi J." (never the full surname)
  and "@HumanitariansAI" confirmed correct everywhere they appear.

- Confirmed `/Users/pranavijs/mycroft` was not modified at any point this session: `git -C
  /Users/pranavijs/mycroft status --short` shows only the same two pre-existing, unrelated
  `package-lock.json` diffs (Goal_Setting_System, Insider_Trading_System) at both the start and end
  of this build — nothing in `Regulatory_QA`, no new commits, no `git add`/`commit`/`push` run by
  this session.
