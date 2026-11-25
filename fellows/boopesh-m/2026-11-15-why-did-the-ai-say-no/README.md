# Why Did the AI Say No? — Boopesh M.

AI-in-finance explainer on explainable AI in lending. When a US lender turns down a credit application, Regulation B
(under the Equal Credit Opportunity Act) asks for a statement of **specific** reasons, the principal ones; "you
failed to reach our score" is named in the rule as not enough. This film shows how a credit model's "no" can be split
into per-feature pushes ("reason codes"), why that is exact for a simple scorecard, and why a black-box model makes it
harder. CFPB Circular 2022-03 said the same duty applies to complex algorithms; ⚠️ per search results it was withdrawn
in May 2025 (see FACTCHECK.md). Every number in the film comes from my own small experiment on **synthetic
applicants**. This is what the rule asks for, not legal advice.

## This week's contribution
- **Question:** when an AI credit model denies a loan, can we name the specific reasons, and does a black-box model
  give the same reasons as a simple scorecard?
- **Prediction:** a logistic scorecard gives exact reasons for free; a boosted model needs an attribution method,
  costs far more to explain, and may disagree.
- **What I built:** `code/credit_reasons.py` (numpy + scikit-learn, seed 42; 20,000 synthetic applicants with five
  plain features and no protected traits; a logistic scorecard and a gradient-boosted model; exact Shapley values
  computed by hand; one counterfactual), a 16:9 explainer (2:27) and a native 9:16 Short (0:46)
  whose charts come from its outputs.
- **Observed result:** both models rank risk equally well (test AUC 0.836 each). Made-up Applicant A (DTI 44 %, cards
  72 % used, 1 missed payment, 4 years of history, $52k) is denied by both at a 30 % risk line I chose (scorecard
  53.2 %, black box 34.1 %). Scorecard reasons (weight × (A − average), exact): debt-to-income +0.82, card use +0.76,
  missed payments +0.43. Black-box reasons (exact Shapley values, 32 combinations × 500 applicants = 16,000 model runs):
  missed payments +0.60, card use +0.45, credit history +0.30. They share 2 of 3 reasons. The black box's list shifts:
  against approved applicants only, or after retraining on another 70 % split, debt-to-income returns to its top 3.
  Paying card balances down by $3,850 (72 % → 34 % of an assumed $10,000 limit) flips both models to "yes"
  (29.9 %, 28.7 %).
- **Next experiment:** the B80 prompt — retrain the black box with 20 seeds and count how often A's top 3 changes.

## Human and AI work
- **My decisions, implementation and verification:** chose the AI-in-finance series and the voice (`am_onyx`,
  approved 2026-10-24); reviews the numbers, the synthetic-applicant framing, the "not legal advice" framing and the ⚠️
  claims about the circular.
- **AI tools/voices used and what they generated:** Claude (Claude Code) tried to read the regulation and the circular,
  read Regulation B from a mirror of the official eCFR, checked the circular by search, wrote and ran the experiment
  (twice, identical), drafted the script, beat sheets and Manim scenes, rendered and checked frames. Kokoro `am_onyx`
  speaks the narration (disclosed on screen and in the audio).
- **What I rejected or corrected:** see [FRICTIONAL.md](FRICTIONAL.md).
- **What remains unverified or failed:** the CFPB circular and its May 2025 withdrawal were not read directly
  (consumerfinance.gov and every copy blocked), only search summaries (⚠️ in [FACTCHECK.md](FACTCHECK.md)); Regulation B
  was read from a GitHub mirror of the official eCFR bulk data, not ecfr.gov itself; the applicants, Applicant A, the
  30 % cutoff and the $10,000 card limit are made up; Shapley values are one attribution method of several; fairness is
  out of scope. Pronunciation of "Shapley" needs a human listen.

## Files
| File | What it is |
|---|---|
| `code/credit_reasons.py` | the experiment (numpy + scikit-learn, seed 42); writes `results.json`; `run.log` is the run |
| `code/typeset.py` | the one formula (push toward no = weight × (A − average)) → SVG via matplotlib MathText |
| `beat_sheet.json` / `make_sheet.py` | the 16:9 film as code |
| `scenes.py` | Manim scenes (read the experiment outputs directly) |
| `short/` | native 9:16 Short: own beat sheet, scenes, paperwork |
| `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `PROOF.md`, `FRICTIONAL.md`, `BUILD-LOG.md`, `description.txt` | paperwork |

## Reproduce
- **Brutalist commit:** `a99b5323`, checked 2026-11-15
  ```bash
  pip install scikit-learn   # 1.9.1 was used
  cd code && python credit_reasons.py > run.log && python typeset.py ../assets ../short/assets && cd ..   # ~10 s
  python3 make_sheet.py && (cd short && python3 make_sheet.py)
  python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <this folder>          # and short/
  python3 <brutalist>/runtime/scripts/remotion_scenes.py <this folder> --only B00    # also B10, B80; short: B00
  <brutalist>/art run <this folder>
  <brutalist>/art final <this folder> --height 2160
  # Short: same on short/, final with --height 3840
  ```

## Watch and review
- Landscape Drive link (add) — 3840×2160 — 2:27 — SHA-256: 494e9c394b7acd0ae387fafb41a861bf34a315cc2e7b907a16bbb81525d661d2 (−14.2 LUFS; verified master cbadb94f…ceb1b283 with audio loudness-normalised, video stream copied)
- Vertical Drive link (add) — 2160×3840 — 0:46 — SHA-256: 7a5d69adb8c42a7dcb82203e7720e588918c7ab061219114bdc0def31869772c (−14.2 LUFS; verified master b09068b5…6b7fc42 with audio loudness-normalised, video stream copied)
- PM review status: pending
- Professors' publication decision: pending
