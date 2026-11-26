# Frictional log — Week of 2026-11-02

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-11-02 — reconstructed 2026-11-25

### Ouro, Smarter by Repeating?

**What I was working on.** A teardown of ByteDance's Ouro looped language models — one layer stack run up to
four times — as two 4K masters, 16:9 and 9:16, from one beat list.

**What I tried and expected.** I wanted the paper body for the exit-gate details; the arXiv HTML version still
returns 404, so the claims stay limited to the abstract, the model card and `config.json`. I also expected the
vertical cut to wait on new scenes: the first draft (9 beats, about 1:42) used `ClaudeScienceLayerStack` and
`ClaudeCodeBeat`, which have no 9:16 twin.

**Where the work resisted, and what I did next.** The sources disagree in two places. The model card's table says the
2.6B model has 24 layers, while `config.json` says 48; the checkpoint's parameter count (2,667,974,657) only works out
with 48, so the reel uses 48. And the card says the 2.6B model matches 3–4B transformers, where the abstract says "up
to 12B" — the fairness beat now shows both. The "roughly 10B of compute" line was checked the same way: 4 × 2.47B
looped layers plus 0.20B of embeddings and head comes to about 10.1B per token. The draft's layer stack and code
sketches were rebuilt as `ReelFramework` rows and a three-bar `BlipLadder` (stored, computed, largest match); nine beats
became eight, and the narration came in at 1:07.9. Both masters passed the clip check and the frame check clean on the first render: the outro title was set to more than 40 characters, the count's axis label kept short, and the 9:16 sheet's narration files checked before rendering — what the previous week's 9:16 checks had caught. Both masters measure −23.6 dB.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
re-cut the beat list and narration onto responsive patterns, found the 24-vs-48 layer discrepancy and resolved it from
the checkpoint's parameter count, checked pronunciation with Kokoro's phonemizer (the narration spells the name "Ooro"
so it is said "OO-roh"), and ran the render and the gates. I chose the topic and accepted putting the model card's
3–4B claim beside the abstract's 12B.

**What I understand now, and what I still don't.** A looped model is small to store and not small to run — compare it
per unit of compute, not per parameter. I still don't know how the exit gate behaves at inference with the default
`early_exit_threshold` of 1.0, which the card says means always using all steps; that stays out of the narration.

### Week 10 Progress: Ouro

**What I was working on.** The week's progress update, as a second video: what shipped, how the week went, what
the paper taught, and what is still open — in 16:9 only; the explainer carries the 9:16 cut.

**What I tried and expected.** I expected it to be quick, and it was — the same six patterns and the same pipeline as
the explainer, authored only after the explainer's frame check had run, so every figure on screen comes from the
finished build.

**Where the work resisted, and what I did next.** Its quality-check line waited on the explainer's frame check, so it was authored last. It ships in 16:9 only — progress updates are landscape-only; the explainer carries the 9:16 cut.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
drafted the update from the explainer's build results (measured narration, clip check, frame check) and rendered it.
I accepted it.

**What I understand now, and what I still don't.** Re-cutting onto patterns that already have 9:16 twins is what made
a zero-new-code vertical cut possible this week. Still open: 9:16 twins for `ClaudeScienceLayerStack` and
`ClaudeCodeBeat`, which a beat with a genuinely layered or code-shaped picture will eventually need.
