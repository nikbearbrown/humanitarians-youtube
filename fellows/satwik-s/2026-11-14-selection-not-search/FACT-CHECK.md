# FACT-CHECK — Week 16: Selection, Not Search (Stage 4b Matching)

**Audited:** beat_sheet.json beat-by-beat against `sources/` (matching_signal_ablation.json / .md, matching_selection.md, weekly_report_2026-11-14.md).
**Signed:** 2026-11-14 · **VERDICT: PASS** (no corrections).

## Claim table

| Beat | Claim | Verdict | Evidence (matching_signal_ablation.json) |
|------|-------|---------|------------------------------------------|
| B03 | top-20 no-vocab: LNP 17/20 (85%), photothermal 12/20 (60%) | SUPPORTED | lnp_sirna retrieval_topk_no_vocab k20: 17, fraction 0.85; photothermal k20: 12, fraction 0.6 |
| B04 | K-sweep LNP: 90% / 85% / 83% | SUPPORTED | lnp k10 9/0.9, k20 17/0.85, k30 25/0.833 |
| B04 | K-sweep photothermal: 80% / 60% / 57% | SUPPORTED | photothermal k10 8/0.8, k20 12/0.6, k30 17/0.567 |
| B05 | LNP selects 32; roles core 7 / method 8 / background 12 / optional 5 | SUPPORTED | lnp selection n_selected 32; roles: core platform 7, supporting method 8, foundational background 12, optional extension 5 |
| B05 | photothermal selects 26; roles core 1 / method 8 / background 12 / optional 5 | SUPPORTED | photothermal selection n_selected 26; roles: core platform 1, supporting method 8, foundational background 12, optional extension 5 |
| B06 | role = category membership, not a tuned threshold; weights only order within a role | SUPPORTED | matching_signal_ablation.md "What this shows" ¶2; matching_selection.md |
| B07 | exclusions 864 (LNP) / 559 (photothermal) | SUPPORTED | lnp n_excluded 864; photothermal n_excluded 559 |
| B07 | high-sim-no-vocab 109 (LNP, e.g. CH28-S02-SS02) / 63 (photothermal, e.g. CH28-S01) | SUPPORTED | lnp headline_high_sim_no_vocab 109, example CH28-S02-SS02; photothermal 63, example CH28-S01 |
| B08 | general embedder all-MiniLM-L6-v2; draft metadata; no learning claim; isolates Stage 4b | SUPPORTED | json embedder field; matching_signal_ablation.md header "Isolates Stage 4b. No sequencing."; weekly_report §source status |

## Totals sanity
- LNP exclusion buckets: generic-only 577 + high-sim-no-vocab 109 + capped 178 = 864 ✓
- photothermal buckets: high-sim-no-vocab 63 + generic-only 234 + capped 262 = 559 ✓
- LNP roles: 7+8+12+5 = 32 ✓ · photothermal roles: 1+8+12+5 = 26 ✓

## Guardrails honored
- Every on-screen number traces to `matching_signal_ablation.json`.
- Draft metadata never presented as approved (B08 stamp).
- No learning-outcome claim anywhere. Isolates Stage 4b (no sequencing) — stated in B01 and B08.
