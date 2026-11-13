# What a Context Window Really Is — Full Script

**Skill:** ai-explainer
**Voice:** af_bella (Anjana) — source `beats.json` says `am_onyx`; overridden per
the series convention (Anjana narrates, no channel handle)
**Target length:** ~2:45 (16:9 master) / same cut in 9:16 
**Register:** Teardown
**Standalone:** third in the loose family with `embeddings-explainer` (what a
vector is) and `vector-db-explainer` (what you do with millions of them). This
one is about the thing all of that has to fit inside.

---

## B00 — The Ask (cold open)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~12s

**Narration:**

Everyone knows the number — 128K, a million, whatever it is this month. Almost
nobody knows what the number is counting, or what it costs, or why the middle of
it is where things go to be forgotten. I'm Anjana.

**Composer ask:**

> Models advertise a context window in tokens. What is actually being measured,
> what does holding it open cost the hardware, and does a bigger number really
> mean the model remembers more?

**Output lines (resolved on screen):**
- tokens, not words — about 75% of the count
- the KV cache is the real bill, paid in VRAM
- open is not the same as recalled

---

## B01 — The Conveyor Belt (13s)

### Narration
Every time you talk to an LLM, it reads everything — your prompt, the conversation history, its own previous answers — all at once, from a fixed-size buffer. That buffer is the context window. Think of it as a conveyor belt: whatever fits on the belt, the model sees. Whatever falls off the end is gone.

### Visual direction
Dark stage. A horizontal conveyor belt stretches across the screen. Text blocks labeled "system prompt," "user message 1," "assistant reply 1," "user message 2" slide onto the belt from the right. The belt has a fixed width. As new blocks arrive, the oldest block on the left falls off the edge and disappears. A glowing bracket above the belt is labeled "context window: 128K tokens." The model, represented by a simple eye icon at the center, watches everything on the belt.

---

## B02 — Tokens, Not Words (12s)

### Narration
But the window isn't measured in words — it's measured in tokens. Tokenizers break text into subword pieces. The word "understanding" might be one token, but "tokenization" becomes three. On average, one token is about three-quarters of a word. So a 128K token window holds roughly 96,000 words — not 128,000.

### Visual direction
Dark stage. The word "understanding" appears, and a single bracket wraps it: "1 token." Below it, "tokenization" appears and splits into three highlighted pieces — "token," "iz," "ation" — each bracketed: "3 tokens." A counter in the corner shows the math: "128,000 tokens x 0.75 = ~96,000 words." A small comparison bar shows 128K labeled "what people assume" next to a shorter 96K bar labeled "what you actually get."

---

## B03 — The KV Cache (13s)

### Narration
Here's the engineering problem. Attention — the mechanism that lets the model relate every token to every other token — scales quadratically. Double the context length, quadruple the computation. The KV cache stores the key and value vectors for tokens already processed, so the model doesn't recompute them on every new token. But that cache lives in GPU memory. A 128K window on a large model can consume tens of gigabytes of VRAM just for the cache.

### Visual direction
Dark stage. A grid appears: rows and columns both labeled with tokens. As the token count doubles from 1K to 2K, the grid quadruples in area — the quadratic scaling made visible. Then the grid compresses into two stacked rectangles labeled "K cache" and "V cache." A GPU memory bar on the right fills up as the context length slider increases. At 128K, the bar is nearly full, with a label: "~40 GB VRAM (KV cache alone)."

---

## B04 — Lost in the Middle (13s)

### Narration
And here's the real catch: a 128K-token window doesn't mean 128K tokens of equal attention. Research shows LLMs attend strongly to the beginning and end of the context, but struggle with information buried in the middle. It's called the "lost in the middle" effect. The window is technically open, but recall degrades. Position matters as much as presence.

### Visual direction
Dark stage. A long horizontal bar represents the full context window. The bar is colored by attention intensity: bright blue at the left edge (beginning), fading to dim grey in the middle, then brightening back to blue at the right edge (end). This creates a U-shaped attention curve shown above the bar. A drops into the middle of the bar, trying to retrieve a fact — it comes up empty, with a small "?" floating above it. The label reads: "lost in the middle."

---

## B05 — Working Around It (12s)

### Narration
So how do you work within these limits? Three strategies. Chunking: break long documents into pieces that fit. Summarization: compress prior conversation into a shorter recap. And RAG — retrieval-augmented generation — where you search a knowledge base only the relevant pieces into the window. The context window is a budget. Spend it on what matters.

### Visual direction
Dark stage. Three columns appear. Left: a long document splits into smaller chunks, each sliding onto the conveyor belt from B01. Center: a tall stack of conversation text compresses into a small summary block. Right: a search icon queries a database, and only two relevant snippets fly into the context window. Below all three, the conveyor belt reappears — now efficiently loaded with chunks, summaries, and retrieved snippets, all fitting within the glowing bracket. Final text fades in: "The context window is a budget. Spend it on what matters." Fade to dark.

---

## B06 — Verdict

**Pattern:** `ClaudeVerdictArtifact` · **Duration:** ~24s

**Narration:**

Let's recap with Claude. The window is a buffer measured in tokens, so the
advertised number is about a quarter larger than the words you actually get.
Holding it open is not free — attention cost grows with the square of the
length, and the cache that avoids recomputing it is paid for in gigabytes of
GPU memory. And a window being open is not the same as the model recalling what
is in it: the middle is where things get lost. Treat it as a budget.

**Artifact lines:**
- The window is a fixed buffer measured in *tokens* — roughly 0.75 words each.
- Attention scales quadratically with length; the KV cache trades recomputation
  for VRAM, and at long contexts that bill is tens of gigabytes.
- Recall is not uniform — the beginning and end of the context are attended to
  far more strongly than the middle.
- Chunking, summarization and retrieval all exist to spend a fixed budget on
  what matters.

---

## B07 — Your Turn

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~30s

**Narration:**

Your turn. Take the longest prompt you regularly send a model and look at what
is actually in it. How much of it is there because it earns its place, and how
much because it was easier to paste everything. Then ask what you would put at
the very start and the very end, if you knew the middle was the part least
likely to be read.

**Composer ask:**

> I regularly send a model a long prompt — documents, history, instructions,
> examples. Can you help me: one, work out which parts of it are actually
> earning their place and which are there because pasting everything was
> easier; two, decide what belongs at the very beginning and the very end,
> given that the middle is the part least likely to be recalled; and three,
> tell me honestly whether I should be chunking, summarizing or retrieving
> instead of growing the prompt — and which one fits my case?

---

## B08 — Title outro

**Pattern:** `ClaudeTitleOutro` · **Duration:** ~5s

**Narration:**

Anjana here, thanks for watching.

**Title:** What a Context Window Really Is
**Subline:** a budget, not a memory
**Handle:** (none)
