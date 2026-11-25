# Gradient Descent, One Step at a Time — one update rule, worked and broken on real numbers

**Week:** 15–21 Nov 2026 (Drive Week 4) · logged 2026-11-22

**Project:** STEM AI explainer series

**Toolkit:** brutalist.art

- **Drive:** https://drive.google.com/drive/folders/1zudlUZG4n6vUShgp1M1VU1pwPly0YjMR
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `exports/landscape/claude-liam-gradient-descent.mp4` (16:9, 3840×2160, 24 fps, 3:12)
- **Next film:** [Backpropagation, One Error at a Time](../2026-11-20-backpropagation/)

## What this film is for

The first film of the STEM series. The cold-open ask: how does a neural network actually learn? Skip the hype; show the one rule underneath, with real numbers. The film shows the update rule, works it on θ², shows two ways it fails (too big a step, a local minimum), and how it scales (backpropagation, mini-batches). It ends with a prompt the viewer pastes into Claude and a 3-point rubric.

## What was built

| Part | What it does |
|---|---|
| `SCRIPT.md`, `beat_sheet.json` (from `make_sheet.py`) | 11 beats of narration and shot cues. Approved at GATE P; one BVDT line added after it. |
| `BUILD-PROMPT.md` | A paste-in prompt that rebuilds the film end to end on this Windows machine with free tools only (Kokoro, Manim, Remotion). It never publishes. |
| `demo/gd_demo.py` | Pure Python + numpy, seed 7. Asserts the closed form θₜ = 3·0.8ᵗ at every step. Writes `demo/evidence.json` and `demo/RUN-LOG.txt`. |
| Audio (`mp3/`) | Kokoro `am_onyx`, 11 beats, 3:12. "eta" pinned to /ˈeɪtə/. `align.py` aligned 11/11 beats with no fallback into `mp3/words.json`. |
| `B02_Landscape` | The bowl L = θ², a ball at θ = 3, the tangent (the slope) and a step arrow. |
| `B03_UpdateRule` | The typeset rule with a box spotlight and a label for each symbol. |
| `B04_FiveSteps` | Ball steps plus a table of executed values: θ 3 → 0.983, loss 9 → 0.9664. |
| `B05_StepSize` | Three bowls side by side: θ₁₀ = 2.4512 / 0.3221 / 18.5752 for η = 0.01 / 0.1 / 1.1. |
| `B06_TwoValleys` | L = θ⁴ − 3θ² + θ. From θ = 2 the ball stops at 1.1309 (loss −1.0702); from −2 it reaches −1.3008 (loss −3.5139). The scene asserts its path matches the evidence. |
| `B07_Batches` | Contour map over (w, b): full batch vs 8 of 200 points per step, MSE 0.15 vs 0.1533. |
| Remotion bookends | `ClaudeComposerAsk` (B00 ask, BHTF Your Turn), `BrutalistHesitantWriter` (B01), `ClaudeVerdictArtifact` (BVDT), `ClaudeTitleOutro` (BOUT, locked). |

## Results

| Measure | Value |
|---|---|
| Master | 3840×2160, 24 fps, yuv420p, h264 + aac, 1 audio stream, 192.500 s (3:12) — `master_check` PASS |
| GATE V | 22 frames, 0 BLOCKER, 0 MAJOR |
| GATE T | PASS, 11 beats, 0 FAILs; one §8.10 advisory: BVDT narration recites the card (0.90) |
| Layout audit | 18 snapshots, 0 errors, 0 warnings |
| `bookend_check` / `beat_lint` | PASS / clean |
| Scene timing | Each Manim scene within ±3% of its audio |
| No-label / bottom-strip check | PASS: 96 frames sampled every 2 s, no review label or bottom strip (`check_no_labels.py`, run 2026-11-24 on the delivered master) |
| Loudness | PASS — −24.70 LUFS integrated (window −28 to −18), −2.96 dBTP true peak (ceiling −1.0) |
| Slots | 11/11 filled: 6 Manim, 5 Remotion |
| Proof gate (`CHECKS-REPORT.md`) | 9 SHOW, 2 CARD; framework, worked example, falsifiability, scaffolded task, bookends, no-source-no-verdict all ✓ |
| Exit codes | `./art run` exit 0; `./art final --out exports/landscape` exit 0 |
| Clock check | Skipped by `master_check`: `clock_check.py` not found in the toolkit |

## Problems found by running it

1. **Kokoro phonemized "eta" as /ˈiːɾə/ and whisper heard "either"** → pinned to /ˈeɪtə/ via `metadata.pronounce`; B03 regenerated. Every other whisper difference was digit normalization, not a mispronunciation.
1. **Manim renders ceil(run_time·fps) frames** → the clock counts whole frames; each scene lands within ±3% of its audio.
1. **GATE A** → stub-safe points and an isolated-copy data fallback; B03's arrow centres made explicit.
1. **GATE A (**`run.sh`**): a docstring containing a fake class line was picked up as a scene** → the docstring was removed.
1. **GATE B: B02's "setting θ" label sat below the safe area** → moved up.
1. **GATE V underfill** → B01 at type 160 with spacing 3.1; B03's equation at 132 pt with labels spread; BVDT from five to six lines.
1. **Hand QC: an underlined "−" read as "=", and an underlined "=" read as "≡"** → B03's spotlight changed from an underline to a box with a minimum height.
1. **Hand QC (frames at 15/50/85% of every beat)** → B02 labels de-collided, B04 table columns widened, B05's runaway arrow redirected, B06/B07 draw from t = 0 so no beat opens empty.

## Evidence

- `FACTCHECK.md` — 17 claims: 14 ✓ (6 of them executed), 2 CORRECTED (#2 "millions of times", #14 "this same rule"), 1 minor (#16 the 1/25 cost ignores fixed overhead). Script hash `b9bb39a3…4b15`, evidence hash `219f97b3…5d052`.
- `SOURCES.md` — Cauchy (1847); Goodfellow, Bengio & Courville, *Deep Learning* §4.3 and §8.1.3; Rumelhart, Hinton & Williams (1986).
- `demo/gd_demo.py`, `demo/evidence.json`, `demo/RUN-LOG.txt` — Python 3.12.13, numpy 2.5.5, Windows 11, seed 7.
- `exports/landscape/claude-liam-gradient-descent.verified.json` — status `ready`, sha256 `7000bed2b3849c51d3e0410d58f47dd43437524056d369e4fe6609b9c201474f`, matching the master.
- `CHECKS-REPORT.md`, `TYPECHECK.md`, `_qc/REPORT.md`, `_qc/sheet_1-3.png`, `layout_audit.md`, `MASTERCHECK.md`, `LOUDNESS.md`, `final.log`, `BUILD-PROMPT.md`.
- Drive week folder: https://drive.google.com/drive/folders/1zudlUZG4n6vUShgp1M1VU1pwPly0YjMR — holds the labelled review cut `claude-liam-gradient-descent-slate.mp4` (Drive copy to be replaced with the clean master).
