# Use the Tool First.

Weekly progress report for the week of 2026-09-11. One subject: the Midjourney
series shipped. The STEM half of this week's submission is
[Why Your Track Gets Turned Down](../2026-09-11-why-your-track-gets-turned-down/).

| | |
|---|---|
| **Runtime** | 2:02 |
| **Format** | 16:9 and 9:16, 4K (3840×2160 / 2160×3840), 30 fps |
| **Voice** | Kokoro `af_bella` — local, free, no API |
| **Beats** | 6 · 3 purpose-built scenes · 1 reused library scene · 2 chassis · **no slates** |
| **Presenter** | Rohan Vijaykumar |
| **Channel** | @HumanitariansAI |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd · **not published** |

## Through-line

**The plan was wrong, and using the tool is what corrected it.** The series was
scoped from web research before access existed. Twenty-nine screenshots of the
real interface overturned five assumptions and revealed two whole surfaces the
plan had missed. That correction, not the six videos, is the reportable part of
the week.

## Every number measured

| Claim | Verified by |
|---|---|
| Six parts, all 3840×2160 | `ffprobe` on each master |
| **18:59** total runtime | sum of six probed durations = 1138.96s |
| Per-part runtimes | `ffprobe` — 3:20 / 3:16 / 3:02 / 3:23 / 2:59 / 2:56 |
| **29** captures | file count in `Midjourney Screenshots/` |
| **23** new components | `Mj*.tsx` count in the shared kit |
| **863** lines of UI spec | `wc -l MIDJOURNEY-UI-SPEC.md` |

`MIDJOURNEY-SERIES-PLAN.md` states both "23 captures" and "29 captures" in
different places. Disk says 29; the reel uses 29 and
[FACTCHECK.md](./FACTCHECK.md) records the discrepancy.

## Beat map

| Beat | Act | In | Dur | Component | What it shows |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 18.97s | `ClaudeComposerAsk` | "Hi, I'm Rohan, for Humanitarians AI" — the week in one line |
| B01 | SHIPPED | 0:18 | 22.72s | `HaiProgressSeriesGrid` | Six parts in a 3×2 grid, total counting to 18:59 |
| B02 | CORRECTION | 0:41 | 24.43s | `HaiProgressOverturned` | Five assumptions struck through, replaced one at a time |
| B03 | KIT | 1:06 | 23.55s | `HaiProgressKitGrid` | 23 component names as evidence, plus spec/capture counts |
| B04 | NEXT | 1:29 | 21.93s | `HaiProgressRoadmap` *(reused)* | Signup docs still open; both tools together next |
| B05 | OUTRO | 1:51 | 10.50s | `ClaudeTitleOutro` | "I'm Rohan Vijaykumar, for Humanitarians AI" |

Total 122.10s. Narration durations are ground truth.

## Library-first outcome

Three searches, three different results — recorded in full in
[PROMPTS.md](./PROMPTS.md):

| Need | Outcome |
|---|---|
| six-part series grid | `HaiProgressSeriesCards` is a real hit but collapses to 245px cards at n=6 → **new 3×2 variant built** |
| plan-vs-reality columns | `MedhavyTwoColumnCard` has the right props — **opened it**, wrong layout grammar (fixed 900px card, top-centre spark, no eyebrow). Extending it would change the medhavy channel's look → **purpose-built instead** |
| shipped/next roadmap | `HaiProgressRoadmap` + its 916 sibling → **reused outright, nothing written** |

## New components

| Component | Portrait sibling |
|---|---|
| `HaiProgressSeriesGrid` | `HaiProgressSeriesGrid916` |
| `HaiProgressOverturned` | `HaiProgressOverturned916` |
| `HaiProgressKitGrid` | `HaiProgressKitGrid916` |

## The vertical cut is re-rendered, not cropped

Built through `shorts.py` and THE ONDA CHECK. Portrait reflows rather than
shrinks: the 3×2 grid becomes 2×3, the side-by-side comparison stacks into
pairs, and the kit's left column becomes a full-width banner. See
[SHOTLIST.md](./SHOTLIST.md).

## What is in this folder

**Committed to GitHub** — text and QC sheets only:

```
beat_sheet.json     the reel: beats, narration, visuals, measured durations
README.md           this file
SOURCE-brief.md     what was asked for, and what it was built from
PROMPT.md           the brief and how each constraint was resolved
FEEDBACK.md         reviewer notes — empty until someone reviews it
BUILD-LOG.md        what actually happened
FACTCHECK.md        every claim, its source, its verdict
SOURCES.md          provenance and what was verified by execution
PEDAGOGY.md         narration sign-off — register, vocabulary, what was cut
SHOTLIST.md         beat-by-beat, and how each one reflows for portrait
PROMPTS.md          the design brief behind each visual
description.txt     YouTube description + chapter markers
qc-sheet-16x9.png   contact sheet — landscape visual QC record
qc-sheet-9x16.png   contact sheet — portrait visual QC record
.gitignore          enforces the media rule below
```

**Never committed** — these go to Google Drive via `./art drive`:

```
mp4/  finished cuts     media/  per-beat 4K renders
mp3/  narration         clips/  compile intermediates
short/  derived portrait reel
```

## Rebuilding it

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>
ART_CONCURRENCY=3 ART_REMOTION_SCALE=2 python3 runtime/scripts/remotion_scenes.py <reel>
python3 runtime/scripts/compile.py <reel> --height 2160

python3 runtime/scripts/shorts.py <reel> --no-endcard
ART_CONCURRENCY=3 ART_REMOTION_SCALE=2 python3 runtime/scripts/remotion_scenes.py <reel>/short
python3 runtime/scripts/compile.py <reel>/short --height 3840

./art drive <reel>
```

Audio first, always. The vertical is re-rendered, never cropped.
