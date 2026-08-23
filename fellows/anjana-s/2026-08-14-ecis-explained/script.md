# ECIS Episode 2 — Two Brains, 25 Companies, One Scorecard

**Skill:** ai-explainer
**Target length:** ~60 seconds
**Voice:** am_onyx (Onyx)
**Narrator:** Anjana
**Style:** Same register as Episode 1. Confident, technical-but-accessible. This is the system grown, not the system explained.

---

## Beat 1 — Recap

**Duration:** ~5 seconds

**Narration:**

ECIS reads earnings calls with four independent readers and one triangulator. That was version one. Here is what it looks like now.

**Visual direction:**

Quick flash of the Episode 1 architecture diagram — the four-reader flow into the triangulator. It appears fully formed, not animated piece by piece like in Episode 1. Hold for two seconds, then a brief zoom-out transition revealing the diagram is now just one piece of a larger system. Visual handoff to Beat 2.

---

## Beat 2 — Two Models

**Duration:** ~15 seconds

**Narration:**

The LLM reader used to be one model. Now it is two. Llama and Mistral process every chunk independently through the same pipeline, the same prompts, the same self-consistency checks. They do not share answers. The triangulator weighs both. When they agree, confidence goes up. When they disagree, the system knows exactly where the language is ambiguous.

**Visual direction:**

The LLM reader node from Episode 1 splits into two parallel nodes — "Llama" and "Mistral" — each in a distinct color (Llama: purple, Mistral: teal). Both receive the same chunk flowing in from the left. Both output independently to the triangulator.

Animated sequence: a chunk flows in, both models process it. First example: both output "raised" — a green agreement line connects them. Second example: Llama outputs "maintained," Mistral outputs "raised" — a red disagreement line appears. The triangulator node pulses, absorbing both signals and outputting a single verdict with an adjusted confidence score.

---

## Beat 3 — Scale

**Duration:** ~12 seconds

**Narration:**

The pipeline now runs across twenty to twenty-five companies. Hundreds of transcripts, thousands of chunks, all flowing through the same four readers, the same routing, the same scorecard. What started on two tickers is now watching a full sector.

**Visual direction:**

The architecture diagram from Beat 2 shrinks to the center of the screen. Around it, a grid of ticker symbols fades in — twenty to twenty-five labels arranged in a circle or grid (NVDA, MSFT, GOOGL, META, AMD, etc.). Data streams flow from each ticker toward the central pipeline. A counter animates upward: "Transcripts processed: 200+" and "Signals extracted: 1,000+."

The visual sells volume — many inputs, one pipeline handling all of them.

---

## Beat 4 — The Boundary

**Duration:** ~12 seconds

**Narration:**

At this scale, the hardest call is not raised or lowered. It is the line between maintained and nothing. A CEO says "we are comfortable with our current outlook." Is that guidance maintained, or is that just a sentence? The system now draws that boundary precisely. Maintained means the company actively reaffirmed. Nothing means there was no guidance at all.

**Visual direction:**

Two side-by-side quote cards on a dark background.

Left card: "We are reaffirming our full-year revenue outlook of twelve billion dollars." Tagged below: "MAINTAINED" in blue, confidence 0.82.

Right card: "We remain focused on executing our strategy." Tagged below: "NONE" in grey, confidence 0.91.

A dividing line between the cards pulses — labeled "The Boundary." The visual point: these two sentences sound similar to a human reader, but the system classifies them differently and correctly.

---

## Beat 5 — The Dashboard

**Duration:** ~10 seconds

**Narration:**

Everything lands in one place. Every signal, every reader's vote, every calibration curve, every model's performance, and every decision the feedback loops make. Not a report generated after the fact. A live system you can query, drill into, and interrogate.

**Visual direction:**

A stylized dashboard mockup animates in — not a screenshot, but a clean motion-graphics representation. Four panels build in sequence:

1. Signal explorer — a table with rows populating (ticker, direction, confidence)
2. Calibration curve — the familiar plot from Episode 1, now with two lines (Llama and Mistral)
3. Model comparison — a side-by-side bar chart of Brier scores
4. Agent activity log — a timeline with event dots appearing

The panels should feel alive — numbers ticking, curves drawing, dots appearing — conveying a live working system.

---

## Beat 6 — Close

**Duration:** ~5 seconds

**Narration:**

Two models. Twenty-five companies. One scorecard that never looks away. ECIS, episode two.

**Visual direction:**

Quick montage: the dual-model node flashes, the ticker grid pulses, the scorecard calibration curve appears. Text lands center screen: "ECIS — Episode 2." Same sign-off style as Episode 1. Fade to Claude-branded outro bookend.

---

## Production Notes

**Total estimated duration:** ~59 seconds of narration + bookends = ~65 seconds total

**Continuity with Episode 1:** Reuse the same visual language — same dark background palette, same node shapes for readers, same calibration curve style. The viewer should feel this is the same system, grown.

**Voice:** am_onyx, same as Episode 1. Pacing slightly faster than Episode 1 — this is an update, not a first explanation. The viewer already knows the basics.

**Visual mix:** All Remotion. Beat 2 (dual model split) is the signature visual. Beat 4 (the boundary) is the insight beat. Beat 5 (dashboard) should feel like a live system, not a static mockup.

**Numbers to confirm before audio:**
- "Twenty to twenty-five companies" — confirmed as preferred range
- "Hundreds of transcripts" — verify approximate count
- "Signals extracted: 1,000+" — verify or adjust the counter number
