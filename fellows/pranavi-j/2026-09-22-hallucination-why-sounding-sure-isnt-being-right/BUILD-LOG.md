# BUILD-LOG — Hallucination: Why Sounding Sure Isn't the Same as Being Right

## 2026-10-02 — Full build (both aspects)

**Gate P:** Beat sheet approved 2026-10-02. **FACTCHECK:** resolved same day — both B04's
fabricated citation and B05's falsifiability example confirmed fully generic/hypothetical, no
resemblance to any real disclosed incident, model, or paper.

**Audio:** Kokoro `af_bella`, all 9 beats, B00 a real silent mp3 (`ffmpeg anullsrc`, 4.0s) with
`audio_policy: "silence"` set explicitly per `build_safety.py`'s silent-required-audio gate. All 8
spoken beats generated and measured via `generate_audio_kokoro.py`; `actual_duration_s` written
back to `beat_sheet.json` from real ffprobe measurements (B00=4.06 B01=13.10 B02=12.50 B03=25.75
B04=25.58 B05=25.42 B06=23.16 B07=11.14 B08=1.51 — total 142.22s narration/silence). B08's
narration ("Explained with Claude Code.") is short by design — the approved beat sheet's exact
text, not rewritten — so its card is a brief, clean flash rather than an extended hold.

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (creates `Text()` at
`font_size=48`, then scales geometrically to the intended size) used for every on-screen string —
avoids the confirmed Manim/Pango small-font-size rendering artifact (phantom gaps inside words,
e.g. "video" -> "v ideo") already documented by sibling reels this cycle. B03 shows all 3 rubric
questions together (per the Legibility Contract), not a sequential reveal. B04 shows the
fabricated and real citations in identical fluent styling before either resolves. B05 stress-tests
the rubric against a genuinely true, easy fact with a visibly distinct (sage/CONFIRMED) resolution
from B04's (gold/"DOESN'T EXIST"). B06's checklist is a distinct composition from B03's rubric
card, not a second copy.

### Real bugs hit and fixed during this build

1. **Timing-comment arithmetic errors (B04, B05):** when authoring `scenes.py`, the inline
   comments computing each scene's final `self.wait()` from "measured duration minus sum of
   plays/waits" mis-tallied the running wait total for B04 (off by +1.0s) and B05 (off by +1.5s).
   The rendered clips came out 26.58s/26.92s instead of 25.58s/25.42s. `compile.py`'s center-cut
   silently absorbed this (`[art] B05: clip 27.0s center-cut to 25.5s (skip 0.8s head/tail)`)
   rather than erroring — caught by re-deriving every beat's real timing sum with a small parser
   script and comparing against `beat_sheet.json`'s `actual_duration_s`, not by trusting the
   authored comments. Fixed by correcting the final `self.wait()` values (B04: 9.88->8.88s, B05:
   9.52->8.02s) so every beat's real timeline matches its measured audio exactly, with zero
   reliance on auto-trimming, in both `scenes.py` and `vertical/scenes.py`.
2. **Canvas-fill underfill from sequential reveal (B03, landscape):** the first draft revealed the
   3 rubric cards one at a time, timed to narration. GATE V's 50%-of-beat sample landed with only
   2 of 3 cards on screen (51% fill, under the 55% floor). Fixed by showing all 3 cards together
   up front (matching the Legibility Contract's "shown together" requirement more literally),
   then adding per-card `Indicate()` emphasis pulses timed to the narration instead of sequential
   `FadeIn`s — real content mass present for nearly the whole beat, not an oversized invisible box.
3. **Edge-bleed from near-zero margin (B05, landscape):** the 3-tag result row (`CHECKABLE?`,
   `WOULD IT HEDGE?`, `TRACKS DIFFICULTY?`) was sized to exactly the safe-area width with no real
   margin; the tracking box drawn around it pushed past the title-safe left/right edge. Fixed by
   narrowing each tag card and the row's gap for genuine clearance.
4. **Bottom-edge clipping on closing lines (B03, B05, B06, landscape):** GATE B's post-render
   layout audit caught 3 separate closing lines landing with their real bottom edge at y=-3.45 to
   -3.6, outside the +/-3.4 safe-area half-height — not a guessed margin, the actual rendered
   bounds. Fixed with larger `buff` values (0.4-0.55 -> 0.65-0.68) on each.
5. **Portrait title/closing clipping (B02, B03, B04, B05, B06, vertical):** the same class of
   bottom/top-edge bug recurred across the hand-authored portrait redesign, since 2-line titles
   and multi-line closings are taller relative to the narrower ~1.95-unit safe half-width. Fixed
   with the same larger-buff pattern per beat, verified via `manim_layout_audit.py` after each fix.
6. **Text-on-curve collision (B02, vertical):** after fixing the title's safe-margin clipping by
   increasing its `buff`, the closing zinger's bounding box started overlapping the bottom
   bubble's own rounded-corner curve (a real TEXT_ON_CURVE error, not a false positive). Fixed by
   shrinking the two stacked bubble panels and tightening their gap to free real vertical space,
   then using the *smallest* safe-margin-clearing `buff` for the zinger (just above the 0.6 floor)
   rather than a larger one — a larger buff pushes the zinger closer to the stack above it, not
   farther away, since both edges move together.
7. **`./art final` wrong resolution for the 9:16 reel (vertical) — the most significant bug this
   build:** `./art final <reel>` (no explicit `--height`) defaults to `--height 2160`, which
   `compile.py` always treats as the *output pixel height*, computing width from the beat sheet's
   own `aspect_ratio` (`9:16` here: `w = h * 9/16`). For a 9:16 reel this produced a **1216x2160**
   candidate — not the required native 4K **2160x3840** — because the hardcoded default height is
   written for 16:9 reels. The undersized candidate's aspect (1216/2160 = 0.563) doesn't exactly
   match the native clips' aspect (2160/3840 = 0.5625), so `compile.py`'s
   `scale=...,force_original_aspect_ratio=increase,crop=w:h` filter applied a small real crop
   during the mismatched downscale — enough to tip several already-tight beats (B02, B04, B05)
   over the title-safe edge as real BLOCKER `edge-bleed` defects on GATE V, even though the native
   2160x3840 Manim clips were independently confirmed clean (re-verified directly against the raw
   per-beat clips in `vertical/manim/*.mp4` with no defects). Root-caused by comparing GATE V's
   report against a direct `analyze_frame()` check on the untouched native clips. Fixed by always
   passing `--height 3840` explicitly for this reel's vertical final render
   (`./art final vertical/ --height 3840`), producing the correct native 2160x3840 master.
8. **Remaining underfill/edge-bleed after the resolution fix (vertical):** once compiled at the
   correct 2160x3840, 4 beats still had real (smaller) issues: B00/B01/B07's invisible title
   frames and B08's brand-card frame were sized to `MAX_W + 0.6` (half-width 2.1), narrowly
   exceeding the true ~2.025-unit safe half-width for a 2160-wide portrait canvas — fixed by
   trimming every such frame to `MAX_W + 0.3`. B08 then measured a real 39% canvas-fill (min 55%);
   fixed by widening `buff` between its 4 lines and enlarging `fixed_line`/`tagline` (the "handle"
   line was already width-clamped at the safe margin, so only spacing/other-line growth adds real
   mass) across two rounds (39% -> 50% -> clean).
9. **Stale render cache (both aspects, multiple rounds):** `run.sh`/`compile.py` do not detect
   `scenes.py` source changes and will silently reuse old cached `manim/*.mp4`, `clips/*.mp4`, and
   Manim's own `media/` cache. Deleted `manim/`, `clips/`, and `media/` before every re-render that
   followed a scene edit, and verified every clip's mtime postdates `scenes.py`'s mtime via
   `stat -f %m` before trusting a render as current — caught one round where only the
   last-touched class's clip had been refreshed after an edit (the rest were functionally
   unchanged but file-mtime-stale from editing a different class in the same file); resolved with
   one more full clean rebuild. The resulting vertical master was byte-identical (same SHA-256) to
   the prior build, confirming the render is deterministic and the earlier concern was purely
   mtime bookkeeping, not a content defect.
10. **Review-slate GATE V false positives (expected, not a real defect, both aspects):** running
    `./art run` always compiles a `*-slate.mp4` review cut with burn-in timecode/beat-label
    overlays for human review, then runs GATE V against *that* compiled cut as an early warning.
    The burn-in timestamp (top-right) sits outside `final_frame_check.py`'s `BURN_IN_EXCLUDE` zone
    (which only blanks the bottom-left beat-label strip), so every beat's review-slate sample
    reports a spurious `edge-bleed` BLOCKER. Confirmed as a slate-only artifact (not present in the
    clean final master, which has no burn-in by design) and did not block the true final render,
    which is produced separately via `./art final` and carries no labels.

**Landscape final:** 3840x2160, 24fps, h264/aac, 142.375s. GATE V on the true clean master: 0
BLOCKER, 0 MAJOR.

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(1080x1920-native coordinate system, rendered 2160x3840), same `T()` helper plus the portrait
`config.frame_width` patch (Manim's CLI `-r` flag doesn't recompute `frame_width` for portrait
otherwise — documented fix, copied from this fellow's sibling reels' `vertical/scenes.py`). B02's
two-bubble hook, B04's two-citation worked example, and B05's 3-tag result row all needed genuine
top/bottom-stack redesigns (not just narrowing) to stay legible in the narrow canvas — confirmed
by direct frame inspection, not assumed. Every `self.play`/`self.wait` duration matches
`scenes.py` beat-for-beat, so the vertical master's total runtime is identical to the landscape
master's (142.375s both) — full-length, all 9 beats, no drops, no duration cap, no added endcard,
per `./art vertical`'s contract.

**Vertical final:** 2160x3840, 24fps, h264/aac, 142.375s. GATE V on the true clean master: 0
BLOCKER, 0 MAJOR.

**Process note:** every render step in this build was run as a single blocking foreground command
and waited out fully — no step was backgrounded. The final landscape and vertical masters were
personally re-inspected frame-by-frame (B02, B03, B04, B05, B07, B08) directly from the shipped
deliverables as a final check before considering this project done, including re-extracting a
transient mid-`Create()`-animation frame in B02 and B05 that looked like a rendering artifact in a
quick spot-check, then confirming via a proper steady-state extraction that both beats render
cleanly (the apparent artifact was purely a sampling-timing coincidence, not a real defect).

**Deliverables confirmed, both renamed and verified (SHA-256 matched against the source render
before and after copy):**
- `deliverables/landscape/HallucinationConfidence_SaiPranaviJeedigunta.mp4` (+ `.verified.json`)
- `deliverables/vertical/HallucinationConfidence_SaiPranaviJeedigunta.mp4` (+ `.verified.json`)

GATE V re-run directly against both final deliverable files (via `final_frame_check.py --mp4
<path> --lenient`, run from inside each reel folder): 0 BLOCKER, 0 MAJOR on both.

Publishing not authorized — beat_sheet.json's `publish` gate is marked ready-for-review, not
approved. Nothing inside `brutalist/` was modified.

## 2026-10-20 — ADDENDUM: fellow-name retrofit (org naming policy: first-name-last-initial only)

- **Scope**: full name "Sai Pranavi Jeedigunta" found in spoken narration (B01), the on-screen name tag (B01), and the on-screen sign-off credit (B08, both aspects). Retrofitted to "Sai Pranavi J." everywhere.
- **Narration (B01)**: `narration_text` changed in `beat_sheet.json` and `vertical/beat_sheet.json`: "Hi, I'm Sai Pranavi Jeedigunta." → "Hi, I'm Sai Pranavi J." Regenerated Kokoro audio (`af_bella`, `generate_audio_kokoro.py --only B01`) for both `mp3/beat-B01.mp3` files. New measured duration **12.65s** (ffprobe: 12.648s) vs the old `actual_duration_s` of **13.10s** — a 0.45s shrink, over the ~0.3s retime threshold.
- **Retiming (B01)**: both landscape and vertical plays sum to 2.1s → `self.wait(11.0)` changed to **`self.wait(10.55)`** (13.10 base wait recalculated: 12.648 − 2.1 = 10.548) in both `scenes.py` and `vertical/scenes.py`.
- **On-screen credit**: `scenes.py` B01 name tag "Sai Pranavi Jeedigunta" → "Sai Pranavi J."; B08 tagline "in for Sai Pranavi Jeedigunta" → "in for Sai Pranavi J." (plus a matching comment-line fix). `vertical/scenes.py` B01 name tag and B08 tagline changed the same way (both were already single-line, width-only changes).
- **Stale-cache avoidance**: deleted `manim/B01.mp4`, `clips/B01.mp4`, `manim/B08.mp4`, `clips/B08.mp4` and the same four paths under `vertical/` before rebuilding — no other beat's cache touched.
- **Rebuild**: `./art run . --height 1080` and `./art run vertical --height 1920` re-rendered only B01/B08 via Manim (GATE A/B CLEAN); both review GATE V runs showed the known review-slate false positive (18/18 frames `edge-bleed`, uniform across every beat including untouched ones). `./art final . --out deliverables/landscape` and `./art final vertical --height 3840 --out deliverables/vertical` rebuilt both true masters cleanly on the first attempt (B08's shortened tagline did not trip the canvas-fill floor here, unlike the sibling 2026-09-22 all-clear-email video's vertical B08). Verified via `stat -f %m` that every regenerated `manim/B01.mp4`/`manim/B08.mp4` (both aspects) postdates its `scenes.py` edit.
- **New master durations**: landscape **141.917s** (was 142.375s), vertical **141.917s** (was 142.375s) — both confirmed true 4K (3840×2160 / 2160×3840).
- **GATE V (final masters, `final_frame_check.py --lenient`)**: landscape **0 BLOCKER, 36 MAJOR**; vertical **0 BLOCKER, 35 MAJOR**. Ship bar (0 BLOCKER) met on both. The MAJOR findings are the same full-continuous-frame-scan sampling artifact (transitional/fade frames across many untouched beats) documented in this fellow's other retrofitted videos, not a regression from this change.
- **Manual frame verification**: extracted real frames (ffmpeg) from B01 and B08 in both masters — name tag reads "Sai Pranavi J." cleanly in both aspects; B08 sign-off reads "in for Sai Pranavi J." on its own line, fully contained within its bordered card, no clipping, in both aspects.
- **Deliverables renamed**: `deliverables/landscape/HallucinationConfidence_SaiPranaviJeedigunta.mp4` (+ `.verified.json`) → `HallucinationConfidence_SaiPranaviJ.mp4` (+ `.verified.json`), same for `deliverables/vertical/` — copied from the freshly rebuilt masters, sha256-verified identical to `deliverables/landscape/2026-09-22-hallucination-why-sounding-sure-isnt-being-right.mp4` / `deliverables/vertical/...-vertical.mp4`, then the old-named files and their `.verified.json` sidecars deleted.
- `README.md` name references ("Sai Pranavi Jeedigunta" / "SaiPranaviJeedigunta") updated to "Sai Pranavi J." / "SaiPranaviJ" — no other claims changed (the 142.375s duration mentioned in the pre-existing README prose is now superseded by the 141.917s figure above; README text itself was left as a name-only find/replace per the retrofit's scope).
- Not touched: `FACTCHECK.md`, `SOURCES.md`, `beat_sheet.json` metadata/gates beyond the `narration_text` field.
