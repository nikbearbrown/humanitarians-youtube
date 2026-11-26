# Frictional log — Week of 2026-09-14

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-09-14 — reconstructed 2026-11-25

### DeepSeek-V3, Balanced Without a Penalty?

**What I was working on.** A short teardown of DeepSeek-V3 — expert routing, bias-based load balancing and
latent attention — as two 4K masters, 16:9 and 9:16, from one beat list. It opens the weekly open-model teardown
series.

**What I tried and expected.** I expected to render the series draft as written: nine beats, about 1:57 estimated,
built on `ClaudeScienceLayerStack`, `ClaudeCodeBeat` and `ClaudeWindow`. I also expected "auxiliary-loss-free" to
mean no balance loss at all.

**Where the work resisted, and what I did next.** Two of those patterns have no 9:16 twin and the third underfills
the portrait canvas, so the draft could not ship in both orientations. It was re-cut to eight beats on patterns that
render in both: the layer stack and the routing sketch became `ReelFramework` rows, and the cache arithmetic became
a `BlipLadder` (40,960 against 576 values per token per layer). The first narration measured 75.4 s, just over the
target, and two lines were tightened to 73.8 s. The report still keeps an extremely
small sequence-wise balance loss as a backstop, so the caveat beat says "mostly, not completely". The narration gate
(GATE P) wants a signed pedagogy review before audio; I review and sign off every master myself before upload, so
the sign-off was given on the finished videos. On review, the summary card's thesis said balancing "no longer needs a loss term", which contradicted the caveat beat; it was reworded to "no longer leans on a big loss term" and that one beat was re-rendered in both cuts. A build check then found that portrait masters were compiling with a silent track — the 9:16 sheet lacked each beat's audio-file reference — so the 9:16 master was recompiled from the same renders, and every master was checked for loudness before delivery. The frame check was clean in both orientations.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build
agent, re-cut the beat list and narration, re-checked every number against the arXiv text and `config.json`, checked
pronunciation with Kokoro's phonemizer, and ran the narration, renders and gates. I chose the topic and the short
format, and accepted the re-cut.

**What I understand now, and what I still don't.** The bias only steers which experts are picked, never how their
outputs are weighted. I still haven't checked how sensitive the balance is to the bias update step γ.

### Week 3 Progress: DeepSeek-V3

**What I was working on.** The week's progress update, as a second video: what shipped, how the week went, what
it taught, and what is still open, in both orientations.

**What I tried and expected.** I expected it to be quick — same patterns and pipeline as the explainer, rendered
after it so every figure on screen comes from the finished build.

**Where the work resisted, and what I did next.** The quality-check row couldn't be written until the explainer's
frame check had run, so this reel was authored last. The first cut measured 53.9 s, under the target, with a one-second end card that would also have underfilled the 9:16 frame; the summary, verdict and sign-off lines were lengthened to 57.5 s and the end-card title extended to “Week 3 Progress: DeepSeek-V3, Built From Parts” before rendering. The frame check was clean in both orientations.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude drafted the update
from the build's own measurements and the report, and rendered it. I accepted it.

**What I understand now, and what I still don't.** Re-cutting onto patterns that render in both orientations is
what let the teardown ship in 16:9 and 9:16 without new scene code. Still open: 9:16 twins for
`ClaudeScienceLayerStack` and `ClaudeCodeBeat`.
