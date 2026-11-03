# FACTCHECK — `ai-data-engineering-etl`

DOUBLE-CHECK LAW. Every on-screen and spoken claim, verdicted. This reel makes
**mechanism claims only** — no vendor benchmarks, no adoption statistics, no model
version numbers, nothing that dates.

Beat ids below are the ids of the **signed 10-beat cut** (the standalone E/T/L
beat was dropped at GATE P; see `PEDAGOGY.md` → "GATE P amendment").

| # | Beat | Claim | Verdict | Basis / fix applied |
|---|---|---|---|---|
| 1 | B01 | "Extract and load are easy — the transform in the middle is where the weeks go" | ⚠️ SIMPLIFICATION — kept, and framed as one | Extract and load have real operational complexity (pagination, CDC, idempotency, backpressure). The claim is about where the *semantic* decisions live, not where all effort lives. The line says "where the weeks go", not "the only hard part". The on-screen verdict matches the spoken line exactly. |
| 2 | B01 | The six chores (rename, cast, null-guard, dedupe, retry/backfill, reconcile) | ✅ TRUE | Each is a standard, non-optional step in a typed source→warehouse load. Nothing here is a vendor-specific artefact. |
| 3 | B03 | `text` → `timestamptz` requires an explicit parse | ✅ TRUE | A text column carries no format guarantee; a typed timestamp target must interpret it. `pd.to_datetime(..., utc=True)` in B04 is the applied fix. |
| 4 | B03 | `float8` → `numeric(12,2)` is "a rounding bug waiting for month-end" | ✅ TRUE (as a risk claim) | IEEE-754 binary64 cannot represent most decimal fractions exactly; conversion to a fixed-scale decimal must round, and aggregation compounds it. Stated as a risk ("waiting for"), never as an observed incident. |
| 5 | B03 | `int NULL` → `int NOT NULL` — "nulls have nowhere to go" | ✅ TRUE | A NOT NULL constraint rejects the row; the pipeline must choose (default, drop, or quarantine). B04 quarantines rather than drops, and says so in a comment. |
| 6 | B03 | "Twelve columns line up. Three do not." | ⚠️ ILLUSTRATIVE — captioned on screen | A **worked example**, not a measured migration. The footnote *"Worked illustrative example — not a measurement of a real migration."* renders inside the beat, and the same 15/12/3 split is stated in B00's output lines. |
| 7 | B03, B00 | "Claude found all three. It decided none of them." | ✅ TRUE as stated | A claim about detection vs. resolution, not about accuracy. The on-screen counter reads `3 flagged · 0 resolved` and the second number never moves off zero — the visual *is* the claim. |
| 8 | B04 | The code shown is the code described | ✅ TRUE | ACTUAL-CODE LAW: `transform.py` is real, runnable pandas, trimmed to the lines that teach — nothing pseudocoded. Its three edits map 1:1 onto the three flags raised in B03. |
| 9 | B05 | The "genuinely good at" list | ✅ TRUE | Each item is a well-established, cheap-to-verify text task: mapping named fields, boilerplate, test scaffolds, stack-trace explanation. No success rate is asserted for any of them. |
| 10 | B05 | The "cannot do for you" list | ✅ TRUE | Each item requires facts absent from the schemas: business semantics, contractual commitments, downstream guarantees. Framed as "cannot do **for you**" (ownership), not "cannot produce text about". |
| 11 | B06 | "The pipeline runs clean… while a bad cast quietly rounds every amount the wrong way" | ⚠️ CONSTRUCTED SCENARIO — kept, framed as a failure *mode* | Built directly from claims 4 and 5, which are mechanism facts. The narration says "here is the failure this creates", never "this happened". No company, no incident, no loss figure. |
| 12 | B06, B07 | "A pipeline that runs is not a pipeline that is right" / "Row count is not correctness" | ✅ TRUE | Cardinality and value fidelity are independent properties; a row-count reconciliation cannot observe a value transformation. This is the standard argument for value-level assertions. |
| 13 | B07 | "writing just got free, and reading did not" | ✅ TRUE as an argument | An asymmetry claim, presented as the episode's judgment, not as data. |

## Things deliberately NOT claimed

- No "X% productivity gain" figure. None is defensible and all of them date.
- No model name or version performance claim.
- No named vendor's tool is praised or criticised.
- No currency amount for the B06 drift — the on-screen text reads
  "quietly drifting · no alarm exists for this", not a fabricated number.
- No claim that the row counter's `48,210` is a real workload. It is a stand-in
  number whose only job is to lock and turn green.

## Corrections applied during scripting

1. An earlier draft of the risk beat said the total was "off by ₹0.004 a row".
   **Removed** — a specific figure implies a measurement that does not exist.
   Replaced with the qualitative "quietly drifting · no alarm exists for this",
   and the scene deliberately carries no magnitude axis.
2. An earlier draft said Transform is "the only hard part". **Softened** to
   "extract and load are easy — the transform in the middle is where the weeks
   go" (see claim 1).
3. An earlier draft of the verdict beat said AI takes you "from two schemas to a
   working transform in an afternoon instead of a fortnight". **Cut** in the GATE
   P shortening — and it should have gone anyway: it is an unsourced speed claim,
   and the reel is stronger without it.
