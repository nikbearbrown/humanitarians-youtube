# FACT-CHECK — "Reordering, Not Retrieval" (week-14)

Audit of `beat_sheet.json` against `sources/`, done before audio. Numeric source of truth is
`ablation_graph_vs_retrieval.json`; the prose docs and the figure are cross-checked against it.

## Verdicts by claim

| # | Claim (on screen / narrated) | Verdict | Evidence / source |
|---|---|---|---|
| 1 | The fair test is an ablation: run with vs without the graph | SUPPORTED | weekly_report §2; README |
| 2 | Two arms, same project + embeddings: retrieval = top-K by similarity; method = core + required-prereq closure, topological sort | SUPPORTED | weekly_report §2 |
| 3 | Four metrics: insertion, broken dependencies, Kendall-tau reordering, personalization | SUPPORTED | weekly_report §2; README |
| 4 | Insertion (K=20): 34 (LNP-siRNA) / 31 (photothermal) | SUPPORTED | json `headline.lnp_sirna.inserted=34`, `photothermal.inserted=31` |
| 5 | Inserted sections are foundations (cell biology, cell cycle, DNA/protein synthesis, signaling) | SUPPORTED | json `inserted_examples` (CH01-S02…S08, CH02-S02) |
| 6 | Retrieval misses 17/12 prerequisites | SUPPORTED | json `retrieval_missing` 17 / 12 |
| 7 | Retrieval mis-orders 3/2 sections | SUPPORTED | json `retrieval_misordered` 3 / 2 |
| 8 | **"20 / 14 dependencies broken"** | SUPPORTED (combined metric) | missing + mis-ordered: 17+3=**20**, 12+2=**14**; matches the figure's left panel (retrieval 20 / 14). Narration decomposes it (17/12 + 3/2); both consistent. |
| 9 | Method breaks 0 / 0 | SUPPORTED | json `method_missing=0`, `method_misordered=0` (both projects) |
| 10 | Kendall tau = -0.44 / 0.00 | SUPPORTED | json `kendall_tau` -0.442 (lnp) / 0.0 (photothermal). Narration: lnp "reversed", photothermal "uncorrelated" — exact (0.0 = uncorrelated, not reversed). |
| 11 | A genuine reshuffle; overturns week 5's "insertion, not reshuffle" | SUPPORTED | weekly_report §1, §3 (week 5 ran on a draft graph with 0 authoritative edges) |
| 12 | Personalization: core Jaccard 0.25; with foundations 0.615 | SUPPORTED | json `personalization.core_jaccard=0.25`, `method_jaccard=0.615` |
| 13 | Robust across K=10/20/30: method breaks 0 at every K; graph inserts dozens; tau ≤ 0 | SUPPORTED | json `sweep`: method 0/0 at all K; lnp inserts 32/34/42, tau -0.333/-0.442/-0.338; photothermal inserts 32/31/34, tau -0.244/0.0/0.002 |
| 14 | B07 table (LNP-siRNA): method breaks 0/0/0; inserts 32/34/42; tau -0.33/-0.44/-0.34 | SUPPORTED | json `sweep.lnp_sirna` |
| 15 | General-domain embedder all-MiniLM-L6-v2; structural result embedding-independent | SUPPORTED | json `embedder`; weekly_report §4 |
| 16 | Reads required edges from the authoritative prereq CSV; Stage-3 graph.json since reconciled | SUPPORTED | weekly_report §4, §6 |
| 17 | Draft edges; measures the mechanism; no learning-outcome claim | SUPPORTED | weekly_report §4; README source-status |
| 18 | Grounding: Liang 2015, Pan 2017, Liang 2018; topological sort; Kendall 1938; ablation | SUPPORTED | weekly_report §5; README |

## Notes carried into the beat sheet
- The figure's left panel is labelled "prerequisite dependencies broken" with retrieval 20 / 14 — the **sum** of missing + mis-ordered. B04 states the combined 20/14 and the decomposition (17/12 + 3/2) so the on-screen figure and the narration agree.
- photothermal tau at K=20 is exactly **0.0** (uncorrelated), not negative; narration says "zero for the other," and the reshuffle claim rests on "at or below zero" + the −0.44 case. No overstatement.
- B07 shows the LNP-siRNA sweep row explicitly and notes photothermal holds too (method 0 at every K) — avoids implying photothermal's tau is also negative (it is ~0).

## Not claimed (guardrails upheld)
- Draft edges are never presented as approved.
- No learning-outcome claim anywhere.
- The embedder limitation is stated (B08), and the structural-result claim is scoped to "retrieval cannot encode a dependency at any embedding quality."

**FACT-CHECK VERDICT: PASS** — all on-screen figures match `ablation_graph_vs_retrieval.json`; no corrections required. Signed 2026-10-31.
