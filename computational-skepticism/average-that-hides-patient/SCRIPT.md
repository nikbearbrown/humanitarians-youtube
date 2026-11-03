# Script: The Average That Hides the Patient

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "safe for every patient?", corrects to "hiding the patient who needs it?".
**Narration**:
"When an AI model's average calibration looks solid, does that mean every patient is protected? It doesn't. A calibration score is a weighted average, and an average can easily bury the patient who needs it most."

## B01 — stakes (The Deployed Sepsis Model)
**Visual**: Manim `B01Scene`. Proprietary sepsis model deployed across hundreds of hospitals. Internal validation badge: developer-reported AUC 0.76 to 0.83, aggregate calibration passed.
**Narration**:
"In hundreds of hospitals, a proprietary AI model monitored patients around the clock for sepsis. On paper, across millions of aggregate records, its calibration and performance numbers looked perfectly acceptable."

## B02 — stakes (The Michigan Medicine Audit: Wong et al. 2021)
**Visual**: Manim `B02Scene`. External validation audit card (Wong et al. 2021, Michigan Medicine, 27,697 patients): AUC drops to 0.63, Positive Predictive Value 12%, missed 67% of sepsis cases highlighted in terracotta.
**Narration**:
"Then independent researchers externally validated it at Michigan Medicine. The model missed sixty-seven percent of sepsis cases. Two out of three patients who actually developed sepsis were completely overlooked."

## B03 — anchor planted (The Patient Population Cloud)
**Visual**: Manim `B03Scene`. Anchor planted: A large population cloud of patient dots distributed across risk bands under a single global Expected Calibration Error gauge.
**Narration**:
"How does a model pass internal validation and fail so catastrophically on the floor? To see the arithmetic trap, look at how calibration is measured across a population."

## B04 — wrong guess (The Aggregate Equivalence Assumption)
**Visual**: Manim `B04Scene`. Wrong guess card: "Aggregate Calibration = Universal Safety. Low global ECE guarantees reliable probabilities for everyone." Struck through with a sharp terracotta slash.
**Narration**:
"The intuitive assumption is that an aggregate calibration score protects everyone equally. If the overall Expected Calibration Error is low, we assume predicted risks match real outcomes across the board."

## B05 — falsification (The Weighted Sum Trap)
**Visual**: Manim `B05Scene`. The weighted average mechanic: population weight bars showing 85% majority group versus 5% high-risk cohort. The majority arithmetically overpowers the overall score.
**Narration**:
"That intuition fails because calibration error is a weighted sum. Every patient group contributes to the final number in proportion to its size. A majority subgroup dominates the arithmetic."

## B06 — mechanism (The Reliability Diagram Diagonal)
**Visual**: Manim `B06Scene`. Reliability diagram coordinate system: Predicted Probability versus Observed Frequency with the 45-degree dashed line of perfect calibration. Bins aligned on the diagonal.
**Narration**:
"In a standard reliability diagram, predictions are grouped into confidence bins. A well-calibrated model tracks the diagonal: patients given an eighty percent risk develop the condition eighty percent of the time."

## B07 — mechanism (Aggregate Smoothing)
**Visual**: Manim `B07Scene`. Aggregate hospital reliability curve hugging the diagonal. Global ECE = 0.018. Routine cases smooth out the errors, creating the illusion of uniform reliability.
**Narration**:
"On aggregate, the entire hospital population hugs that diagonal. The healthy majority and routine admissions smooth out the errors, creating the illusion of trustworthy probabilities."

## B08 — anchor / manim move: collapse (The Cloud Collapses into One Metric)
**Visual**: Manim `B08Scene`. MANIM MOVE `collapse`. The wide cloud of patient dots physically collapses and pools inward into a single central box stamped "Global ECE: 0.018". All subgroup distinction vanishes.
**Narration**:
"Watch what happens when the entire patient cloud collapses into a single aggregate metric. Thousands of individual patients pool into one neat, reassuring number. All subgroup distinction vanishes."

## B09 — anchor payoff (Re-separating into Subgroups: Off the Diagonal)
**Visual**: Manim `B09Scene`. The collapsed box re-separates into distinct clinical subgroups. Adult cohort stays on the diagonal. Rare-disease and high-risk cases swing violently off the diagonal (illustrative ECE 0.103 in terracotta). Subgroup values marked as illustrative.
**Narration**:
"Now, re-separate those same patients into clinical subgroups. The adult cohort stays on the diagonal. But look at the rare cases and high-risk patients: their predictions swing wildly off the line."

## B10 — one flag (The Arithmetic Washout)
**Visual**: Manim `B10Scene`. Washout arithmetic card: 500 vulnerable patients with 25% calibration error + 9,500 routine patients with 1% error = Global ECE 0.022. The arithmetic dilutes the catastrophe 20 to 1.
**Narration**:
"A tiny subgroup can suffer catastrophic miscalibration with zero impact on the global score. In a cohort of ten thousand, a five percent group with broken probabilities moves the global error by a fraction of a percent."

## B11 — direction A (The Danger of Global False Assurance)
**Visual**: Manim `B11Scene`. Direction A card: Global Metric Only. Deploying on aggregate calibration creates blind spots where vulnerable patients receive dangerous probabilities under a clean seal.
**Narration**:
"In one direction, relying on a global metric gives false assurance. Deploying a model without subgroup decomposition exposes vulnerable patient pools to blind spots hidden inside a clean summary."

## B12 — direction B (The Subgroup Decomposition Protocol)
**Visual**: Manim `B12Scene`. Direction B card: Per-Subgroup Decomposition. Separate reliability curves for demographic and clinical cohorts establish where probabilities are earned and where clinical oversight must intervene.
**Narration**:
"In the other direction, requiring per-subgroup reliability curves reveals exactly where the model's probabilities hold and where human clinical oversight must step in."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"An aggregate calibration score doesn't tell you the model is safe for every patient — it tells you the majority is drowning out the vulnerable."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take the predictive model your team uses in production. Look up its published calibration error or reliability curve. Now, break down the evaluation data by demographic, severity, or site cohorts. Check whether any subgroup's error is more than double the global average. Run that decomposition before your next deployment review. Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"The Average That Hides the Patient. Liam, in for Bear."
