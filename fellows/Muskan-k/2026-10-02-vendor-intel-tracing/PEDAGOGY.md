# PEDAGOGY — One Brief, One Trace. (claude-hai · Vendor Intelligence update, ~2.5min)

**Genre:** project update, single change (Langfuse trace grouping), structured
around one reusable lesson.

**The ONE insight:** **trace the RUN, not the model.** The Langfuse handler was
attached to the model, and `get_llm()` rebuilds the model every call — so one brief
logged ~20 disconnected traces. Attaching the handler once to the graph invocation
gives one nested trace.

**Audience (HAI):** followers of the Fellows' build; anyone wiring up tracing on an
agent/graph who sees scattered traces.

## Act structure
- B00 ASK (composer) — ~20 traces for one brief, tool calls missing ✓
- B01 THE PROBLEM — 20 disconnected, same-named, flat; tool calls untraced ✓
- B02 THE CAUSE (the lesson) — handler on the model + model rebuilt per call →
  N traces; attach to the run instead ✓
- B03 THE FIX — get_llm() drops the callback; new trace_config() (handler +
  brief:{company} + metadata); supervisor.py:503 → graph.invoke() ✓
- B04 THE RESULT — one trace, 92 nested observations, tool calls traced ✓
- B05 verdict · B06 handoff (check your own dashboard) · B07 outro ✓
- Body B01–B04 = 4K PIL cards; Claude UI only at B00/B05/B06/B07 (ILLUSTRATE LAW).

## Correctness (DOUBLE-CHECK LAW — verbatim from the change log)
- ~20 disconnected traces, all named "ChatBedrockConverse".
- Cause: callback attached to the model; `get_llm()` builds a fresh model per call.
- `get_llm()` no longer attaches a callback.
- New `trace_config()` builds the run config with the handler, a `brief:{company}`
  name, and metadata.
- `supervisor.py:503` passes it to `graph.invoke()`.
- Result: one trace with 92 nested observations instead of 20 flat rows; tool calls
  now traced (never before). No invented figures.

## PROOF self-check
Has a reusable lesson shown before the fix (B02), a real before/after artifact (B04),
and a scaffolded task (B06) — should score better than a pure changelog, though it is
still an update. Production gate: every figure (20, "ChatBedrockConverse", 92) is a
legible on-screen artifact from the creator's own run.

## Narration review (GATE P)
Listen for: does B02 land "trace the run, not the model" as the lesson? Is B04
clearly the SAME brief, now one legible tree? Are the code names (get_llm,
trace_config, graph.invoke) spoken clearly?

VERDICT: PASS 