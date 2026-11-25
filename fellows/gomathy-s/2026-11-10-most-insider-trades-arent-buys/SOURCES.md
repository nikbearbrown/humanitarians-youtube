# SOURCES — Most Insider Trades Aren't Buys

All study numbers come from the **committed** Mycroft insider-signals files at
`mycroft-work` commit **fed487c** (`git show fed487c:insider-signals/<file>`).
The working tree has uncommitted ENRICH work (`enriched_buys.csv`,
`enrich-audit.md`, Rules 7–9, an edited `status.md`); **none of it is used**.
Paths below are relative to `insider-signals/` in the Mycroft repository (commit fed487c is on [GomathySelvamuthiah/mycroft](https://github.com/GomathySelvamuthiah/mycroft), branch `feature/insider-trading-signals`).

No return, price-move, outperformance or "signal works" result is stated or
implied anywhere in the reel. None has been computed (`PRE_REGISTRATION.md`,
"Not yet registered": ENRICH outcomes and SIGNALS labels are not computed).

## Study numbers

| On screen | Spoken | Value | Source file | How |
|---|---|---|---|---|
| B02, B03, B06, B09 | "almost a million" | **999,542** Form 4 rows | `data/raw/parsed/<q>_parse_summary.json` × 14 (2023q2 … 2026q3), field `form4_rows`; also `data/verified/conformance-audit.md` "All" row | summed across the 14 files; equals the audit's "All" row |
| B02 | — | 14 quarters, Q2 2023 – Q3 2026, by filing date | the 14 parse summaries; `status.md` l.17 ("study period 2023 Q2 – 2026 Q3") | SEC data-set quarters are filing-date quarters |
| B03 | — | S 301,979 (30.2%), A 217,494 (21.8%), F 170,600 (17.1%), M 143,930 (14.4%), other 83,199 (8.3%) | 14 parse summaries, per-code counts | summed; % = count / 999,542; "other" = remainder (asserted in `scenes.py`) |
| B03, B09 | "about eight percent" | P **82,340** (8.2%) | 14 parse summaries, code P count; conformance-audit.md "All" row (Code P) | summed |
| B04 | — | **−3,845** failed checks | 14 parse summaries: price missing/≤0 3,296; P but not "acquired" 284; shares missing 250; trans_date after filing 11; equity-swap 4 | 82,340 − 78,495 = 3,845 = 3,296+284+250+11+4 (asserted) |
| B04, B05 | "about seventy-eight thousand" | **78,495** qualifying buys | parse summaries (`qualifying`); conformance-audit.md "All" row; `status.md` l.17 ("78,495 buys promoted") | |
| B05 | — | Repeat amendments **−699** | conformance-audit.md "All" row (Rule 2 collapsed) and l.144 | |
| B05 | "private deals, employee plans" | **−3,032** | conformance-audit.md "All" row (Rule 1) | |
| B05 | "late filings" | **−4,028** (filed > 30 calendar days after trade) | conformance-audit.md "All" row (Rule 3); rule text `PRE_REGISTRATION.md` Rules 2–5 table | |
| B05 | "stocks under a dollar" | **−5,630** (price < $1.00) | conformance-audit.md "All" row (Rule 4); rule text `PRE_REGISTRATION.md` | |
| B05 | — | 10b5-1 plan buys kept, flagged (4,404 cannot make a cluster STRONG) | conformance-audit.md l.130; `PRE_REGISTRATION.md` Rule 1 table | count not shown on screen |
| B05 | — | joint filing = one insider | `PRE_REGISTRATION.md` Rule 5; conformance-audit.md l.130 | |
| B06, B09 | "about sixty-five thousand" | **65,106** eligible buys | conformance-audit.md "All" row and l.130 | 78,495 − 699 − 3,032 − 4,028 − 5,630 = 65,106 (asserted) |
| B06 | "six and a half percent" | 65,106 / 999,542 = 6.51% → **6.5%** | computed from the two rows above | asserted in `scenes.py` |
| B06 | — | **4,146** issuers · **38,320** filings | conformance-audit.md l.130 | |
| B07 | "twenty-five random buys … no errors beyond rounding" | **15** exact, **10** rounding only, **0** other | conformance-audit.md "Spot-check against the individual filings" (l.1450–1452; seed 16486067862572434945, full 14-quarter sample); `logs/RUN_LOG.md` l.26, l.42–43 | |
| B07 | — | Equifax: filed $166.1941, data set $166.19 | conformance-audit.md spot-check table row 6 (accession 0001225208-23-009811) | |
| B08 | "Every filter was fixed before any return was computed"; card "Filters fixed first / Before any returns" | the B05 filters are Rules 1–4 (Rule 2 amendment linking refined by 2a, 2b); Rules 1, 2–5, 2a, 6 registered 2026-11-04, 2b on 2026-11-05, each "before any prices, returns, clusters or scores were computed"; Amendments: "None" | `PRE_REGISTRATION.md` header (l.9, l.12–18), rule headings (l.23, l.51–54, l.89–91, l.102–105), Amendments | |
| B08 | "Changing one later would void the test" | "A rule changed after outcomes have been seen voids the backtest, and the change must be logged under Amendments" | `PRE_REGISTRATION.md` l.5–6 | |
| B09 | "hasn't been tested" | no outcome computed | `PRE_REGISTRATION.md` "Not yet registered"; `status.md` at fed487c (ENRICH not run) | |

Underlying data: SEC, *Insider Transactions Data Sets*,
https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets
(quarterly `<q>_form345.zip`).

## Form 4 facts (checked against SEC's own pages)

| Beat | Claim | SEC source |
|---|---|---|
| B01 | A Form 4 reports a change in an insider's beneficial ownership, not only buys | Form 4 (SEC 1474, 03-26), https://www.sec.gov/files/form4.pdf, General Instruction 1(a): "a transaction resulting in a change in beneficial ownership"; Investor Bulletin (SEC Pub. No. 137), https://www.sec.gov/files/forms-3-4-5.pdf: insiders report "purchases, sales, and holdings" |
| B01 | Due within two business days | Form 4 Gen. Instr. 1(a): "before the end of the second business day following the day on which a transaction … has been executed"; Investor Bulletin: "within two business days following the transaction date" |
| B01 | "Insider" = officers, directors, > 10% holders | Investor Bulletin |
| B03 | S = sale, A = grant/award, F = payment of exercise price or tax with securities, M = option exercise/conversion | Ownership Form Codes, https://www.sec.gov/edgar/searchedgar/ownershipformcodes.html; Investor Bulletin code table |
| B04 | P = "Open market or private purchase" | Form 4 Gen. Instr. 8, code list; Ownership Form Codes page |
| B05 | 10b5-1 plan trades are marked on the form | Form 4 instruction 10 (Rule 10b5-1(c) checkbox) |

## INFERENCE / editorial simplifications (labelled)

- **"almost a million"**: rounding of 999,542. **INFERENCE (rounding).**
- **"about eight percent", "about seventy-eight thousand", "about sixty-five thousand", "six and a half percent"**: spoken roundings; the exact figures are on screen. **INFERENCE (rounding).**
- **"Transactions"** is used for Form 4 *non-derivative table rows*. One filing can hold several rows; the derivative table is not counted. The B02 meta line says "Non-derivative table · Form 4 only". **INFERENCE (terminology).**
- **"Tax/exercise payments (F)"** glosses SEC's "Payment of exercise price or tax liability by delivering or withholding securities". **INFERENCE (plain-English label).**
- **"employee plans"** (B05 narration) covers Rule 1's ESPP and DRIP flags. DRIP is dividend reinvestment, not strictly an employee plan; the screen says "ESPP, DRIP". **INFERENCE (simplification).**
- **"Then filters remove … "**: Rule 2 repeat amendments are *counted once* (collapsed into the original), not dropped as bad data. The screen shows the −699 as "Repeat amendments". **INFERENCE (simplification).**
- **"Most aren't buys"** is a share-of-rows statement (91.8% of rows aren't code P). It says nothing about what buys predict.
- **"no errors beyond rounding"**: a 25-buy sample, not a census. **INFERENCE (sample).**
- **"We checked"** (B07): the spot-check was run in Gomathy's audit (`logs/RUN_LOG.md` l.26, l.42–43; conformance-audit.md l.1450–1452). "We" means the audit, not the narrator. **INFERENCE (attribution).**
- **"buys are left to test"** (B06): 65,106 is the eligible set the pre-registered test will draw on. "Left to test" describes the planned test; no test has been run (B09). The screen keeps the term "eligible buys". **INFERENCE (framing).**
- **"Every filter"** (B08) means the eligibility filters shown in B05 (Rules 1–4). The items under "Not yet registered" (return window, role weights, size buckets, T_strong, the cluster definition) are scoring parameters, not filters, and none has been computed. **INFERENCE (scope).**
- **"Those are coded P"** (B04): "those" refers back to B03's purchases; P = "Open market or private purchase" (SEC row below).
