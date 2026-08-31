# VISUAL QC — human-eye pass

`_qc/REPORT.md` and `short/_qc/REPORT.md` are GATE V's machine output and are
overwritten on every run. This is the VISUAL QC LAW pass beside them: frames
sampled, frames **read**, nine-point rubric audited, defects and fixes — for
**both** deliverables.

## Machine gates, final state

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE P — human signs the narration | **PASS**, signed 2026-08-28 (Om Mali); gate verified open with **no override**, and no audio existed before the signature | same audio, same signature |
| GATE F — paperwork set present | pass (FACTCHECK · SHOTLIST · PROMPTS) | inherits the parent's FACTCHECK |
| GATE L — beat-mix lint | `clean — beat mix OK` | n/a (derivative) |
| GATE A — static pre-flight, 10 scenes | 10 clean / 0 warn / 0 error | same file |
| GATE W — WCAG + margins + overlap | 10 clean | same file |
| GATE B — pixel layout audit, per scene | **CLEAN on all ten** | **CLEAN on all ten** (`--portrait`) |
| GATE V — frame-level QC on the compiled cut | **28 frames · BLOCKER 0 · MAJOR 0** | **28 frames · BLOCKER 0 · MAJOR 0** (after two failures — see below) |
| motion histogram | annotate 3 · drawon 3 · type-on 2 · kinetic 2 · stagger 2 · isotype 1 · fade 1 — max lane 21%, no warning | identical |
| slots | **14/14 filled**, zero slates | **14/14 filled**, zero slates |
| master | 3840×2160 · **173.57 s (2:53.6)** · 31.3 MB · −21.0 LUFS | 2160×3840 · **173.57 s (2:53.6)** · 32.5 MB · −21.0 LUFS |

Same beats, same audio, same runtime in both aspects. No beat was cut for 9:16.

## Frames read (not just sampled)

- **Assets:** the eight-plate contact sheet read three times across the
  generator's tuning passes, plus a close read of the path fan on its own.
- **Pre-render, per scene:** all 10 scenes as final-frame stills **in both
  aspects**, read individually; B08 read three times.
- **Post-render:** `_qc/contact_sheet.png` (16 frames) read on the compiled 16:9
  cut, and `short/_qc/contact_sheet.png` read on the compiled 9:16 cut.
- **Instrumented:** B11's portrait frame measured numerically against GATE V's
  own safe band at three timestamps, to find the edge-bleed cause rather than
  guess at it — the ink box was cols 66..2093 against a safe band of 108..2052.

## Nine-point rubric

| # | Check | Verdict |
|---|---|---|
| 1 | Edge bleed / clipping | **fixed** — B08's portrait card was 4.10 units wide in a 4.5-unit frame; B11's card shadow crossed the portrait safe edge. Both now measured inside. |
| 2 | Title-safe margins | clean — the band plan holds on all 10 Manim beats in both aspects |
| 3 | Container overflow | **fixed** — B08's card was too short for its own contents in 16:9 (signature underline on the border) |
| 4 | Collision | **fixed** — B08's "the rover" label on the closing line (9:16); B09's headings on the title and on their own row labels (9:16) |
| 5 | Offscreen anchors | clean |
| 6 | Legibility | clean — body ≥17pt Manim, titles 30–36, hero numbers 36–98. Terracotta never body text; accents use `#A44A32`. |
| 7 | Brand bug placement | clean — bug on all 10 Manim beats in both aspects, chip on B00/B12, full handle on B13 |
| 8 | Aspect | clean — plates framed at native aspect, never stretched, in either cut |
| 9 | Canvas fill | **fixed** — see below |

## The one that mattered: the compiler was hiding a pacing bug

The first full pass produced a cut that passed GATE V with zero defects and was
still wrong. `compile.py` fills a beat by **slowing the clip to length**, and
these scenes ran 8–12 s against 22–34 s beats — so three beats were being
stretched **3.2–3.3×** into visible slow-motion, and the compiler said so:

    WARNING B05: clip 9.0s slowed 3.3x into 29.7s beat — extreme slow-mo
    WARNING B07: clip 7.9s slowed 3.2x into 24.9s beat — extreme slow-mo
    WARNING B10: clip 10.4s slowed 3.3x into 34.0s beat — extreme slow-mo

GATE V samples still frames, so it can never see this. The fix was not to shorten
the narration — the human had signed it — but to pace the picture to it: a
`Paced` base class that multiplies every `run_time`, rests after each reveal, and
pads the tail to the beat's measured duration. Every slot now lands within
0.05 s of its beat and **the compiler reports no fit factor at all**.

## The 9:16 GATE V failures

Two rounds, six defects, all real, none fixed by relaxing a gate.

**Round one — 2 BLOCKER, 4 MAJOR.**

1. **B08 edge-bleed.** `cw, ch = P(6.30, 4.10), P(3.44, 3.10)` had its
   landscape/portrait values transposed by an earlier patch, so the portrait card
   came out 4.10 units wide inside a 4.5-unit frame. Landscape was unaffected
   (6.30 is fine at 14.22), which is exactly why only the 9:16 cut caught it.
2. **B11 underfill, 42%.** `ClaudeVerdictArtifact916` sized its body type at 1.7%
   of frame height, producing an ~800 px card in a 1920 px frame.
3. **B13 underfill, 19%.** `ClaudeTitleOutro916` centred three small blocks in the
   middle of the column and left the top and bottom thirds empty.

(2) and (3) are the **same root cause Ep. 05 fixed for the landscape components
and did not carry across to the portrait ones.** Both were fixed at the root, in
`runtime/remotion/src/scenes/`, not in this reel — and `consumers.json` confirms
this reel is currently their only consumer, so nothing else moved.

**Round two — 2 BLOCKER.** The rescaled B11 card then crossed the *top* safe
edge, and its box-shadow crossed the left/right one. Backed the type down and
narrowed the card from 92% to 84% of width. Measured, not guessed: ink now spans
rows 486..3380 and cols 165..1994 against a safe band of 192..3648 / 108..2052,
at 79% coverage, stable across three sampled timestamps.

## Known-good, but worth a human ear

- **The reel was re-cut from 5:23 to 2:54** on request. The narration was
  rewritten (974 words to 487); no beat was dropped. The final 13 s came from
  regenerating at `--speed 1.13` rather than editing a signed script — so the
  words are exactly as signed but the delivery is 13% brisker. **That is worth a
  listen**; if it reads as rushed, the alternative is a trimmed script to sign.
- **B12 (handoff) runs 19.0 s** on a near-static composer — the longest static
  stretch, same shape as Eps. 03–05. The prompt is long because HANDOFF LAW
  requires it read verbatim.
- **Two SKIN LINT notices on the 9:16 compile** — "the cold open is
  'ClaudeComposerAsk916' but COLD OPEN LAW wants ClaudeComposerAsk", and the same
  for the outro. These are **expected**: the `916` compositions are the portrait
  counterparts the ONDA CHECK is designed to rewire to. The lint only knows the
  landscape names.
- **The portrait verdict card's title bar is a single non-wrapping line.** The
  parent's artifact title ellipsised at the larger portrait type, so the 9:16
  sheet carries a shorter one ("Verdict — one page"). Worth a look if you change
  either title.
