# FEEDBACK — "How Bluetooth Audio Works"

Reviewer notes. No reviews yet; the open questions below are for Rohan V.'s review.

## Open questions for Rohan V.

1. **Is the single dropout in the small-buffer clip audible enough?** The 50 ms clip has two glitches 0.13 s apart
   inside one body-blocking moment, heard as one short stutter about 2.1 s into the clip; the 200 ms clip has none.
   The window was picked as typical (2 glitches in its 6 s against 1.5 expected), not as the worst moment. On your
   earbuds or phone speaker, do you hear the stutter without being told where it is? If not: point at it on screen
   more strongly, pick a busier window, or use the 20 ms buffer (103 glitches in two minutes), at the risk of
   overstating how often real earbuds cut out.
2. **Length.** The video runs about 2:26 (146.30 s), longer than the usual ~2:08. B04 alone is 30.49 s with its two
   clips. Is the pace right for a beginner, and if something should go, which beat?
3. **Logos.** No Bluetooth SIG, Qualcomm (aptX), Sony (LDAC) or Antares (the Auto-Tune reel) logos were used: none
   was in the toolkit, and downloading needs your OK. Apple, Android and ffmpeg appear with their marks from the
   toolkit. Sony is named on screen in B03 ("LDAC · UP TO, SONY") and the Bluetooth SIG in B06 ("SAYS THE BLUETOOTH
   SIG") without a mark. Should those marks be downloaded and added?
4. **B03 on the phone, "AAC · APPLE 272".** The 272 kbit/s is ffmpeg's AAC encoder on my test track, not what an
   iPhone sends. In landscape the note under the bars says so ("measured on my test track with ffmpeg's encoders");
   on the phone that note is dropped to keep the column clear. Is the bar misleading there without it?
5. **Chapter times in the description** come from the beat durations (146.30 s in all); check them against the
   final cut.

## Settled before review (2026-11-19)

Raised by the fact check (an independent Claude agent; FACTCHECK) and re-voiced the same day (BUILD-LOG §2):

- **B02.** The earlier "twenty-two percent … under eight percent" included body blocking, which B02 never
  mentions. Now the Wi-Fi-only figures: seventeen percent, about one percent; the HUD shows 17% and 0.9%.
- **B03.** "Apple's devices use AAC" → "prefer AAC" (they fall back to SBC when the headphones lack AAC).
- **B06.** "The newest version, LE Audio" → "Bluetooth's next generation, LE Audio": LE Audio is not a version of
  Bluetooth.
- Also re-worded: B01 "under a quarter" (23%); B04 names both causes of lost packets ("from Wi-Fi or your own
  body") and calls the reserve "the main reason" Bluetooth lags, not the only one; B04 and B05 trimmed for length.

Snapshot review fixes (BUILD-LOG §5): 3D labels outside the stage, B04's tank labels on the phone, long bar labels.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration forces
regenerating that beat's audio and re-running `bash ../run_audio.sh <reel>` (Kokoro, `align.py`, `mix_listen.py`
for B04's clips, `sync_cues.py`, then `props.durationSeconds`), rebuilding and re-rendering the scene
(`python build_hf.py B0x --render` for a HyperFrames beat, which reads the new cues), and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | TOO MUCH DATA | HyperFrames `data` (`hyperframes/B01-l.html`, `B01-v.html`, `scenes/B01.js`) |
| B02 | THE RADIO | HyperFrames `hopping` |
| B03 | CODECS | HyperFrames `codecs` |
| B04 | THE BUFFER | HyperFrames `buffer`, + the two listening clips (`evidence/small_buffer.wav`, `large_buffer.wav`) |
| B05 | LIP SYNC | HyperFrames `lipsync` |
| B06 | LE AUDIO | HyperFrames `leaudio` |
| B07 | WHAT TO DO | `HaiApplyCard` |
| B08 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [evidence/run.log](./evidence/run.log). Re-running the evidence is
`python bluetooth.py` (the track and the radio are seeded, so the simulation and the clips repeat; a different
ffmpeg build may move the measured data rates slightly), then `python build_hf.py` to rewrite the compositions.
Rendering writes its temporary frames to D:, never C:.
