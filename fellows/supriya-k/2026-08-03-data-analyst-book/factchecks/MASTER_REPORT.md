# Fact-Check Master Report — Data Analyst Interview Preparation

*Phase 4. Run date: 2026-07-15. Covers all 10 chapters after the human rewrite (GATE 3).*

## Method

Each chapter was scanned for checkable assertions. Most content is **definitional or mechanical** (what a JOIN returns, what a p-value is, how STAR is structured) — these are anchored to the Phase-1 Wikipedia sources and need no re-verification. The **uncertain specifics** flagged in Phase 1 (`[verify]` / `[UNVERIFIED]`) were web-verified against authoritative vendor/official docs. Practice questions were audited against the original-questions rule.

> **Note on `facts.json` routing.** The canonical `facts/facts.json` at the repo root belongs to the *AI1 CLI* book. To preserve book isolation (P6 — canonical flows downstream, never back), findings for this book are recorded here in `factchecks/` rather than written into the root dictionary. If this book becomes its own repo, it gets its own `facts/`.

## Verified claims (previously flagged)

| # | Claim | Chapter | Verdict | Source |
|---|---|---|---|---|
| 1 | VLOOKUP lookup value must be in the leftmost column; **approximate match is the default** | 6 | **CONFIRMED** | Microsoft Support, VLOOKUP function |
| 2 | XLOOKUP **defaults to exact match** | 6 | **CONFIRMED** | Microsoft Support, XLOOKUP function |
| 3 | `COUNTIFS(criteria_range1, criteria1,…)`; `SUMIFS(sum_range, criteria_range1,…)` (sum range first) | 6 | **CONFIRMED** | Microsoft Support, COUNTIFS / SUMIFS |
| 4 | MySQL: CTEs since 8.0.1, window functions since 8.0.2 | 4 | **CONFIRMED** | dev.mysql.com (8.0 Reference Manual) |
| 5 | PACE framework originates in **Google's** Advanced Data Analytics program | 8 | **CONFIRMED** | Google Advanced Data Analytics (Coursera) |

**Result:** no factual errors found. All five flags resolved as CONFIRMED; chapters updated to drop the hedge tags and add inline citations ([^xlfns], [^xllookup], [^mysqlver], [^pace]).

## Definitional claims (anchored, no web re-check needed)

| Chapter | Anchored to |
|---|---|
| 3 (SQL I) | Wikipedia: SQL; Join (SQL) |
| 4 (SQL II) | Wikipedia: Window function (SQL) |
| 5 (Statistics) | Wikipedia: Statistical hypothesis test; A/B testing — **p-value phrased to avoid the common misinterpretation** (checked) |
| 6 (Spreadsheets) | Wikipedia: Pivot table |
| 7 (pandas) | Wikipedia: pandas (software) |
| 9 (Behavioral) | Wikipedia: STAR method |
| 1, 2, 8, 10 (process) | `blueprint-trends-notes.md` (2026 career-guide sources) — labeled as process description, not technical fact |

## Original-questions audit

Every practice question uses an **invented scenario** — FreshCrate (meal-kits), Loopr (streaming), library-checkouts, conference-signups, a food-delivery A/B test, a ride-share case. No question is copied from or references any external bank (grep for LeetCode / StrataScratch / Glassdoor / HackerRank / InterviewQuery: **none found**). Generic *question types* (e.g. "how would you measure the success of feature X?") are phrased originally around invented features. **Original-questions rule upheld.**

## Citations resolve

All external citations point to live pages fetched during Phases 1 and 4 (Wikipedia articles; Microsoft Support; dev.mysql.com). No dead or hallucinated links.

## Outstanding

- None blocking. Code examples (MySQL, pandas) are standard and were reviewed for correctness; they are additionally exercisable by a reader. If desired, a future pass could run each code block against a live MySQL 8.0 / pandas instance for belt-and-suspenders confirmation.
