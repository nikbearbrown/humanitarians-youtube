# Can AI Predict Your Next Click? — How Customer Engagement Scoring Works (16:9)

*Alternative titles: "Click. Convert. Leave. — How AI Predicts Customer Behavior" ·
"Predictive Customer Analytics — How AI Scores Engagement"*

A native **16:9 landscape** AI/STEM explainer, backed by a real, reproducible
machine-learning pipeline on synthetic data.

> **16:9 presenter-intro edition.** This folder is the landscape recomposition of
> `youtube/mycroft-thesisguard-brief/Can AI Predict Your Next Click` (9:16). It opens with:
>
> **B00** — *"Hi, I am Dhrumil Shah, and this video is about how AI estimates which customers
> will click, buy, or leave, and why those scores are probabilities, not certainties."*
>
> Narration, measured timing, captions text, music, mix, data, charts, and every on-screen
> claim are **identical** to the 9:16 cut. Only layout changed: every scene was redrawn for a
> wide canvas — not cropped, resized, or letterboxed. Separate Remotion composition:
> `CanAIPredictYourNextClick16x9`. The folder name omits the "?" because Windows does not
> allow it in file names.

**Presenter:** Dhrumil Shah · **Voice:** Kokoro `af_kore` (local) · **Runtime:** 2:36 · **Beats:** 17 ·
**Masters:** 3840×2160 · 1920×1080 · 1280×720 · 960×540 at 30 fps

## What is different from the 9:16 cut

Only layout. Documented scene by scene in [SHOTLIST.md](SHOTLIST.md):

- **Two-column scenes.** Most beats put the headline or explanation in a left column and the
  visual (cards, rings, chart, Manim diagram) in a right column.
- **Vertical stacks became rows.** Target cards (B05), Customer A's three probability rings
  (B08), and Customer B's rings (B09) sit side by side.
- **The training split is a horizontal timeline** (B06) — five prediction dates left to right
  with a dashed time-split marker before the test month.
- **The prediction date is a horizontal line** (B04): past windows above, locked future below,
  feature vector to the right.
- **Segmentation** (B10): count cards stacked beside a wider scatter plot.
- **End card** (B16): *Prediction ≠ Certainty* set on one line.
- **Captions** move to a bottom band clear of the player's progress bar; the 9:16 right-rail
  and bottom-UI reservations do not apply.
- **Thumbnail** is a 16:9 YouTube cover with the headline left and the silhouette + rings right.

## Problem statement

Marketing teams cannot manually judge, for thousands of customers, who is likely to click
the next email, who is likely to buy, and who is quietly leaving. Predictive models can
score those likelihoods — but they are routinely misunderstood as knowing what a person
will do, as proving that a campaign worked, or as permission to act without review.

## Video objective

Answer one question honestly: **Can AI really predict what a customer will do next?**
It can estimate probabilities from patterns in past behavior. **Prediction ≠ certainty**,
and **prediction ≠ causation**.

```text
EVENTS → FEATURES → MODEL → PROBABILITY → ACTION → MEASURE
```

## The demonstration: BrewBox

A **fictional online coffee shop** with 5,000 synthetic customers over 240 days
(1,217,852 events). No real person, email address, or protected attribute exists in the data.

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

Logistic regression beat histogram gradient boosting on validation log loss for all three
targets — a result on this dataset, not a general claim. Leakage prevention: history-slice
feature code (asserted), label windows that close before later prediction dates, targets/IDs/
opens excluded, and a 20-run label-shuffle test averaging ROC-AUC 0.52 (real model 0.89).

## Evaluation (held-out test date, 2026-07-04)

| Model | Base rate | ROC-AUC | PR-AUC | Brier | ECE | Precision / Recall / F1 |
|---|---:|---:|---:|---:|---:|---|
| Click · 7d | 29.2% | 0.881 | 0.760 | 0.125 | 0.020 | 0.65 / 0.75 / 0.69 |
| Purchase · 7d | 11.6% | 0.889 | 0.576 | 0.070 | 0.010 | 0.51 / 0.57 / 0.54 |
| Churn · 30d | 24.4% | 0.882 | 0.674 | 0.116 | 0.019 | 0.61 / 0.75 / 0.67 |

Top purchase group: 55% predicted, 56% observed. Feature importance is association, not
causation. The synthetic generator is cleaner than a real CRM, so real metrics will be lower.

## Claude's role

Claude is **not** the predictor. The scikit-learn models produce the scores; Claude turns them
into plain language, questions possible leakage, and drafts a holdout experiment for a person
to approve — see `prompts/claude_explain_scores.md`.

## Real-world example

Salesforce documents **Einstein Engagement Scoring** predicting email opens, clicks,
subscriber retention, and web conversion (checked 2026-09-12; `FACTCHECK.md` S01 — human
confirmation pending). Email opens are treated as noisy because Apple Mail Privacy Protection
can download remote content in the background regardless of engagement.

## Folder structure

```text
Can AI Predict Your Next Click_16x9/
├── README.md · research.md · script.md · beat_sheet.json
├── BUSINESS_REQUIREMENTS.md · DATA_DICTIONARY.md
├── SHOTLIST.md · FACTCHECK.md · PEDAGOGY.md · ASSETS.md · BUILD-LOG.md
├── data/ · src/ · models/ · evaluation/ · prompts/          (ML pipeline — shared with the 9:16 cut)
├── audio/       beat_00.wav … beat_16.wav · narration_master.wav · final_mix.wav · timings.json
├── captions/    captions.srt · captions.vtt · captions.json · cues.json · VALIDATION.md
├── assets/      charts/ · music/ · sfx/
├── storyboard/  beat_00.png … beat_16.png (960×540 stills of the 16:9 composition)
├── scenes/      remotion/CanAIPredictYourNextClick16x9.tsx · CPNCCover16x9.tsx · data/ · manim/ · renders/ (B12_frames/ PNG sequence used by B12)
├── scripts/     generate_narration · build_captions · generate_music_sfx · mix_audio · stage_manim_clip · sync_to_remotion · render_masters
├── thumbnails/  cover_1920x1080.png · cover_3840x2160.png
├── _qc/         OUTPUT-PROBE.md · qc-sheet.png · stills/ · review_cut_960x540.mp4
└── output/      Can-AI-Predict-Your-Next-Click-{4k,1920x1080,1280x720,proxy-960x540}(16x9)_Dhrumil_Shah.mp4
```

## Reproduction

Requirements: Python 3.12 with `numpy pandas scikit-learn matplotlib joblib kokoro-onnx manim`,
FFmpeg, Node 20+, and this workspace's `runtime/remotion` and `runtime/models/kokoro`.
No API keys or paid services.

```bash
# ML pipeline and audio are already built in this folder; re-run only if inputs change
python src/01_generate_data.py && python src/02_prepare_features.py && python src/03_train_models.py
python src/04_evaluate_models.py && python src/05_score_customers.py && python src/06_export_visualizations.py
python scripts/generate_narration.py && python scripts/build_captions.py
python scripts/generate_music_sfx.py && python scripts/mix_audio.py
manim -r 1728,1728 --fps 30 --media_dir scenes/renders/_manim -o B12_calibration scenes/manim/calibration_scene.py CalibrationScene
python scripts/stage_manim_clip.py

# 16:9 film
python scripts/sync_to_remotion.py        # requires CanAIPredictYourNextClick16x9 + CPNCCover16x9 in runtime/remotion/src/Root.tsx
python scripts/render_masters.py storyboard
python scripts/render_masters.py cover
python scripts/render_masters.py review
python scripts/render_masters.py master
python scripts/render_masters.py qc
```

## Citations

- Salesforce Help — *Einstein Engagement Scoring for Email Model Card*; Trailhead — *Einstein Engagement Scoring in Marketing Cloud*
- Apple — *Mail Privacy Protection & Privacy*; Apple Support — *Use Mail Privacy Protection*
- Kaufman, Rosset, Perlich & Stitelman (2012). Leakage in data mining. *ACM TKDD* 6(4). doi:10.1145/2382577.2382579
- Niculescu-Mizil & Caruana (2005). Predicting good probabilities with supervised learning. *ICML*. doi:10.1145/1102351.1102430
- Gutierrez & Gérardy (2017). Causal inference and uplift modelling: A review. *PMLR* 67:1–13.
- scikit-learn User Guide — *Permutation feature importance*; *Probability calibration*

## Limitations

- Synthetic data; churn definition and segment thresholds are demonstration choices.
- No uplift experiment was run; the B13 holdout diagram is illustrative.
- Salesforce claims rely on documentation fetched on 2026-09-12.
- Narration voice is `af_kore` (female) while the intro says "I am Dhrumil Shah" — see open items.

## Human review status

| Gate | Status |
|---|---|
| Fact-check S01 (Salesforce wording) | ⏳ human confirmation required |
| Fact-check G05 ("Only a holdout test") | ⏳ reviewer decision |
| Gate P narration review (`PEDAGOGY.md`) | ⏳ not signed |
| Presenter voice (`af_kore` vs a male voice such as `am_onyx`) | ⏳ presenter decision |
| Visual QC of rendered masters | see `BUILD-LOG.md` |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
