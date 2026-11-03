# ECIS — Explainer Video Script

**Skill:** ai-explainer
**Target length:** ~2 minutes
**Voice:** am_onyx (Onyx)
**Style:** Vox-style narration, direct and confident, fintech register

---

## Beat 1 — The Hook

**Duration:** ~12 seconds

**Narration:**

Every quarter, a CEO gets on a call and says something like "we remain cautiously optimistic about our forward outlook." Did that company just raise guidance? Lower it? Or say absolutely nothing? ECIS reads the transcript and tells you — automatically, with a confidence score you can actually trust.

**Visual direction:**

Remotion text animation. A real earnings call quote fades in center-screen in a monospaced font. Three labels animate in below it — "Raised?" / "Lowered?" / "Maintained?" — each pulsing once before "Raised" locks in with a green highlight and a confidence badge reading "0.87". Claude-branded intro bookend leads into this.

---

## Beat 2 — The Problem

**Duration:** ~18 seconds

**Narration:**

Here is the problem. An earnings call transcript runs five to ten thousand words of hedged, legalistic language. A simple keyword search catches the obvious phrases but misses anything subtle. A single language model will hallucinate signals that are not there. And reading every transcript manually does not scale — not when you are tracking thirty to fifty companies every quarter.

**Visual direction:**

A wall of dense transcript text scrolls vertically at high speed — too fast to read, conveying volume. Specific phrases highlight in sequence as the narration mentions them: a keyword match lights up green, then a hallucinated extraction flashes red with a strike-through, then the scroll accelerates to show scale. End on a freeze-frame of one ambiguous sentence with a question mark overlay.

---

## Beat 3 — The Architecture

**Duration:** ~28 seconds

**Narration:**

ECIS does not trust any single method. It runs four independent readers on every chunk of every transcript. A keyword reader scans for known guidance phrases. FinBERT, a financial sentiment model, scores the tone. A named entity recogniser extracts the hard numbers — dollar amounts, percentages, dates. And a large language model reasons through the passage step by step, with chain-of-thought prompting, self-consistency checks across three temperature passes, and a second verification call where the model critiques its own work. A triangulator then fuses all four signals using dynamic weights — readers that keep being right get more influence.

**Visual direction:**

Manim-style animated flow diagram. A transcript document icon enters from the left and splits into chunks. Each chunk flows into four parallel nodes arranged vertically — Keyword, FinBERT, NER, LLM — each drawn in a distinct colour. Arrows from all four converge into a central Triangulator node on the right, which outputs a single signal block labelled with direction and confidence. The dynamic weights visualise as varying line thicknesses on the arrows feeding the triangulator.

---

## Beat 4 — Smart Routing

**Duration:** ~22 seconds

**Narration:**

Not every chunk needs the full treatment. An orchestration agent classifies each chunk into one of four categories based on the fast-pass results. Category A — both readers agree — goes to the LLM for confirmation. Category B — one reader flagged something, the other did not — gets the full extraction pipeline. Category C — the readers disagree — routes to a dedicated conflict resolution subgraph. And Category D — neither reader detected anything — gets skipped entirely. That single routing step cuts LLM inference calls by sixty to eighty percent.

**Visual direction:**

Animated decision tree built in Manim or Remotion. Chunks enter from the top and flow down through a classification node. Four branches split outward — A, B, C, D — each labelled with its rule. Category D chunks visually dissolve or grey out, showing the compute savings. A counter in the corner tallies "LLM calls saved: 60–80%" as D chunks accumulate.

---

## Beat 5 — The Honest Scorecard

**Duration:** ~25 seconds

**Narration:**

Every signal ECIS extracts is pre-registered — written to an append-only log the moment it is produced, before anyone knows whether the prediction was correct. After thirty days, the system checks the market. Did the stock outperform its sector benchmark? The Brier score measures overall accuracy. The skill score answers whether each reader actually beats the keyword baseline. Expected calibration error checks whether the system's confidence means what it says — when it says eighty percent, is it right eighty percent of the time? And Murphy decomposition separates fixable calibration errors from genuine lack of signal.

**Visual direction:**

Two-part visual. First part: a code block showing the Pydantic signal schema slides in, with the key fields highlighted — ticker, direction, confidence, supporting_quote. An "append-only" lock icon stamps onto it. Second part: transition to an animated calibration curve — a Plotly-style scatter plot where the X axis is stated confidence, the Y axis is observed accuracy, and dots plot along or away from a diagonal reference line. Bins that sit on the diagonal glow green; bins that deviate glow amber.

---

## Beat 6 — Self-Correction

**Duration:** ~20 seconds

**Narration:**

ECIS is not a static pipeline. Three agentic feedback loops run continuously. The calibration watchdog detects when confidence scores drift and fits a new recalibration model. The orchestration learning graph checks whether skipped chunks contained missed signals and adjusts routing thresholds accordingly. And the vindication tracker records which reader wins each conflict and reweights the triangulator over time. Routine adjustments happen automatically. Structural changes — model reversion, reader removal, threshold shifts over twenty-five percent — pause the system and wait for a human to approve.

**Visual direction:**

Three circular loop arrows animate in sequence, each cycling back through a simplified version of the pipeline. Loop one: a recalibration curve updating. Loop two: the routing thresholds sliding. Loop three: triangulator weight bars shifting. On the final sentence, a human silhouette icon appears at a gate checkpoint, with an "Approve / Reject" button pair, conveying the human-in-the-loop interrupt.

---

## Beat 7 — The Close

**Duration:** ~8 seconds

**Narration:**

Four readers. One scorecard. Three feedback loops. And a human who signs every gate that matters. That is ECIS.

**Visual direction:**

Quick montage: the four reader icons flash in sequence, the scorecard table appears, the three loop arrows pulse, and the human gate icon locks. Cut to the Claude-branded outro bookend with the project name "ECIS" and a link or QR code to the repo.

---

## Production Notes

**Total estimated duration:** ~2 minutes 13 seconds (adjust narration pacing to land between 1:50 and 2:20)

**Voice:** am_onyx — its deeper register suits the authoritative, technical-but-accessible tone. Avoid af_bella here; the content is dense enough that a warmer voice risks sounding incongruent.

**Visual mix:** Beats 3 and 4 are the Manim-heavy segments (flow diagrams, decision trees). Beats 1, 2, 5, and 6 lean on Remotion motion graphics (text animation, chart animation, looping arrows). Beat 5 bridges both with a code block transitioning to a chart.

**Pacing:** The narration is written to be read at a natural speaking pace, roughly 150–160 words per minute. If the TTS output runs long, trim the parenthetical details in Beats 3 and 5 first — those are the densest and most cuttable without losing the story.

**Bookends:** Claude-branded intro before Beat 1, Claude-branded outro after Beat 7, per the ai-explainer skill spec.
