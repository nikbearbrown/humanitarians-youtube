# How KV Cache Works — script (final, as shot)

Channel claude-hai · Persona Simba · Register Pragmatist · Voice Kokoro `af_bella`
16:9 long cut: 4:24 (264.3s) · 9:16 Shorts: 1:04 (64.2s)

Timestamps and durations are Kokoro-measured from the locked audio, not estimates — this is exactly what's spoken in the final render. Pre-production shot notes, on-screen prop text, and build rationale live in `SCRIPT-kv-cache.md`; this file is narration only, dated to the finished cuts.

## 16:9 — long cut

### B00 · INTRO (0:00–0:18)
> Hi, I am Simba. Every time a language model writes the next word, it has to look back at everything it already wrote. So why doesn't generating the ten-thousandth token take ten thousand times longer than the first? The answer is a cache — and it's one of the simplest ideas in modern inference.

### B01 · SUMMARY (0:18–0:32)
> Here's the idea. Once a token's Key and Value are computed, they never change again. So instead of recomputing them every step, you compute each one exactly once, cache it, and reuse it for every token that comes after.

### B02 · STRUCTURE (0:32–0:56)
> Every token, at every layer, produces three vectors: a Query, a Key, and a Value. The Query is what this token is looking for. The Key is what every other token offers to be matched against. The Value is what actually gets pulled forward if that match is strong. And because generation is causal, token five can only ever attend to tokens one through five — never anything after it.

### B03 · PROBLEM (0:56–1:15)
> Done naively, generating the next token means running the entire sequence back through the model — recomputing the Key and Value for every earlier token, all over again. But those earlier tokens haven't changed. Their Keys and Values are exactly what they were last step. You'd be redoing work whose answer you already have.

### B04 · STRUCTURE (1:15–1:33)
> So the fix is a cache: one Key list and one Value list, per layer, per attention head. The first time a token is processed, its Key and Value get computed and appended. They sit there, untouched, for the rest of generation — because a causal model never needs to revisit them.

### B05 · RESULTS (1:33–1:55)
> So here's what one real generation step does. Compute Query, Key, and Value for the one new token — nothing else. Append its Key and Value onto the cache. Then let its Query attend across everything in the cache, old and new, to decide what comes next. Every step after the first does the same small amount of new work, no matter how long the sequence has gotten.

### B06 · REASONING (1:55–2:27)
> To be precise about what this buys you: the heavy matrix multiplies — the projections, the feedforward layers — drop from work that grows with the whole sequence, every step, to a fixed, small amount, every step. What doesn't go away is the attention calculation itself — comparing the new Query against a cache that keeps growing is still more work at token ten thousand than at token ten. The cache removes the redundant recomputation. It doesn't repeal the fact that a longer cache means more to look through.

### B07 · REASONING (2:27–2:51)
> But that cache has to live somewhere, for as long as generation runs — every layer, every attention head, both the Keys and the Values, all held in memory at once. The longer the conversation, the bigger the cache. This isn't a free lunch — it's a trade. You've converted repeated compute into standing memory, and on a long enough context, that memory bill becomes the thing you're actually rationing.

### B08 · FINDINGS (2:51–3:32)
> Because that memory bill is real, serving systems attack it directly. Grouped-query attention shares Key and Value heads across several Query heads, shrinking the cache without changing what each token can attend to as freely. Sliding-window caching just stops keeping tokens past a fixed distance back. Quantizing the cache stores each Key and Value in fewer bits. And PagedAttention — the technique behind vLLM — manages the cache in fixed-size pages instead of one long block, so a server handling many requests at once doesn't waste memory to fragmentation. Different levers, same target: the standing cost this trade created.

### B09 · SUMMARY (3:32–4:04)
> So: KV caching is what makes long, fast generation possible at all — without it, a long conversation would get slower with every single word. What it costs in return is memory, growing the whole time generation runs. And it's worth saying plainly what it doesn't fix: attention itself still does more work the longer the cache gets. The cache solves the redundant-recomputation problem. It was never a fix for attention's own growth — that's a different problem, with its own different solutions.

### B10 · NEXT STEPS (4:04–4:20)
> Your turn. Next time you're running or serving a model with a long context window, work out what its KV cache actually costs in memory at that length — and whether grouped-query attention, a sliding window, or a quantized cache would buy that memory back.

### B11 · OUTRO (4:20–4:24)
> How KV cache works. Simba, for Humanitarians AI.

## 9:16 — Shorts cut

### B00 · INTRO (0:00–0:13)
> Hi, I am Simba. Why doesn't generating token ten thousand take ten thousand times longer than token one? Because a model never recomputes a token's Key and Value once they're cached — it just reuses them.

### B01 · SUMMARY (0:13–0:24)
> Once a token's Key and Value are computed, they never change again. So cache them once, and reuse them for every token after — instead of recomputing them every single step.

### B02 · RESULTS (0:24–0:41)
> Here's one real decode step. Compute Query, Key, and Value for the new token only. Append its Key and Value to the cache. Then attend across everything in the cache, old and new, to produce the next token. Every step after the first does the same small amount of work.

### B03 · SUMMARY (0:41–0:58)
> KV caching is what makes long, fast generation possible — without it, a conversation would get slower with every word. What it costs is memory, growing the whole time generation runs. And it doesn't fix attention's own growth — that's a different problem.

### B04 · OUTRO (0:58–1:04)
> Full build, with the memory trade-offs, is on the channel. Simba, for Humanitarians AI.

---

This script covers general transformer-inference mechanics, not a proprietary or sprint-specific result — no source report to fact-check against. Kept deliberately qualitative on the memory-growth numbers (B07's "×" values are relative illustration, not a claimed real figure) rather than inventing a precise size or speedup, per `SCRIPT-kv-cache.md`'s own build notes.
