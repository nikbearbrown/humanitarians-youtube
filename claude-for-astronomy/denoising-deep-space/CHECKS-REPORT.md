# CHECKS-REPORT — *The Sharpest Guess.*

Ep. 09 · written **before the first slate compiled**, as the PROOF GATE in
`skills/make/ai-explainer/SKILL.md` requires. Classification rules are
nopunt's (`skills/make/nopunt/SKILL.md`).

```
14 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

nopunt's rule: **HOLD** is legitimate only when the beat needs a genuine
archival *photograph*. Everything else animates, and leaving it unfilled is a
PUNT. This reel has no photographs, so it has no HOLDs — and no PUNTs.

| Beat | Class | Artifact named in `shot.show` | Tool |
|---|---|---|---|
| B00 | SHOW | the composer types the ask; three result lines land | Remotion `ClaudeComposerAsk` |
| B01 | SHOW | name card; two rows, one struck, one boxed in the accent | Manim |
| B02 | SHOW | three sets of kinetic type on a card, third underlined | Manim |
| B03 | SHOW | `twokinds.png` — striped, cleaned, blurred, true | Manim + computed plate |
| B04 | SHOW | `forward.png` — the four-step chain + the 98% counter | Manim + computed plate |
| B05 | SHOW | `nullspace.png` — two skies, their difference, one image | Manim + computed plate |
| B06 | SHOW | `threeanswers.png` — three samples + three χ² values | Manim + computed plate |
| B07 | SHOW | the training-tile card, the arrow, the prior box, the counter | Manim |
| B08 | SHOW | `posterior.png` — samples, mean, disagreement map | Manim + computed plate |
| B09 | SHOW | `varratio.png` + the two published figures, tagged | Manim + computed plate |
| B10 | SHOW | the automation card + two schematic panels + QUALITATIVELY | Manim |
| B11 | SHOW | four artefact lines, one per spoken clause | Remotion `ClaudeVerdictArtifact` |
| B12 | SHOW | the handoff prompt types itself; three grading lines | Remotion `ClaudeComposerAsk` |
| B13 | SHOW | title restate, rule, handle, subline | Remotion `ClaudeTitleOutro` |

**No beat is a bare CARD.** Every beat whose narration makes a factual or
structural claim names its on-screen artifact in `shot.show`, and every one of
those artifacts exists.

## Teaching-arc checklist

| Item | Where | Note |
|---|---|---|
| **FRAMEWORK before examples** | B02 (BLUF), then B03–B04 | B02 states the whole shape in one breath — blurred and noisy, some of it arithmetic, the rest an assumption. B03 draws the distinction and B04 gives the mechanism, both *before* any reconstruction is shown. |
| **WORKED EXAMPLE** | B07 (the diffusion prior) and B09 (its published variance ratios) | One named system, followed through: what it was trained on, what it costs, and the metric its authors propose for catching its own failures. |
| **FALSIFIABILITY** | B05, B06, B09 — and the generator itself | B05 is a *proof*: two skies, one image, asserted numerically. B06 forces three priors to identical χ² so the difference between them cannot be explained by fit quality. B09 gives the detector. And `gen_deconv.py` asserts two of its own claims and writes nothing if either fails — it has already refused to run five times, four of them for real errors of mine. |
| **SCAFFOLDED TASK** | B12 | The prompt is read aloud, then discussed: what to run it on ("something you have enhanced") and what to look for ("whether it asks for a range"). Three grading criteria on screen. |
| **BOOKENDS** | B00 · B11 · B12 · B13 | All four present, in order, in the fixed Claude skin. |
| **NO-SOURCE-NO-VERDICT** | every claim beat | Each of B03–B10 carries a citation line. B05's cite points at this reel's own computation rather than a paper, and says so. The two verdict-shaped beats (B06's "sharpness is a choice", B10's "report the range") both cite. |

## Legibility contract

Checked on every SHOW claim beat:

- **Artifact named in `shot.show`** — yes, all 14.
- **~15–35% negative space** — GATE B measures ink coverage per snapshot; no
  scene is flagged for over- or under-fill in either aspect.
- **Nothing un-highlighted below ~40% opacity** — the reel uses colour and
  weight for emphasis, never opacity fades. The one exception is B07's
  training tiles, whose fill opacity varies 0.25–0.85 by design to read as a
  heterogeneous dataset; they carry no text.
- **Comparisons side-by-side, held ≥2 s** — B03 (four panels), B04 (four),
  B05 (two skies + one image), B06 (three), B08 (five), B10 (two schematics).
  At the solved pacing every one is held well over 2 s.

## PPT TEST

No beat could be exported as a static slide. Every beat has motion that enacts
its sentence: type struck through on the spoken contrast (B01, B10), counters
running to their value on the spoken figure (B04, B05, B07), χ² values typing
in under each reconstruction as the claim of equal fit is made (B06), a
terracotta box filling where the assumption enters (B07), a disagreement map
arriving last and alone (B08), a ring closing on the weak-data end of a curve
(B09). **No two consecutive beats share a visual scheme.**

## ILLUSTRATE LAW

The Claude UI appears at **B00, B11, B12, B13 only** — cold open, verdict,
handoff, outro. All ten inner beats illustrate their own concept as reel-local
Manim. No composer wallpaper.

## Gates at the time of writing

| Gate | Result |
|---|---|
| F — paperwork set | FACTCHECK · SHOTLIST · PROMPTS all present |
| L — beat-mix lint | clean |
| A — static pre-flight | 10/10 `rc=0` |
| W — WCAG · margins · overlap | 10/10 `rc=0` |
| B — pixel-true layout, both aspects | 20/20 `rc=0` (after 7 fixes) |
| Visual pre-flight | 11 defects found by reading frames; all fixed |
| P — human signature | **PASS** — signed Om Mali, 18/09/2026 (this row updated after the fact; the rest of this document was written before the first compile, as the PROOF GATE requires) |

## Not run, and why

**GATE T (type-lock) could not be run: `scripts/type_check.py` does not exist
in this toolkit.** `skills/make/ai-explainer/SKILL.md` describes GATE T as
"ALWAYS RUN" and as a hard block on `./art run` and `./art final`, but the
script is not shipped in `brutalist.art` — `find . -name type_check.py` returns
nothing, and `run.sh` wires no such gate. The same is true of GATE SHARPNESS.
This is a gap between the doctrine and the shipped toolkit, not a step skipped
here; it is logged in `BUILD-PROMPT.md` § "Still unpatched upstream".

What GATE T would have checked is partly covered by gates that *did* run:
§8.1 minimum type size and §8.3 contrast by GATE W, §8.2 overflow and §8.5
wordy-card by GATE B. §8.4 kerning sanity and §8.6 golden strings per rendered
frame are **not** covered by anything automated — and this reel is the clearest
case yet for why that matters: the `✓` character is absent from EB Garamond and
rendered as stray digits on screen, which is exactly a §8.4-class defect. It
was caught by reading frames, not by a gate.
