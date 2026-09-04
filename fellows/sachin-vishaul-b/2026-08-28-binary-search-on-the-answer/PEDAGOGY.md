# PEDAGOGY — "Claude, Halved."

Narration sign-off record. Audience: someone actively grinding LeetCode who
knows classic binary search but hasn't connected it to "search the answer
space" problems.

## The one thing this video has to land

**The hard part is recognizing a monotonic predicate hiding in a problem —
once you see it, the binary search itself is boilerplate.** The video
spends more weight on "how do you know this pattern applies" (B02, B05)
than on the mechanical loop itself (B04).

## Act structure

| | |
|---|---|
| B00 cold open | ✓ Distinguishes this from classic array search immediately |
| B01 executive summary | ✓ One breath: a one-time flip is binary-searchable |
| B02 framework | ✓ The answer-range model, before any example |
| B03 worked example | ✓ The canonical instance (ship capacity), concretely simulated |
| B04 mechanism in motion | ✓ The halving loop, shown mechanically |
| B05 falsifiability | ✓ Non-monotonic predicates silently break the pattern — the single most common real bug applying it |
| B06 verdict | ✓ States recognition as the real skill, not the loop |
| B07 handoff | ✓ A concrete task with a self-check (print the feasibility sequence, confirm one flip) |
| B08 outro | ✓ Title restate + sign-off |

## Why B05 is the most important beat, not a footnote

Binary-search-on-the-answer is a pattern that looks correct even when
applied wrong — it terminates and returns *a* value, just not the right
one, if monotonicity fails. B05 is given a full beat (side-by-side
monotonic vs. non-monotonic sequences) rather than a caveat line precisely
because this is where real solutions go wrong.
