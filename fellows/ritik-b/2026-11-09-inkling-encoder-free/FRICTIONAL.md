# Frictional log — Week of 2026-11-09

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-11-09 — reconstructed 2026-11-25

### Inkling, Encoder-Free at Scale?

**What I was working on.** A two-minute teardown of Thinking Machines' Inkling as two 4K masters with the same
content — 16:9 and 9:16 — built so the viewer leaves with a method, not a list of facts.

**What I tried and expected.** The researched draft (12 beats, about 2:46) was written for eight new `Inkling*` scenes.
I expected to build those scenes; instead I re-cut the draft onto the six patterns that already have 9:16 twins, so this
week and the next two could render in parallel without touching the shared toolkit, and put the effort into the teaching
structure: a four-step audit shown first, then each step run on Inkling.

**Where the work resisted, and what I did next.** Re-checking the draft against the sources found two problems. The
announcement says a small number of contaminated Terminal Bench 2.1 solutions were scored 0 — not that a benchmark was
zeroed out, as the draft had it. And the draft's "first two layers are dense" rested on a config field whose meaning
isn't documented; the weight map confirmed it (layers 0–1 carry dense feed-forward weights, layers 2 onward carry
experts). The same weight map gave a number I didn't expect: `total_size` is 1,904,604,285,204 bytes, which at two bytes
per parameter is about 952B, not the stated 975B — so the claim check gained an "ambiguous" row. Then the PROOF
self-review of the beat sheet scored 10/12 with the production gate failing: the worked example's arithmetic was spoken
at the start of its beat but sat in a caption that only appears at 80%, three claims were voiced and never shown, and
step 4 named no test. Six edits to the sheet took it to 12/12 with the gate passing, before any audio. The narration
first measured 2:12.9, so four beats were trimmed to 2:07.5. After the render, GATE V was clean in both cuts, but my own frame review (PROOF-2) found two framework labels — CONVOLUTION and CONTAMINATION — running into their detail text in 16:9. I shortened them to CONV and LEAKAGE and re-rendered those two beats in both cuts, so the two sheets stay identical; the automated gate doesn't measure that kind of overlap.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
re-verified every number against `config.json`, the weight map, the model card and the announcement, re-cut and
narrated the beat list, ran the PROOF self-review against the patterns' reveal timings, and rendered and checked both
cuts. I chose the topic, set the two-minute length and the PROOF standard, and accepted keeping the parameter count as
"ambiguous" rather than calling it wrong.

**What I understand now, and what I still don't.** Sparse compute is not sparse memory: Inkling's attention design cuts
the million-token cache six-fold, but every expert still has to be resident, and the weights are 1.9 TB. Grading the
sheet against the reveal timings catches legibility problems while they are still cheap edits. I still don't know why
the checkpoint implies about 952B against the stated 975B — mixed precision or a counting convention would explain it,
and neither the config nor the card says which.

### Week 11 Progress: Inkling

**What I was working on.** The week's progress update, as a second video: what shipped, what the pre-render
review caught, what the sources corrected, and what is still open — in 16:9 only; the explainer carries the 9:16 cut.

**What I tried and expected.** The same patterns and pipeline as the explainer, authored only after the explainer's
frame check had run, so every figure on screen — the PROOF scores, the runtime, the gate results — comes from the
finished build.

**Where the work resisted, and what I did next.** The first narration measured 1:44, under the 1:50 floor, so four beats each gained one sentence, each voiced over a caption already on screen; it measured 1:52. The pre-render check also caught the narration counting five moves over four rows, and the explainer's frame-check result (two overlapping labels) had to be written into three beats before audio.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
drafted the update from the explainer's build results and its PROOF-REVIEW.md, ran a short PROOF check on it (production
gate and show-over-say), and rendered it. I accepted it.

**What I understand now, and what I still don't.** Showing the review itself — what it caught and the score before and
after — is a more honest progress update than a list of what shipped. Still open: the 975B vs ≈952B gap.
