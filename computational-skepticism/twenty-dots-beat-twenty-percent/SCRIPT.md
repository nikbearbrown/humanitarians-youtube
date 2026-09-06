# Script — Twenty Dots Beat "Twenty Percent"

**Series**: Computational Skepticism for AI  
**Episode**: Twenty Dots Beat "Twenty Percent"  
**Candidate**: Candidate 30  
**Source**: *Computational Skepticism for AI*, Chapter 10 (*Visualization Under Validation: Honest, Misleading, and the Choices Between*)  
**Register**: Plain (explain the epistemic mechanism, then stop)  
**Narrator**: Liam (Kokoro `am_onyx`, in for Bear)  
**Palette**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`  
**Kinetic Move**: `split`  

---

### B00 — Brutalist Hesitant Writer Cold Open
**Visual**: Writer types the naive framing in serif type on cream ground, pauses in hesitation, strikes the misconception with terracotta, and types the real question.  
**Typing text**:
```
When communicating model uncertainty,
isn't 20% probability
the clearest way to report it?
```
**Hesitate & Replace**:
- `triggerWords`: "the clearest way to report it?"
- `replacementWords`: "a trap for human intuition?"

**Narration (Liam)**:
> When we report model uncertainty or diagnostic risk, we default to percentages. Twenty percent chance of failure. Ninety percent accuracy. But percentages force mental arithmetic that human intuition consistently botches. Twenty dots beat twenty percent every time. Let's trace why.

---

### B01 — Stakes: The Physician Diagnostic Study
**Move**: 1 Stakes First  
**Visual**: Manim card displaying the clinical screening numbers: "Sensitivity: 90%", "False Positive Rate: 9.9%", "Prior Prevalence: 0.8%". A silhouette of a physician with an estimated risk callout: "Estimated probability of disease: 80% to 90%". Struck with a warning callout.  
**Narration (Liam)**:
> Consider Gerd Gigerenzer's famous study of experienced physicians. They were given standard mammography statistics: ninety percent sensitivity, a nine point nine percent false-positive rate, and a baseline prevalence of roughly eight in one thousand. When asked the chance a positive patient actually has cancer, most estimated eighty to ninety percent.

---

### B02 — The Wrong Guess: Doctors Are Bad at Math
**Move**: 2 Wrong Guess  
**Visual**: Manim illustration showing a complex Bayesian formula struck out in terracotta, replaced by a side-by-side comparison bar: Percentage Presentation (<20% correct) vs Natural Frequency Presentation (>80% correct).  
**Narration (Liam)**:
> The standard reaction is that physicians are bad at probability, and that professionals simply need more training in statistical formulas. But when Gigerenzer presented the exact same medical facts as counts of people rather than normalized percentages, correct answers jumped from under twenty percent to over eighty percent.

---

### B03 — Mechanism: The Percentage Fog
**Move**: 3 Epistemic Mechanism (Part 1: Concealed Base Rates)  
**Visual**: Manim diagram showing two diverging percentage bars: 90% sensitivity looks huge, 9.9% false positives looks small. Then zoom in to show the underlying denominators: 8 disease cases vs 992 healthy cases.  
**Narration (Liam)**:
> Percentages conceal population scale. Ninety percent sensitivity sounds overwhelming, while a ten percent false-positive rate sounds harmless. But because the disease is rare, ten percent of a massive healthy population produces roughly one hundred false alarms, completely swamping the eight genuine cases.

---

### B04 — Anchor Planted: The 1,000-Person Grid
**Move**: 4 Anchor Planted (Kinetic Move: `split` Part 1)  
**Visual**: A 1,000-dot grid (40 columns by 25 rows) fills the frame. The dots split into two distinct clusters: a small cluster of 8 terracotta dots (women with cancer) and a large cluster of 992 muted ink dots (healthy women).  
**Narration (Liam)**:
> Picture one thousand women screened for cancer. Grounded as countable individuals, the data splits immediately. Only eight women actually have the disease. Nine hundred and ninety-two women are healthy.

---

### B05 — Anchor Move: The Screening Split
**Move**: Kinetic Move (`split` Part 2)  
**Visual**: The screening test runs. The 8 sick dots split: roughly 7 or 8 turn bright terracotta (true positives). The 992 healthy dots split: roughly 99 turn terracotta (false alarms), while the remaining 893 fade away. The positive pool clusters together: 8 true cases amid 99 false alarms.  
**Narration (Liam)**:
> Now run the screening test. The eight cancer cases split: roughly seven or eight test positive. The healthy group splits: ninety-nine test positive as false alarms. Fade the negative tests. In the positive room, roughly eight out of one hundred and seven people are sick. That is under ten percent, visible at a single glance.

---

### B06 — Mechanism: The Perception Hierarchy
**Move**: 3 Epistemic Mechanism (Part 2: Cleveland–McGill Hierarchy)  
**Visual**: Manim hierarchy chart ranking perceptual channels: Position and Count at the top with minimal decoding error, down through Length, Angle, Area, and Shaded Color.  
**Narration (Liam)**:
> This works because of how the human visual system decodes information. In the Cleveland–McGill perception hierarchy, abstract percentages and color shading require error-prone mental computation. Spatial position and discrete item counts sit at the absolute top, decoded effortlessly without arithmetic.

---

### B07 — Anchor Payoff: The Twenty-Dot Quantile Dotplot
**Move**: 4 Anchor Paid Off (Kinetic Move: `split` Part 3)  
**Visual**: The crowd condenses into a clean 20-dot quantile dotplot: twenty circular marks along a horizontal baseline. Exactly four dots are filled in terracotta; sixteen are open circles. Below, the clear natural-frequency sentence: "Out of 20 deployments, expect about 4 failures."  
**Narration (Liam)**:
> This brings us to the quantile dotplot. If your AI model has a twenty percent probability of failure, reporting "twenty percent risk" sounds like an abstract quibble. Showing twenty dots with exactly four filled transforms an elusive percentage into a concrete count: out of twenty deployments, expect about four failures.

---

### B08 — One Flag: The Translation Boundary
**Move**: One Inference Flag  
**Visual**: Manim callout highlighting the boundary between perception and judgment: "Position and count eliminate the translation tax. They do not decide your risk tolerance."  
**Narration (Liam)**:
> Here is the essential distinction. Showing twenty dots removes the translation tax; it does not make the decision for you. Four filled dots give stakeholders an accurate grasp of the odds, but human judgment must still decide whether four failures in twenty is acceptable.

---

### B09 — Limits & Both Directions
**Move**: 5 Both Directions  
**Visual**: Manim split-screen: Left panel: "Abstract Percentages: Miscalibration & Confusion". Right panel: "Extreme Base Rates: Dot Grid Scalability Limit (e.g. 1 in 100,000)".  
**Narration (Liam)**:
> Both limits matter. Relying on raw percentages guarantees miscalibration, because human working memory confuses conditional test rates with actual posterior odds. But quantile dotplots also fail when base rates are extreme, where representing one failure in a million either forces rounding or an unreadable sea of dots.

---

### BCRY — Carry-Out Line
**Move**: 6 Carry-Out Line  
**Visual**: Remotion `WantQuote` component. Cream background, warm ink serif type, terracotta accent.  
**Quote**: "Position and count replace mental arithmetic with direct perception."  
**Narration (Liam)**:
> Position and count replace mental arithmetic with direct perception.

---

### BHTF — Your Turn Handoff
**Move**: Your Turn Audit Prompt  
**Visual**: Remotion `ClaudeComposerAsk` component.  
**Narration (Liam)**:
> Your turn. Here's the prompt — read it with me. Take one critical failure rate or diagnostic risk in your system currently reported as a percentage. Redesign it as a twenty-dot quantile dotplot with natural-frequency narration underneath: out of twenty cases, expect about N. Test both on a non-technical stakeholder. Does their risk assessment change? Liam, in for Bear.

---

### BOUT — Outro CTA
**Move**: Series Outro  
**Visual**: Remotion `OutroCTA` component.  
**Narration (Liam)**:
> Twenty Dots Beat "Twenty Percent". Liam, in for Bear.
