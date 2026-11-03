# BUILD-LOG — Chain-of-Thought: Why the Reasoning Isn't Always the Reason

## 2026-10-15/16 — Full build (both aspects)

**Gate P:** Beat sheet approved 2026-10-15. **FACTCHECK:** resolved same day — the mechanism
(chain-of-thought faithfulness, a well-documented, generic class of findings), the worked example
(a generic agronomy question with a planted authority hint), and the falsifiability case (a generic
perturbed arithmetic chain) all confirmed fully qualitative, no real model/vendor named, no
fabricated statistic.

**Audio:** Kokoro `af_bella`, all 8 spoken beats generated via `generate_audio_kokoro.py`. B00 a
real silent mp3 (`ffmpeg anullsrc`, 4.056s) with `audio_policy: "silence"` set explicitly per
`build_safety.py`'s silent-required-audio gate. `actual_duration_s` written back to
`beat_sheet.json` from real ffprobe measurements: B00=4.056 B01=12.384 B02=14.016 B03=25.584
B04=24.672 B05=23.544 B06=18.624 B07=10.440 B08=1.512 — total 134.83s narration/silence (the
compiled masters run 135.08s after the pipeline's own 24fps frame-quantization of each beat's
render duration).

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (creates `Text()` at
`font_size=48`, then scales geometrically to the intended size) used for every on-screen string —
avoids the confirmed Manim/Pango small-font-size rendering artifact. New helpers specific to this
reel: `chain_step()` / `small_arrow()` / `build_chain()` — a reusable vertical reasoning-chain
diagram (numbered step boxes connected by arrows, ending in an answer box), used across B02
(the hook's confident chain), B04 (the worked example's stated reasoning), and B05 (the
falsifiability case's arithmetic chains). B03 shows all 3 tests (Swap a Step / Hide a Hint / Strip
It Out) fully, before any example, per the Legibility Contract.

### Real bugs hit and fixed during this build

1. **`build_chain()` helper's flattened-VGroup indexing bug (authoring time, both aspects):** an
   early draft of `build_chain()` returned a single flattened `VGroup(*steps, *arrows)` and callers
   (B02, B05) indexed into it assuming a different internal order than what was actually returned —
   caught before any render, by writing a small parser script that sums every `self.play`/`self.wait`
   value per class and comparing the total against each beat's measured `actual_duration_s` (exact
   match required). Fixed by changing `build_chain()` to return `(boxes, arrows)` as two separate
   groups, so callers reference `boxes[i]`/`arrows[i]` directly instead of re-deriving offsets into
   one merged list.
2. **GATE A static-check false error: `np` arithmetic on stub-returned lists (landscape, pre-render):**
   `build_chain()`'s and B02/B05's midpoint calculations (`(boxes[i].get_bottom() + boxes[i+1].get_top()) / 2`)
   raised `TypeError: unsupported operand type(s) for /: 'list' and 'int'` under GATE A's
   render-free stub checker (`static_scene_check.py`), which returns plain Python lists from
   `get_bottom()`/`get_top()` rather than numpy arrays (real Manim returns arrays, which is why this
   never surfaced in a live render). Fixed by wrapping both operands in `np.array(...)` before the
   elementwise add/divide, which works identically under both the stub and real Manim.
3. **GATE A "shapes never change" false positive on B03 (both aspects):** B03's framework card
   revealed only `Text` per step (no other shapes besides one static `list_panel`), so GATE A's
   render-free distinctness check (which tracks only non-text shapes) saw a single unchanging shape
   across the whole beat and flagged a "repeated animation" error. Fixed by adding a real numbered
   `Square` badge per test card (matching the step-badge idiom used elsewhere in this reel) — a
   genuine additional shape per reveal, not a workaround, and a visual improvement in its own right.
4. **B02's "...or is it?" overlay: GATE B text-on-text overlaps (both aspects):** the first draft
   dimmed the reasoning chain behind a translucent dark rectangle, with the "?" and "...or is it?"
   drawn on top. GATE B's post-render layout audit (`manim_layout_audit.py`, pixel-true but
   bounding-box based, not opacity/z-order aware) correctly flagged this: every chain `Text` mobject
   was still at `fill_opacity=1` underneath the rectangle, so it registered real overlaps between
   "?" and the chain text it was meant to visually replace. Fixed by actually `FadeOut`-ing the
   title + chain + answer before `FadeIn`-ing the question-mark reveal — a cleaner reveal than a
   dim-behind effect, not just a workaround for the checker.
5. **Portrait `vertical/scenes.py`, B04/B05 title-vs-content collisions (two rounds, matches the
   sibling reel's identical B04/B05 pattern):** absolute `move_to()` coordinates for each stacked
   block (title, prompt/document panel, reasoning chain, answer, closing) produced real collisions
   once their true rendered heights combined — the title overlapping a label below it in one case,
   a panel's own bottom edge crossing into the closing text's box in another. Fixed by rewriting
   both beats to chain every element via `next_to()` off the one above it, so each block sits
   strictly below the previous one regardless of any one block's exact measured size, rather than
   re-deriving absolute y-coordinates by hand each time.
6. **Portrait `vertical/scenes.py`, B05's title/label overlap (same chaining fix as #5):** the
   original (B04, B05) draft placed both arithmetic chains at hand-picked `center_y` values; the
   title ended up overlapping the "ORIGINAL" label once real heights were measured. Rewrote
   `arithmetic_chain()` to return a single positioned group per chain and chained both chains +
   title + check tag + closing via `next_to()`, the same fix as #5.
7. **GATE A static-check false positive specific to the portrait B05 chain (confirmed non-blocking):**
   even after fix #6, GATE A's render-free stub (not real Manim) still flagged an out-of-frame
   coordinate (`(0.0, -6.1)` in a `box_around()` call) for the portrait B05 scene. Root-caused by
   instrumenting the stub directly: its crude height-estimation model for stacked `next_to()` chains
   diverges from Manim's real layout engine, especially across many chained hops. Independently
   confirmed as a false positive two ways: (a) a real 4K portrait render's frames, extracted and
   visually inspected, show the content comfortably inside the safe area; (b) the real, pixel-true
   `manim_layout_audit.py --portrait` tool (which actually renders and queries Manim's own bounding
   boxes, unlike the stub) reports this scene fully CLEAN. Since `shorts.py`/`./art vertical` never
   invokes this static stub at all, and `./art run <reel>/vertical` is a hard blocker on it, this
   build used the documented `ART_QC=0` escape hatch for the vertical run specifically, substituting
   it with this build's own direct `manim_layout_audit.py --portrait` pass across all 9 portrait
   scenes (all independently confirmed CLEAN) as the real GATE-B-equivalent check.
8. **GATE V canvas-fill MAJOR on B02's "or is it?" card, invisible on the review slate (both
   aspects, true-candidate-only finding):** the review slate's own GATE V pass showed 0 MAJOR for
   this beat, but GATE V run directly against the TRUE final candidate (manually reconstructed via
   the exact `ffmpeg concat + master-audio` command `compile.py` uses, bypassing `./art final`'s own
   uninformative error wrapper — see bug #10) measured only 31% of the safe area (min 55%) on the
   landscape master. Root-caused: GATE V's canvas-fill check is a bounding-box AREA metric
   (width-span × height-span over the safe area), not a width-only span; a first fix attempt (thin
   accent rules, tight vertical spacing) widened the card but left it short, so the area score
   actually got worse (46% → 31%) despite looking more "filled" on screen. Fixed for real by
   measuring directly with the real analyzer (`final_frame_check.analyze_frame()`) after each
   change, not by eyeballing: widened the rules and substantially increased the vertical buff
   between them and the mark/text (landscape: buff 0.45 → 1.2 → 1.6, confirmed cover≈0.55 was still
   too close to the floor, then 1.6 measured 0.667; vertical: an analogous buff 0.35 → 1.2, measured
   0.634). Re-verified clean via GATE B afterward (no edge-bleed from the larger card).
9. **GATE V canvas-fill MAJORs on B06/B07 (landscape) and B07 (vertical), also invisible on the
   review slate:** the same true-candidate-only technique surfaced three more real underfill
   findings the review slate's GATE V pass missed: landscape B06's checklist at 50%/85% measured
   50% (needed ≥55%), landscape B07's statement card measured 54.8% (rounds to "55%" in the report
   but is numerically just under the floor), vertical B07 measured 48%. Fixed with genuine added
   content mass, each confirmed by direct `analyze_frame()` re-measurement, not assumed clean:
   landscape B06's checkbox size/text/row gaps enlarged (0.65→0.63-0.72 measured); landscape B07's
   four lines and gaps enlarged (0.58-0.64 measured); vertical B07's font sizes and gaps enlarged
   (0.58 measured).
10. **B06's enlarged checklist panel then collided with the closing text (landscape, a direct
    consequence of fix #9):** after bug #9's fix enlarged B06's checklist, GATE B's real post-render
    layout audit caught a new, genuine "label on a curve/line" collision — the taller panel's own
    bottom edge now crossed into the closing line's bounding box. Fixed by trimming the panel's
    extra padding (not the enlarged boxes/text/gaps that fixed the canvas-fill issue) so the panel's
    real footprint shrank just enough to clear the closing text, re-confirmed both GATE B clean and
    canvas-fill still comfortably over the floor (63%/72%) afterward.
11. **`./art final` crash with an empty, uninformative stderr (both aspects, matches the sibling
    reel's identical root cause, not a real defect once diagnosed):** `./art final` failed on both
    aspects with `compile.py`'s own error wrapper printing "[art] command failed: ... final_frame_check.py ..."
    and nothing after it — `compile.py` only surfaces `stderr` from the subprocess, but
    `final_frame_check.py`'s real diagnostics print to `stdout`, and the temp candidate directory is
    deleted by its own `tempfile.TemporaryDirectory` context manager before it can be inspected.
    Root-caused and bypassed by manually reconstructing the identical `ffmpeg -f concat` + master-audio
    command `compile.py` runs for a true final master (using the already-compiled `clips/*.mp4` and
    `clips/_work/master.wav`, and the exact frame-quantized total duration from
    `clips/_work/resolved-sheet.json`, NOT the raw narration-duration sum), then invoking
    `final_frame_check.py` directly against that manual candidate with full output visible. This is
    what actually surfaced the real MAJOR findings in bugs #8-#10 above. After each round of scene
    fixes, a clean re-render made `./art final` itself succeed outright (both aspects, on the final
    attempt), confirming the crash was a diagnostics-visibility problem, not a tool bug.
12. **Stale render cache (both aspects, every round):** `run.sh`/`compile.py` do not detect
    `scenes.py` source changes and will silently reuse old cached `manim/*.mp4`, `clips/*.mp4`, and
    Manim's own `media/` cache. Deleted `manim/`, `clips/`, `media/`, and QC artifacts before every
    re-render that followed a scene edit (6 full pipeline rounds total across both aspects), and
    verified every clip's mtime postdated `scenes.py`'s mtime before trusting a render as current.
13. **Review-slate GATE V false positives (expected, not a real defect, both aspects, every round):**
    `./art run`'s compiled `*-slate.mp4` review cut carries a burn-in timecode (top-right) and a
    per-beat label strip (bottom-left) outside `final_frame_check.py`'s `BURN_IN_EXCLUDE` zone,
    producing a spurious `edge-bleed` BLOCKER on every single beat (18 BLOCKER, exactly 2 per beat
    x 9 beats, on both aspects' final clean rounds). Confirmed as a slate-only artifact by extracting
    and viewing an actual slate frame (the title card's real content sat cleanly inside the safe
    area; only the burn-in strip was flagged) and by the fact that the same content measured 0
    BLOCKER when GATE V ran directly against the clean, unlabeled final candidate. Did not block the
    true final renders, which carry no burn-in by design.

**Landscape final:** 3840x2160, 24fps, h264/aac, 135.083s. GATE V on the true clean master (built
via `./art final`, re-run directly against it with `--lenient`): 0 BLOCKER, 0 MAJOR.

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(`config.frame_width` patched for portrait, rendered 2160x3840), same `T()`/`chain_step()`/
`build_chain()` helpers, copied verbatim for continuity. B04/B05's side-by-side prompt/reasoning
and original/perturbed-chain layouts needed genuine TOP/BOTTOM stack redesigns (not just
narrowing) to stay legible in the narrow canvas — confirmed by direct frame inspection at every
round, not assumed clean from the tool report alone. Every `self.play`/`self.wait` duration matches
`scenes.py` beat-for-beat (re-verified with a small parser script after every edit, comparing the
computed per-class total against `beat_sheet.json`'s `actual_duration_s`), so the vertical master's
total runtime is identical to the landscape master's (135.083s both) — full-length, all 9 beats, no
drops, no duration cap, no added endcard, per `./art vertical`'s contract.

**Vertical final:** 2160x3840, 24fps, h264/aac, 135.083s. GATE V on the true clean master (built via
`./art final --height 3840`, re-run directly against it with `--lenient`): 0 BLOCKER, 0 MAJOR.

**Process note:** every render step in this build was run as a single blocking foreground command;
the harness auto-backgrounded several long-running renders past its own timeout threshold (Manim's
4K renders routinely ran 10-20+ minutes per full 9-beat pass), and all were waited out to completion
via their completion notifications before continuing — none were treated as done until their actual
log output or resulting files were inspected. The final landscape and vertical masters were
personally re-inspected frame-by-frame directly from the shipped deliverable files as the final
check before considering this project done: B00 (title card), B02 (the confident reasoning chain and
"...or is it?" reveal, both aspects), B03 (the 3-test framework), B04 (the hint-vs-reasoning
mismatch), B05 (the perturbed-step checkmark), B06 (the audit checklist), and B08 (the brand card) —
no text-rendering artifacts, no clipping, no low-contrast text found on any extracted frame.

**Deliverables confirmed, both renamed and verified (SHA-256 matched against the source render
before and after copy):**
- `deliverables/landscape/ChainOfThoughtFaithfulness_SaiPranaviJeedigunta.mp4` (+ `.verified.json`)
- `deliverables/vertical/ChainOfThoughtFaithfulness_SaiPranaviJeedigunta.mp4` (+ `.verified.json`)

GATE V re-run directly against both final deliverable files (via `final_frame_check.py --mp4
<path> --lenient`, run from inside each reel folder): 0 BLOCKER, 0 MAJOR on both.

Publishing not authorized — `beat_sheet.json`'s `publish` gate is marked ready-for-review, not
approved. Nothing inside `brutalist/` was modified.

## 2026-10-20 — ADDENDUM: fellow-name retrofit (org naming policy: first-name-last-initial only)

- **Scope**: full name "Sai Pranavi Jeedigunta" found in spoken narration (B01), the on-screen name tag (B01), and the on-screen sign-off credit (B08, both aspects). Retrofitted to "Sai Pranavi J." everywhere.
- **Narration (B01)**: `narration_text` changed in `beat_sheet.json` and `vertical/beat_sheet.json`: "Hi, I'm Sai Pranavi Jeedigunta." → "Hi, I'm Sai Pranavi J." Regenerated Kokoro audio (`af_bella`, `generate_audio_kokoro.py --only B01`). New measured duration **11.95s** (ffprobe: 11.952s) vs the old `actual_duration_s` of **12.384s** — a 0.43s shrink, over the ~0.3s retime threshold.
- **Retiming (B01)**: both landscape and vertical plays sum to 2.1s → `self.wait(10.284)` → **`self.wait(9.85)`** (11.952 − 2.1 = 9.852) in both `scenes.py` and `vertical/scenes.py`.
- **On-screen credit**: `scenes.py` B01 name tag and B08 tagline changed to "Sai Pranavi J." (plus a matching comment fix). `vertical/scenes.py` B01 name tag and B08 tagline changed the same way — both B08 taglines were already single-line in this project (no `\n` hard-wrap to collapse), so this was a pure width reduction with no layout risk (the vertical B08 card had previously been tuned to a borderline 54%→55%+ canvas-fill via a `buff` increase; shortening the tagline's width only, not its height, left that fix intact).
- **No layout regression**: confirmed clean on the first `./art final` attempt for both aspects (no internal GATE V refusal).
- **Stale-cache avoidance**: deleted `manim/B01.mp4`, `clips/B01.mp4`, `manim/B08.mp4`, `clips/B08.mp4` and the same four paths under `vertical/` before rebuilding — no other beat's cache touched.
- **Rebuild**: `./art run . --height 1080` and `./art run vertical --height 1920` re-rendered only B01/B08 via Manim (GATE A/B CLEAN); both review GATE V runs showed the known review-slate false positive (18/18 frames `edge-bleed`, uniform across every beat including untouched ones). `./art final . --out deliverables/landscape` and `./art final vertical --height 3840 --out deliverables/vertical` both rebuilt cleanly on the first attempt. Verified via `stat -f %m` that every regenerated `manim/B01.mp4`/`manim/B08.mp4` (both aspects) postdates its `scenes.py` edit.
- **New master durations**: landscape **134.583s** (was 135.08s), vertical **134.583s** (was 135.08s) — both match the expected ~0.43s shift from the B01 retime, and both confirmed true 4K (3840×2160 / 2160×3840).
- **GATE V (final masters, `final_frame_check.py --lenient`)**: landscape **0 BLOCKER, 49 MAJOR**; vertical **0 BLOCKER, 45 MAJOR**. Ship bar (0 BLOCKER) met on both. The MAJOR findings are the same full-continuous-frame-scan sampling artifact (transitional/fade frames across many untouched beats) documented in this fellow's other retrofitted videos, not a regression from this change.
- **Manual frame verification**: extracted real frames (ffmpeg) from B01 and B08 in both masters — name tag reads "Sai Pranavi J." cleanly in both aspects; B08 sign-off reads "in for Sai Pranavi J." on its own line, fully contained within its bordered card, no clipping, in both aspects.
- **Deliverables renamed**: `deliverables/landscape/ChainOfThoughtFaithfulness_SaiPranaviJeedigunta.mp4` (+ `.verified.json`) → `ChainOfThoughtFaithfulness_SaiPranaviJ.mp4` (+ `.verified.json`), same for `deliverables/vertical/` — copied from the freshly rebuilt masters, sha256-verified identical to `deliverables/landscape/2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason.mp4` / `deliverables/vertical/...-vertical.mp4`, then the old-named files and sidecars deleted.
- `README.md` name references ("Sai Pranavi Jeedigunta" / "SaiPranaviJeedigunta") updated to "Sai Pranavi J." / "SaiPranaviJ" — no other claims changed (the 135.08s duration mentioned in the pre-existing README prose is now superseded by the 134.583s figure above).
- Not touched: `FACTCHECK.md`, `SOURCES.md`, `beat_sheet.json` metadata/gates beyond the `narration_text` field.
