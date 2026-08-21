# PEDAGOGY — Gate P (narration review before audio)

Episode 3 of 10 · *Agentic AI: From the Loop to MCP* · 2026-08-21

## The one idea

**A tool is not a function you expose — it is a contract you write in English. The model
reads the contract, never the code. So the description IS the tool.**

## Why this episode, now

Episodes 1 and 2 built a loop and made its feedback honest. Both took "it calls a tool" for
granted. This is where that gets paid for — and the payoff is deliberately counter-intuitive
for a programmer audience: the part you'd think is the tool (the function) is the one part
the model never receives.

It also sets up Episode 9. MCP standardises exactly this seam — name, description, schema.
A viewer who has felt how much weight the description carries will understand why a protocol
for it matters; one who hasn't will hear Episode 9 as plumbing.

## Audience

Students and mid-career learners. This is the most immediately *actionable* episode so far:
the takeaway is three questions every description must answer, plus a test they can run
today (read only the payload; if a stranger can't choose, neither can the model).

## Structure (13 beats, ~4 min, three acts)

1. **B00 cold open** — the ask answered in three lines: what crosses the wire, what doesn't,
   what that implies.
2. **Act 1 — what the model actually sees** (B01–B03): the bug is in the sentence, not the
   function → the three things that cross the wire → **the real printed payload**, ending on
   the line `not sent — the function body`.
3. **Act 2 — the description is the tool** (B04–B07): writing it *is* the work → the
   fourteen real lines that build the payload → the three questions a description must
   answer → **a real A/B**: identical function bodies, 13-character vs 292-character
   contract.
4. **Act 3 — what tools cost** (B08–B09): four prices every tool charges → the rule for
   writing one.
5. **Verdict** (BVDT), **Your turn** (BHTF), **Outro** (BOUT) with the episode-4 promise.

## SHOW-DON'T-TELL check

- B03 and B07 are the spine and both are pure show: real program output the viewer reads
  while the voice reacts. B03's last line (`not sent — the function body`) is the episode's
  thesis delivered by the program, not the narrator.
- B07 is a controlled experiment on screen: the `function bodies identical: True` line is
  the control, so the viewer can see that *only* the sentence changed.
- B02's arc completes toward "The model"; the `description` feed is the single terracotta
  moment.
- No beat survives the PPT test. Typing appears only in B00 and BHTF.
- No two consecutive beats share a visual scheme (verified programmatically). Pattern spread
  is the widest of the three episodes so far — nine distinct patterns across 13 beats.

## Honesty notes confirmed at this gate

- [x] **B05 code is REAL and verbatim** — `to_schema()` pulled from `tools.py` by
      `inspect.getsource()` at authoring time, so it cannot drift from the file. Line count
      checked programmatically: **14**, which is what the narration says.
- [x] **B03 is real output**, printed by `wire_view()`. The description is wrapped and
      elided *by the program*, which also prints the full character count — nothing is
      quietly hidden.
- [x] **B07's figures are real and were corrected during authoring.** An early draft claimed
      the two function bodies were "byte-for-byte identical" when they were not; the file was
      changed so the claim is true, and `tools.py` now *asserts* it on screen. The word count
      ("three words") and both character counts (13, 292) are measured, not estimated.
- [x] **The `audit()` heuristic is labelled as a heuristic**, in its own docstring and in
      FACTCHECK. It is a keyword check, not a linter, and the episode does not claim
      otherwise. Its first question was renamed "what it returns" during authoring because
      "Reads a file." *does* say what it does — the honest gap is that it never says what
      comes back.
- [x] **No claim about how any specific model behaves.** The episode describes the payload
      format and reasons about ambiguity; it never asserts what a model *did*, because
      nothing here calls one. No model, vendor, benchmark or price appears.
- [x] **The verdict names the cost** (HAI honesty clause): every tool charges context,
      ambiguity, blast radius and maintenance.

## Verdict

- Plan (act map + lane histogram): APPROVED — 13/13 Remotion, zero slates.
- Narration (read every line aloud): APPROVED — body beats 36–56 words, inside budget.
- Fact-check (`FACTCHECK.md`): CLEARED.

> VERDICT: PASS (FINAL scope) — prepared by Onyx build agent under the fellow's standing
> delegation for this series (2026-08-13). Unlocks audio and the clean master render.
>
> This sign-off does **not** authorize publishing. That remains a separate, explicit
> human decision.
