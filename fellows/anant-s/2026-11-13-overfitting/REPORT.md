# Overfitting, When a Perfect Score Lies — a 3:19 explainer on training error, test error and the U

**Week:** 8–14 Nov (Drive Week 3) · logged 2026-11-23

**Project:** STEM AI explainer series

**Toolkit:** brutalist.art

- **Drive:** https://drive.google.com/drive/folders/1SlLqr6rzO6sGKukxhy-S5gk-9tCDSl9a
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `exports/landscape/claude-liam-overfitting.mp4` (16:9, 3840×2160, 24 fps, 3:19)

## What this film is for

It answers one ask: my model scored zero error on its training data, so should I trust it? The film sets up a hidden curve, 16 noisy training points and 1,000 locked test points, defines the grade (MSE), and fits three models. It sweeps degrees 0 to 15 to show the U of overfitting, then bends two simple stories: complexity alone is not the problem, and a score used to choose the model is no longer an honest score.

## What was built

| Part | What it does |
|---|---|
| Script / narration | 11 beats, 677 words, in `SCRIPT.md` (generated from `beat_sheet.json` by `make_sheet.py`, which asserts every spoken figure against `evidence.json` and the length budget). Kokoro `am_onyx`; "Namaste" pinned to /nˈʌməstˌeɪ/. Audio 198.5 s after padding. |
| Evidence demo | `demo/overfit_demo.py` (pure Python + numpy, about 7 s) writes `demo/evidence.json` and `demo/RUN-LOG.txt`. Extended after GATE P with `more_data[*].curve`, `pool_preview`, `selection.grid100_peek` and `grid100_untouched`; existing values byte-for-byte unchanged (key-by-key diff). |
| Remotion bookends | B00 `ClaudeComposerAsk` (cold open), B01 `BrutalistHesitantWriter` (summary), BVDT `ClaudeVerdictArtifact` (recap), BHTF `ClaudeComposerAsk` (Your Turn), BOUT `ClaudeTitleOutro`. |
| `B02_Setup` | Hidden curve sin(πx), 16 dots knocked off by noise, a locked test box of 1,000 points. |
| `B03_ErrorMeasure` | Typeset MSE with box spotlights; worked term: gap −1.032, squared 1.065; 4.546 ÷ 16 = 0.284. |
| `B04_ThreeFits` | Degree 1, 3 and 15 side by side with executed train/test counters; test counter to 9,882.6. |
| `B05_TheU` | Train and test error across degrees 0–15, noise floor at 0.040, minimum at degree 5 (0.0466), exit chips. |
| `B06_MoreData` | Degree-15 refit as n grows: test 28.776 at 20 points, 0.0476 at 100, 0.0413 at 1,000. |
| `B07_PeekedScore` | Trial grids: choose and report on validation 69.6% optimistic vs untouched test 55.2%; control 53.3%. |
| Master | `exports/landscape/claude-liam-overfitting.mp4`; 11/11 slots filled (6 Manim, 5 Remotion). |

## Results

| Measure | Value |
|---|---|
| Build chain | `./art run` exit 0 · `./art final` exit 0 |
| GATE V | 22 frames · BLOCKER 0 · MAJOR 0 |
| GATE T | PASS · 11 beats · 0 FAILs; one advisory: §8.10 BVDT narration recites the card (0.91) |
| Scene gates (A / W / B) | 0 / 0 / 0 (CLEAN) for all six Manim scenes |
| Bookend check | `bookend_check` PASS (planning session, `CHECKS-REPORT.md`) |
| Strip check (label corner + full bottom band) | PASS · 99 frames sampled every 2.0 s · max off-background fraction 0.000, 0 hits in both regions (`labels_rc=0`) |
| Master check | PASS · 3840×2160 · 24 fps · yuv420p · h264 · 198.8 s; the duration clock check was skipped (`clock_check.py` not found) |
| Loudness | PASS · −24.69 LUFS integrated · −2.93 dBTP true peak (window −28 to −18 LUFS, ceiling −1.0 dBTP) |
| Preview length vs audio | +0.31% to +1.06% per scene, all within ±3% |
| Word clock | `align.py` aligned 11/11 beats, 0 fallbacks |
| Length | 3:19 |

## Problems found by running it

1. **The evidence lacked data for two scenes** — `evidence.json` had the degree-15 curve only for n = 16 and n = 200, and no per-trial outcomes for the B07 grids. The demo was extended before audio instead of refitting inside the scene; 68 of the first 100 trials are optimistic under peek and 59 untouched.
1. **B03 worked term ran off the right edge** and collided with its label — restacked and centred; the equation went from 104 to 92 pt to sit inside ±6.0; spotlight padding went from 0.08 to 0.2 per side because the stroke sat on the "−"; signed numbers were braced so LaTeX does not space the minus as a binary operator.
1. **B05 layout** — the monospace exit-value line ran off-frame (now serif); the "Lowest test error" label crossed the training line (now "best: degrees 3 to 6", moved); two run times were trimmed because the clock ran 0.1–0.3 s late.
1. **B06 monospace table columns collided** — now a serif table with wider columns and a narrower plot.
1. **B07** — grid titles overlapped (shortened); the opening was underfilled (the split strip now starts large mid-frame and parks at the top); grids enlarged and spread.
1. **B02 opening underfilled at about 47%** — the plot starts full-width and shrinks left when the test set arrives; "locked away" leaves before "grade on these" lands.
1. **Terracotta text and arrow tips read 2.74:1 on cream under GATE T §8.3** — terracotta moved to non-text shapes only: the B02 test-set box outline, B03 spotlight boxes, a box around the B04 9,882.6 counter, the B05 test dots and curve, the B06 meeting ring, the B07 optimistic cells.
1. **B07's right grid was empty at the 50% frame** — both grids now appear as ghost outlines when the grid stage opens.
1. **The first B04 re-render was killed externally (exit 143)** — re-run clean.
1. **GATE T §8.1 failed on B03: smallest text run 38 px < 41 px** — the 38 px run was the hat accent on f̂. Enlarging the formula pushed it past title-safe, and a tighter spotlight box fused with the glyphs. Fix: the prediction is written f(xᵢ) without the hat, the worked-term line went from 48 to 60, and the formula keeps 92 pt. The 4K midpoint measured 56 px (PASS).
1. **GATE T §8.3 then flagged the wide terracotta spotlight box** at the midpoint — the moving spotlight is now ink, and terracotta is only on the final "MSE = 0" box. The 4K midpoint test passed at 56 px and 10.04:1 contrast.
1. **Hand QC: the B03 spotlight box on "MSE" overlapped the "="** — tightened to pad 0.16; the settled frame was verified clean.

## Evidence

- `FACTCHECK.md` — 22 claims; 3 corrected from the draft (#1 "usually means" → "can mean"; #20 the "four times in ten" statistic dropped; #22 "zero" → "essentially zero"); algebra checks.
- `SOURCES.md` — Hastie, Tibshirani & Friedman, *ESL* (2009) §2.4, §7.2–7.3, §7.10; James et al., *ISL* §2.2; Bishop, *PRML* (2006) §1.1; Cawley & Talbot (2010), *JMLR* 11; Belkin et al. (2019), *PNAS* 116(32); seeds.
- `demo/overfit_demo.py`, `demo/evidence.json`, `demo/RUN-LOG.txt` — Python 3.12.13, numpy 2.5.5, Windows 11. Hashes after the extension (`BUILD-LOG.md`): script `4cb1d91f…f9d5`, evidence `988d991c…381c`; `FACTCHECK.md` and `SOURCES.md` list the earlier hashes.
- `exports/landscape/claude-liam-overfitting.verified.json` — status `ready`, sha256 `254049bbf9e9b97acd7e6807f6b443556fc070beb147077581343bf523696db0`, 198.75 s.
- `CHECKS-REPORT.md`, `TYPECHECK.md`, `_qc/REPORT.md`, `MASTERCHECK.md`, `LOUDNESS.md`, `final.log`, `BUILD-LOG.md`.
- Drive week folder: https://drive.google.com/drive/folders/1SlLqr6rzO6sGKukxhy-S5gk-9tCDSl9a (Drive copy to be replaced with the clean master)
