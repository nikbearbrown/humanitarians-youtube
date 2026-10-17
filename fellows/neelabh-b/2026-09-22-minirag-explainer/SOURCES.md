# SOURCES — claude-liam-minirag

## Primary source (the only one)

**Fan, Tianyu; Wang, Jingyuan; Ren, Xubin; Huang, Chao** (corresponding author).
*MiniRAG: Towards Extremely Simple Retrieval-Augmented Generation.*
University of Hong Kong. arXiv:2501.06713v3, 26 January 2025. 16 pp.

- Local copy read for this build: `/Users/neela/Desktop/Humanitarians/MiniRag Paper.pdf`
- Authors' code and datasets: `https://github.com/HKUDS/MiniRAG`
- Read in full (all 16 pages including the appendix) on 2026-09-08.

Every number, quotation and structural claim in the reel traces to this one
paper. Claim-by-claim verification is in `FACTCHECK.md` (25 rows).

## What each beat draws on

| Beat | Source location |
|---|---|
| B00, B01 | Abstract; §1 Introduction |
| B02 | §1; §4 Related Works (RAG's three components) |
| B03 | Table 1, LiHuaWorld block; §3.2 |
| B04 | §3, the three stated research questions |
| B06 | Figure 1; §2.2.1; §2.2.2 |
| B07 | §2.1 (node and edge taxonomy, text-attributed edges) |
| B08 | Table 3 (case study, verbatim responses) |
| B09 | Table 1, both benchmark blocks |
| B10 | Table 2 (ablation) |
| B11 | Table 1, MultiHop-RAG block |
| B12 | §1, §3.2, Figure 3; §5 Conclusion |

## Corrections applied during scripting (DOUBLE-CHECK LAW)

The register's value is the rewrite. Three of the paper's own framings were
checked and **not** carried into narration:

1. **"Comparable performance to LLM-based methods"** (abstract). Dropped. On
   LiHuaWorld, MiniRAG + gpt-4o-mini scores 54.08 against LightRAG + gpt-4o-mini
   at 56.90 — the paper's own Table 1 does not support the general claim. The
   reel makes the narrower one that does hold: MiniRAG beats the lightweight
   alternatives **when the model is small**.
2. **"State-of-the-art performance across all evaluation settings"** (§1).
   Dropped for the same reason.
3. **Storage.** Only the published ratio (~25%) appears. Figure 3 is a scatter
   plot with no accompanying MB table, so no absolute storage figure is spoken
   or shown.

## Material fact the paper underplays — added deliberately

**B11 exists because of it.** On MultiHop-RAG with Phi-3.5-mini, MiniRAG scores
49.96% accuracy against LightRAG's 27.03% — but its error rate is 28.44% against
LightRAG's 11.78%. Both figures come from the paper's Table 1. §3.2 discusses
the accuracy gains and the storage savings; it does not discuss the error rate.
The reel states this as an observation about the paper's emphasis, never as a
claim its authors made.

## Explicitly not claimed

- **LiHuaWorld is not real user data.** It is GPT-4-generated with human
  curation, produced via AgentScope (Appendix, "Event Generation with Human
  Oversight"), for the privacy reasons the authors state. The reel never
  describes it as real chat logs.
- No latency, energy, or memory figures — the paper publishes none.
- Nothing about models or systems released after 26 January 2025.

## Generated assets

- **Narration:** Kokoro `am_onyx` (Liam), local, free. 16 MP3s in `mp3/`.
  Deterministic for a given text; regenerate any single beat with
  `--only <BEAT_ID>`.
- **Visuals:** all Remotion, all deterministic. Five reel-local components in
  `runtime/remotion/src/MiniRag.tsx`; the rest are existing registered scenes.
  `BrutalistHesitantWriter` is seeded (`minirag-bluf-01`) so its typing
  performance is identical on every render.
- **No AI image or video generation.** No Higgsfield, no paid API.
  **Total cost: $0.00.**

## Toolkit patch this build depends on

`runtime/scripts/build_safety.py:186` — the slug regex was widened from
`[A-Za-z0-9]` to `[A-Za-z0-9_]` as the leading character class. Unrelated to this
reel's content: without it the toolkit's own `./art smoke` fixture (`_smoke`)
fails validation, so the pipeline could not be verified end to end. Recorded here
because it is an uncommitted local change a rebuild depends on.
