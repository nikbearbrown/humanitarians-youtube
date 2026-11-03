# SOURCES — "Memory and Context"

## Primary source

**`context.py`** — authored for this episode, runnable, no dependencies and no API key.

- `budget_row()` is shown verbatim in **B05**, extracted with `inspect.getsource()` at
  authoring time so the beat cannot drift from the file.
- **B03** shows the real turn-by-turn budget table; **B07** shows the real `first_overflow()`
  comparison. Both copied from the program's own output.
- **It imports the earlier episode’s `tools.py` unchanged** and calls `to_schema()` on the same
  `read_file` and `count_rows`. The 903-character instruction cost is therefore a real
  measurement of the previous episode's artifact, not a made-up number.

Captured run, 2026-08-13:

```
THE BUDGET, TURN BY TURN   (budget = 2000 chars)
turn  instructions  history  room to answer
   1           903       88            1009
   8           903      704             393

DOES A BIGGER WINDOW FIX IT?
  budget  2000 chars  ->  first overflow at turn 13
  budget  4000 chars  ->  first overflow at turn 36
  budget  8000 chars  ->  first overflow at turn 81
```

## Honesty note carried in the source itself

`context.py`'s docstring states that it measures **characters, not tokens**, and that
`BUDGET = 2000` is deliberately small so the arithmetic is visible in four minutes. Real
context windows are far larger. The episode's claim is about the shape of the curve — fixed
cost re-paid every turn, linear history growth, inevitable overflow — not about any specific
window size.

## Continuity

`agent_loop.py` (Ep 1) → `trace_loop.py` (Ep 2) → `tools.py` (Ep 3) → `context.py` (Ep 4),
which imports Ep 3 directly. Four episodes, one artifact, extended not rewritten.

## Toolkit provenance

Built with `brutalist.art` (`ai-explainer`), Kokoro `am_onyx`, cost $0.00. Patterns used:
`ClaudeComposerAsk`, `ClaudeScienceLayerStack`, `ClaudeScienceSourceFlow`, `ClaudeWindow`,
`CwcConceptCard`, `ClaudeCodeBeat`, `ClaudeScienceChipGrid`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`. No new component; no retint.
