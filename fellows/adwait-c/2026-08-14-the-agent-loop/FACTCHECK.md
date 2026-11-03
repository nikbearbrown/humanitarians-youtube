# FACTCHECK — Episode 2, "The Agent Loop"

DOUBLE-CHECK LAW. As with episode 1, this is definitional teaching material, so the
standard is *"does it survive a sceptical reading"* — plus, here, *"was it actually run"*,
because two beats show real program output.

| # | Claim (beat) | Verdict | Basis / fix |
|---|---|---|---|
| 1 | "One pass is three moves: thought, action, observation." (B00, B02) | **ACCURATE** | Definitional; the standard decomposition of a tool-using agent turn. Presented as the episode's frame, not attributed to a paper or vendor. |
| 2 | "Two of the three are the model talking to itself; only the observation is reality." (B02, B04, BVDT) | **ACCURATE** | Structurally true: the thought and the action are both model output. Only the observation originates outside the model. This is the episode's thesis and it is defended, not asserted. |
| 3 | B03 trace — THOUGHT / ACTION / OBSERVATION lines | **VERIFIED BY EXECUTION** | Captured from `python3 trace_loop.py`, run 2026-08-13. The THOUGHT and ACTION lines are verbatim. Both OBSERVATION *values* — `ok` and `ERROR FileNotFoundError: sales.csv` — are verbatim program output. |
| 4 | The `(lazy)` / `(honest)` labels in B03 | **ON-SCREEN ANNOTATION — disclosed** | These two parentheticals are **not** in the program output; they are added so the frame reads standalone. The honest observation's full printed form is `read_file({'path': 'sales.csv'}) -> ERROR FileNotFoundError: sales.csv`; the ACTION line directly above already carries the call, so the repeat was trimmed for legibility. No value was altered. |
| 5 | B06 code — `record()`, shown verbatim (B06) | **VERIFIED** | Reproduced character-for-character from `trace_loop.py`, including the inline comment. |
| 6 | "That is seven lines… the comment on line five." (B06) | **VERIFIED BY COUNT** | The `record()` block is 7 lines as shown (def, docstring, `try:`, `result =`, `except` + comment, `return` error, `return` value). The comment is on line 5. Counted against the rendered code string, not estimated. |
| 7 | "A good observation carries the call, the value, and the error verbatim." (B05, BVDT) | **EDITORIAL — the episode's recommendation** | This is the fellow's design guidance, not a cited standard. It is *demonstrated* rather than asserted: B03 shows what breaks when the error is dropped. Framed in the narration as advice. |
| 8 | "Swallow an error and the loop stops iterating; it starts repeating." (B07, BVDT) | **VERIFIED BY EXECUTION** | Not asserted — *run*. `run_lazy()` in `trace_loop.py` drives the real loop with the lazy recorder. Because a lazy observation carries no tool name, `think_names()` cannot tell what has already been tried, so it selects the same call every pass. The eight identical lines on screen in B07 are that program's actual output, not a mock-up. |
| 9 | "One guess, repeated eight times, at eight times the price." (B07) | **VERIFIED BY EXECUTION** | "Eight" is the default `max_steps = 8` carried from episode 1's `agent_loop.py`, and the run terminates at `stopped: step budget exhausted` — both visible on screen. The price claim is arithmetic given per-step billing, and is the one editorial word in the line. |
| 10 | Four ways a loop dies (B08) | **ACCURATE, framed as four named modes** | No progress, oscillation, budget exhaustion, false completion. Presented as "they die in four ways" with the caption "three of these are bugs, only one is a clean stop" — a taxonomy the episode owns, not a citation. |
| 11 | "A model cannot reliably tell you it is finished." (B09, BVDT) | **ACCURATE, deliberately scoped** | Claim is about *reliability*, not capability — models frequently do report completion, and the failure mode named at B08 is precisely when that report is wrong. Not a claim that self-assessment never works. |

## Corrections applied during authoring

- **Trimmed the duplicated call prefix in B03's honest observation.** The raw line repeats
  `read_file({'path': 'sales.csv'})`, which already appears on the ACTION line directly
  above; keeping both would have overflowed the artifact and taught nothing extra. Logged
  as row 4 above rather than silently shortened.
- **Changed "nine lines" to "seven lines" in B06 narration** after counting the rendered
  code string. The draft number was an estimate; the shipped number is a count.
- **Scoped the "cannot tell you it is finished" claim to reliability** — an earlier draft
  said models "cannot know" when they are done, which is stronger than the evidence.
- **Removed a comparison to episode 1's material** that would have re-taught the loop.
  B00 now restates the definition in a single clause.

## Anti-dating audit

Searched the full narration and every prop string for model names, version numbers,
benchmark scores, prices, and vendor names. **Zero hits.** `FileNotFoundError` and
`sales.csv` are the only literal identifiers on screen, both from the shipped file.

## Verdict

> FACT GATE: CLEARED. Rows 3 and 5 are verified by execution; row 4 discloses the only
> on-screen text that is not raw program output; rows 7 and 10 are labelled editorial.
