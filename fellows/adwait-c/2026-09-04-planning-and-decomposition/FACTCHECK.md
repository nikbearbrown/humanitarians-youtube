# FACTCHECK — "Planning and Decomposition"

Every figure on screen is printed by `planner.py`. The file is a **cost model with stated
assumptions**, not a benchmark, and it says so in its own docstring.

| # | Claim (beat) | Verdict | Basis |
|---|---|---|---|
| 1 | "There are only two ways: plan then execute, or step by step; everything else blends them." (B01) | **ACCURATE as framing** | Definitional. Presented as the two poles of a spectrum, with the narration explicitly saying everything else is a blend, so it does not overclaim a strict dichotomy. |
| 2 | 9 calls vs 16 calls on an 8 step task; planning saves 7 (B00, B02, BVDT) | **VERIFIED BY EXECUTION** | `plan_then_execute()` → 1 + 8 = 9. `step_by_step()` → 2 × 8 = 16. Printed and copied verbatim. |
| 3 | The per-strategy call formulas | **MODEL, stated in code** | Plan-then-execute charges one planning call plus one per step; step-by-step charges a decide and an execute per step. Both assumptions are written in the functions' docstrings, on screen in B05's neighbouring code and in SOURCES.md. |
| 4 | Failure table, k = 1…8 (B04) | **VERIFIED BY EXECUTION** | Copied verbatim from the printed table. On failure, plan-then-execute discards the failed step and everything planned after it, re-plans, and redoes them. |
| 5 | "Fail at step one and it is 18 against 18, the entire advantage is gone." (B04, BVDT) | **VERIFIED — and corrected before audio** | Both strategies reach exactly 18. **The program originally labelled this "planning now costs MORE", which was false: it is a tie.** See corrections. |
| 6 | B05 code, nine lines (B05) | **VERIFIED — verbatim** | `inspect.getsource(planner.planning_pays)`, unmodified. Line count computed, not estimated. |
| 7 | Four-case table: one PLAN, three "do not plan" (B06) | **VERIFIED BY EXECUTION** | Printed verbatim. The four cases shown are all-true plus each single condition flipped; the narration says "change any single one", which is exactly what is on screen. |
| 8 | The three conditions themselves (B05, B07, BVDT) | **EDITORIAL — the fellow's rubric** | Not a cited standard. Framed as a test the viewer can run, and *demonstrated* rather than asserted: B04 shows what happens when stability fails, and B06 shows the rule flipping. |
| 9 | "The costliest pattern is a plan written, displayed, then ignored." (B08, B09, BVDT) | **EDITORIAL, arithmetically supported** | The cost claim follows from the model: you pay the planning call *and* the step-by-step call count. The "nobody can audit it" point is judgement, phrased as judgement. |
| 10 | "Most agent frameworks plan by default." (B00) | **SOFTENED — deliberately unquantified** | Stated as a general observation, with no framework named, no proportion claimed, and no citation implied. An earlier draft said "almost every framework", which asserted more than could be shown. |

## Corrections applied during authoring

- **The tie was mislabelled, and it was caught before audio.** `planner.py` printed
  "planning now costs MORE" whenever plan-then-execute did not strictly win, so the k=1 row
  claimed planning was *worse* when both strategies cost exactly 18. That is an overstatement
  on screen, in the one beat whose entire purpose is to test the video's own premise. The
  comparison now distinguishes three outcomes — wins, *advantage is GONE*, costs more — and
  the narration matches: "eighteen calls against eighteen. The entire advantage is gone."
- **"Almost every framework" → "Most agent frameworks"**, and no framework is named.
- **The cost model is labelled as a model** in the file docstring, and the narration never
  calls these measurements of quality or speed — only of calls.

## Anti-dating audit

No model, vendor, framework, benchmark or price appears. The only identifiers on screen are
`planner.py`, `planning_pays`, and the three condition names.

## Verdict

> FACT GATE: CLEARED. Rows 2, 4, 5, 6 and 7 verified by execution; row 3 discloses the model's
> assumptions; rows 8, 9 and 10 are labelled editorial or deliberately unquantified.

## Corrections applied 2026-10-26

- **An em dash survived in the narration of BOUT.** House style forbids it: it reads as a pause the voice does not take. Rewritten by hand into a full stop or a colon rather than swapped for a comma, since the sentence wanted the stronger break. The affected beat's audio was regenerated and the reel recompiled in both aspect ratios, because new words mean a new duration and the measured duration is what every other beat is cut against. Found by scanning all 489 narration lines in the batch for em dashes, spoken week or episode numbers, and back-references, rather than by re-reading the four sheets I happened to have open.
