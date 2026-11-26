# Frictional log — Week of 2026-09-28

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-09-28 — reconstructed 2026-11-25

### Llama 4, Ten Million Tokens?

**What I was working on.** A short teardown of Llama 4 Scout — interleaved RoPE and no-position layers,
chunked attention, and the 10,485,760-token configured maximum — as two 4K masters, 16:9 and 9:16, from one beat list.

**What I tried and expected.** I expected to render the series draft as written: nine beats, about 1:55 estimated,
built on `ClaudeScienceLayerStack`, `ClaudeCodeBeat` and `ClaudeWindow`, with the skeptic's point resting on the
config value alone.

**Where the work resisted, and what I did next.** The same three patterns blocked the 9:16 cut, so the draft was
re-cut to eight beats: the layer pattern and the two attention masks became `ReelFramework` rows, and the worked
example became a two-bar `BlipLadder` (3,617 against 20,001 tokens visible to the token at position 20,000). Re-reading
Meta's release post for the re-cut, I found it says Scout was pre- and post-trained with a 256K context length, which
makes the skeptic's beat concrete: the trained length sits far below the configured ceiling, so the reel shows both
numbers. The first estimate ran 81.7 s; the narration was tightened to 68.3 s. The narration gate (GATE P) wants a signed pedagogy review before audio; I review and sign off every master
myself before upload, so the sign-off was given on the finished videos.
Before rendering, the end-card title was extended to “Llama 4, Ten Million Tokens? Configured, Not Measured.”, because short titles underfill the 9:16 end card. Both masters were checked for loudness, and the frame check was clean in both orientations.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build
agent, re-cut the beat list and narration, re-checked every number against the primary source and `config.json`,
checked pronunciation with Kokoro's phonemizer, and ran the narration, renders and gates. I chose the topic and the
short format, and accepted the re-cut.

**What I understand now, and what I still don't.** Past its 8,192-token chunk, a token hears older context only
through the 12 NoPE layers. I don't know how well that holds at length — that needs a needle-plus-reasoning grid at
several lengths and depths.

### Week 5 Progress: Llama 4 Scout

**What I was working on.** The week's progress update, as a second video: what shipped, how the week went, what
it taught, and what is still open — as a single 16:9 master, since progress updates are now landscape-only.

**What I tried and expected.** I expected it to be quick — same patterns and pipeline as the explainer, rendered
after it so every figure on screen comes from the finished build.

**Where the work resisted, and what I did next.** The quality-check row couldn't be written until the explainer's
frame check had run, so this reel was authored last. Like last week's, it ships as a single 16:9 master; its end-card title was set to “Week 5 Progress: Llama 4 Scout, Built From Parts” before rendering. The frame check was clean.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude drafted the update
from the build's own measurements and the release post and config, and rendered it. I accepted it.

**What I understand now, and what I still don't.** A configured maximum is a promise from the code; only a test at length is evidence. Still open: 9:16 twins for
`ClaudeScienceLayerStack` and `ClaudeCodeBeat`.
