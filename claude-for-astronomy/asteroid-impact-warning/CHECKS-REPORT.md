# CHECKS-REPORT — *The Number Went Up.*

Ep. 08 · written **before the first slate compiled**, as the PROOF GATE in
`skills/make/ai-explainer/SKILL.md` § "PROOF GATE" requires. Classification
rules are nopunt's (`skills/make/nopunt/SKILL.md`).

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
| B03 | SHOW | `detect.png` — two epochs and their difference, mover ringed | Manim + computed plate |
| B04 | SHOW | `stamps.png` — eight classes, two ringed | Manim + computed plate |
| B05 | SHOW | `tracklet.png` — fitted line, hollow artefacts, three counters | Manim + computed plate |
| B06 | SHOW | two boxes, the arrow, and the fan of permitted orbits | Manim |
| B07 | SHOW | the published probability record, rebuilt as a plot | Manim |
| B08 | SHOW | `bplane.png` + `impactprob.png`, both computed here | Manim + computed plates |
| B09 | SHOW | the Moon, the shrinking cloud, the struck figure | Manim |
| B10 | SHOW | the automation card + `completeness.png` + the counter | Manim + computed plate |
| B11 | SHOW | four artefact lines, one per spoken clause | Remotion `ClaudeVerdictArtifact` |
| B12 | SHOW | the handoff prompt types itself; three grading lines | Remotion `ClaudeComposerAsk` |
| B13 | SHOW | title restate, rule, handle, subline | Remotion `ClaudeTitleOutro` |

**No beat is a bare CARD.** Every beat whose narration makes a factual or
structural claim names its on-screen artifact in `shot.show`, and every one of
those artifacts exists.

## Teaching-arc checklist

| Item | Where | Note |
|---|---|---|
| **FRAMEWORK before examples** | B02 (BLUF), then B06 | B02 states the whole shape in one breath — scan, filter, decide. B06 makes the learned/computed split explicit *before* either worked example lands. |
| **WORKED EXAMPLE** | B04–B05 (the classifier) and B07 (2024 YR4) | One on each side of the handoff. Both are single named cases with published numbers, not surveys. |
| **FALSIFIABILITY** | B08, and the generator itself | B08's claim — that the rise is forced by geometry — is stated as something checkable, and `gen_neo.py` checks it against an analytic prediction and refuses to write a plate if it disagrees. B09 then tests the claim against a *second* independent case (the Moon) and it holds. |
| **SCAFFOLDED TASK** | B12 | The prompt is read aloud, then discussed: what to run it on ("a forecast you actually track") and what to look for ("whether it asks what is shrinking"). Three grading criteria on screen. |
| **BOOKENDS** | B00 · B11 · B12 · B13 | All four present, in order, in the fixed Claude skin. |
| **NO-SOURCE-NO-VERDICT** | every claim beat | Each of B03–B10 carries a citation line. The two verdict-shaped beats (B06's "it never computes a risk", B10's "the search is the unfinished part") both cite. |

## Legibility contract

Checked on every SHOW claim beat:

- **Artifact named in `shot.show`** — yes, all 14.
- **~15–35% negative space** — GATE B measures ink coverage per snapshot; no
  scene is flagged for over- or under-fill in either aspect.
- **Nothing un-highlighted below ~40% opacity** — the reel uses colour and
  weight for emphasis, never opacity fades. The only sub-full-opacity element
  anywhere is `_plate(..., opacity=)`, which is unused in this reel.
- **Comparisons side-by-side, held ≥2 s** — B03 (three panels), B04 (eight
  panels), B06 (two boxes), B08 (three panels + curve), B10 (card + bars). At
  the solved pacing every one of these is held well over 2 s.

## PPT TEST

No beat could be exported as a static slide. Every beat has motion that enacts
its sentence: type struck through on the spoken contrast (B01, B04, B09, B10),
counters running to their value on the spoken figure (B05, B07, B09, B10), a
line fitted through points as the claim is made (B05), a boundary where the
accent stops (B06), a cloud shrinking across three states (B08). **No two
consecutive beats share a visual scheme.**

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
| B — pixel-true layout, both aspects | 20/20 `rc=0` |
| P — human signature | **PASSED** — signed Om Mali, 11/09/26 (this row updated after the fact; the rest of this document was written before the first compile, as the PROOF GATE requires) |

## Not run, and why

**GATE T (type-lock) could not be run: `scripts/type_check.py` does not exist
in this toolkit.** `skills/make/ai-explainer/SKILL.md` describes GATE T as
"ALWAYS RUN" and as a hard block on `./art run` and `./art final`, but the
script is not shipped in `brutalist.art` — `find . -name type_check.py` returns
nothing, and `run.sh` wires no such gate. The same is true of GATE SHARPNESS.
This is a gap between the doctrine and the shipped toolkit, not a step that was
skipped here; it is logged in `BUILD-PROMPT.md` § "Still unpatched upstream".

What GATE T would have checked is partly covered by gates that *did* run:
§8.1 minimum type size and §8.3 contrast by GATE W, §8.2 overflow and §8.5
wordy-card by GATE B. §8.4 kerning sanity and §8.6 golden strings per rendered
frame are **not** covered by anything, and were verified by reading frames
instead (`_qc/VISUAL-QC.md`).
