# Week 24 topic-video — final

*Which of Gardner's Eight Intelligences Can a Machine Do?* Tanmay Kulkarni, in for Humanitarians AI.
Assembled 2026-09-27: the record of how both films were made and verified, with their captions and
YouTube descriptions.

Text and code only. **The two masters live in the shared Google Drive**, not in this repository.
See the links below. The working folder (audio, clips, QC frames and the reference builds) is
outside this repo.

## Where the topic came from

**Source topic:** `claude-for-design/introducing-theoristai` in the `humanitarians-youtube` repository,
an unbuilt 10-beat auto-conversion of **Nik Bear Brown's essay ["Introducing Theorist.ai"](https://humanitariansai.substack.com/p/introducing-theoristai)**
(Humanitarians AI, March 2026; cross-posted to NortheasternISE as "Knowing Enough to Distrust the
Machine").

- **The film builds on one sentence of that essay:** that Gardner's 1983 framework "did not need to
  ask which intelligences were endangered by technology, because technology — in 1983 — was not yet a
  serious competitor to any of them." It does not take up the essay's wider argument about education.
- **Selection:** a randomized, unseeded draw over the library's singleton topics. Draw 3, after
  draws 1 and 2 were rejected as fellow-authored.
- **Uniqueness:** checked against `main` and all 46 fellow branches, read-only, on an isolated
  bare mirror; nothing in the shared repo was checked out, fetched into or modified. No fellow has
  built or extended it. The source author is the founder, not a fellow.

The full draw, exclusions and uniqueness evidence are in `TOPIC-DECISION.md`.

## The files

| | File | | |
|---|---|---|---|
| **Long** | `gardner-eight-intelligences-machine-final.mp4` | 3840×2160 · 24 fps · 5:46 (346.0s) | −14.9 LUFS / −1.9 dBFS |
| **Short** | `gardner-eight-rooms-short-final.mp4` | 2160×3840 · 24 fps · 1:37 (96.5s) | −14.8 LUFS / −1.9 dBFS |

Each film's master is on Drive (below); its captions (`.srt` and `.vtt`) and YouTube title, description and tags
(`*-youtube.md`) are in this folder.

**Structure:**
- **Long, "EIGHT ROOMS":** Gardner's theory as a house. The camera walks into each room, and a light
  comes on only when Gardner's own writing says a machine does what that room is for.
- **Short, "ONE HOUSE, ONE CAMERA":** its own script, not a cut of the long. One continuous take
  of the same house, with its own ending, and it points to the long for the rest.

## Links

Drive links added 2026-09-28. Add the YouTube URL once each film is live.

| | Drive | YouTube |
|---|---|---|
| Long (16:9, 4K) | [Drive](https://drive.google.com/file/d/18oBFVkfVDDN8z4SXJoEduqzuTUQJVmAY/view?usp=drive_link) | *(to add)* |
| Short (9:16, 4K) | [Drive](https://drive.google.com/file/d/1rQQmz8awD92X9UZS06K2E43x3hcgJsLO/view?usp=drive_link) | *(to add)* |

**One dependency.** The Short's description (`gardner-eight-rooms-short-youtube.md`) points to
the long's Drive link for now. Once the long is live, swap in its YouTube URL and set it as the
Short's related video in YouTube Studio.

## Uploading: three choices only you can make

1. **Altered or synthetic content.** The narration is a synthetic voice (Kokoro), speaking as Tanmay
   Kulkarni. Both descriptions say so. Whether to also tick YouTube's "altered or synthetic content"
   box is your call. It's meant for realistic content that could mislead, and a voice that introduces
   itself by a real name is the case to think about.
2. **Thumbnail.** Both films open on ~0.3s of cream while the first scene fades in. Pick a custom
   thumbnail rather than frame 0.
3. **Captions.** Upload the `.srt` as English captions, not YouTube's auto-captions. It shows the
   written forms of names and years ("Furuzawa", "Stachura", "1983"), where the audio uses spellings
   the voice needs.

## The record

- **`FACTCHECK.md`:** every claim with its verification level. Every quote was checked against raw
  page text, and the rejected or qualified claims are kept.
- **`TOPIC-DECISION.md`:** the draw, exclusions and uniqueness verification.
- **`PEDAGOGY.md`:** the signed Gate P record. Read aloud and signed by Tanmay Kulkarni, 2026-09-26
  (long) and 2026-09-27 (Short, in `SHORT.md`). It notes one post-sign-off TTS spelling change
  (years written in words), with the words themselves unchanged.
- **`READ-ALOUD.md`** (and `READ-ALOUD-SHORT.md`): the sheets Gate P was read from.
- **`BEATS-DRAFT.md`:** the structural reasoning behind EIGHT ROOMS.
- **`PROOF-REVIEW-FINAL.md`, `PROOF-REVIEW-SHORT.md`, `PROOF-REVIEW-BOTH.md`:** every review
  pass, the defects each found, and how each was fixed and re-measured. The last is the joint sign-off:
  - both films **clear-for-public**
  - long **10/12** (the two 1s are by design), Short **12/12**
  - production gate PASS
  - claims on screen when spoken: **35/35** and **16/16** (timed on the Whisper clock)
  - 0 dark frames, and 0 Shorts-UI-zone failures on the Short

## Rebuilding

`beat_sheet.json` (and `beat_sheet-short.json`) is the source of truth, generated by
`build_beat_sheet.py` / `build_short_sheet.py`. The build runs in the working folder, where the
audio and clips live; the scripts here are the record of it. Measured Kokoro audio is the clock and is never hand-repaired.

```
python3 build_beat_sheet.py                 # narration + props; cues from the measured audio (cue_align.py)
<toolkit>/generate_audio_kokoro.py <reel>   # only after Gate P
<toolkit>/remotion_scenes.py <reel> --only <beat> --force   # never while a sheet rebuild is running
<toolkit>/compile.py <reel> --height 2160   # 3840 for the Short
pacing_pass.py <reel> --hold 0.3            # then two-pass loudnorm to −14 LUFS / −2 dBTP
python3 make_captions.py . 0.3              # and: python3 make_captions.py short 0.3
```

**Timing note.** Cues and captions are timed from the audio itself (`cue_align.py`):
- **Pause clock (most beats):** sentences are pinned to the real pauses in each beat's audio.
- **Whisper clock (B05, B06, B07, B17 in the long; S02, S04, S05 in the Short):** Whisper
  (`whisper_align.py`, faster-whisper base.en, run locally) supplies the word timings, snapped to
  the audio's own pauses.
- **Why the split:** Whisper confirmed the pause clock within 0.23s everywhere except those beats'
  mid-phrase cues, which were 0.3–1.4s off. Only those seven beats were re-rendered.
- **Captions:** use the Whisper clock throughout.
- **Words:** Whisper also checked what the voice said, word by word, against the script. There
  were no mispronunciations, and every difference was a transcription spelling ("a jar", "Kolkarni").
