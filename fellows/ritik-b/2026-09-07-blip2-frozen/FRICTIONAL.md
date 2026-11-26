# Frictional log — Week of 2026-09-07

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-09-07 — reconstructed 2026-11-25

### BLIP-2, How Much Can You Freeze?

**What I was working on.** An explainer on BLIP-2 — a frozen image encoder and a frozen language model joined by
a small trained Q-Former — as two 4K masters, 16:9 and 9:16, from one beat list. It follows last week's BLIP reel.

**What I tried and expected.** I expected to need new scene components again, as VQA (7) and BLIP (5) did. Instead I
tried building it entirely from existing toolkit patterns that already have 9:16 twins — including two that BLIP
had promoted to shared scenes — and expected the story to be "freezing is efficient".

**Where the work resisted, and what I did next.** The paper's tables changed the story. The headline (65.0 zero-shot
VQAv2 against Flamingo80B's 56.3) only holds with FlanT5 as the frozen LLM; with OPT the same bridge scores 52.3 and
52.6, below Flamingo, so the receipt beat shows every configuration, not the best one. Table 1 gives 188M trainable
parameters and Table 2 gives 103M–108M; I used 188M only where the paper does (the 54x claim). The first narration
estimate ran 2:09, over the two-minute cap, and was cut to 1:57.6. The narration gate (GATE P) wants a signed
pedagogy review before audio; I review and sign off every master myself before upload, so audio came first
and the sign-off was given on the finished videos. The first frame check failed both cuts: the three list beats were built on ClaudeWindow, which filled only 17–19% of the 16:9 frame and 39–46% of the 9:16 one, against a 55% minimum. I re-cut them onto ReelFramework (same narration, same facts) and re-rendered just those beats; the 16:9 cut is now clean, and the 9:16 end card sits at 53% fill. The first 9:16 master also came out silent — the step that shares narration between the two cuts dropped each beat's audio path — so I fixed that step, recompiled, and now check every master's loudness before it counts as done.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
drafted the beat list and narration, checked every number against the arXiv text, checked pronunciation with Kokoro's
phonemizer, and ran the render and the gates. I chose the topics — BLIP-2 plus a progress update, over a second
explainer — and accepted the table-first receipt beat.

**What I understand now, and what I still don't.** A headline number is a claim about one row; the audit question
"does the win survive a different LLM?" is now part of the freeze audit.

### Week 2 Progress: BLIP-2

**What I was working on.** The week's progress update, as a second video: what shipped, how the week went, what it
taught, and what is still open, in both orientations.

**What I tried and expected.** I expected a progress update to be quick, and it was — same patterns, same pipeline as
the explainer, rendered after it so every figure on screen comes from the finished build.

**Where the work resisted, and what I did next.** The quality-check line couldn't be written until the explainer's
frame check had run, so this reel was authored last. Its 9:16 end card first filled only 41% of the frame — "Week 2 Progress: BLIP-2" is too short for a portrait poster — so the closing card now reads "Week 2 Progress: BLIP-2, Built From Parts", and both cuts are frame-check clean.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude drafted the update
from the build log and the earlier reels' BUILD-LOGs and rendered it. I accepted it.

**What I understand now, and what I still don't.** Writing scenes once for both canvases is what made a zero-new-code
week possible. Still open: 9:16 twins for `ClaudeScienceLayerStack` and `ClaudeCodeBeat`.
