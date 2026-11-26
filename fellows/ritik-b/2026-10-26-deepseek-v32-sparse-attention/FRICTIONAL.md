# Frictional log — Week of 2026-10-26

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-10-26 — reconstructed 2026-11-25

### DeepSeek-V3.2, Sparse Enough?

**What I was working on.** A teardown of DeepSeek-V3.2-Exp's sparse attention — the lightning indexer that
picks 2,048 tokens per query — as two 4K masters, 16:9 and 9:16, from one beat list.

**What I tried and expected.** I expected sparse attention to make the whole attention cost sub-quadratic. I also
expected the vertical cut to wait on new scenes: the first draft of the sheet (9 beats, about 1:49) used
`ClaudeScienceLayerStack` and `ClaudeCodeBeat`, and neither has a 9:16 twin.

**Where the work resisted, and what I did next.** The cost doesn't go sub-quadratic: the indexer still scores every
earlier token, so that pass stays O(L²), just much cheaper per pair (64 small heads, FP8). Rather than write new
scenes, the build re-cut the draft onto patterns that already have 9:16 twins: the layer stack became `ReelFramework`
rows, and the code-block count became a three-bar `BlipLadder` (dense, indexer, sparse main attention). The bars made
the point better than the code did — the indexer bar stays as long as the dense one. Nine beats became eight, and the
narration came in at 1:11.9. The first 9:16 frame check failed two beats: the ask beat's segment title, "DeepSeek-V3.2 Teardown", ran past the title-safe edge at portrait width (it is now "Sparse Attention"), and the 29-character outro title filled only 51% of the end card (it is now "DeepSeek-V3.2, Sparse Enough? Count Each Pass."). A preview frame also showed the count's axis label truncated in 9:16, so it was shortened. Separately, the 9:16 sheet was missing each beat's `audio_file`, which compiles a silent narration track; it was added, and the portrait master was recompiled and loudness-checked (−23.7 dB, same as the 16:9) before delivery. After those prop fixes both masters pass the frame check clean.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
re-cut the beat list and narration onto responsive patterns, re-checked the config values against the Hugging Face
`config.json`, checked pronunciation with Kokoro's phonemizer, and ran the render and the gates. I chose the topic and
accepted the three-bar count and the "cheaper per pair, not fewer pairs" line.

**What I understand now, and what I still don't.** "Sparse" names one pass, not the model — the question to ask is
which pass got sparse. I still don't know how often the indexer drops a fact on multi-fact questions; that is the
handoff test, and it is not run here.

### Week 9 Progress: DeepSeek-V3.2

**What I was working on.** The week's progress update, as a second video: what shipped, how the week went, what
the paper taught, and what is still open — in 16:9 only; the explainer carries the 9:16 cut.

**What I tried and expected.** I expected it to be quick, and it was — the same six patterns and the same pipeline as
the explainer, authored only after the explainer's frame check had run, so every figure on screen comes from the
finished build.

**Where the work resisted, and what I did next.** Its quality-check line couldn't be written until the explainer's frame check had run, so it was authored last, after the explainer's prop fixes. The first outro line ("That's week nine.") ran 1.3 seconds — too short to read the end card — so it was lengthened. Mid-build, progress updates became 16:9 only (the explainer keeps both orientations), so this update's 9:16 render was stopped and dropped.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
drafted the update from the explainer's build results (measured narration, clip check, frame check) and rendered it.
I accepted it.

**What I understand now, and what I still don't.** Re-cutting onto patterns that already have 9:16 twins is what made
a zero-new-code vertical cut possible this week. Still open: 9:16 twins for `ClaudeScienceLayerStack` and
`ClaudeCodeBeat`, which a beat with a genuinely layered or code-shaped picture will eventually need.
