# Script: Same CSV, two dashboards, opposite beliefs

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "the same belief?", corrects to "opposite beliefs?".
**Narration**:
"If two builders plot the exact same validation CSV, will their dashboards tell the same story? They won't. Without changing a single byte of data, they can engineer opposite beliefs. Here's how."

## B01 — stakes (The Fixed Validation CSV)
**Visual**: Manim `B01Scene`. The raw validation CSV table on cream card. Overall 94% accuracy, but Groups A, B, and C drop to 61%, and calibration error spikes. Handed to two builders with opposite instructions.
**Narration**:
"Take one byte-for-byte fixed validation CSV for a deployed model. Hand it to two builders. Tell one to reassure a nervous partner, and the other to provoke hard questions. Watch what happens."

## B02 — stakes (Two Opposite Takeaways)
**Visual**: Manim `B02Scene`. Two deployment partners reviewing two dashboards from this exact CSV. Partner 1 walks away reassured: "System Safe to Deploy". Partner 2 walks away alarmed: "Subgroup Failure & Overconfidence".
**Narration**:
"The deployment partner walks away from the first dashboard convinced the system is safe to ship, and from the second convinced it needs immediate review. The data never changed. The beliefs did."

## B03 — wrong guess (The Data Tampering Fallacy)
**Visual**: Manim `B03Scene`. Wrong guess card: "Someone altered the dataset rows or faked the numbers." Struck through with terracotta slash. SHA-256 hash match confirms byte-for-byte identical data.
**Narration**:
"The natural instinct is to assume someone doctored the rows, filtered the test set, or falsified a metric. But check the hash: both dashboards query the exact same table. The numbers are identical; the architecture is not."

## B04 — mechanism (The Structural Argument)
**Visual**: Manim `B04Scene`. Left side: unchanged CSV anchored in place. Right side: dashboard canvas. Annotation: "A dashboard is an argument made through structural choices."
**Narration**:
"A dashboard is not a transparent window into facts. It is an argument made through structural choices. Five quick decisions — each taking thirty seconds — completely transform what the reader perceives before any number is read."

## B05 — mechanism (Choice 1: Headline Dominance vs Equal Panels)
**Visual**: Manim `B05Scene`. Choice 1 in action: Reassuring dashboard stamps a massive bold metric: **94% Accuracy**. Honest dashboard displays three equal panels: Overall, Subgroups, Calibration.
**Narration**:
"Choice one is visual hierarchy. The reassuring dashboard leads with a massive bold metric: ninety-four percent accuracy. The eye stops there. The honest dashboard displays equal panels, forcing the viewer to integrate the whole picture."

## B06 — mechanism (Choice 2: Axis Truncation on Subgroups)
**Visual**: Manim `B06Scene`. Choice 2 in action: Subgroup bar chart. On the honest dashboard, 0–100% axis shows the 33-point plunge to 61%. On the reassuring dashboard, the axis is compressed, flattening the drop into a hairline dip.
**Narration**:
"Choice two is axis scaling. When displaying the three failing subgroups, the builder squeezes the vertical scale. A thirty-point drop that should look alarming flattens into a harmless ripple. The disparity vanishes into the baseline."

## B07 — anchor / manim move: accumulate (Accumulating Choices 3, 4, & 5)
**Visual**: Manim `B07Scene`. MANIM MOVE `accumulate`. The dashboard layout accumulates choices 3, 4, and 5 side-by-side with the unchanged CSV. Choice 3: Color salience (green vs gray). Choice 4: Tab burial (calibration curve tucked into sub-tab). Choice 5: Reassuring framing banner.
**Narration**:
"Watch the choices accumulate beside the unchanged CSV. Choice three: paint the overall score reassuring green and gray out the disparities. Choice four: bury the broken calibration curve inside an obscure sub-tab. Choice five: stamp a green banner declaring the system verified."

## B08 — anchor payoff (Identical Data, Inverted Reality)
**Visual**: Manim `B08Scene`. The two finished dashboards side by side with the unchanged CSV between them. Dashboard A manufactures false confidence; Dashboard B exposes the real failure modes.
**Narration**:
"Here is the final payoff. Identical data, identical rows, but two completely opposite arguments. The reassuring dashboard manufactures confidence by burying doubt; the honest dashboard makes the failure modes visible at a glance."

## B09 — one flag (Defaults vs Malice)
**Visual**: Manim `B09Scene`. One flag card: "Library Defaults vs Deliberate Malice". Layouts often result from default plotting library templates optimized for looking finished rather than honest.
**Narration**:
"One flag — we cannot infer that misleading dashboards stem from deliberate bad faith. Most builders simply accept default plotting templates designed to look polished and clean, never realizing their layout choices are making an argument."

## B10 — direction A (Accurate Data Does Not Guarantee Truth)
**Visual**: Manim `B10Scene`. Direction A card: Verified Data ≠ Honest Communication. Zero calculation errors, yet a deceptive visual argument.
**Narration**:
"In one direction, verifying the numbers does not verify the dashboard. You can audit every cell in the underlying CSV, confirm zero calculation errors, and still hand stakeholders a completely deceptive visual argument."

## B11 — direction B (Honest Structure Preserves Evidence)
**Visual**: Manim `B11Scene`. Direction B card: Honest Layout = Preserved Evidence. Exposing reality so human judgment can evaluate tradeoffs.
**Narration**:
"In the other direction, an honest layout does not make the decision for you. It does not prove the model is ready or broken. It simply preserves the evidence so human judgment can operate on reality rather than reassurance."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"A dashboard argues by structure before any number is read — the design choices are the argument."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take the primary dashboard your team uses to evaluate model performance. Identify five layout choices: the headline metric, the axis baselines, the color salience, the tab placement, and the card framing. For each choice, write down the argument the visual structure makes before anyone reads the numbers. Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"Same CSV, two dashboards, opposite beliefs. Liam, in for Bear."
