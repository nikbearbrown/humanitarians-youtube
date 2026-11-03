# PROMPT — "Claude, Gated." (Week 2)

## The brief

Turn Week 2 of `finance-event-signals` into a ≤3-minute build-log video:
the GIGO gate and the LangGraph agent, with the human ClearGate as the
episode's spine — what got built, what broke, what got fixed, with real
evidence.

## Constraints given

| Constraint | Resolution |
|---|---|
| ≤3:00 target | Measured 1:52 |
| Real content only | Every reject reason, every count, traces to `RUN_LOG.md` or a commit |
| At least one real revision cycle | The LangGraph `{}`-return bug and its fix |
| A falsifiability beat | The ~88% offline-model withhold rate |
| Skin choice | `github` for code/diff/pipeline beats; `claude` bookends only |
| Persona | `claude-liam` (Kokoro `am_onyx`) |

## Structure

```
B00  cold open       two gates named
B01  framework       the chain, gate to gate
B02  ask             reject and say why
B03  code            four real reject paths
B04  output          four malformed cases, four honest rejections
B05  change          LangGraph nodes need a real delta
B06  code (revision) the real fixed line
B07  output (fixed)  97 signals, 12/85 split, 0 crashes
B08  falsifiability  the 88% withhold rate
B09  summary         6→3 gates, still DRAFT
B10  handoff         test your own gate, three ways
B11  outro           title restate
```
