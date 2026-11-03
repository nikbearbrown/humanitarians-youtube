# What Happens Inside a Transformer Layer

**Skill:** ai-explainer
**Voice:** af_bella (Anjana) — source files say `am_onyx`; overridden per the
convention used across this series (Anjana narrates, no channel handle)
**Target length:** ~3:35 (16:9 master) / ~2:40 (9:16 short)
**Register:** Teardown
**Topic:** One token passes through one transformer layer. Four operations —
self-attention, feed-forward, layer norm, residual connection — each shown on
a real-sounding financial sentence.

---

## Beat 0 — The Ask (cold open)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~12s

**Narration:**

Every transformer layer does the same four things in the same order, and
stacking enough of them gives you every modern language model. I'm Anjana —
here's what one token actually sees on its way through one layer.

**Composer ask:**

> I keep hearing that a transformer is "just attention plus a feed-forward
> network," but I've never seen what one layer actually does to a single word.
> Can you walk one token through one layer, step by step?

**Output lines (resolved on screen):**
- attention gathers context
- feed-forward processes it
- residual and layer norm hold it together

---

## Beat 1 — The Hook

**Duration:** ~7s brief / ~15s actual

**Narration:**

A transformer model can have dozens of layers. But every layer does the same
four things in the same order. Self-attention. Feed-forward. Layer norm.
Residual connection. Here is what one token sees as it passes through one
layer.

**Visual direction:**

A vertical stack of identical blocks — Layer 1 through Layer 12. One block in
the middle glows and expands while the rest dim and recede, opening to reveal
an empty interior. A single token enters from the left: the word "revenue"
from the sentence "We expect revenue growth to moderate," a small glowing
block with the word on it. Microscope in.

---

## Beat 2 — Self-Attention

**Duration:** ~13s brief / ~42s actual — the centerpiece

**Narration:**

Step one. Self-attention. The token "revenue" needs to understand its role in
the sentence. It creates three vectors from itself: a query, a key, and a
value. The query asks "what should I pay attention to?" Every other token in
the sentence also has a key. The query compares against every key and computes
a score. High score means high relevance. "Revenue" scores high against
"growth" and "moderate" because they directly affect its meaning. It scores
low against "we" and "to" because they add no context. The scores become
weights. The weighted sum of all values produces a new, context-aware
representation of "revenue." The word has not changed. But now it knows what
surrounds it.

**Visual direction:**

Inside the expanded layer, "revenue" sits center stage with the other five
tokens in a row. Three vectors split out of it — a gold Q ("What should I
attend to?"), a blue K, a green V — and the other tokens show dimmer K and V
vectors of their own. The gold query reaches out to every key and a score
lands on each connection: growth 0.42 (thick, bright), moderate 0.31, expect
0.15, we 0.07, to 0.05 — they sum to 1.0. The value vectors scale by those
weights and flow back into "revenue," which now glows differently. It has
absorbed context.

**Label:** Same word. New meaning. Context-aware.

---

## Beat 3 — Feed-Forward Network

**Duration:** ~10s brief / ~27s actual

**Narration:**

Step two. The feed-forward network. Attention told "revenue" what to look at.
Now the feed-forward network decides what to do with that information. It is
two linear transformations with a non-linearity in between. The vector expands
to a higher dimension, passes through an activation function that introduces
non-linearity, then compresses back down. This is where the model transforms
raw attention patterns into useful features. Attention gathers context. The
feed-forward network processes it.

**Visual direction:**

The context-aware "revenue" vector enters a Feed-Forward Network box as a
narrow color strip. It stretches to four times its width — "Expand: d_model →
4× d_model." It passes through a wave-shaped gate labelled "GELU"; some cells
brighten, others go dark. It compresses back to its original width — same size
as the input, but transformed. The token exits with a subtly different glow.

**Label:** Attention gathers. Feed-forward processes.

---

## Beat 4 — The Glue: Layer Norm and Residual

**Duration:** ~12s brief / ~45s actual

**Narration:**

Two more operations hold everything together. Residual connections. Before
attention and before the feed-forward step, the original input was saved.
After each operation, the original is added back to the result. This means the
model can never completely forget what the token started as. If the layer
learns nothing useful, the residual ensures the token passes through
unchanged. No damage done. Layer normalization runs after each addition. It
rescales the values so they stay in a stable range. Without it, values drift
higher and higher through twelve layers and the model breaks. Residual
connections protect the signal. Layer norm keeps the numbers in check.
Together they are why you can stack twelve, twenty-four, or ninety-six layers
and the model still trains.

**Visual direction:**

A side-view data-flow diagram of the full layer. The token enters from the
left and the path splits: the main path through the attention block, a curved
bypass carrying the original around it. They merge at a "+" node — "Original +
transformed = protected." A brief flash shows the bypass carrying the token
through unchanged when attention learns nothing. Then a Layer Norm box, where
the vector's extreme values visibly settle into a stable range. The same
residual-plus-norm pattern repeats around the feed-forward block, and the full
structure reads: Input → Attention → Add & Norm → Feed-Forward → Add & Norm →
Output.

**Label:** Residual protects the signal. Layer norm keeps the numbers in check.

---

## Beat 5 — The Close

**Duration:** ~7s brief / ~16s actual

**Narration:**

Four operations. Attention gathers context. Feed-forward processes it.
Residual connections protect the signal. Layer norm keeps it stable. Stack
twelve of these and you have BERT. Stack ninety-six and you have GPT. Same
four steps, repeated. That is a transformer.

**Visual direction:**

The expanded layer collapses back into its block and rejoins the stack.
Microscope out. On "twelve," twelve blocks glow — "BERT." On "ninety-six," the
stack extends dramatically — "GPT." The title lands: What Happens Inside a
Transformer Layer / Four operations. One building block. Every modern language
model.

---

## Beat 6 — The Verdict

**Pattern:** `ClaudeVerdictArtifact` · **Duration:** ~24s

**Narration:**

Let's recap with Claude. Attention is the only step where a token looks at the
rest of the sentence — it gathers context, and it does it with a query against
every other token's key. The feed-forward network never looks sideways; it
processes what attention gathered. The residual connection means a layer that
learns nothing does no harm, and layer norm keeps the numbers from drifting as
you stack. Four operations. That is the entire building block.

---

## Beat 7 — Your Turn (handoff)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~40s

**Narration:**

Your turn. "Take the sentence 'We expect revenue growth to moderate' and walk
me through what self-attention would compute for the token 'moderate' instead
of 'revenue' — which other words should it score highest against, and why?
Then tell me honestly: if I stacked twelve of these layers, what does the
twelfth layer know about 'moderate' that the first one didn't, and how would I
even check?" Paste that into Claude and find out whether you can predict what
a layer will pay attention to before it does.

**Why this prompt:** it re-runs the episode's own worked example on a different
token, which is the fastest way to find out whether the mechanism actually
landed — and its last clause asks the honest question the video leaves open.

---

## Beat 8 — Outro

**Pattern:** `ClaudeTitleOutro` · **Duration:** ~5s

**Narration:**

Attention, feed-forward, residual, norm. That's Anjana.

---

## Production Notes

**Total estimated duration:** ~3:35 (16:9). B02 and B04 run long against their
briefs — 115 and 121 words against a 45–70-word range — because the source
narration is dense; kept verbatim, with the evidence carried on screen.

**Voice:** `af_bella` (Anjana). The source `beats.json` and `README.md` say
`am_onyx`; overridden per the series convention.

**Technical accuracy notes (carried from the pre-production script):**
- QKV is shown as single-head attention, not multi-head, for clarity.
- The feed-forward expansion ratio (4×) is the standard for most architectures.
- The activation is labelled GELU; the ReLU/GELU distinction does not matter here.
- Residual connections happen twice per layer (around attention and around
  feed-forward); both are shown.
- Layer norm is placed post-norm (after the add), the original Vaswani
  arrangement. Most modern models use pre-norm; see `PEDAGOGY.md`.

**Delivery:** rendered at 4K in both 16:9 (3840×2160) and 9:16 (2160×3840).

**No company names anywhere** — the running sentence is a generic
illustrative construction, not a transcript quote.
