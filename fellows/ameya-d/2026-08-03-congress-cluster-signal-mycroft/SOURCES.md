# SOURCES — congress-cluster-signal

Every on-screen number traces to the project's own artifacts. DOUBLE-CHECK LAW:
no figure appears on screen that isn't sourced here. Version-drifting counts are
stated once and dated; nothing is annualized or rounded up for effect.

Primary source: `RESEARCH_REPORT.md` (Ameya Deshmukh, working paper, July 2026),
cross-checked against the actual pipeline code (`market_adjusted.py`,
`backtest.py`).

## Dataset (B00, B01)
| Claim on screen / in VO | Value | Source |
|---|---|---|
| Total trades | 13,877 | RESEARCH_REPORT §2 table |
| Members of Congress | 108 | §2 table |
| Date range | May 2023 – June 2026 | §2 table |
| Trades with complete pricing | 10,183 (73%) | §2 table |
| STOCK Act disclosure window | 45 days | §1 (Public Law 112-105) |

## Methodology (B02, B03)
| Claim | Value | Source |
|---|---|---|
| Return measured from disclosure date, 30-day window | — | §3.1 |
| alpha = trade 30d return − SPY 30d (matched window) | — | §3.2; `market_adjusted.py:92` |
| Code shown in B03 | verbatim (trimmed) | `market_adjusted.py:54-63, 91-92` |

## Aggregate result (B04) — RESEARCH_REPORT §4.1
| Trade type | n | Raw 30d | SPY | Alpha |
|---|---|---|---|---|
| BUY | 5,162 | +2.23% | +2.10% | +0.13% |
| SELL | 4,972 | +2.01% | +2.02% | −0.01% |

## Cluster definition + tiering (B05, B06)
| Claim | Value | Source |
|---|---|---|
| Cluster = ≥2 distinct politicians, same ticker, 30-day window | — | §3.3; `backtest.py:67-96` |
| signal_score = cluster_size × max(BCR of members) | — | §3.4; `backtest.py:80-82` |
| Tiers: STRONG ≥2.0 · WATCH ≥1.0 · SKIP <1.0 (cluster) · SOLO no cluster | — | §3.4; `backtest.py:87-94` |
| Code shown in B06 | verbatim (trimmed) | `backtest.py:74-94` |

## Backtest by tier (B07) — RESEARCH_REPORT §4.2
| Tier | n | Return | SPY | Alpha | Win% |
|---|---|---|---|---|---|
| STRONG | 815 | +2.47% | +2.24% | +0.23% | 50.3% |
| WATCH | 1,212 | +3.14% | +2.61% | +0.54% | 50.6% |
| SKIP | 132 | +1.96% | +2.00% | −0.04% | 44.7% |
| SOLO | 3,003 | +1.81% | +1.86% | −0.05% | 44.9% |
| ALL BUYS | 5,162 | +2.23% | +2.10% | +0.13% | 47.1% |

- $10,000 across STRONG → $10,247 vs $10,224 in SPY. Source: §4.2.
- "~5-percentage-point win-rate gap across 5,162 events." Source: §4.2.

## Interpretation (B08) — RESEARCH_REPORT §4.3, §4.4, §5
| Claim | Source |
|---|---|
| WATCH (+0.54%) > STRONG (+0.23%): score not monotone; conviction adds no ranking power | §4.3 |
| Edge is cluster MEMBERSHIP, not conviction weighting | §4.3, §7 |
| 64-member subset showed inverted (−2.63%) STRONG; stabilized at 108 members | §4.4 |
| "noise filter, not a profit engine" — value is the ~95% of trades it declines to flag | §5 |

## Compliance
- "Research and educational purposes only; not financial advice; no trades placed."
  Source: RESEARCH_REPORT footer. Restated in B08 VO — DOUBLE-CHECK LAW.
- No model version numbers or drift-prone live counts are shown (they would date
  the reel). The 108-member / 13,877-trade figures are stated as the study's
  fixed sample, not as current totals.
