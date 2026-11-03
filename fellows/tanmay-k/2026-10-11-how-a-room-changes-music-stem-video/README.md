# How a Room Changes Music: One Cellist, Seven Concert Halls

*How a Room Changes Music: One Cellist, Seven Concert Halls.* Tanmay Kulkarni, in for Humanitarians AI · Week 26 topic
video · built 2026-10-10

Text and code only. **The two masters live in the shared Google Drive**, not in this repository. See the links below.
The working folder (audio, clips, stills, QC frames) is outside this repo.

> **This repository copy:** the two `.mp4` masters aren't committed (video is gitignored repo-wide), and neither is
> the simulated cathedral's audio (`ir/simulated-cathedral.wav`). `make_ir.py` regenerates it from its seed, and
> `ir/simulated-cathedral.json` records its measurements. The Short's files sit alongside the long's instead of in
> `short/`: `beat_sheet-short.json`, `FACTCHECK-SHORT.md`, `SHOTLIST-SHORT.md`, `READ-ALOUD-SHORT.md`,
> `build_short_sheet.py`, `make_read_sheet_short.py` and the `…-short.*` captions and metadata. Where the records
> below say `short/…`, read the flat name.

## The topic

**Chosen topic: `claude-for-music/how-music-works-audible`** in the `humanitarians-youtube` repository.
It's an unbuilt 10-beat auto-conversion of Humanitarians AI's review
**["How Music Works"](https://humanitariansai.substack.com/p/how-music-works-audible)** (February 2026;
credited in the repo to Nik Bear Brown, Founder) of David Byrne's *How Music Works* (2012).

- **The film builds on the review's two ideas:** that the room shapes music, and that recording
  technology does too. It went looking for people who *measured* the first. It found one cellist, seven
  halls, and a slowdown at both ends, then extended it to twelve players, birds, a 78 rpm record and the
  skip button.
- **Selection:** a randomized, unseeded draw over the library's singleton topics. Draw 1 of 5.
- **Uniqueness:** checked against `main` and all 60 fellow branches, read-only, on an isolated bare
  mirror; nothing in the shared repo was checked out, fetched into or modified. The one neighbour (a
  fellow's audio-engineering series on MP3s, loudness and mono phones) is a recorded boundary, and the
  film stays off it. The angle's narration was also checked against all of our Week 15–25 films.

The draw, exclusions and uniqueness evidence are in `TOPIC-DECISION.md`; the angle and its boundaries
are in `ANGLE.md`.

## The files

| | File | | |
|---|---|---|---|
| **Long** | `how-a-room-changes-music-final.mp4` | 3840×2160 · 24 fps · 6:19 (379.2 s) | −14.7 LUFS / −1.9 dBTP |
| **Short** | `how-a-room-changes-music-short-final.mp4` | 2160×3840 · 24 fps · 2:15 (135.4 s) | −14.8 LUFS / −1.9 dBTP |

Each film carries its captions (`.srt` and `.vtt`) and its YouTube title, description, chapters and
tags (`*-youtube.md`) beside it.

**Structure:**
- **Long, "THE VOICE CHANGES ROOMS":** the film's form is its own sound. One sentence is heard inside a
  simulated cathedral, then with room between its phrases. The argument runs: wet room → one player →
  many players → noise → machines. The decide/ask test comes at B13, the viewer's own clap task at
  B18–B20, and the same sentence returns at the end in two opposite rooms.
- **Short:** its own script, one arc, for a viewer who never sees the long film. It has its own
  framework beat, clap task and payoff, and uses only portrait-safe components.

## Links

Add the temporary Drive links and, once live, the YouTube URLs.

| | Drive | YouTube |
|---|---|---|
| Long (16:9, 4K) | <!-- DRIVE_LINK_LONG --> *(to add)* | <!-- YOUTUBE_LINK_LONG --> *(to add)* |
| Short (9:16, 4K) | <!-- DRIVE_LINK_SHORT --> *(to add)* | <!-- YOUTUBE_LINK_SHORT --> *(to add)* |

**Placeholder in the descriptions:** `[FULL VIDEO LINK]` in the Short's description. Swap in the long's
YouTube URL once it's live, and set the long as the Short's related video in YouTube Studio.

## Before public: one open condition

**FACTCHECK A1, A5 and A18 are still sourced from reviews and summaries of the book, not the book
itself:**
- A1: Byrne's chapter-1 argument
- A5: CBGB as a room with very little echo
- A18: Edison's cylinders

Check them against *How Music Works*. If one fails, only B05/B06/B15 (and S02/S03 in the Short) change:
audio, render and compile for those beats. This is the condition in `PROOF-REVIEW-3.md` and
`PROOF-REVIEW-4.md`. Optional: read the 20 s → 5 s intro figures in the paper itself (A20); the Ohio
State citation is on screen meanwhile.

## Uploading: three choices only you can make

1. **Altered or synthetic content.** The narration is a synthetic voice (Kokoro), introducing itself as
   Tanmay Kulkarni, and the cathedral echo is simulated. Both descriptions say so. Whether to also
   tick YouTube's "altered or synthetic content" box is your call.
2. **Thumbnail.** Pick a custom one. B09's arch with "slower too" and "74%" is the strongest frame;
   D02's four islands of voice with the echo between them is the most distinctive.
3. **Captions.** Upload the `.srt` as English captions, not YouTube's auto-captions. It shows the
   written forms ("1752", "74%", "303", "78 rpm") where the voice says the words, and no name is
   ever split across two cues.

## The record

- **`FRICTIONAL.md`:** the dated process log: what was tried, where it resisted, what was done next,
  and who decided. Drafted from the records; awaiting your review.
- **`FACTCHECK.md`:**
  - A1–A22: every claim, with its source.
  - B1–B5: our own demonstration, heuristic, test and simulated echo.
  - §C: what was researched and left out, including the measured cathedral IR, cut because its own
    licence file says non-commercial.
- **`TOPIC-DECISION.md`**, **`ANGLE.md`:** the draw, the uniqueness checks, the angle and its boundaries.
- **`PEDAGOGY.md`:** the signed Gate P record: long form; B01/B02 after the licence and demo findings;
  the Short; the Short's Option A lines.
- **`READ-ALOUD.md`**, **`READ-ALOUD-SHORT.md`:** the sheets Gate P was read from.
- **`BEATS-DRAFT.md`:** the structure, read-through logs, the 12/12 changes, audio, render and compile.
- **`PROOF-REVIEW.md` → `PROOF-REVIEW-4.md`:** beat sheet → stills → masters → the Short's Option A.
  The final verdict:
  - long: production gate PASS, **12/12**
  - Short: production gate PASS, **11/12**
  - every claim on screen when spoken, checked on frames pulled from the final files: 61 (long) and
    31 (Short)
  - Gate V: 0 BLOCKER / 0 MAJOR on both cuts
  - the only silences ≥ 1 s are the two clap-task holds in each cut
- **`experiment/`:** the five Whisper runs that turned the cold open from "slower" into "pauses", and
  the pre-registered final decision (`demo_final.json`).

## Rebuilding

`beat_sheet.json` (here and in `short/`) is the source of truth, generated by `build_beat_sheet.py` /
`short/build_short_sheet.py`. Measured Kokoro audio is the clock and is never hand-repaired. Run from
the working folder (`Week 26/topic-video/`); the scripts resolve the toolkit relative to it.

```
/opt/homebrew/bin/python3.12 make_ir.py         # the simulated cathedral (seeded), then:
/opt/homebrew/bin/python3.12 room_voice.py      # DEMO beats: Kokoro + IR, envelopes, Whisper check
python3 build_beat_sheet.py                     # narration + props; cues on the measured clock (cue_align.py)
/opt/homebrew/bin/python3.12 make_audio.py      # only after Gate P; overrides asserted; --dir short for the Short
python3 proof_check.py [short/beat_sheet.json]  # quotes/figures/sources on screen, statically
<toolkit>/remotion_scenes.py <reel> --only <beat> --force   # never while a sheet rebuild is running
/opt/homebrew/bin/python3.12 portrait_check.py <9:16 stills>   # Shorts zones, on pixels
python3 make_gate_f.py                          # SHOTLIST / PROMPTS / short FACTCHECK (GATE F)
/opt/homebrew/bin/python3.12 <toolkit>/compile.py <reel> --height 2160   # 3840 for the Short
python3 pacing_pass.py <reel> --hold 0.3        # reads each beat's hold_after_s; then normalise.py
python3 make_captions.py .  ;  python3 make_captions.py short
python3 assertion_frames.py <reel> <final.mp4> <out>   # PROOF: one frame per claim, on the final file
```

**Components.** `RoomVoice`, `HallTempo` and `AskAnswer` were written for this film in `brutalist.art`
(`runtime/remotion/src/scenes/`), local and uncommitted as in Weeks 24–25. All three are dual-aspect,
use absolute-second timing, have neutral defaults, and keep display text in props.
