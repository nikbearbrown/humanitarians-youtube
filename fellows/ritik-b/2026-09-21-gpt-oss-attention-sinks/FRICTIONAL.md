# Frictional log — Week of 2026-09-21

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-09-21 — reconstructed 2026-11-25

### gpt-oss, Paying Attention to Nothing?

**What I was working on.** A short teardown of gpt-oss-120b — the learned attention sink in every head and
the alternating sliding-window layout — as two 4K masters, 16:9 and 9:16, from one beat list.

**What I tried and expected.** I expected to render the series draft as written: nine beats, about 1:55 estimated,
built on `ClaudeScienceLayerStack`, `ClaudeCodeBeat` and `ClaudeWindow`. I also expected the sink to need a long
explanation.

**Where the work resisted, and what I did next.** As with last week's teardown, two of those patterns have no 9:16
twin and the third underfills the portrait canvas, so the draft was re-cut to eight beats: the layer stack and the
softmax sketch became `ReelFramework` rows, and the cache arithmetic became a three-bar `BlipLadder` (≈ 9.7 GB
all-full, ≈ 4.8 GB as built, ≈ 4.7 MB for the sliding layers). The first trim measured 64.2 s, just under the target,
so one line was restored, giving 66.8 s. The cache figures rest on an assumption the
config doesn't state — a 2-byte cache — so the beat says so on screen. The sink itself is one sentence in the model
card, so the reel states what it does and that its per-head behaviour isn't documented. The narration gate (GATE P) wants a signed pedagogy review before audio; I review and sign off every master
myself before upload, so the sign-off was given on the finished videos.
Before rendering, the end-card title was extended to “gpt-oss, Paying Attention to Nothing? By Design.”, because short titles underfill the 9:16 end card, and the 9:16 sheet was re-synced so it carries every beat's audio-file reference. Both masters were checked for loudness, and the frame check was clean in both orientations.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build
agent, re-cut the beat list and narration, re-checked every number against the primary source and `config.json`,
checked pronunciation with Kokoro's phonemizer, and ran the narration, renders and gates. I chose the topic and the
short format, and accepted the re-cut.

**What I understand now, and what I still don't.** The sink lets the attention weights over real tokens sum to less
than one, so a head can effectively opt out. I don't know yet which layers lean on it most — sliding or full; that
needs measuring on the 20b model.

### Week 4 Progress: gpt-oss

**What I was working on.** The week's progress update, as a second video: what shipped, how the week went, what
it taught, and what is still open — as a single 16:9 master, since progress updates are now landscape-only.

**What I tried and expected.** I expected it to be quick — same patterns and pipeline as the explainer, rendered
after it so every figure on screen comes from the finished build.

**Where the work resisted, and what I did next.** The quality-check row couldn't be written until the explainer's
frame check had run, so this reel was authored last. From this week the progress updates ship as a single 16:9 master, so only the landscape cut was rendered; its end-card title was set to “Week 4 Progress: gpt-oss, Built From Parts” before rendering. The frame check was clean.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude drafted the update
from the build's own measurements and the model card, and rendered it. I accepted it.

**What I understand now, and what I still don't.** One learned number per head is enough to let attention opt out, and an alternating layout is checkable from the config alone. Still open: 9:16 twins for
`ClaudeScienceLayerStack` and `ClaudeCodeBeat`.
