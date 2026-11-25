# Hedging When Trading Isn't Free — Boopesh M.

STEM explainer: "Deep Hedging" (Buehler, Gonon, Teichmann & Wood, *Quantitative Finance* 19(8), 2019,
DOI 10.1080/14697688.2019.1571683, arXiv:1802.03042), with a small replication of my own.

## This week's contribution
- **Question:** if every trade costs a fee, can a learned hedge beat the textbook Black–Scholes delta hedge?
- **Prediction:** the learned hedge trades less and keeps more money, and with zero fees it should match Black–Scholes.
- **What I built:** `code/deep_hedge.py` (Black–Scholes world, short ATM call, 0.5 % fee, small network trained on
  the entropic utility), a 16:9 explainer (2:33) and a native 9:16 Short (0:51) whose charts come from its outputs.
- **Observed result (40,000 test paths, 0.5 % fee):** average P&L −$1.11 (BS) → −$0.65 (deep); fees $1.11 → $0.65;
  shares traded 2.23 → 1.30; worst-5 % average −$2.56 → −$2.14; entropic utility −1.31 → −0.92. But the spread is
  wider ($0.57 → $0.75). With zero fee the network is close to BS (0.024-share average gap), slightly worse in utility.
- **Next experiment:** double the fee to 1 % (the B80 prompt) and try a Heston simulator.

## Human and AI work
- **My decisions, implementation and verification:** chose the paper and the replication setup, the voice
  (`am_onyx`, approved); reviews the numbers and the paper-only claims.
- **AI tools/voices used and what they generated:** Claude (Claude Code) ported the script to numpy with a gradient
  check, ran it, drafted script, beat sheets and Manim scenes, rendered and checked frames. Kokoro `am_onyx` speaks
  the narration (disclosed on screen and in the audio).
- **What I rejected or corrected:** see [FRICTIONAL.md](FRICTIONAL.md).
- **What remains unverified or failed:** the paper PDF could not be opened (arXiv blocked); see ⚠️ rows in
  [FACTCHECK.md](FACTCHECK.md). PyTorch run not done (numpy port used). Pronunciation needs a human listen.

## Files
| File | What it is |
|---|---|
| `code/deep_hedge.py` | the experiment (numpy, seed 7); writes `results.json`, `arrays.npz`; `run.log` is the run |
| `code/typeset.py` | equations → SVG via matplotlib MathText |
| `beat_sheet.json` / `make_sheet.py` | the 16:9 film as code |
| `scenes.py` | Manim scenes (read the experiment outputs directly) |
| `short/` | native 9:16 Short: own beat sheet, scenes, paperwork |
| `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `PROOF.md`, `FRICTIONAL.md`, `description.txt` | paperwork |

## Reproduce
- **Brutalist commit:** `a99b5323`, checked 2026-10-24
  ```bash
  cd code && python deep_hedge.py && python typeset.py ../assets ../short/assets && cd ..
  python3 make_sheet.py
  python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <this folder>
  python3 <brutalist>/runtime/scripts/remotion_scenes.py <this folder> --only B00   # also B10, B80
  <brutalist>/art run <this folder>
  <brutalist>/art final <this folder> --height 2160
  # Short: same on short/ (remotion B00), final with --height 3840
  ```

## Watch and review
- Landscape Drive link (add) — 3840×2160 — 2:33 — SHA-256: c555305956a0fdca09a8cd465976e2dad8fb800d1d6555d1e8f1a5953c450ca7 (−14.2 LUFS; verified master e2efd5eb…b4676 with audio loudness-normalised, video stream copied)
- Vertical Drive link (add) — 2160×3840 — 0:51 — SHA-256: 193a2855eac6a85f50f828817aa8e44689beef8b1f7ddd3054f1a3703e9f14f7 (−14.2 LUFS; verified master a773b3e6…2203b with audio loudness-normalised, video stream copied)
- PM review status: pending
- Professors' publication decision: pending
