# PEDAGOGY — State Is The Hard Part (Part 2)

GATE P: narration reviewed before audio. Lean by design — act structure in
`CHECKS-REPORT.md`, evidence in `FACTCHECK.md`. This file records **what
difficulty was kept because it IS the lesson, and what was cut as extraneous.**

## Act structure — checked, detail in CHECKS-REPORT.md

Cold open with RESULT lines ✓ · hesitant-writer BLUF at B01 ✓ · framework before
examples (B02 before B03–B09) ✓ · worked example (B10) ✓ · falsifiability (B11) ✓ ·
verdict (B12) ✓ · handoff read aloud and discussed (B13) ✓ · title-restate outro ✓.

ILLUSTRATE LAW: UI at B00, B12, B13, B14 only. The seven pattern beats differ by
topology — fan-and-converge, three-way split, gated chain, monitored chain,
three-way classify, suspended checkpoint, retrieval pipeline.

## Friction protected

**KEPT — the thesis is an interpretation, and it is stated as a claim.** "State
is the hard part" is not a sentence in the source; it is our synthesis of seven
separately-named bottlenecks. The easy version would present it as if the book
said it. Instead the reel argues it — B02 sets it up, each beat supplies a piece,
B12 closes it — and `FACTCHECK.md` flags it as interpretation. A viewer can
disagree with the thesis and still have learned all seven patterns.

**KEPT — B11, again arguing against the reel.** One task, one user, one session:
skip all seven. Sharper here than in Part 1, because these patterns cost standing
infrastructure — a vector store to reindex, an alert matrix to tune, a review
queue someone must actually staff. Naming the maintenance cost is what stops this
from being an architecture-astronaut video.

**KEPT — "your latency is now human response time" (B08).** The unglamorous
consequence of human-in-the-loop. Easy to omit, and omitting it is how HITL gets
adopted and then quietly removed six weeks later.

**KEPT — the denoise step as the accent of B05.** The narration says plainly that
this is the step people skip. Calling out the commonly-skipped step by name is
more useful than a neutral walkthrough.

**CUT — the two formulas.** The source gives a composite retrieval score
(`w1·similarity + w2·recency + w3·frequency`) and a σ-threshold for drift. B04
teaches the *idea* — score on all three, never similarity alone — without the
weights, and B06 shows the threshold as a chip rather than an equation. At ~20s
per beat a formula would consume the beat and teach less than the sentence does.
EQUATIONS.md-style tangents exist for when an equation earns a beat group; these
did not.

**CUT — named vendor technologies.** The source names MCP, Redis, RabbitMQ,
Celery, Jira. On screen these became "shared store", "vector store", "queue".
Vendor names date a video faster than anything else and none of them is the
lesson. The one exception is keeping "read-only" literal in B03 and Part 1's
B07, because the specific permission is the safety mechanism.

**CUT — the source's Orchestration Matrix table.** It is a good summary, and B12
already is one. Two summary beats in a row would be a slideshow.

**CUT — the Kanban/Jira metaphor for multi-agent coordination.** An analogy that
needs its own explanation is a tax, not a shortcut. The shared-store diagram
carries it directly.

## Register

HAI Plain. Continuous with Part 1: same voice (`af_sarah`), same structure, same
honest-cost discipline. The reel assumes Part 1 but does not require it — B00
restates the premise in one line for a cold viewer.

VERDICT: PASS
