# BUILD-LOG — building-the-filing-timeline-triage-and-document-server

AI Debt Tracker, week 3. `brutalist.art` · skill `ai-explainer` · channel `claude-hai`.
Free and local end to end — Kokoro TTS, Remotion, ffmpeg. **`$0.00`, no API key.**

---

## 1. What the source gave, and what was built from it

| Source | Became |
|---|---|
| `narration_script.md` — 8 sections, 441 words, 3:00 target | 12 beats, 704 words |
| `pantry/adt-w3-holdout.svg` | B01 `W3Recheck` + B02 `W3Fresh` |
| `pantry/adt-w3-funnel.svg` | B03 `W3Timeline` (top band) + B04 `W3Funnel` |
| `pantry/adt-w3-triage.svg` | B05 `W3Check` |
| `pantry/adt-w3-docs.svg` | B07 `W3Docs` |
| the script's Notes | B06 `W3Wrong` + B08 `W3Next` |

The four figures were moved out of the folder root into `pantry/` so nothing in the build
path can slot one as media (REBUILD LAW). Every body beat is a native Remotion scene.

**Numbers were not read off the figures by eye.** Each bar's geometry in the SVGs was
recomputed as a ratio and had to agree with its printed fraction before the value entered
`figdata.json`:

```
funnel rules stage   394/593 * 340px = 225.9   drawn 225.9      ✓
check precision      240/260                   = 0.923 = 24/26  ✓
check pass line      x=497 -> (497-250)/260    = 0.95           ✓
holdout fresh bar    56.7/170                  = 0.3335 = 1/3   ✓
```

## 2. Structural decisions

Eight script sections → eight body beats, with five changes, all listed in `PEDAGOGY.md`
for individual sign-off and all signed:

1. **0:15 split into B01 and B02.** At ~95 spoken words it was the longest section and
   carried two separate arguments — *which score is evidence*, and *what is still broken*.
2. **The exclusion moved ahead of the fraction.** The script states "of the three that had
   any debt" after the numbers. Said first, the denominator can never be heard as 5.
3. **The optional line "and one reading mistake was mine" kept.** Two seconds, and it
   removes an asymmetry where only the answer key's mistakes get named.
4. **The two false alarms named on the frame** instead of left inside "24 of 26".
5. **The closing on-camera section became B08**, a limits beat. Every episode in this series
   ends on its own limits, and they otherwise reached no frame.

No Manim beats, so GATE B never fires. No slates.

## 3. Assertions carried in `build_beat_sheet.py`

The build fails rather than let a number drift. Three of these hold *arguments*, not
arithmetic:

- **FRAMING** — `FRESH_SHARE < LAST_SHARE`. B01 exists because 3 of 3 is a calibration on
  the reports the fixes were made against and 1 of 3 is the measurement. If the fresh score
  ever caught up, the beat would be drawing a distinction that no longer exists.
- **SECOND** — recall `== 1.0` *and* `>= pass line 0.95`, while precision `<` recall and
  event type `<` precision. "It found everything" only means something beside what it cost.
- **THIRD** — `precision.of - recall.got == len(false_alarms) == 2`. The frame cannot name
  two mistakes while the arithmetic implies a different number.

Plus composition (`469+94+30 == 593`), funnel (`394+199 == 593`, `163+21 == 184`), the draw
(`3+2 == 5`), rules share inside 0.64–0.69 (the narration says "two thirds"), every B06
failure carrying a consequence, and `8 < 21` on the quote check.

Three claims are **not** measured in `figdata.json` and are named constants, each attributed
on the frame that uses it: `AGENT_STATE` (B00/B04/B08), `LABELLER` (B05/B08),
`OWN_MISTAKE` (B02).

## 4. GATE P

`PEDAGOGY.md` was written PENDING and the build stopped there. The audio gate was confirmed
refusing the unsigned reel before anything was generated:

```
[kokoro] GATE P: PEDAGOGY.md needs a signed VERDICT: PASS line (--no-gate to override)
exit=1
```

`--no-gate` was not used; it is blocked by the permission classifier and routing around a
quality gate is not a build step. Audio was generated only after the author signed.

This file deliberately never spells the signed-verdict phrase outside a quotation of the
gate's own error text, and `PEDAGOGY.md` never spells it at all except as the signature —
in week 1 a placeholder that quoted the phrase was itself enough to open the gate. The gate
now matches a verdict *line*, not a substring (`runtime/scripts/generate_audio_kokoro.py`).

## 5. Toolkit changes

| File | Change |
|---|---|
| `runtime/remotion/src/BuildingTheTriage.tsx` | NEW — the eight reel-local scenes |
| `runtime/remotion/src/Root.tsx` | one `<Folder>`, each scene registered twice (1920×1080 and 1080×1920 under `<pattern>916`) |

`BuildingTheTriage.tsx` imports nothing from `AiDebtTracker.tsx`,
`GroundingTheDebtTracker.tsx`, `BuildingTheAnswerKey.tsx` or the week 1–11 reel files, by
series convention: every earlier signed master stays re-renderable byte-identically. Its
chassis is a copy of week 2's, which arrives with week 2's portrait values already raised.

Nothing else in the toolkit was touched for this episode, and nothing outside this folder
in the fellow tree was touched at all.

## 6. Timing

```
12 beats · 8 body at 54–70 words (band 45–72) · 704 words
narration 205.45s (3:25.4), measured — the mp3 durations are the master clock
```

Both cuts use the same mp3s; `make_vertical.py` copies them rather than regenerating, so no
number can differ between the two masters.

## 7. Portrait pass

Expected, and budgeted for. The chassis arrives with week 2's portrait values already
raised, so this pass was small — two beats, both found by LOOKING at frames rather than by a
gate.

| Beat | What portrait did | Change |
|---|---|---|
| B04 `W3Funnel` | **GATE V BLOCKER x2, `edge-bleed`.** Every figure clipped: `593` rendered as `59`, `394` as `39`, `199` as `19`, `184` as `18`. | The track width was `SAFE.w - f(430, 0)`. The 430 is the label column, which in landscape sits *beside* the track and so has to be subtracted — but in portrait the label stacks *above* it, zeroing the subtraction while the value column (124px) and its gap (14px) still sat beside the track. The row ran 138px past the title-safe edge. Now `SAFE.w - f(430, 138)`, capped at `f(1180, 834)` so 834 + 14 + 124 = 972 exactly. |
| B01 `W3Recheck` | Passed every gate and was wrong anyway: the whole argument — three cells, a two-cell excluded tail and the fraction — occupied 768 of 972 safe pixels, with three dead bands down the frame. | Per-report `UNIT` 112 -> 136, bar height 72 -> 96, row gap 50 -> 64. The widest row now measures 888 and still clears the edge. |

Landscape values were not touched in either fix, so the 16:9 cut is unchanged by the portrait
pass. Both cuts then recompiled, and GATE V was re-run **with an explicit `--mp4`** on each
delivered file — with two non-slate cuts in a folder the gate otherwise grades whichever it
finds first.

## 7a. What reading the frames caught that no gate did

Three defects, all in the landscape cut, all invisible to GATE V:

1. **B02 said "a super micro coupon".** `str.capitalize()` lower-cases the whole string
   before raising its first letter, and it ate a company name. Replaced with a helper that
   raises only the first character.
2. **B07 rendered `-> -> refused:`.** `W3Docs` draws its own arrow before the refusal and the
   prop carried a second one.
3. **B08's quote row read "13 of 21 quotes found".** The arithmetic was right — 21 - 8 — but
   every other beat and the narration state *8 of 21 were not verbatim*, so the frame made
   the viewer subtract, and "quotes found" reads like a recall score, which is the exact
   misreading that row exists to prevent. Now "8 of 21 not verbatim".

None of these is a thing a gate can see. The blind-spot list this series keeps now runs to
twelve: overlap; whether a number is the *right* number; whether a source line cites a file
containing the claim; whether a caption describes the chart beneath it; an empty element vs
an intentional one; whose words are on the frame; whether a bar measures the thing the beat
is about; missing currency symbols; a text box sized to two pixels wrapping one word per
line; half-empty portrait frames; a case-folded proper noun; and a figure stated as its own
complement.

## 8. Delivery

```
Mycroft_OmMali_30_10_2026.mp4                                   3840x2160  24fps  205.45s  33b54384c0ae81ad
building-the-filing-timeline-triage-and-document-server-slate.mp4  3840x2160  24fps  205.45s  b19dc494ad922e1b
vertical/...-916.mp4                                            2160x3840  24fps  205.45s  8de4dbad18e0dd01
vertical/...-916-slate.mp4                                      2160x3840  24fps  205.45s  17bae74c24d1f9a2
```
(SHA-256, first 16 hex digits.) All four are mirrored into `mp4/`.

GATE V, explicit `--mp4`, on both delivered masters: **0 BLOCKER, 0 MAJOR**, 24 frames each.

The masters stay in this folder. Nothing was published, and nothing was spent: `$0.00`.
