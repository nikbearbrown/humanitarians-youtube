# Week 27 work-video

*Minutes of the Meeting: What an AI Is Handed.* Tanmay Kulkarni, in for Humanitarians AI.
**Text and code only. The two masters (the long film and its Short) live in the shared Google Drive.**

## The contribution

**[nikbearbrown/mycroft#70](https://github.com/nikbearbrown/mycroft/pull/70), merged (commit `8665a9f`, CI `verify` passing).**
It closes three `[TODO: DEV]` steps of Mycroft's What-If Simulation Agent recipe and maps two of its nodes, in sample mode:
- provenance for the recipe (its nodes, its connections, its fixtures)
- data-shape validation, with the *Parse & Validate Input* node's own rules plus one stated addition (numeric fields must be finite)
- a Python port of the six steps before the AI (parse, three simulators, aggregate and score, build the AI briefing), checked against
  the original JavaScript on 23 requests, with a self-test of 10 deliberate breaks
- 25 invented sample requests with a SHA-256 manifest

`main` gained 43 added and 2 modified files, nothing removed. The recipe stays `DRAFT` (`todos_open: 5`); nothing calls the AI service
or the database. Every fact in the films is read from files merged into `main` @ `8665a9f` (`FACTCHECK.md`, W1 to W20; the Short's
`FACTCHECK-SHORT.md`). The contribution's own code lives in that repository and is not duplicated here.

## The angle

Weeks 25 and 26 were also Mycroft contributions: three pairs that must agree (porting, rounding), then four mornings with a dashboard
(hand-offs taken on trust). This film takes neither shape. Its subject is **what an AI is handed**: the workflow ends in a 470-word
briefing, written by six local steps, and the AI never sees the original request. Its structure is **the minutes of one meeting**
about one invented stock: a chair opens, three voices speak, they disagree, the chair weighs them 45, 35 and 20, and the minutes go to
the one party who was not in the room. It ends on a question: *who had a vote, and how much?* The audit against Weeks 15 to 26
(210 narration beats) and the framing rules are in `ANGLE.md`.

## The files

| | File | | |
|---|---|---|---|
| **Long** | `minutes-of-the-meeting.mp4` (Drive) | 3840×2160 · 30 fps · 3:54 (234.3 s) | −14.8 LUFS / −1.9 dBTP |
| **Short** | `minutes-of-the-meeting-short.mp4` (Drive) | 2160×3840 · 30 fps · 1:24 (84.5 s) | −14.6 LUFS / −1.5 dBTP |

Each film carries its captions (`.srt` and `.vtt`) and its YouTube title, description, chapters and tags (`*-youtube.md`) beside it.

**Structure:**
- **Long, "MINUTES OF ONE MEETING":** 12 beats. B01 opens on the last line of the briefing; B02 sets the question; B03 to B06 are the chair
  and the three voices; B07 is the disagreement and the weighing; B08 is the minutes; B09 is the turn, my own minute-taker; B10
  adjourns; B11 gives the viewer the task.
- **Short, *Who Fills the Blank?*:** its own script (`SCRIPT-SHORT.md`), one continuous scene: a blank in the AI's last line that three
  voices and a chair fill in, the minutes the AI actually gets, a plain account of what the full film shows, and the loop closed on the blank.

## Links

Add the temporary Drive links and, once live, the YouTube URLs.

| | Drive | YouTube |
|---|---|---|
| Long (16:9, 4K) | <!-- DRIVE_LINK_LONG --> *(to add)* | <!-- YOUTUBE_LINK_LONG --> *(to add)* |
| Short (9:16, 4K) | <!-- DRIVE_LINK_SHORT --> *(to add)* | <!-- YOUTUBE_LINK_SHORT --> *(to add)* |

**Placeholder in the Short's description:** `[FULL VIDEO LINK]`. Swap in the long's YouTube URL once it is live, and set the long as the
Short's related video in YouTube Studio.

## Uploading: three choices only you can make

1. **Altered or synthetic content.** The narration is a synthetic voice (Kokoro), introducing itself as Tanmay Kulkarni, and every
   company and number is invented. Both descriptions say so. Whether to also tick YouTube's "altered or synthetic content" box is your call.
2. **Thumbnail.** Pick a custom one. The long's B07 (the weights, the scale, the pieces and SELL on one slide) is the strongest frame;
   B01 (the last line of the briefing, highlighted) is the cleanest hook. For the Short, the frame where SELL fills the blank.
3. **Captions.** Upload each `.srt` as English captions, not YouTube's auto-captions; they keep "What-If" spelled as written, where the voice says "what if".

## The record

- **`FRICTIONAL.md`:** the dated process log. Drafted from the records; awaiting review.
- **`ANGLE.md`:** the approved angle, the uniqueness audit against every earlier work video, the rejected angles and why.
- **`SCRIPT.md`**, **`SCRIPT-SHORT.md`:** the signed scripts. **`READ-ALOUD.md`**, **`READ-ALOUD-SHORT.md`:** the sheets Gate P was read from.
- **`PEDAGOGY.md`:** the Gate P verdict log and the teaching-score trajectory.
- **`FACTCHECK.md`** (W1 to W20), **`FACTCHECK-SHORT.md`:** every claim with its evidence at `8665a9f`, and what is left out and why.
- **`PROOF-REVIEW.md`** (script, 10/12 then 12/12), **`PROOF-REVIEW-STILLS.md`** (12/12), **`PROOF-REVIEW-CUT.md`** (compiled cut: 12/12,
  production gate PASS), **`PROOF-REVIEW-SHORT.md`** (plan stage 9/12 then 12/12; compiled Short 12/12, Shorts gate 12/12). The cut reviews
  record what they found and fixed, including a slow-motion pace and transitions that lagged, both caught by ear and eye and not by the
  machine checks.
- **`beat_sheet.json`**, **`beat_sheet-short.json`:** the build's source of truth (measured clock).

## Rebuilding

`beat_sheet.json` is the source of truth, generated by `build_beat_sheet.py` (the Short's by `build_short_sheet.py`). Every figure on a
slate is read from the merged repository (`git show 8665a9f:<path>` in a local clone of Mycroft). Measured Kokoro audio is the clock and is
never hand-repaired. The scene code (the slates and the Short's one scene), the on-screen and figure checks and the gate scripts stay in the
working folder, as the scene code did for the earlier work videos; the scripts here need them and a local checkout of the toolkit.

```
build_beat_sheet.py --planning   # beat_sheet.json on the planning clock
make_audio.py                    # whole-beat Kokoro audio (python3.12); Whisper word times
build_motion.py --plan           # cues on the Whisper word clock; --render, --encode: the beat videos
compile_master.py                # master, captions, loudness (-14 LUFS two-pass)
build_beat_sheet.py              # again, on the measured clock
make_audio_short.py, compile_short.py, build_short_sheet.py   # the Short, from the folder that holds short/
```

Slates and scene are drawn in code (Pillow); no generated imagery, no stock, no third-party images; open-licence fonts only
(EB Garamond, Inter, PT Mono). Narration is a synthetic voice (Kokoro, run locally).
