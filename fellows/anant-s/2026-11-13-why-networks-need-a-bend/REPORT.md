# Why Neural Networks Need a Bend — a 4:12 explainer on why stacked straight layers collapse into one

**Week:** 8–14 Nov (Drive Week 3) · logged 2026-11-23

**Project:** STEM AI explainer series

**Toolkit:** brutalist.art

- **Drive:** https://drive.google.com/drive/folders/1SlLqr6rzO6sGKukxhy-S5gk-9tCDSl9a
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `exports/landscape/claude-liam-nonlinearity.mp4` (16:9, 3840×2160, 24 fps, 4:12)

## What this film is for

It answers one ask: why does every neural network put a bend between its layers, and wouldn't more straight layers be enough? The film shows, with executed numbers, that straight layers collapse into one matrix, that no line separates XOR, and that one ReLU bend solves it. It then shows the limits: the bend makes a solution possible, not easy to find, and a ReLU network is made of straight pieces.

## What was built

| Part | What it does |
|---|---|
| Script / narration | 14 beats, 840 words, in `SCRIPT.md` (generated from `beat_sheet.json` by `make_sheet.py`). Kokoro `am_onyx`; ReLU, XOR, numpy and Jambo pinned in IPA in `metadata.pronounce`. Measured audio 251.7 s after padding. |
| Evidence demo | `demo/nonlinearity_demo.py` (pure Python + numpy, about 60 s) writes `demo/evidence.json` and `demo/RUN-LOG.txt`. It asserts the collapse is identical, the ten-layer and bias gaps are below 10⁻¹², the best line gets exactly 3 of 4, no deep-linear seed reaches 4 of 4, the hand-set ReLU net outputs (0, 1, 1, 0), and the diagonal trace matches its closed form. |
| Remotion bookends | B00 `ClaudeComposerAsk` (cold open), B01 `BrutalistHesitantWriter` (summary), BVDT `ClaudeVerdictArtifact` (recap), BHTF `ClaudeComposerAsk` (Your Turn), BOUT `ClaudeTitleOutro`. |
| `B02_TwoMoves` | A grid through a matrix stays straight; through ReLU it creases; "bend" boxed. |
| `B03_Collapse` | Seeded matrices W₁, W₂ and x = (−1, 2); both paths give (7, 8); box on "=". |
| `B04_TenLayers` | 1,000 points through ten layers vs one multiplied-out matrix; largest gap 8.88×10⁻¹⁵; bias identity. |
| `B05_NoLine` | XOR square, line sweep over 115,560 lines, best 3 of 4, four-inequality proof. |
| `B06_StuckAtHalf` | Two-layer net with no bend: loss flattens at 0.25, every output 0.5, same as the best line. |
| `B07_ReluFix` | Hand-set ReLU net (Goodfellow, Bengio & Courville 2016, §6.1), row-by-row table, output 0, 1, 1, 0. |
| `B08_Fold` | The four points on one line, the ReLU fold, a separating line, the band in input space. |
| `B09_HundredSeeds` | Two 10×10 seed grids: 18/100 with two units, 91/100 with eight; dead-unit inset. |
| `B10_StraightAgain` | Diagonal trace with two kinks, continued straight to (3, 3) → −4. |
| Master | `exports/landscape/claude-liam-nonlinearity.mp4`; 14/14 slots filled (9 Manim, 5 Remotion). |

## Results

| Measure | Value |
|---|---|
| Build chain | `./art run` exit 0 · `./art final` exit 0 |
| GATE V | 28 frames · BLOCKER 0 · MAJOR 0 |
| GATE T | PASS · 14 beats · 0 FAILs; one advisory: §8.10 BVDT narration recites the card (0.94) |
| Scene gates (A / W / B) | 0 / 0 / 0 for all nine Manim scenes |
| Bookend check | `bookend_check` PASS (planning session, `CHECKS-REPORT.md`) |
| Strip check (label corner + full bottom band) | PASS on 126 samples, background-relative version (`BUILD-LOG.md`). The copy in `final.log` is the earlier absolute-darkness run, which flagged the dark-polarity outro at t = 248 s and 250 s (`labels_rc=2`). |
| Master check | PASS · 3840×2160 · 24 fps · yuv420p · h264 · 251.9 s; the duration clock check was skipped (`clock_check.py` not found) |
| Loudness | PASS · −24.67 LUFS integrated · −2.98 dBTP true peak (window −28 to −18 LUFS, ceiling −1.0 dBTP) |
| Preview length vs audio | −0.2% to +1.2% per scene (B02 −0.2%, B10 +1.2%) |
| Word clock | `align.py` aligned 14/14 beats, 0 fallback |
| Length | 4:12 |

## Problems found by running it

1. **B07 matrices bled off the right edge** in the preview frames — shrunk and moved.
1. **B02, B07 and B09 underfilled at the 50% frame** — B02 draws the ReLU axes from t = 0.2, B07 shows the x column early, B09 ghosts the 8-unit grid and uses a callout card.
1. **B08 band contrast was too low** — raised to SOFT at 50%.
1. **B06 per-bar values collided** — replaced with one label, "each 0.5".
1. **B10 piece equations were struck through by the t-axis** — moved to the lower left. Several overruns were also tightened.
1. **B02's strip landed 0.19 s after "A network alternates"** — within tolerance, but I asked for the bottom strip to go. It was removed and "bend" in the ReLU header is boxed in ink; the re-check gave A=0, W=0, B=0, 19.12 s against 19.16 s of audio (−0.2%), and GATE V 0 BLOCKER, 0 MAJOR.
1. **The absolute-darkness strip check falsely flagged the dark-polarity outro** — the background-relative check passed on 126 samples.
1. **B03 "x" looked garbled at 85% in hand QC** — a mid-Write frame; it settles correctly, so no change was made.

## Evidence

- `FACTCHECK.md` — 31 claims; 4 corrected from the draft (#2, #3, #23, #28) and the B00 result line qualified (#29); algebra checks by hand.
- `SOURCES.md` — Goodfellow, Bengio & Courville (2016) §6.1; Minsky & Papert (1969); Nair & Hinton (2010); Glorot, Bordes & Bengio (2011); Saxe, McClelland & Ganguli (2014); Montúfar et al. (2014); Arora et al. (2018); seeds.
- `demo/nonlinearity_demo.py`, `demo/evidence.json`, `demo/RUN-LOG.txt` — Python 3.12.13, numpy 2.5.5, Windows 11.
- `exports/landscape/claude-liam-nonlinearity.verified.json` — status `ready`, sha256 `e0a001d96cbb9cf1ecb8eb2d9b6edf5f46aeb0659e48f5f6a9c5ed473332e019`, 251.92 s.
- `CHECKS-REPORT.md`, `TYPECHECK.md`, `_qc/REPORT.md`, `MASTERCHECK.md`, `LOUDNESS.md`, `final.log`, `BUILD-LOG.md`.
- Drive week folder: https://drive.google.com/drive/folders/1SlLqr6rzO6sGKukxhy-S5gk-9tCDSl9a (Drive copy to be replaced with the clean master)
