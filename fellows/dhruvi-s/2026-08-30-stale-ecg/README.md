# A Stale ECG Is Worse Than No ECG

**Fellow:** Dhruvi Shah
**Date:** 2026-08-30
**Topic:** Clinical ML · evidence decay
**Format:** CLI explainer (Claude skin) + 9:16 short
**Runtime:** ~3:16 master (12 beats) · ~2:42 short (8 beats)
**Narrator:** Kokoro `af_bella` (Bella) — HAI persona default
**Register:** Pragmatist · **Channel:** @HumanitariansAI

## What this video is about

Adding a routine ECG to an in-hospital mortality model moves AUROC from 0.8574
to 0.8595 across 144,668 cardiac admissions in MIMIC-IV. That +0.0021 looks like
nothing — and it hides a sign change.

Split the admissions by how old the ECG was at admission and the aggregate comes
apart: a same-day ECG helps (+0.0046), while an ECG more than a year old makes
the model **worse than leaving the ECG out entirely** (-0.0048). The
fresh-minus-stale contrast is +0.0092 (95% CI 0.0057–0.0126, bootstrap
p < 0.001) and a slope of -0.0033 AUROC per decade of days. The contrast stays
positive in 5 of 5 fold seeds, though its magnitude varies (+0.0061 to +0.0094)
— the sign is what replicates, not the size.

Because same-day-ECG patients are being actively worked up, the bin comparison is
confounded by case mix. The within-patient design removes it: hold rows, labels
and EHR features fixed, and feed the same admissions progressively older ECGs
from the same patient. The harm survives (+0.0056 at median age 0.2 days,
-0.0051 at 508 days).

The mechanism is a train/deploy mismatch — the model learned to trust the ECG
because training ECGs were mostly fresh. The obvious fixes (age-as-a-feature,
matching the training age distribution) are reported as **negative results**:
both straddle zero.

**The one thing:** a model that consumes "whatever is on file" inherits the age
of that file, and age is not in the feature vector.

## Package contents (fellows checklist)

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth), 12 beats |
| `short/beat_sheet.json` | 9:16 companion plan, 8 beats |
| `README.md` | This file |
| `SOURCES.md` | Per-figure provenance — every on-screen number traced to a file |
| `PEDAGOGY.md` | GATE P — what each beat teaches and why it sits where it sits |
| `FACTCHECK.md` | Claim-level verdicts |
| `NARRATION-GATE-P.md` | Line-by-line house-narration review sheet |
| `CHECKS-REPORT.md` | PROOF GATE — 11 SHOW / 0 justified-HOLD / 1 CARD / 0 PUNT |
| `BUILD-LOG.md` | Build record |
| `mp3/timings.json` | Measured narration clock (master) |
| `short/mp3/timings.json` | Measured narration clock (short) |
| `BUILD-PROMPT.md` | Reproducible rebuild instructions |
| `description.txt` | YouTube description + chapter markers |
| `stale-ecg.srt` | Master captions |
| `short/stale-ecg-short.srt` | Short captions |

### Not in this folder

Rendered masters and generated assets are gitignored and stay local:
`stale-ecg.mp4`, `stale-ecg-slate.mp4`, `short/stale-ecg-short.mp4`,
`qc-sheet.png`, the per-beat `mp3/beat-*.mp3` renders, and the
`_qc/ clips/ images/ manim/ media/ mp4/ pantry/` directories. Only
`mp3/timings.json` is kept, as the measured narration clock.

**Master + short (Google Drive):** https://drive.google.com/drive/folders/15UD3wZW9K8EA5MH55d8nhEr_IYj_WSlQ?usp=sharing

## Source analysis

Code, data pipeline and full write-up: `mimic-research` (Dhruvi Shah).
`PAPER.md` has methods, tests and limitations; `ANALYSIS.md` is the
plain-language version. All figures are rebuilt as native animation from
`results/results.json` and `results/within_patient.json` per REBUILD LAW — no
screenshots.

## Data use

MIMIC-IV and MIMIC-IV-ECG are credentialed PhysioNet resources under a Data Use
Agreement. Only aggregate results appear on screen. No patient-level data, no
row-level records, no identifiers.

## Limitations

Report and measurements, not waveform — a waveform model would likely find more,
so these numbers bound ECG value from below. Absolute effects are small
(~0.005–0.010 AUROC); the sign change is the finding, not the magnitude. Single
centre, retrospective (BIDMC), so association rather than cause. The
within-patient design removes case mix but not unmeasured time-varying
confounding. Admissions with no pre-admission ECG (23.5%) are excluded
throughout, and that exclusion is not random.

Not medical advice. This is a video about model evaluation.

## Toolkit (rebuild)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Repo: https://github.com/nikbearbrown/brutalist.art

Audio-first, Kokoro-only on house beats, no API keys. Full rebuild path is in
`BUILD-PROMPT.md`.

## Publishing

Not authorized by this package. Masters stay local until a human decides to
share or upload.
