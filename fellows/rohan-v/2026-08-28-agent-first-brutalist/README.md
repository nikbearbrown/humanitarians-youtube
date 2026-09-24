# Your Weekly Video, Handled.

The complete Humanitarians AI fellow workflow — from a machine with nothing
installed, to four files delivered to the two correct places.

| | |
|---|---|
| **Runtime** | 4 min 14 s |
| **Format** | 16:9, 4K (3840×2160), 30 fps |
| **Voice** | Kokoro `af_bella` — local, free, no API |
| **Beats** | 13 · all machine-rendered · **no slates** |
| **Presenter** | Rohan V. |
| **Channel** | @HumanitariansAI |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd · **not published** |

## What this video covers

Ten pipeline steps. Seven belong to the agent, three to the fellow — and none of
the three requires a command line.

| Beat | | |
|---|---|---|
| B00 | Cold open | Four files a week, no code required |
| B01 | Requirement | What's due every Friday, and the flexibility floor |
| B02 | Setup *(once)* | Claude desktop app — you approve, you don't type |
| B03 | Plan | One plain sentence becomes a beat sheet |
| B04 | Mechanism | The voice is generated first, and it is the clock |
| B05 | **Yours** | Watch the preview — the step Claude cannot do |
| B06 | Formats | 16:9 master, 9:16 derived automatically |
| B07 | Submit · code | Docs to GitHub, under 25 MB, never the media |
| B08 | Submit · access | Fork + PR or branch + PR — the agent picks |
| B09 | **Yours** | Upload the four videos to Drive, by hand |
| B10 | Recap | Seven automated, three yours |
| B11 | Your turn | A paste-ready prompt |
| B12 | Outro | Sign-off |

## What is in this folder

**Committed to GitHub** — text only, nothing over 25 MB:

```
beat_sheet.json     the reel itself: every beat, its narration, its visual,
                    its measured duration, and its build stamp
README.md           this file
SOURCE-brief.md     what was asked for, and what it was built from
PROMPT.md           the brief and how each constraint was resolved
FEEDBACK.md         reviewer notes — empty until someone reviews it
BUILD-LOG.md        what actually happened, including the defects found
FACTCHECK.md        every factual claim, its source, its verdict
SOURCES.md          provenance, and what was verified by execution
PEDAGOGY.md         narration sign-off — register, vocabulary, what was cut
SHOTLIST.md         beat-by-beat: component, lane, duration, what's on screen
PROMPTS.md          the prompt behind each visual (open slots: none)
description.txt     YouTube description + chapter markers
.gitignore          enforces the media rule below
```

**Never committed** — these go to Google Drive instead:

```
mp4/     the finished cuts        media/   per-beat 4K renders
mp3/     narration, one per beat  _qc/     QC report + contact sheet
```

The visual components live in the toolkit's shared scene library
(`runtime/remotion/src/scenes/HaiSubmit*.tsx`, registered in `Root.tsx` under
`hai-weekly-submission`) so the next fellow's reel can reuse them. `PROMPTS.md`
records the prompt behind each one.

## Rebuilding it

Everything here regenerates for $0.00:

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>        # audio is the clock
ART_CONCURRENCY=4 python3 runtime/scripts/remotion_scenes.py <reel>
python3 runtime/scripts/compile.py <reel> --height 2160
python3 runtime/qc/final_frame_check.py <reel>                 # then LOOK at the frames
```

Audio first, always. Measured narration durations are ground truth and every
visual conforms to them — never fix timing by hand; rewrite the line and
re-measure.

## The three links this video gives its viewer

| Purpose | Link |
|---|---|
| The toolkit | https://github.com/nikbearbrown/brutalist.art |
| Submit code + docs | https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows |
| Upload finished videos | https://drive.google.com/drive/folders/1yf3ZJ9NfDJvdDAiuPiWEwKDjdkQMEh0g |

## Open items

- **9:16 version not built.** The reel is 4:14, over the 3:00 Shorts cap, and
  none of the ten components has a portrait layout yet. `shorts.py` refuses to
  centre-cut Remotion beats because it chops text mid-word, so this needs ten
  real portrait layouts plus a decision on whether to cut for the cap.
