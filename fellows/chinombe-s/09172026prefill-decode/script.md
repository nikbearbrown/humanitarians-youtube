# Prefill vs. Decode — Final Script (as produced)

*claude-hai · Simba · 4:02 · 16:9*

**[0:00 B00 — INTRO]**
> Hi, I am Simba. Every time a language model answers you, it's actually doing two completely different jobs. First it reads your entire prompt, all at once. Then it writes the reply, one word at a time. Those two jobs load the GPU in opposite ways — and mixing them badly is one of the biggest reasons a server ends up slow.

**[0:21 B01 — SUMMARY]**
> Prefill reads your whole prompt in a single parallel pass across every input token. Decode writes the reply one token at a time, each one waiting on the last. Same model, same GPU — two completely different kinds of work.

**[0:36 B02 — STRUCTURE]** *(diagram: `ParallelPass`)*
> Prefill looks at every token in your prompt at the same time — a hundred tokens or a thousand, it's one forward pass either way, computed as one big matrix multiplication. Every input token feeds into that single pass at once, and it fans back out into two things: a KV cache entry for every token, and the first token of the reply.

**[0:58 B03 — REASONING]**
> That shape is what decides the bottleneck. Prefill multiplies a big batch of tokens against the same weights at once — lots of math per byte of memory it touches, so the GPU's compute cores stay busy. Decode does the opposite: one token's worth of math, but it still has to pull in every model weight and the entire key-value cache from memory to do it. Almost nothing to compute, a lot to read. That's why prefill is called compute-bound, and decode is called memory-bound.

**[1:29 B04 — STRUCTURE]** *(diagram: `AutoregressiveLoop`)*
> Decode's loop never changes shape: take the last token and the cache built so far, run one forward pass, get the next token out, append it to the cache, and do it again. Every step depends on the step before it — there's no way to skip ahead or run two steps at once for the same reply. And the cache it reads from grows by exactly one block, every single time around.

**[1:52 B05 — RESULTS]**
> Servers measure these two phases separately. Time to first token is how long prefill takes — it grows with how long your prompt is. Time per output token is how long each decode step takes — it barely changes with prompt length, but it's set by how much has to be read from memory every single step.

**[2:11 B06 — REASONING]**
> Put both phases on the same GPU without care, and they fight. A big prefill batch can hog the GPU for the time it takes to finish, and every decode step waiting behind it in the queue stalls until it's done — a new prompt showing up mid-conversation can freeze everyone else's reply. That's not a bug in one phase — it's the two bottlenecks colliding.

**[2:33 B07 — FINDINGS]**
> One fix keeps them on the same GPU, but schedules around the collision. Sarathi-Serve splits a big prefill into small chunks, and slots each chunk between ongoing decode steps instead of running it all at once. No decode ever waits for a whole prefill to clear — and that alone bought two-point-six to five-point-six times the serving capacity of vLLM, depending on the model.

**[2:57 B08 — FINDINGS]**
> The other fix doesn't share the GPU at all. DistServe runs prefill and decode on separate pools of GPUs entirely, each one tuned to its own bottleneck instead of splitting one GPU's time between two different jobs. Against the same latency bar, that served seven-point-four times more requests, while hitting a twelve-point-six times tighter deadline on over ninety percent of them.

**[3:21 B09 — SUMMARY / VERDICT]**
> So: every reply is two jobs, not one. Prefill reads your prompt in one compute-bound pass; decode writes the reply memory-bound, one token at a time. Left alone on shared hardware, they collide — and two different fixes, chunking the prefill or splitting the GPUs entirely, both turn that collision into serving capacity, because they stopped treating one bottleneck like the other.

**[3:46 B10 — NEXT STEPS]**
> Your turn. If your own serving stack feels slow, check which clock is actually stuck — time to first token, or time per output token. The fix for one is not the fix for the other.

**[3:57 B11 — OUTRO]**
> Prefill versus decode. Simba, for Humanitarians AI.

---
## Sources
- Agrawal et al., "Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve," OSDI 2024. [arXiv:2403.02310](https://arxiv.org/abs/2403.02310)
- Zhong et al., "DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving," OSDI 2024. [arXiv:2401.09670](https://arxiv.org/abs/2401.09670)
