# BUILD-LOG — "Unblocking the Team."

Built 2026-08-29 for the week-02 submission (dated 2026-09-04). What actually
happened, in order, including two toolkit bugs fixed along the way.

## 1 — Source gathering

Read Rohan's brief, then verified everything in it that carried a number rather
than trusting the planning document:

- `ffprobe` on all three Suno masters → 3840×2160, 236.55s / 188.94s / 209.21s
- Confirmed all three `.mp4` files exist on disk
- Read `lyrical-literacy/SERIES-PLAN.md` for part titles and the
  no-screen-recordings standard
- Confirmed `week-01/2026-08-28-agent-first-brutalist/` exists, so B01's claim
  that the setup was packaged as a video is checkable

**Finding: the plan document is stale.** `SERIES-PLAN.md` estimates Part 1 at
"~3:30" and Parts 2–3 at "~3–4 min". The built masters are 3:57 / 3:09 / 3:29.
The reel reports the probed values, not the estimates. Logged in FACTCHECK.md.

Searched for the signup documentation on disk — **none found**, consistent with
the brief calling it in-progress. B03 and B04 label it `IN PROGRESS` in the
graphic rather than the narration alone.

## 2 — Library-first gate

Per toolkit doctrine, ran `./art scenes` for all four visual needs before
authoring anything. All four returned genuine misses; the closest candidates and
why they failed are recorded in [PROMPTS.md](./PROMPTS.md).

**Toolkit bug #1 — `scene_search.py` crashed on Windows.** Every search died
with `UnicodeEncodeError: 'charmap' codec can't encode character '→'` at
line 175 — scene descriptions contain arrows and middots, and the Windows
console defaults to cp1252. Fixed by forcing UTF-8 on `sys.stdout`/`sys.stderr`
at import, with `errors="replace"` as a fallback. The library-first gate is
mandatory doctrine, so a crash here silently pushes an author toward inventing
components that already exist.

## 3 — Four components authored

Written to `runtime/remotion/src/scenes/`, registered in `Root.tsx` under a new
folder `hai-weekly-progress`:

| Component | Frames registered | Notes |
|---|---|---|
| `HaiProgressBlocker` | 690 | Break keyed to `durationInFrames × 0.46` |
| `HaiProgressSeriesCards` | 840 | Total counter frames 122–178 |
| `HaiProgressSignupChain` | 690 | Doc sheet at `max(120, dur × 0.42)` |
| `HaiProgressRoadmap` | 450 | Settles by frame 132, then holds |

Prefixed `HaiProgress*` rather than week-specific so next week's report reuses
them. B01 and B03 key their reveal off `durationInFrames` so a narration
re-record does not push the event off the end of the beat.

**Toolkit bug #2 — `build_scene_index.py` crashed on Windows.** `./art
scene-index` died with `UnicodeDecodeError: 'charmap' codec can't decode byte
0x81`. Four IO calls read and wrote without an explicit encoding: `Root.tsx`
read at line 43, component files read at line 69, `scenes.json` written at 341,
`SCENE-DOC-TODO.md` written at 361. All four now pass `encoding="utf-8"`.

Without this fix the four new components would never enter `scenes.json`, which
is the only way anyone finds them later — the components would exist and be
undiscoverable.

After the fix: `scenes.json — 628 renderable, 115 undocumented, 0 unresolved`.

Verified all four resolve:

```
HaiProgressBlocker       RENDERABLE  16:9
HaiProgressSeriesCards   RENDERABLE  16:9
HaiProgressSignupChain   RENDERABLE  16:9
HaiProgressRoadmap       RENDERABLE  16:9
```

## 4 — Beat sheet

Six beats. Narration written to a per-beat word budget derived from `af_bella`'s
measured rate (~2.85 words/sec) to land the 2:00 target on the first pass rather
than by trimming afterwards.

## 5 — Audio (the master clock)

```
beat-B00.mp3  19.35s
beat-B01.mp3  24.11s
beat-B02.mp3  30.27s
beat-B03.mp3  22.68s
beat-B04.mp3  12.63s
beat-B05.mp3  10.71s
```

Total **119.75s = 1:59**, a quarter-second under the 2:00 brief. Cost $0.00 —
Kokoro runs locally. The word budget held on the first pass; B00 and B05 were
re-recorded later for the pronunciation fix in §10 below.

## 6 — Scene render

`ART_CONCURRENCY=3 ART_REMOTION_SCALE=2` for 4K. Six beats rendered to
`media/B0*.mp4` at 3840×2160.

## 7 — Compile, and two more Windows bugs

**Toolkit bug #3 — `compile.py` crashed printing its own progress.** Same
cp1252 root cause as #1: `[art] compiled B01 VIDEO 24.1s ← B01.mp4` contains a
`←`, and the print died after every beat had already been conformed. Fixed with
the same stdout/stderr UTF-8 reconfigure.

**Toolkit bug #4 — `--review` was completely broken on Windows.** With #3 out
of the way, the review compile failed inside ffmpeg:

```
No option name near '/Rohan/Claude/HAI/.../EBGaramond-Regular.ttf:text=...'
Error parsing filterchain '[v5]drawtext=fontfile=D:\...'
```

The running-timecode overlay passes a raw Windows font path into
`-filter_complex`. ffmpeg's filter parser treats `\` as an escape and splits
options on `:`, so `D:\Rohan\...` destroys the filterchain. Tested two
candidate fixes against ffmpeg directly:

| Attempt | Result |
|---|---|
| Forward slashes + escaped drive colon (`D\:/Rohan/...`) | **still fails** — the colon still splits the option |
| Same, but the value single-quoted (`'D\:/Rohan/...'`) | **works** |

Escaping alone is not sufficient; the quotes are what stop the option split.
Fixed at `compile.py:621`.

This mattered beyond convenience: `make_qc_sheet()` runs *after* the review
encode, so a failed review pass means **no `qc-sheet.png` is ever produced**.
That is why the two week-01 reels shipped without one. The mandatory visual QC
gate was silently unreachable on this platform.

## 8 — Visual QC, and two defects it caught

Ran the review pass, read `qc-sheet.png`, then pulled full-resolution frames of
the settled state of each new scene. Two real defects, both found by looking
rather than by probing:

**QC finding #1 — B01 emptied its own left half.** The first cut of
`HaiProgressBlocker` migrated the three work chips from left to right once the
wall parted. The settled frame therefore had a populated right column, an empty
left column under a live "WHAT THEY FINISHED" heading, and a bridge line
dangling from nothing. It read as broken, not resolved.

Redesigned: the left column now **stays populated for the whole beat** — the
team's finished work never stopped being true — and the right column holds
dashed placeholder rows reading `waiting`, which fill in staggered as solid
cards reading `received`. Both ends of the bridge now terminate on real content
at every frame.

**QC finding #2 — the total read 10:34, the docs said 10:35.** `fmt()` in
`HaiProgressSeriesCards` truncated: 634.70s → `floor(34.7)` → `10:34`. B04's
card and FACTCHECK.md both said 10:35. Changed to round the total to the
nearest second before splitting, so it now reads 10:35 and the reel is
internally consistent.

**Toolkit bug #5 — zod defaults are not render defaults.** Re-rendering B01
after the redesign failed with `Cannot read properties of undefined (reading
'length')`. The new `items` prop had a `z.array(...).default([...])` in the
schema, but the render path passes the beat's props as JSON and Remotion merges
them against the `<Composition>` `defaultProps` — not against the zod schema.
A prop with only a zod default arrives `undefined`. Added `items`, `leftHead`
and `rightHead` to both `Root.tsx` `defaultProps` and the beat sheet, matching
how `HaiProgressSeriesCards` already carries `parts` in both places.

## 9 — Final compile

Clean master via `compile.py --height 2160` (no beat markers, no timecode),
renamed to convention. The 9:16 cut is derived from that same master by
letterbox onto a 2160×3840 cream field — no beat re-rendered, no crop, so
nothing in the title-safe area is lost. Audio forced to mp3 on the vertical cut.

Verified both outputs by probe **and** by frame:

| File | Dimensions | Duration | Audio |
|---|---|---|---|
| `..._16x9.mp4` | 3840×2160 | 119.75s | aac |
| `..._9x16.mp4` | 2160×3840 | 119.77s | mp3 |

The 9:16 frame was pulled and inspected: letterbox field matches `#FAF9F5`,
nothing cropped, total reads 10:35.

## 10 — Reviewer fix: name pronunciation

Rohan flagged that Kokoro mispronounced his name in the opener and the sign-off.
The standing rule — spell it phonetically in `narration_text` so `af_bella`
hits it — had been recorded against the Suno tutorial series and was not
carried over to this reel. That was a filing error, not a new requirement.

| Beat | Was | Now |
|---|---|---|
| B00 | "Hi, I'm Rohan, …" | "Hi, I'm Row-Haan, …" |
| B05 | "I'm Rohan Vijaykumar, …" | "I'm Row-Haan VeeJayKooMaar, …" |

The phonetic spelling is confined to `narration_text`. Every on-screen string
still reads `Rohan Vijaykumar` — `ClaudeTitleOutro.subline`,
`ClaudeComposerAsk.greeting`, `metadata.presenter`, and all docs. A note in
`metadata.note` now states the split so a future build cannot collapse it.

Because narration is the master clock, the fix cascaded:

1. Regenerated all six mp3s — B00 19.20 → **19.35s**, B05 10.18 → **10.71s**,
   the other four byte-identical
2. Re-rendered B00 and B05 only, to extend their media to the new durations
3. Recompiled the review cut, regenerated `qc-sheet.png`
4. Recompiled the clean master, re-derived the 9:16
5. Updated the durations and the outro chapter marker (01:48 → **01:49**) in
   README, SHOTLIST, PEDAGOGY, SOURCES and description.txt

**Claude cannot hear audio**, so the corrected clips were cut to mp3 and sent to
Rohan for confirmation rather than being signed off as verified. Total moved
from 119.07s to 119.75s, still inside the 2:00 brief.

## 11 — Reviewer fix: the 9:16 was a letterbox, not a vertical

Rohan rejected the vertical cut: "it looks like the 16:9 master is just being
squeezed... everything in the current 9:16 video looks small and compressed and
hard to read. The contents should adapt to the new aspect ratio instead." He was
right, and he was right that the repo already says so.

### What was wrong

The first vertical cut was produced by scaling the 3840×2160 master to 2160 wide
and padding to 2160×3840 on a cream field. The content therefore occupied a
~1215px band in the middle of a 3840px-tall frame — roughly 32% of the canvas —
with landscape-scaled type. On a phone it is unreadable.

### The actual doctrine

`runtime/scripts/shorts.py` implements **THE ONDA CHECK**: for every Remotion
beat it looks up a `<Pattern>916` composition in `Root.tsx` and rewires the
short's beat sheet to it. The script's own words: *"portrait re-render on
short/, never a crop."* Around 105 `*916` compositions already exist. Crops are
reserved for captured media that has no code representation.

### Toolkit bug #6 — the ONDA CHECK was silently disabled on Windows

This is why the wrong method got used, and it is the most serious bug found in
this build:

```python
def root_tsx_text():
    p = ... / "Root.tsx"
    try:
        return p.read_text()      # cp1252 on Windows → UnicodeDecodeError
    except Exception:
        return ""                 # swallowed → registry looks empty
```

`portrait_pattern()` then tests `f'id="{cand}"' in tsx` against an empty string,
so **every** portrait composition reports as missing — including
`ClaudeComposerAsk916` and `ClaudeTitleOutro916`, which have been in the library
all along. The script printed six confident "no such composition — add one, or
drop a pantry crop" warnings, and the crop fallback looked like the sanctioned
path. A bare `except Exception: return ""` turned an encoding error into a
factually wrong answer about the library's contents.

Fixed: explicit `encoding="utf-8"`, and the handler narrowed to `OSError` with a
loud warning so a genuinely unreadable `Root.tsx` can never again masquerade as
an empty registry. `shorts.py` also needed the same stdout UTF-8 reconfigure as
bugs #1–#3.

With it fixed, all six beats rewire correctly on the first run.

### Four portrait siblings authored

Each re-exports the landscape schema (`export const fooBar916Schema =
fooBarSchema`) so props are identical and the beat sheet carries no
format-specific content — standing rule #4.

| Component | Reflow — rotate the logic, not shrink the pixels |
|---|---|
| `HaiProgressBlocker916` | Left→wall→right becomes top→wall→bottom. The wall is a full-width band that parts sideways; the bridge descends |
| `HaiProgressSeriesCards916` | Three side-by-side cards become a vertical stack, each full width with badge/name/skill left and runtime/4K right |
| `HaiProgressSignupChain916` | Horizontal chain becomes a vertical stack, the connector running through the hue dots as a step sequence |
| `HaiProgressRoadmap916` | Horizontal spine becomes a vertical spine down the left gutter; top-to-bottom is forward in time |

**Portrait safe area.** Content is confined to y 230–1440 of 1920 — the top 12%
and bottom 25% are reserved for platform UI. Nothing is centred in the full
frame height. Every font size derives from `height`.

### Visual QC on the portrait cut — two more defects

| Finding | Fix |
|---|---|
| B02's two-line footnote overlapped the spark line — the spark was pinned to a fixed `height * 0.706` while the footnote's height varies | Rebudgeted the column (cards 229→210px) and placed the spark relative to `FOOT_TOP` instead of a fixed fraction |
| B01's descending bridge bar ran straight through its own label | Gave the label a `CLAUDE.PAGE` background chip so the bar reads as a labelled connector |

Confirmed by probe that the portrait beats are natively **2160×3840**, not
upscaled: each was rendered from a 1080×1920 composition at
`ART_REMOTION_SCALE=2`.

## Outputs

```
2026-09-04_unblocking_the_team_16x9.mp4   3840×2160
2026-09-04_unblocking_the_team_9x16.mp4   2160×3840
```

Both stay local and go to Google Drive. Only the text files and `qc-sheet.png`
are committed to GitHub, per the media rule in `.gitignore`.

## Toolkit changes made in this build

Both fixes live in `RohanClaudeHAIbrutalist.art` and benefit every future reel
built on Windows:

| File | Change | Why it matters |
|---|---|---|
| `runtime/scripts/scene_search.py` | Force UTF-8 on stdout/stderr at import | Library-first search crashed on any description containing `→` |
| `runtime/scripts/build_scene_index.py` | Explicit `encoding="utf-8"` on 4 read/write calls | Without it new components never enter `scenes.json` and are undiscoverable |
| `runtime/scripts/compile.py` | Force UTF-8 on stdout/stderr at import | Compile died printing its own `←` progress lines |
| `runtime/scripts/compile.py:621` | Quote + escape the drawtext font path | `--review` was unusable on Windows, so `qc-sheet.png` could never be generated |
| `runtime/scripts/shorts.py` | Force UTF-8 on stdout/stderr at import | Scaffolding died printing its ONDA CHECK arrows |
| `runtime/scripts/shorts.py` | `read_text(encoding="utf-8")`; narrow the swallowing `except Exception` to `OSError` + warn | **The ONDA CHECK reported every 916 composition as missing, making a letterboxed crop look like the sanctioned path** |
| `runtime/remotion/src/Root.tsx` | New `hai-weekly-progress` folder, 8 compositions (4 landscape + 4 portrait) | — |
| `runtime/remotion/src/scenes/HaiProgress*.tsx` | 4 new components | — |
| `runtime/remotion/src/scenes/HaiProgress*916.tsx` | 4 new portrait siblings | — |

Bugs #1, #2 and #3 share one root cause, the same one hit during the week-01
builds: Windows cp1252 is the default encoding and the toolkit's text is UTF-8.
Any `read_text()` / `write_text()` / console print of non-ASCII fails until an
encoding is passed explicitly.

Bug #4 is separate and more consequential — it silently disabled the mandatory
visual QC gate on Windows. Both prior reels were signed off without the contact
sheet the framework expects, because the command that produces it could not
complete. It works now, and this reel is the first on this machine to ship with
a real `qc-sheet.png`.

Bug #5 is a Remotion contract detail worth remembering: **a prop that exists
only as a zod default will arrive `undefined` at render time.** Anything a
component indexes into must be in `defaultProps`.
