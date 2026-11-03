# PROMPTS — claude-liam-minirag

Every prompt that appears **on screen** in this reel, verbatim, plus the
generation prompts behind the reel-local components. ASK → RESULT LAW: a Claude
composer beat is never decoration; it is always followed by what it produced.

## On-screen prompt 1 — B00, the cold open

Shown in `ClaudeComposerAsk.command`. Answered in the same beat by three output
lines, per COLD OPEN LAW.

> Read the MiniRAG paper (arXiv:2501.06713). Does retrieval-augmented generation
> actually need a large language model — and what exactly breaks when you swap in
> a small one?

**Output lines shown:**
- existing RAG collapses on small models — GraphRAG stops entirely
- MiniRAG moves the reasoning out of the model, into the index
- 53.29% vs 39.81% — Phi-3.5-mini on LiHuaWorld

## On-screen prompt 2 — B05, the ask of the ask→result pair

Shown in `ClaudeComposerAsk.command`. **Result = B06**, the rebuilt Figure 1.
This is the receipt: the prompt that made the next shot.

> Rebuild Figure 1 of the MiniRAG paper as an animated Remotion diagram:
> heterogeneous graph indexing on the left, the two-step lightweight retrieval in
> the middle, integration and generation on the right. Cream stage, warm ink,
> exactly one terracotta accent.

## On-screen prompt 3 — B14, the handoff

Shown in `ClaudeComposerAsk.command` and **read aloud verbatim**, then discussed,
per HANDOFF LAW.

> I want to test whether MiniRAG's core claim holds on my own data. Help me
> design a small experiment: (1) pick a document set I already have; (2) define
> ten questions where the answer needs two hops; (3) tell me what accuracy and
> what error rate would make me believe the index is doing the work, not the
> model.

**The rubric spoken after it** (the scaffolding the teaching-arc checklist
requires — "paste this prompt, then check whether the output does A, B and C"):

1. Does the answer separate **accuracy** from **error rate**?
2. Does it name a **baseline** to compare against?
3. Does it say what result would prove the claim **wrong**?

> If it skips that third one, push back.

## Generation prompts — the five reel-local components

Not shown on screen (only B05's is). Recorded so the build is reproducible.

**`MiniRagStackToday`**
> Three labelled stages left-to-right on a cream stage — INDEX, RETRIEVE,
> GENERATE — each with a one-line subtitle, connectors drawing between them. Then
> a terracotta band sweeps in beneath all three and lights them simultaneously,
> labelled LARGE LANGUAGE MODEL. The band is the point: one dependency under
> every stage.

**`MiniRagPipeline`**
> Rebuild MiniRAG's Figure 1 as three panels. Left: raw text collapsing into a
> small heterogeneous graph. Middle: two labelled steps, with a terracotta pulse
> travelling a discovered path on step two. Right: retrieved evidence entering a
> small model, an answer emerging. Simplified-redraw credit bottom-right.

**`MiniRagHeteroGraph`**
> Build a heterogeneous graph on cue: soft rectangles for text chunks, small
> circles for entities popping out of them, then entity↔entity edges in ink and
> entity↔chunk edges in terracotta. One edge expands to reveal its written
> description.

**`MiniRagWorkedQuery`**
> A single query full-width at top. Two columns beneath — one system per column,
> each showing its retrieval steps then its final answer. The failing answer is
> struck through; the correct one resolves in terracotta and matches a ground
> truth revealed at the top.

**`MiniRagAblationDrop`**
> A complete graph with a large counter beside it. Per step, strip one structural
> layer away and tick the counter down to the new value. On the final step the
> structure collapses to a flat list and the counter plunges. Bracket the gap
> between first and last values.

## Not used

No Higgsfield, no image generation, no paid API. Kokoro `am_onyx` is the only
generative call in this build and it runs locally. **Cost: $0.00.**
