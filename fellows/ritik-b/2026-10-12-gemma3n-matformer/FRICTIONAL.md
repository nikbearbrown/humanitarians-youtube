# Frictional log — Week of 2026-10-12

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-10-12 — reconstructed 2026-11-25

### Gemma 3n, Four Billion or Eight?

**What I was working on.** A one-minute re-cut of the Gemma 3n E4B teardown — MatFormer nesting and per-layer
embeddings, and what "effective 4B" means — as two 4K masters, 16:9 and 9:16, from one beat list.

**What I tried and expected.** The drafted teardown ran 9 beats, about 1:53 by estimate, with a
`ClaudeScienceLayerStack` beat and two `ClaudeCodeBeat` beats that have no 9:16 twin. I rebuilt the nesting and the
per-layer embeddings as `ReelFramework` rows and the parameter arithmetic as a `BlipLadder` chart, and expected to
keep the draft's numbers as they were.

**Where the work resisted, and what I did next.** The draft said "about 8B" and that the per-layer table was "almost a
third" of it. Reading the safetensors index gave the real totals — 8,387,373,392 for E4B and 5,976,833,472 for E2B —
so the table (262,144 × 35 × 256 = 2,348,810,240) is 28%, and the re-cut shows the bars instead of a fraction. The
docs' only "effective" figure is for E2B (1.91B effective of over 5B loaded, Fig. 1); there is none for E4B, so the
chart labels which model each bar belongs to and marks the "4" in E4B as a dashed line rather than inventing an E4B
number. The end-card title was set to 44 characters before rendering so the portrait card fills the frame; both cuts
passed the frame check on the first pass. Measured narration: 1:12.3 over 8 beats. The narration gate (GATE P) wants
a signed review before audio; I review and sign off every master myself before upload, so audio came first and the
sign-off was given on the finished videos.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
re-cut the beat list and narration, read both configs, both weight indexes and the Gemma 3n docs to check every
number, checked pronunciation of "E4B", "E2B" and "MatFormer" with Kokoro's phonemizer, and ran the render and the
gates. I chose the topic and accepted the re-cut, including dropping "almost a third".

**What I understand now, and what I still don't.** "Effective" is a memory budget for one model under one setup
(PLE caching plus skipping the vision and audio weights), not a smaller model. I don't know E4B's effective footprint
— Google doesn't publish it in the docs — which is what the hand-off's laptop measurement would show.

### Week 7 Progress: Gemma 3n

**What I was working on.** The week's progress update, as a second video: what shipped, how the week went, what it
taught, and what is still open. Progress updates are 16:9 only.

**What I tried and expected.** Same patterns and pipeline as the explainer, authored after the explainer's frame check
so every figure on screen comes from the finished build.

**Where the work resisted, and what I did next.** Little did: the explainer passed the frame check in both
orientations on the first pass, so the quality line could be written straight away. The lesson beat took the most
care — it had to say that Google's 1.91B "effective" figure belongs to E2B without implying an E4B number the docs
don't give. Measured narration: 1:00.7 over 7 beats; frame check clean.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude drafted the update
from this week's build and rendered it. I accepted it.

**What I understand now, and what I still don't.** Reading the weight index, not just the config, is what turned
"about 8B" into 8.39B. Still open: 9:16 twins for `ClaudeScienceLayerStack` and `ClaudeCodeBeat`.
