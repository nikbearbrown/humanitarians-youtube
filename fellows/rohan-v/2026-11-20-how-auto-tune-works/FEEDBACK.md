# FEEDBACK — "How Auto-Tune Works"

Reviewer notes. No reviews yet; the open questions below are for Rohan V.'s review.

## Open questions for Rohan V.

1. **Does the synthetic "ah" singer sound convincing in B05?** It is a source-filter voice: a buzzing source shaped
   by four fixed "ah" resonances, one vowel throughout, no consonants or breath, with a scoop into each note,
   vibrato and slow drift added on purpose. Does it read as a singer, or as a synth? If it sounds too artificial,
   does that weaken the point of the three takes?
2. **Are the three takes distinguishable on phone speakers?** The differences are small in absolute terms: as sung
   about 29 cents off on average, gentle 6.5, retune speed zero 0.4 (with about ±8 cents of wobble left). Each take
   is 3.89 s with 0.7 s between them. On a phone speaker, and on earbuds, can you hear as sung → gentle → zero
   change, and does zero sound robotic? Please say what you listened on.
3. **The gentle take's last note.** "Averaged under seven cents" is true as an average (6.5), but the final held
   C4 is still 19 cents flat after gentle correction (FACTCHECK row 15). The narration now says "averaged"; is the
   flat ending audible in B05, and does it need a word?
4. **B04, "Auto-Tune's patent keeps the length by repeating whole cycles."** The "patent's way" in the run is my
   reconstruction from the patent's text, not Antares' code, and later versions added formant correction. Is it
   clear enough that B04 is about the patent's method, not today's product?
5. **LOGO LAW.** Antares is named on screen in B06 ("ANTARES AUDIO TECHNOLOGIES") without its mark: no Antares logo
   was in the toolkit, and downloading one needs your OK. Should one be downloaded and added?
6. **Chapter times in the description** come from the beat durations (137.27 s in all); check them against the
   final cut.

## Settled before review (2026-11-19)

Raised by the fact check (an independent Claude agent; FACTCHECK) and re-voiced the same day (BUILD-LOG §2):

- **B03.** "my singer was under seven cents off" → "my singer averaged under seven cents off": the 6.5 is an
  average, and one note is 19 cents flat.
- **B08.** The close now names the job ("Find the repeat, pick the note, and shift the pitch.") rather than my
  PSOLA method, which is not the patent's.

Snapshot review fixes (BUILD-LOG §5): detector-miss spikes in the drawn pitch tracks, tracks washed to white, B04's
blank 3D stage, colliding lane labels, phone label overlaps.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration forces
regenerating that beat's audio and re-running `bash ../run_audio.sh <reel>` (Kokoro, `align.py`, `mix_listen.py`
for B05's takes, `sync_cues.py`, then `props.durationSeconds`), rebuilding and re-rendering the scene
(`python build_hf.py B0x --render` for a HyperFrames beat, which reads the new cues), and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | PITCH | HyperFrames `pitch` (`hyperframes/B01-l.html`, `B01-v.html`, `scenes/B01.js`) |
| B02 | OFF KEY | HyperFrames `offkey` |
| B03 | SNAP | HyperFrames `snap` |
| B04 | SHIFTING | HyperFrames `shift` |
| B05 | LISTEN | HyperFrames `listen`, + the three takes (`evidence/take.wav`, `gentle.wav`, `hard.wav`) |
| B06 | THEN AND NOW | HyperFrames `history` |
| B07 | WHAT TO DO | `HaiApplyCard` |
| B08 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [evidence/run.log](./evidence/run.log). Re-running the evidence is
`python autotune.py` (seeded, so the numbers and the takes repeat), then `python build_hf.py` to rewrite the
compositions. Rendering writes its temporary frames to D:, never C:.
