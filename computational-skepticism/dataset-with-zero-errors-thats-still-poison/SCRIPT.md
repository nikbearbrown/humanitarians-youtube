# The Dataset With Zero Errors That's Still Poison — Script

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Narrator**: Liam (in for Bear)
**Register**: Plain (Epistemic mechanism, then stop)
**Visual Object**: The Feedback Loop (Past World → Faithful Record → Trained Model → Automated Decisions → Future World)
**Manim Move**: trace

---

### [B00] Hesitant Writer Cold Open (Remotion)
*(Visual: Hesitant writer types naive question, hesitates on 'be free of bias', corrects to 'still produce harmful bias')*
**Liam**: If a dataset has no errors, no mislabels, and perfect coverage, you might assume the model trained on it cannot produce biased decisions. It can. In fact, its perfect accuracy is often what makes it harmful. Let's see why.

### [B01] 1 Stakes: The Clean Historical Dataset (Manim)
*(Visual: Tech company promotion archive card with 10 years of records, clean badges for 0 data-entry errors and 100% verified labels)*
**Liam**: A company trains an AI hiring tool on ten years of clean promotion records. Every entry is verified: who applied, who was promoted, when, and their documented performance. Zero data-entry errors. Zero annotator mistakes.

### [B02] 1 Stakes: Flawless Validation Metrics (Manim)
*(Visual: High-performing model scorecard with green metrics, 94% validation accuracy, and training convergence)*
**Liam**: The model trains to convergence. Validation accuracy is stellar. Test metrics come back completely green. Every standard diagnostic says the model learned the historical distribution with flawless fidelity.

### [B03] 4 ANCHOR PLANTED: The Feedback Loop (Manim)
*(Visual: THE ANCHOR — A circular 5-node loop: Past World → Faithful Record → Trained Model → Automated Decisions → Future World)*
**Liam**: To understand why this is dangerous, look at the system as a closed loop: past world, to faithful record, to trained model, to automated decisions, to future world. The dataset is an archive of past practices, not an oracle of fairness.

### [B04] 2 Wrong Guess: Bias as Noise or Error (Manim)
*(Visual: Naive mental model diagram equating bias strictly to data errors, dirty labels, or annotator slips, labeled 'The Quality Reflex')*
**Liam**: Intuition assumes that algorithmic bias comes from errors: noisy measurements, prejudiced annotators, or sloppy sampling. The common reflex is: "the labels are clean, so the pipeline is clean."

### [B05] 2 BREAK IT: Historical Reality Falsifies the Reflex (Manim)
*(Visual: Falsifying historical case: Promotion disparity 3x for men vs qualified women shown as faithful record of past world)*
**Liam**: That assumption breaks against historical reality. In the ten years the data recorded, the company promoted men to senior roles at three times the rate of equally qualified women. The data did not corrupt that history — it recorded it faithfully.

### [B06] 3 Mechanism: Historical Distribution vs Fair Distribution (Manim)
*(Visual: P(Y_historical | x) in ink contrasted with P(Y_fair | x) in terracotta, showing the fundamental divergence)*
**Liam**: So the model learns the conditional probability of historical promotion given candidate features, and learns it well. But the historical distribution is not a fair distribution. The world it mastered is a world you did not want to reproduce.

### [B07] 3 Mechanism: MANIM MOVE trace (Past World → Record → Model) (Manim)
*(Visual: Kinetic trace lighting up Past World → Faithful Record → Model, showing loss function optimizing proxy weights)*
**Liam**: Trace the flow: historical disparity in the past world flows into the clean training set. The model's loss function rewards fitting that pattern exactly, discovering subtle proxies that predict historical selection.

### [B08] 4 ANCHOR PAYOFF: Automated Decisions Exclude Candidates (Manim)
*(Visual: Kinetic trace continuing Model → Automated Decisions, rejecting qualified applicants from historically excluded groups)*
**Liam**: Now deploy the model. It ranks future candidates based on who looks like past winners. Its automated decisions reject qualified applicants from historically excluded groups.

### [B09] 4 ANCHOR PAYOFF: Closing the Feedback Loop (Manim)
*(Visual: Kinetic trace completing the loop: Decisions → Future World → New Dataset for Next Retraining run)*
**Liam**: Those automated decisions shape the future world. In three years, the company collects new promotion data. Because the model filtered the candidates, the new records reflect the exact same disparity — now laundered as machine-driven merit. The loop closes, feeding the next training run.

### [B10] 3 ONE FLAG: Technical Fixes Spend Predictive Fit (Manim)
*(Visual: The One Flag banner: Technical fixes (reweighting, constraints) trade predictive fit for less inheritance of the past)*
**Liam**: One flag — every algorithmic fix, from reweighting to fairness constraints, trades away predictive fit on the training data to inherit less of the past; you, not the loss function, must decide how much fit to spend.

### [B11] 5 DIRECTION A: What Zero Errors Does Not Guarantee (Manim)
*(Visual: Direction A: 0 Data Errors & 100% Clean Labels ≠ Unbiased / Safe AI struck through with heavy terracotta bar)*
**Liam**: So in one direction, a dataset with zero data-entry defects and flawless labels does not guarantee an unbiased model. When the past was unequal, a faithful record ensures the model will be unequal too.

### [B12] 5 DIRECTION B: What Bias Does Not Imply About Data Quality (Manim)
*(Visual: Direction B: Biased Predictions ≠ Broken Data / Mislabeled Rows. Data faithfully recorded historical reality)*
**Liam**: And in the other direction, a biased prediction does not mean the training data was corrupt or sloppily labeled. The data did not fail; it told the exact truth about a world we should not automate.

### [BCRY] 6 CARRY-OUT: The Single Sentence (Remotion)
*(Visual: Remotion WantQuote with the carry-out sentence in elegant serif typography)*
**Liam**: When a dataset faithfully records a discriminatory past, the model's accuracy is the harm — it projects what was into what will be, and calls the projection truth.

### [BHTF] Your Turn Handoff (Remotion)
*(Visual: Remotion ClaudeComposerAsk displaying paste-ready prompt for Claude)*
**Liam**: Your turn. Here's the prompt — read it with me. Identify an AI model in your organization that predicts success or risk based on historical records. Trace the feedback loop: does high predictive accuracy on past data reinforce historical selection patterns into future decisions? Liam, in for Bear.

### [BOUT] Outro (Remotion)
*(Visual: Remotion OutroCTA with Humanitarians AI branding and title restatement)*
**Liam**: The Dataset With Zero Errors That's Still Poison. Liam, in for Bear.
