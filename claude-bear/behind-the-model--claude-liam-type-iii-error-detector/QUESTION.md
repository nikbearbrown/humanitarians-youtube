# QUESTION

**The question:** If Claude's answer technically satisfies what I asked, how do
I tell whether it solved the right problem?

**Mode:** redo — source is
`anthropics/youtube/behind-the-model/claude-liam-type-iii-error-detector/beat_sheet.json`
("Type III Error Detector — Wrong Problem, Right Solution," Teardown-register
CLI-explainer, `brand: "claude-liam"`, cold open `NikBearBrownOpen`, ASK/CODE
terminal beats, a Manim OUTPUT table beat, a CHANGE revision beat, SUMMARY,
NEXT STEPS, `YOURTURN`, `ClaudeTitleOutro`). The source is a CLI walkthrough
(write a script that generates reframings and runs a distinctness test on
them); the facts carry forward, compressed out of the terminal/code beats
and into the hai-simple ten-beat Plain spine — no script is written or run
on screen, the method is explained directly.

**Why it earns a reel:** the natural assumption is that if an answer
literally satisfies the problem as stated, it's a good answer. But an AI is
particularly good at exactly this failure — optimizing the objective you
wrote down, not the one you meant. The concrete case that breaks the
assumption (source B01/B04): ask Claude to cut support-ticket volume, and
"hide the contact button" is technically correct — the ticket count drops —
while the underlying need (people who can't get help) is untouched. Howard
Raiffa's name for solving the wrong problem correctly is Type III error.

**Naive framing (B00, corrected on screen):** "Did Claude get the answer
wrong?" → corrects "answer" to "problem" (the real frame: check whether the
problem was wrong, not whether the answer satisfies it).

**Body facts carried from source (unchanged):**
- AI is particularly good at Type III errors: it optimizes the objective you
  stated, not necessarily the one you meant (source B01)
- the anchor: "reduce support ticket volume" → "hide the contact button" —
  technically correct (ticket count drops), completely wrong (source B01)
- the reframing/distinctness test: state the problem several genuinely
  different ways, write a candidate answer for each framing, then test each
  answer against the OTHER framings (source B02/B03)
- if an answer designed for one framing also satisfies every other framing,
  the framings never actually differed — that convergence is the Type III
  warning sign (source B04: the "improve search UX" answer passed all three
  framings, and row three was "not distinct")
- the fix when framings collapse is to add another genuinely different
  framing (source B05: the "constraints" move — what's blocking
  self-service) and re-run the test; some of the framings become distinct
  again (source B06: three of four distinct)
- the test does not prove you found the right problem — it proves your
  framings were different from each other, which is necessary before any of
  them is worth trusting, not sufficient (source B07)

**Compression, per the constitution/IVP/IAG redo precedent:** ten beats —
B00 (writer) + B01–B06 (body) + BCRY + BHTF + BOUT. B01 plants the anchor
(the support-ticket ask and its technically-correct-but-wrong answer) and
states the Type III fact; B02 states the wrong guess (does the answer
satisfy the ask? yes, so it looks solved); B03 breaks it with a second
honest framing of the same problem and states the reframing mechanism's
first half; B04 states the mechanism's second half (test every answer
against every framing; convergence is the warning); B05 covers direction A
(divergent answers don't prove you found the right problem, only that the
framings genuinely differed); B06 covers direction B (convergence doesn't
mean no better answer exists — add another framing) and pays off the
anchor with the search-UX fix.

**No inference flag.** Every claim here describes a design practice — how
to state a problem multiple honest ways and test candidate answers against
each framing — rather than an empirical claim about model internals needing
a hedge. Per `simple`'s ONE-FLAG LAW ("if the source genuinely supports
everything, there is no flag"), this document records that instead of
forcing a flag where none is needed.
