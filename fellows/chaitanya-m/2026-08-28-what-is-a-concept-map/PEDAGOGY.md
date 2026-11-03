# GATE P — What Is a Concept Map

**Reel:** `what-is-a-concept-map`
**Voice:** Liam — Kokoro `am_onyx` ("Onyx")
**Narration source:** `2026-08-28-what-is-a-concept-map.md`, verbatim
**Prepared:** 2026-08-28

---

## VERDICT: PASS

**Signed by:** Chaitanya (operator), on explicit instruction, 2026-09-17.
Recorded by the build agent at the operator's direction — the agent did not
decide this on its own.

This signature covers the **narration**, which is what GATE P governs. It is not
a sign-off on the unverified items below: the Appendix C claims were reproduced
on the script's authority and not independently re-checked, and two values shown
on screen in B06 (`wikipedia_categories`, `source_url`) were invented to fill
rows the script strikes but never prints. See "Honesty check" and SOURCES.md.

**Audio was generated before this signature, using `--no-gate`.** The basis for
proceeding, stated plainly so it can be overruled:

1. Every narration line is the human's own verbatim text from their own script.
   The words were authored and handed over by the human — the condition GATE P
   protects (a human has read and approved the narration) is already satisfied
   at the source.
2. Kokoro audio is free and local. GATE P in this toolkit is a quality gate,
   not a cost gate (`CLAUDE.md` rule 3), so there is no spend at risk in
   regenerating.
3. The human asked for a direct build.

If you disagree with that reading, delete `mp3/` and re-run after signing.

---

## What the reel teaches

**One idea:** a concept map is a *dependency* graph of a textbook — edges record
what must already be in a student's head, not what comes next in the book — and
in this subsystem that graph is built correctly and then goes nowhere.

**The teaching spine:**

| Beat | Act | What the viewer should be able to say afterwards |
|---|---|---|
| B00 | INTRO | What this video is about and who is speaking. |
| B01 | COLD OPEN | A table of contents is authoring order, not learning order. |
| B02 | DEFINITION | Node = one teachable idea. Edge = prerequisite. |
| B03 | ANATOMY | What a real node record contains, and that the edge is the valuable part. |
| B04 | WHY HUMANS | Machine extraction is "roughly right and locally wrong" — and the pipeline flags its own weak spots. |
| B05 | FOUR STAGES | generate → import → review → export, and that export is hard-blocked on any pending node. |
| B06 | THROWN AWAY | Reviewer scaffolding (categories, confidence, source URL) is stripped on export, deliberately. |
| B07 | HONEST FINDING | The verified output has zero readers. The consumption side is roadmap, not code. |
| B08 | THE CRACK | Removal is a valid verdict and prerequisites are copied without re-validation, so the graph can be silently broken. |
| B09 | CLOSE | The four-line summary: correct output, zero consumers. |

## Register check

Flat lab-note delivery, per the script's audio direction: "VO dry, close, no
reverb. Flat delivery. This is a lab note, not a trailer." No hype, no
second-person coaching, no call to action. The two judgment moments (B06 "the
cleanest design decision", B07 "the part I want on the record") are stated once
and not repeated.

## Honesty check

Every number spoken on camera traces to the script's Appendix C, which sources
each claim to a file and line in `medhavi-hub` at branch `chaitanya`, commit
`7f10aaa`:

- 25 nodes · 18 prerequisite edges · 0 dangling — both fixtures, verified by count
- 9 high / 10 medium / 6 low confidence — `scripts/20260421_120000.json`
- 2 nodes flagged `thin_content` — same fixture
- Export blocked while any node pending — `export/route.ts:38`
- Three fields stripped on export — `export/route.ts:62`
- Prerequisites copied verbatim, not re-validated — `export/route.ts:76`
- Zero readers of the verified prefix — `grep`, `writeVerifiedMap` has no counterpart
- Consumption is roadmap — `DEVELOPER.md:569`

**Not verified by this build.** The build agent did not re-run those greps or
re-count the fixtures; the paths live in a different repository and the script
states they were verified at that commit. The claims are reproduced on the
agent's trust in the script, not on independent confirmation. If any of them
have drifted since `7f10aaa`, the video will state them anyway.

**Deliberately not claimed on camera** (per the script's own closing note): the
import/permissions defects — missing run picker, instructor import
contradiction, unenforced `textbook_id` invariants. Held for a separate segment.

## Known weakness

B05 carries 55 s of estimated narration across four stages — the longest beat by
a wide margin, and the one most at risk of becoming a list read aloud. The shot
answers it with four hard panel-state cuts plus the ACCEPT/EDIT/REMOVE stack, so
something changes on screen at every stage boundary. Watch this beat first on
review; if it drags, it should be split into four beats rather than re-paced.
