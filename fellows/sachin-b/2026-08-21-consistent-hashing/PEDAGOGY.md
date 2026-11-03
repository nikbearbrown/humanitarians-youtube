# PEDAGOGY — "Claude, Ringed."

Narration sign-off record. Audience: someone prepping system-design
interviews who has heard "consistent hashing" as a term but not seen the
actual ring mechanism.

## The one thing this video has to land

**A ring plus "next clockwise" gets you locality for free — small changes
stay small — but locality alone doesn't get you fairness. That needs
virtual nodes.** Both halves of that sentence are separate, necessary
claims; the video proves each with its own beat rather than asserting both
at once.

## Act structure

| | |
|---|---|
| B00 cold open | ✓ Frames the mechanism as the point, not the term |
| B01 executive summary | ✓ One breath: same circle, servers and keys |
| B02 framework | ✓ The ring model, before any example |
| B03 worked example | ✓ Four keys, concretely assigned |
| B04 dynamic case | ✓ The locality claim, proven by showing only one arc remap |
| B05 falsifiability | ✓ The fairness gap at small N — real, well-known, not a caveat |
| B06 verdict | ✓ States virtual nodes as required, not optional polish |
| B07 handoff | ✓ Three concrete steps (add a node, remove a node, add virtual nodes) with measurable outcomes |
| B08 outro | ✓ Title restate + sign-off |

## Why a hand-drawn ring, not a citation to a real system

The mechanism itself (the ring, the arc) is what's being taught, and it's a
pure algorithm — there is no "real screenshot" of a ring to show. Every
diagram performs the mechanism directly (REBUILD LAW).
