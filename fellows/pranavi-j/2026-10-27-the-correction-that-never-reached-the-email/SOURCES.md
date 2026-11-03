# Sources — The Correction That Never Reached The Email

This is a real Project 29 (`mycroft`) engineering report, not a general topic explainer. Every
on-screen claim traces to this week's real fix in the repo, not an external source.

1. **`scripts/regulatory-intel/workflow.dev.json`** (`Layer 2 - LLM Re-Score` node) — the real
   `jsCode` that reviews any item with `urgency_score > 6` and writes back `llm_reviewed`,
   `llm_verdict`, `llm_corrected_impact_level`, `llm_downgrade`. Shown verbatim in B03. Read
   directly from the file on disk this session (read-only, not modified).
2. **`scripts/regulatory-intel/workflow.dev.json`** (`Generate Email` node, current/post-fix
   state) — the real, current bucketing logic: `effectiveImpact()` and the two filter lines that
   use it. Shown verbatim in B04. Also the source for B03's pre-fix lines, reconstructed by
   programmatically undoing the exact fix diff (confirmed to match exactly once — see
   `verification/verify_effective_severity.mjs`).
3. **`scripts/regulatory-intel/workflow.dev.json`** (`High Priority Filter` node) — the real
   `n8n-nodes-base.if` conditions (`urgency_score > 6`, `llm_downgrade === false`), confirming the
   filter only gates on the binary downgrade flag, never on the corrected label. Used in B03's
   framing.
4. **`scripts/regulatory-intel/C3-VERIFICATION.md`** — this week's own write-up of the bug, the
   fix diff, and the verification table (`critical_count`/`high_count` before and after). Used
   verbatim in B04's diff and cross-checked against this session's own harness in B05.
5. **`/Users/pranavijs/mycroft/logs/RUN_LOG.md`**, entry dated `2026-10-27` ("Project 29
   regulatory workflow: C3 fix") — the Recipe/Inputs/Commands/Outputs/Result/Open-issues framing
   this video's B01–B06 follow. The "Open issues" line (the separate, unfixed `get_stats()`
   dashboard defect, 57/411 rows) is quoted in B06's second honest-limit card.
6. **`verification/verify_effective_severity.mjs`** and
   **`verification/verify_effective_severity_output.txt`** (this project folder) — the live
   Node.js `vm` harness built and run this session: extracts the real `jsCode` from the
   `Generate Email` node in `workflow.dev.json` on disk, shims `$("High Priority Filter").all()`
   to return a 3-item synthetic batch matching the 3 real cases `C3-VERIFICATION.md` describes, and
   separately reconstructs the pre-fix version by undoing the exact diff. Used verbatim in B05.
7. **`scripts/regulatory-intel/B5-VERIFICATION.md`**, **`B6-VERIFICATION.md`** — the two earlier
   fixes already closed in this same `Generate Email` node, named (not detailed) in B06's first
   honest-limit card as "the two earlier fixes already closed in this node."
8. **`scripts/regulatory-intel/C2-VERIFICATION.md`** — the prior fix that introduced
   `Layer 2 - LLM Re-Score` and its fields, named in this video's continuity framing (B01/BEAT-SHEET)
   as the step whose stated purpose C3 makes actually work for the first time.

No external (non-`mycroft`) sources used. No real third-party product, vendor, or individual named.
The regulator/agency names that appear in example field values in this project's own data
(SEC, CFTC, FINRA) are the pipeline's own existing, already-public source labels, not a claim about
any specific agency's filings.
