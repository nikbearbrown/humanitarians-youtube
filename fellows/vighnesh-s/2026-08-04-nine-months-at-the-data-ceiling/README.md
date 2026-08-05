# Weekly Research Report: Nine Months at the Data Ceiling

**Fellow:** Vighnesh ("Manny") Sairaman
**Week ending:** August 4, 2026 (2026-W32)
**Project:** NeuroVEP / ANN mfVEP response classifier
**Advisor:** Dr. Craig Versek
**Reporting period covered:** 2025-W48 → 2026-W32
**Source status:** All results are final and reviewed. Numbers trace to
`docs/progress_report.md`, `docs/architecture_alternatives.md`, `merge_report.md`,
and the fellow's Executive Summary and Work Chronology. See `SOURCES.md`.

This report asks: **can a neural network read a multifocal visual evoked
potential and separate a real visual-field defect from a healthy eye — and if
not, what is actually stopping it?** The answer is a negative result reached by
systematic elimination, and it is the most useful thing the project produced.

The beat sheet contains **12 beats**: a Bella cold open, an executive summary,
two method beats, a results chart and its reading, the failure beat, the causal
finding, the hardware-loss interruption, next steps, a runnable CLI exercise, and
the Humanitarians AI outro. Measured runtime is **4m20s**. Builder:
`ai-explainer` chassis on the `hai` brand.

## Scope note — this is a retrospective, not a backdated weekly

This single report covers nine months. It is dated to the week it was actually
made (2026-W32) and it does **not** claim to be the weekly cadence for the
period it describes. Reports from 2026-W33 forward pair current work with one
labelled retrospective slice each week. Nothing in this folder is dated to a week
in which it was not produced.

## What the report covers

| Beat | Act | Content |
|---|---|---|
| B00 | ASK | Cold open — the question, the narrator, the three results |
| B01 | SUMMARY | Ten architectures, one binding constraint: n = 17 |
| B02 | METHOD | mfVEP, AD25 labelling, the `(2, 10, 600)` input |
| B03 | METHOD | Why leave-one-subject-out, and why from the start |
| B04 | RESULTS | Left-eye accuracy across six models, 17-fold LOSO |
| B05 | RESULTS | Reading the chart — capacity is not the bottleneck |
| B06 | FAILURE | The NB10b leakage defect, self-caught, re-reported downward |
| B07 | FINDING | The model memorises subject identity, not signal morphology |
| B08 | RECOVERY | Hardware loss and the 151,927-file reconstruction |
| B09 | NEXT | Stacked meta-learner; the unwritten clinical-threshold analysis |
| B_CLI | WORKED EXAMPLE | Audit your own CV splits for subject leakage |
| B_OUTRO | OUTRO | Humanitarians AI sign-off |

## Headline results

Left-eye accuracy under 17-fold leave-one-subject-out cross-validation:

| Model | acc_L | Note |
|---|---|---|
| DualEye CNN (NB04) | 0.723 | baseline |
| Per-eye heads (NB06) | 0.749 | |
| + full nnlib augmentation (NB09) | 0.694 | augmentation did not help |
| FBCSP-LDA | 0.728 | classical baseline |
| ATCNet | 0.773 | |
| **EEGNet** | **0.801** | AUC_L 0.892 at 2,578 parameters — best in project |

After the leakage correction, the numbers the project stands behind are
**sensitivity 61.4%, specificity 80.6%.**

## The load-bearing beat

B06 reports that NB10b split at the **sector** level, placing the same subject in
both the augmentation pool and the validation pool. Every headline number under
that split was inflated. It was caught during review, corrected to a strict
subject-level split, and the results were **re-reported downward**. That beat is
the longest in the reel by design. A result that got worse under review is the
one worth showing.

## Production state

- Plan approval: complete
- Narration review (GATE P): **signed** — see `PEDAGOGY.md`
- Audio lock: complete — Kokoro `af_bella`, 12 beats, 260.28s measured
- Slate previz: rendered
- Final compile: complete — 12/12 slots filled, zero slates
- Visual QC (GATE V): reported 24 `edge-bleed` blockers, **all attributable to the
  review cut's own burned-in timecode and beat labels**, which do not exist in the
  clean master. Verified by frame extraction from the master before acceptance.
- Publishing: not authorized — master held locally per toolkit doctrine

## Known deviation

The motion histogram is `illustrate: 10 / 12` (83%), against the ~40% cap in
`MOTION.md`. This is a consequence of building from stock registered scenes only
(`ClaudeComposerAsk`, `SlateCard`, `BarChart`, `OutroSeries`) so the reel rebuilds
on a clean install with no custom TSX. The result is legible but static.
Converting the excess to other motion languages requires authoring per-beat
Remotion scenes and is the first improvement if this becomes a series.

## Rebuild

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install

REEL=path/to/2026-08-04-nine-months-at-the-data-ceiling
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
./art run   "$REEL"     # review cut
./art final "$REEL"     # clean master
```

`beat_sheet.json` is the source of truth — one beat per moment, with narration,
visual intent, and shot instructions. Preserve it before experimenting; make a
copy or a branded variant rather than overwriting a finished plan. Audio is
free and local (Kokoro); no API key is required.

**Build note:** on Python 3.14 the toolkit's dependencies have no wheels — build
an isolated Python 3.11 environment first. Do not run two compiles against the
same reel concurrently; the second deletes the first's `media/_ext_*.mp4` temps
and the ffmpeg concat fails half-written.

## Fact-check prompt

Run this after editing the narration:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and
> methodological claim — accuracies, AUCs, parameter counts, sample counts, file
> counts, sensitivity and specificity. Check each against `SOURCES.md` and the
> named primary artifact. Produce a table with beat ID, claim, verdict
> (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required
> correction. Pay specific attention to any claim about dates in 2026-W20 →
> W24, whose original timestamps did not survive a disk carve and must not be
> asserted. Do not silently repair the script: list every proposed change for
> human review.

## Files

| File | |
|---|---|
| `beat_sheet.json` | the source of truth — 12 beats, metadata, shot specs |
| `NARRATION.md` | the narration as plain prose, for reading aloud at GATE P |
| `PEDAGOGY.md` | signed GATE P, act structure, evidence table, friction protected |
| `SOURCES.md` | every claim → its artifact, and what is deliberately not claimed |
| `BUILD-LOG.md` | what was run, what failed, what was overridden |

Audio and video masters are not committed — `.gitignore` excludes `*.mp3` and
`*.mp4` and the toolkit holds masters locally until a human authorizes release.
