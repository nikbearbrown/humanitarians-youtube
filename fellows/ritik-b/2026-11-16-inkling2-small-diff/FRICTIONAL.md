# Frictional log — Week of 2026-11-16

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-11-16 — reconstructed 2026-11-25

### Inkling 2 Small, What Changed?

**What I was working on.** A two-minute audit of what changed from Inkling to Inkling 2 Small, as two 4K masters with
the same content — 16:9 and 9:16 — built so the viewer leaves with a three-step method they can rerun on any two
generations of an open model: diff the configs, recompute the headline, match each change to a stated reason.

**What I tried and expected.** The researched draft (12 beats, about 2:48) was written for `Inkling*` scenes that were
never built. I re-cut it onto six patterns that already have 9:16 twins, to ten beats, and expected the content to carry
over unchanged.

**Where the work resisted, and what I did next.** The PROOF self-review of the first cut scored 9/12 with the production
gate failing. The summary pattern renders only three roadmap cards, so the fourth step of a four-step rubric was spoken
and never shown — the rubric became three steps. Two numbers (31.9M per expert, ≥ 500 GB to serve) sat in text that
fades in late, so they moved into bar subtitles and the heading. A computed 292M encoder became the honest range
291.7–292.9M, and the link from the attention-residual config key to a published paper is my inference, so the video
calls it the nearest paper and scores it BORROWED, not CHECKED. Nine edits took it to 12/12 with the gate passing, before
any audio. Re-checking the draft against the sources, I dropped four items the audit didn't need or I couldn't confirm in
those words: a KV-cache ladder, a third-party benchmark score, the alignment caveats and a training-data line.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
re-fetched both `config.json` files, both release posts, the model cards and the paper, re-cut and narrated the beat list,
ran the PROOF self-review against the patterns' reveal timings, and rendered and checked both cuts. I chose the topic, set
the length and the PROOF standard, and accepted the three-step rubric and the BORROWED label.

**What I understand now, and what I still don't.** Both headline numbers — 17B active and 594B total — reproduce from
the config, but only with untied embeddings; tied embeddings would give 16.3B and 593.1B. "Small" is small per token
(−59% compute) more than in memory (−39% stored, still ≥ 500 GB to serve). I still don't know why the lab dropped the
encoder-free input, or audio, or what it expects attention residuals to buy: the November post has no architecture
section, and July's did.

### Week 12 Progress: Inkling 2 Small

**What I was working on.** The week's progress update, as a second video, in 16:9 only: what shipped, how it was
checked before and after rendering, what the check caught, and what is still open.

**What I tried and expected.** The same patterns and pipeline as the explainer, authored after the explainer's GATE V had
run, so every figure on screen — the PROOF scores, the runtime, the gate results — comes from the finished build.

**Where the work resisted, and what I did next.** The first draft said three numbers were voiced before they were
readable; the explainer's review lists two, plus one rubric step that never reached the screen, so I corrected it. One
framework label (ATTRIBUTION) was too wide for its column in 16:9 and would have run into its text, so it became CREDIT
before rendering.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
drafted the update from the explainer's build results and its PROOF-REVIEW.md, ran a short PROOF check on it (production
gate and show-over-say) and rendered it. I accepted it.

**What I understand now, and what I still don't.** Scoring a cut against its own standard before the render is cheaper
than finding the same problems in frames. Still open: the lab's reasons for the changes.
