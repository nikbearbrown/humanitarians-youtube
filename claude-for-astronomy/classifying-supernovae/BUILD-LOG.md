# BUILD-LOG — *What We Chased Before.*

**AI in Astronomy & Space Science · Ep. 10** · slug `classifying-supernovae`
Built with `brutalist.art` (the free-only Fellow Tier), skill `ai-explainer`,
channel `claude-hai`, Pragmatist register. Built 2026-09-25.

**Total spend: $0.00.** Kokoro TTS runs locally; every plate is computed here;
no API key was used or required at any step.

---

## What shipped

| | 16:9 | 9:16 |
|---|---|---|
| `claude-for-astronomy_OmMali_25_09_2026.mp4` | 3840 × 2160 · 147.72 s · 3545 frames · 17.2 MB | — |
| `classifying-supernovae-9x16.mp4` | — | 2160 × 3840 · 147.72 s · 3545 frames · 18.5 MB |

24 fps, h264 + AAC, −21.0 LUFS integrated, LRA 3.0 LU, both cuts sharing one
audio mix. **2:27.7** — 32.3 s inside the 3:00 cap.

Both masters live in this folder. Nothing was published; there is no
publishing machinery in this toolkit.

---

## The episode

Topic 10 of the brief is AI triaging which transient sky events to chase. The
obvious telling is a speed story. This one is about the **feedback loop**: the
training set is the output of the system's own past decisions, because
spectroscopy is scarce and what got a spectrum became what got a label.

The centrepiece is not an anecdote but an experiment — `assets/gen_triage.py`
runs 60 repeats × 12 seasons × 20 spectra across three follow-up strategies
and **asserts its own central claim**, writing no plates if the claim fails.

Headline result: spending the budget on confidence raises overall accuracy
0.883 → 0.897 while the rare class's **median recall stays at exactly zero**,
never recognised once in 48 of 60 runs. Spending it where the model is least
sure reaches median recall 0.638, fails in 0 of 60, and ends with *higher*
accuracy too. One night in ten on doubt takes the chance of ever finding the
rare class from 35% to 92%, for 18% of the confirmations.

---

## Pipeline, in the order it ran

1. **Research** from primary sources → `SOURCES.md`, `FACTCHECK.md`. Fourteen
   claims checked; published and computed-here figures kept visibly apart, on
   screen and in the voice.
2. **`assets/gen_triage.py`** — six plates, each reporting its own diagnostics,
   with a three-part self-check.
3. **`beat_sheet.json`** — 14 beats, 429 words, sized to the measured
   seconds-per-word rate carried forward from Ep. 09.
4. **Paperwork** — SHOTLIST, PROMPTS, CHECKS-REPORT, PEDAGOGY.
5. **GATE P** — signed `VERDICT: PASSED`, Om Mali, 25/09/26. Audio is not
   generated before this, even though audio here is free.
6. **Audio** — `generate_audio_kokoro.py`, voice `af_bella`, 14 MP3s totalling
   147.7 s. **These durations are the master clock from here on.**
7. **Pacing solved without rendering** — natural scene lengths measured under
   a dry-run stub, then RT/HOLD solved per scene against the measured MP3s.
8. **Pacing verified at 24 fps in both aspects** before committing to 4K.
9. **20 scenes rendered at 4K, one Manim process at a time**, each verified
   against its beat, with `frames/24 == duration` and monotonic mtimes.
10. **Remotion bookends** via `remotion_scenes.py` (foreground, never a
    hand-rolled `npx remotion render`), then `compile.py --height 2160`.
11. **GATE V**, then the 9:16 derivative, then GATE V again.
12. **Both masters read frame by frame** → `_qc/VISUAL-QC.md`.

---

## Gate results

| Gate | Result |
|---|---|
| F — paperwork set | present |
| L — beat-mix lint | clean |
| A — static pre-flight | 10/10 `rc=0` |
| W — WCAG · margins · overlap | 10/10 `rc=0` |
| B — pixel layout, both aspects | 20/20 `rc=0`, after 11 fixes |
| P — human signature | PASSED, before audio |
| Pacing — 24 fps, both aspects | 20/20 inside `−0.25 s … +0.05 s` |
| V — 16:9 master | 28 frames · 0 BLOCKER · 0 MAJOR |
| V — 9:16 master | 28 frames · 0 BLOCKER · 0 MAJOR |

**GATE T and GATE SHARPNESS were not run: they are not shipped in this
toolkit**, despite `ai-explainer/SKILL.md` describing GATE T as "ALWAYS RUN".
`scripts/type_check.py` does not exist and `run.sh` wires no such gate. Said
plainly rather than quietly skipped — see CHECKS-REPORT for what covers which
clause instead.

---

## Pacing

Every scene is a `Paced` subclass: a run-time multiplier, a per-reveal hold,
and a `hold_to_beat()` tail that pads to the measured narration.

`TAIL_TRIM = 0.18` is subtracted from every beat target. `renderer.time`
**under-reports** the rendered length — each play's frame count rounds up and
the error accumulates with the number of reveals — and lowering RT or HOLD
cannot fix it, because a smaller body raises `target − now` by exactly the
same amount. Ep. 09's B10 overshot by +0.12 s for this reason.

It worked cleanly here. All 20 clips landed **−0.13 to −0.22 s** under their
beats, no scene hit the 0.35 s floor, and no RT rescue was needed.

Undershoot is safe and overshoot is not: `compile.py` pads a short clip by
holding its last frame, which is invisible, but centre-cuts a long one, which
would clip the closing line off both ends.

---

## Errors this build caught

**Three in the experiment, all mine**, before a single frame rendered:

1. I claimed rare-class recall "collapses" under greedy. It does not — it
   starts at zero, because a brightness-biased seed set contains no rare
   objects, and never leaves. The loop does not create the blind spot; it
   inherits and preserves it. The claim was rewritten to match the
   experiment, not the other way round.
2. **I quoted a mean of a bimodal outcome.** A 12-repeat mean read 0.088 where
   the median is 0.000 and 48 of 60 runs end with no recall at all. "Low
   recall" and "usually none whatsoever" are different claims and only the
   second is true. Now 60 repeats and medians throughout.
3. Two plates measured the same configuration with different statistics
   (0.281 against 0.000), plus an off-by-one: the loop recorded metrics at the
   *top* of each season, so its last point reflected eleven rounds, not twelve.

**Two plates that computed the truth and drew it badly:** `loop.png` put
accuracy on a 0–1 axis where all three curves collapsed to one flat line
(zoomed to 0.84–0.94), and `budget.png` plotted a median of a bimodal variable
as a jagged step (replaced with P(rare class ever found)).

**Ten GATE B failures**, of which B05 was a genuine redesign: a closed ellipse
drawn through four boxes put a stroke under all eight labels, and the portrait
boxes ran off-frame. It became a chain with a return leg routed below in
landscape and beside in portrait.

**A patch script that reported success and wrote nothing.** Its second
substitution failed an assert because an earlier edit had already changed the
surrounding text, so the file was never written — and the generator then ran
with the old code and produced identical output. The same failure mode as
Ep. 09's. Any patch of this shape needs its assertions checked *and* its
output diffed.

**My own B03 portrait "nudge" made it worse** — raising the column pushed it
into the plate's caption. Reverted; the real fix was the portrait reduction.

**Two defects only reading the finished frames caught** — B04's chip sitting
eleven pixels under the axis labels with GATE B clean, and the one-page recap
omitting the cost. Both in `_qc/VISUAL-QC.md`.

**GATE V was checking the wrong file.** Given only a reel folder it takes
`glob("*.mp4")[0]`, and `…-9x16.mp4` sorts before `….mp4`. Every bare call
after the vertical copy existed silently re-checked the vertical file. Caught
because the gate's B11 verdict and a hand measurement of the landscape frame
disagreed, and only one file could explain both.

---

## Aspect discipline

`scenes.py` renders both cuts from one source. Manim keeps `frame_height =
8.0` in either aspect, so the vertical band plan is identical and only the
horizontal extent changes — x ±6.15 landscape, ±1.80 portrait.

**Portrait is not a crop.** It has less usable area, so it carries fewer
elements, larger. The rule, unchanged since Ep. 08: *anything the narration
speaks stays on screen; the on-screen-only extras are what portrait loses.*

Portrait remains the stricter aspect. Ep. 08 failed GATE B 8/10 in portrait
against 1/10 in landscape.

---

## Reproducing this reel

```bash
PY=.venv/Scripts/python.exe            # a Windows venv has no python3.exe
R=<this folder>

$PY assets/gen_triage.py               # plates; asserts its own claim
$PY runtime/scripts/generate_audio_kokoro.py "$R"     # needs GATE P signed
$PY -m manim -qk --fps 24 -r 3840,2160 scenes.py <Scene>   # one at a time
$PY -m manim -qk --fps 24 -r 2160,3840 scenes.py <Scene>
$PY runtime/scripts/remotion_scenes.py "$R"
$PY runtime/scripts/compile.py "$R" --height 2160
$PY runtime/qc/final_frame_check.py "$R" --mp4 "$R/claude-for-astronomy_OmMali_25_09_2026.mp4"
```

The 9:16 cut is built the same way through `shorts.py --drop --no-endcard`,
with the portrait clips staged into `short/manim/` and `--height 3840`.

Pass `--mp4` explicitly to the frame check. Always.
