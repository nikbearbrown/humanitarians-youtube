# How PagedAttention Works — script (final, as shot)

Channel claude-hai · Persona Simba · Register Pragmatist · Voice Kokoro `af_bella`
16:9 long cut: 3:33 (213.6s) · 9:16 Shorts: 0:59 (59.3s)

Timestamps and durations are Kokoro-measured from the locked audio, not estimates — this is exactly what's spoken in the final render. Pre-production shot notes, on-screen prop text, and build rationale live in `SCRIPT-paged-attention.md`; this file is narration only, dated to the finished cuts.

## 16:9 — long cut

### B00 · INTRO (0:00–0:22)
> Hi, I am Simba. Say a server is handling a hundred conversations with a language model at once. Each one needs its own slice of GPU memory for everything it's generated so far. Reserve too little, and long conversations break. Reserve the max for everyone, and most of that memory just sits empty. That's the problem PagedAttention solves.

### B01 · SUMMARY (0:22–0:33)
> PagedAttention splits each request's cache into small, fixed-size blocks that don't have to sit next to each other in memory — so nothing is reserved for tokens that might never come.

### B02 · STRUCTURE (0:33–0:52)
> Before this, most serving systems gave each request one contiguous slab of memory, sized for the longest sequence allowed — a short reply still reserving room for thousands of tokens it would never use. The paper behind this technique measured the damage: sixty to eighty percent of that memory going to waste.

### B03 · PROBLEM (0:52–1:09)
> Picture that memory as one giant reserved block per conversation — only a sliver of it holding real, generated tokens. The rest sits empty, waiting for tokens that may never arrive, unusable by anyone else even while other requests are queued for space.

### B04 · STRUCTURE (1:09–1:37)
> PagedAttention borrows an old idea from operating systems: paging. Instead of one contiguous slab, each sequence's key and value cache is split into small, fixed-size blocks — sixteen tokens each, in the original design. A block table maps each sequence's logical blocks to wherever they actually sit in physical memory — scattered, not sequential, exactly like a page table maps virtual memory to physical RAM.

### B05 · STRUCTURE (1:37–1:58)
> Blocks get allocated one at a time, only as new tokens are actually generated — never reserved in advance. Every block before the last one is completely full. Only the final, in-progress block can be partly empty. So the absolute most any single sequence can waste is less than one block — a few tokens, not a few thousand.

### B06 · REASONING (1:58–2:19)
> Because sequences are just pointers into a shared pool of blocks, requests can share memory too. Ask a model for several sampled outputs from the same prompt, or run a beam search, and every candidate starts by pointing at the exact same prompt blocks — copied only if and when one candidate's tokens actually diverge from another's.

### B07 · RESULTS (2:19–2:33)
> The result, measured against those same fragmented systems: KV cache waste drops from that sixty-to-eighty percent down to under four percent. Almost every byte allocated is a byte actually holding a real token.

### B08 · FINDINGS (2:33–2:51)
> That reclaimed memory goes straight into serving more requests at once. vLLM, the engine built around this technique, reported two to four times the throughput of the strongest prior systems — with the gap widening on longer sequences, exactly where fragmentation used to hurt most.

### B09 · SUMMARY (2:51–3:17)
> So: PagedAttention is a memory manager, not a shortcut around attention's own math. It applies an operating-system idea — paging — to the KV cache, cutting waste from sixty-to-eighty percent down to under four, and buying two to four times the throughput because that freed memory now serves more requests. What it doesn't do is make attention itself cheaper — a longer, more-shared cache is still more work to attend across.

### B10 · NEXT STEPS (3:17–3:29)
> Your turn. If you're serving a model yourself, check how your KV cache is actually allocated — one reserved slab per request, or blocks handed out only as tokens arrive?

### B11 · OUTRO (3:29–3:33)
> How PagedAttention works. Simba, for Humanitarians AI.

## 9:16 — Shorts cut

### B00 · INTRO (0:00–0:15)
> Hi, I am Simba. Serving a hundred conversations at once means giving each one memory for everything it's said so far. Reserve the max for everyone, and most of it sits empty. PagedAttention borrows an old OS trick — paging — to fix that.

### B01 · SUMMARY (0:15–0:25)
> PagedAttention splits the cache into small, fixed-size blocks that don't have to sit together in memory — so nothing is reserved for tokens that might never come.

### B02 · RESULTS (0:25–0:39)
> Measured against ordinary allocation: sixty to eighty percent of KV cache memory wasted before PagedAttention. Under four percent wasted after. That reclaimed memory buys two to four times the throughput.

### B03 · SUMMARY (0:39–0:53)
> PagedAttention is a memory manager, not a shortcut around attention's own math — it cuts cache waste from sixty-to-eighty percent to under four, and buys more throughput. What it doesn't do is make attention itself any cheaper.

### B04 · OUTRO (0:53–0:59)
> Full build, with how the sharing works, is on the channel. Simba, for Humanitarians AI.

---

This script covers general LLM-serving mechanics, not a proprietary or sprint-specific result — a direct follow-on to `how-kv-cache-works`, which named PagedAttention as a mitigation without explaining it. Every figure (60–80% waste, under 4% waste, 2–4× throughput, the 16-token default block size) is drawn from the published vLLM paper (Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention," SOSP 2023), kept to that paper's own headline numbers rather than newer vLLM-project benchmarks, per `SCRIPT-paged-attention.md`'s Sources.
