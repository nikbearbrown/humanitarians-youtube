# FEEDBACK — "How Spatial Audio Works"

Reviewer notes. No reviews yet; the open questions below are for the first reviewers.

## Open questions for reviewers

1. **Does the B04 listening clip read as circling on ordinary earbuds?** It is rendered by my head model: timing,
   the head's shadow, and, for the half of the turn behind your ears, my outer-ear stand-in (a simple high cut,
   not a real ear's peaks and notches). The left/right part of the cue lives entirely in the difference between
   the two channels. On wired earbuds or basic Bluetooth earbuds, does it sound like a turn around your head, a
   swing from side to side, or something inside your head? Does the behind half sound behind you, or just duller?
   Does it help to watch the orbit and the dial while listening? Please say what you listened on. On a phone
   speaker or a mono setting the clip carries no direction at all. It hasn't been tested with listeners yet.
2. **The phone cut drops B04's "rendered by my model" note** (it was cut to keep the phone column clear). The
   chart above it now says "MY MODEL'S FILTER PAIR"; is the clip's origin clear enough on the phone?
3. **B05: "so it stays put in the room."** Apple says the sound stays anchored to the device (the iPhone or iPad);
   the two agree while the device stays still. Is the simplification fair?
4. **B02's "fourteen decibels".** Real heads give about 20 dB at 4 kHz (fact sheet §1.7), so my sphere is milder.
   The narration says "in my model"; is that enough?
5. **Dolby is named on screen in B07 without a mark.** The standard apply card has no logo slot. Does LOGO LAW
   want Dolby's mark there, and if so, where?
6. **Chapter times in the description** come from the beat durations (128.22 s in all); check them against the
   final cut.

Resolved before review (BUILD-LOG §6): B06's "3200 POINTS" counter removed; B06's spark line reworded; B04's chart
titled "MY MODEL'S FILTER PAIR"; the circling clip given the outer-ear cue for its behind half.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration forces
regenerating that beat's audio and re-running `bash run_audio.sh <reel>` (Kokoro, `align.py`,
`mix_listen.py` for B04's clip, `sync_cues.py`, then `props.durationSeconds`), rebuilding and re-rendering the
scene (`python build_hf.py B0x --render` for a HyperFrames beat, which reads the new cues), and recompiling both
cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | TIMING | HyperFrames `itd` (`hyperframes/B01-l.html`, `B01-v.html`, `scenes/B01.js`) |
| B02 | LEVEL | HyperFrames `ild` |
| B03 | FRONT OR BACK | HyperFrames `frontback` |
| B04 | THE FILTERS | HyperFrames `hrtf`, + the stereo listening clip (`evidence/circle.wav`) |
| B05 | HEAD TRACKING | HyperFrames `tracking` |
| B06 | YOUR EARS | HyperFrames `personal` |
| B07 | WHAT TO DO | `HaiApplyCard` |
| B08 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [evidence/run.log](./evidence/run.log). Re-running the evidence is
`python spatial.py` (seeded, so the numbers and the clip repeat), then `python build_hf.py` to rewrite the
compositions. Rendering writes its temporary frames to D:, never C:.
