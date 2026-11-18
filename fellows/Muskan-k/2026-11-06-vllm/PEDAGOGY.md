# PEDAGOGY — vLLM (claude-hai · AI, Explained · ~2.5min)

**Genre:** concept explainer (framework-first, built to pass PROOF). Topic named by
request: vLLM / efficient LLM inference and serving.

**The ONE reusable idea (throughline/verdict):** LLM serving is **memory-bound**, not
compute-bound — the **KV cache** fills the GPU and caps throughput — and vLLM wins by
**treating the KV cache like an OS treats RAM**: *PagedAttention* (page it into
fixed-size blocks, allocate on demand, share) + *continuous batching* (swap requests in
and out every step, keep the batch full). The transferable lesson the viewer keeps:
**memory-bound? stop reserving for the worst case — page it and keep the pipeline full.**

**Audience (HAI):** followers of the Fellows' STEM thread; anyone serving an open model
and hitting slow throughput / OOM.

## Act structure
- B00 HOOK (composer) — same model, same GPU, so why is vLLM many× faster? ✓
- B01 FRAMEWORK (versus) — the compute-bound guess vs the truth: the KV cache
  (per-token keys/values) in GPU memory is the bottleneck ✓
- B02 THE WASTE (grid) — naive contiguous per-request allocation sized for max length →
  60–80% idle, GPU waits ✓
- B03 PAGEDATTENTION (example) — page the cache into fixed-size blocks, block table maps
  logical→physical, <4% waste, copy-on-write block sharing for shared prefixes ✓
- B04 CONTINUOUS BATCHING (versus) — static padding vs iteration-level scheduling; admit/
  evict per step, batch stays full ✓
- B05 VERDICT (artifact) · B06 HANDOFF (compute or memory? page it) · B07 OUTRO ✓
- Body B01–B04 = 4K PIL cards; Claude UI only at B00/B05/B06/B07 (ILLUSTRATE LAW).

## Correctness (DOUBLE-CHECK LAW)
Facts verified against the PagedAttention/vLLM (SOSP '23, Kwon et al.) and continuous-
batching (Orca, OSDI '22) line of work; figures kept qualitative where brittle.
- **KV cache**: keys/values cached per token to avoid recomputing attention each step;
  grows with sequence length × concurrent requests; dominant *dynamic* GPU memory
  consumer. Decode is memory-bandwidth-bound → memory, not FLOPs, caps batch size. ✓
- **The waste**: reserving one contiguous slab per request sized for the max output
  length causes internal + external fragmentation; vLLM paper measured ~60–80% of KV
  memory wasted under naive allocation. ✓
- **PagedAttention**: fixed-size KV *blocks*, non-contiguous, allocated on demand; a
  block table maps logical→physical (OS paging analogy); waste falls to <4%; blocks are
  shareable with copy-on-write for shared prefixes / parallel sampling. ✓
- **Continuous (iteration-level) batching**: schedules per decode step; finished
  sequences freed and waiting ones admitted immediately — vs static batching padding to
  the longest/slowest. ✓
- **Throughput**: headline gains are several× over prior serving systems (~2–4×) and up
  to ~an order of magnitude+ over naive HF Transformers, at comparable latency. Card and
  narration say "several× / many times, same latency" to avoid a brittle exact figure. ✓

## PROOF note (framework-first)
Teaching rubric: one transferable framework ("serving is memory → page the KV cache,
keep the batch full") with a falsifiable diagnostic the viewer keeps (B06: compute-bound
or memory-bound? reserving for the worst case?). Production gate: every card legible; no
brittle exact speedup asserted; Pragmatist register, not vendor hype.

## Narration review (GATE P)
Listen for: is "memory-bound, not compute-bound" landed as the reframe (B01)? Is the OS-
paging analogy (B03) made concrete, not hand-waved? Does B06 leave a diagnostic the
viewer can run before buying hardware? Are speedups kept qualitative (no invented number)?

VERDICT: PASS
