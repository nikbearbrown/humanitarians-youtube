# BUILD-LOG — The Correction That Never Reached The Email

## 2026-10-27 — Research and verification

**Gate P:** Beat sheet approved 2026-10-27. **FACTCHECK:** resolved same day — all claims traced
to the real, current `scripts/regulatory-intel/workflow.dev.json` (`Layer 2 - LLM Re-Score`,
`Generate Email`, `High Priority Filter` nodes, read-only, not modified this session),
`scripts/regulatory-intel/C3-VERIFICATION.md`, `/Users/pranavijs/mycroft/logs/RUN_LOG.md`'s
2026-10-27 entry, and this session's own live Node.js `vm` verification harness
(`verification/verify_effective_severity.mjs`, `verification/verify_effective_severity_output.txt`):
pre-fix (reconstructed by undoing the exact C3 diff) `critical_count: 2, high_count: 1`; post-fix
(the real, current `jsCode`) `critical_count: 1, high_count: 2` — matching `C3-VERIFICATION.md`'s
own independently-reported table exactly. See `FACTCHECK.md` and `SOURCES.md` for the full
claim-by-claim trace. See `FRICTIONAL.md` for the real, dated build-time snags.

## 2026-10-27 — Full build (both aspects)

**Audio:** Kokoro `af_bella`, all 9 beats. B01-B08 generated via `generate_audio_kokoro.py`
(measured durations: B01 17.14s, B02 19.54s, B03 27.07s, B04 19.82s, B05 29.42s, B06 29.83s,
B07 11.18s, B08 1.51s). B00 is a real silent mp3 (`ffmpeg anullsrc`, requested 4.05s, measured
4.10s — mp3 frame-boundary rounding, used the real measured value) with `audio_policy: "silence"`
set explicitly per `build_safety.py`'s silent-required-audio gate. Total measured runtime 159.61s
audio / 159.79s compiled (24fps rounding) — within this project's ~2:40 target.

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (Pango/Cairo
small-font-size-artifact workaround), copied from this fellow's closest siblings
(`2026-10-20-the-filter-that-didnt-know-its-own-labels/scenes.py`,
`2026-10-21-calibration-why-confidence-isnt-accuracy/scenes.py`) for visual consistency. B03 shows
the real 4 fields `Layer 2 - LLM Re-Score` writes, verbatim, next to the real pre-fix 2-line
bucketing from `Generate Email`, with the `impact_level` substring isolated via Manim `Text`
character-index slicing (no re-creation, no paraphrase) and boxed gold/crimson in both lines. B04
shows the real diff adding `effectiveImpact()` (struck-through before, added after, exactly as in
`C3-VERIFICATION.md`'s "The fix"). B05 shows the real before/after Node.js harness results
(`critical_count: 2 -> 1`, `high_count: 1 -> 2`) from this session's own run. B06 shows both honest
limits as separate full-weight cards.

**Timing verification before rendering:** reused a standalone checker (parses every
`run_time=`/`self.wait()` literal per `Scene` class and sums it against each beat's measured
`actual_duration_s`, kept in the session scratchpad, not part of this project folder — same
checker pattern this fellow's 2026-10-20 report documented building). All 9 landscape scenes
matched their measured durations exactly on the first pass; all 9 vertical scenes matched on the
first pass too (no timing-arithmetic slip this build — see `FRICTIONAL.md`).

**GATE A (pre-flight):** all 9 landscape scenes and all 9 vertical scenes individually checked via
`static_scene_check.py --class <Name>` — clean, 0 warn/error, before each full `./art run`. One
real bug caught here on the first landscape pass: `B04_EffectiveImpactDiff` raised
`AttributeError: property 'width' of 'Line' object has no setter` — the draft built each
strike-through `Line` before the whole-diff-block `fit()` call, then tried to rescale the `Line`'s
read-only `.width` afterward. Fixed by grouping each strike `Line` with its minus-text line into a
shared `VGroup` BEFORE the block-level `fit()`, so it scales automatically as part of the group.

**GATE B (post-render layout audit) — real defects found and fixed, vertical only (landscape was
clean on the first pass):**
- `B03_FieldWrittenFieldIgnored`: title's real top edge at y=3.5 (buff 0.5 -> 0.68, the same
  systemic portrait safe-area floor this fellow's sibling reels' BUILD-LOGs already document for
  any 2-line `title.to_edge(UP)`); the un-capped fields/code panel stack combined with the closing
  caption produced both a real safe-area floor overflow (caption bottom at y=-3.5) AND a real
  `text-on-text` overlap (the caption crossing the code panel's own last line, 14% overlap) — fixed
  by capping the stack's height (`scale_to_fit_height(3.5)`, later raised to 4.3 once GATE V found
  it too small — see below) and switching the caption's position from an independent
  `to_edge(DOWN)` to `next_to(panels, DOWN, buff=0.35)`, which structurally guarantees no overlap
  regardless of the panel stack's exact size.
- `B04_EffectiveImpactDiff`: the same systemic title/caption safe-area floor (buff 0.5/0.45 -> 0.68
  on both edges).
All of the above are genuine measured overflows/overlaps (re-confirmed by reading the actual
reported bounding boxes against the documented safe-area half-extents), not false positives.

**GATE V (true final masters, `final_frame_check.py --lenient`, run standalone from inside the
reel folder against the real candidate — never the `-slate.mp4` review file, which carries a
burn-in timestamp overlay this checker's burn-in mask doesn't cover and which uniformly
false-flags every sampled frame as `edge-bleed` in both aspects — confirmed by extracting and
visually inspecting a real slate frame, same documented false positive this fellow's sibling reels
already found):**
- Landscape: `./art run`'s embedded review-slate GATE V reported `BLOCKER=18 MAJOR=0` (the known
  burn-in false positive, confirmed by extracting `B00`'s slate frame at t=2s — real content sits
  comfortably inside its bordered frame; the flagged corner holds only the slate's own
  `00:00:02.000` timestamp overlay). Built the true final master manually (`ffmpeg -f concat` +
  `clips/_work/master.wav`) and ran `final_frame_check.py . --mp4
  deliverables/landscape/EffectiveSeverity_SaiPranaviJ.mp4 --lenient`: **0 BLOCKER, 0 MAJOR** —
  clean on the first true-master pass, no further fixes needed.
- Vertical: same review-slate burn-in false positive on the first `./art run vertical` pass
  (`BLOCKER=18 MAJOR=0`). Built the true final master the same way and ran
  `final_frame_check.py vertical --mp4 deliverables/vertical/EffectiveSeverity_SaiPranaviJ.mp4
  --lenient`: **BLOCKER=0, MAJOR=6** — real `underfill` findings (not false positives): `B02`
  (51% of the safe area, min 55%), `B03` (50%), `B08` (45%). Fixed by widening internal buffs and
  enlarging type in all three scenes (B02's tile padding/buffs, B03's panel-stack height cap
  raised from 3.5 to 4.3, B08's font sizes and top-level buff) rather than adding an invisible
  spacer — re-ran `./art run vertical`, GATE B clean, rebuilt the true final master, re-ran
  `final_frame_check.py vertical --lenient`: **0 BLOCKER, 0 MAJOR.**

**Landscape final:** 3840x2160, 24fps, h264/aac, 159.79s. `final_frame_check.py --lenient` on the
true final master: **0 BLOCKER, 0 MAJOR.**

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(rendered 2160x3840), same `T()` helper plus the portrait `config.frame_width` patch (copied
verbatim from the sibling reels' documented fix). B02's 2-tile row, B03's fields/code panel row,
and B06's 2-card row each became stacked columns; B05's 3 side-by-side row-cards were redesigned
as ONE compact table-style panel (header + 3 rows + totals) rather than a literal vertical stack of
3 bordered cards, to fit the same measured beat duration's worth of content inside this frame's
narrower safe area (documented in `vertical/scenes.py`'s own module docstring).

**Vertical final:** 2160x3840, 24fps, h264/aac, 159.79s — **identical duration to the landscape
master** (same timeline, every beat kept, nothing dropped, via `./art vertical` — no cap, no
rewritten outro, no added endcard). `final_frame_check.py --lenient` on the true final master:
**0 BLOCKER, 0 MAJOR.**

**Deliverables:**
- `deliverables/landscape/EffectiveSeverity_SaiPranaviJ.mp4` (+ `.verified.json`, SHA-256
  `13c3a30644d9c5a1d5b1a5fa7ab5055eef320050b9934fb83bb2b612960abfc0`)
- `deliverables/vertical/EffectiveSeverity_SaiPranaviJ.mp4` (+ `.verified.json`, SHA-256
  `f11c036c7caa06a3255403277b4ec45037dbd3545ce849da0c9dc6668e024c32`)

Both final masters were personally re-inspected frame-by-frame (B00's title card and B03's
fields/code panels with the `impact_level` boxes highlighted, B04's struck-through diff and
`effectiveImpact()` addition, B05's real harness table with the gold-boxed recategorized row, B06's
honest-limit cards, B07's re-colored takeaway line, and B08's sign-off) directly from the shipped
deliverables, in both aspects, before considering this project done — no text-rendering artifacts,
no clipping, no overlap, "Sai Pranavi J." (never the full surname) and "@HumanitariansAI" confirmed
correct everywhere they appear.

## Summary — final gate results

| Aspect | Resolution | Duration | GATE V (true final master) |
|---|---|---|---|
| Landscape | 3840x2160 @ 24fps | 159.79s | 0 BLOCKER, 0 MAJOR |
| Vertical | 2160x3840 @ 24fps | 159.79s | 0 BLOCKER, 0 MAJOR |

No persistent/unavoidable MAJOR findings remain on either true final master — both are fully
clean.

Publishing not authorized. Nothing inside `brutalist/` was modified; nothing inside
`/Users/pranavijs/mycroft` was modified (confirmed via `git status --short` before and after this
session — only pre-existing, unrelated `package-lock.json` changes from before this session were
present).
