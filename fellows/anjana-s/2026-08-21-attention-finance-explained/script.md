# Attention Is All You Need (To Read an Earnings Call)

**Skill:** ai-explainer
**Target length:** ~63 seconds
**Voice:** am_onyx (Onyx)
**Style:** Technical but accessible. The viewer has heard "attention" and "transformer" as buzzwords but not seen the mechanism itself. Explain by showing one sentence read two different ways.

---

## Beat 1 — The Hook

**Duration:** ~8 seconds

**Narration:**

A CEO says "We expect revenue to remain broadly in line with prior guidance despite near-term headwinds." That is twenty words. A human reads it in three seconds. But which word matters most? It depends on which other words are in the sentence. That is attention.

**Visual direction:**

The full sentence appears on a dark background, centered, as separate word blocks — evenly spaced, neutral white/grey, no highlights. On "which word matters most?" a question mark floats above the sentence. On "That is attention," a soft brightness pulse ripples across all the words simultaneously — not highlighting any one word, just signaling a new way of reading is coming.

---

## Beat 2 — The Old Way

**Duration:** ~12 seconds

**Narration:**

Older models read left to right. One word at a time, in order. By the time the model reaches "headwinds" at the end, it has already decided how to feel about "revenue" at the beginning. It cannot go back. So a sentence that starts positive and ends cautious gets classified as positive, because the model made up its mind too early.

**Visual direction:**

Same sentence, same word blocks. A glowing cursor moves left to right, coloring words as it passes: "revenue," "broadly in line," "with prior guidance" turn green (positive signal); a verdict bar above the sentence fills green, "POSITIVE," well before the cursor reaches the end. "despite" turns amber, "near-term headwinds" turns amber/red — but the verdict bar is already mostly filled and doesn't move much. The verdict locks in "POSITIVE ✓," then a red ✗ stamps over it. Label: "Left-to-right. Made up its mind too early."

---

## Beat 3 — Attention

**Duration:** ~15 seconds

**Narration:**

A transformer does not read left to right. It reads everything at once. Every word looks at every other word and asks one question: how much do you matter to me? "Revenue" looks at "headwinds" and increases its attention. "Broadly" looks at "in line" and locks on. "Despite" looks at everything before it and reweighs the whole sentence. This is self-attention. Every word has context from every other word before any decision is made.

**Visual direction:**

Same word blocks, reset to neutral. "Revenue" glows and thin lines fan out to every other word; two lines glow thick — "revenue"↔"headwinds" (a long connection spanning the full sentence) and "revenue"↔"in line." Then "despite" glows and its own thick lines radiate to "revenue," "guidance," "headwinds" — visually reweighing the sentence, pulling meaning away from the positive start. All words then activate at once: a dense, organic mesh of connections, some thick, some faint — labeled "Self-attention. Every word sees every word." The web funnels into a verdict bar that fills amber, "NEUTRAL / CAUTIOUS," with a green ✓.

---

## Beat 4 — Why Finance Needs This

**Duration:** ~15 seconds

**Narration:**

Financial language is built to be ambiguous. CEOs hedge. Lawyers soften. Analysts qualify. A single sentence can start with optimism, pivot on "however," and land on caution, all in twenty words. Without attention, the model reads the optimism and stops. With attention, the model sees that "however" reweighs everything before it. That is why attention changed financial NLP. Not more data. Not bigger models. The ability to see the whole sentence at once and understand that the last word can change the meaning of the first.

**Visual direction:**

Three rapid-fire examples, ~5 seconds each, same template: sentence appears, one key attention line draws through the pivot word (which glows amber), then a split verdict compares "without attention" (green, wrong ✗) against "with attention" (amber, correct ✓).
1. "We delivered strong results but expect moderation going forward." — line: "strong"↔"moderation" through "but."
2. "Margins improved sequentially although headcount reductions contributed significantly." — line: "improved"↔"reductions" through "although."
3. "Revenue grew twelve percent excluding the impact of foreign currency fluctuations." — line: "grew"↔"excluding."

Rhythm accelerates slightly; example 3 resolves fastest.

---

## Beat 5 — The Close

**Duration:** ~7 seconds

**Narration:**

One idea. Every word sees every other word before any decision is made. That is attention. And it is all you need to read an earnings call.

**Visual direction:**

The Beat 1 sentence returns with the full attention web from Beat 3 visible, pulsing gently. On "That is attention," the web pulses once, brightly. On "it is all you need to read an earnings call," the sentence and web dissolve together into the title:

**Attention Is All You Need**
*(To Read an Earnings Call)*

A parenthetical riff on the 2017 paper title. Fade to Claude-branded outro bookend.

---

## Production Notes

**Total estimated duration:** ~57 seconds of narration + bookends = ~63 seconds total

**Voice:** am_onyx — clear and measured, matching the FinBERT reel's register. This is a companion piece: same NLP-internals territory, different single idea (the mechanism, not the fine-tuning).

**Visual mix:** All Remotion. The attention-web sequence in Beat 3 is the signature visual and reappears in Beat 5's close — build it once, reuse the asset. Beat 4's three rapid-fire examples are the payoff: the same mechanism, applied three times fast.

**Tone:** One idea, landed hard. No invented company names or tickers — every example sentence is a generic, illustrative CEO-speak construction, not a real transcript quote.
