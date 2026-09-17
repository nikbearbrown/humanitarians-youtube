# BUILD-LOG — "16-bit or 24-bit: What Bit Depth Does"

What broke, what it cost, and what changed because of it. Kept because most of
these are repeat offenders.

## 1 — The plan was rebuilt twice before a frame was rendered

The first plan was ASK → BLUF → MECHANISM → COMPARISON → LIMIT → APPLY → OUTRO.
Rohan stopped it after seeing the cut:

> It starts out very abruptly. what is a person who knows nothing about audio
> going to understand? … Stop whatever you're doing now and get the basics
> right first. Revise the plans for both videos

The rewrite added BACKGROUND and ANALOGY beats. Then the rewrite over-corrected
into a reel with no mechanism in it, and:

> Okay. and dont make the video too high level either. it has to be a good
> balance. at the end of the day the viewer has to learn somthing

**Cost:** two full plan revisions, no wasted renders — because the plan was
approved before any beat was rendered. That is the only reason this was cheap.

## 2 — ffmpeg cannot measure 24-bit quantisation noise

The first measurement used `ffmpeg` + `volumedetect` and returned `-inf` for
24-bit, which looked like a spectacular result and was an artefact: ffmpeg's
filter graph is 32-bit float internally (a 24-bit mantissa), so a 24-bit round
trip is *lossless to ffmpeg*.

**Fix:** rewrite the measurement in float64 numpy — `measure_bitdepth.py`. It
produced −149.56 dBFS for 24-bit, a real number.

**Irony:** that number was then cut from the reel anyway, for being one
comparison too many. It lives in MEASUREMENTS.txt.

## 3 — No scene in this project had ever loaded a font

The biggest fidelity bug found this week, and it was silent. The house type is
Tiempos, which was never bundled, and **no scene loaded any font at all** — so
every reel before this one rendered in whatever the headless Chrome fell back
to: Georgia or Segoe UI.

**Fix:** `runtime/remotion/src/lib/haiType.ts` — `Source Serif 4` and `Inter`
via `@remotion/google-fonts`, exported as `HAI_TYPE`. Every new component pulls
from it.

It is also a **determinism** fix: `loadFont()` blocks the render until the face
is ready, so a beat can no longer race its own typography.

## 4 — `remotion-bits` has an undeclared dependency

Bundling failed with `Can't resolve 'culori'`. `remotion-bits@0.2.1` imports it
and does not declare it.

**Fix:** `npm i culori@4`.

## 5 — `@remotion/paths` was a version ahead of core

`4.0.490` against core `4.0.486`. Remotion's own warning says mismatched
versions cause "failed renders and unclear errors".

**Fix:** pinned to `4.0.486`. Pre-existing condition, not caused by this week.

## 6 — `HaiApplyCard` silently drops unknown props

B05 rendered the literal string **"Set in beat sheet."** The card's schema is
`eyebrow / title / lede / steps / sparkLine`; the beat sheet was passing
`heading` and `lines`, which zod accepted and the component ignored.

**Fix:** corrected both beat sheets. Worth remembering that a silently dropped
prop looks exactly like a component bug.

## 7 — Gate V failed the first clean master, and was right

**0 BLOCKER, 4 MAJOR** — every one `underfill`, every one at the 50% sample:

| beat | fill at 50% | floor |
|---|---|---|
| B01 `BitSoundToNumbers` | 39% | 55% |
| B02 `BitStaircase` | 31% | 55% |
| B03 `BitGapIsHiss` | **22%** | 55% |
| B04 `BitRoomUnderneath` | 48% | 55% |

The canvas-fill law measures the **bounding box of all ink** against the safe
area — not ink density. Each of those four beats had keyed its entire lower half
to a late cue, so at the beat's own midpoint the frame was genuinely half empty.
Not a gate artefact; a real defect a viewer would feel as dead air.

**The fix was not to move a cue.** Cues are measured spoken words and moving one
would desynchronise the reel. Instead every beat was split in two:

- **Shell** — card, panel, axis furniture, provenance footnote — arrives when the
  *section* is introduced.
- **Content** — the thing that teaches — still waits for the phrase that earns
  it.

| beat | what moved earlier | to which cue |
|---|---|---|
| B01 | the two question-card shells + their QUESTION n labels | `numbers` 0.401 |
| B02 | the plot panel + the ladder (it *is* the fine ruler's markings) | `marks` 0.213 |
| B03 | the music panel + the music waveform; then the comparison card shells | `often` 0.287, then 0.42 |
| B04 | the MEASURED provenance footnote | `sixteen` 0.333 |

Second run: **0 BLOCKER, 0 MAJOR.**

## 8 — Three defects the gate could not see

Gate V passed. Reading the contact sheet and three full-resolution mid-beat
frames found three more:

| where | defect | fix |
|---|---|---|
| B01 | the numbers panel was a full-height card carrying **one row of digits at 34% of its height** — a large empty box with text near the top | sized the strip to its contents (0.085 of frame height) and centred it on the chain's midline, so wave / microphone / numbers share one horizon |
| B02 | the honesty caption sat 0.106 below the plot while the prose it followed arrived at 0.92 — so for most of the beat it **floated alone in white space** | caption now hugs the plot it describes; the prose moved below it |
| B04 | the yardstick tick rails had been moved onto the shell in fix 7 and appeared as **four orphan dashes at the frame edge** with no labels attached | rails back on `anchor` with their labels; the MEASURED footnote already carries the bounding box |

The B04 one is the instructive case: a fix for a gate finding introduced a new
visual defect that the same gate could not detect. Passing a gate is not the
same as being right.

## 9 — `compile.py --review` was broken on Windows

The timecode burn-in passes a Windows font path straight into ffmpeg's
filterchain, where `C:\…` destroys the filter syntax. Escaping alone is not
enough — the value also has to be single-quoted.

```python
"'" + str(font).replace("\\", "/").replace(":", "\\:") + "'"
```

**Knock-on:** `make_qc_sheet()` runs *after* the review encode, so while the
encode failed the QC sheet could never be produced. That is why week-01 shipped
without one.

## 10 — cp1252 again, in five more scripts

Windows' default encoding corrupted non-ASCII characters in
`scene_search.py`, `build_scene_index.py`, `compile.py`, `beat_lint.py`,
`final_frame_check.py`, `static_scene_check.py`, `gate_shape.py` and
`shorts.py`.

**Fix:** explicit `encoding="utf-8"` on every `read_text` / `write_text` /
`open` (18 files swept), plus `os.environ.setdefault("PYTHONUTF8", "1")` before
spawning child gates.

**The one that mattered:** `shorts.py:246` read the parent beat sheet with a bare
`read_text()`, mangled it in memory, and wrote it back as *faithfully encoded
mojibake* — which is exactly the "weird accents above the letter a" Rohan
reported in the week-03 shorts. Fixed at source. Both week-04 short beat sheets
were byte-checked for `\xc3\x82\xc2\xb7` and friends: **clean**, with all 9
middots and 6 em-dashes intact.

## 11 — Gate V must be judged on the clean master

`./art run` (review cut) always fails Gate V with 14 `edge-bleed` blockers,
because the timecode burn-in sits outside title-safe by design. Gate V is
meaningful only on `./art final`.

## What this week added to the toolkit

| Addition | Why it exists |
|---|---|
| `lib/haiType.ts` | fonts were never loaded (§3) |
| `lib/cueKit.tsx` | one waveform, one hiss, one head block, one spark line, `exclusive()` and the spring constants — so eight new components do not each reinvent them |
| THE WORD CLOCK, used end to end | `align.py` → `words.json` → `cues.json` → `sync_cues.py` → `props.cues`. 30 cues, 30 resolved |
| "shell early, content on the word" | §7 — a design rule that came out of a gate finding |
| 8 new landscape components | 4 for this reel, 4 for its sibling |
| 8 new `916` portrait siblings | native portrait, never a crop |

## Ledger

| | |
|---|---|
| Plan revisions | 2 (both before any render) |
| Measurement rewrites | 1 (ffmpeg → numpy) |
| Gate V runs | 2 landscape, 1 portrait |
| Gate V findings | 4 MAJOR, all fixed → 0/0 |
| Defects found by eye that the gate missed | 3 |
| Beats re-rendered after QC | 5 landscape (of 7) |
| Toolkit bugs fixed | 6 |
| Paid API calls | **0** |
| Cost | **$0.00** |
