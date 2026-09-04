# How KV Cache Works — Beat Sheet

**Title:** How KV Cache Works
**Slug:** how-kv-cache-works
**Channel:** claude-hai · **Persona:** Simba · **Register:** Pragmatist · **Voice:** Kokoro `af_bella`
**Format:** ai-explainer (16:9 long cut) + 9:16 Shorts derivative (THE SHORTS LAW: single cycle, no revision, points back to the long cut)

No sprint report backs this one — general transformer-inference mechanics (Query/Key/Value projections, causal masking, GQA, sliding-window caching, quantized caches, PagedAttention/vLLM). Both cuts render from `beat_sheet.json` at true 4K (`ART_SCALE` scale=2). Durations below are Kokoro-measured (`actual_duration_s`), not estimates — audio is the master clock.

## 16:9 — long cut (12 beats, 4:24 / 264.3s, 3840×2160)

| # | Act | Start | Dur | Pattern | Motion | What's on screen |
|---|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 18.4s | ClaudeComposerAsk | type-on | Cold open — the ask types in ("why isn't token 10,000 ten thousand times slower"), answered: cached K/V, never recomputed |
| B01 | SUMMARY | 0:18 | 14.0s | ClaudeStatement | fade | BLUF: once a token's Key and Value are computed they never change — cache once, reuse forever |
| B02 | STRUCTURE | 0:32 | 23.9s | TokenSplit | illustrate | One token fans out into Query / Key / Value, each with its role; causal-masking note beneath |
| B03 | PROBLEM | 0:56 | 19.6s | GrowthMeter | illustrate | Done naively: 4 climbing bars, "2 redone" → "5 redone" — every step recomputes K/V that never changed |
| B04 | STRUCTURE | 1:15 | 17.4s | DataTable | illustrate | The cache as an append-only table — 3 tokens' K/V land, status "appended," footnote: never rewritten |
| B05 | RESULTS | 1:33 | 22.3s | DecodeStep | illustrate | One real decode step: new token → compute Q/K/V → append + attend → next token |
| B06 | REASONING | 1:55 | 32.2s | FindingPair | illustrate | What actually gets cheaper: projections + feedforward flat, attention-against-the-cache still grows |
| B07 | REASONING | 2:27 | 23.9s | GrowthMeter | illustrate | The price is memory: relative growth across short / longer / long / very-long context, in × |
| B08 | FINDINGS | 2:51 | 41.3s | TestSuiteProof | stagger | 4 numbered levers — GQA, sliding window, quantized cache, PagedAttention/vLLM — same target: standing memory cost |
| B09 | SUMMARY | 3:32 | 31.1s | ClaudeVerdictArtifact | stagger | Verdict: buys flat decode cost / costs standing memory / NOT fixed: attention's own per-step growth |
| B10 | NEXT STEPS | 4:04 | 16.2s | ClaudeComposerAsk | type-on | Handoff — "Your turn." prompt types in |
| B11 | OUTRO | 4:20 | 4.0s | ClaudeTitleOutro | fade | Title restate, terracotta period, handle, subline "cache once · attend forever" |

## 9:16 — Shorts cut (5 beats, 1:04 / 64.2s, 2160×3840)

Per THE SHORTS LAW: single cycle, no revision pass — condenses the cold open and verdict, reuses the one illustrated middle beat (`DecodeStep916`, same props as the long cut's B05), and points back to the long cut for the memory trade-offs.

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 13.3s | ClaudeComposerAsk916 | Condensed cold open |
| B01 | SUMMARY | 0:13 | 10.9s | ClaudeStatement916 | The idea, stated |
| B02 | RESULTS | 0:24 | 17.6s | DecodeStep916 | The one real decode step |
| B03 | SUMMARY | 0:41 | 16.4s | ClaudeVerdictArtifact916 | Verdict, condensed |
| B04 | OUTRO | 0:58 | 5.9s | ClaudeTitleOutro916 | Title restate, "full build on the channel" |

`beat_sheet.json` in each reel's own folder (`how-kv-cache-works/` and `how-kv-cache-works-916/`) is the heart — this table is derived from it, not the other way around. Edit the sheet, not this file, if the reel changes.
