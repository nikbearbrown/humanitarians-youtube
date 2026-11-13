# FEEDBACK — "How Netflix Streams"

Reviewer notes. No reviewer has left notes yet; the open questions below are for the first review.

## Open questions for reviewers

1. **B02 and B03, synthetic clips.** The grainy clip's random grain is a harsher case than real film grain, and
   VMAF was trained on natural video, not test patterns. Is "my test card" / "the grainy clip" enough of a label, or
   should B03 say the clips are test material?
2. **Description timestamps** are the summed narration lengths (the week-11 method); check them against the final.
3. **Pacing.** At 2:08 this is shorter than last week's 2:37. Is any beat too fast for a beginner, especially B04
   (59 words in 18.9 s)?

## Settled before review (2026-11-10)

Raised by the first fact check and fixed in the film the same day (FACTCHECK, "Flags, corrected"; BUILD-LOG §2,
§5):

- **B04, red blocks on lanes that never stalled.** Only real stalls are red now: one block, always-the-best, chunk
  50.
- **B04, the speed ribbon.** Now placed on the chunks' axis, so its dips sit over the chunks they slowed.
- **B04, "looked better".** Now "streamed at a higher quality", the bitrate claim the run supports.
- **B06, 2022 figures in the present tense.** Now "By twenty twenty-two, that network had…", labelled "· 2022" in
  both cuts.
- **B07, "more than".** Now "matters as much as"; the card's unsourced cable tip is gone.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration
forces regenerating that beat's audio, re-running `align.py` and `sync_cues.py`, writing
`props.durationSeconds` (all in `bash ../run_audio.sh <reel>`), rebuilding and re-rendering the scene
(`python build_hf.py B0x --render` for a HyperFrames beat, which reads the new cues), and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | THE LADDER | HyperFrames `ladder` (`hyperframes/B01-l.html`, `B01-v.html`, `scenes/B01.js`) |
| B02 | VMAF | HyperFrames `vmaf` |
| B03 | PER TITLE | HyperFrames `pertitle` |
| B04 | THE PLAYER | HyperFrames `player` |
| B05 | CLOSE BY | HyperFrames `cdn` |
| B06 | SCALE | HyperFrames `scale` |
| B07 | WHAT TO DO | `HaiApplyCard` |
| B08 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [evidence/run.log](./evidence/run.log). Re-running the evidence is
`python stream.py` (the player is seeded and the encodes are deterministic settings, so the numbers should repeat;
a different ffmpeg or libvmaf build may move the scores slightly), then `python build_hf.py` to rewrite the
compositions. Rendering writes its temporary frames to D:, never C:.
