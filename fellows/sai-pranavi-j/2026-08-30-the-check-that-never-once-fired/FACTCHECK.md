# FACTCHECK — The Check That Never Once Fired

Status: **RESOLVED — fellow reviewed 2026-08-30. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B05 | "A check specifically written to catch CFTC filings... caught none of them" / "every single one of the twelve real CFTC filings came back mislabeled" | PASS, **with required framing** | `B2-VERIFICATION.md` "Live verification" — 12/12 items from the live CFTC feed, tested 2026-08-30 | Narration must frame this as *today's live test result* ("tested against every real CFTC item I could pull live," "twelve real filings, tested today"), not "this rule has never worked in production" — we have no historical log of every past run, only today's measurement. Beat sheet draft already uses this framing; keep it. |
| 2 | B03 | The CFTC-detection condition as quoted | PASS | Verbatim from `workflow.dev.json` prior to commit `d59fbd5` | — |
| 3 | B04 | Example title/link (Swap Execution Facility Order Book Requirement...) has no "CFTC" in title, no agency slug in link | PASS | `B2-VERIFICATION.md`, pulled live 2026-08-30 | — |
| 4 | B05 | "Eighty-three of the hundred forty-six items... were actually other agencies... also called 'Securities'" | PASS | `B2-VERIFICATION.md` table, live test 2026-08-30 | — |
| 5 | B05 | "The three feeds that were already working... didn't change at all" | PASS | `B2-VERIFICATION.md` table: SEC 0/25, FINRA 0/100, Investment Advisor 0/100 | — |
| 6 | B06 | Fix description (`dc:creator`-based classification) | PASS | `B2-VERIFICATION.md` "The fix"; `workflow.dev.json` post-fix | — |
| 7 | B07 | "A safeguard that's never once tested against real input isn't protecting anything" | PASS | Editorial takeaway, consistent with the demonstrated mechanism; not a factual claim requiring a source | — |
| 8 | *(implicit, not in script)* | That this misclassification ever caused a real downstream error (a wrong alert sent, a wrong report shown to a human) | **NOT CLAIMED — do not add** | `B2-VERIFICATION.md` and `SOURCES.md` are explicit: this measures classification behavior on a live test, not the fellow's actual hand-built n8n run history | Keep the script scoped to "the classifier mislabels items" — do not narrate or imply a specific past incident (a bad alert, a wrong report) that hasn't been observed |

## Dramatization check

No beat invents a crash, an outage, or a specific past incident that didn't happen. The main risk
in this reel is overstating "never once fired" from a single-day test into a permanent historical
claim about the pipeline's entire run history — the beat sheet draft already scopes every mention
to "tested live today" / "pulled live" language. This file exists to make that a reviewed,
deliberate choice.

## Resolved 2026-08-30

1. **Live-test framing** (row #1): current wording ("tested live today," "pulled live") confirmed
   sufficient — no additional on-screen date caption needed.
2. **No implied incident** (row #8): confirmed — the script stays scoped to "the classifier
   mislabels items on a live test," no claim of an actual past bad alert or report.

Both open items are closed. Gate P (narration review) can proceed.
