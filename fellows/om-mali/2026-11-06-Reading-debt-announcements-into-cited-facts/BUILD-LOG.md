# BUILD-LOG — reading-debt-announcements-into-cited-facts

AI Debt Tracker, week 4. `brutalist.art` · skill `ai-explainer` · channel `claude-hai`.
Free and local end to end — Kokoro TTS, Remotion, ffmpeg. **`$0.00`, no API key.**

The author's own `README.md` and `FRICTIONAL.md` were already in this folder and are **not
touched by this build**. The figure→beat map that lives in a README in some earlier weeks is
in §2 below instead.

---

## 1. What the source gave, and what was built from it

| Source | Became |
|---|---|
| `narration_script.md` — 7 sections (5 body), 371 words, 2:30–2:40 target | 12 beats, 698 words |
| `pantry/adt-w4-grounding.svg` | B02 `W4Copy` (the Alphabet example) + B05 `W4Refused` (the tally) |
| `pantry/adt-w4-reader.svg` | B03 `W4Bakeoff` + B04 `W4Cite` |
| `pantry/adt-w4-triage.svg` | B06 `W4Triage` |
| `pantry/adt-w4-holdout.svg` | B07 `W4Key` |
| the script's Notes + `FRICTIONAL.md` | B01 `W4Pipeline` + B08 `W4Limits` |

The four figures were moved out of the folder root into `pantry/` so nothing in the build
path can slot one as media (REBUILD LAW). Every body beat is a native Remotion scene.

**Numbers were not read off the figures by eye.** Each bar's geometry in the SVGs was
recomputed as a ratio and had to agree with its printed fraction before the value entered
`figdata.json`:

```
reader B1 bar        236.2/280                 = 0.8436 = 135/160  ✓
reader event bar     263.2/280                 = 0.9400 = 157/167  ✓
reader B2 bar        280.0/280                 = 1.0    = 160/160  ✓
grounding scale      250.2/227 = 1.1023 px/copy; 3 -> 3.3, 24 -> 26.5 ✓
triage fresh bar     266.7/300                 = 0.8890 = 8/9      ✓
triage pass line     x=485 -> (485-200)/300    = 0.95             ✓
holdout fresh bar    34/170                    = 0.2    = 1/5      ✓
```

## 2. Figure → beat map

| Beat | Act | Scene (`ReadingIntoCitedFacts.tsx`) | Source | What it argues |
|---|---|---|---|---|
| B00 | Cold open | `ClaudeComposerAsk` | — | *Read it into facts; the model never types a number* — lands ANSWERED, carrying its own bad news |
| B01 | The reader | `W4Pipeline` | script 0:15 | The model is bracketed by code on both sides |
| B02 | The copy check | `W4Copy` | `adt-w4-grounding` (top) | It rewrote the currency sign while claiming to copy |
| B03 | The result | `W4Bakeoff` | `adt-w4-reader` | It passed its check; the third bar is the honest one |
| B04 | What pointing buys | `W4Cite` | script notes | The same number twice, and only one can be checked |
| B05 | What was refused | `W4Refused` | `adt-w4-grounding` (bars) | 24 refusals, 8 of them real |
| B06 | Triage, fresh | `W4Triage` | `adt-w4-triage` | A check the project set itself, and failed |
| B07 | The answer key | `W4Key` | `adt-w4-holdout` | One of five, and four defects with names on them |
| B08 | The limits | `W4Limits` | `FRICTIONAL.md` | Every number above, and nobody has checked any of it |
| B09 | Verdict | `ClaudeVerdictArtifact` | — | Five findings, two of them failures, and they are not last |
| B10 | Handoff | `ClaudeComposerAsk` | — | Run the dumb baseline before you build the clever thing |
| B11 | Outro | `ClaudeTitleOutro` | — | Title restate |

## 3. Structural decisions

Five script body sections → eight body beats, with four changes, all listed in `PEDAGOGY.md`
for individual sign-off:

1. **0:15 split into B01 and B02.** The section describes a mechanism; the script then shows
   the case that proves the mechanism matters 65 seconds later, at 1:20. Held until after the
   result, the Alphabet example reads as an excuse for the result.
2. **0:45 split into B03 and B04.** It carries two arguments — *here is the comparison* and
   *here is why the comparison does not mean what you would assume*. B04 exists to draw the
   same value twice, cited and uncited, because that is the week's actual product.
3. **1:20's tally became B05.** One refusal is an anecdote; 24 of 254 is the shape.
4. **The closing on-camera section became B08**, a limits beat, carrying the gate record.

No Manim beats, so GATE B never fires. No slates.

## 4. Assertions carried in `build_beat_sheet.py`

Four of these hold *arguments*, not arithmetic:

- **FRAMING** — `B2_SHARE > READER_SHARE`. The week's check, fixed in week 1, was to beat
  B1's regex rules. The reader did. The baseline nobody planned to take seriously — one model
  call typing every value — read more fields right than the reader. The whole reel is built on
  that gap. If the reader ever overtook B2, the build fails rather than let the episode become
  a victory lap.
- **SECOND** — `fresh triage share < 0.95 ≤ last week's share`. This check **failed**, and
  the reel says so in the cold open, in B06 and in the verdict. A reel announcing a failure
  its arithmetic does not support would be lying in the other direction.
- **THIRD** — `reader.extra > b2.extra > b1.extra`. The reader invents the most instruments
  of the three. 94% without 29 beside it is a flattering number.
- **FOURTH** — `8 + 16 == 24` and `227 + 3 + 24 == 254`. The refusal tally closes both ways.

Plus `reader.of != b1.of` (the three bars do **not** share a denominator), `62 + 4 == 66` with
62 more than ten times 4 (mostly easy documents), `1 of 5 < 3 of 3` on the answer key, four
defects in four **distinct** companies, `51 of 51` and `19 of 19` on the machine check, and —
because B02 is one character wide — that the `€` really is in the passage and the `$` really
is in the copy.

Three claims are **not** measured in `figdata.json` and are named constants, each attributed
on the frame that uses it: `GATE_RECORD` (B00/B08/B09), `LABELLER` (B04/B08), `CHECK_ORIGIN`
(B03/B08).

**One thing was removed rather than drawn.** The first draft of `figdata.json` gave the three
open reader defects ids P47–P49. `FRICTIONAL.md` gives ids for P41–P46 and none for these, so
the ids were invented. They were deleted, the field now carries a note saying the source gives
none, and FACTCHECK row 25 records it.

## 5. Toolkit changes

| File | Change |
|---|---|
| `runtime/remotion/src/ReadingIntoCitedFacts.tsx` | NEW — the eight reel-local scenes |
| `runtime/remotion/src/Root.tsx` | one `<Folder>`, each scene registered twice (1920×1080 and 1080×1920 under `<pattern>916`) |

`ReadingIntoCitedFacts.tsx` imports nothing from `AiDebtTracker.tsx`,
`GroundingTheDebtTracker.tsx`, `BuildingTheAnswerKey.tsx`, `BuildingTheTriage.tsx` or the week
1–11 reel files, by series convention: every earlier signed master stays re-renderable
byte-identically. Its chassis is a copy of week 3's, which arrives with week 3's portrait
values already raised and one new shared helper:

```tsx
/** Highlight — renders `text`, with the first occurrence of `mark` wrapped in the accent. */
```

It exists because B02's claim is one character wide, and the build asserts the character is
there — a `mark` that stops matching would leave a clean-looking frame with no argument on it.

`W4Bakeoff` and `W4Triage` both compute a `BESIDE` constant per orientation and subtract it
from the track width. That is week 3's B04 blocker written into the chassis rather than
rediscovered: in landscape the label column sits beside the track and pays for the value
columns; in portrait it stacks above and pays for nothing.

Nothing else in the toolkit was touched for this episode, and nothing outside this folder in
the fellow tree was touched at all.

## 6. Timing

```
12 beats · 8 body at 54–71 words (band 45–72) · 698 words
narration 202.12s (3:22.1), measured — the mp3 durations are the master clock
```

Both cuts use the same mp3s; `make_vertical.py` copies them rather than regenerating, so no
number can differ between the two masters.

## 7. GATE P

`PEDAGOGY.md` was written PENDING and the build stopped there. The audio gate was confirmed
refusing the unsigned reel before anything was generated:

```
[kokoro] GATE P: PEDAGOGY.md needs a signed VERDICT: PASS line (--no-gate to override)
exit=1
```

`--no-gate` was not used; it is blocked by the permission classifier, and routing around a
quality gate is not a build step.

This file deliberately never spells the signed-verdict phrase outside a quotation of the
gate's own error text, and `PEDAGOGY.md` never spells it at all except as the signature — in
week 1 a placeholder that quoted the phrase was itself enough to open the gate. The gate now
matches a verdict *line*, not a substring
(`runtime/scripts/generate_audio_kokoro.py`).

## 8. Portrait pass

**No rescale pass was needed on the body beats.** That is a first for this series, and it is
not luck: the chassis arrived with week 3's portrait values already raised, and `W4Bakeoff`
and `W4Triage` were written with a per-orientation `BESIDE` constant from the start —

```tsx
const BESIDE = f(330 + 24 + 112 + 150 + 28 + 150 + 60, 108 + 146 + 150 + 28 + 60);
const BAR_W  = Math.min(SAFE.w - BESIDE, f(700, 470));
```

— which is week 3's B04 blocker (every figure clipped to its first two digits in 9:16)
written into the component instead of rediscovered in QC.

Portrait did fail GATE V, but on the **bookends**, not the body:

| Beat | What portrait did | Change |
|---|---|---|
| B00, B10 `ClaudeComposerAsk916` | **GATE V BLOCKER ×4, `edge-bleed`.** The segment title wrapped to three lines and line 2 — "Announcements into Cited" — ran to the frame edge, past title-safe. | The title block in `scenes/ClaudeComposerAsk.tsx` sets `left: PAD_X` and **no right bound**, so the box runs to the viewport and wraps there. The running-text block twenty lines below it already sets both. Added `right: PAD_X`. |

That fix is in a **shared proven-core component**, so it was checked against the series
convention that every earlier signed master stays re-renderable byte-identically. The bound
is `width - 2*PAD_X` = 908px in portrait; the longest wrapped title line in the series so far
is week 3's "Timeline, Triage and" at ≈764px, and every landscape title is a single line far
inside 1613px. No earlier reel has a line that the new bound would re-wrap, so none of them
renders differently — and none was re-rendered, because sibling week folders are not this
build's to touch. Week 4's own bookends were re-rendered in **both** orientations so that one
component version is behind every frame shipped here.

## 8a. What reading the frames caught that no gate did

Four defects in the landscape cut, all invisible to GATE V:

1. **B06 drew an accent rule with nothing under it.** `FootNote` rendered its divider even
   for an empty string, and B06 passes `note: ""`. A rule where a rule is allowed to be is
   not something a frame check can object to. `FootNote` now returns null on empty text.
2. **B03's "EXTRA" column header sat over nothing.** It was justified to the right edge of
   the safe area while the extras column ends wherever the row ends — about 90px apart. The
   header row now mirrors the data row's structure instead of guessing an offset.
3. **B04's left-hand card asserted something the data does not log.** It shows B2 reporting
   Alphabet's €1,500,000,000 correctly. That follows from B2 reading 160 of 160, but it is an
   inference, not a transcript, and the frame now says so: *"B2 read 160 of 160, so this is a
   value it got right too."*
4. **B08 overran its column** — the last next-step collided with the Source line, exactly the
   risk `CHECKS-REPORT.md` listed at #6. Every size in the beat came down a notch and two
   limits lost words; no claim was cut.

None of these is a thing a gate can see. The blind-spot list this series keeps now runs to
fifteen: overlap; whether a number is the *right* number; whether a source line cites a file
containing the claim; whether a caption describes the chart beneath it; an empty element vs
an intentional one; whose words are on the frame; whether a bar measures the thing the beat
is about; missing currency symbols; a text box sized to two pixels wrapping one word per
line; half-empty portrait frames; a case-folded proper noun; a figure stated as its own
complement; **a divider rule with no content under it; a column header aligned to the wrong
column; and a frame that quietly claims more than the data logs.**

## 9. Delivery

```
Mycroft_OmMali_06_11_2026.mp4                             3840x2160  24fps  202.12s  20646d81e7ee7ed5
reading-debt-announcements-into-cited-facts-slate.mp4     3840x2160  24fps  202.12s  8de4650f1913bfdd
vertical/...-916.mp4                                      2160x3840  24fps  202.12s  b7bbadfd77191edc
vertical/...-916-slate.mp4                                2160x3840  24fps  202.12s  1104218c5676991a
```
(SHA-256, first 16 hex digits.) All four are mirrored into `mp4/`.

GATE V, explicit `--mp4`, on both delivered masters: **0 BLOCKER, 0 MAJOR**, 24 frames each.

```
12 beats · 8 body at 54-71 words · 698 words
body 143.9s · bookends 58.2s · master 3:22.1, identical in both orientations
```

The masters stay in this folder. Nothing was published, and nothing was spent: `$0.00`.
