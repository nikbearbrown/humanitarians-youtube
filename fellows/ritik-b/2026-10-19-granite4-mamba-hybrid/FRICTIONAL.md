# Frictional log — Week of 2026-10-19

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-10-19 — reconstructed 2026-11-25

### Granite 4.0, Mostly Mamba?

**What I was working on.** A one-minute re-cut of the Granite 4.0-H-Small teardown — 36 Mamba-2 layers and four
attention layers, no position encoding — as two 4K masters, 16:9 and 9:16, from one beat list.

**What I tried and expected.** The drafted teardown ran 9 beats, about 1:53 by estimate, with a
`ClaudeScienceLayerStack` beat and two `ClaudeCodeBeat` beats that have no 9:16 twin. I rebuilt the layout and the
no-position-encoding argument as `ReelFramework` rows and the memory arithmetic as a `BlipLadder` chart, and expected
the draft's numbers to carry over unchanged.

**Where the work resisted, and what I did next.** Most did: every config number re-checked (attention at layers 6,
16, 26, 36; 8 KV heads × 128; Mamba-2 128 heads × 64 × 128 state; `position_embedding_type: nope`), and the recurrence
the reel shows is the Mamba-2 paper's §2.1, eq. 2. One draft line did not: it credited "IBM's pitch" of memory savings
on long, concurrent workloads to the model card, and the model card never mentions memory, so the line was cut rather
than re-sourced. On a gigabyte axis the 75 MB Mamba state prints as 0.1, so its bar's label carries "≈ 75 MB". The
end-card title was set to 51 characters before rendering so the portrait card fills the frame. Measured narration:
1:15.2 over 8 beats, a fraction over the target. The narration gate (GATE P) wants a signed review before audio; I
review and sign off every master myself before upload, so audio came first and the sign-off was given on the finished
videos.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
re-cut the beat list and narration, re-checked every number against `config.json`, the model card and the arXiv text,
checked pronunciation of "IBM's", "Mamba two" and "rope" with Kokoro's phonemizer, and ran the render and the gates.
I chose the topic and accepted the re-cut, including cutting the unsupported vendor line.

**What I understand now, and what I still don't.** With Mamba carrying word order, the attention layers can drop
position encoding entirely. What I still don't know is how far exact retrieval survives on four layers out of forty —
the hand-off's needle test at 4K, 32K and 128K is how to find out.

### Week 8 Progress: Granite 4.0

**What I was working on.** The week's progress update, as a second video: what shipped, how the week went, what it
taught, and what is still open. Progress updates are 16:9 only.

**What I tried and expected.** Same patterns and pipeline as the explainer, authored after the explainer's frame check
so every figure on screen comes from the finished build.

**Where the work resisted, and what I did next.** The lesson beat had to name a cut without overstating it: the draft's
vendor memory line wasn't wrong so much as unsupported by the page it cited, so the update says the card never makes
the claim and that the line was removed. Measured narration: 0:58.5 over 7 beats; frame check clean.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude drafted the update
from this week's build and rendered it. I accepted it.

**What I understand now, and what I still don't.** A source line is a promise that the cited page says the thing; it
is cheaper to check that while re-cutting than after upload. Still open: 9:16 twins for `ClaudeScienceLayerStack` and
`ClaudeCodeBeat`.
