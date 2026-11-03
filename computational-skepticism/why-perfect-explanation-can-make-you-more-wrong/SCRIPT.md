# Script: Why a Perfect Explanation Can Make You More Wrong

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "strictly more reliable", corrects to "sometimes dangerously wrong".
**Narration**:
"When an AI tool gives an accurate explanation, you assume it makes human decisions more reliable. In practice, a truthful explanation can make you far more confident in a wrong call. Let's see why."

## B01 — stakes (The Screening AI - Composite Case)
**Visual**: Manim `B01Scene`. Medical screening interface: AI malignancy risk prediction (84% High Confidence), feature X (texture) and feature Y (asymmetry) highlighted. Labeled "COMPOSITE CLINICAL ILLUSTRATION".
**Narration**:
"A radiologist reviews a screening image. An AI tool predicts high risk of malignancy at eighty-four percent confidence. And the system provides an explanation: the prediction was driven by texture pattern X and asymmetry Y."

## B02 — stakes (The False Concurrence & Benign Truth)
**Visual**: Manim `B02Scene`. Clinician reviews features X and Y ("Features Verified"), orders biopsy. Outcome stamp: "BIOPSY RESULT: BENIGN".
**Narration**:
"The radiologist looks at the image. Feature X is there. Feature Y is there. The explanation feels coherent, so she concurs and orders a biopsy. The biopsy comes back completely benign."

## B03 — wrong guess (The Explanation Fallacy)
**Visual**: Manim `B03Scene`. Striking down the misconception: "Assumption: Accurate Explanation = Correct Decision". The model was not lying about itself.
**Narration**:
"The natural reaction is to assume the AI hallucinated or gave a fake explanation. But the explanation was completely accurate: the model really used features X and Y. The model did not lie about itself."

## B04 — mechanism (Shortcut Learning)
**Visual**: Manim `B04Scene`. Training data correlation (Shortcut: features X & Y correlated with cancer scans) vs Deployment population (features X & Y belong to benign condition).
**Narration**:
"What happened is shortcut learning. In training, features X and Y correlated with cancer cases. But in this patient's population, those same features belong to a benign condition. The model learned a shortcut."

## B05 — mechanism (Internal Accounting vs The World)
**Visual**: Manim `B05Scene`. Two panels: "MODEL'S INTERNAL ACCOUNTING (What the network calculated)" vs "STATE OF THE WORLD (What is biologically true)".
**Narration**:
"Post-hoc explanations faithfully describe a model's internal accounting. They tell you what the model did. They cannot tell you whether what the model did warrants belief about the real world."

## B06 — anchor planted (The Two-Path Decision Flow)
**Visual**: Manim `B06Scene`. Two-Path Decision Flow: Path A (Prediction Alone) vs Path B (Prediction + Explanation), each with a confidence meter.
**Narration**:
"To see how this misleads, compare two ways a clinician evaluates an AI output: seeing the prediction alone, versus seeing the prediction paired with an explanation."

## B07 — anchor payoff / manim move: compare (Path A: Prediction Alone)
**Visual**: Manim `B07Scene`. MANIM MOVE `compare` (Panel A): Prediction Alone. Clinician sees 84% score, remains cautious. Confidence meter stays balanced at 50%.
**Narration**:
"In Path A, the doctor sees only the eighty-four percent score. Because she knows classifiers can be noisy, she treats the score with healthy skepticism, keeping her confidence balanced at fifty percent."

## B08 — anchor payoff / manim move: compare (Path B: Prediction + Explanation)
**Visual**: Manim `B08Scene`. MANIM MOVE `compare` (Panel B): Prediction + Explanation. Clinician sees 84% score plus highlighted features. Plausible narrative triggers unearned trust: Confidence meter surges to 90%.
**Narration**:
"In Path B, she sees the exact same score alongside the highlighted features. Because the story is plausible and verifiable, her confidence surges to ninety percent — locking in an aggressive, mistaken decision."

## B09 — epistemic mechanism (The Fluency Trap)
**Visual**: Manim `B09Scene`. The Fluency Trap: Well-formed narrative -> unearned epistemic trust. The explanation does epistemic work it never earned.
**Narration**:
"This is the fluency trap: well-formed outputs are mistaken for evidence of truth. The explanation gave a flawed decision a convincing narrative, transferring unearned confidence from the machine's accounting to the human mind."

## B10 — one flag (Transparency Is Not Truth)
**Visual**: Manim `B10Scene`. THE ONE FLAG: Explaining the calculation does not validate the reality. Transparency of internal math is not proof of truth in deployment.
**Narration**:
"One flag — an explanation provides transparency into a model's internal computation, but transparency of math is not proof of truth in deployment. Inspecting internal weights does not validate reality."

## B11 — direction A (Accurate Does Not Mean Correct)
**Visual**: Manim `B11Scene`. Direction A: Faithful Explanation ⇏ Correct Decision (Accurate report of a broken shortcut).
**Narration**:
"So in one direction, a perfectly faithful explanation does not prove the model is right. It may simply give you a pristine, high-fidelity view of a broken shortcut."

## B12 — direction B (Flawed Does Not Mean Dishonest)
**Visual**: Manim `B12Scene`. Direction B: Flawed Prediction ⇏ Dishonest Tool (Tool exposed its internal accounting; human supervision must supply the external check).
**Narration**:
"And in the other direction, a wrong decision does not mean the explanation tool lied. It did its job by exposing the model's logic — leaving the skepticism to us."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"A faithful explanation describes the model's internal accounting, not the world — so when a model learns a shortcut, an accurate explanation makes a wrong call feel right."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take a deployed classifier in your stack that provides feature explanations. Audit five cases where the model made an error. Did the explanation faithfully describe the model's shortcut, and would reading it make a reviewer more likely to approve the mistake? Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"Why a Perfect Explanation Can Make You More Wrong. Liam, in for Bear."
