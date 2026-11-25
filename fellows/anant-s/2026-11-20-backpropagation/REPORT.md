# Backpropagation, One Error at a Time — the chain rule, run backward on real numbers

**Week:** 15–21 Nov 2026 (Drive Week 4) · logged 2026-11-22

**Project:** STEM AI explainer series

**Toolkit:** brutalist.art

- **Drive:** https://drive.google.com/drive/folders/1zudlUZG4n6vUShgp1M1VU1pwPly0YjMR
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `exports/landscape/claude-liam-backpropagation.mp4` (16:9, 3840×2160, 24 fps, 3:17)
- **Previous film:** [Gradient Descent, One Step at a Time](../2026-11-20-gradient-descent/)

## What this film is for

Film 1 named backpropagation in its scale beat; this film explains it. The cold-open ask: gradient descent needs a slope for every weight, so how does a network get all of them at once? The answer is shown on a two-weight network, with numbers from a script that was run, checked against finite differences, then pushed until it fails with ten sigmoid layers. It ends with a prompt the viewer pastes into Claude and a 3-point rubric.

## What was built

| Part | What it does |
|---|---|
| `SCRIPT.md`, `beat_sheet.json` (from `make_sheet.py`) | 11 beats of narration and shot cues. Approved at GATE P. |
| `demo/bp_demo.py` | Pure Python + numpy, deterministic. Writes `demo/evidence.json` and `demo/RUN-LOG.txt`. Asserts the chain-rule product equals dL/dw1 to 1e-12 and that finite differences agree. |
| Audio (`mp3/`) | Kokoro `am_onyx`, 11 beats. "tanh" pinned to /tæntʃ/, "backpropagation" to /bˌækpɹˌɑːpəɡˈeɪʃən/. Silences padded with `stem-films/tools/pad_silence.py`, then `align.py` for the word clock. |
| `B02_Chain` | The network as four steps in a row, each with a local-slope tag. |
| `B03_ChainRule` | ∂L/∂w₁ = ∂L/∂y · ∂y/∂h · ∂h/∂z · ∂z/∂w₁, each factor spotlit in a box. |
| `B04_Forward` | Forward pass with x = 1, t = 0.2, w₁ = 0.5, w₂ = 2: z 0.5, h 0.4621, y 0.9242, L 0.5245. |
| `B05_Backward` | Backward pass: 1.4485 × 2 × 0.7864 × 1 = 2.2783 for ∂L/∂w₁; ∂L/∂w₂ = 0.6694. One step at η = 0.1 takes the loss 0.5245 → 0.0983. |
| `B06_Check` | Central differences (ε = 1e-5) vs backprop: 2.27828974 both, \ |
| `B07_Vanishing` | Ten sigmoid layers (slope ≤ 0.25); the gradient reaching the first layer is 3.483e-07. |
| Remotion bookends | `ClaudeComposerAsk` (B00 ask, BHTF Your Turn), `BrutalistHesitantWriter` (B01), `ClaudeVerdictArtifact` (BVDT), `ClaudeTitleOutro` (BOUT, locked). |

## Results

| Measure | Value |
|---|---|
| Master | 3840×2160, 24 fps, yuv420p, h264, 1 audio stream, 196.833 s (3:17) — `master_check` PASS |
| GATE V | 22 frames, 0 BLOCKER, 0 MAJOR |
| GATE T | PASS, 11 beats, 0 FAILs; one §8.10 advisory: BVDT narration recites the card (0.91) |
| Gates A, W, B | Pass for all six Manim scenes |
| Layout audit | 28 snapshots, 0 errors, 0 warnings |
| `bookend_check` / `beat_lint` | PASS / clean |
| No-label strip check | PASS — 98 frames sampled every 2.0 s, max dark fraction in label zone 0.00 |
| Loudness | PASS — −24.63 LUFS integrated (window −28 to −18), −3.12 dBTP true peak (ceiling −1.0) |
| Slots | 11/11 filled: 6 Manim, 5 Remotion |
| Proof gate (`CHECKS-REPORT.md`) | 9 SHOW, 2 CARD; framework, worked example, falsifiability, scaffolded task, bookends, no-source-no-verdict all ✓ |
| Exit codes | `run_exit=0`, `final_exit=0`, `labels_rc=0` |
| Clock check | Skipped by `master_check`: `clock_check.py` not found in the toolkit |

## Problems found by running it

1. **Kokoro read "tanh" as "tan"** → pinned to /tæntʃ/ via `metadata.pronounce`.
1. **Whisper heard "backpropagation" as "back repugation"** → pinned to /bˌækpɹˌɑːpəɡˈeɪʃən/; the affected beats were regenerated.
1. **The toolkit ignores** `lead_silence_s`**/**`tail_silence_s` → `stem-films/tools/pad_silence.py` padded the audio directly (B01 +0.8 s lead, BVDT +0.5 s lead, BOUT +1.0 s tail), then `align.py` ran.
1. **GATE V underfill** → B01's on-screen correction shortened to "tests every weight" → "sends the error backward", at type 160 (narration unchanged); B02 ghosts its full layout from t = 0.2; B06 shows its cost-row labels early.
1. **GATE T §8.3 false positive: terracotta arrow tips in B05 read as low-contrast accent text** → the accent changed, not the gate. All arrows and labels are ink; terracotta stays only on box outlines (B04's loss, B05's ∂L/∂w₁), B02's frame, B03's brace and the filled bars in B06/B07.

## Evidence

- `FACTCHECK.md` — 13 claims: 11 ✓ (7 of them executed), 2 minor (#9 a backward pass is a small constant multiple of a forward pass; #12 vanishing gradients are "one reason" for ReLU). Algebra checks: 1.4485 × 2 × 0.7864 × 1 = 2.2783.
- `SOURCES.md` — Rumelhart, Hinton & Williams (1986); Goodfellow, Bengio & Courville, *Deep Learning* §6.5 and §8.2; Hochreiter (1991); Bengio, Simard & Frasconi (1994); Glorot, Bordes & Bengio (2011).
- `demo/bp_demo.py`, `demo/evidence.json`, `demo/RUN-LOG.txt` — Python 3.12.13, numpy 2.5.5, Windows 11.
- `exports/landscape/claude-liam-backpropagation.verified.json` — status `ready`, sha256 `89161db107f4db3aaf972e72bdfa3044b1317a082b431e6d64b1ac392766d860`, matching the master.
- `CHECKS-REPORT.md`, `TYPECHECK.md`, `_qc/REPORT.md`, `layout_audit.md`, `MASTERCHECK.md`, `LOUDNESS.md`, `final.log`.
- Drive week folder: https://drive.google.com/drive/folders/1zudlUZG4n6vUShgp1M1VU1pwPly0YjMR — holds the labelled review cut `claude-liam-backpropagation-slate.mp4` (Drive copy to be replaced with the clean master).
