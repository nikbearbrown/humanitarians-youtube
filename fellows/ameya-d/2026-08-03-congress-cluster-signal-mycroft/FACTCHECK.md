# FACTCHECK.md — congress-cluster-signal

Every on-screen / narrated claim, its verdict, and its source. Full source table
in `SOURCES.md`. Primary source: `RESEARCH_REPORT.md` (Deshmukh, July 2026),
cross-checked against `market_adjusted.py` and `backtest.py`.

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B00 | 13,877 congressional trades backtested | ✅ TRUE | RESEARCH_REPORT §2 |
| B01 | STOCK Act (2012): disclose trades within 45 days | ✅ TRUE | §1; Public Law 112-105 |
| B01 | 13,877 trades · 108 members · May 2023–Jun 2026 | ✅ TRUE | §2 table |
| B02 | Return measured 30 days from the DISCLOSURE date | ✅ TRUE | §3.1 |
| B02 | alpha = trade 30d return − SPY 30d (matched window) | ✅ TRUE | §3.2; market_adjusted.py:92 |
| B03 | Code shown is the real `market_adjusted.py` (trimmed) | ✅ TRUE | market_adjusted.py:54-63, 91-92 |
| B04 | BUY: raw +2.23%, SPY +2.10%, alpha +0.13%, n=5,162 | ✅ TRUE | §4.1 |
| B04 | SELL alpha −0.01% | ✅ TRUE | §4.1 |
| B05 | Cluster = ≥2 politicians, same ticker, 30-day window | ✅ TRUE | §3.3; backtest.py:67-96 |
| B05 | signal_score = cluster_size × max BCR; tier at entry | ✅ TRUE | §3.4; backtest.py:80-94 |
| B06 | Code shown is the real `backtest.py: tag_signal` (trimmed) | ✅ TRUE | backtest.py:74-94 |
| B07 | STRONG n=815 α+0.23% win 50.3% | ✅ TRUE | §4.2 |
| B07 | WATCH n=1,212 α+0.54% win 50.6% | ✅ TRUE | §4.2 |
| B07 | SKIP n=132 α−0.04% win 44.7% | ✅ TRUE | §4.2 |
| B07 | SOLO n=3,003 α−0.05% win 44.9% | ✅ TRUE | §4.2 |
| B07 | $10k STRONG → $10,247 vs $10,224 SPY | ✅ TRUE | §4.2 |
| B07 | ~5-pt win-rate gap across 5,162 events | ✅ TRUE | §4.2 |
| B08 | WATCH (+0.54%) > STRONG (+0.23%): score non-monotone | ✅ TRUE | §4.3 |
| B08 | Edge is cluster membership, not conviction weighting | ✅ TRUE | §4.3, §7 |
| B08 | 64-member subset inverted (−2.63%); stable at 108 | ✅ TRUE | §4.4 |
| B08 | "noise filter, not a profit engine" | ✅ TRUE (interpretation) | §5 |
| B08 | research/education only — not financial advice | ✅ TRUE | RESEARCH_REPORT footer |
| B09 | Handoff prompt (last-90-days cluster rerun) | ✅ well-formed, runs against the same pipeline | derived from backtest.py |

**Corrections applied (DOUBLE-CHECK LAW):** none required — all figures matched
the paper and code on first pass. No model-version numbers or drift-prone live
counts are shown on screen; the 108-member / 13,877-trade figures are stated as
the study's fixed sample, not current totals.
