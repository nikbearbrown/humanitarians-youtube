# CHECKS-REPORT — *What We Chased Before.*

Ep. 10 · written **before the first slate compiled**, as the PROOF GATE in
`skills/make/ai-explainer/SKILL.md` requires. Classification rules are
nopunt's.

```
14 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

nopunt's rule: **HOLD** is legitimate only for a genuine archival
*photograph*. This reel has none, so it has no HOLDs — and no PUNTs.

| Beat | Class | Artifact named in `shot.show` | Tool |
|---|---|---|---|
| B00 | SHOW | the composer types the ask; three result lines land | Remotion |
| B01 | SHOW | name card; two rows, one struck, one boxed | Manim |
| B02 | SHOW | three sets of kinetic type, the third underlined | Manim |
| B03 | SHOW | `deadline.png` + the shaded window + two counters | Manim + computed plate |
| B04 | SHOW | `selection.png` — four published bars, the gap ringed | Manim + computed plate |
| B05 | SHOW | four chained boxes and the terracotta return leg | Manim |
| B06 | SHOW | `loop.png` — accuracy against rare-class recall | Manim + computed plate |
| B07 | SHOW | `composition.png` + the 0.19% / 16.8% pair | Manim + computed plate |
| B08 | SHOW | `boundary.png` — season 1 and season 8 + two chips | Manim + computed plate |
| B09 | SHOW | the deployed card, the chip, the two unexpected classes | Manim |
| B10 | SHOW | the tell card + `budget.png` + the 35% → 92% counter | Manim + computed plate |
| B11 | SHOW | five artefact lines — four spoken clauses plus the cost | Remotion |
| B12 | SHOW | the handoff prompt types itself; three grading lines | Remotion |
| B13 | SHOW | title restate, rule, handle, subline | Remotion |

**No beat is a bare CARD.**

## Teaching-arc checklist

| Item | Where | Note |
|---|---|---|
| **FRAMEWORK before examples** | B02, then B03–B05 | B02 states the shape in one breath; B03 gives the pressure, B04 the selection, B05 the mechanism — all before any experimental result. |
| **WORKED EXAMPLE** | B09 | One named deployed system followed through: the rule it uses, the telescope, the spectra spent, and the classes it turned up that nobody was looking for. |
| **FALSIFIABILITY** | B06, B08, B10 — and the generator | B06 is an experiment whose result is asserted; `gen_triage.py` refuses to write plates if the claim does not hold, and it refused three times for real errors. B10 states the cost of the fix, not just its benefit. |
| **SCAFFOLDED TASK** | B12 | The prompt is read aloud, then discussed: run it on a model you rely on; watch whether it asks what is missing. Three criteria on screen. |
| **BOOKENDS** | B00 · B11 · B12 · B13 | All four, in order, in the fixed Claude skin. |
| **NO-SOURCE-NO-VERDICT** | every claim beat | B03–B10 all carry a citation line. B06–B08 and B10 cite *this reel's own computation* and say so explicitly. |

## Legibility contract

- **Artifact named in `shot.show`** — all 14.
- **~15–35% negative space** — GATE B reports no over- or under-fill in either aspect.
- **Nothing un-highlighted below ~40% opacity** — the reel uses colour and
  weight for emphasis, never opacity fades.
- **Comparisons side-by-side, held ≥2 s** — B04 (four bars), B06 (two panels),
  B07 (two panels), B08 (two snapshots), B10 (card + curve). All held well
  over 2 s at the solved pacing.

## PPT TEST

No beat could be exported as a static slide. Type struck on the spoken
contrast (B01, B09, B10); counters running to value on the spoken figure (B03,
B06, B07, B10); a chain assembling and then *closing on itself* (B05); two
panels where one curve moves and two do not (B06); rings migrating across a
feature space between two snapshots (B08). **No two consecutive beats share a
visual scheme.**

## ILLUSTRATE LAW

The Claude UI appears at **B00, B11, B12, B13 only**. All ten inner beats
illustrate their own concept as reel-local Manim. No composer wallpaper.

## Gates at the time of writing

| Gate | Result |
|---|---|
| F — paperwork set | FACTCHECK · SHOTLIST · PROMPTS all present |
| L — beat-mix lint | clean |
| A — static pre-flight | 10/10 `rc=0` |
| W — WCAG · margins · overlap | 10/10 `rc=0` |
| B — pixel-true layout, both aspects | 20/20 `rc=0` (after 11 fixes) |
| Visual pre-flight | 4 defects found by reading frames; all fixed |
| P — human signature | **PASSED** — `PEDAGOGY.md`, signed Om Mali, 25/09/26 |

## Gates after the build

| Gate | Result |
|---|---|
| P — human signature | PASSED before any audio was generated |
| Pacing — 24 fps, both aspects | 20/20 inside `-0.25 s … +0.05 s`; every clip lands −0.13 … −0.22 s under its beat |
| V — frame QC, 16:9 master | 28 frames · BLOCKER 0 · MAJOR 0 → `_qc/REPORT-16x9.md` |
| V — frame QC, 9:16 master | 28 frames · BLOCKER 0 · MAJOR 0 → `_qc/REPORT-9x16.md` |
| Frame reading, both aspects | 2 defects found and fixed — see `_qc/VISUAL-QC.md` |

**GATE V has to be pointed at the file you mean.** It picks
`glob("*.mp4")[0]` when given only a reel folder, and
`classifying-supernovae-9x16.mp4` sorts *before*
 `claude-for-astronomy_OmMali_25_09_2026.mp4` because `-` precedes `.`. Once the 9:16 copy
existed, every bare `final_frame_check.py <reel>` call silently re-checked the
vertical file while reporting as though it were the landscape one. Both rows
above come from explicit `--mp4` runs.

## Not run, and why

**GATE T (type-lock) could not be run: `scripts/type_check.py` does not exist
in this toolkit.** SKILL.md describes it as "ALWAYS RUN" and a hard block on
`./art run` and `./art final`, but the script is not shipped and `run.sh`
wires no such gate; the same is true of GATE SHARPNESS.

§8.1 min-size and §8.3 contrast are covered by GATE W; §8.2 overflow and §8.5
wordy-card by GATE B. **§8.4 kerning/font-coverage and §8.6 golden strings are
covered by nothing automated.** Ep. 09 shipped a frame where the `✓` character
— absent from EB Garamond — rendered as stray digits, and only reading frames
caught it. This reel uses no glyph outside the font's coverage for that reason.
