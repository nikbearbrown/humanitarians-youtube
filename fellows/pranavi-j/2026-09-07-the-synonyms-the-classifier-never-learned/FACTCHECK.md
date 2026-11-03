# FACTCHECK — The Synonyms the Classifier Never Learned

Status: **RESOLVED — fellow reviewed 2026-08-31. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | "Eighteen real items... still landing in Unknown Source" / Google News lacks `dc:creator` | PASS | `UNKNOWN-SOURCE-INVESTIGATION.md` "Starting point" — 18 items live 2026-08-30 (note: `FINDINGS.md` from 2026-07-24 recorded 21 — doc explicitly notes feed content changes daily, this is expected drift, not an error) | Narration should say "eighteen, as of this investigation" if precision matters — beat sheet already scopes to a specific measured count, not an eternal claim |
| 2 | B04 | The two example titles (recoverable "Exempt Reporting Advisers" one, not-recoverable "FCA Decision Notice" one) | PASS | Quoted verbatim from `UNKNOWN-SOURCE-INVESTIGATION.md`'s two example lists | — |
| 3 | B05 | The fix code (2 new regex/substring checks) and the before/after table (18→8, all 5 feeds) | PASS | `UNKNOWN-SOURCE-INVESTIGATION.md` "The fix" and "Live verification (2026-08-30)" — full table there | — |
| 4 | B05 | "Zero items that were already correctly labeled got reclassified" | PASS | Explicit in source doc: "zero unexpected reclassifications of items that were already correctly labeled something other than 'Unknown Source'" | — |
| 5 | B06 | The remaining 8 are framed as a deliberate tradeoff, not an unsolved bug | PASS, **framing must be preserved** | Source doc is explicit: "This was the explicitly-flagged tradeoff before starting this investigation... Left open." Not framed as a TODO or promise. | Narration must NOT say "I'll fix this next" or imply an active plan to close the remaining 8 — the source material treats this as a closed, deliberate decision, not an open task |
| 6 | B06 | "FCA Decision Notice" example — UK regulator, correctly out of scope | PASS | `UNKNOWN-SOURCE-INVESTIGATION.md` "Not recoverable from title alone" — explicit example given | — |
| 7 | B07 | "Not every fix should chase a hundred percent" | PASS — editorial takeaway, consistent with the demonstrated mechanism; not a factual claim requiring a source | — | — |

## Dramatization check

No beat invents a crash, an incident, or overstates the fix as complete. The main risk in this
reel is understating or overstating the remainder — either implying the 8 remaining items are a
bug still to be fixed (source doc explicitly frames it as a deliberate stop) or implying the fix
recovered more than 10/18. Both are guarded against in the beat sheet draft above.

## Resolved 2026-08-31

1. **B06 "deliberate tradeoff" framing** (row #5): kept as drafted — no objection raised, no
   wording change.
2. **"Eighteen" count** (row #1): confirmed fine stated plainly, no on-screen date qualifier
   needed — same pattern as prior reports' live-snapshot counts.

Both open items are closed. Gate P (narration review) can proceed.
