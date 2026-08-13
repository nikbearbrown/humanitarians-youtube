# SOURCES — Episode 2, "The Agent Loop"

## Primary source

**`trace_loop.py`** — authored for this episode, shipped in this folder, runnable with no
dependencies and no API key.

- `record()` is the function reproduced verbatim in beat **B06**, including its inline
  comment (`# the error IS the observation`).
- `record_badly()` is the counter-example the episode argues against. It is real code, not
  a strawman written only for the slide — it returns `"ok"` on both success and failure,
  which is the single most common way an observation gets destroyed in practice.
- Beat **B03** shows real printed output from `python3 trace_loop.py`, captured
  2026-08-13. `read_file` deliberately raises `FileNotFoundError` for `sales.csv` so the
  same call can be recorded two ways in one run and compared side by side.

Captured run, 2026-08-13:

```
WITH A LAZY OBSERVATION
  THOUGHT      I need read_file to make progress on the goal.
  ACTION       read_file({'path': 'sales.csv'})
  OBSERVATION  ok
  NEXT PASS    sees 'ok' and moves on. The file was never read.

WITH AN HONEST OBSERVATION
  THOUGHT      I need read_file to make progress on the goal.
  ACTION       read_file({'path': 'sales.csv'})
  OBSERVATION  read_file({'path': 'sales.csv'}) -> ERROR FileNotFoundError: sales.csv
  NEXT PASS    sees the error, and can try a different path.
```

See `FACTCHECK.md` row 4 for the one on-screen deviation from this output (the
`(lazy)` / `(honest)` labels, and the trimmed duplicate call prefix).

Beat **B07** shows the third block of the same run — `run_lazy()`, the full loop driven
with the lazy recorder, printed verbatim:

```
THE LAZY OBSERVATION, RUN TO THE STEP BUDGET
  pass 1   read_file({'path': 'sales.csv'}) -> ok
  pass 2   read_file({'path': 'sales.csv'}) -> ok
  pass 3   read_file({'path': 'sales.csv'}) -> ok
  pass 4   read_file({'path': 'sales.csv'}) -> ok
  pass 5   read_file({'path': 'sales.csv'}) -> ok
  pass 6   read_file({'path': 'sales.csv'}) -> ok
  pass 7   read_file({'path': 'sales.csv'}) -> ok
  pass 8   read_file({'path': 'sales.csv'}) -> ok
  stopped: step budget exhausted
```

Nothing about that repetition is hard-coded. `think_names()` decides each pass by reading
the observations for tool names it has already tried; a lazy observation carries no tool
name, so the set stays empty and the same call is chosen every time. The episode's central
claim is therefore demonstrated by execution rather than asserted by narration.

## Continuity with Episode 1

`trace_loop.py` **extends** `agent_loop.py` from
`fellows/adwait-changan/2026-08-07-what-makes-ai-agentic/` — same loop, same tool set,
same `max_steps = 8` default (which is where B07's "eight times" comes from). Only the
recording of the observation changes. This is the playlist's continuity rule: one running
artifact, extended weekly, never rewritten from scratch.

## Nothing else is cited, deliberately

No model, vendor, product, benchmark, or price is named. See `FACTCHECK.md` for the
claim-by-claim audit and the anti-dating search.

## Register rewrite (DOUBLE-CHECK LAW)

There is no prose source to parrot. The episode's argument — *the observation is the
load-bearing part, and everyone implements it carelessly* — is the fellow's framing. The
Teardown register earns its place at B07 and B09, where the design is judged: a loop
without honest feedback is named as "one guess, billed repeatedly", and the stopping rules
are assigned to the builder rather than to the model.

## Toolkit provenance

- Built with `brutalist.art` (pared-down, free-only edition), skill `ai-explainer`.
- Voice: Kokoro `am_onyx` ("Onyx"), generated locally. Cost: $0.00.
- Remotion patterns used, all pre-existing in `runtime/remotion/src/Root.tsx`:
  `ClaudeComposerAsk`, `CwcConceptCard`, `ClaudeScienceSourceFlow`, `ClaudeWindow`,
  `ClaudeScienceLayerStack`, `ClaudeCodeBeat`, `MedhavyConceptCard`,
  `ClaudeScienceChipGrid`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`.
  No new scene component was written; no pattern was retinted.
