# What Happens When You Teach BERT to Read Financial Statements

**Skill:** ai-explainer
**Target length:** ~60 seconds
**Voice:** am_onyx (Onyx)
**Style:** Technical but accessible. The viewer knows what AI is but not what BERT is. Explain by showing, not lecturing.

---

## Beat 1 — The Hook

**Duration:** ~8 seconds

**Narration:**

BERT is one of the most widely used language models in the world. It reads text and understands context. But hand it an earnings call, and it gets confused. Financial language does not work like normal English.

**Visual direction:**

The word "BERT" appears center screen in bold. Below it, a subtitle: "Bidirectional Encoder Representations from Transformers." The subtitle fades to a simpler label: "A language model that reads context."

A short sentence appears: "The market reacted positively." BERT processes it — a green "POSITIVE" tag appears. Clean, correct, easy.

Then a second sentence replaces it: "Revenue missed estimates by a narrow margin." BERT tags it "POSITIVE" — wrong. A red "X" stamps over the tag. The model got it wrong because it read "narrow margin" as a positive phrase.

---

## Beat 2 — Where General NLP Gets It Wrong

**Duration:** ~12 seconds

**Narration:**

In everyday language, "exceeded expectations" is positive and "significant loss" is negative. Straightforward. But in finance, "beat estimates by a narrow margin" is cautious. "Headwinds" is not about weather. "Adjusted" usually means something was removed to make the numbers look better. The same words carry different weight when money is on the line.

**Visual direction:**

Three example pairs appear one at a time, each showing the same phrase with two interpretations:

Pair 1:
- General English: "beat estimates" → ✅ Positive
- Financial context: "beat estimates by a narrow margin" → ⚠️ Cautious

Pair 2:
- General English: "headwinds" → 😕 Unclear / weather
- Financial context: "headwinds" → 🔴 Risk warning

Pair 3:
- General English: "adjusted results" → ✅ Sounds improved
- Financial context: "adjusted results" → ⚠️ Non-GAAP, items removed

Each pair appears with a split — general meaning on the left (green), financial meaning on the right (amber or red). The gap between the two columns is the problem.

---

## Beat 3 — The Fine-Tuning

**Duration:** ~15 seconds

**Narration:**

FinBERT takes the original BERT model and fine-tunes it on fifty thousand financial sentences from earnings calls, analyst reports, and financial news. The architecture stays the same. The weights change. The model learns that "decline" next to "revenue" is negative, but "decline" next to "expenses" is positive. It learns that "in line with expectations" is neutral, not positive. It learns the difference between what words mean in general and what they mean when money is involved.

**Visual direction:**

A simplified neural network diagram. The BERT architecture is drawn as a stack of layers — embedding layer at the bottom, transformer blocks in the middle, classification head at the top.

On "fine-tunes it on fifty thousand financial sentences" — a stream of text fragments flows into the bottom of the network. The text looks like real financial language: "revenue growth," "margin compression," "forward guidance," "operating leverage."

The transformer layers pulse as data flows through — the weights are updating. Color shifts subtly from a neutral grey to a warm gold, conveying that the model is being reshaped.

On "decline next to revenue is negative, but decline next to expenses is positive" — two small examples animate beside the network:
- "revenue decline" → red arrow down
- "expense decline" → green arrow up

Same word, opposite meaning. The model now knows.

---

## Beat 4 — Inside the Model

**Duration:** ~15 seconds

**Narration:**

Here is what happens when FinBERT reads a sentence. The text is split into tokens. Each token gets an embedding, a vector that captures its meaning. The transformer layers process these embeddings in parallel, and every token attends to every other token. That is the key. FinBERT does not read left to right. It sees the whole sentence at once. The classification head at the top outputs three probabilities: positive, negative, neutral. One sentence in, three numbers out, in about ten milliseconds.

**Visual direction:**

A real earnings call sentence enters from the left: "We expect moderate growth in the second half."

**Tokenization (0-3s):** The sentence splits into tokens — each word becomes a separate block: [We] [expect] [moderate] [growth] [in] [the] [second] [half]. The blocks separate and arrange in a row.

**Embeddings (3-5s):** Each block transforms into a colored vector bar — a vertical strip of color representing its embedding. Different words get different color patterns.

**Attention (5-10s):** Lines draw between every token and every other token — a web of attention connections. Some lines are thick (strong attention), others thin. "Moderate" connects strongly to "growth." "Expect" connects to "second half." The model is reading context, not words.

**Classification (10-13s):** The attention web funnels upward into the classification head. Three bars appear at the top:
- Positive: 0.24
- Negative: 0.11
- Neutral: 0.65

The "Neutral" bar is longest and glows — FinBERT correctly reads "moderate growth" as a measured, neutral statement.

**Speed tag (13-15s):** A small clock icon appears: "10ms" — this whole process took ten milliseconds.

---

## Beat 5 — The Close

**Duration:** ~7 seconds

**Narration:**

Same architecture. Different training data. Different understanding. That is what happens when you teach BERT to read financial statements. It stops reading words. It starts reading money.

**Visual direction:**

Split screen. Left: the original BERT label with a general text icon. Right: FinBERT label with a financial document icon. A transformation arrow connects them.

On "It stops reading words. It starts reading money." — the left side fades to black. The right side grows to fill the screen. Title text lands: "FinBERT — BERT, Fine-Tuned for Finance."

Fade to Claude-branded outro bookend.

---

## Production Notes

**Total estimated duration:** ~57 seconds of narration + bookends = ~63 seconds total

**Voice:** am_onyx — clear and measured. This script is more educational than the ECIS videos. Slower pacing on Beat 4 (the inside-the-model walkthrough) helps the viewer follow the visual.

**Visual mix:** All Remotion. Beat 3 (fine-tuning) and Beat 4 (inside the model) are the visual centerpieces. The attention web in Beat 4 is the signature moment — it should feel precise and alive, like watching a brain think.

**Tone:** Not hype, not fear. Just: here is a tool, here is what it does, here is why it matters. The viewer should walk away understanding what FinBERT is and why financial NLP needs specialized models.
