# FACTCHECK — "Memory and Context"

Every figure on screen is a real measurement printed by `context.py`, which imports Episode
3's `tools.py` unchanged. Nothing here is estimated.

| # | Claim (beat) | Verdict | Basis |
|---|---|---|---|
| 1 | "An agent has no memory — it has a context window" (B00, BVDT) | **ACCURATE** | Definitional, and true of the inference contract regardless of vendor. Product-level "memory" features are layers above the model; the narration says *a model*, not *a chatbot product*. |
| 2 | Every turn re-sends instructions + tools + full history (B02, BVDT) | **ACCURATE** | Structural property of stateless inference, established in Ep 1 and demonstrated by `budget_row()` re-charging `instructions` on every turn. |
| 3 | 903 characters of instructions (B03) | **VERIFIED BY MEASUREMENT** | `len(SYSTEM) + sum(len(json.dumps(to_schema(fn))) for fn in TOOLSET)` using Ep 3's real `read_file` and `count_rows` schemas. |
| 4 | 88 characters per observation; room falling 1009 → 393 over 8 turns (B03) | **VERIFIED** | Printed table, copied verbatim into the beat. |
| 5 | B05 code, ten lines (B05) | **VERIFIED — verbatim** | `inspect.getsource(context.budget_row)`; line count computed, not estimated. |
| 6 | Overflow at turns 13 / 36 / 81 for budgets 2000 / 4000 / 8000 (B07, BVDT) | **VERIFIED** | `first_overflow()` output, copied verbatim. **See correction below — this was briefly wrong.** |
| 7 | "History grows linearly and the budget is constant, so every budget overflows" (B07) | **ACCURATE** | Follows from the model: history is `88 × turns`, budget is fixed, so room goes negative for any finite budget. |
| 8 | Four eviction policies (B06) | **ACCURATE, framed as four named options** | Drop-oldest, summarise, retrieve-on-demand, refuse. Presented as the four choices available, with the caption ruling out a fifth "everything fits" option — which is the honest claim, since the arithmetic forbids it. |
| 9 | The three-question rubric (B08, BVDT) | **EDITORIAL — the episode's recommendation** | The fellow's guidance, demonstrated rather than asserted: B03 and B07 are the rubric applied. |

## Corrections applied during authoring

- **A false "never" was caught before audio, and it would have been the worst error in the
  series.** `first_overflow()` originally capped at 40 turns, so the 8000-character budget
  returned `None`. Left alone, B07 would have shown "first overflow at turn None" while the
  narration claimed overflow is unavoidable — the video would have contradicted its own
  falsifiability beat on screen. The horizon was raised to 500; the real answer is turn 81.
  The beat is only honest because that was found.
- **Characters, not tokens — disclosed in the file itself.** `context.py`'s docstring states
  it plainly, and the narration never says "tokens" or implies a real window is 2000
  characters. The claim is about the *shape* of the curve.
- **The budget is deliberately small, and that is stated in the source**, so the arithmetic
  fits a four-minute video.

## Anti-dating audit

No model, vendor, benchmark, price or context-window size for any real product appears.
On-screen identifiers are `context.py`, `budget_row`, `first_overflow`, and the column names.

## Verdict

> FACT GATE: CLEARED. Rows 3–6 verified by execution; row 9 labelled editorial; the token
> vs character distinction is disclosed in the source and never blurred in the narration.
