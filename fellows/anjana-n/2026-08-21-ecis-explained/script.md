# ECIS Episode 3 — Three Models, Zero Shortcuts

**Skill:** ai-explainer
**Target length:** ~60 seconds
**Voice:** am_onyx (Onyx)
**Narrator:** Anjana
**Style:** Same register as Episodes 1 and 2. The system is maturing — the tone should reflect confidence and precision. This episode is about discipline, not just scale.

---

## Beat 1 — Recap

**Duration:** ~5 seconds

**Narration:**

Last time, ECIS had two models reading every earnings call. Llama and Mistral, side by side. That was episode two. Now there are three.

**Visual direction:**

The dual-model architecture from Episode 2 appears instantly — Llama (purple) and Mistral (teal) feeding into the triangulator. Same visual language, same node shapes. Hold for two seconds. Then the frame pulls back slightly, making room on the right side for something new. Visual handoff to Beat 2.

---

## Beat 2 — The Third Model

**Duration:** ~15 seconds

**Narration:**

Qwen two point five, fourteen billion parameters. Twice the size of the other two. It runs the same pipeline, the same prompts, the same self-consistency checks. But it sees things differently. More reliable on structured output. Fewer retries on malformed responses. The architecture was reworked so multi-model is not an add-on anymore. Model identity flows through the pipeline state. The triangulator weighs all three independently.

**Visual direction:**

A third node animates in to the right of Llama and Mistral — "Qwen 14B" in a warm amber color. It is visibly larger than the other two nodes, reflecting the parameter count difference.

All three nodes now sit in a row: Llama (purple), Mistral (teal), Qwen (amber). Arrows flow from all three down to the triangulator. The triangulator node pulses and its internals briefly show three weight bars — one per model — each at a different level.

A chunk flows through all three. Llama outputs "raised 0.81." Mistral outputs "raised 0.77." Qwen outputs "raised 0.84." The triangulator absorbs all three and outputs "raised 0.86" — boosted by three-way agreement.

A label appears below the architecture: "Multi-model native. Not bolted on."

---

## Beat 3 — Quality Gates

**Duration:** ~12 seconds

**Narration:**

More models means more signals. More signals means more noise. So the pipeline now gates its own input. Chunks that are empty, mostly boilerplate, or too short are rejected before any reader sees them. And on the output side, signals below a minimum confidence threshold are logged for audit but excluded from the scorecard. The system tracks what it is uncertain about without letting that uncertainty pollute its accuracy metrics.

**Visual direction:**

A conveyor belt visual — chunks flowing from left to right toward the reader nodes.

**Input gate (0-6s):**
A gate barrier appears before the readers. Chunks approach. Most pass through. But three chunks are stopped:
- One is greyed out: "EMPTY" stamp, rejected
- One has red highlights: "BOILERPLATE 0.87" stamp, rejected (ratio above 0.8)
- One is tiny: "TOO SHORT" stamp, rejected

The rejected chunks drop off the belt into a "Rejection Log" bin below. The good chunks continue through.

**Output gate (6-12s):**
On the right side, after the triangulator, a second gate appears. Signals pass through. One signal shows confidence 0.31 — it hits the gate, gets tagged "LOW CONFIDENCE," and is diverted into a separate "Audit Log" bin. It is preserved but separated from the scorecard path. A small label: "Logged. Not scored."

---

## Beat 4 — Provenance

**Duration:** ~12 seconds

**Narration:**

Every signal ECIS produces now stores the exact prompt that created it. The system prompt, the few-shot examples it retrieved, the temporal context from prior quarters, and the chunk itself. If a signal looks wrong six months from now, you can rebuild the exact conditions that produced it and re-run the extraction. Same model, same prompt, same answer. Nothing is a black box. Every decision has a receipt.

**Visual direction:**

A single signal card appears center screen — the familiar format from Episode 1: ticker, direction, confidence, supporting quote.

On "stores the exact prompt" — the card flips or expands, revealing layers behind it like a stack of cards or an accordion:

Layer 1: "System Prompt" — a text block preview
Layer 2: "Few-Shot Examples (3)" — three small example cards
Layer 3: "Temporal Context" — a prior-quarter chunk preview
Layer 4: "Source Chunk" — the original transcript text

All four layers are visible in a stacked arrangement behind the signal card. A label appears: "Full provenance. Fully reproducible."

On "Every decision has a receipt" — a small receipt icon stamps onto the card — a visual seal.

---

## Beat 5 — The Dashboard

**Duration:** ~10 seconds

**Narration:**

The dashboard now shows all three models in one view. Calibration curves overlaid on the same chart. Brier scores side by side. Signal counts per model. You can filter by ticker, by model, by confidence range, and drill into any signal to see its full provenance. One screen to see how three models read the same market.

**Visual direction:**

The Episode 2 dashboard returns but upgraded with a third model.

**Calibration curve (0-4s):**
The familiar calibration plot now has three lines drawing against the diagonal:
- Purple (Llama)
- Teal (Mistral)
- Amber (Qwen)

The three lines weave around the diagonal — close but different. Qwen's line tracks slightly closer to the diagonal than the others.

**Bar chart (4-7s):**
The Brier score comparison from Episode 2 now shows three grouped bars instead of two. Purple, teal, amber side by side per metric.

**Signal explorer (7-10s):**
The signal table now has a "Model" column. A filter dropdown appears and selects "Qwen 14B" — the table filters to show only Qwen extractions. One row is tapped, expanding to show the provenance stack from Beat 4.

---

## Beat 6 — Close

**Duration:** ~6 seconds

**Narration:**

Three models. Every input gated. Every signal traceable. ECIS, episode three.

**Visual direction:**

Quick montage — three flashes:

1. **"Three models"** — the triple-node architecture flashes (purple, teal, amber)
2. **"Every input gated"** — the conveyor-belt quality-gate visual from Beat 3 flashes
3. **"Every signal traceable"** — the provenance stack from Beat 4 flashes

Title text lands: **ECIS — Episode 3**

Same sign-off style as Episodes 1 and 2. Fade to Claude-branded outro bookend.

---

## Production Notes

**Total estimated duration:** ~60 seconds of narration + bookends = ~66 seconds total

**Continuity:** Purple for Llama, teal for Mistral (from Ep 2), amber for Qwen (new). Same node shapes, same dark background, same calibration curve style. The viewer should feel the system growing across episodes.

**Voice:** am_onyx, same as Episodes 1 and 2. This episode has a slightly more disciplined tone — the system is maturing, not just expanding.

**Visual mix:** All Remotion. The conveyor belt in Beat 3 and the provenance stack in Beat 4 are the new visual signatures. Beat 2's triple-model node is the evolution of Episode 2's dual-model node.

**Numbers to confirm before audio:**
- "Fourteen billion parameters" — correct for Qwen2.5-14B
- Confidence gating threshold — what is the actual configured value?
- Boilerplate rejection ratio — 0.8 is from the implementation doc, confirm

**Scope note:** this episode covers implementation only — the third model,
the quality gates, and provenance tracking were built and tested this week,
but not yet run across the full 25-company pipeline. No "ran at scale"
claim belongs anywhere in this episode; that's future work, not this week's
result.
