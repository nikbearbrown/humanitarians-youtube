# FACTCHECK — The Correction That Never Reached The Email

Status: **RESOLVED — fellow reviewed 2026-10-27. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B03 | `Layer 2 - LLM Re-Score` writes back four fields on every item it reviews: `llm_reviewed`, `llm_verdict`, `llm_corrected_impact_level`, `llm_downgrade` | PASS — verbatim read of the node's `jsCode`, the `results.push({ json: { ...json, llm_reviewed: true, llm_verdict: verdict.verdict, llm_corrected_impact_level: verdict.corrected_impact_level, llm_reasoning: verdict.reasoning, llm_downgrade: isDowngrade } })` block (and the parallel `llm_reviewed: false` branches for not-reviewed/error cases) | `scripts/regulatory-intel/workflow.dev.json` ("Layer 2 - LLM Re-Score" node) | — |
| 2 | B03 | `Generate Email`'s pre-fix bucketing read only `i.json.impact_level`, never `llm_corrected_impact_level` | PASS — confirmed via `grep` that `llm_corrected_impact_level` is written in exactly one place (`Layer 2 - LLM Re-Score`) and, pre-fix, read nowhere in the repo (per `RUN_LOG.md`'s 2026-10-27 entry); the pre-fix two-line bucketing shown in B03 is reconstructed by undoing exactly the diff in `C3-VERIFICATION.md`'s "The fix" section, confirmed to occur verbatim once in the real post-fix file before being substituted back (see `verification/verify_effective_severity.mjs`) | `scripts/regulatory-intel/workflow.dev.json` ("Generate Email" node); `C3-VERIFICATION.md` | — |
| 3 | B03 | `High Priority Filter` only gates on `urgency_score > 6` and `llm_downgrade === false` — it does not look at `llm_corrected_impact_level`, so a confirmed-but-recategorized item still passes through to `Generate Email` | PASS — verbatim read of the node's `conditions` (`n8n-nodes-base.if`, `number: urgency_score > 6`, `boolean: llm_downgrade === false`) | `scripts/regulatory-intel/workflow.dev.json` ("High Priority Filter" node) | — |
| 4 | B04 | The fix is one helper, `effectiveImpact()`, preferring `llm_corrected_impact_level` when `llm_reviewed` is true and a correction exists, falling back to `impact_level` otherwise; `criticalItems`/`highItems` now filter on `effectiveImpact(i)` | PASS — exact diff matches `C3-VERIFICATION.md`'s "The fix" section and the real, current `jsCode` in `workflow.dev.json` on disk, confirmed by reading the live node directly (not from the markdown alone) | `scripts/regulatory-intel/workflow.dev.json` ("Generate Email" node, current state); `C3-VERIFICATION.md` | — |
| 5 | B04 | Items never sent to the LLM (`llm_reviewed: false`, below the `urgency_score > 6` review threshold) are unaffected — they fall through to the original `impact_level`, exactly as before | PASS — direct reading of `effectiveImpact()`: the ternary's condition requires `item.json.llm_reviewed` to be truthy before it ever reads `llm_corrected_impact_level`; an unreviewed item (`llm_reviewed: false`) always falls to the `: item.json.impact_level` branch | `scripts/regulatory-intel/workflow.dev.json` ("Generate Email" node) | — |
| 6 | B05 | Live before/after Node.js harness table: a 3-item batch (confirmed+recategorized, confirmed+unchanged, never-reviewed); pre-fix `critical_count: 2, high_count: 1`; post-fix `critical_count: 1, high_count: 2`; items 2 and 3 unchanged in both | PASS — real output from this session's own harness (`verification/verify_effective_severity.mjs`), captured verbatim in `verification/verify_effective_severity_output.txt`. The post-fix code path is the real, current `Generate Email` `jsCode` extracted directly from `workflow.dev.json` on disk (read-only, not modified), executed in a sandboxed Node `vm` with `$("High Priority Filter").all()` shimmed to return the synthetic batch. The pre-fix path is built by programmatically undoing the exact post-fix block (string substitution, confirmed to match exactly once before trusting it) rather than retyping a reconstruction from memory. These counts match `C3-VERIFICATION.md`'s own independently-reported table (`critical_count: 2, high_count: 1` before; `critical_count: 1, high_count: 2` after) exactly, corroborating both this session's harness and the original investigation. | Narration/table must not claim a specific count of real historical emails affected in production — not measured, not shown |
| 7 | B06 | Honest limit 1: this fix only changes `Generate Email`'s bucketing — `Layer 2 - LLM Re-Score`'s own logic, `High Priority Filter`'s `llm_downgrade` gate, and the two earlier fixes already closed in this node (B5's under-reported sources, B6's dropped-on-exactly-1-item bug) are untouched | PASS — verbatim from `C3-VERIFICATION.md`'s "What's NOT touched" section; corroborated by reading the current `jsCode` for `Layer 2 - LLM Re-Score` and the `High Priority Filter` conditions directly — neither was edited by the C3 diff | `C3-VERIFICATION.md`; `scripts/regulatory-intel/workflow.dev.json` | — |
| 8 | B06 | Honest limit 2: a separate, unrelated defect was found the same week in `Regulatory_QA/backend/app/crud.py`'s `get_stats()` — dashboard stats re-bucket by raw `urgency_score` with cutoffs that disagree with the `impact_level` column, affecting 57 of 411 real rows; not fixed this week | PASS — verbatim from `RUN_LOG.md`'s 2026-10-27 entry, "Open issues": "A related, separate defect was also found this week in `Regulatory_QA/backend/app/crud.py`'s `get_stats()` ... 57/411 real rows land in a different tier ... Not fixed this week; candidate for a future week." Not independently re-verified this session (not re-run against the live 411-row dataset) — carried forward as stated in the real run log, phrased as a found-but-not-fixed open issue, not a claim this session re-measured it | Must stay phrased as "found, not fixed this week," not folded into this video's own fix claim |
| 9 | B07 | Takeaway: "a correction that's computed but never read isn't a correction" | PASS — editorial framing of the mechanism established in B03/B04, not a new factual claim requiring separate citation | — | — |

## Dramatization check

No beat claims this bug ever caused a real human operator to act on a wrong severity in a real
incident, or states how many historical alert emails were actually affected — B05's harness is a
3-item synthetic batch built to cover every real case this node sees (confirmed-recategorized,
confirmed-unchanged, never-reviewed), not a claim about production email history. The separate
`get_stats()` defect (B06) is clearly flagged as found-but-not-fixed this week, not folded into the
claim of what C3 actually closed. No invented statistics beyond what `RUN_LOG.md` and
`C3-VERIFICATION.md` state.

## Continuity with this fellow's prior reports

This is the third fix in the `Generate Email` node this cycle — after B5 (under-reported sources)
and B6 (dropped-on-exactly-1-item), both already covered in earlier weekly reports — and the second
bug specifically in the Layer 2 LLM pipeline C2 introduced. B06's first honest limit names both
predecessor fixes explicitly so this continuity is visible on screen, not just asserted in
narration.

## Resolved 2026-10-27

1. Confirmed every quoted field name, code line, and diff against the real, current
   `workflow.dev.json` on disk and `C3-VERIFICATION.md`, not from memory or paraphrase.
2. Confirmed B05's harness table by actually running `verification/verify_effective_severity.mjs`
   this session and cross-checking its output against `C3-VERIFICATION.md`'s own independently
   reported table — both agree exactly.
3. Confirmed B06's second honest limit (the `get_stats()` defect) is carried forward verbatim from
   `RUN_LOG.md`'s "Open issues" line, not re-measured or escalated this session.

Gate P (narration review) can proceed.
