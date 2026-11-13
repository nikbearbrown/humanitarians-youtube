# PEDAGOGY — The Context Window Isn't Memory (claude-hai, 12-beat / 60s cut)

**Reworked from the 9-beat/154.5s long cut to match the Brutalist
first-project spec (60s, 12 beats — see the on-screen example prompt in
`youtube/brutalist/claude-liam-brutalist-your-first-project/`).** Same
thesis, facts, sources, Bella voice (`af_bella`), `@HumanitariansAI` branding.
This is a fresh gate pass — the long cut's PASS verdict does not carry over
to materially different content.

Thesis (unchanged): a context window is a fixed, shared token budget for one
turn — not persistent memory — and what happens when it fills up is
application-defined, not one universal mechanism.

## Act structure
- B00 cold open, ask lands answered (COLD OPEN LAW). Hook rewritten to open
  on the memory misconception directly: "long chats seem to forget... it's a
  budget, not memory" ✓
- B01 executive summary via `BrutalistHesitantWriter` — same correction
  ("Claude's memory" → "a fixed budget") as the long cut, single line only
  (the stakes line was cut for length; see SHOTLIST.md) ✓
- B02–B08 body, seven short beats instead of four longer ones — the same
  four ideas from the long cut (shared layers, tokens ≠ words, the ceiling,
  bigger ≠ better), with the layers idea split across two beats (B02/B03) ✓
- B06 restores "context rot" as an explicit tendency ("recall can slip past a
  point") — cut from the long cut's B00 for length, put back here per this
  pass's instruction ✓
- Handoff (B10) carries a real prompt AND one concrete check — thinner than
  the long cut's three-point rubric, but still a real criterion, not "ask
  Claude about X" ✓
- Summary (B09) restates the thesis verbatim, as this pass required: "a
  context window is a fixed, shared budget — not memory. Bigger isn't
  automatically better." ✓
- Title-restate outro (B11), `OutroSeries` — replaces the long cut's
  `OutroCTA`, which failed GATE T (see SHOTLIST.md) ✓

## Register discipline
- No hedging language outside the one still-flagged inference point (B05,
  token density by content type — see BUILD-LOG.md item 2; unchanged from
  the long cut, no on-screen disclaimer, per prior explicit instruction).
- No design judgment — B09 is headed "Summary," not "Verdict."
- HAI greeting word-budget honored: "Hi, Bella."

## Evidence discipline
Full fact-by-fact table with sources: `FACTCHECK.md`. No claim was added or
changed by the 60s compression — only cut, merged, or reworded for length.
The one wording change this pass made to a *claim* (not just a cut) is B09:
"Bigger doesn't mean better" → "Bigger isn't automatically better," matching
the long cut's B08 phrasing exactly — no new claim, a consistency fix.

## Friction protected
- Kept: the app-dependent ceiling framing (B07: error / summary / dropped
  turns) even compressed to three words — the long cut's earlier correction
  (this was once wrongly "oldest turns always dropped") stays fixed, not
  reverted under space pressure.
- Kept: the one unsourced claim (B05, token density) rather than deleting it
  — still true and useful, still logged as inference, not presented as fact.
- Cut, disclosed, not hidden: WORKED EXAMPLE and FALSIFIABILITY are
  measurably weaker in this cut than the long cut. See CHECKS-REPORT.md.

## Known open items
See CHECKS-REPORT.md (two disclosed checklist weaknesses) and BUILD-LOG.md
item 2 (B05's inference flag, no on-screen disclaimer). B04's Manim scene
is simplified from the long cut — still text-plus-bar only, no token-cost
table. SOURCES.md carries the full source list and compression log.

VERDICT: PASS.
