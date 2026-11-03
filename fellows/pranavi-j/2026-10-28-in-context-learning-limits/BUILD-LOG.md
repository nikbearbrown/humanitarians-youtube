# BUILD-LOG — In-Context Learning: What the Prompt Can (and Can't) Teach

## 2026-10-28 — Full build (both aspects)

**Gate P:** Beat sheet approved 2026-10-28. **FACTCHECK:** resolved same day — the mechanism
(in-context learning as pattern-location/task-location within the prompt, not weight learning),
the worked example (a generic, invented Caesar-shift-by-3 substitution rule taught purely via
example pairs), and the falsifiability case (the identical task reordered with one mapping
flipped against the otherwise-consistent rule) all confirmed fully qualitative, no real
model/vendor named, no benchmark claimed, with order-sensitivity and prior-conflict claims kept
hedged and generic per the ICL research literature. Confirmed distinct from this fellow's five
prior videos: hallucination, tokenization, lost-in-the-middle, chain-of-thought faithfulness, and
calibration.

**Audio:** Kokoro `af_bella`, all 8 spoken beats generated via `generate_audio_kokoro.py`. B00 a
real silent mp3 (`ffmpeg anullsrc`, 4.104s) with `audio_policy: "silence"` set explicitly per
`build_safety.py`'s silent-required-audio gate (the script correctly skips synthesizing B00 rather
than producing empty narration — the silent mp3 has to be created by hand). `actual_duration_s`
written back to `beat_sheet.json` from real ffprobe measurements: B00=4.104 B01=14.64 B02=21.26
B03=35.21 B04=28.49 B05=27.17 B06=27.70 B07=13.06 B08=1.51 — total 173.14s narration/silence.

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (creates `Text()` at
`font_size=48`, then scales geometrically to the intended size) for every on-screen string —
avoids the confirmed Manim/Pango small-font-size rendering artifact. New helpers specific to this
reel: `pair_row()` / `example_panel()` — a bordered panel holding a stack of "INPUT -> OUTPUT"
example-pair rows, the core recurring visual idiom (a toy rule shown only as example pairs, never
named/explained on screen), reused across B02 (the hook), B04 (the worked example), and B05 (the
falsifiability case). B03 shows all 3 tests (Spot the Mapping / Shuffle the Set / Push Past the
Window) fully, before any example, per the Legibility Contract.

### Real bugs/findings hit and fixed during this build

1. **Manim always renders at the hardcoded native resolution regardless of `run.sh`'s `--height`
   flag (confirmed, matches the sibling reel's documented finding):** `run.sh` invokes `manim -r
   "3840,2160"` unconditionally for a 16:9 reel; the `--height` flag only controls the compiled
   *review* cut's resolution. Confirmed directly via `ffprobe` on `manim/B04.mp4` after the first
   `--height 480` QC pass: already true 3840x2160. The fast QC pass therefore produced true-4K
   Manim renders and true GATE A/B results on the first attempt — no redundant full-height
   re-render of the Manim stage was needed for the landscape master.
2. **Real GATE V MAJOR on the first low-res pass, not a review-slate false positive — B02's
   fade-out/fade-in transition landed exactly on a GATE V sample point at near-zero opacity:**
   the first `scenes.py` draft held B02's example-panel content on screen until t=10.0s, then
   cross-faded (FadeOut 0.5s, FadeIn 0.6s) to the "Learning, or locating?" overlay. GATE V's 50%
   steady-state sample (~10.63s into a 21.26s beat) landed ~0.13s into the overlay's own FadeIn,
   while it was still almost fully transparent — correctly flagged `empty-frame` MAJOR on direct
   measurement. Fixed by front-loading B02's early waits (10.0s of pre-transition holds compressed
   to 6.0s) so the transition completes by t=7.1s, well clear of both GATE V sample points, with no
   change to the total beat duration (the saved 4.0s moved to the post-transition hold on the
   overlay). Confirmed clean (0 MAJOR on this beat) on the re-render.
3. **Expected review-slate false positive, matching the sibling reel's documented finding exactly
   (18 BLOCKER, 2 per beat x 9 beats, `edge-bleed`):** after fix #2, the review slate's GATE V
   showed exactly 18 BLOCKER / 0 MAJOR — the same documented pattern from this fellow's prior
   episode, caused by the review cut's own burn-in timecode/label strip sitting outside
   `final_frame_check.py`'s `BURN_IN_EXCLUDE` zone, not a real defect in the scene content. Per the
   documented workaround, re-verified directly against the TRUE final candidate (not the review
   slate) before accepting this as clean — see below.
4. **`./art final`'s GATE V step workaround (matches the documented bug, both aspects):** ran
   `compile.py --height 2160` directly (true 4K, no `--review` flag, so no burn-in strip) to
   produce the clean candidate, then ran `final_frame_check.py --lenient` directly against that
   true candidate file (never the `-slate.mp4` review cut) to get real, visible diagnostics.
5. **Stale render cache (landscape, the one round that touched `scenes.py` after the first QC
   pass):** deleted `manim/B02.mp4` and its `media/videos/.../B02_LearningOrLocatingHook` cache
   explicitly before re-rendering B02 only, per the documented stale-cache bug (`run.sh`/
   `compile.py` do not detect `scenes.py` source changes and will silently reuse old cached
   outputs) — avoided a wholesale re-render of all 9 beats.
6. **A real content bug in `example_panel()`'s row-indexing, present in BOTH `scenes.py` and
   `vertical/scenes.py` identically (B05):** `rows = panel_content[1][1]` double-indexed into the
   returned `rows` VGroup (an extra `[1]`), so `flipped_row = rows[flip_index]` pulled an unrelated
   text mobject from a different row than intended. Confirmed visually by extracting a real
   rendered frame from the landscape master: the flip-indicator box was a tiny dot around the SUN
   row's output text, and the "FLIPPED" tag floated off to the side, nowhere near the actual
   flipped DOG row. The landscape GATE B layout audit had NOT flagged this (the wide landscape
   layout happened to leave enough slack that nothing visibly overlapped) — caught only by
   inspecting an actual frame against the beat's own intent, not by trusting a clean QC pass alone.
   Fixed to `rows = panel_content[1]` in both files; re-verified correct via a second extracted
   frame (landscape) and a direct `manim_layout_audit.py --portrait` pass (vertical).
7. **A second, genuine portrait-only bug exposed once bug #6 was fixed (vertical B05 only):**
   with the flip_box now correctly positioned on the DOG row, placing the "FLIPPED" tag directly
   below it (as the first fix attempt did) landed on the next row's text ("CAT -> FDW") in this
   file's tightly-packed portrait row stack — confirmed via `manim_layout_audit.py --portrait`
   (1 ERROR text-on-text `->`/`FLIPPED`, 2 WARNING `CAT`/`FLIPPED` and `FDW`/`FLIPPED`). Fixed by
   moving the tag to sit below the WHOLE panel instead of inline between rows, rebalancing
   `self.wait()` values by 0.1s to keep the beat's total duration exactly matched to
   `actual_duration_s` (27.17s). Re-audited: CLEAN, 0 errors, 0 warnings.
8. **GATE V MAJOR on the TRUE landscape candidate (not the review slate) — B04 canvas-fill
   underfill, a real finding:** `final_frame_check.py --lenient` run directly against the first
   true 4K landscape master measured B04's steady-state frame at 53% of the safe area (min 55%)
   at both sampled timestamps. Fixed with genuine added content mass — a top framing rule folded
   into the title's existing `self.play()` and a bottom framing rule folded into the closing's
   existing `self.play()` (same idiom as B00/B01/B02's top/bottom rules), not a padding trick, and
   with zero change to the beat's total timing (both rules added to existing animation calls, no
   new `self.play`/`self.wait` lines). Re-rendered, re-verified GATE A/B clean, and the review
   slate's GATE V returned to the expected 18 BLOCKER / 0 MAJOR false-positive pattern before
   rebuilding the true final candidate a second time.
9. **That same B04 fix's own framing rules introduced a genuine NEW edge-bleed BLOCKER on the
   re-check (not a false positive):** the rules' `buff` values (0.3 from the top edge, 0.35 from
   the bottom) put them 0.1 units past the landscape safe half-height — computed exactly from
   `final_frame_check.py`'s own `SAFE` constants (1728x972 of a 1920x1080 reference canvas, a flat
   5% margin on every side, i.e. ±3.6 in Manim's 8-unit `frame_height`) rather than eyeballing it.
   Fixed by widening both buffs to 0.5 (edge at ±3.5, a real 0.1-unit clearance). Re-verified on
   the true candidate: **0 BLOCKER, 0 MAJOR** for the landscape master.
10. **Vertical's first true-candidate GATE V came back far worse than the review slate's expected
    false-positive pattern (4 BLOCKER, 7 MAJOR) — all genuine findings, none of them burn-in
    artifacts:** found by computing the exact sample timestamps from `vertical/beat_sheet.json`'s
    own `render_duration_s` values (matching `final_frame_check.py`'s internal `beat_spans()`/
    `sample_beats()` logic exactly) and extracting real frames, not guessing from the contact
    sheet. Three distinct root causes, all fixed:
    - **B01 edge-bleed** (frame height=7.4, half 3.7 > the portrait safe half-height of 3.6 — this
      frame is a VISIBLE bordered rectangle, `opacity=0.0` only zeroes the fill, not the stroke).
      Fixed to height=7.0; pre-emptively tightened B00's identical frame (7.2, exactly on the
      boundary) the same way.
    - **B02 empty-frame/underfill** — the same content-fade/overlay-fade timing bug already found
      and fixed in landscape's B02 (see #2 above), never ported to `vertical/scenes.py`'s own,
      separately-authored B02. Applied the identical front-loaded-waits fix.
    - **B03 edge-bleed** (left/right) — `test_card()`'s `head_t` (fit to `MAX_W-0.5`) plus the
      badge and the list_panel's own `+0.6` padding combined past the portrait safe half-width of
      2.025 (`frame_width = 8*2160/3840 = 4.5`, 5% margin = 0.225). Fixed by tightening per-element
      width budgets (head_t to `MAX_W-0.9`, body_t to `MAX_W-0.4`) and the panel padding (+0.6 ->
      +0.3).
    - **B06/B07/B08 underfill** (53%/53%/42%) — B06 fixed with the same real-framing-rule idiom as
      landscape B04. B07/B08's frames were sized FROM their own short text content
      (`content.height + 0.8`/`content.height + 0.6`), guaranteeing underfill on a tall portrait
      canvas regardless of text arrangement — fixed by sizing both frames from the portrait safe
      bounds themselves (fixed 4.0x7.0, matching B00/B01's own confirmed-safe dimensions).
    Re-verified every changed beat's exact `run_time`/`self.wait()` timing sum against its
    `actual_duration_s` (via a small regex script) before re-rendering — unchanged in all cases.
11. **A second true-candidate GATE V pass on vertical still found 2 real MAJORs (0 BLOCKER) — B02
    underfill (48%):** the content-fade timing fix (bug #10's second bullet) had resolved B02's
    empty-frame finding, but the "Learning, or locating?" overlay card itself was simply too small
    for a portrait canvas. Rendered B02 in isolation, extracted real frames at its own internal
    50%/85% points (a standalone-rendered beat has its own t=0, not the full video's absolute
    timestamp), and confirmed visually before trusting a fix: the overlay occupied only the
    vertical-center third of the frame. Fixed with real added size (qmark 120pt -> 160pt, overlay
    text 36pt -> 40pt, inter-element buff 0.7 -> 0.9, rules widened 1.6 -> 1.9 units per side).
    Re-verified via a second extracted frame (overlay now spans ~70% of frame height) before the
    full true-4K rebuild. Final GATE V on this vertical candidate: **0 BLOCKER, 0 MAJOR**.

**Landscape final:** 3840x2160, 24fps, h264/aac, **173.375s**. GATE V on the true clean master
(`final_frame_check.py --lenient`, run directly against `deliverables/landscape/
InContextLearningLimits_SaiPranaviJ.mp4`, not the `-slate.mp4` review cut): **0 BLOCKER, 0 MAJOR.**

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(`config.frame_height`/`frame_width` patched for portrait per the documented manim-CLI-ordering
bug, rendered 2160x3840), same `T()`/`panel()`/`box_around()`/`pair_row()`/`example_panel()`
helpers copied verbatim (narrower fonts/padding), scaffolded via `./art vertical`
(`runtime/scripts/shorts.py --vertical`), which confirmed it copies the parent's mp3s and beat
sheet metadata but — correctly, per its own documented contract — does not auto-generate a
portrait Manim layout for a GENERATED/manim beat; it flags each beat `native portrait scene`
and expects the hand-authored `vertical/scenes.py` this build already had ready. Every
`self.play`/`self.wait` duration matches `scenes.py` beat-for-beat (hand-verified per beat against
each `actual_duration_s`), so the vertical master's total runtime matches the landscape master's —
full-length, all 9 beats, no drops, no duration cap, no added endcard, per `./art vertical`'s
contract.

**Vertical final:** 2160x3840, 24fps, h264/aac, **173.375s** — identical duration to the landscape
master (both masters share the same per-beat `actual_duration_s`/`render_duration_s` timeline).
GATE V on the true clean master (same manual-reconstruction workaround as landscape, run directly
against `deliverables/vertical/InContextLearningLimits_SaiPranaviJ.mp4`): **0 BLOCKER, 0 MAJOR.**

**Deliverables confirmed (both masters, both GATE V clean):**
- `deliverables/landscape/InContextLearningLimits_SaiPranaviJ.mp4` — 3840x2160, 24fps, h264/aac,
  173.375s. GATE V: 0 BLOCKER, 0 MAJOR.
- `deliverables/vertical/InContextLearningLimits_SaiPranaviJ.mp4` — 2160x3840, 24fps, h264/aac,
  173.375s. GATE V: 0 BLOCKER, 0 MAJOR.

Both masters' durations match exactly (173.375s each, to the millisecond as reported by `ffprobe`).

Publishing not authorized — `beat_sheet.json`'s `publish` gate is marked ready-for-review, not
approved. Nothing inside `brutalist/` was modified.
