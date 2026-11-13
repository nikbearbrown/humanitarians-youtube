# SHOTLIST — Same Prompt, Different Answer

Typed work order. 9 beats, 2:23.5 at measured audio. All-Remotion reel: no
Manim, no stills, no human-supplied media, no open slots.

| Beat | Act | Component | Status | What is on screen |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | library | Composer on cream. `Olá, Jainil`. The question types in; two output lines answer it. |
| B01 | BLUF | `BrutalistHesitantWriter` | library | "The model picks the next word." typed, then `picks` deleted and `draws` typed. 15.2s window. |
| B02 | SETUP | `BarChart` | **reuse** | Seven candidate tokens as probability bars at T=1.0. `the` accented at 46.5%. |
| B03 | TURN | `DistributionShape` | **reuse** | The same scores at T=0.2 drawn solid, with T=1.0 behind as a dashed ghost. Two stat cells: 46.5% → 95.1%. |
| B04 | EVIDENCE | `PositionCurve` | **reuse** | Chance every token matches, against answer length. Falls from 95% to the floor; low callout reads "1 in 22,991". `plotScale: 1.3`. |
| B05 | LAND | `DigitDiff` | **NEW** | Two mono numbers, character-aligned. Everything from the first disagreeing digit goes terracotta on both rows. |
| B06 | SOURCE | `FormACard` | library | Two verbatim quotes from SGLang's deterministic-inference docs. `qc.sparse`. |
| B07 | HANDOFF | `ClaudeComposerAsk` | library | `Your turn.` The viewer's prompt types in full. |
| B08 | OUTRO | `HaiTitleOutro` | library | Title restate, SUBSCRIBE, `@HumanitariansAI`. `qc.sparse`. |

## GATE L outcome — three reuses, one build

The best library result so far. Three of the four body beats are carried by
components built for earlier videos, unmodified except for one opt-in prop:

- **`BarChart`** (pre-existing) — token probabilities, exactly what it is for.
- **`DistributionShape`** (built hours earlier for *The Tails Go First*) — its
  `ghost` prop was built to show a distribution that has lost something. Here
  the same mechanic shows a distribution being *reshaped*, which is the
  identical visual problem with a different meaning.
- **`PositionCurve`** (built 2026-10-02) — a value decaying against a axis, with
  the low point called out. The `plotScale` prop added earlier today for
  *The Tails Go First* is reused here for the same reason: a curve that decays
  to the floor leaves too much dead space at default size.

| Built | Why GATE L was a miss |
|---|---|
| `DigitDiff` / `916` | Nothing compares two numbers character by character and marks where they diverge. The top hit was a two-panel figure hardcoded to another reel. Printing both numbers without aligning them and marking the split would make the difference invisible, which is the opposite of the beat's job. |

`DistributionShape`'s `curve` minimum was lowered from 8 points to 4 so it could
take seven tokens. No existing reel passes fewer than 8, so nothing changed.

## Deliberate repetition

None. Four body beats, four different components.

## Portrait notes

`DigitDiff916` sets the numbers smaller relative to the frame rather than
cropping: the figure's width is set by the longest value, so a centre crop
would cut off the trailing digits — which are exactly the digits that differ.
`firstDivergence` is imported from the landscape scene (shared logic), while the
schema is declared locally so `--check` reports real props (gotcha A12).

## Caveat on B03's x axis

`DistributionShape` draws a continuous silhouette, and B03 feeds it seven
discrete tokens ordered by probability. The resulting shape therefore reads as
a decay curve rather than a bell — which is correct (sorted probabilities do
decay monotonically) but is worth stating. B02 immediately precedes it with the
same seven tokens as labelled bars, so the viewer already has the mapping, and
the axis ends are labelled `the` and `such` rather than numbers. The component
was reused rather than rebuilt because the `ghost` overlay — showing the same
distribution at a different temperature — is the whole point of the beat and
nothing else in the library does it.
