# PEDAGOGY — "Claude, Ingested." (Week 1)

Narration sign-off record. Audience: a smart non-technical-to-intermediate
viewer curious what "building a real data pipeline with Claude Code" looks
like day to day — not a distributed-systems expert.

## The one thing this video has to land

**A pipeline that's honest about failure is worth more than one that looks
clean.** Two real bugs get shown breaking on camera and get fixed on
camera; one design flaw (the lookback window) gets disclosed rather than
smoothed over. The viewer should leave believing the "97 events, 0
duplicates" claim specifically because they watched the replay test that
earned it.

## Act structure

| | |
|---|---|
| B00 cold open | ✓ "Namaste — this is Liam, in for Bear." Persona + series framing in the first breath |
| B01 framework | ✓ The 5-hop chain stated before any code — scaffold before mechanism |
| B02-B04 first cycle | ✓ Ask → real buggy code → real failure. The bug is shown, not summarized |
| B05-B07 revision | ✓ Change → real diff → real fixed-run numbers. THE REVISION LAW: at least one real cycle |
| B08 falsifiability | ✓ The lookback-window finding — a real design miss, not a caveat folded into narration |
| B09 summary | ✓ Recipe stays DRAFT — the lesson is that proving a spine and clearing gates are different jobs |
| B10 handoff | ✓ A scaffolded task with a checkable rubric (three concrete outcomes), not "try building a pipeline" |
| B11 outro | ✓ Title restate + "Liam, in for Bear" sign-off |

## Why the bugs are shown, not narrated

Per SHOW-DON'T-TELL: the CODE beats show the real `secclient.go` lines
(the manual `Accept-Encoding` header) and the real diff removing them —
never a description of what the bug "was." The OUTPUT beats show the actual
symptom text (`invalid character '\x1f'`) and the actual fixed-run counts,
not a narrated summary of them.
