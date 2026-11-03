# Beat 4 — Inside the Model

**Visual type:** Remotion
**Duration:** ~15 seconds

## What the viewer sees

A real sentence enters from the left: "We expect moderate growth in the second half."

**Tokenization (0-3s):**
The sentence breaks apart into individual tokens, each becoming a separate rounded block:
[We] [expect] [moderate] [growth] [in] [the] [second] [half]

The blocks separate and arrange in a horizontal row with small gaps. Each block has a slightly different background shade.

**Embeddings (3-5s):**
Each token block transforms — morphing from a word label into a vertical color strip (a visual representation of its embedding vector). Different words get different color patterns. "Moderate" gets a mixed amber/green pattern. "Growth" gets a bright green. "Expect" gets a neutral blue.

**Attention (5-10s):**
Lines draw between every token and every other token — a web of connections. The line thickness varies:
- Strong connection: "moderate" ↔ "growth" (thick line — the model links these)
- Strong connection: "expect" ↔ "second half" (thick line — temporal context)
- Weak connections: "in" ↔ "the" (thin, nearly invisible)

The web should feel alive — like a brain making connections. Not every line is equal. The model is weighing what matters.

A small label appears: "Bidirectional — every token sees every other token"

**Classification (10-13s):**
The attention web funnels upward into a classification head node. Below it, three horizontal bars grow from left to right:
- Positive: 0.24 (short, blue)
- Negative: 0.11 (shortest, red)
- **Neutral: 0.65** (longest, gold, glows)

The "Neutral" bar is clearly dominant. FinBERT correctly reads "moderate growth" as measured and neutral — not enthusiastically positive.

**Speed (13-15s):**
A small stopwatch icon appears in the corner: "10ms." This whole process — tokenize, embed, attend, classify — took ten milliseconds.

## Technical notes

- The tokenization step should feel physical — the sentence breaking apart like letter tiles
- Embeddings as color strips is a metaphor, not a literal visualization — keep it abstract and pretty
- The attention web is the visual centerpiece — spend time making it feel alive and organic
- Line thickness in the attention web conveys importance — don't make all lines equal
- The three probability bars at the top should be clear and readable
- The 10ms speed tag is a wow moment — make it snappy
