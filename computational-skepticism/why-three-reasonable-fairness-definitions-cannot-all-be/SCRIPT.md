# Script: Why Three Reasonable Fairness Definitions Cannot All Be True

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question:
"If an AI model has calibrated scores,
shouldn't its error rates
be equal across groups?"
Hesitates on "be equal across groups?", corrects to "diverge across groups?".
**Narration**:
"When an algorithm's scores mean the exact same thing across groups, we assume its error rates can be made equal too. But a four-line theorem from Bayes' rule proves they cannot. Let's trace why."

## B01 — stakes (The Public Dispute)
**Visual**: Manim `B01Scene`. Two opposing audit reports on the same model.
ProPublica: "False-Positive Rates Diverge Across Groups."
Northpointe: "Risk Scores Are Calibrated Across Groups."
Bottom banner: "BOTH AUDITS ARITHMETICALLY CORRECT".
**Narration**:
"In 2016, journalists reported that the COMPAS risk tool had unequal false-positive rates across racial groups; its maker proved its scores were calibrated. Both were mathematically correct."

## B02 — stakes (Definition One: Calibration Parity)
**Visual**: Manim `B02Scene`. Definition 1 Card: Calibration Parity (Predictive Parity).
Formula: $P(Y = 1 \mid \text{Score} = s, \text{Group } A) = P(Y = 1 \mid \text{Score} = s, \text{Group } B) = s$.
Meaning: An honest score. Score 70% means 70% risk for everyone.
**Narration**:
"The maker checked calibration parity: when the model assigns a risk score of seventy percent, exactly seventy percent of defendants in every group go on to reoffend. The score is honest."

## B03 — stakes (Definitions Two and Three: Equalized Odds)
**Visual**: Manim `B03Scene`. Definitions 2 & 3 Card: Equalized Odds.
Condition 1: False-Positive Rate Parity (Equal false alarm rate across groups).
Condition 2: True-Positive Rate Parity (Equal detection rate across groups).
Meaning: Error costs distributed equally across groups.
**Narration**:
"The critics checked equalized odds: innocent people should face the same low false-positive rate, and guilty people should face the same true-positive rate, regardless of group. Error costs are shared equally."

## B04 — wrong guess (The Tooling Fallacy)
**Visual**: Manim `B04Scene`. The Naive Assumption Card: "Bad Data or Biased Algorithm?"
Struck with Terracotta stroke: Neither. No algorithm, clean data, or optimization can satisfy both.
**Narration**:
"The natural assumption is that one side made an engineering error, collected bad data, or used a biased loss function that better tooling could fix. But no algorithm can satisfy both."

## B05 — mechanism (Four Quantities from Bayes' Rule)
**Visual**: Manim `B05Scene`. The four fundamental quantities defined:
Prevalence: $p = P(Y = 1)$ (Base Rate).
Sensitivity: $t = P(\hat{Y} = 1 \mid Y = 1)$ (True Positive Rate).
False Alarm: $f = P(\hat{Y} = 1 \mid Y = 0)$ (False Positive Rate).
Precision: $v = P(Y = 1 \mid \hat{Y} = 1)$ (Positive Predictive Value).
Bayes' formula displayed.
**Narration**:
"To see why, write down Bayes' rule. In any group with positive base rate p, true-positive rate t, and false-positive rate f, the positive predictive value v is precision: the probability a positive score is real."

## B06 — anchor planted (The Odds Identity Balance)
**Visual**: Manim `B06Scene`. Visual Object: The Odds Balance.
Formula: $\frac{v}{1 - v} = \frac{p}{1 - p} \cdot \frac{t}{f}$.
Left pan: Precision Odds $\frac{v}{1-v}$.
Right pan: Base-Rate Odds $\frac{p}{1-p}$ multiplied by Error-Rate Ratio $\frac{t}{f}$.
Balanced in equilibrium.
**Narration**:
"Rearrange Bayes' rule into odds form. The precision odds equal the base-rate odds multiplied by the error-rate ratio: v over one minus v equals p over one minus p, times t over f."

## B07 — anchor payoff / manim move: transform (Two Groups Side by Side)
**Visual**: Manim `B07Scene`. MANIM MOVE `transform`.
Group A and Group B balance equations displayed.
Calibration sets $v_A = v_B$, forcing the left-hand ratio to 1.
Equations transform into the ratio of error rates vs ratio of base rates:
$\frac{t_A / f_A}{t_B / f_B} = \frac{p_B(1 - p_A)}{p_A(1 - p_B)}$.
**Narration**:
"Now put Group A and Group B side by side. Calibration requires the score to mean the same probability everywhere, fixing the precision ratio to one. Transform the balance: the error-rate ratio is tied directly to the base rates."

## B08 — epistemic mechanism (The Tilted Balance)
**Visual**: Manim `B08Scene`. The Balance Tilts.
When base rates differ ($p_A \neq p_B$), the base-rate factor shifts away from 1.0 (e.g. 0.28).
The error-rate scale tilts sharply to compensate.
Terracotta visual indicator: Error-rate ratios cannot remain equal.
**Narration**:
"Whenever the base rates differ between groups, the base-rate term moves away from one. To preserve equality, the error-rate ratio t over f is mathematically forced to tilt in the opposite direction."

## B09 — epistemic mechanism (The Four-Line Impossibility)
**Visual**: Manim `B09Scene`. Chouldechova's Impossibility Theorem.
Four-line summary.
Line 1: Calibration requires $v_A = v_B$.
Line 2: Odds identity forces $\frac{t_A/f_A}{t_B/f_B} = \text{Base Rate Disparity Factor}$.
Line 3: Equalized odds demands $t_A = t_B$ and $f_A = f_B$ (Ratio = 1.0).
Line 4: Contradiction unless base rates are identical.
**Narration**:
"Equalized odds demands equal true-positive rates and equal false-positive rates, forcing the error ratio to one. But with different base rates, that equality is impossible. One of the two fairness definitions must break."

## B10 — one flag (The Two Theoretical Escapes)
**Visual**: Manim `B10Scene`. THE ONE FLAG: The Two Degenerate Escapes.
Escape 1: Groups have identical underlying base rates ($p_A = p_B$).
Escape 2: Perfect deterministic prediction ($t = 1.0, f = 0.0$, zero errors).
Warning badge: Neither escape exists in real-world human evaluations.
**Narration**:
"One flag — the arithmetic allows exactly two escapes: identical base rates across all groups, or clairvoyant prediction with zero errors. In real-world social evaluations, neither escape ever happens."

## B11 — direction A (Calibration ⇏ Equal Error Rates)
**Visual**: Manim `B11Scene`. Direction A: Calibrated Scores $\not\Rightarrow$ Equal Error Rates.
Card: Proving honest probabilities across groups with unequal base rates mathematically guarantees unequal false-positive or false-negative rates.
**Narration**:
"In one direction, proving your risk scores are perfectly calibrated across demographic groups does not mean error rates are fair. If base rates differ, calibrated scores guarantee unequal error rates."

## B12 — direction B (Equal Error Rates ⇏ Calibrated Scores)
**Visual**: Manim `B12Scene`. Direction B: Equal Error Rates $\not\Rightarrow$ Calibrated Scores.
Card: Forcing error rates to match across groups with unequal base rates mathematically distorts the scores, making them mean different probabilities for different groups.
**Narration**:
"In the other direction, forcing error rates to match across groups with different base rates does not guarantee score honesty. It mathematically guarantees that identical scores mean different probabilities for different groups."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"Calibrating scores across groups with different base rates forces their error rates apart — the conflict is Bayes' rule, not a tooling gap."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take a predictive model evaluated across demographic groups in your organization. Measure the base rate of the positive outcome in each group, and inspect both the false-positive rate and the positive predictive value. When the base rates differ, which definition of fairness did the team choose to satisfy — and who signed off on the definition that had to break? Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"Why Three Reasonable Fairness Definitions Cannot All Be True. Liam, in for Bear."
