# Script: The Best Fix for a Biased Model Didn't Touch the Model

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question:
"If an AI model is producing biased outcomes,
shouldn't we fix it by
retraining the model?"
Hesitates on "retraining the model", corrects to "looking outside the model".
**Narration**:
"When an AI system produces biased outcomes, engineers reflexively fix the code or retrain the model. But the fix that actually works often leaves the model completely untouched. Let's trace why."

## B01 — stakes (The Parable Setup)
**Visual**: Manim `B01Scene`. Parable setup card labeled "CONSTRUCTED COMPOSITE CASE". A deployed AI decision pipeline produces documented disparities in downstream decisions. Three engineering teams are assigned to fix it.
**Narration**:
"Consider a constructed case from real practice. A deployed AI pipeline produces documented disparities in downstream decisions. Three engineering teams are given the exact same mission: eliminate the disparity."

## B02 — stakes (Team One: The Loss Function Fix)
**Visual**: Manim `B02Scene`. Team One: Loss Function Rewritten. Added fairness penalty to training loss. Retrained model. Disparity: Slight, partial drop.
**Narration**:
"The first team rewrites the loss function. They add an algorithmic penalty to punish disparate group error rates and retrain. The disparity drops slightly, but mostly persists."

## B03 — wrong guess (Team Two: The Training Data Resampling Fix)
**Visual**: Manim `B03Scene`. Team Two: Training Data Resampled. Recaptured underrepresented groups, balanced dataset, retrained. Disparity: Reshaped, not resolved.
**Narration**:
"The second team rebuilds the training data. They recruit underrepresented groups, rebalance the dataset, and retrain the original model. The disparity shifts shape, but the core imbalance remains."

## B04 — mechanism (Team Three: The Deployment Room Fix)
**Visual**: Manim `B04Scene`. Team Three: Deployment Context. Examines downstream human reviewers and decision thresholds. Never touches weights or data. Disparity: Drops dramatically.
**Narration**:
"The third team touches neither the model nor the training data. Instead, they examine the room the model was deployed into: downstream human review and decision thresholds. The disparity collapses by an order of magnitude."

## B05 — mechanism (The Three Teams Puzzle)
**Visual**: Manim `B05Scene`. The three teams comparison. Teams One and Two were not incompetent; their fixes worked on the specific paths they touched. But they were low-leverage because most of the bias traveled elsewhere.
**Narration**:
"Teams one and two were not incompetent. Their fixes were genuine, but low leverage. They acted on real causal paths that happened to carry very little of the bias."

## B06 — anchor planted (The Causal Path Diagram)
**Visual**: Manim `B06Scene`. Visual Object: Causal path diagram from World / Protected Attribute -> Proxies -> Model Features -> Model Output -> Reviewer Room -> Final Outcome.
**Narration**:
"To see why, draw the causal path from the world to the final decision. The protected attribute feeds proxy features, which split: some enter the model, but others bypass it directly into human review."

## B07 — anchor payoff / manim move: trace (Tracing Paths & Dams)
**Visual**: Manim `B07Scene`. MANIM MOVE `trace`. Trace bias flow through the network. An intervention acts as a dam: it only blocks what its specific path carries. Team One dammed the model, leaving the bypass channel wide open.
**Narration**:
"Trace the bias flow along every channel. An intervention acts as a dam: it only stops what its specific path carries. Team One dammed the model, leaving the bypass channels wide open."

## B08 — epistemic mechanism (Why Bypasses Dominate)
**Visual**: Manim `B08Scene`. Human reviewers interpret scores through their own lenses or apply uneven thresholds. Bias flows around the algorithm. Polishing model weights leaves that downstream conduit completely untouched.
**Narration**:
"When human reviewers systematically interpret scores differently or enforce uneven appeal thresholds, bias flows around the algorithm. Polishing the model's weights leaves that downstream conduit completely untouched."

## B09 — epistemic mechanism (Leverage Analysis Procedure)
**Visual**: Manim `B09Scene`. Leverage Analysis 4-step card: 1. Trace full pipeline graph. 2. Identify all flow paths. 3. Test candidate dams. 4. Intervene at the highest-volume bottleneck.
**Narration**:
"Leverage analysis asks where the bias actually travels before writing code. You map every path from world to outcome, and locate the bottleneck that carries the largest share of the disparity."

## B10 — one flag (Qualitative Leverage vs Complete Shield)
**Visual**: Manim `B10Scene`. THE ONE FLAG: Qualitative effect sizes. Blocking the downstream bypass is high leverage, but it does not mean the model itself is blameless or exempt from scrutiny.
**Narration**:
"One flag — high leverage at deployment does not mean the model is blameless. It means an intervention's impact is bounded by its path, and treating the model as the sole culprit misallocates engineering effort."

## B11 — direction A (In-Model Debiased ⇏ Fair Outcome)
**Visual**: Manim `B11Scene`. Direction A: Perfectly Debiased Model Parameters does NOT imply Fair Final Outcomes (downstream review paths leak bias).
**Narration**:
"So in one direction, proving your model's internal weights are perfectly balanced does not guarantee an unbiased outcome in the world."

## B12 — direction B (Disparate Outcome ⇏ Flawed Model)
**Visual**: Manim `B12Scene`. Direction B: Disparity in Final Decisions does NOT imply the ML model was the primary source of the bias.
**Narration**:
"And in the other direction, discovering a disparity in final decisions does not mean the model was the primary culprit. The highest-leverage bias path may live entirely outside the model."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"An intervention only removes what its causal path carries — and the highest-leverage path often bypasses the model entirely."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take an AI model in your organization that assists real-world decisions. Map the causal path from real-world inputs to the final outcome: data collection, model scoring, and the human review process. If an unfair disparity appears, which path carries the most bias — and would retraining the model even touch it? Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"The Best Fix for a Biased Model Didn't Touch the Model. Liam, in for Bear."
