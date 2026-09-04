# How KV Cache Works — script

**Format** `ai-explainer` (16:9) · **Channel** claude-hai · **Register** Pragmatist
**Persona** Simba · **Voice** Kokoro `af_bella` · **Slug** `how-kv-cache-works`
**Runtime** ~3:40 (11 beats, estimated at Kokoro's measured ~3.6 words/sec — audio generation sets the real clock)

---

## The one idea

> A token's Key and Value vectors, once computed, never change again — causal masking guarantees
> that. So instead of recomputing every past token's Key and Value at every generation step, you
> compute each one exactly once and cache it. That turns the expensive part of decoding from
> quadratic to linear, at the cost of memory that grows with every token you generate.

**Every claim in this script is standard transformer-inference mechanics** — the same math behind
`transformers`, vLLM, and every other autoregressive LLM serving stack. No numbers are invented to
fill a beat; where a figure would need a specific model or hardware to be exact (cache size in GB,
speedup factor), the script stays qualitative rather than inventing false precision.

---

## Beat sheet

### B00 · INTRO — cold open
`ClaudeComposerAsk` · ~18s

**On screen**
- Greeting types in: `Hi, Simba` · terracotta spark
- Composer holds the ask, send button arms
- `walking the cache…` then output lines land — the ask arrives already answered

```
topic:    INFERENCE · WHY GENERATION DOESN'T SLOW DOWN
segment:  How KV Cache Works
command:  "A model generates token 1 fast. Why is token 10,000 not 10,000 times
           slower — when it has to attend to every token before it?"
output:   → because it never recomputes those tokens' Keys and Values
          → it just caches them, once, and reuses them forever
folder:   @HumanitariansAI
```

**Narration**
> Hi, I am Simba. Every time a language model writes the next word, it has to look back at
> everything it already wrote. So why doesn't generating the ten-thousandth token take ten
> thousand times longer than the first? The answer is a cache — and it's one of the simplest ideas
> in modern inference.

---

### B01 · SUMMARY — BLUF
`ClaudeStatement` · ~14s

**On screen**
- Single sentence sets, terracotta underline settles beneath it

**Narration**
> Here's the idea. Once a token's Key and Value are computed, they never change again. So instead
> of recomputing them every step, you compute each one exactly once, cache it, and reuse it for
> every token that comes after.

---

### B02 · STRUCTURE — what attention actually needs
Custom scene — needs building · ~22s

**On screen**
- One token's hidden state splits into three vectors: Query, Key, Value — each its own small
  matrix multiply
- Query asks "what am I looking for," Key answers "what do I contain," Value answers "what do I
  hand over if you attend to me"
- A causal mask draws in: token 5 can see tokens 1 through 5, never token 6

**Narration**
> Every token, at every layer, produces three vectors: a Query, a Key, and a Value. The Query is
> what this token is looking for. The Key is what every other token offers to be matched against.
> The Value is what actually gets pulled forward if that match is strong. And because generation is
> causal, token five can only ever attend to tokens one through five — never anything after it.

---

### B03 · PROBLEM — the naive way is wasteful
Custom scene — needs building · ~24s

**On screen**
- Token-by-token generation shown naively: at every new step, the WHOLE sequence gets pushed back
  through every layer — Keys and Values for tokens 1 through N all recomputed, again
- A growing redundant-work bar chart: step 1 redoes 1 token's projections, step 1000 redoes 1000
  tokens' projections that were already computed 999 times before

**Narration**
> Done naively, generating the next token means running the entire sequence back through the model
> — recomputing the Key and Value for every earlier token, all over again. But those earlier
> tokens haven't changed. Their Keys and Values are exactly what they were last step. You'd be
> redoing work whose answer you already have.

---

### B04 · STRUCTURE — what the cache actually holds
Custom scene — needs building · ~20s

**On screen**
- A cache box per layer, per attention head: two growing lists, Keys and Values, one entry added
  per generated token
- The cache visibly only ever appends — never rewrites an old entry

**Narration**
> So the fix is a cache: one Key list and one Value list, per layer, per attention head. The first
> time a token is processed, its Key and Value get computed and appended. They sit there,
> untouched, for the rest of generation — because a causal model never needs to revisit them.

---

### B05 · RESULTS — the actual step
Custom scene — needs building · ~24s

**On screen**
- A single new token arrives: only ITS Query, Key, and Value get computed fresh
- Its new Key and Value append to the cache
- Its Query attends across the WHOLE cache — old and new — to produce the next output

**Narration**
> So here's what one real generation step does. Compute Query, Key, and Value for the one new
> token — nothing else. Append its Key and Value onto the cache. Then let its Query attend across
> everything in the cache, old and new, to decide what comes next. Every step after the first does
> the same small amount of new work, no matter how long the sequence has gotten.

---

### B06 · REASONING — what actually gets cheaper
Custom scene — needs building · ~26s

**On screen**
- Two cost lines drawn side by side: "projections + feedforward, per step" (flat, small, same at
  step 1 and step 10,000) vs. "attention score against the cache" (grows with sequence length,
  because there's more to attend to)
- Caption: caching removes the redundant matrix multiplies; it does not remove attention's own
  growth

**Narration**
> To be precise about what this buys you: the heavy matrix multiplies — the projections, the
> feedforward layers — drop from work that grows with the whole sequence, every step, to a fixed,
> small amount, every step. What doesn't go away is the attention calculation itself — comparing
> the new Query against a cache that keeps growing is still more work at token ten thousand than at
> token ten. The cache removes the redundant recomputation. It doesn't repeal the fact that a
> longer cache means more to look through.

---

### B07 · REASONING — the price is memory, not compute
Custom scene — needs building · ~24s

**On screen**
- A memory bar that grows with every generated token — every layer, every head, both Key and
  Value, all held live in GPU memory for as long as generation continues
- Caption: this is a straight trade — recomputation cost is gone, and it's been converted into a
  standing memory cost instead

**Narration**
> But that cache has to live somewhere, for as long as generation runs — every layer, every
> attention head, both the Keys and the Values, all held in memory at once. The longer the
> conversation, the bigger the cache. This isn't a free lunch — it's a trade. You've converted
> repeated compute into standing memory, and on a long enough context, that memory bill becomes the
> thing you're actually rationing.

---

### B08 · FINDINGS — how serving systems shrink the bill
Custom scene — needs building · ~26s

**On screen**
- A short list of real, named techniques, each with its one-line mechanism: Multi-Query and
  Grouped-Query Attention (share Key/Value heads across multiple Query heads, so there's less
  cache per token) · sliding-window caching (only keep the most recent window, drop the rest) ·
  quantized cache (store Keys and Values in fewer bits) · PagedAttention (manage the cache like
  paged virtual memory instead of one long contiguous block, so serving many requests at once
  doesn't waste space to fragmentation)

**Narration**
> Because that memory bill is real, serving systems attack it directly. Grouped-query attention
> shares Key and Value heads across several Query heads, shrinking the cache without changing what
> each token can attend to as freely. Sliding-window caching just stops keeping tokens past a fixed
> distance back. Quantizing the cache stores each Key and Value in fewer bits. And PagedAttention —
> the technique behind vLLM — manages the cache in fixed-size pages instead of one long block, so a
> server handling many requests at once doesn't waste memory to fragmentation. Different levers,
> same target: the standing cost this trade created.

---

### B09 · VERDICT — the trade, stated plainly
`ClaudeVerdictArtifact` · ~18s

**On screen**
- Artifact page, lines stagger in

```
title:    How KV Cache Works
heading:  What it buys you, what it costs
lines:
  · Buys: decoding cost per token stays flat instead of growing with the whole sequence.
  · Costs: a standing memory footprint that grows with every token you keep alive.
  · NOT solved by caching alone: attention's own per-step cost still grows with context length.
```

**Narration**
> So: KV caching is what makes long, fast generation possible at all — without it, a long
> conversation would get slower with every single word. What it costs in return is memory, growing
> the whole time generation runs. And it's worth saying plainly what it doesn't fix: attention
> itself still does more work the longer the cache gets. The cache solves the redundant-recomputation
> problem. It was never a fix for attention's own growth — that's a different problem, with its own
> different solutions.

---

### B10 · NEXT STEPS — handoff
`ClaudeComposerAsk`, greeting `Your turn.` · ~16s

**On screen**
- Composer, empty, greeting `Your turn.`
- The prompt types in as it's read aloud

```
command: "Next time you're running or serving a model with a long context window,
          check what its KV cache actually costs in memory at that length — and
          whether GQA, a sliding window, or a quantized cache would buy that
          memory back."
```

**Narration**
> Your turn. Next time you're running or serving a model with a long context window, work out what
> its KV cache actually costs in memory at that length — and whether grouped-query attention, a
> sliding window, or a quantized cache would buy that memory back.

---

### B11 · OUTRO
`ClaudeTitleOutro` · ~5s

**On screen**
- Poster serif title, terracotta period · handle beneath

```
title:    How KV Cache Works
handle:   @HumanitariansAI
subline:  cache once · attend forever
```

**Narration**
> How KV cache works. Simba, for Humanitarians AI.

---

## Build notes

**GATE L not yet run.** This is the script-writing pass only — no scene search or component
authoring has happened. B02–B08 are marked "Custom scene — needs building"; check the existing
Remotion component library before authoring from scratch, same discipline as every reel before
this one. B00, B10 → `ClaudeComposerAsk` · B01 → `ClaudeStatement` · B09 → `ClaudeVerdictArtifact`
· B11 → `ClaudeTitleOutro` are all house patterns and renderable today.

**No sprint report backs this one — it's general technical content.** Every mechanism described
(Query/Key/Value projections, causal masking, the cache-append step, GQA, sliding-window caching,
quantized caches, PagedAttention/vLLM) is standard, widely published transformer-inference
mechanics, not a claim sourced from a specific benchmark or team. Deliberately kept qualitative
rather than quoting specific speedup or memory-size numbers, since no particular model or hardware
config was measured for this script — inventing a precise figure here would violate the same
DOUBLE-CHECK discipline this project applies to sprint-report numbers, just with "the published
literature" standing in for "the source report."

**No 9:16 cut drafted.** Wasn't asked for. If a Short gets made, THE SHORTS LAW applies the same
way it has for every other reel: single cycle, no revision — likely B00 → B01 → B05 (the actual
step) → B09 (verdict) → B11.

**Duration.** The estimates above are arithmetic (word count ÷ Kokoro's measured rate), not
measurement. Generate audio first and let it set the real clock, same as always.
