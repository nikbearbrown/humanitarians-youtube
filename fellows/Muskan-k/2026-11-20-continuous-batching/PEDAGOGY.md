# PEDAGOGY — Continuous Batching (claude-hai · AI, Explained · ~2.5min)

**Genre:** concept explainer (framework-first, built to pass PROOF). Topic named by
request: continuous batching / processing multiple requests efficiently. A deliberate
**zoom-in** on the one beat the vLLM reel (2026-11-06) only had room to name.

**The ONE reusable idea (throughline/verdict):** serving many users on one GPU means
**keeping the batch full**, and the enemy is **waiting** — waiting to fill a batch, and
waiting on the slowest request. Static (request-level) batching has both; **continuous
(iteration-level) batching** schedules one decode step at a time — evict finished
sequences, admit waiting ones — so the batch is re-planned every token and never empties.
The transferable test the viewer keeps: **is it slow because the batch isn't full, or
because one slow item blocks the rest? If either — schedule the smallest unit of work and
let items leave/join independently.**

**Audience (HAI):** followers of the Fellows' STEM thread; anyone serving a model (or any
throughput pipeline with variable-length jobs).

## Act structure
- B00 HOOK (composer) — one GPU, a hundred users; batch or stall ✓
- B01 FRAMEWORK (versus) — one-at-a-time wastes a parallel machine vs batched (N for ~the
  cost of one); occupancy = throughput ✓
- B02 THE STALL (grid) — static batching: wait to fill, lockstep to the longest, held/
  padded slots, head-of-line blocking ✓
- B03 THE FIX (example) — iteration-level scheduling: after each token, finished leave /
  waiting join; batch re-planned every step ✓
- B04 THE TRADE (grid, falsifiability) — prefill stalls, KV-memory ceiling, tail latency;
  throughput-vs-latency tension bounded by memory ✓
- B05 VERDICT (artifact) · B06 HANDOFF (full, or waiting?) · B07 OUTRO ✓
- Body B01–B04 = 4K PIL cards; Claude UI only at B00/B05/B06/B07 (ILLUSTRATE LAW).

## Correctness (DOUBLE-CHECK LAW)
Verified against Orca (OSDI '22, iteration-level scheduling) and the continuous-batching
serving literature; figures kept qualitative where brittle.
- **Why batch:** a GPU is a throughput machine; LLM decode is memory-bandwidth-bound, so
  a forward pass over a batch of N costs ≈ a pass over 1 until the compute-bound regime —
  batching amortizes it, so occupancy drives throughput. Narration says "almost for the
  cost of one" (hedged), not "free." ✓
- **Static batching failure:** requests run in lockstep and the batch completes only when
  the longest sequence finishes; shorter ones hold padded slots; new requests can't be
  admitted until the batch clears (head-of-line blocking). Acute for LLMs because output
  lengths vary widely. ✓
- **Continuous batching:** scheduling at the granularity of one decoding iteration;
  finished sequences are evicted and waiting ones admitted each step, so batch
  composition changes continuously. a.k.a. iteration-level / in-flight / dynamic batching. ✓
- **The costs (honest boundary):** a newly admitted request must **prefill** (process its
  whole prompt — compute-heavy) which can interfere with others' single-token **decode**,
  causing latency hiccups (mitigated by chunked prefill / prefill-decode disaggregation —
  named in narration only as "process the whole prompt in one go"); and the KV cache for
  every concurrent sequence sets a hard memory ceiling on batch size. So it's a
  throughput/tail-latency tension bounded by memory. ✓
- **Speedup:** several×–~an order of magnitude over static batching depending on workload;
  kept qualitative on-card to avoid a brittle number. ✓

## PROOF note (framework-first)
Teaching rubric: one transferable framework (occupancy = throughput; schedule the
smallest unit; let items leave/join) with a falsifiable boundary (B04) and a diagnostic
the viewer keeps (B06). Production gate: every card legible; no invented speedup; register
Pragmatist. Distinct from the vLLM reel: that one was *memory* (PagedAttention) with
batching as a coda; this one is *scheduling*, with memory as the coda.

## Narration review (GATE P)
Listen for: is "occupancy is throughput" landed (B01)? Are the *two* waits of static
batching both named (B02)? Is the per-token re-planning made concrete (B03)? Is B04 a
real cost, not a footnote — prefill interference + memory ceiling? Speedups qualitative?

VERDICT: PASS
