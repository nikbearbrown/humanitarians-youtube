# FACTCHECK — hai-agents-on-their-own

Status: **GATE F — drafted 2026-10-18. 3 rows VERIFIED-LOCAL, 3 rows SPEC-ASSERTED,
1 row ARGUMENT.**

Verdict vocabulary: **VERIFIED-LOCAL** = checked against first-party evidence produced on
this machine during the build. **SPEC-ASSERTED** = a general statement about how agent
software works; consistent with the local evidence but not checked against primary
documentation in this session. **ARGUMENT** = reasoning, not a measurement.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B01/B02 | An agent is the same model placed in a loop with the ability to act between turns; the pause for a human is what disappears | SPEC-ASSERTED | A description of the common agent architecture, consistent with the background-task evidence in row 3 | Confirm phrasing against a primary agent-architecture reference |
| 2 | B03 | Four terms: tool, loop, autonomy, guardrail | SPEC-ASSERTED | "Tool" and "guardrail" are directly evidenced in rows 3–5; "loop" and "autonomy" are descriptive | Keep as working definitions, not quoted standards |
| 3 | B04 | A long job ran unattended on this machine and reported its own completion — task `bvg1cuail`, exit code 0 | **VERIFIED-LOCAL** | Real background task from this build session; the id, status and exit code are the actual values | Re-capture if the id is stale at publish time |
| 4 | B05 | The system attaches a rule telling the agent that an automated event is NOT a message from the user and must not be read as acknowledgement or consent | **VERIFIED-LOCAL** | Quoted verbatim from the notification received in this session; line breaks added for the card, wording unchanged | Must stay verbatim — it is the point of the beat |
| 5 | B06 | Building the previous video, the toolkit refused to produce a final cut six separate times: missing paperwork, text outside the safe area, a glyph under the size floor | **VERIFIED-LOCAL** | Real gate output from the `hai-mcp-explained` build earlier today. Counted refusals: GATE F (×2), GATE T (×3), gate-v BLOCKER (×1) | The "six" is a count of actual refusals — recount if beats change |
| 6 | B06 | The toolkit cannot judge whether the film is good; it checks what a human already decided mattered | ARGUMENT | Interpretation of what the gates do. It is the project's own stated position — brutalist.art's README argues Claude "cannot watch the video" | Keep attributed as the project's position, not a proven fact |
| 7 | B07 | If you cannot say what would make it stop, it is not ready to run on its own | ARGUMENT | A judgement offered as advice, not a finding. Narrated as a test, not a citation | — |

## Honesty notes

- **Narration is AI-generated** (Kokoro `am_onyx`), disclosed aloud in B00.
- **Rows 3, 4 and 5 are first-party** — a real task event, a real guardrail string, and real
  gate refusals, all produced while making the companion video. None are reconstructions.
- **Row 5 is self-referential on purpose.** The evidence that an agent needs external limits
  is the set of limits that stopped this very build.
