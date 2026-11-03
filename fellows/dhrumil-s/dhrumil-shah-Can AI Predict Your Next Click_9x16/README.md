# Can AI Predict Your Next Click? — How Customer Engagement Scoring Works

*Alternative titles: "Click. Convert. Leave. — How AI Predicts Customer Behavior" ·
"Predictive Customer Analytics — How AI Scores Engagement"*

A native **9:16 vertical** AI/STEM explainer, backed by a real, reproducible
machine-learning pipeline on synthetic data.

> **Presenter-intro edition.** This folder is the same film as
> `youtube/claude-for-marketing/predictive-customer-analytics`, with one new opening beat:
>
> **B00** — *"Hi, I am Dhrumil Shah, and this video is about how AI estimates which customers
> will click, buy, or leave, and why those scores are probabilities, not certainties."*
>
> Every other beat, number, chart, and claim is unchanged. Because audio is the clock, all
> narration, captions, music, and the mix were regenerated so timings shift by the intro's
> measured 10.96 s. Separate Remotion composition: `CanAIPredictYourNextClick9x16`.
> The folder name omits the "?" because Windows does not allow it in file names.

**Presenter:** Dhrumil Shah · **Voice:** Kokoro `af_kore` (local) · **Runtime:** 2:36 · **Beats:** 17 ·
**Masters:** 2160×3840 · 1080×1920 · 720×1280 · 540×960 at 30 fps

## Problem statement

Marketing teams cannot manually judge, for thousands of customers, who is likely to click
the next email, who is likely to buy, and who is quietly leaving. Predictive models can
score those likelihoods — but they are routinely misunderstood as knowing what a person
will do, as proving that a campaign worked, or as permission to act without review.

## Video objective

Answer one question honestly: **Can AI really predict what a customer will do next?**
It can estimate probabilities from patterns in past behavior. **Prediction ≠ certainty**,
and **prediction ≠ causation**.

The film walks a general audience through a genuine ML workflow:

```text
EVENTS → FEATURES → MODEL → PROBABILITY → ACTION → MEASURE
```

## The demonstration: BrewBox

A **fictional online coffee shop** with 5,000 synthetic customers over 240 days
(1,217,852 events: newsletters, clicks, site visits, searches, product views, cart adds,
purchases, unsubscribes). A coffee shop gives every viewer an intuitive picture of all three
behaviours: clicking a *new-roast* email, buying a bag of beans, and quietly going silent.
No real person, email address, or protected attribute exists anywhere in the data.

## AI/ML architecture

```text
customer_events.csv ──► point-in-time features ──► 3 classifiers ──► probabilities
                          (history slice [0, s))     click · buy · churn     │
                                                                             ▼
                        human decision ◄── Claude explanation ◄── segments + evaluation
```

| Model | Target (window) | Population | Selected algorithm |
|---|---|---|---|
| Click | ≥ 1 newsletter click in the next 7 days | subscribed customers | Logistic regression |
| Conversion | ≥ 1 purchase in the next 7 days | all customers with ≥ 14 days tenure | Logistic regression |
| Churn | no click, visit, or purchase for 30 days *(demo definition)* | active in prior 90 days | Logistic regression |

**Model approach.** For each target, a logistic-regression baseline (log-scaled,
standardised features) and a histogram gradient-boosting classifier were trained on three
earlier prediction dates and compared on a later validation date by **log loss** — a proper
scoring rule that rewards calibrated probabilities, which matters because the film shows
percentages. Logistic regression had lower validation log loss for all three targets, so it
was kept; this is a result on this dataset, not a general claim that it beats boosting.

**Leakage prevention.** Feature code receives only the event history before the prediction
date (enforced by `assert`); every training label window closes before the validation date,
and every validation window before the test date; targets, IDs, and email opens are excluded
from inputs; a 20-run label-shuffle test averages ROC-AUC 0.52 (real model 0.89).

## Evaluation (held-out test date, 2026-07-04)

| Model | Base rate | ROC-AUC | PR-AUC | Brier | ECE | Precision / Recall / F1 @ validation threshold |
|---|---:|---:|---:|---:|---:|---|
| Click · 7d | 29.2% | 0.881 | 0.760 | 0.125 | 0.020 | 0.65 / 0.75 / 0.69 |
| Purchase · 7d | 11.6% | 0.889 | 0.576 | 0.070 | 0.010 | 0.51 / 0.57 / 0.54 |
| Churn · 30d | 24.4% | 0.882 | 0.674 | 0.116 | 0.019 | 0.61 / 0.75 / 0.67 |

Why these metrics: the events are imbalanced, so accuracy alone would flatter a model that
predicts "no" for everyone. ROC-AUC measures ranking; PR-AUC must be read against the base
rate; Brier score and the reliability diagram check that "55%" behaves like 55%
(top purchase group: 55% predicted, 56% observed). Charts are in `evaluation/`.

**Explainability.** Permutation importance and standardised coefficients: recent site visits
raise click and purchase probability; days since last activity raises churn risk.
These are associations the model relies on, **not causal effects**.

**Simulation caveat.** The generator has a clean latent structure, so these metrics are
higher than a real CRM would usually produce.

## Claude's role

Claude is **not** the predictor. The scikit-learn models produce the scores. Claude is the
reasoning layer that turns scores into plain language, questions possible leakage, and drafts
a holdout experiment for a person to approve — see `prompts/claude_explain_scores.md`.
Only pseudonymous IDs and aggregate outputs are shared with it.

## Real-world example

Salesforce documents **Einstein Engagement Scoring** predicting email opens, clicks,
subscriber retention, and web conversion (checked 2026-09-12; see `FACTCHECK.md` S01 — human
confirmation pending). It is referenced as one commercial implementation, not the only one.
Email opens are treated as noisy because Apple Mail Privacy Protection can download remote
content in the background regardless of engagement.

## Video production workflow (audio is the clock)

1. **Research** → `research.md`, `FACTCHECK.md`
2. **Dataset → features → training → evaluation → scoring → export** → `src/01–06`
3. **Script and beat sheet** → `script.md`, `beat_sheet.json` (source of truth)
4. **Narration** → Kokoro `af_kore`, synthesised sentence by sentence and measured →
   `audio/beat_XX.wav`, `audio/narration_master.wav`, `audio/timings.json`
5. **Captions** → `captions/captions.srt`, `captions.vtt`, burned-in `captions.json`
6. **Music + SFX** → code-synthesised, side-chain ducked, −14 LUFS → `audio/final_mix.wav`
7. **Scenes** → Remotion composition (all layouts native 9:16) + one Manim reliability diagram
8. **Storyboards → review cut → 4K master → derived masters → QC** → `storyboard/`, `output/`, `_qc/`

## Folder structure

```text
predictive-customer-analytics/
├── README.md · research.md · script.md · beat_sheet.json
├── BUSINESS_REQUIREMENTS.md · DATA_DICTIONARY.md
├── SHOTLIST.md · FACTCHECK.md · PEDAGOGY.md · ASSETS.md · BUILD-LOG.md
├── data/        customer_events.csv · customer_features.csv · scored_customers.csv · …
├── src/         common.py · 01_generate_data.py … 06_export_visualizations.py
├── models/      click_model.joblib · conversion_model.joblib · churn_model.joblib · model_selection.json
├── evaluation/  metrics.csv · roc/pr/calibration/confusion/importance PNGs · leakage_checks.json · subgroup_check.csv
├── prompts/     claude_explain_scores.md
├── audio/       beat_01.wav … beat_16.wav · narration_master.wav · final_mix.wav · timings.json
├── captions/    captions.srt · captions.vtt · captions.json · cues.json · VALIDATION.md
├── assets/      charts/ · music/ · sfx/
├── storyboard/  beat_01.png … beat_16.png (9:16 stills of the actual composition)
├── scenes/      remotion/ (composition + cover + data) · manim/ · renders/
├── scripts/     generate_narration · build_captions · generate_music_sfx · mix_audio · sync_to_remotion · render_masters
├── thumbnails/  cover_1080x1920.png · cover_2160x3840.png
├── _qc/         OUTPUT-PROBE.md · qc-sheet.png · stills/
└── output/      predictive_customer_analytics_{4k_vertical,1080x1920,720x1280,proxy_540x960}.mp4
```

## Reproduction

Requirements: Python 3.12 with `numpy pandas scikit-learn matplotlib joblib kokoro-onnx manim`,
FFmpeg, Node 20+, and this workspace's `runtime/remotion` (with its bundled Chrome Headless Shell)
and `runtime/models/kokoro` model files. No API keys or paid services.

```bash
# from this folder
python src/01_generate_data.py
python src/02_prepare_features.py
python src/03_train_models.py
python src/04_evaluate_models.py
python src/05_score_customers.py
python src/06_export_visualizations.py

python scripts/generate_narration.py
python scripts/build_captions.py
python scripts/generate_music_sfx.py
python scripts/mix_audio.py
manim -r 1728,1728 --fps 30 --media_dir scenes/renders/_manim -o B12_calibration scenes/manim/calibration_scene.py CalibrationScene
python scripts/stage_manim_clip.py       # constant-fps re-encode; raw Manim mp4 breaks Remotion's compositor

python scripts/sync_to_remotion.py        # requires both compositions registered in runtime/remotion/src/Root.tsx
python scripts/render_masters.py storyboard
python scripts/render_masters.py cover
python scripts/render_masters.py master
python scripts/render_masters.py qc
```

If narration text changes, re-run from `generate_narration.py` onward — never retime by hand.

## Citations

- Salesforce Help — *Einstein Engagement Scoring for Email Model Card*; Trailhead — *Einstein Engagement Scoring in Marketing Cloud*
- Apple — *Mail Privacy Protection & Privacy*; Apple Support — *Use Mail Privacy Protection*
- Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012). Leakage in data mining: Formulation, detection, and avoidance. *ACM TKDD*, 6(4). doi:10.1145/2382577.2382579
- Niculescu-Mizil, A., & Caruana, R. (2005). Predicting good probabilities with supervised learning. *ICML*. doi:10.1145/1102351.1102430
- Gutierrez, P., & Gérardy, J.-Y. (2017). Causal inference and uplift modelling: A review of the literature. *PMLR* 67:1–13.
- scikit-learn User Guide — *Permutation feature importance*; *Probability calibration*

## Limitations

- Synthetic data: real behaviour is noisier; metrics will be lower in practice.
- Churn definition is a demonstration choice.
- Segment thresholds are business choices, not optimised for cost.
- No uplift experiment was run; the B13 holdout diagram is illustrative.
- Subgroup audit uses simulation-only state a real business could not observe.
- Salesforce claims rely on documentation fetched on 2026-09-12 and can change.

## Human review status

| Gate | Status |
|---|---|
| Fact-check S01 (Salesforce wording) | ⏳ human confirmation required |
| Fact-check G05 ("Only a holdout test") | ⏳ reviewer decision |
| Gate P narration review (`PEDAGOGY.md`) | ⏳ not signed |
| Visual QC of rendered masters | see `BUILD-LOG.md` |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
