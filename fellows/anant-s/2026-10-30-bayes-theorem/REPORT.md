# Bayes' Theorem: The Positive That's Usually Wrong — what a positive test means, counted out on 10,000 people

**Week:** 25–31 Oct (Drive Week 1) · logged 2026-11-24

**Project:** STEM AI explainer series

**Toolkit:** brutalist.art

- **Drive:** https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `tldr-bayes-theorem.mp4` (16:9, 3:43)

## What this film is for

The cold open asks: a test that catches 99% of cases says I am positive — how likely is it that I am sick? The answer is about 1 in 6, not 99%. The film counts it out on 10,000 people (1% sick, 99% sensitivity, 5% false alarms), shows why the 99% answers a different question, builds Bayes' theorem from the counts, and ends on the base rate: same test, rarer disease, a much weaker positive.

## What was built

| Part | What it does |
|---|---|
| Script and narration | 15 beats in `beat_sheet.json` (via `make_sheet.py`), Kokoro `am_onyx`, $0. Whisper diff on every beat; `align.py` wrote `mp3/words.json`. |
| B00 `ClaudeComposerAsk` | Cold open: "Hello, Liam", the ask types in, three answer lines (about 1 in 6; sensitivity 99 of 100 sick; base rate 1 in 100). |
| B01 `BrutalistHesitantWriter` | "means you're probably sick" corrected to "can still be a false alarm"; fontSize 160, lineSpacing 3.3, lead 0.8 s. |
| `B10_YouArePositive` | The "you" square, a POSITIVE stamp, P(sick) = ? |
| `B11_TenThousand` | A 10,000-square grid counts up; the scan over the 100 sick catches 99. |
| `B12_FalseAlarms` | The scan over the 9,900 healthy; 495 stay lit. |
| `B13_WrongCrowd` | A box round the sick block, 99/100; the 495 outside pulse. |
| `B14_OnlyThePositives` | The 594 positives regroup; predict hold. |
| `B15_OneInSix` | The squares morph into 99/594, then 1/6. |
| `B16_BuildBayes` | Counts → probabilities → Bayes' theorem (MathTex, staged). |
| `B17_ReadTheLine` | The equation read piece by piece with a box spotlight; the bar has a direction. |
| `B18_BackToYou` | B10's "you" square returns into the block; 1/100 → 1/6. |
| `B19_BaseRateDial` | A base-rate curve with a sweeping marker: 1/1,000 → about 2%, 1/10 → about 69%, 1/2 → 95%. |
| Remotion bookends | BVDT `ClaudeVerdictArtifact` (4 lines), BHTF `ClaudeComposerAsk` ("Test Positive Twice", prompt plus three checks), BOUT `ClaudeTitleOutro`. |
| Evidence demo | `demo/bayes_demo.py` (standard library, exact `Fraction` counts, seeded simulation) writes `demo/evidence.json` and `demo/RUN-LOG.txt`; `make_sheet.py` asserts every spoken number against it. |

## Results

| Measure | Value |
|---|---|
| Master | 3840×2160, 24 fps, h264, yuv420p, 223.7 s (3:43) — MASTERCHECK PASS |
| Slots | 15/15 filled: 10 Manim, 5 Remotion/bookend video |
| GATE V | 30 frames, BLOCKER 0, MAJOR 0 |
| GATE T | PASS, 15 beats, 0 FAILs; one §8.10 advisory (BVDT narration recites the card, 0.86) |
| Bookend check | PASS |
| Label / bottom-strip check | PASS — 112 frames sampled every 2.0 s; label corner and bottom band max off-background 0.000, 0 hits |
| Loudness | PASS — −24.61 LUFS integrated (window −28 to −18), true peak −3.06 dBTP (ceiling −1.0); every narration beat has audio |
| Hand QC | All 15 beats checked; clean |
| Evidence run | All assertions passed; 100,000-person simulation gives P(D\ |
| Checksum | sha256 `c01206b09541201…` matches `.verified.json` (`ready`) |

## Problems found by running it

1. **A 1,000-person grid gives 9.9 and 49.5 people.** The demo asserts whole counts. → The population became 10,000, drawn as a 125 × 80 grid.
1. **Whisper heard "sick" right after a number as "six"** (B15 "Ninety-nine sick." → "996"; B13 → "106"), and B17's "…zero five nine four: one sixth" ran together. → B13 "who are sick", B15 "have the disease", B17 colon → full stop. Each beat was regenerated and re-aligned.
1. **At 480p the 100 sick, drawn as one row, read as a hairline.** → A 10 × 10 block; the B13 line "for this row" became "for this block".
1. **The 10,000-mark grid at DIM #8B8F96 measured 0.277 luminance separation,** below GATE V's 0.30. → DIM #7A7E86, and cleared negatives a lighter CLEAR #E6E2D8 so the 495 lit marks read.
1. **Frame and gate fixes in the previews:** the B17 equation clipped at the left edge (new layout), the B19 y-axis drawn on the right (x = log₁₀ + 3), stub-unsafe code (GATE A), and counters outside ±6.0 (GATE B).
1. **Two cues ran 0.11 s late** (B14, B18). → Their opening moves were shortened from 0.8 to 0.65 s.
1. **B12 rendered blank from about 45% to the end, though every gate passed** (V, T, strip 133/133, master, loudness). `play()` put the cleared rows on top of the draw order, hiding the sick block, the "you" badge, the scan bar and all 495 false-alarm marks. → `set_z_index(1)` on those before the sweep; stale clips moved to `_superseded/`; full queue re-run.
1. **After the ai-explainer conversion, B01 measured 49% fill at fontSize 145.** → Re-rendered at fontSize 160 (59%). The 145 clip is in `_superseded/b01_underfill/`.

## Evidence

- `FACTCHECK.md` — 29 claims; draft claims corrected at #1–#3 and #5 (e.g. "99%-accurate" → "catches 99% of cases"; overall accuracy is 95.04%).
- `SOURCES.md` — 7 references, including Bayes and Price (1763), Altman and Bland (1994) and Gigerenzer and Hoffrage (1995).
- `demo/bayes_demo.py`, `demo/evidence.json`, `demo/RUN-LOG.txt` — script sha256 `9d72b9a1…`, evidence sha256 `6bcda52e…`; ends "all assertions passed".
- `exports/landscape/tldr-bayes-theorem.verified.json` — sha256 of the master and of every input clip and mp3.
- `final.log`, `TYPECHECK.md`, `LOUDNESS.md`, `MASTERCHECK.md`, `_qc/` (contact sheets and final frames).
- `_superseded/B12_hidden_marks.mp4`, `_superseded/B12_manim_hidden_marks.mp4` — the blank B12 clips.
- `_superseded/format-tldr/` — the retired TL;DR B00–B03.
- Drive: https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE (Drive copy to be replaced with the clean master)
