# PEDAGOGY — "Claude, Traced." (Week 3)

Narration sign-off record. Audience: same as Weeks 1-2.

## The one thing this video has to land

**"It's configured correctly" and "it's proven to work" are different
claims, and this video says which one it's making at every step.** The
trace propagation and the chaos test earn "proven" (real trace shown, real
kill-a-pod test run). The HPA only earns "configured correctly" — and the
video says so instead of blurring the two.

## Act structure

| | |
|---|---|
| B00 cold open | ✓ Both halves of the week named up front |
| B01 framework | ✓ Why Kafka needs manual header work, stated before the code |
| B02-B04 first cycle | ✓ Ask → real kafka.go → a real Jaeger trace, not a description of one |
| B05-B07 revision | ✓ A real k8s bug → the real fix → a real chaos-test result |
| B08 falsifiability | ✓ The HPA finding — the strongest honesty beat in the whole series, a real recorded limit |
| B09 summary | ✓ States plainly that two wins and one gap isn't a promotion |
| B10 handoff | ✓ The chaos test itself, restated as a scaffolded viewer task |
| B11 outro | ✓ Title restate + sign-off |

## Why the readiness-probe bug beat looks like Week 2's, not Week 1's

Same shape as the Week 2 LangGraph bug: fix landed in the same commit as
the original manifest, no "before" commit to diff. B06 shows only the real,
current fixed wait-loop, narrated from the project's logged account.
