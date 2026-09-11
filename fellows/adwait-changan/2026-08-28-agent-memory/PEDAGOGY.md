# PEDAGOGY — Gate P (narration review before audio)

*Agentic AI: From the Loop to MCP* · 2026-08-28
**First episode built under the PROOF standard and the HAI six-criteria PM gate.**

## The one idea

**An agent has no memory. It has a context budget it re-pays every single turn — so what
looks like forgetting is overflow, and eviction is a design decision you either make or
inherit.**

## HAI PM criteria — how this episode meets them

1. **Brutalist format** — `ai-explainer`, Claude skin, 13 beats, zero slates.
2. **4K at source** — mastered at 3840×2160.
3. **Both aspect ratios** — 9:16 derived via `./art shorts` after the 16:9 master locks.
4. **Formatting clean** — frame-level visual QC before master; mono tables sized against a
   computed wrap budget, not eyeballed.
5. **Intro line present, verbatim** — B00 opens *"Hi, I am Adwait Changan, and this video is
   about why agents do not actually forget."* This is the first episode to carry it; the earlier episodes
   open on the Onyx persona and **fail this criterion** until retrofitted.
6. **Real takeaway** — the viewer leaves able to measure their own agent's fixed cost and
   name their eviction policy. B08 is that rubric; BHTF makes them run it.

## PROOF compliance — the three gaps the earlier episodes had, closed here

- **Framework before examples.** B01 (the three-part budget) and B02 (re-sent every turn)
  both land before the first measured example at B03. the earlier episodes put an example first.
- **A falsifiability beat — B07.** The framework's obvious objection ("just use a bigger
  window") is *tested*, not waved away: doubling the budget moves first overflow from turn
  13 → 36 → 81 and never removes it. This is the beat all three previous episodes lacked.
- **Side-by-side in one frame.** B03 holds all eight turns together; B07 holds all three
  budgets together. Ep1 failed the production gate on exactly this.

## Structure (13 beats, ~4 min)

Hook (B00, with the intro line) → **framework shown** (B01–B02) → **worked example on real
numbers** (B03) → reframe (B04–B06: overflow not amnesia, the code, the four eviction
policies) → **falsifiability** (B07) → **reusable rubric** (B08–B09) → verdict → scaffolded
task → outro naming episode 5.

## Honesty notes confirmed at this gate

- [x] **Every figure on screen is a real measurement.** 903 characters of instructions, 88
      per observation, room falling 1009 → 393, overflow at turns 13 / 36 / 81 — all printed
      by `context.py`, which imports the earlier episode’s `tools.py` **unchanged**.
- [x] **Characters, not tokens — and the file says so in its own docstring.** The budget
      (2000) is deliberately small so the arithmetic is visible in four minutes. The
      narration never calls these tokens and never implies a real model's window is 2000.
- [x] **A false "never" was caught before audio.** `first_overflow()` originally capped at 40
      turns and reported `None` for the 8000-char budget, which would have put an incorrect
      "it never overflows" on screen. The horizon was raised to 500 and the real answer is
      turn 81. The falsifiability beat is only honest because that was fixed.
- [x] **B05 code is verbatim** via `inspect.getsource()`; the line count in the narration
      ("ten lines") was counted, not estimated.
- [x] **The verdict names the limit** — a bigger window buys turns, not a fix.

## Verdict

- Plan: APPROVED — 13/13 Remotion, zero slates, no consecutive pattern repeats.
- Narration: APPROVED — body beats 38–61 words.
- Fact-check (`FACTCHECK.md`): CLEARED.

> VERDICT: PASS (FINAL scope) — prepared by the build agent under the fellow's standing
> delegation for this series. Unlocks audio and the clean master render.
>
> Does **not** authorize publishing. Upload to Drive, notification of Shradha and Sanjana,
> and any YouTube action remain explicit human decisions.
