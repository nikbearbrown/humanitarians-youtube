# Frictional log — Week of 2026-10-05

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-10-05 — reconstructed 2026-11-25

### Qwen3-Next, Attention Optional?

**What I was working on.** A one-minute re-cut of the Qwen3-Next-80B-A3B teardown — Gated DeltaNet layers in a
3:1 hybrid with gated full attention — as two 4K masters, 16:9 and 9:16, from one beat list.

**What I tried and expected.** The drafted teardown ran 9 beats, about 1:54 by estimate, and leaned on a
`ClaudeScienceLayerStack` beat and two `ClaudeCodeBeat` beats. I expected to trim narration and keep the beats. Those
two patterns have no 9:16 twin, though, so the layer stack and the delta-rule sketch became `ReelFramework` rows and
the memory arithmetic became a `BlipLadder` chart. I expected the memory beat to be one ratio.

**Where the work resisted, and what I did next.** Re-checking `config.json` for the chart turned the 512x headline
into a statement about one context length: a full-attention layer's cache (2 × 256 × 2 = 1,024 values per token)
equals the DeltaNet state (32 × 128 × 128 = 524,288 values) at exactly 512 tokens. So the chart shows 512, 4K, 32K
and 262K tokens and says where the break-even is. To fit about a minute I folded the draft's separate trade-off beat
into the verdict and the hand-off; measured narration came to 1:07.0 over 8 beats. The first 9:16 master compiled
with a silent track — the portrait sheet was missing the per-beat audio paths — and a loudness check caught it, so the
sheet was patched and the master recompiled. The portrait end card then failed the frame check at 49% fill with the
31-character title, so the end-card title became "Qwen3-Next: Attention Optional, or Rationed?" in both cuts and that
beat was re-rendered; both cuts are now clean. The narration gate (GATE P) wants a signed review before audio; I
review and sign off every master myself before upload, so audio came first and the sign-off was given on the
finished videos.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
re-cut the beat list and narration, re-checked every number against `config.json`, the model card and the arXiv text
(the gated delta rule is §3.1, eq. 10), checked pronunciation with Kokoro's phonemizer, and ran the render and the
gates. I chose the topic and accepted the re-cut, including keeping the hand-off probe over a separate trade-off beat.

**What I understand now, and what I still don't.** A fixed-size state is not automatically smaller: here it wins only
past 512 tokens, and by 512x only at the full 262,144. I still don't know how much exact recall the hybrid loses —
that is what the hand-off's 20-key probe would measure.

### Week 6 Progress: Qwen3-Next

**What I was working on.** The week's progress update, as a second video: what shipped, how the week went, what it
taught, and what is still open. Progress updates are 16:9 only.

**What I tried and expected.** I expected a progress update to be quick, and it was — same patterns, same pipeline as
the explainer, authored after the explainer's frame check so every figure on screen comes from the finished build.

**Where the work resisted, and what I did next.** Its quality line changed while I wrote it: the explainer's portrait
end card first failed the frame check, then passed after the re-titled end card was re-rendered, so the "shipped" beat
was re-narrated to say clean in both orientations after one end-card fix. Its own end-card title was set to 45
characters before rendering so the card fills the frame. Measured narration: 0:58.9 over 7 beats; frame check clean.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude drafted the update
from this week's build and rendered it. I accepted it.

**What I understand now, and what I still don't.** Re-cutting onto patterns that already have 9:16 twins is what kept
the week to zero new scene code. Still open: 9:16 twins for `ClaudeScienceLayerStack` and `ClaudeCodeBeat`.
