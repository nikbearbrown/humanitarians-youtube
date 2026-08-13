# PEDAGOGY — Gate P (narration review before audio)

Episode 2 of 10 · *Agentic AI: From the Loop to MCP* · 2026-08-14

## The one idea

**The loop only works because the observation is real. Take the honest observation away
and you do not have an agent iterating — you have one guess, repeated at full price.**

## Why this episode is not a repeat of episode 1

Episode 1 looked at the loop from **outside** and asked *what is it*. Episode 2 goes
**inside a single pass** and asks *which part is doing the work*. The answer is
deliberately counter-intuitive: not the reasoning, which is what everybody focuses on, but
the observation, which is what everybody implements carelessly. Nothing from episode 1 is
re-explained — B00 restates the definition in one clause and moves on.

The episode also pays a debt: episode 1 asserted "the loop adds state, feedback, and a
stopping rule" and moved on. Episode 2 is where feedback and the stopping rule are
actually cashed out.

## Audience

Same as episode 1 — students and mid-career learners. The takeaway is deliberately
*something they can do*: three properties an observation must carry, and three stopping
rules they must write themselves. The HAI spine question lands at B09 and the verdict:
the stopping rules are yours, not the model's, which is the honest limit of the technique.

## Structure (13 beats, ~4 min, three acts)

1. **B00 cold open** — Onyx, the callback to episode 1, the ask answered in three lines.
2. **Act 1 — one turn, slowed down** (B01–B03): stop drawing the loop, run it → the
   anatomy of one pass (thought / action / observation, only one of which is reality) →
   a **real printed trace** from the shipped file, showing the same failed call recorded
   two ways.
3. **Act 2 — the observation is load-bearing** (B04–B07): the claim → the three things a
   good observation carries → the seven real lines of `record()` → what a loop without
   feedback actually is.
4. **Act 3 — how loops die** (B08–B09): the four death modes → the three stopping rules
   you have to write yourself.
5. **Verdict** (BVDT), **Your turn** (BHTF), **Outro** (BOUT) with the episode-3 promise.

## SHOW-DON'T-TELL check

- B03 is the spine of the episode and it is pure show: the viewer *reads* a real trace and
  sees `ok` sitting next to `ERROR FileNotFoundError: sales.csv`. The voice only reacts.
- B02's arc closes on itself; the observation feed is the single terracotta moment.
- B08's four chips land in narration order, with "false completion" held alone at the end.
- No beat survives the PPT test as a static slide. Typing appears only in B00 and BHTF.
- No two consecutive beats share a visual scheme (verified programmatically).

## Honesty notes confirmed at this gate

- [x] **B06 code is REAL and shown verbatim** — `record()` from `trace_loop.py`, in this
      folder, including the inline comment the narration points at. Line five is in fact
      the `except` line carrying that comment; checked, not assumed.
- [x] **B03's trace is REAL output**, captured from `python3 trace_loop.py` on 2026-08-13.
      The two observation *values* (`ok` and `ERROR FileNotFoundError: sales.csv`) are
      verbatim; the `(lazy)` / `(honest)` parentheticals are on-screen labels added for
      legibility and are disclosed in FACTCHECK.md.
- [x] **`trace_loop.py` extends episode 1's `agent_loop.py`** rather than replacing it,
      per the playlist's continuity rule — same loop, one thing changed.
- [x] **No version-dated claims.** No model, vendor, benchmark, or price appears.
- [x] **The verdict names a limit** (HAI honesty clause): a model cannot reliably tell you
      it is finished, so the stopping rules are the builder's responsibility.

## Verdict

- Plan (act map + lane histogram): APPROVED — 13/13 Remotion, zero slates.
- Narration (read every line aloud): APPROVED — body beats 41–54 words, inside budget.
- Fact-check (`FACTCHECK.md`): CLEARED.

> VERDICT: PASS (FINAL scope) — prepared by Onyx build agent under the fellow's standing
> delegation for this series (2026-08-13). Unlocks audio and the clean master render.
>
> This sign-off does **not** authorize publishing. That remains a separate, explicit
> human decision.
