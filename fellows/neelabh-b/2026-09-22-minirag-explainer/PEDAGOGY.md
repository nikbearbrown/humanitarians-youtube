# PEDAGOGY — claude-liam-minirag

Narration sign-off. What the reel teaches, in what order, and why each beat sits
where it does.

## The one idea

**MiniRAG's contribution is not a better model — it is a better place to put the
work.** Retrieval-augmented generation had quietly assumed a large language model
at every stage. MiniRAG moves the reasoning into a graph index, so a phone-sized
model only has to do the two things small models are actually good at: extract
entities, and write the final sentence.

The ablation is what makes this a claim rather than an assertion. Pull the index
out and accuracy halves. That is the beat the whole film is built to earn.

## The arc

| Beats | Move | Why here |
|---|---|---|
| B00–B01 | The question, then the gist | EXECUTIVE-SUMMARY LAW: the viewer holds the whole shape before any detail. The hesitant writer types the misconception the body then dismantles — *bigger model* corrected to *better index* |
| B02 | The framework | Must precede every example. Three stages, one hidden dependency |
| B03 | The break | The framework fails in front of you. Numbers on screen, voice reacting |
| B04 | The paper's own questions | Turns a critique into a research programme |
| B05–B06 | Ask → result | The prompt, then the artifact it produced. The one place the interface earns a beat mid-film |
| B07 | The mechanism | Now that you know *where* the work moved, *how* it moved |
| B08 | Worked example | One real query, both systems, side by side. The mechanism performs itself |
| B09 | The results | Four models, same direction |
| B10 | The evidence for the claim | Take the index out and watch it collapse. This is the load-bearing beat |
| B11 | Where it bites | The honest cost. Required, and the reason this is a research explainer |
| B12 | Why it matters | On-device, private, a quarter of the storage |
| B13–B15 | Verdict, your turn, title | The standard close |

## Register decisions

**Teardown, not press release.** The narration explains the mechanism and then
judges it. Three places where that shows:

- B02 ends on *"That is the design assumption. Nobody ever wrote it down."* — the
  Teardown move of naming what a design takes for granted.
- B10 ends on *"That is the claim, tested."* — crediting the authors for
  falsifying their own architecture rather than only benchmarking it.
- B11 opens with *"Now the part the paper does not dwell on."* — the judgment the
  register exists for. It is stated as an observation about emphasis, not as an
  accusation, because the numbers are the authors' own.

**Plain language over jargon.** "Heterogeneous graph indexing" is spoken once, in
B06, after the viewer has already seen the thing it names. B07 explains it as
"two kinds of node, two kinds of edge" before ever using the term again.

**Numbers are spoken as words, evidence lives on screen.** Body beats run 45–70
words. Every figure the voice says has a bar, counter, or card carrying it at the
same moment. Nothing is recited that the viewer cannot see.

## What was deliberately left out

- **The equation.** §2.2.2's relevance-scoring function `ω_e(e)` is real and
  central, but explaining it needs the five-zone equation tangent — a 45-second
  detour that would double the film's technical load for a mechanism the graph
  animation already conveys. Also: LaTeX is not installed on this machine, so
  a typeset equation beat could not render. Noted rather than hidden.
- **The LiHuaWorld dataset construction.** A genuinely interesting contribution
  (a year of simulated personal chat, built because existing RAG benchmarks use
  Wikipedia). It is its own video. Mentioned nowhere rather than half-explained.
- **GraphRAG's Leiden clustering, LightRAG's dual-level retrieval.** Baseline
  internals. The reel needs only that they assume a large model.

## The handoff

HANDOFF LAW requires the prompt be read aloud and discussed, and the
teaching-arc checklist requires it be *scaffolded* — a rubric, not "ask Claude
about X". B14 gives a three-part experiment design **and** three things to check
in the answer, ending on the one that matters: *does it say what result would
prove the claim wrong.* That is the same standard the reel just applied to the
paper.

## Sign-off

Narration checked against `FACTCHECK.md` (25 claims, all traced to the source).
Three of the paper's own framings were dropped as unsupported by its own tables;
one finding the paper underplays was promoted to a full beat. Recorded in
`SOURCES.md`.

**Status: ready for human review. Not published, not uploaded.**
