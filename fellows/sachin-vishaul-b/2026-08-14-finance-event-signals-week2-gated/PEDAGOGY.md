# PEDAGOGY — "Claude, Gated." (Week 2)

Narration sign-off record. Audience: same as Week 1 — curious what building
real guardrails into a data pipeline looks like, not a distributed-systems
expert.

## The one thing this video has to land

**A gate is only real if it's enforced with evidence, not asserted.** The
GIGO gate is proven with four real reject cases, not a description of its
rules. The human gate is proven by literally hitting it three ways (no
reviewer, one clear, a repeat clear) and reading off the real status codes.

## Act structure

| | |
|---|---|
| B00 cold open | ✓ Both gates named up front |
| B01 framework | ✓ The chain stated before any example |
| B02-B04 first cycle | ✓ Ask → real reject-path code → four real rejected test cases |
| B05-B07 revision | ✓ A real LangGraph bug → the real fixed line → real clean-run numbers |
| B08 falsifiability | ✓ The 88% withhold rate — a real, named limit of the offline model, not a caveat |
| B09 summary | ✓ Gates down 6→3, still DRAFT — building and clearing are different jobs |
| B10 handoff | ✓ Three concrete API calls + expected status codes (400/200/409) |
| B11 outro | ✓ Title restate + sign-off |

## Why the LangGraph bug beat looks different from Week 1's

Unlike Week 1 (two full commits to diff), this bug and its fix landed in
the same commit — there's no "before" commit to diff. The CODE beat shows
only the real, current, fixed line (including its own inline comment
documenting the bug), narrated from the project's own logged account,
rather than reconstructing a fabricated "before" snippet.
