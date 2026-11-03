# Script: Why the Same Number Can Be Three Different Claims

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "what we can conclude?", corrects to "what verb we've earned?".
**Narration**:
"When a model hits eighty-seven percent on a benchmark, does that score tell you what you can conclude? It doesn't. The number is data. The verb is a claim with an evidence price."

## B01 — stakes (Three Engineers, One Score)
**Visual**: Manim `B01Scene`. A single benchmark card displaying 87% accuracy. Three engineering report excerpts emerge below: Engineer A writes "we observe," Engineer B writes "we find," Engineer C writes "we conclude."
**Narration**:
"Three engineers inspect the exact same model run. The held-out test score is eighty-seven percent. Engineer A writes 'we observe.' Engineer B writes 'we find.' Engineer C writes 'we conclude.' Only one of them is telling the truth."

## B02 — stakes (The Invisible Inflation)
**Visual**: Manim `B02Scene`. The 87% metric displayed on a card. As the verb shifts from "observe" to "conclude", a red inflation gauge spikes upward while the underlying data stays completely unchanged.
**Narration**:
"Eighty-seven percent looks like a hard, objective fact. But in a validation report, the verb does the heavy lifting. Changing that one word transforms a local measurement into a sweeping guarantee, without altering a single digit of data."

## B03 — wrong guess (The Score Dictates the Verb)
**Visual**: Manim `B03Scene`. Wrong guess card: "Claim strength scales directly with accuracy score (70% suggests, 87% finds, 99% concludes)." Struck through with a terracotta slash. A single test split card confirms the score is an outcome, not an evidentiary warrant.
**Narration**:
"The natural assumption is that claim strength scales with the score: seventy percent suggests, eighty-seven percent finds, and ninety-nine percent concludes. But accuracy is an outcome, not an evidentiary warrant."

## B04 — mechanism (Warranted Assertibility & The Frozen Ladder)
**Visual**: Manim `B04Scene`. Warranted assertibility diagram. The frozen eight-rung ladder appears: hypothesize, suggest, observe, find, show, demonstrate, conclude, prove.
**Narration**:
"Claims operate on warranted assertibility: you are entitled to assert only what your evidence pays for. The discipline uses a frozen eight-rung ladder: hypothesize, suggest, observe, find, show, demonstrate, conclude, prove."

## B05 — mechanism (The Entry Rungs: Hypothesize, Suggest, Observe)
**Visual**: Manim `B05Scene`. Highlight on the bottom three rungs: Hypothesize (pre-evidence idea), Suggest (consistent data, alternatives open), Observe (clean measurement, conditions stated).
**Narration**:
"The entry rungs cost little. 'Hypothesize' requires only a reason to explore. 'Suggest' requires data consistent with an idea without ruling out rivals. 'Observe' requires a clean measurement with its conditions stated."

## B06 — mechanism (The Mid Rungs: Find and Show)
**Visual**: Manim `B06Scene`. Highlight on the mid rungs: Find (replicated across seeds/variation) and Show (robustness confirmed, alternative explanations ruled out).
**Narration**:
"'Find' costs replication: the result must hold across seeds or parameter variations. 'Show' costs robustness and actively ruling out alternative explanations. A single run can never buy 'show,' no matter how high the score."

## B07 — mechanism (The Summit: Demonstrate, Conclude, Prove)
**Visual**: Manim `B07Scene`. Highlight on the top rungs: Demonstrate (designed stress experiment), Conclude (question settled, survives sensitivity analysis), Prove (strictly formal mathematics).
**Narration**:
"'Demonstrate' requires a purpose-built stress experiment with formal controls. 'Conclude' means the motivating question is settled and survives sensitivity checks. And 'prove' is reserved strictly for formal mathematics."

## B08 — anchor / manim move: accumulate (Stacking Evidence Under the Sentence)
**Visual**: Manim `B08Scene`. MANIM MOVE `accumulate`. A sentence on screen: "We [VERB] that the model achieves 87% accuracy." The verb slot is a dial. Evidence blocks stack beneath it one by one (single run → replicated seeds → subgroup checks → adversarial stress), causing the dial to climb rung by rung.
**Narration**:
"Watch the sentence on screen. The verb slot is a dial. As we stack evidence beneath it—first a single run, then replicated seeds, then subgroup audits, then adversarial stress tests—the dial climbs from observe to find, show, and conclude."

## B09 — anchor payoff (Paying the Toll)
**Visual**: Manim `B09Scene`. Return to the three engineers. The single-run receipt is held up against the ladder. Engineer A's "observe" is approved (paid in full). Engineer B's "find" is flagged (unbacked credit). Engineer C's "conclude" is rejected (gross over-claim).
**Narration**:
"Now look back at our three engineers. They had one run on one held-out split. That evidence pays the price for 'observe.' Engineer B borrowed unbacked credit. Engineer C committed outright verb inflation."

## B10 — one flag (Editorial Standard vs Physical Constant)
**Visual**: Manim `B10Scene`. One flag card: "Editorial Calibration Standard vs Physical Law". The ladder order represents an agreed operational convention for calibration, demanding receipts before spending verbs.
**Narration**:
"One flag — this eight-rung hierarchy is an editorial standard for calibration, not a law of physics. Different teams may use slightly different terms, but the core principle is universal: every verb requires evidentiary receipts."

## B11 — direction A (High Accuracy Does Not Buy Strong Verbs)
**Visual**: Manim `B11Scene`. Direction A card: 99% Accuracy ≠ Conclude. Single benchmark test split with massive 99% score, yet capped at "observe" because replication and sensitivity checks were never run.
**Narration**:
"In one direction, a ninety-nine percent score on a single benchmark does not buy you 'conclude.' Without replication, distribution shifts, and sensitivity analysis, you have only paid for 'observe.'"

## B12 — direction B (Modest Verbs Protect the Work)
**Visual**: Manim `B12Scene`. Direction B card: Calibrated Verbs = Durable Engineering. "Observe" survives scrutiny; "Conclude" collapses under peer audit.
**Narration**:
"In the other direction, writing 'observe' or 'find' does not diminish your engineering. Modest, calibrated verbs survive peer scrutiny, while inflated claims collapse the moment someone checks your test setup."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"Every claim-verb has an evidence price — you can only spend the verb your validation actually paid for."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take the last validation report or model card your team drafted. Highlight every occurrence of observe, find, show, and conclude. For each one, list the exact evidence backing that sentence: was it a single run, replicated seeds, subgroup checks, or a stress test? If the evidence doesn't pay the verb's price, downgrade it to the rung it earned. Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"Why the same number can be three different claims. Liam, in for Bear."
