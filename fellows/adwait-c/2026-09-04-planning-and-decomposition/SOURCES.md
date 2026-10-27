# SOURCES — "Planning and Decomposition"

## Primary source

**`planner.py`** — authored for this video, shipped here, runnable with no dependencies and
no API key.

- `planning_pays()` is shown verbatim in **B05**, extracted with `inspect.getsource()` at
  authoring time so the beat cannot drift from the file.
- **B02**, **B04** and **B06** show its real printed output: the clean-run comparison, the
  failure table, and the four-case rule.

## The model, stated plainly

The file counts **model calls**, a fair proxy for latency and spend, under two assumptions
that are written into the functions themselves:

- **plan-then-execute** — one planning call, then one call per step. On a surprise at step
  *k*, the failed step and everything planned after it are discarded, then re-planned and
  redone.
- **step-by-step** — a decide call and an execute call per step. A surprise discards nothing,
  because nothing beyond the current step was ever decided.

It does **not** measure answer quality, and the video never suggests it does. What it
measures is the shape of the trade.

Captured run:

```
NOTHING GOES WRONG
  plan-then-execute     9 calls
  step-by-step         16 calls
  planning saves        7 calls

SOMETHING GOES WRONG AT STEP k
  k   plan-then-execute   step-by-step  plan discarded
  1                  18             18               8   <- planning's advantage is GONE
  8                  11             18               1
```

## Register

No prose source to parrot. The argument — *a plan is a bet that the world will hold still* —
is the fellow's framing. The Teardown register earns its place at B08, where the common
middle ground is named as the most expensive option of the three rather than the safe one.

## Toolkit provenance

Built with `brutalist.art` (`ai-explainer`), Kokoro `am_onyx`, cost $0.00. Patterns used:
`ClaudeComposerAsk`, `ClaudeScienceLayerStack`, `ClaudeWindow`, `CwcConceptCard`,
`ClaudeCodeBeat`, `ClaudeScienceChipGrid`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`.
No new component; no retint.
