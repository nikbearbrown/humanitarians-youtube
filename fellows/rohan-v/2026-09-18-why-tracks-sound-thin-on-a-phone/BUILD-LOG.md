# BUILD-LOG — "Why Your Track Sounds Thin On A Phone"

What broke, what it cost, and what changed because of it.

Several entries here are shared with the sibling reel
[16-bit or 24-bit: What Bit Depth Does](../2026-09-18-what-bit-depth-does/BUILD-LOG.md) —
both were built in the same session on the same new toolkit code. The ones below
are the ones specific to this reel, plus a short index of the shared ones.

## 1 — `volumedetect` prints at info level, so `-v error` hides the answer

The first pass of the Case 2 measurement returned **nothing at all**. The
command was written with `-v error` out of habit, and `volumedetect` reports its
`mean_volume` at ffmpeg's *info* level — so the flag suppressed the very numbers
being measured.

**Fix:** drop `-v error`, keep `-hide_banner -nostats`, and grep for
`mean_volume:`. MEASUREMENTS.txt carries a note about it at the bottom, because
this will happen to someone else.

**Cost:** one measurement pass, and a few minutes believing the fold-down had
done nothing.

## 2 — The prediction was written down first, and it held

Not a failure, and the most valuable thing in this reel. For a 0.6 ms delay,
summing predicts nulls at odd multiples of 833 Hz and peaks halfway between.
That was written into MEASUREMENTS.txt **before** the measurement ran.

| band | predicted | measured |
|---|---|---|
| 830 Hz | NULL | **−10.2 dB** |
| 1660 Hz | peak | −0.4 dB |
| 2500 Hz | NULL | **−9.8 dB** |
| 3300 Hz | peak | −0.6 dB |

All four landed. And the *depth* of the nulls — about −10 dB rather than
−∞ — is what produced the reel's entire framing: a 120 Hz-wide analysis band
collects energy from frequencies that are not cancelling, and broadband noise
only cancels completely at the exact null frequency. **That is why the reel says
"holes", not "silence".** A cleaner result would have made a worse video.

## 3 — And then the whole table was cut

> These are too detailed. Keep it high level. Use details only where necessary.

B04's axis is now labelled only LOW NOTES → HIGH NOTES and carries no numbers at
all. The strongest evidence in either week-04 reel is in the log and not in the
video. Recorded here because it was the right call and it did not feel like it.

Also cut: per-row live waveforms and frequency columns in B03 (position and
outcome only), and a three-column before/after comparison.

## 4 — `MonoDoorToWaves` had both arrows pointing the same way

During the "pushing against each other" state, both figures' arrows pointed
right — directly contradicting the narration that was playing over them. The
frame asserted the opposite of the beat's entire point.

```tsx
// wrong: dir was constant
{person(1, 1, op(sDoor), hOpp)}
// right: with `opposed`, the right-hand person pushes LEFT
{person(1, opposed > 0.5 ? -1 : 1, op(sDoor), hOpp)}
```

**Found by:** reading the contact sheet frame by frame. No gate checks whether a
diagram agrees with its own narration.

## 5 — Gate V failed the first clean master

**0 BLOCKER, 1 MAJOR** — B02 `underfill`, 50% against a 55% floor.

The canvas-fill law measures the **bounding box of all ink** against the safe
area, and with the wave panel keyed to `agree` (0.808) the entire right half of
that frame was empty at its own midpoint. A real defect, not a gate artefact.

**The fix improved the teaching.** The panel now arrives on `opposite` (0.311),
so the viewer watches the two lanes go out of phase exactly as the narration
says they do, and sees the sum lane collapse on `nomove` — instead of meeting an
already-collapsed sum at the end of the beat. Only the closing sentence still
waits for `agree`.

Second run: **0 BLOCKER, 0 MAJOR.**

## 6 — Two defects the gate could not see

Gate V passed. Reading the contact sheet found two more, one of them a
correctness bug:

### The wide layer claimed to be "unchanged" before the reveal

B03's verdict text is driven by `shown = r.delta * travel`, and `travel` is 0
until that row's own cue lands. So the wide-airy-layer row printed **"unchanged"**
for the seven seconds between its arrival and `gone` — stating the exact
opposite of what the beat exists to say, in the frame, while the narration was
saying "dropped by almost fifty decibels".

```tsx
// wrong: any row with travel == 0 reads "unchanged"
{shown > -0.05 ? 'unchanged' : `${shown.toFixed(1)} dB — effectively gone`}
// right: only a genuinely centred part may say "unchanged";
//        the wide row says nothing until there is something true to say
{centred
  ? (shown > -0.05 ? 'unchanged' : `…`)
  : (travel < 0.02 ? '' : `${shown.toFixed(1)} dB — effectively gone`)}
```

This is the most serious defect found in either reel this week, and no gate
would ever have caught it — the frame was well-composed, well-filled and
legible. It was simply wrong.

### The door did not read as a door

At 323 × 112 px the door panel was a horizontal **bar** with an arrow in it, and
the two figures — a 0.040 dot on a 0.028 stem — read as punctuation beside it.
Since `rotateY` about a left edge is exactly how a door swings, the panel has to
be a front-facing, taller-than-wide shape.

**Fix:** door to 230 × 248 px with a proper jamb; figures given shoulders, a
torso at human proportion, and a visible arm reaching toward the door. The
portrait sibling got the same treatment at 243 × 211 (portrait has less vertical
room, so it is squarer — but it reads).

## 7 — Shared with the sibling reel

Full detail in
[the other BUILD-LOG](../2026-09-18-what-bit-depth-does/BUILD-LOG.md):

| # | What |
|---|---|
| 3 | **No scene in this project had ever loaded a font** — every earlier reel rendered in fallback Georgia/Segoe UI. Fixed with `lib/haiType.ts` |
| 4 | `remotion-bits@0.2.1` has an undeclared dependency on `culori` |
| 5 | `@remotion/paths` was a version ahead of core; pinned to 4.0.486 |
| 6 | `HaiApplyCard` silently drops unknown props — B05 rendered the literal "Set in beat sheet." |
| 9 | `compile.py --review` was broken on Windows: a raw font path destroys ffmpeg's filterchain, which is also why week-01 shipped with no QC sheet |
| 10 | cp1252 corruption in eight scripts — including the `shorts.py:246` bare `read_text()` that caused the week-03 mojibake |
| 11 | Gate V is only meaningful on `./art final`; the review cut always fails with 14 `edge-bleed` blockers by design |

Both week-04 short beat sheets were byte-checked for mojibake: **clean**, with
all 9 middots and 7 em-dashes intact.

## Ledger

| | |
|---|---|
| Plan revisions | 2 (both before any render) |
| Measurement passes wasted to a tool footgun | 1 |
| Predictions made before measuring | 1, and it held on all four positions |
| Gate V runs | 2 landscape, 1 portrait |
| Gate V findings | 1 MAJOR, fixed → 0/0 |
| Defects found by eye that the gate missed | 3 (one of them a factual error on screen) |
| Beats re-rendered after QC | 3 landscape (of 7) |
| Paid API calls | **0** |
| Cost | **$0.00** |
