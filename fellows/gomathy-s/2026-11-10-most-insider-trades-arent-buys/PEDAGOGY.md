# PEDAGOGY — Most Insider Trades Aren't Buys (claude-hai, 12 beats / ~65 s)

Verdict: PASS — reviewed and approved by Gomathy. Self-check written by the builder after the review cuts; author reviewed and accepted the known weaknesses listed below. Applies to both cuts — vertical/ carries the same narration, with on-screen text shortened only where portrait width required it.

Thesis: most Form 4 rows aren't buys. Of 999,542 Form 4 transactions filed
Q2 2023 – Q3 2026, 82,340 (8.2%) are code P. After parse checks and four
pre-registered filters, 65,106 eligible buys remain (6.5%). Whether those buys
predict anything **has not been tested**. Primary source: Gomathy's Mycroft
insider-signals audit files at commit fed487c. Form 4 facts come from SEC's
Form 4 instructions and Investor Bulletin.

Audience (`claude-hai`): students getting started with AI and with reading
financial data. Spine question (when to lean on a tool and when not to) lands
in B07–B10: check the data against the filings, fix the rules before looking
at outcomes, and when you ask an AI about a Form 4, check that it read the
footnotes.

## Act structure

| Beat | Role | Self-check |
|---|---|---|
| B00 | Cold open, ask lands answered (COLD OPEN LAW) | ✓ the viewer's own question ("Is that a signal?"); the answer the reel gives is "count first", not "yes" or "no" |
| B01 | BLUF via hesitant writer | ✓ correction is the reel's misconception: "an insider buying" → "any change in an insider's holdings, due within two business days" (SEC verbatim). ✗ ~6.0 s, short of the ≥ 9 s the law asks for (same trade as p-value) |
| B02 | Framework: the denominator | ✓ 999,542 on screen; spoken "almost a million" (INFERENCE: rounding); 14 quarters on screen only |
| B03 | Most aren't buys | ✓ share by code, computed from the parse summaries; the spoken list of codes was cut for runtime, so the bars carry it |
| B04 | Real buys: code P → 78,495 | ✓ SEC's own definition ("open market or private") is on the card; the −3,845 row matches the parse-summary failure reasons |
| B05 | Pre-registered filters | ✓ the four exclusions with exact counts; the footer keeps 10b5-1 plan buys "kept, flagged", so "employee plans" in the narration can't be read as 10b5-1 |
| B06 | Eligible count | ✓ 65,106, and 65,106 / 999,542 ≈ 6.5% typeset with MathTex. Narration says "buys left to test" (planned test, not a result); the screen keeps "eligible buys" |
| B07 | Spot-check against the filings | ✓ 15 / 10 / 0 on screen, with one real example (Equifax $166.1941 → $166.19). ~ the narration summarises ("no errors beyond rounding") |
| B08 | Rules first | ✓ "Every filter was fixed before any return was computed" (B05 Rules 1–4 all registered before any returns); card "Filters fixed first"; a rule changed after outcomes are seen voids the backtest |
| B09 | Summary (verdict bookend) | ✓ "Returns: not tested / No result claimed" on screen and spoken |
| B10 | Your turn: prompt + one check | ✓ prompt read verbatim; check: "did it read the footnotes?" (footnotes are where ESPP/DRIP/private flags and 10b5-1 details live) |
| B11 | Title-restate outro | ✓ "Most Insider Trades Aren't Buys." Bella, in for Gomathy |

## Register (Plain)

- One idea per beat. Spoken numbers are rounded; the exact numbers are on screen.
- No return, alpha, "beats the market" or "signal works" language anywhere. B00 asks the question; B09 says it is untested.
- Hedges only where the source is an inference ("almost", "about"; the "employee plans" simplification; the 25-buy sample). Each is labelled in SOURCES.md.
- UI chip reads "Claude"; no model versions or dates in narration.

## Evidence discipline

Every number on screen is a constant in `scenes.py` (or a card prop), copied
from a named committed file and cross-checked by asserts (the subtraction chain,
the failure-reason sum, the percentages). SOURCES.md gives each number's file
and line. The uncommitted ENRICH/returns work in the Mycroft tree is not used.

## Known weaknesses (for the reviewer)

1. B01 runs ~6.0 s, short of the executive-summary law's ≥ 9 s.
2. "Transactions" means Form 4 *non-derivative table rows*. The B02 meta line says so; the narration doesn't.
3. "Employee plans" (B05 narration) covers ESPP and DRIP, but DRIP is dividend reinvestment. The screen shows "ESPP, DRIP".
4. B05 narration says "filters remove". Repeat amendments (−699) are actually collapsed into the original buy, not removed as bad data.
5. B07 narration summarises; the exact 15 / 10 / 0 split is on screen only. A 25-buy sample is not a census.
6. B03 is 2.9 s for six bars; dense for a first viewing.
7. Runtime ~64.7 s, not 60 s (Kokoro speed 1.08; the user chose trims over speed-up).
8. Portrait shortens some labels to stay at or above size 32 ("Registered Filters", "Private, ESPP, DRIP", "Over 30 days to file", "Tax/exercise (F)"); the Equifax name is dropped from the B07 example.
