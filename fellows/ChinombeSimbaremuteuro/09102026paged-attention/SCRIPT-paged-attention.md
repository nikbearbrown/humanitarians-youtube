# How PagedAttention Works — Script

**Title:** How PagedAttention Works
**Slug:** how-paged-attention-works (suggested)
**Channel:** claude-hai · **Persona:** Simba · **Register:** Pragmatist · **Voice:** Kokoro `af_bella`
**Format:** ai-explainer, single 16:9 cut
**Target runtime:** 4:00 — 12 beats, ~239s by word count. As with the other general-mechanics videos in this series, the Kokoro-measured actual duration tends to run a little longer than the word-count estimate on the denser explanatory beats, so expect the finished cut to land close to, and possibly a touch over, 4:00.

No sprint report backs this one — general LLM-serving mechanics, not a Mycroft result. It's a natural follow-on to `how-kv-cache-works`, which named PagedAttention as one of four memory-cost mitigations (B08) without explaining it; this script goes one level deeper into that single technique. All cited figures (60–80% memory waste under naive allocation, sub-4% waste and 2–4x throughput under PagedAttention, the 16-token default block size) are from the published vLLM paper and project — see Sources.

Pattern column below is a suggestion, not a commitment — same convention as this series' other scripts: reused house components (`ClaudeComposerAsk`, `ClaudeStatement`, `FactStack`, `GrowthMeter`, `ClaudeVerdictArtifact`, `ClaudeComposerAsk`, `ClaudeTitleOutro`) are already built and QC'd from prior reels; the two beats marked **NEW** describe a shape (a block/page-table diagram) nothing in the library currently covers, so GATE L and any new component authoring happen at build time, not here.

## Beats

### B00 · INTRO — cold open (~26s)
**Pattern:** `ClaudeComposerAsk` (reuse) · **Motion:** type-on

> Hi, I am Simba. Say a server is handling a hundred conversations with a language model at once. Each one needs its own slice of GPU memory for everything it's generated so far. Reserve too little, and long conversations break. Reserve the max for everyone, and most of that memory just sits empty. That's the problem PagedAttention solves.

**On screen:** ask types in as the question above (condensed); output lines land answered:
- "an old OS idea — paging — applied to the KV cache"
- "cache waste: 60–80% down to under 4%"

### B01 · SUMMARY — BLUF (~14s)
**Pattern:** `ClaudeStatement` (reuse) · **Motion:** fade

> PagedAttention splits each request's cache into small, fixed-size blocks that don't have to sit next to each other in memory — so nothing is reserved for tokens that might never come.

**On screen — kicker:** THE IDEA · **sparkLine:** "So memory is claimed as it's used, not reserved in advance."

### B02 · STRUCTURE — the old way (~22s)
**Pattern:** `FactStack` (reuse) · **Motion:** illustrate

> Before this, most serving systems gave each request one contiguous slab of memory, sized for the longest sequence allowed — a short reply still reserving room for thousands of tokens it would never use. The paper behind this technique measured the damage: sixty to eighty percent of that memory going to waste.

**On screen — kicker:** BEFORE PAGEDATTENTION · **facts:**
- one contiguous slab per request, allocated up front
- sized for the longest sequence the system allows — not the one actually asked for
- measured waste: 60–80% of KV cache memory, to fragmentation and over-reservation

**closingLine:** Most of what's reserved is never actually used.

### B03 · PROBLEM — the waste, illustrated (~18s)
**Pattern:** `GrowthMeter` (reuse) · **Motion:** illustrate

> Picture that memory as one giant reserved block per conversation — only a sliver of it holding real, generated tokens. The rest sits empty, waiting for tokens that may never arrive, unusable by anyone else even while other requests are queued for space.

**On screen:** three bars — "reserved" (full height), "actually used" (short), "wasted" (tall, terracotta) — with a value label on each.

### B04 · STRUCTURE — paging, the core idea (~27s) — **NEW**
**Pattern:** TBD at build (GATE L) — needs a block/page-table diagram; no existing component covers this shape · **Motion:** illustrate

> PagedAttention borrows an old idea from operating systems: paging. Instead of one contiguous slab, each sequence's key and value cache is split into small, fixed-size blocks — sixteen tokens each, in the original design. A block table maps each sequence's logical blocks to wherever they actually sit in physical memory — scattered, not sequential, exactly like a page table maps virtual memory to physical RAM.

**On screen:** logical blocks (0, 1, 2, 3…) on the left, physical memory slots scattered on the right, dashed lines from each logical block to its actual physical slot via a small "block table" in the middle.

### B05 · STRUCTURE — allocation on demand (~24s)
**Pattern:** `FactStack` (reuse) · **Motion:** illustrate

> Blocks get allocated one at a time, only as new tokens are actually generated — never reserved in advance. Every block before the last one is completely full. Only the final, in-progress block can be partly empty. So the absolute most any single sequence can waste is less than one block — a few tokens, not a few thousand.

**On screen — kicker:** ALLOCATED ON DEMAND · **facts:**
- one new block claimed only when the current block fills up
- every block but the last is completely full
- worst case waste: under one block per sequence

**closingLine:** Waste is capped by the block size, not by how long the conversation might get.

### B06 · REASONING — memory sharing (~26s) — **NEW**
**Pattern:** TBD at build (GATE L) — needs a shared/forked-blocks diagram; related to but distinct from B04's diagram · **Motion:** illustrate

> Because sequences are just pointers into a shared pool of blocks, requests can share memory too. Ask a model for several sampled outputs from the same prompt, or run a beam search, and every candidate starts by pointing at the exact same prompt blocks — copied only if and when one candidate's tokens actually diverge from another's.

**On screen:** one prompt's blocks in the center, three candidate-output arrows fanning out from them, all pointing at the same shared blocks until a small "diverges here → copied" branch appears on one arrow only.

### B07 · RESULTS — what it buys, part one (~14s)
**Pattern:** `DataTable` or `ClaudeStatement`-style stat card (reuse) · **Motion:** illustrate

> The result, measured against those same fragmented systems: KV cache waste drops from that sixty-to-eighty percent down to under four percent. Almost every byte allocated is a byte actually holding a real token.

**On screen:** before/after bar or two-row stat — "before: 60–80% wasted" / "PagedAttention: <4% wasted."

### B08 · FINDINGS — what it buys, part two (~19s)
**Pattern:** `FindingPair` or `TestSuiteProof` (reuse) · **Motion:** illustrate

> That reclaimed memory goes straight into serving more requests at once. vLLM, the engine built around this technique, reported two to four times the throughput of the strongest prior systems — with the gap widening on longer sequences, exactly where fragmentation used to hurt most.

**On screen — sparkLine:** "2–4× throughput over prior state-of-the-art serving (vLLM, vs. Orca / FasterTransformer)."

### B09 · SUMMARY — verdict (~29s)
**Pattern:** `ClaudeVerdictArtifact` (reuse) · **Motion:** stagger

> So: PagedAttention is a memory manager, not a shortcut around attention's own math. It applies an operating-system idea — paging — to the KV cache, cutting waste from sixty-to-eighty percent down to under four, and buying two to four times the throughput because that freed memory now serves more requests. What it doesn't do is make attention itself cheaper — a longer, more-shared cache is still more work to attend across.

**Artifact lines:**
- Delivered: fixed-size KV cache blocks, a block table, and copy-on-write sharing across candidates.
- Proven: cache waste under 4% (vs. 60–80% before); 2–4× reported throughput over prior serving systems.
- NOT fixed: attention's own per-step compute cost — a longer, more-shared cache is still more work to attend over.

### B10 · NEXT STEPS — handoff (~12s)
**Pattern:** `ClaudeComposerAsk` (reuse) · **Motion:** type-on

> Your turn. If you're serving a model yourself, check how your KV cache is actually allocated — one reserved slab per request, or blocks handed out only as tokens arrive?

### B11 · OUTRO (~4s)
**Pattern:** `ClaudeTitleOutro` (reuse) · **Motion:** fade

> How PagedAttention works. Simba, for Humanitarians AI.

**On screen:** title restate, terracotta period, handle, subline "paging · not a compute fix."

---

## Sources
Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention," SOSP 2023 (the paper introducing PagedAttention and vLLM) — figures cited: 60–80% KV cache memory waste under conventional contiguous allocation; under 4% waste and 2–4× throughput improvement over then-state-of-the-art serving systems (Orca, FasterTransformer) under PagedAttention/vLLM; 16-token default block size. Kept deliberately to the paper's own headline numbers rather than newer vLLM-project benchmarks, since this script is explaining the original technique, not vLLM's current-day performance.
