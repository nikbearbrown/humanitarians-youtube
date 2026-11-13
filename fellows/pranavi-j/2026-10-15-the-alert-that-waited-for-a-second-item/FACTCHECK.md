# FACTCHECK — The Alert That Waited for a Second Item

Status: **RESOLVED — fellow reviewed 2026-10-15. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | `Generate Email`'s `hasData` guard requires `newItems.length > 1` | PASS — verbatim, confirmed via `grep -o "newItems.length > 1"` returning exactly 1 match in `workflow.dev.json` before the fix | `scripts/regulatory-intel/workflow.dev.json`, `Generate Email` node, pre-fix | — |
| 2 | B03/B04 | A single new high-priority item fails this check and falls to the empty-result branch, which has nowhere to go downstream | PASS — traced the `If` node's connections directly; its true-output connection array is `[]` | `workflow.dev.json` node graph | — |
| 3 | B04 | The fix is `newItems.length > 1` -> `newItems.length > 0` | PASS — exact diff applied and committed (`f9eed1e`) | `B6-VERIFICATION.md` | — |
| 4 | B05 | Live before/after harness table (0/1/2 items) | PASS — real measured output from running the exact extracted `jsCode` via `new Function('$', code)`, both before and after the patch, then re-run against the real patched file on disk | `B6-VERIFICATION.md` verification table | — |
| 5 | B06 | "I don't have evidence this specific case ever occurred on a real run" | PASS — true; this pipeline is not instrumented to log per-run item counts at that granularity, and no live-run evidence was claimed or fabricated | — | Must stay phrased as an honest limitation, not softened into implying it was caught live |
| 6 | B06 | A related `Regulatory_QA` / `source_feed` compatibility gap exists, flagged but not fixed | PASS — confirmed live: `SourceFeed('Federal Register - Department of Labor')` raises `ValueError` against the real `Regulatory_QA/backend/app/models.py` enum; not yet triggered in practice because the frontend doesn't currently pass `source_feed` as a query param, but a real latent gap | Investigation notes from this week's search for the next fix | Keep framed as "identified, not yet fixed" — do not claim it's resolved |

## Dramatization check

No beat claims this bug caused an actual missed alert on a real historical run — explicitly the
opposite, B06 states plainly this was caught by code review, not by an incident. No invented
statistics (e.g. no claim about how often exactly-1-item runs occur in practice — not measured,
not stated).

## Open items (resolve before Gate P)

None identified — all claims trace directly to `B6-VERIFICATION.md` and this week's RUN_LOG entry,
both already written against live-verified evidence.
