# FACTCHECK — The Brand That Didn't Exist

Status: **GATE F SIGNED — 2026-09-03.** Every on-screen figure recomputed from
the shipped `results/` files. **The paper abstract's headline figures are NOT
used, because they are not reproducible from the data in the archive.**

Source: `D:/Projects/geo-main.zip` → GEO research platform.
Conditions identified by the `rag_version` field on each run's records:

```
A  no RAG           results/report_20260415_133752.json
C  RAG + neutral    results/report_20260415_133654.json   rag_version=baseline
B  RAG + optimized  results/report_20260415_133611.json   rag_version=optimized
```

## Verified — used on screen

| # | Beat | Claim | Verdict | Derivation |
|---|---|---|---|---|
| 1 | B01,B03 | Top brand 95%, bottom 15% | ✓ PASS | Condition A `brand_metrics`: HubSpot 0.95, Copper 0.15, n=40 each |
| 2 | B03 | 20 prompts · 4 models · 9 brands | ✓ PASS | `baseline_*.json`: 80 records, 20 unique prompts, `model_key` ∈ {gpt-5.4-mini, llama-4-maverick, mistral-large, deepseek-v3.2}; `brand_metrics` has 9 entries |
| 3 | B03 | Baseline mean 50.3% | ✓ PASS | mean of the 9 Condition A rates = 0.5028 |
| 4 | B04 | Neutral RAG mean 86.7% (+36.4) | ✓ PASS | mean of the 9 Condition C rates = 0.8667 |
| 5 | B05 | Optimized RAG mean 91.1% (+4.4 over C) | ✓ PASS | mean of the 9 Condition B rates = 0.9111 |
| 6 | B05 | Bottom tier +69.4, top tier +11.7 | ✓ PASS | A→B lift, split at baseline ≤30% (Freshsales, Less Annoying CRM, Notion, Copper) vs ≥80% (HubSpot, ClickUp, Asana) |
| 7 | B05 | GEO strategies = statistics, quotations, citations | ✓ PASS | README + `data/brands.json` optimized versions; strategy set from KDD 2024, arXiv:2311.09735 |
| 8 | B06 | Pseudo-brand 8.6% cold (3 of 35) | ✓ PASS | `pseudo_brand_20260415_095028.json`, `nexacrm_mentioned` true in 3 of 35 (7 models × 5 prompts) |
| 9 | B06 | 90% and 95% with retrieved content | ✓ PASS | `…103941` 18/20; `…131814` 19/20 |
| 10 | B06 | Ranked #1 in every case where mentioned | ✓ PASS | `nexacrm_position` is 1 for every mentioned record in all three runs |

## NOT used — abstract figures that failed verification

Reported for the authors; none of these appears in the video.

| Abstract says | Archive shows |
|---|---|
| HubSpot 87.1%, Copper 0% | 95.0% and 15.0% (Condition A) |
| Copper 0% → 100% under optimized RAG | 15.0% → 92.5% |
| Pseudo-brand 50% mention rate | 8.6% cold; 90% / 95% with RAG |
| 140 queries | 80 baseline records (20 prompts × 4 models) |
| 18 brands | 9 in `brands.json`, plus 1 pseudo-brand |
| GPT-4o-mini | `config.py` and every result row say `openai/gpt-5.4-mini` |
| "neutral RAG *decreases* mention rates" (context dilution) | Neutral RAG **increases** every brand's rate vs Condition A (mean 50.3% → 86.7%) |

Every finding's **direction** survives; the magnitudes and setup counts do not.
The video therefore reports the measured values and makes no dilution claim.

## Claims deliberately NOT made

- **No claim that any brand is better than another.** The video states
  explicitly that mention rate does not measure product quality or fit.
- **No claim about models not in the runs.** `config.py` defines 7 models;
  only 4 ran the main conditions. The video says "four models".
- **No causal claim about why parametric visibility differs** between brands —
  the archive does not contain evidence for that.
- **Brand names in B01 are anonymised** ("brand A" / "brand B") because that
  beat is the one-breath summary; the named ranking appears in B03 where the
  source file is on screen.
