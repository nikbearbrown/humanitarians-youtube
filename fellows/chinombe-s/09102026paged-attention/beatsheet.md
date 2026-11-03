# How PagedAttention Works — Beat Sheet

**Title:** How PagedAttention Works
**Slug:** hai-paged-attention
**Channel:** claude-hai · **Persona:** Simba · **Register:** Pragmatist · **Voice:** Kokoro `af_bella`
**Format:** ai-explainer (16:9 long cut) + 9:16 Shorts derivative (THE SHORTS LAW: single cycle, no revision, points back to the long cut)

No sprint report backs this one — general LLM-serving mechanics (the vLLM PagedAttention technique), a follow-on to `how-kv-cache-works`, which named PagedAttention as one of four memory-cost mitigations (B08) without explaining it. Both cuts render from `beat_sheet.json` at true 4K (`ART_SCALE` scale=2). Durations below are Kokoro-measured (`actual_duration_s`), not estimates — audio is the master clock.

## 16:9 — long cut (12 beats, 3:33 / 213.6s, 3840×2160)

| # | Act | Start | Dur | Pattern | Motion | What's on screen |
|---|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 22.2s | ClaudeComposerAsk | type-on | Cold open — the ask types in (a server reserving max GPU memory per conversation, most of it empty), answered: paging, applied to the KV cache, cache waste 60–80% down to under 4% |
| B01 | SUMMARY | 0:22 | 11.2s | ClaudeStatement | fade | BLUF: each request's cache splits into small, fixed-size blocks that don't have to sit next to each other in memory |
| B02 | STRUCTURE | 0:33 | 19.3s | FactStack | illustrate | Before PagedAttention — one contiguous slab per request, sized for the max sequence, 60–80% measured waste |
| B03 | PROBLEM | 0:52 | 16.9s | GrowthMeter | illustrate | Three bars — reserved (100%), actually used (~25%), wasted (70%, terracotta) — the reserved slab mostly empty |
| B04 | STRUCTURE | 1:09 | 27.6s | PageTable | illustrate | Logical blocks 0–3 on the left, the same blocks scattered into a different order on the right, connected through a "block table" — the page-table indirection PagedAttention borrows from OS memory |
| B05 | STRUCTURE | 1:37 | 21.1s | FactStack | illustrate | Allocated on demand — one block claimed only when the current one fills, every block but the last completely full, worst-case waste under one block |
| B06 | REASONING | 1:58 | 21.3s | SharedBlocks | illustrate | Shared prompt blocks fanning out to three candidates (parallel sampling / beam search); one candidate's line turns dashed-terracotta where it diverges and gets copied |
| B07 | RESULTS | 2:19 | 13.8s | DataTable | illustrate | Cache waste, before and after — naive contiguous allocation 60–80% vs. PagedAttention under 4%, footnote citing Kwon et al., SOSP 2023 |
| B08 | FINDINGS | 2:33 | 18.5s | FactStack | illustrate | What the reclaimed memory buys — more requests served, vLLM's reported 2–4× throughput over Orca/FasterTransformer, gap widening on longer sequences |
| B09 | SUMMARY | 2:51 | 26.0s | ClaudeVerdictArtifact | stagger | Verdict: delivered — fixed-size blocks, a block table, copy-on-write sharing / proven — under 4% waste, 2–4× throughput / NOT fixed — attention's own per-step compute cost |
| B10 | NEXT STEPS | 3:17 | 11.4s | ClaudeComposerAsk | type-on | Handoff — "Your turn." prompt types in |
| B11 | OUTRO | 3:29 | 4.3s | ClaudeTitleOutro | fade | Title restate, terracotta period, handle, subline "paging · not a compute fix" |

## 9:16 — Shorts cut (5 beats, 0:59 / 59.3s, 2160×3840)

Per THE SHORTS LAW: single cycle, no revision pass — condenses the cold open and verdict, reuses the one "wait, what" comparison-table moment (`DataTable916`, same content as the long cut's B07), and points back to the long cut for how the sharing works.

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 16.0s | ClaudeComposerAsk916 | Condensed cold open |
| B01 | SUMMARY | 0:15 | 9.9s | ClaudeStatement916 | The idea, stated |
| B02 | RESULTS | 0:25 | 13.7s | DataTable916 | Cache waste, before (60–80%) and after (<4%), 2–4× throughput footnote |
| B03 | SUMMARY | 0:39 | 14.1s | ClaudeVerdictArtifact916 | Verdict, condensed |
| B04 | OUTRO | 0:53 | 5.7s | ClaudeTitleOutro916 | Title restate, "full build on the channel" |

`beat_sheet.json` in each reel's own folder (`hai-paged-attention/` and `hai-paged-attention-916/`) is the heart — this table is derived from it, not the other way around. Edit the sheet, not this file, if the reel changes.
