# The 99.9% Accuracy Trap — Boopesh M.

AI-in-finance explainer: why a fraud model can be 99.9 % accurate and still useless, and what to measure instead
(recall, precision, and a cutoff chosen by the cost of each mistake). Real-data facts come from the widely used
Kaggle / ULB Machine Learning Group + Worldline credit-card dataset (492 frauds in 284,807 transactions); every model
number comes from my own small experiment on **synthetic** data with the same size and fraud rate.

## This week's contribution
- **Question:** if fraud is about 1 transaction in 580, what does "99.9 % accurate" actually tell you?
- **Prediction:** a do-nothing model will look almost as accurate as a real one, so accuracy can't separate them.
- **What I built:** `code/fraud_trap.py` (seed-locked synthetic data, 284,807 rows / 492 frauds; "always legit"
  baseline, logistic regression, small gradient-boosted model; precision–recall curves; threshold sweep; an
  illustrative cost rule), a 16:9 explainer (2:23) and a native 9:16 Short (0:53) whose charts come from its outputs.
- **Observed result (85,443 test transactions, 148 frauds):** "always legit" is 99.83 % accurate and catches 0.
  Logistic regression: 99.90 %, catches 66 (2 false alarms). Gradient boosting: 99.90 %, catches 127 (68 false
  alarms). Lowering the boosted model's cutoff from 0.9 to 0.01 raises catches 126 → 136 and false alarms 49 → 189.
  If a miss costs 50× a false alarm (assumption), the cheapest cutoff is 0.015 (136 caught, 173 false alarms).
- **Next experiment:** the B80 prompt (a 10:1 cost ratio), and the real Kaggle dataset when it is reachable.

## Human and AI work
- **My decisions, implementation and verification:** asked for "more AI in finance, not too advanced"; chose the
  voice (`am_onyx`, approved 2026-10-24); reviews the numbers, the synthetic-data framing and the ⚠️ claims.
- **AI tools/voices used and what they generated:** Claude (Claude Code) checked the dataset facts by search, wrote
  and ran the experiment, drafted script, beat sheets and Manim scenes, rendered and checked frames. Kokoro
  `am_onyx` speaks the narration (disclosed on screen and in the audio).
- **What I rejected or corrected:** see [FRICTIONAL.md](FRICTIONAL.md).
- **What remains unverified or failed:** the real dataset was not used (Kaggle blocked); the Kaggle→paper citation
  link and paper venue are from search results (⚠️ in [FACTCHECK.md](FACTCHECK.md)); the synthetic data's difficulty
  (`class_sep = 2.0`) was chosen by me; the 50:1 cost ratio is an assumption. Pronunciation needs a human listen.

## Files
| File | What it is |
|---|---|
| `code/fraud_trap.py` | the experiment (sklearn 1.9.1, seed 42); writes `results.json`, `curves.npz`; `run.log` is the run |
| `code/run_first_try_class_sep_1.0.log` | first, harder synthetic setting (kept for honesty) |
| `code/typeset.py` | the two formulas (recall, precision) → SVG via matplotlib MathText |
| `beat_sheet.json` / `make_sheet.py` | the 16:9 film as code |
| `scenes.py` | Manim scenes (read the experiment outputs directly) |
| `short/` | native 9:16 Short: own beat sheet, scenes, paperwork |
| `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `PROOF.md`, `FRICTIONAL.md`, `BUILD-LOG.md`, `description.txt` | paperwork |

## Reproduce
- **Brutalist commit:** `a99b5323`, checked 2026-11-01
  ```bash
  pip install scikit-learn   # 1.9.1 used
  cd code && python fraud_trap.py > run.log && python typeset.py ../assets ../short/assets && cd ..
  python3 make_sheet.py && (cd short && python3 make_sheet.py)
  python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <this folder>          # and short/
  python3 <brutalist>/runtime/scripts/remotion_scenes.py <this folder> --only B00    # also B10, B80; short: B00
  <brutalist>/art run <this folder>
  <brutalist>/art final <this folder> --height 2160
  # Short: same on short/, final with --height 3840
  ```

## Watch and review
- Landscape Drive link (add) — 3840×2160 — 2:23 — SHA-256: 4a34fe75a30bcb1cf43f1100d97bcebcd89bb92f5aff2602eda9c58b84b8a278 (−14.1 LUFS; verified master f3e7e564…b51e3ebe with audio loudness-normalised, video stream copied)
- Vertical Drive link (add) — 2160×3840 — 0:53 — SHA-256: 56893c18832918756b6f22cab189adbf7a8d4bfe1d3638a8422195226391beb2 (−14.2 LUFS; verified master 6e3e4134…7cca012a with audio loudness-normalised, video stream copied)
- PM review status: pending
- Professors' publication decision: pending
