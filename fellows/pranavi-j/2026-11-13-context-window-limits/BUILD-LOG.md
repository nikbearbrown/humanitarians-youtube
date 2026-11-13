# BUILD-LOG — Context Window Limits: The Budget That Doesn't Grow

## 2026-11-13 — Landscape build

**Gate P:** Beat sheet approved 2026-11-13. **FACTCHECK:** resolved same day — the mechanism
(fixed-size context windows and their two broad overflow patterns, generically stated), the
worked example (an invented, illustrative 1,000-token budget scenario), and the falsifiability
case (the identical scenario with an explicit-error system added) all confirmed fully qualitative,
no real model/vendor named, no specific context-window size claimed as universal, with overflow
claims kept hedged and generic per the well-documented architectural facts about transformer-based
language models. Confirmed distinct from this fellow's eight prior videos: prompt injection,
embeddings, RAG grounding, hallucination, tokenization, lost-in-the-middle, chain-of-thought
faithfulness, calibration, in-context learning limits, and Goodhart's Law / proxy metrics —
particular care taken distinguishing from in-context learning limits, the closest adjacent topic.

**Audio:** Kokoro `af_bella`, all 8 spoken beats generated via `generate_audio_kokoro.py --only
B01 B02 B03 B04 B05 B06 B07 B08` in one pass (no retries needed). B00 a real silent mp3 (`ffmpeg
anullsrc`, requested 4.1s, measured via ffprobe at 4.128s — intended as the real measured value,
not the requested one). An `Edit` meant to hand-write that 4.128s into B00's `actual_duration_s`
instead collided with a value `generate_audio_kokoro.py` had already written for the same
skipped/silent beat (it defaults silent beats' `actual_duration_s` to their
`estimated_duration_s`, 4, rather than leaving the field unset) — the edit inserted a duplicate
JSON key instead of replacing it, and the later-occurring, Kokoro-written `4` silently won on
every parse thereafter (see `FRICTIONAL.md` for the full root-cause trace, found only after the
build while re-confirming numbers for this log). Net effect: B00's silent title card plays 4.0s,
not the originally-intended 4.128s — a real but harmless 0.128s trim off an already-long static
hold on a SILENT beat, confirmed to have had no visible effect on either final master.
`actual_duration_s` for the 8 spoken beats written back automatically from real Kokoro
measurements: B01=16.49 B02=22.61 B03=34.10 B04=31.75 B05=24.79 B06=28.13 B07=14.16 B08=1.51 —
total with B00 as actually used by the pipeline (4.0): 177.54s narration/silence.

**`scenes.py` (landscape):** authored with the `T()` safe-text helper for every on-screen string,
and the `PALETTE`/`fit()`/`panel()`/`box_around()`/`stat_row()`/`metric_panel()` helpers copied
verbatim from the Goodhart's Law reel for visual/house-style continuity across the series. B03
shows all 3 tests (Count the Tokens / Share the Pool / Watch the Edge) fully, before any example,
per the Legibility Contract. B04/B05 share the exact same budget-panel composition, the exact same
token counts (850 fixed + conversation history growing from 150 to 310 against a 1,000-token
budget), and the exact same overflow condition, isolating the one variable the rubric's own test
(#3, Watch the Edge) names — whether the system checks the total before answering.

### Real findings during this build

1. **A real GATE B layout bug on B02, caught correctly on the first automated pass (not a false
   positive):** `correct_tag` ("NOT WORDS EITHER"), positioned via `next_to(trend_block, RIGHT,
   buff=2.9)`, landed outside the safe area (box x up to 7.04 against a ±6.3 safe half-width).
   First fix attempt made it worse — chaining the trailing tags further RIGHT off each other with
   smaller buffs pushed the same tag past the hard frame edge instead (box x up to 7.54 against
   the 7.11 frame edge), because chaining several independently-`next_to`'d short text mobjects
   rightward off an already-centered anchor accumulates drift with nothing recentering the row.
   Real fix: restructured the two trailing tags to stack DOWN off `trend_block` instead (each one
   individually centers at x=0), matching the pattern this file's structure-card beats already
   use. Re-ran: GATE A/B/W clean. See `FRICTIONAL.md` for the full blow-by-blow.
2. **GATE A/W clean on all 9 beats; GATE B clean on 8/9 on the first attempt, 9/9 on the second**
   (after the B02 fix above) — no further layout-audit failures.
3. **Manim rendered at true native 3840x2160 regardless of `run.sh`'s `--height 480` flag**
   (confirmed directly via `ffprobe` on `manim/B0N.mp4` files, matching both sibling reels'
   documented finding): the fast low-res QC pass therefore produced true-4K Manim renders and true
   GATE A/B results on the first attempt for 8/9 beats.
4. **Expected review-slate GATE V false positive, matching both sibling reels' documented finding
   exactly:** the review slate's GATE V (`run.sh`'s embedded check against the `-slate.mp4` review
   cut) reported **18 BLOCKER / 0 MAJOR** — the documented burn-in global-timecode overlay pattern
   (2 per beat x 9 beats), not a real defect in the scene content. Per the documented workaround,
   did NOT trust this result and verified directly against the TRUE final candidate before
   accepting anything as clean.
5. **The TRUE final landscape candidate passed GATE V clean on the FIRST attempt — 0 BLOCKER, 0
   MAJOR, no fix cycle needed:** built via `./art final <reel> --out deliverables/landscape`
   directly (true 4K, no `--review` flag, so no burn-in strip). `FACTCHECK.md`/`SHOTLIST.md`/
   `PROMPTS.md` all existed, so `compile.py`'s own embedded GATE V step (no `--lenient`, any
   BLOCKER *or* MAJOR refuses the write) ran to completion and wrote the candidate without
   raising — the documented manual `ffmpeg -f concat` reconstruction workaround was not needed
   this build. Independently re-ran `final_frame_check.py --lenient` directly against the written
   candidate as explicit confirmation, never trusting the embedded step's silent success alone:
   **0 BLOCKER, 0 MAJOR.**
6. **A non-blocking motion-histogram warning, expected for an all-Manim reel:** `compile.py`
   printed `WARNING: 'build' carries 9/9 beats (100%) — over the ~40% pantry cap` — this lint is
   aimed at pantry/Ken-Burns-still reels mixing motion languages; it's a warning only (does not
   raise `BuildError`), and both sibling STEM reels (also 100% self-contained Manim) carry the
   same warning for the same structural reason. Not a real defect; noted here rather than silently
   ignored.
7. **Real frames independently extracted and inspected (not just the automated gates) at B02
   (both the panel-content phase and the overlay phase), B03, B04, B05 (both at two separate
   timestamps each to confirm steady-state stability), and B06:** all clean — budget panels fully
   legible, both the TRUNCATED/CAUGHT tags sit clear of their panels with no overlap, no
   off-frame/off-safe-area content, no Pango small-font-size word-gap artifacts visible anywhere
   (every on-screen string went through `T()`).

**Landscape final:** `deliverables/landscape/ContextWindowLimits_SaiPranaviJ.mp4` — 3840x2160,
24fps, h264/aac, **177.625s** (ffprobe; the small difference from the 177.668s raw audio sum is
`compile.py`'s documented pad-never-truncate frame-rounding of each beat's `render_duration_s` to
the nearest whole frame at 24fps, plus a 0.1s head/tail center-cut `compile.py` applied to B00's
silent clip to conform it exactly to its rounded render duration). GATE V on the true clean master
(`final_frame_check.py --lenient`, run directly against the deliverable, not a `-slate.mp4` review
cut): **0 BLOCKER, 0 MAJOR.**

## 2026-11-13 — Vertical build

Scaffolded via `./art vertical <reel> --no-endcard --handle "@HumanitariansAI"` (both flags
explicit: `shorts.py`'s defaults are a silent endcard even under `--vertical`, and the
`@nikbearbrown` handle — neither acceptable for this house's required naming). Confirmed it copies
the parent's 9 mp3s and beat-sheet metadata into `vertical/` (`aspect_ratio: "9:16"`, `kind:
"vertical"`, `fit: "pad"`) and correctly refuses to auto-generate a portrait Manim layout for any
GENERATED beat — exactly the documented contract. `vertical/scenes.py` was hand-authored ahead of
rendering, with every beat's timing hand-matched to `../scenes.py` beat-for-beat while authoring.

### Real findings during the vertical build

1. **A real GATE A false positive on B04 (and, by construction, every other beat in the file),
   matching the documented stub-vs-real-Manim divergence class exactly:** the static pre-flight
   checker reported "1 explicit coord(s) outside the frame" for a `move_to` call that does not
   exist anywhere in `vertical/scenes.py` (confirmed by direct grep — every `move_to()` in this
   file takes `.get_center()` or `ORIGIN`, never a literal coordinate). Independently verified via
   the real pixel-true `manim_layout_audit.py --portrait`, run against a scratch copy of the file
   for ALL 9 beats (not just the one GATE A happened to flag first): 7/9 came back CLEAN
   immediately; B04 and (after a full sweep) two text-block margins came back with 2 real WARNINGs
   (not errors) — see finding 2.
2. **Two real portrait-safe-area warnings, found by the real auditor BEFORE any render, not after:**
   B04's title and closing lines each measured 0.1 unit outside the portrait safe y-bound (`±3.4`),
   because this portrait frame's safe half-height is tighter than the landscape frame's (3.6) that
   the copied `buff=0.5` edge convention was tuned against — same `frame_height=8` does not mean
   same safe margin once the aspect ratio changes. Fixed by raising every `to_edge(UP/DOWN,
   buff=0.5)` text margin to `0.7` (rule-line margins 0.35→0.55) across all 6 affected beats,
   computed from the real safe half-height, not guessed. Re-audited all 9 beats: all CLEAN.
   Proceeded past GATE A using the documented `ART_QC=0` escape hatch, with every beat already
   independently verified beforehand rather than trusted from the escape hatch after the fact.
3. **A real GATE V underfill failure on the first true vertical candidate, not a burn-in false
   positive:** `./art final --height 3840` REFUSED with 0 BLOCKER, 6 MAJOR `underfill` (B02 44%,
   B03 54%, B06 47%, B08 34% of the safe area, min 55%) — confirmed real via a manual
   `ffmpeg -f concat` reconstruction and a direct `final_frame_check.py` run (no `--review` label
   present, so not the documented burn-in artifact). Root cause: this portrait file's content was
   sized too close to the landscape proportions, leaving real negative space in the taller 9:16
   frame. Fixed each beat with genuine added content mass (larger real text, wider real rules, more
   real spacing between real elements) — never a padding rectangle.
4. **B08's fix round-tripped once:** the first attempt recovered the fill ratio but introduced a
   real 2-BLOCKER `edge-bleed` (the enlarged frame's half-width, 2.05, exceeded the portrait safe
   half-width, 1.95) plus a still-short 51% fill. Fixed by capping the frame width inside the safe
   bound (half-width 1.85) and recovering fill by stacking the two-line captions instead of
   widening them. Re-verified via the real portrait auditor: CLEAN.
5. **A self-caused false signal, caught and traced to its real cause rather than blamed on real
   content:** after the B08 re-fix, the manual-candidate GATE V workaround reported 6 NEW `low-
   contrast` MAJORs on B01/B04/B08 — beats B01 and B04 whose scene code was never touched this
   session. Traced to a real, reproducible cause (confirmed via `ImageChops.difference()` on
   extracted frames, and via `clips/manifest.json`, which showed every clip cached at `270x480@24`
   instead of true resolution): an intervening `ART_QC=0 ./art run --height 480` call, made solely
   to re-render the single changed B08 Manim scene, had silently reverted ALL 9 clips in the shared
   `clips/` cache back to review-preview resolution as a side effect of its own internal
   `compile.py --review --height 480` step — so the manual workaround was unknowingly checking
   stale low-resolution material, where anti-aliasing blends measurably shift a borderline-already
   contrast reading. Not a real defect. Lesson: the manual GATE V workaround is only trustworthy
   immediately downstream of a true-height `./art final` pass; any later preview-height `./art run`
   call reverts the shared `clips/` cache, even for beats it didn't re-render. Resolution: stopped
   hand-reconstructing from stale `clips/`, and re-ran the real `./art final --height 3840` command
   directly, which recompiles `clips/` at the correct height itself before its own (always-strict)
   embedded GATE V check.
6. **The TRUE vertical candidate passed GATE V clean on this re-run — 0 BLOCKER, 0 MAJOR:**
   `./art final --height 3840 --out deliverables/vertical` succeeded with no BuildError.
   Independently re-ran `final_frame_check.py --lenient` directly against the written candidate:
   **0 BLOCKER, 0 MAJOR.** Real frames extracted and personally inspected at B02, B03, B04, B05
   (two timestamps), B06, and B08 — all clean, properly filled, no overlap, mechanism legible in
   both B04 (TRUNCATED — SILENTLY) and B05 (CAUGHT IMMEDIATELY).

**Vertical final:** `deliverables/vertical/ContextWindowLimits_SaiPranaviJ.mp4` — 2160x3840, 24fps,
h264/aac, **177.625s** — identical duration to the landscape master to the millisecond. GATE V on
the true clean master (`final_frame_check.py --lenient`, run directly against the deliverable):
**0 BLOCKER, 0 MAJOR.**

**Deliverables confirmed (both masters, both GATE V clean, both ffprobe-verified):**
- `deliverables/landscape/ContextWindowLimits_SaiPranaviJ.mp4` — 3840x2160, 24fps, h264/aac,
  177.625s. GATE V: 0 BLOCKER, 0 MAJOR.
- `deliverables/vertical/ContextWindowLimits_SaiPranaviJ.mp4` — 2160x3840, 24fps, h264/aac,
  177.625s. GATE V: 0 BLOCKER, 0 MAJOR.

Both masters' durations match exactly (177.625s each, to the millisecond as reported by `ffprobe`).

Publishing not authorized — `beat_sheet.json`'s `publish` gate is marked ready-for-review, not
approved. Nothing inside `brutalist/` was modified.
