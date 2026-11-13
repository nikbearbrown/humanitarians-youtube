# BUILD-LOG — Lost in the Middle: Why More Context Doesn't Guarantee a Better Answer

## 2026-10-10/11 — Full build (both aspects)

**Gate P:** Beat sheet approved 2026-10-06. **FACTCHECK:** resolved same day — the mechanism (a
well-documented, generic U-shaped attention effect) and the worked example (a generic onboarding
document with one buried fact) confirmed fully qualitative, no real model/vendor named, no
fabricated statistic.

**Audio:** Kokoro `af_bella`, all 9 beats. B00 a real silent mp3 (`ffmpeg anullsrc`, 4.06s) with
`audio_policy: "silence"` set explicitly per `build_safety.py`'s silent-required-audio gate. All 8
spoken beats generated via `generate_audio_kokoro.py`; `actual_duration_s` written back to
`beat_sheet.json` from real ffprobe measurements: B00=4.06 B01=16.90 B02=16.97 B03=24.00 B04=21.60
B05=15.60 B06=28.27 B07=11.23 B08=1.51 — total 140.14s narration/silence (the compiled masters run
140.33s after the pipeline's own 24fps frame-quantization of each beat's render duration).

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (creates `Text()` at
`font_size=48`, then scales geometrically to the intended size) used for every on-screen string —
avoids the confirmed Manim/Pango small-font-size rendering artifact. New helpers specific to this
reel: `document_stack()` (a stack of varied-width `Line`s standing in for dense body text, used in
B02/B04/B05's document illustrations) and `curve_y()`/`attention_curve_mobject()`/`curve_point()`
(a real plotted `ParametricFunction` U-shape — high at both ends, low in the middle — used for
B03's main diagram and reused as a small "mini curve" inset in B04/B05 to tie the worked example
back to the mechanism). B03 shows the full U-shaped curve, tick labels, and HIGH/LOW callouts
before any numeric claim (there are no numbers on the diagram at all, per FACTCHECK.md). B04 and
B05 use the identical document/question, differing only in the highlighted fact's position and
the model's answer — matching the Legibility Contract's "only position changes" requirement.

### Real bugs hit and fixed during this build

1. **Low-contrast MAJOR from a semi-transparent curve fill (B03, landscape):** the first draft
   drew a translucent "terrain" shade (`curve_fill_area()`, 16% opacity gold) under the attention
   curve for visual richness. GATE V's frame-level QC flagged a real low-contrast MAJOR (0.14-0.16
   luminance separation, under the 0.3 floor) — confirmed by hand-computing the blended luminance
   of a 16%-opacity gold wash over the cream background, not a false positive. Fixed by dropping
   the fill entirely and switching the curve's own stroke color from gold to teal (luminance
   separation ~0.67 vs gold's ~0.25) and bumping the context bar's fill opacity 0.18->0.4 — the
   solid-stroke curve + bar + ticks still read as a real diagram without the low-contrast wash.
2. **Label-on-shape collisions from inline document captions (B02 landscape; B04/B05 both
   aspects):** early drafts placed small text labels ("the fact is here", "fact here", "FOUND" /
   "MISSED?" tags) directly `next_to()` a highlighted document line or document panel. GATE B's
   post-render layout audit caught these overflowing past the panel's own edge into its
   rounded-rectangle stroke, or landing on a neighboring packed document line — the highlighted
   lines were often nearly panel-width wide, leaving no real room beside them. Fixed with two
   different strategies depending on layout: in landscape's B02 (two side-by-side panels), labels
   moved into the real open gap corridor between the panels; in B04/B05's single full-width
   document column (both aspects), the inline label was dropped entirely and the gold/sage
   highlight box alone carries the "visually obvious position" requirement — confirmed sufficient
   by direct frame inspection.
3. **B03's `LOW` label inside the context bar's own rectangle (landscape):** placing the label
   below the curve's dip point landed it inside the bar's own fill area — a real
   label-on-shape collision. Fixed by placing it ABOVE the dip instead, where the curve stays near
   its low value for a wide stretch around the center, clearing both the bar and the curve itself.
4. **Portrait frame_width patch (vertical, both reels' standard fix):** `vertical/scenes.py`
   includes the documented `config.frame_width` recompute (Manim's CLI `-r` flag alone leaves
   `frame_width` at the 16:9 default even for a portrait render), copied from this fellow's
   sibling reels.
5. **Portrait B02 tag overflow:** the FOUND/MISSED? tags, originally placed `next_to()` the whole
   stacked document panel, landed off-frame (box starting at x=2.0, outside the +/-1.95 safe
   half-width) — portrait has no spare width beside a panel that already spans most of the safe
   width. Fixed by shortening the panel headers (SHORT PARAGRAPH/LONG DOCUMENT -> SHORT DOC/LONG
   DOC) and placing the tags next to the header label itself, inside the panel's own safe bounds.
6. **Portrait B03 safe-area/collision cascade:** the start/end tick labels' real bounding boxes
   landed just past the +/-1.95 safe half-width (bar narrowed 3.6->3.2 to fix); a note's real
   bottom edge overlapped the title once the title's own buff was corrected for a separate
   safe-area issue (notes narrowed and moved lower to clear both the title and the "HIGH" labels).
7. **Portrait B04/B05 vertical-budget overflow:** the worked-example and falsifiability beats'
   original composition (tall document panel + Q&A panel + mini attention-curve inset + closing
   line) did not fit the portrait canvas's real vertical budget — GATE B caught the mini curve's
   own label overlapping the closing text at 90%. Confirmed by hand-computing both elements'
   y-ranges (not a false positive): there simply wasn't enough room below the Q&A panel for both
   the inset and the closing line inside the safe area. Fixed by dropping the mini-curve inset
   from the portrait layout only (kept in landscape, where it passed): the MISSED/FOUND tag plus
   the document highlight already make the outcome and position visually obvious, and the full
   attention-curve tie-back is taught once, clearly, in B03.
8. **Portrait B04/B05 title-vs-document-panel collision (two-round fix):** the document panel's
   top edge sat only ~0.2 units below the safe ceiling — less than a single title line's own
   height, so no title buff value could clear the ceiling AND clear the panel at once. Fixed by
   shrinking/shifting the panel down (3.3/1.4 -> 2.7/1.25 center) rather than the title; required
   a second round when B05's two-line title's SECOND line still clipped the panel at an
   intermediate size (3.0/1.4), confirming the panel — not the title — was the real constraint.
9. **Portrait B01 frame edge-bleed (true final candidate, not caught until a byte-identical manual
   rebuild of the real `./art final` candidate):** the exec-summary card's decorative frame
   (height 7.3, half-height 3.65) exceeded the portrait safe half-height (3.6 for a 2160-wide
   canvas) by ~0.05 units (~24px at 4K) — the frame's own stroke, not the text, was the content
   crossing the line. Caught only by reconstructing the exact `./art final` ffmpeg command by hand
   (concat + master audio, `-t` set to the pipeline's real frame-quantized total, 140.333s, not
   the raw narration-duration sum, 140.14s) and running `final_frame_check.py` directly against it
   with full stdout visible — `compile.py`'s own error wrapper only surfaces `stderr`, and this
   gate's diagnostics print to `stdout`, so the real defect was invisible through `./art final`'s
   own error message. Fixed by trimming the frame height to 7.1.
10. **Landscape B06/B07 canvas-fill underfill (true final candidate):** the same direct-candidate
    technique surfaned two real MAJOR underfill findings invisible on the review slate (whose
    burn-in overlay produces unrelated BLOCKER noise, masking real MAJOR signal underneath in
    casual review): B06's checklist card at the 50% sample (title + panel + 2 of 3 checked rows,
    before the closing line appears) measured 47% of the safe area; B07's statement card measured
    49% at both samples. Confirmed by direct frame inspection — both compositions were small and
    centered with large empty margins. Fixed with genuine added content mass: B06's checkbox size,
    item font, and row/item buffs all increased (0.5->0.75 box, 25->34pt text, 0.6->0.9 row gap);
    B07's three statement lines and two punchline lines all increased in size (38/32->48/40/44pt)
    with wider buffs. Re-verified via a fast direct-manim-render + `--frames-dir` iteration loop
    (bypassing the full pipeline for speed) before committing to a full official re-render — both
    measured 0% MAJOR afterward.
11. **Portrait B03/B06 canvas-fill underfill (true final candidate):** B03's 50%-sample state
    (title + curve + HIGH/LOW + first note only; the second note and closing line appear later,
    synced to narration) measured 53% — everything clustered in the top half of the portrait
    canvas, leaving the entire bottom half empty. Fixed by shifting the whole diagram (bar, curve,
    ticks, HIGH/LOW labels) down by 1.0 unit (same shape, same height, just lower in the frame) —
    a real repositioning, not a timing change, so no play/wait value moved. B06's checklist
    measured 54% (just under the 55% floor); fixed with the same box/font/buff bump pattern as the
    landscape version, scaled for the narrower canvas.
12. **"Cannot inspect B08" / GATE V crash via `./art final` (both aspects, root-caused not a real
    defect):** `./art final` initially failed on both reels with `compile.py`'s own error wrapper
    showing an empty `stderr` ("[art] command failed: ... final_frame_check.py ..." with nothing
    after it) — genuinely uninformative. Root-caused by manually reconstructing the identical
    ffmpeg concat+audio command `compile.py` runs for a true final master and invoking
    `final_frame_check.py` directly: the FIRST manual reconstruction attempt used the raw
    narration-duration sum (140.14s) for ffmpeg's `-t` flag, which is NOT what `compile.py`
    actually uses (it sums each beat's 24fps-quantized `render_duration_s`, totalling 140.333s) —
    producing an artificially short candidate whose last frame landed just before B08's 85%-sample
    timestamp, reproducing the identical crash as a genuine (if misleading) symptom of a duration
    mismatch, not a tool bug. Rebuilding with the correct 140.333s `-t` value made the crash
    disappear entirely and surfaced the REAL (minor) underfill findings documented above. This
    confirms the original `./art final` failures were very likely a one-off stale-state artifact
    from an earlier attempt's `resolved-sheet.json`/clip-cache mismatch, resolved by the full clean
    re-render that followed each round of scene fixes (which `./art final` then passed cleanly,
    twice, once per aspect).
13. **Stale render cache (both aspects, every round):** `run.sh`/`compile.py` do not detect
    `scenes.py` source changes and will silently reuse old cached `manim/*.mp4`, `clips/*.mp4`, and
    Manim's own `media/` cache. Deleted `manim/`, `clips/`, `media/`, and QC artifacts before every
    re-render that followed a scene edit (11 rounds total across both aspects), and verified every
    clip's mtime postdated `scenes.py`'s mtime via `stat -f %m` before trusting a render as current.
14. **Review-slate GATE V false positives (expected, not a real defect, both aspects, every
    round):** `./art run`'s compiled `*-slate.mp4` review cut carries a burn-in timecode (top-right)
    outside `final_frame_check.py`'s `BURN_IN_EXCLUDE` zone, producing a spurious `edge-bleed`
    BLOCKER on every single beat (18 BLOCKER, exactly 2 per beat x 9 beats, every round on both
    aspects). Confirmed as a slate-only artifact by extracting and viewing an actual slate frame
    (the title card's real content sat cleanly inside the safe area; only the burn-in strip was
    flagged) and by the fact that the same content measured 0 BLOCKER when GATE V ran directly
    against the clean, unlabeled final candidate. Did not block the true final renders, which carry
    no burn-in by design.

**Landscape final:** 3840x2160, 24fps, h264/aac, 140.333s. GATE V on the true clean master
(re-run directly against the renamed deliverable file): 0 BLOCKER, 0 MAJOR.

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(frame_width-patched coordinate system, rendered 2160x3840), same `T()`/`document_stack()`/curve
helpers, copied verbatim for continuity. B02's two-document hook, B04/B05's document+Q&A worked
example, and B03's attention-curve diagram all needed genuine redesigns (not just narrowing) to
stay legible and safely positioned in the narrow canvas — confirmed by direct frame inspection at
every round, not assumed clean from the tool report alone. Every `self.play`/`self.wait` duration
matches `scenes.py` beat-for-beat (re-verified with a small parser script after every edit,
comparing the computed per-class total against `beat_sheet.json`'s `actual_duration_s`), so the
vertical master's total runtime is identical to the landscape master's (140.333s both) —
full-length, all 9 beats, no drops, no duration cap, no added endcard, per `./art vertical`'s
contract.

**Vertical final:** 2160x3840, 24fps, h264/aac, 140.333s. GATE V on the true clean master
(re-run directly against the renamed deliverable file): 0 BLOCKER, 0 MAJOR.

**Process note:** every render step in this build was run as a single blocking foreground command
and waited out fully — no step was backgrounded intentionally (the harness auto-backgrounded two
long-running renders past its own timeout threshold; both were waited out to completion via a
blocking wait loop before continuing, not treated as done). The final landscape and vertical
masters were personally re-inspected frame-by-frame directly from the shipped deliverable files as
the final check before considering this project done: B02 (short-vs-long document reveal), B03
(the U-shaped curve, both aspects), B04 (buried-fact miss), B05 (repositioned-fact find), B06
(checklist), B07 (statement card), and B08 (brand card) — no text-rendering artifacts, no
clipping, no low-contrast text found on any extracted frame.

**Deliverables confirmed, both renamed and verified (SHA-256 matched against the source render
before and after copy):**
- `deliverables/landscape/LostInTheMiddle_SaiPranaviJeedigunta.mp4` (+ `.verified.json`)
- `deliverables/vertical/LostInTheMiddle_SaiPranaviJeedigunta.mp4` (+ `.verified.json`)

GATE V re-run directly against both final deliverable files (via `final_frame_check.py --mp4
<path> --lenient`, run from inside each reel folder): 0 BLOCKER, 0 MAJOR on both.

Publishing not authorized — `beat_sheet.json`'s `publish` gate is marked ready-for-review, not
approved. Nothing inside `brutalist/` was modified.

## 2026-10-20 — ADDENDUM: fellow-name retrofit (org naming policy: first-name-last-initial only)

- **Scope**: full name "Sai Pranavi Jeedigunta" found in spoken narration (B01), the on-screen name tag (B01), and the on-screen sign-off credit (B08, both aspects). Retrofitted to "Sai Pranavi J." everywhere.
- **Narration (B01)**: `narration_text` changed in `beat_sheet.json` and `vertical/beat_sheet.json`: "Hi, I'm Sai Pranavi Jeedigunta." → "Hi, I'm Sai Pranavi J." Regenerated Kokoro audio (`af_bella`, `generate_audio_kokoro.py --only B01`). New measured duration **16.49s** (ffprobe: 16.488s) vs the old `actual_duration_s` of **16.90s** — a 0.41s shrink, over the ~0.3s retime threshold.
- **Retiming (B01)**: both landscape and vertical plays sum to 2.1s → `self.wait(14.8)` → **`self.wait(14.39)`** (16.488 − 2.1 = 14.388) in both `scenes.py` and `vertical/scenes.py`.
- **On-screen credit**: `scenes.py` B01 name tag and B08 tagline changed to "Sai Pranavi J." (plus a matching comment fix). `vertical/scenes.py` B01 name tag and B08 tagline changed the same way — both B08 taglines were already single-line in this project (no `\n` hard-wrap to collapse), so this was a pure width reduction with no layout risk.
- **No layout regression**: confirmed clean on the first `./art final` attempt for both aspects (no internal GATE V refusal), consistent with the tagline being single-line before and after.
- **Stale-cache avoidance**: deleted `manim/B01.mp4`, `clips/B01.mp4`, `manim/B08.mp4`, `clips/B08.mp4` and the same four paths under `vertical/` before rebuilding — no other beat's cache touched.
- **Rebuild**: `./art run . --height 1080` and `./art run vertical --height 1920` re-rendered only B01/B08 via Manim (GATE A/B CLEAN); both review GATE V runs showed the known review-slate false positive (18/18 frames `edge-bleed`, uniform across every beat including untouched ones). `./art final . --out deliverables/landscape` and `./art final vertical --height 3840 --out deliverables/vertical` both rebuilt cleanly on the first attempt. Verified via `stat -f %m` that every regenerated `manim/B01.mp4`/`manim/B08.mp4` (both aspects) postdates its `scenes.py` edit.
- **New master durations**: landscape **139.875s** (was 140.33s), vertical **139.875s** (was 140.33s) — both match the expected ~0.41s shift from the B01 retime, and both confirmed true 4K (3840×2160 / 2160×3840).
- **GATE V (final masters, `final_frame_check.py --lenient`)**: landscape **0 BLOCKER, 35 MAJOR**; vertical **0 BLOCKER, 41 MAJOR**. Ship bar (0 BLOCKER) met on both. The MAJOR findings are the same full-continuous-frame-scan sampling artifact (transitional/fade frames across many untouched beats) documented in this fellow's other retrofitted videos, not a regression from this change.
- **Manual frame verification**: extracted real frames (ffmpeg) from B01 and B08 in both masters — name tag reads "Sai Pranavi J." cleanly in both aspects; B08 sign-off reads "in for Sai Pranavi J." on its own line, fully contained within its bordered card, no clipping, in both aspects.
- **Deliverables renamed**: `deliverables/landscape/LostInTheMiddle_SaiPranaviJeedigunta.mp4` (+ `.verified.json`) → `LostInTheMiddle_SaiPranaviJ.mp4` (+ `.verified.json`), same for `deliverables/vertical/` — copied from the freshly rebuilt masters, sha256-verified identical to `deliverables/landscape/2026-10-06-lost-in-the-middle-why-more-context-isnt-better.mp4` / `deliverables/vertical/...-vertical.mp4`, then the old-named files and sidecars deleted.
- `README.md` name references ("Sai Pranavi Jeedigunta" / "SaiPranaviJeedigunta") updated to "Sai Pranavi J." / "SaiPranaviJ" — no other claims changed (the 140.33s duration mentioned in the pre-existing README prose is now superseded by the 139.875s figure above).
- Not touched: `FACTCHECK.md`, `SOURCES.md`, `beat_sheet.json` metadata/gates beyond the `narration_text` field.
