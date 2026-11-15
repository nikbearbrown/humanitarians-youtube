# FACTCHECK — Most Insider Trades Aren't Buys

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B01 | Form 4 = any change in an insider's holdings, due within two business days | ✓ PASS: verbatim Gen. Instr. 1(a) and Investor Bulletin | SEC form4.pdf; SEC Pub. No. 137 |
| 2 | B02 | 999,542 Form 4 rows, 14 quarters (Q2 2023 – Q3 2026, filing date) | ✓ PASS: 14 parse summaries sum = conformance-audit "All" row | Mycroft @ fed487c |
| 3 | B03 | S 30.2 / A 21.8 / F 17.1 / M 14.4 / other 8.3 / P 8.2 % | ✓ PASS: computed from the summed per-code counts; asserted in `scenes.py` | parse summaries |
| 4 | B04 | "Those are coded P": purchases carry code P = open market or private purchase | ✓ PASS: SEC code list | form4.pdf; ownershipformcodes.html |
| 5 | B04 | 82,340 P − 3,845 failed checks = 78,495 qualifying | ✓ PASS: failure reasons sum to 3,845 (price, shares, date, code/swap) | parse summaries |
| 6 | B05 | −699 / −3,032 / −4,028 / −5,630 under Rules 2, 1, 3, 4 | ✓ PASS: conformance-audit "All" row; order of application per PRE_REGISTRATION | conformance-audit.md |
| 7 | B05 | 10b5-1 plan buys kept and flagged; joint filing = one insider | ✓ PASS | PRE_REGISTRATION Rules 1, 5 |
| 8 | B06 | "About sixty-five thousand buys are left to test": 65,106 eligible = 6.5% of 999,542; 4,146 issuers; 38,320 filings | ✓ PASS: arithmetic asserted; counts from the audit. "Left to test" = planned, not run (INFERENCE, framing) | conformance-audit.md l.130 |
| 9 | B07 | "We checked" 25 random buys vs filing XML: 15 exact, 10 rounding only, 0 other; Equifax $166.1941 → $166.19 | ✓ PASS: full-period sample (seed 16486067862572434945); "we" = Gomathy's audit (INFERENCE, attribution) | conformance-audit.md l.1450–1461; RUN_LOG |
| 10 | B08 | Every filter (B05: Rules 1–4, with 2a/2b) fixed before any return computed; card "Filters fixed first / Before any returns"; a later change voids the backtest | ✓ PASS: Rules 2–5, 2a/6 and 2b say registered "before any prices, returns, clusters or scores were computed" (l.53, l.91, l.105); Rule 1 was registered 2026-11-04, when the file records "Not computed: prices, returns …" (l.12–18); Amendments "None"; "every filter" scoped to B05 (INFERENCE, scope) | PRE_REGISTRATION.md |
| 11 | B09 | Whether eligible buys predict anything hasn't been tested | ✓ PASS: no ENRICH/SIGNALS output at fed487c | PRE_REGISTRATION "Not yet registered" |
| 12 | all | No claim about returns or beating the market | ✓ PASS: none stated or implied | — |

Algebra checked separately from typography (MATH-TYPESETTING.md): B06
65,106 / 999,542 = 0.06514 → "≈ 6.5%" (rounding, hence ≈). B05 subtraction
chain exact. Spoken roundings and terminology simplifications are labelled
INFERENCE in `SOURCES.md`.
