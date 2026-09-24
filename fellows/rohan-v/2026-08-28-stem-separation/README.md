# Stem Separation: Estimation, Not Extraction

A non-technical explainer on how stem separation models work — what they
receive, what they produce, and when the output should not be trusted.
Waveform motion graphics show the mix collapse, the probability outputs,
and the bleed artifact directly on screen.

| | |
|---|---|
| **Runtime** | ~2:22 |
| **Format** | 16:9 and 9:16, 4K (3840×2160 / 2160×3840), 30 fps |
| **Voice** | Kokoro `af_bella` — local, free, no API |
| **Beats** | 7 · 3 purpose-built waveform scenes · 4 library components · **no slates** |
| **Presenter** | Rohan V. |
| **Channel** | @HumanitariansAI |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd · **not published** |

## What this video covers

Through-line: the model estimates, it does not recover.

| Beat | | |
|---|---|---|
| B00 | Cold open | "Hi, I'm Rohan, for Humanitarians AI" — the question the model is being asked |
| B01 | BLUF | 4 colored waveform tracks collapse into one mixed signal — what the model receives |
| B02 | Framework | Mixed waveform fans into 3 estimated stem outputs — probability, not recovery |
| B03 | Mechanics | The cake analogy — additive, irreversible, statistics-based |
| B04 | Limits | Vocal stem with ghost drum bleed — the estimation cost made visible |
| B05 | Apply | The trust test — three things to check before using a stem |
| B06 | Outro | "I'm Rohan V., for Humanitarians AI" — matches first video |

## What is in this folder

**Committed to GitHub** — text only, nothing over 25 MB:

```
beat_sheet.json     the reel itself: every beat, its narration, its visual,
                    its measured duration, and its build stamp
README.md           this file
SOURCE-brief.md     what was asked for, and what it was built from
PROMPT.md           the brief and how each constraint was resolved
FEEDBACK.md         reviewer notes — empty until someone reviews it
BUILD-LOG.md        what actually happened, including v1 vs v2 changes
FACTCHECK.md        every factual claim, its source, its verdict
SOURCES.md          provenance, and what was verified by execution
PEDAGOGY.md         narration sign-off — register, vocabulary, what was cut
SHOTLIST.md         beat-by-beat: component, lane, duration, what's on screen
PROMPTS.md          the prompt behind each visual + HAI channel standard
description.txt     YouTube description + chapter markers
.gitignore          enforces the media rule below
```

**Never committed** — these go to Google Drive instead:

```
mp4/     the finished cuts        media/   per-beat 4K renders
mp3/     narration, one per beat  _qc/     QC report + contact sheet
```

## New Remotion scenes in this reel

Three components built for this video and registered in the shared toolkit:

| Component | Folder | What it does |
|---|---|---|
| `StemSepMixCollapse` | `stem-separation-explainer` | 4 colored tracks → one combined waveform |
| `StemSepStemOutput` | `stem-separation-explainer` | Mixed waveform → 3 estimated stem outputs |
| `StemSepBleedViz` | `stem-separation-explainer` | Vocal stem + ghost bleed + comparison strip |

## HAI channel standard (all future videos)

- **Opener**: `ClaudeComposerAsk` — "Hi, I'm Rohan, for Humanitarians AI."
- **Outro**: `ClaudeTitleOutro` — `title` / `@HumanitariansAI` / `Rohan V.`
- Narration closer: "I'm Rohan V., for Humanitarians AI."

## Rebuilding it

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>
ART_CONCURRENCY=4 python3 runtime/scripts/remotion_scenes.py <reel>
python3 runtime/scripts/compile.py <reel> --height 2160
```

Audio first, always.

## Renders

The 4K masters are in Google Drive, not in git — renders go to Drive, source and build assets stay here.

[`2026-08-28/` on Drive](https://drive.google.com/drive/folders/1UBpIYX_NBcEpMebfTLbJYtmN7WYwZ3Kf) — `2026-08-28_stem_separation_16x9.mp4` and `2026-08-28_stem_separation_9x16.mp4`.
