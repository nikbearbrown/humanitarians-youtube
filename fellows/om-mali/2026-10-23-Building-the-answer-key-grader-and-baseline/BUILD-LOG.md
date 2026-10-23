# BUILD-LOG — building-the-answer-key-grader-and-baseline

AI Debt Tracker, **week 2**. `brutalist.art`, skill `ai-explainer`, channel `claude-hai`.
Free and local end to end — Kokoro TTS, Remotion, ffmpeg. **`$0.00` spent, no API key used.**

---

## What the source material was, and what it wasn't

The folder arrived with `narration_script.md` (author-written, 3:00 target, 448 words) and six
files loose in the root — `adt-w2-answerkey`, `adt-w2-handcheck` and `adt-w2-headroom`, each a
PNG with its SVG beside it. They were moved into `pantry/` as reference, where this series
keeps them; they are never slotted as media.

**There was no `figdata.json`.** The script's "Where every number comes from" table names the
project files behind each figure, but those live in the AI Debt Tracker repo, not here. So
`figdata.json` was written by transcribing the author's published results out of the three
SVGs — which carry every datum as geometry *and* as text — and cross-checking each against the
script's table. Neither reading was taken on trust: every bar's width was recomputed as a ratio
and had to agree with its printed fraction. All of them did:

```
answerkey   510.5 / 620 = 0.8234 = 900/1093      23.3 / 620 = 0.0376 = 41/1093
handcheck   136 / 170   = 0.800  = 8/10          113.3 / 170 = 0.667 = 2/3
headroom    243.8 / 260 = 0.9375 = 30/32         216.7 / 260 = 0.8333 = 5/6
```

There was no `description.txt` this week; the long-form one was written from the script.

## The fellow tree was renamed between sessions

Every folder under `fellows/om-mali/` now carries a topic slug — week 1 is
`2026-10-16-feasibility-Answer-key-and-model-selection`. Its masters and helper scripts are
intact, and `lock_durations.py` and `make_vertical.py` were copied forward from there. Nothing
outside this reel's own folder was written during this build; other sessions are editing the
om-mali tree.

## Structure: 7 script sections → 8 body beats

| Decision | Why |
|---|---|
| **1:13 split into B03 (the five bugs) and B04 (calibrated vs measured)** | At ~95 spoken words it is by far the longest section and it carries two different arguments: *the grader was wrong in five specific ways*, and *the number that follows a fix is not evidence*. One frame holding both makes the second a footnote on the first. |
| **B05 leads with the zero, against the script's order** | Said as written, a listener hears a 90% system with a caveat attached. The zero is the finding; 90.7% is the thing that hides it. The empty track is drawn before either flattering number appears. |
| **"So ten of ten is a calibration, not a score" added to the voice** | The script's Notes make exactly this point and its body does not. It is the sentence that stops the reel overselling itself. |
| **The closing on-camera section becomes B08, a limits beat** | Every episode in this series ends on its own limits, and the limits live in the script's Notes, which otherwise reach no frame. The three next steps sit inside it. |
| **Oracle and Broadcom named aloud; AMD and Equinix only on the frame** | Five company names in one spoken sentence is a list, not evidence. Two carry the point in the voice and all five are legible on screen. |

Resulting edit: **12 beats** — B00 cold open, B01–B08 body, B09 verdict, B10 handoff, B11
outro. Body beats 58–71 words, 718 words total, **204.51 s (3:24.5)** measured.

The word band is 45–72, four wider at the top than week 1's. This script **speaks its large
numbers** — "one thousand and ninety three", "nine thousand six hundred and fifty three" — and
one figure can cost six words. Tightening the band would mean cutting evidence to pay for the
way a number is pronounced.

## Scenes

`runtime/remotion/src/BuildingTheAnswerKey.tsx` — eight components, registered twice in
`Root.tsx` (1920×1080 and 1080×1920 under the `916` name). The file imports nothing from
`AiDebtTracker.tsx`, `GroundingTheDebtTracker.tsx` or the week 1–11 reel files, by series
convention: every earlier signed master stays re-renderable byte-identically.

The chassis was copied forward from week 1 **including its tuned portrait values** — week 1
underfilled on six of eight body beats and the fix was 73 raised `f(landscape, portrait)`
values, so starting from the tuned version rather than the original saves repeating it.

Three drawings carry their beat's argument and should not be "simplified":

- **B05 is an outlined track held EMPTY**, with the word inside it. A bar of width zero reads
  as "nothing was caught"; an absent bar reads as a rendering fault, which this series has
  shipped before. The flattering 90.7% sits *beneath* it at smaller size.
- **B04's dashed rule** separates the ten reports that *found* the five fixes from the three
  picked first and graded once. Merge the bars into one group and the beat stops arguing.
- **B06 draws a span on one axis**, not two bars. Two bars show two quantities; the distance
  between them is the claim.

## Defects found and fixed

1. **B06's baseline label wrapped one word per line.** The label was sized from its own tick
   position (`width: Math.max(x0, 1) * 2`), which collapses to **2 pixels** when the baseline
   is 0 — which it always is on this frame, that being the entire point — so "copying forward:
   0" stacked into three lines. The label is now anchored to the tick but sized independently.
   **GATE V passed this frame**: a 2px-wide text column is neither an edge bleed nor a fill
   failure.

2. **B06's announced label was pinned to the frame's right edge**, not to its own marker. On
   the first axis the tick is at 94% of the width so it looked deliberate; on the second, at
   83%, the label floated a long way from the mark it describes. Both labels now right-align
   to their own tick.

3. **Portrait underfilled on six of eight body beats** on the first portrait read — B01,
   B02, B04, B05, B06 and B07. Not wrong, just small; the failure mode caught early for the
   fifth week running. **59 `f(landscape, portrait)` values were raised**, the landscape half
   of every one unchanged, so the 16:9 master did not need re-rendering. The largest single
   change is B05's empty track, 168 → 300px tall: the whole beat is that rectangle being
   empty, and at 168px it read as a thin strip rather than a void. B03 and B08 were already
   right and were left alone. Details in `vertical/README.md`.

## GATE P actually bound this week, for the first time

Last week's build generated audio while `PEDAGOGY.md` said `VERDICT: PENDING`, because the gate
searched the whole file for the substring and that file's own placeholder spelled the phrase
out. That hole was closed on 2026-10-18; `generate_audio_kokoro.py` now reads the first VERDICT
token on a line and requires *it* to say PASS.

This week the gate refused the unsigned reel exactly as intended:

```
[kokoro] GATE P: PEDAGOGY.md needs a signed VERDICT: PASS line (--no-gate to override)
```

Weeks 9–12 generated their pre-signature review audio with `--no-gate` and recorded it. That
flag is **blocked by this environment's permission classifier**, through both shells, so there
was no review cut this time: the build stopped, the author was shown `PEDAGOGY.md`'s nine-item
sign-off list and the six FACTCHECK rows that matter, signed on the paperwork, and the pipeline
ran straight through with the gate on. The audio was generated once, under a signed gate, and
has not been regenerated since.

**This file's `PEDAGOGY.md` deliberately never spells the signed-verdict phrase out** except as
the signature itself — its sign-off instruction describes the words rather than quoting them.

## What GATE V did not catch, again

Across thirteen episodes the gate has been blind to: overlap; whether a number is the *right*
number; whether a source line cites a file containing the claim; whether a caption describes
the chart beneath it; an empty element versus an intentional one; whose words are on the frame;
whether a bar measures the thing the beat is about; and whether money figures carry a currency
symbol. This week add: **a text box sized to two pixels, wrapping one word per line, is neither
an edge bleed nor a fill failure.**

Defects 1 and 2 were both found by reading frames. The gate passed the 16:9 cut on its first
run, with both of them in it.

## Toolkit changes

- `runtime/remotion/src/BuildingTheAnswerKey.tsx` — new, reel-local.
- `runtime/remotion/src/Root.tsx` — one new `<Folder>` registering the eight scenes twice.
- No change to any shared `scenes/` component, any script, or any gate. The unknown-prop lint
  stayed **silent for every beat of both cuts**, including the bookends.

## Verification

```
GATE L   clean, first run
GATE V   16:9  0 BLOCKER / 0 MAJOR, 24 frames (defects 1-2 were invisible to it)
         9:16  0 BLOCKER / 0 MAJOR, 24 frames, after the rescale pass
         both re-run with --mp4 pointed at the exact delivered file
PROOF    12 beats: 8 SHOW / 4 justified-HOLD / 0 PUNT
GATE P   PASS — signed by the author (Om Mali), 2026-10-23, with the gate ENFORCED
GATE F   not triggered (no Manim beats)
COST     $0.00

Mycroft_OmMali_23_10_2026.mp4                       3840x2160  24fps  204.51s  AA9B9266...
vertical/...-916.mp4                                2160x3840  24fps  204.51s  88CCA953...
mp4/ mirrors md5-identical to both masters; the two cuts share one set of mp3s.
```
