# The Backtest Mirage — Boopesh M.

AI-in-finance explainer: why an AI that searches thousands of trading strategies always finds one that looks
brilliant on past data, and then fails on new data (backtest overfitting, a multiple-testing problem). Anchored on
Bailey, Borwein, López de Prado & Zhu, "Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest
Overfitting on Out-of-Sample Performance", *Notices of the AMS* 61(5), 2014 (⚠️ the paper could not be opened from the
build container; its details come from search summaries, see FACTCHECK.md). Every number in the film comes from my
own small experiment on **synthetic noise data**, where no strategy can have a real edge.

## This week's contribution
- **Question:** if an AI tries 10,000 trading rules on a market with nothing to find, how good does the best one look?
- **Prediction:** the best backtest will look good by luck alone, better the more rules are tried, and it will be
  worth nothing on data the search never saw.
- **What I built:** `code/backtest_mirage.py` (numpy, seed 42; 7 years of pure-noise daily returns, 5 years searched,
  2 years held out; 10,000 random long/short rules; the same search repeated on 200 fresh noise markets), a 16:9
  explainer (2:24) and a native 9:16 Short (0:45) whose charts come from its outputs.
- **Observed result:** the best of 10,000 rules has an in-sample Sharpe ratio of 1.69 and an out-of-sample Sharpe of
  −0.37. Over 200 noise markets the median best in-sample Sharpe climbs with the number of rules tried: −0.08 (1),
  0.69 (10), 1.06 (100), 1.34 (1,000), 1.58 (10,000), while the winners' out-of-sample average is about zero (−0.02 at
  10,000). The spread of a zero-edge 5-year Sharpe is 0.44, matching 1/√5 = 0.45. The best of 45 rules reaches a median
  of 0.91 (0.99 for 45 independent tries), in line with the paper's warning as summarised in search results (about 45 tries
  on 5 years of data can give a Sharpe near 1 by luck). The bar that only 5 % of pure-noise searches beat rises from 0.78 (1 rule) to 1.91 (10,000 rules), so the
  1.69 winner is correctly rejected.
- **Next experiment:** the B80 prompt — plant a small real edge and add trading costs; does the search find it?

## Human and AI work
- **My decisions, implementation and verification:** chose the AI-in-finance series and the voice (`am_onyx`,
  approved 2026-10-24); reviews the numbers, the synthetic-noise framing and the ⚠️ claims about the paper.
- **AI tools/voices used and what they generated:** Claude (Claude Code) tried to read the paper, checked its details
  by search, wrote and ran the experiment (twice, identical), drafted the script, beat sheets and Manim scenes,
  rendered and checked frames. Kokoro `am_onyx` speaks the narration (disclosed on screen and in the audio).
- **What I rejected or corrected:** see [FRICTIONAL.md](FRICTIONAL.md).
- **What remains unverified or failed:** the paper was not read directly (ams.org and every copy blocked), so its
  wording and the 45-trials figure are from secondary summaries (⚠️ in [FACTCHECK.md](FACTCHECK.md)); the data is
  synthetic noise; no trading costs; the rules are a simple random search, not a trained model. Pronunciation of
  "Borwein" and "Zhu" needs a human listen.

## Files
| File | What it is |
|---|---|
| `code/backtest_mirage.py` | the experiment (numpy, seed 42); writes `results.json`, `curves.npz`; `run.log` is the run |
| `code/typeset.py` | the one formula (Sharpe noise ≈ 1/√years) → SVG via matplotlib MathText |
| `beat_sheet.json` / `make_sheet.py` | the 16:9 film as code |
| `scenes.py` | Manim scenes (read the experiment outputs directly) |
| `short/` | native 9:16 Short: own beat sheet, scenes, paperwork |
| `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `PROOF.md`, `FRICTIONAL.md`, `BUILD-LOG.md`, `description.txt` | paperwork |

## Reproduce
- **Brutalist commit:** `a99b5323`, checked 2026-11-08
  ```bash
  cd code && python backtest_mirage.py > run.log && python typeset.py ../assets && cd ..   # ~1 min, numpy only
  python3 make_sheet.py && (cd short && python3 make_sheet.py)
  python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <this folder>          # and short/
  python3 <brutalist>/runtime/scripts/remotion_scenes.py <this folder> --only B00    # also B10, B80; short: B00
  <brutalist>/art run <this folder>
  <brutalist>/art final <this folder> --height 2160
  # Short: same on short/, final with --height 3840
  ```

## Watch and review
- Landscape Drive link (add) — 3840×2160 — 2:24 — SHA-256: 3ae8c51555e605794f6851226d0dd205f8a4352b2c67bb1ef19eee6ef55661fa (−14.2 LUFS; verified master 2463630b…eb97f0f0 with audio loudness-normalised, video stream copied)
- Vertical Drive link (add) — 2160×3840 — 0:45 — SHA-256: 97134de6416ca71e1d42ab92e5ea6a94f6c845117034c433087efbb0d221980b (−14.3 LUFS; verified master f3c8f271…1be47667 with audio loudness-normalised, video stream copied)
- PM review status: pending
- Professors' publication decision: pending
