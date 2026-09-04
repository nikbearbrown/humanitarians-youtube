# Unblocking the Team.

Weekly progress report for the week of 2026-09-04. Not an explainer — this is
the project-progress half of the fellow's weekly submission. Four purpose-built
motion-graphics scenes carry the report: the blocker that got cleared, the
training series that shipped, the signup path being written down, and what is
committed next.

| | |
|---|---|
| **Runtime** | 1:59 |
| **Format** | 16:9 and 9:16, 4K (3840×2160 / 2160×3840), 30 fps |
| **Voice** | Kokoro `af_bella` — local, free, no API |
| **Beats** | 6 · 4 purpose-built scenes · 2 chassis components · **no slates** |
| **Presenter** | Rohan Vijaykumar |
| **Channel** | @HumanitariansAI |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd · **not published** |

## Through-line

**Every blocker hit this week became a reusable asset.** The GitHub wall became
a video. The Suno learning curve became a three-part series. The signup maze is
becoming written documentation. That is what makes this a progress report rather
than a list of tasks.

## Beat map

| Beat | Act | Dur | Component | What it reports |
|---|---|---|---|---|
| B00 | ASK | 19.35s | `ClaudeComposerAsk` | "Hi, I'm Rohan, for Humanitarians AI." Shipped training material, not a research result |
| B01 | BLOCKER | 24.11s | `HaiProgressBlocker` | Marketing team finished work but could not reach GitHub; workshop + walkthrough video cleared it |
| B02 | SHIPPED | 30.27s | `HaiProgressSeriesCards` | Suno series, 3 parts, 10:35 of 4K training material |
| B03 | IN FLIGHT | 22.68s | `HaiProgressSignupChain` | Four accounts before a fellow makes anything; guide being written |
| B04 | NEXT | 12.63s | `HaiProgressRoadmap` | Midjourney series, end of next week |
| B05 | OUTRO | 10.71s | `ClaudeTitleOutro` | "I'm Rohan Vijaykumar, for Humanitarians AI." |

Total 119.75s. Narration durations are ground truth — every visual is cut to fit
the voice, never the reverse.

The presenter's name is spelled phonetically in `narration_text` only
(`Row-Haan VeeJayKooMaar`) so Kokoro pronounces it correctly. Every on-screen
string keeps the correct spelling.

## New Remotion scenes in this reel

Four components built for this reel and registered in the shared toolkit under
folder `hai-weekly-progress`. All four were genuine library misses, confirmed
with `./art scenes` before authoring. They are prefixed `HaiProgress*` rather
than week-specific so future weekly reports reuse them instead of rebuilding.

| Component | What it does |
|---|---|
| `HaiProgressBlocker` | Finished work stacks left, a wall blocks it, the wall parts and a bridge carries it across |
| `HaiProgressSeriesCards` | One card per shipped part — waveform, runtime, 4K badge — over a counting total bar |
| `HaiProgressSignupChain` | Four tool cards in brand hues, linked, with a documentation sheet sliding in beneath |
| `HaiProgressRoadmap` | Timeline with a NOW pin: solid cards shipped, dashed cards committed |

Plus a native portrait sibling for each, registered at 1080×1920 and re-exporting
the landscape schema so props are identical:

`HaiProgressBlocker916` · `HaiProgressSeriesCards916` ·
`HaiProgressSignupChain916` · `HaiProgressRoadmap916`

## The vertical cut is re-rendered, not cropped

The 9:16 lives in `short/`, built by `shorts.py` via the **ONDA CHECK**: each
beat's pattern is rewired to its `916` sibling and re-rendered portrait.
Letterboxing or centre-cutting the landscape master is not the method — see
[SHOTLIST.md](./SHOTLIST.md) for how each beat reflows and the portrait safe
area it respects.

## HAI channel standard

Held identical to the two week-01 reels:

- **Opener**: `ClaudeComposerAsk` — narration opens "Hi, I'm Rohan, for Humanitarians AI."
- **Outro**: `ClaudeTitleOutro` — `title` / `@HumanitariansAI` / `Rohan Vijaykumar`
- Narration closes "I'm Rohan Vijaykumar, for Humanitarians AI."

## What is in this folder

**Committed to GitHub** — text only, nothing over 25 MB:

```
beat_sheet.json     the reel itself: every beat, its narration, its visual,
                    its measured duration, and its build stamp
README.md           this file
SOURCE-brief.md     what was asked for, and what it was built from
PROMPT.md           the brief and how each constraint was resolved
FEEDBACK.md         reviewer notes — empty until someone reviews it
BUILD-LOG.md        what actually happened, including the toolkit bugs fixed
FACTCHECK.md        every factual claim, its source, its verdict
SOURCES.md          provenance, and what was verified by execution
PEDAGOGY.md         narration sign-off — register, vocabulary, what was cut
SHOTLIST.md         beat-by-beat: component, lane, duration, what's on screen
PROMPTS.md          the prompt behind each visual + HAI channel standard
description.txt     YouTube description + chapter markers
qc-sheet-16x9.png   contact sheet of the landscape cut — visual QC record
qc-sheet-9x16.png   contact sheet of the portrait cut — visual QC record
.gitignore          enforces the media rule below
```

**Never committed** — these go to Google Drive instead:

```
mp4/     the finished cuts        media/   per-beat 4K renders
mp3/     narration, one per beat  clips/   compile intermediates
short/   derived portrait reel    _qc/     QC frames + report
```

`short/` is a derived scaffold — regenerate it with
`python3 runtime/scripts/shorts.py <reel> --no-endcard`. Its QC sheet is
promoted to `qc-sheet-9x16.png` and committed.

## Rebuilding it

```bash
# 1 — audio is the master clock
python3 runtime/scripts/generate_audio_kokoro.py <reel>

# 2 — landscape scenes at 4K
ART_CONCURRENCY=3 ART_REMOTION_SCALE=2 python3 runtime/scripts/remotion_scenes.py <reel>

# 3 — 4K master (add --review for the QC contact sheet)
python3 runtime/scripts/compile.py <reel> --height 2160

# 4 — native portrait cut (ONDA CHECK rewires each beat to its 916 sibling)
python3 runtime/scripts/shorts.py <reel> --no-endcard
ART_CONCURRENCY=3 ART_REMOTION_SCALE=2 python3 runtime/scripts/remotion_scenes.py <reel>/short
python3 runtime/scripts/compile.py <reel>/short --height 3840

# 5 — deliver: docs to GitHub, videos to Drive
./art drive <reel>
```

Audio first, always. The vertical is re-rendered, never cropped.

## Delivery

Two destinations, and they never mix:

| What | Where |
|---|---|
| Docs + QC sheets (<25 MB) | GitHub — `fellows/rohan-v/2026-09-04-unblocking-the-team/` |
| `*_16x9.mp4`, `*_9x16.mp4` | Google Drive — dated folder `2026-09-04/`, via `./art drive` |

`./art drive <reel>` derives the dated subfolder from the reel name and uploads
only the two named deliverables — review cuts, per-beat media, `clips/` and
`short/` are excluded so working files cannot reach the shared folder. Verify
with `rclone check`.
