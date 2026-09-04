# BUILD-LOG — claude-quickstarts--browser-coordinate-scaling

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-quickstarts/youtube/browser-coordinate-scaling/beat_sheet.json`
(a Teardown-register scaffold, 4/8 beats filled with Manim, no SCRIPT.md, built
from `browser-use-demo/browser_use_demo/tools/coordinate_scaling.py`). Question,
facts, and mechanism carried over unchanged: Claude's vision encoder resizes
16:9 screenshots to a fixed 1456×819; the fix multiplies by the inverse resize
ratio (`viewport_w/1456`, `viewport_h/819`) and clamps to bounds. B00 replaced
the source's `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter`
(WRITER LAW: "exact" → "scaled"). Register re-registered Teardown → Plain (the
source narration carried no design judgment to remove). Close/outro re-skinned
to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Source's B05 verdict/
recap beat dropped as a restatement; source's B04 exclusions beat folded into
B04's both-directions clause. No source beat was `ai-video-prompt`, pantry, or
a human-drop slot (all were already Remotion/Manim-shaped, just unbuilt), so
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00.

**Duplicate-source note (logged for transparency, not treated as a blocker):**
the identical question and underlying facts were already built and delivered
on 2026-08-28 as `hai-simple/claude-basics--browser-coordinate-scaling`, from a
*different* source-sheet path (`anthropics/youtube/claude-basics/browser-coordinate-scaling/`).
`queue_scan.py --from-sheets` queues every `beat_sheet.json` under `anthropics/`
independently, by design (no cross-path dedup per its own docstring: "the
entire folder is Claude questions — they ALL get redone as hai-simple"), so
this is a second, separately sourced redo target, not a re-run of the same
job. To avoid a byte-identical duplicate, this build uses fresh narration
throughout and a new worked anchor example ((728, 364) → (960, 480) on a
1920×1080 screen, chosen so the arithmetic is exact: 1920/1456 = 1080/819 =
120/91 exactly, since 91 | 1456 and 91 | 819) rather than reusing the sibling's
(728, 409) → (1280, 720) example, which also had a small rounding slip
(409 × 1440/819 = 719.12, not 720 as the original scaffold claimed).

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`. Durations: B00
   11.16s, B01 19.03s, B02 17.24s, B03 18.33s, B04 25.86s, BCRY 8.96s,
   BHTF 15.42s, BOUT 4.57s.
2. Wrote `scenes.py` (4 Manim scenes, B01–B04) sized to the measured
   durations, and `render_scenes.py`; rendered all four in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` (foreground; the
   first invocation tripped the shell's 2-minute default timeout mid-run —
   B00 had already landed — so it was re-run with a longer tool-level
   timeout to finish BCRY/BHTF/BOUT; never treated the partial run as done
   until the second invocation's exit was observed).
4. **B00 TIMING LAW bug found and fixed before it reached compile:** the
   first B00 render (params matching the sibling reel's: charMs=55,
   hesitateBetween=22, mistakeRate=6, hesitateWithin=3, plus 8 punctuation
   marks in the writer text) did not finish typing its own correction inside
   the 11.16s beat — a frame pull at 11.0s (near the clip's end) still showed
   "exact" typed and un-replaced, the same failure class the pilot lesson in
   SKILL.md warns about. Root cause: fixed per-punctuation-mark pauses
   (400–800ms, hardcoded in the component, not prop-tunable) plus the
   trigger-word swap overhead summed to an estimated ~14s of typing, well
   over the 11.16s budget. Fixed by rewriting the writer text to cut
   punctuation marks from 8 to 4 ("Claude clicks at (728, 364) on my screens
   exact spot right?") and slowing down less aggressively (charMs 55→38,
   hesitateBetween 22→12, mistakeRate 6→4, hesitateWithin 3→2). Re-rendered;
   verified via frame pulls at 8.5s and 9.5s that the correction ("exact" →
   "scaled") completes and rests legibly with buffer before the beat ends.
5. **Gate V (visual) caught one real layout bug, fixed at the root:** B02's
   "same (728, 364)" caption, positioned `next_to(dot2, DOWN, buff=0.28)`,
   collided with the screen rectangle's bottom border — the label text
   visibly crossed the box outline on a frame pull. Fixed by moving the dot/
   miss mark up within the box (DOWN 0.35 → DOWN 0.15) and placing the
   caption below it with a smaller buff, giving the label clear room inside
   the border. Verified clean on re-pull.
6. **GATE T (type_check.py) caught one kerning false positive, verified
   then exempted (not the layout bug above — a separate step's result):**
   after the B02 fix, `type_check.py` flagged B02Scene for kerning
   (max inter-glyph gap 50px > threshold). Pulled the checker's own sample
   frame (t=dur×0.5 of manim/B02.mp4) and read it directly: the "same (728,
   364)" caption and the nearby terracotta Cross() miss-mark sit on visually
   distinct rows, fully legible, correctly kerned — the same false-positive
   mechanism already documented in `type_check.py` for other reels (icon-
   adjacent-to-text compound peak-ink band, e.g. S08Scene; MONO parens/comma
   numeric labels dragging mean letter width down, e.g. SERB04Scene). Font
   is named (Menlo/MONO) in every `Text()` call, so the structural Pango
   check already passed. Added `B02Scene` to `type_check.py`'s existing
   `KERNING_EXEMPT_PATTERNS` with a comment following the file's established
   precedent format — fixed content first (steps 4–5 above), touched the
   validator only for this confirmed false positive.
7. `compile.py` → `claude-quickstarts--browser-coordinate-scaling.mp4`, 8/8
   real (no slate), 121.6s, 3840×2160 (THE 4K LAW).

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the B02 fixes above
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio aac present, duration 121.58s; mp4
  mtime newer than beat_sheet.json mtime

**Gate V (visual):** pulled 20 frames at 6s spacing across the full 121.6s
runtime plus targeted pulls around B00's correction and B02's fix, and read
them directly. B00's correction ("exact"→"scaled") lands and rests legibly
before the beat ends. B01→B04's anchor pair ((728, 364) on 1456×819 → miss,
then (960, 480) on 1920×1080 → hit) is visually recognizable as the same
rectangle pair across all three appearances, per ANCHOR LAW. B04's non-16:9
caveat box sits clear of the frame's right edge. BCRY/BHTF/BOUT text is
centered, legible, no overlap, safe inset respected, HAI skin correct
(@HumanitariansAI, no Claude branding). No blockers remaining.

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:4 — remotion at 50% of beats, over the ~40% pantry cap in MOTION.md.
Structural, not a defect: hai-simple's mandated shape is B00 (writer) + BCRY
+ BHTF (Your Turn) + BOUT (outro) all REMOTION by skill contract, against 4
GRAPHIC body beats for this 8-beat reel — the ratio is fixed by beat count,
same as the sibling `claude-basics--browser-coordinate-scaling` reel's
identical, already-accepted warning.

**Zero inference flags:** every on-screen claim (the 1456×819 resize target,
the inverse-ratio formula, the clamp, the non-16:9 exception) is a direct
read of `coordinate_scaling.py` — see SOURCES.md. Per ONE-FLAG LAW, a fully-
sourced explanation carries no flag.

Metadata file written: `claude-quickstarts--browser-coordinate-scaling.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `hai-simple` prefix,
since `claude-quickstarts` has no direct entry in the map — plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-31 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.
