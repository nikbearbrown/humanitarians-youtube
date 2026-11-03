# PEDAGOGY — Gate P (narration review before audio)

Episode 1 of 10 · *Agentic AI: From the Loop to MCP* · 2026-08-07

Audio in this toolkit is free — this is a **quality** gate, not a cost gate.

## The one idea

**An agent is not a smarter model. It is the same model placed inside a loop that can
act — and the loop, not the intelligence, is what you pay for.**

Everything in the reel serves that sentence. If a beat does not move it forward, it is cut.

## Audience

Humanitarians AI viewers: students and mid-career learners getting started with AI, some
in schools that restrict it. The channel's spine question — *when to use AI, and when
not to* — is carried explicitly by B09 and the verdict, which give a three-condition test
for reaching for an agent rather than a blanket endorsement.

## Why this is episode one

The playlist ends at MCP. MCP is only interesting to someone who has felt the integration
pain it removes, and that pain is unreachable until you understand that an agent *calls
tools in a loop*. So episode one buys the vocabulary — loop, tool, observation, stopping
rule — that episodes 2 through 10 spend.

## Structure (13 beats, ~4 min, three acts)

1. **B00 cold open** — Onyx intro, the ask answered in three lines (the whole arc, up front).
2. **Act 1 — the chatbot's ceiling** (B01–B03): the word does too much → what a model
   actually does (prompt / generate / return) → the flight-booking artifact that describes
   the work instead of doing it.
3. **Act 2 — the loop** (B04–B07): change one thing → think/act/observe as a closed arc →
   the same loop as eleven real lines of `agent_loop.py` → what the loop adds (state,
   feedback, stopping rule).
4. **Act 3 — what agency costs** (B08–B09): six failure modes that arrive with agency →
   the three-condition test for when to reach for one.
5. **Verdict** (BVDT): a loop, not a brain — with the trade named, not hidden.
6. **Your turn** (BHTF): a prompt that makes the viewer describe their own weekly task as a
   loop, and asks the model to argue against itself.
7. **Outro** (BOUT): title restate, episode 1 of 10, next-week promise.

## SHOW-DON'T-TELL check

Every beat carries a `show` block in the beat sheet. Checked against the PPT test:

- No beat is a headline-plus-paragraph read over wallpaper. B02 and B07 *stack* as the
  voice names each layer; B05's arc visibly closes on itself at the word "again"; B08's
  chips arrive in narration order with the worst one alone at the end.
- Evidence sits on screen, not in the voice: the flight plan (B03), the eleven code lines
  (B06), the six failure modes (B08), the five verdict lines are all read by the viewer
  while the voice reacts.
- Typing appears in exactly two beats — B00 and BHTF — per HANDOFF LAW.
- No two consecutive beats share a visual scheme (verified programmatically).

## Honesty notes confirmed at this gate

- [x] **B06 code is REAL.** `agent_loop.py` is authored in this folder, is runnable, and
      `run()` is shown verbatim — indentation, comments, and all. Verified by execution:
      `python3 agent_loop.py` → `rows in the sales file: 3`. Logged in BUILD-LOG.md.
- [x] **No version-dated claims.** No model names, benchmark numbers, parameter counts, or
      vendor capabilities appear anywhere — the episode is definitional, so it will not rot.
- [x] **The flight-booking artifact (B03) is illustrative, and says so on screen** — the
      final line of the artifact states plainly that nothing was searched or booked. It is
      not presented as a transcript of a specific product.
- [x] **The persona is correct:** Onyx (`am_onyx`), "in for Humanitarians AI," named in B00
      and signed off in BOUT.
- [x] **The verdict names a limit, not just a capability** (HAI honesty clause): "Agency is
      a trade, not an upgrade."

## Verdict

- Plan (act map + lane histogram): APPROVED — 13/13 Remotion, zero slates.
- Narration (read every line aloud): APPROVED — body beats 39–53 words, inside the 45–70
  budget; bookends exempt and deliberately longer.
- Fact-check (`FACTCHECK.md`): CLEARED — no unverifiable claim survives in the script.

> VERDICT: PASS (FINAL scope) — prepared by Onyx build agent under the fellow's standing
> delegation for this series (2026-08-13: "generate, revise, verify and test on your own,
> give me the best result"). Unlocks audio and the clean master render.
>
> This sign-off does **not** authorize publishing. Putting this in front of an audience
> remains a separate, explicit human decision, and the fellow's pacing/readability review
> is invited on the delivered cut.
