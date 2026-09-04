# PEDAGOGY — "Claude, Cached."

Narration sign-off record. Audience: a smart non-technical-to-intermediate
viewer who has used an LLM chat interface and noticed the pause-then-stream
pattern but never had it explained mechanically.

## The one thing this video has to land

**The pause and the streaming are two different computational regimes, not
one thing slowing down and speeding up.** Prefill is a big parallel matmul
over the whole prompt (compute-bound); decode is one cheap step per token
that just reads a growing cache (memory-bound). Once the viewer has that
split, "why is a long conversation slow" answers itself.

## Act structure

| | |
|---|---|
| B00 cold open | ✓ The felt experience (pause, then fast) named before any mechanism |
| B01 executive summary | ✓ One breath: cache K/V, don't recompute — before any jargon |
| B02 framework | ✓ Every token makes a K/V; causal masking means the past is fixed — stated before the worked example |
| B03-B04 worked example | ✓ Prefill and decode shown as two distinct beats, mechanically, not narrated as one blur |
| B05 falsifiability | ✓ Real limit: unbounded cache growth — the actual cost of the mechanism, not a caveat |
| B06 verdict | ✓ Names the trade-off explicitly: compute for memory |
| B07 handoff | ✓ A measurable task (time prefill vs. decode yourself), not "go read about it" |
| B08 outro | ✓ Title restate + sign-off |

## Why Manim, not screen recordings

Attention internals aren't visible in any UI — there's nothing to screen-
record. Every mechanism beat (B02-B05) is a purpose-built diagram
(token squares, K/V blocks, a growth curve) that performs the mechanism
directly, per the toolkit's REBUILD LAW and SHOW-DON'T-TELL LAW.
