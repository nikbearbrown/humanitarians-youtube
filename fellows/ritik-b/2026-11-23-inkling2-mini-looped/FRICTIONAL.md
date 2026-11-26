# Frictional log — Week of 2026-11-23

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-11-23 — reconstructed 2026-11-25

### Inkling 2 Mini, Looped Is Better?

**What I was working on.** A two-minute audit of Thinking Machines' Inkling 2 Mini — a looped mixture-of-experts model
that stores 24 layers but runs 48 per token — as two 4K masters with the same content, 16:9 and 9:16, built around three
checks a viewer can reuse on any open model: read the config, compute the cost, check each claim against its evidence.

**What I tried and expected.** The researched draft (12 beats) was written for `Inkling*` scenes that were never built.
I re-cut it onto six patterns that already have 9:16 twins, to eleven beats, and expected the facts to carry over.

**Where the work resisted, and what I did next.** Re-checking the draft against the sources, one claim had to go: the
lab's text says the model trails Qwen3.8-27B on ComplexConstraints, but its own table shows 33.4% against 30.1%. The
one-pass 3.4B figure can't be rebuilt from the config, so it is labelled lab-reported; the +1.0B per extra pass is
computed. The PROOF self-review of the first cut scored 10/12 with the production gate failing — mostly numbers spoken
before they were on screen — and fourteen edits took it to 11/12 with the gate passing, before any audio. Friction
stayed at 1 of 2: the tensions are shown side by side but resolved for the viewer. After the render, GATE V was clean
in both cuts, but my frame review found one row reading "Zero-indexed: layers 7–18" — that range counts from one — so I
reworded it and re-rendered that beat in both cuts.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
re-checked every number against `config.json`, the two model cards and the lab post, re-cut and narrated the beat list,
ran the PROOF self-review against the patterns' reveal timings, and rendered and checked both cuts. I chose the topic,
set the length and the PROOF standard, and accepted shipping at 11/12 with friction noted for the series.

**What I understand now, and what I still don't.** Looping saves memory, not compute: all 26.4B parameters (about
20 GB) stay resident, and each token pays for about 5.4B. On the lab's variable-loop model, three passes instead of one
add 42 points on a long-context graph test but about one on closed-book trivia — looping adds reasoning, not knowledge.
I still don't know whether "over 50% more compute-efficient" holds: the evidence is one sentence, a scaling-law
prediction, and the 28 evaluations behind "27 of 28" are not listed.

### Week 13 Progress: Inkling 2 Mini

**What I was working on.** The week's progress update, as a second video, in 16:9 only and about a minute long: what
shipped, how it was checked, and what is still open.

**What I tried and expected.** The same patterns and pipeline as the explainer, authored after the explainer's GATE V had
run, so the PROOF scores, the runtime and the gate results on screen come from the finished build.

**Where the work resisted, and what I did next.** Partway through I set a shorter bar — a progress update only needs
about a minute — so I cut it to seven beats. The short pre-render check made two edits so the PROOF score and the
first-pass result are on screen as they are said.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
drafted the update from the explainer's build results and its PROOF-REVIEW.md, ran a short PROOF check on it and
rendered it. I accepted it.

**What I understand now, and what I still don't.** Reveal timing is part of the argument: evidence has to land before
the voice does. Still open: how to leave a tension open for the viewer within two minutes.
