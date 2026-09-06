# Script: You Can't Escape the Fairness Impossibility — You Can Only Choose Where to Sign

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question:
"If group fairness is mathematically impossible,
can't a better framework
escape the trade-off?"
Hesitates on "escape the trade-off?", corrects to "just relocate the bill?".
**Narration**:
"When group fairness metrics hit an impossibility theorem, engineers look for an escape hatch: individual fairness, causal models, or an inequality index. But every one hands you back the same bill. Let's see where it lands."

## B01 — stakes (The Impossibility Remainder)
**Visual**: Manim `B01Scene`.
Title: THE IMPOSSIBILITY REMAINDER
The group fairness conflict: Demographic Parity, Equalized Odds, and Calibration Parity cannot align across unequal base rates.
The Invoice attached: "BILL: Choose which group rate gives."
**Narration**:
"The fairness impossibility theorem proved that group metrics cannot simultaneously align when base rates differ. It feels like an arithmetic trap. So machine learning researchers built three clever escape hatches to bypass group metrics entirely."

## B02 — stakes (Escape Hatch One: Individual Fairness)
**Visual**: Manim `B02Scene`.
Title: ESCAPE HATCH 1 — INDIVIDUAL FAIRNESS
Intuition: "Treat similar individuals similarly."
Visual: Stepping down from aggregate group clouds to paired individuals.
**Narration**:
"The first exit drops down from groups to individuals. Instead of balancing aggregate statistics across populations, demand that similar people receive similar outcomes. If you audit individuals one pair at a time, maybe the group conflict evaporates."

## B03 — epistemic mechanism (Relocation One: The Ruler d)
**Visual**: Manim `B03Scene`.
Title: THE FIRST RELOCATION: THE RULER (d)
A calibrated ruler labeled "Similarity Metric d".
The invoice hops onto the ruler: "BILL: Define who counts as comparable."
Callout: "Omit zip code? Bake historical disparity in? You decide."
**Narration**:
"Watch where the price moves. To treat similar people similarly, you must first define who counts as similar. That requires a task-specific ruler, the similarity metric d. Decide which features matter, and the equation works. Pick a metric that ignores historical inequalities, and you bake structural unfairness directly into the guarantee. The impossibility did not vanish; it relocated into the ruler."

## B04 — stakes (Escape Hatch Two: Causal Fairness)
**Visual**: Manim `B04Scene`.
Title: ESCAPE HATCH 2 — CAUSAL FAIRNESS
Intuition: Observational data conflates discrimination with legitimate pathways.
Visual: Climbing the ladder from observational correlation to structural generative models.
**Narration**:
"The second exit climbs Pearl's causal ladder. Group and individual metrics only look at observational correlations. But correlation cannot separate wrongful discrimination from disparity that arose through a legitimate credential. Build a structural causal model of how the data was generated, and maybe you can target only the unfair paths."

## B05 — epistemic mechanism (Relocation Two: The Causal Graph)
**Visual**: Manim `B05Scene`.
Title: THE SECOND RELOCATION: THE CAUSAL GRAPH
A directed acyclic graph: Sensitive Attribute A -> Mediator M -> Prediction Y_hat, and direct path A -> Y_hat.
The invoice hops onto the graph: "BILL: Declare which causal paths are illegitimate."
Callout: "Data alone cannot draw this graph or judge its paths."
**Narration**:
"And here is the invoice on the causal exit. Which causal pathways are illegitimate discrimination, and which are legitimate business requirements? The data cannot tell you. You cannot even ask the question without first drawing a full causal graph of the world on your own authority. Causal fairness did not solve the impossibility; it billed you for a complete theory of the world."

## B06 — stakes (Escape Hatch Three: The Inequality Index)
**Visual**: Manim `B06Scene`.
Title: ESCAPE HATCH 3 — CONTINUOUS INEQUALITY
Moving from a binary pass/fail to a continuous scoreboard.
Visual: Economists' inequality lens — total unfairness decomposed into within-group and between-group components.
**Narration**:
"The third exit treats fairness not as a binary pass or fail, but as a continuous scoreboard. Borrowing inequality metrics from economics, we can treat each person's prediction benefit like income, measuring total unfairness on a single scale that splits into within-group and between-group components."

## B07 — epistemic mechanism (Relocation Three: The Alpha Slider)
**Visual**: Manim `B07Scene`.
Title: THE THIRD RELOCATION: THE ALPHA SLIDER
A tuning slider labeled "Sensitivity Parameter α" with low α (bottom inequity) vs high α (top inequity).
The invoice hops onto the slider: "BILL: Define 'benefit' and decide whose disparity matters most."
**Narration**:
"Now look at where the price landed. To use an inequality index, you must assign a numerical benefit to every outcome, which is already a moral choice. Then you must tune the sensitivity slider, alpha. Low alpha weights disparities at the bottom; high alpha weights the top. The index gives you a higher-resolution scoreboard, but it cannot dissolve the values choice you had to make."

## B08 — anchor payoff / manim move: morph (The Hopping Invoice)
**Visual**: Manim `B08Scene`. MANIM MOVE: `morph`.
Visual Object: The Traveling Invoice.
A prominent, stylized Invoice / Price-Tag card morphs and hops across four stations:
Station 1: Group Dial (Which rate gives?)
Station 2: Ruler d (Who is similar?)
Station 3: Causal Graph (Which paths are illegitimate?)
Station 4: Alpha Slider (Whose inequality counts?)
Stamp: "VALUES JUDGMENT REQUIRED — SIGN HERE".
**Narration**:
"Trace the invoice across all four frameworks. The group dial forced you to choose which error rate breaks. The individual ruler forced you to define similarity. The causal graph forced you to judge which paths are legitimate. The inequality slider forced you to weight who matters most. The mathematical impossibility is never solved; it is only re-addressed to the person who must sign the object."

## B09 — one flag (The Upstream Construct Limit)
**Visual**: Manim `B09Scene`.
THE ONE FLAG: The Upstream Construct Gap.
A model predicting "Observed Proxy (Re-arrest / Default)" vs the true construct "Social Construct (Public Safety / Creditworthiness)".
Banner: "No metric downstream can validate the task upstream."
**Narration**:
"Here is the one flag: even if you sign all three, none of these frameworks can tell you whether the prediction task itself was fair to pose. An algorithm can satisfy individual, causal, or group fairness on an observed proxy like re-arrest or test scores, while completely missing the social construct you actually care about. That gap sits upstream of every metric on this page."

## B10 — both directions (The Dual Limits)
**Visual**: Manim `B10Scene`.
Two side-by-side diagnostic cards:
Left: Direction A — Mathematical Elegance Smuggles Values (A clean proof can hide biased assumptions).
Right: Direction B — Rejection Leaves Coarse Blindspots (Ignoring advanced tools blinds you to individual and causal harms).
**Narration**:
"This cuts both directions. In one direction, a mathematically rigorous framework can satisfy its proof perfectly while smuggling biased assumptions into the similarity metric or the causal graph. In the other direction, refusing these frameworks leaves you trapped in coarse group averages that cannot distinguish legitimate credentials from systemic discrimination."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
Quote: "You cannot escape the fairness impossibility — every advanced framework simply relocates the values choice to a new object you have to sign."
SparkLine: "The bill always comes due."
**Narration**:
"You cannot escape the fairness impossibility — every advanced framework simply relocates the values choice to a new object you have to sign."

## BHTF — your turn handoff (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
Topic: "FAIRNESS RELOCATION AUDIT"
Command:
"Take an algorithmic decision system in your organization that claims to satisfy individual, causal, or continuous fairness. Identify the specific object that encodes its core assumptions — the similarity metric, the causal graph, or the benefit function. Who defined that object, what values trade-off does it embed, and who signed off on it?"
**Narration**:
"Your turn. Here's the prompt — read it with me. Take an algorithmic decision system in your organization that claims to satisfy individual, causal, or continuous fairness. Identify the specific object that encodes its core assumptions — the similarity metric, the causal graph, or the benefit function. Who defined that object, what values trade-off does it embed, and who signed off on it? Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
Line: "Computational Skepticism for AI from @HumanitariansAI."
Title: "You Can't Escape the Fairness Impossibility — You Can Only Choose Where to Sign"
Subline: "Liam, in for Bear."
**Narration**:
"You Can't Escape the Fairness Impossibility — You Can Only Choose Where to Sign. Liam, in for Bear."
