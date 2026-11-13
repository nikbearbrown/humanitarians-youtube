# BUILD-LOG — "Writing the Lyrical Literacy Fellows Handbook"

What broke, what it cost, and what changed because of it. Built 2026-10-05 (late for the week
of 28 Sep – 2 Oct).

## 1 — Showing a document without showing it unreadably

A whole handbook page at video size is unreadable and fails GATE T §8.1 (the type check
measures text inside images too). The new `HaiDocPages` scene shows six **crops** of the real
v1.0 PDF, rendered at 300 dpi and cut so their body type lands above the floor; behind the
current crop are blank sheets (no thumbnails with sub-floor text). Portrait shows each crop
larger (first 1.65× with a pan, finally 2.2× with no pan; see §5). The crops' page numbers, clip boxes and SHA-256 are in
`pantry/handbook/crops.json`, beside the PDF's own hash.

The first crop pass was misaligned (clip boxes started 30 pt inside the page margin, cutting
the left edge of three crops); re-cut from the 63 pt margin.

## 2 — What is never shown

The handbook holds a shared login and staff contact details. None of the crops comes from
Section 3, Document control or Section 4.1, and the handbook file itself is not committed.

## 3 — Library first

Six of eight beats reuse library scenes with this week's content: `ClaudeComposerAsk`,
`HaiProgressSignupChain` (five tools, cue-driven), `HaiProgressOverturned` (five rows,
cue-driven), `HaiVerdictSplit`, `HaiProgressRoadmap` (fixed timing, no cue support),
`HaiApplyCard`, `HaiTitleOutro`. Portrait strings are shortened in `vertical/beat_sheet.json`
(`vertical_strings.py`), with `phoneType` on the scenes that support it.

## 4 — No names

Standing instruction: nobody but the presenter is named. The reviewer, supervisor and the
program's founder appear by role only, in narration and on screen.

## 5 — Portrait fixes found in the rendered frames

- `HaiProgressRoadmap916` had no phone type scale (its labels were well under the 9:16 floor).
  It gained an opt-in `phoneType` (title 5.0vh, card labels and sub-lines 4.2vh, small labels
  3.1vh, no sub-line on committed cards, no-wrap card labels, no eyebrow, layout spread to
  y 20–79%); without the flag, earlier reels are unchanged. The first phone sizes (labels 3.4vh,
  small 2.2vh) passed at 1080 × 1920 but failed GATE T §8.1 at the 4K master (lowercase x-height
  62–71 px against a 72 px floor), so they were raised and re-checked on a 4K probe still.
- `HaiProgressSignupChain916` placed its spark line for four tools; with five it collided with
  the last card. With more than four tools it now follows the sheet; four or fewer are unchanged.
- `HaiDocPages` portrait: the crops are shown 2.2× with no pan, so the start of each line stays
  in view; the stats sit at 70% of the height.
- Portrait titles and steps shortened where they wrapped (`vertical_strings.py`).

## 6 — The first renders played on the wrong clock

`props.durationSeconds` was missing from the beat sheets, so `HaiDocPages` played on its 20 s
default and the cue-driven library scenes (`HaiProgressSignupChain`, `HaiProgressOverturned`)
fell back to their fixed staggers. Written into every beat of both sheets; B01–B04 (landscape)
and B01–B05 (portrait) re-rendered.

## 7 — Gate V refused the first portrait final

The first portrait final passed GATE T and was then refused by Gate V (3 BLOCKER, 1 MAJOR):

- **B01 edge-bleed.** The two blank sheets behind the crop are offset 14 px each to the right, so
  with a full-width sheet they ended past the title-safe edge. The portrait sheet is now narrower
  by the stack offset.
- **B04 edge-bleed at 85%.** "not used by a new fellow" (no-wrap) ran past the card. Shortened to
  "used by a new fellow": it sits under the NOT YET header, so it still says the same thing.
- **B04 underfill at 50% (52% of the safe box).** The not-yet item and the spark line arrive late in
  the beat, so mid-beat the lower band was empty. `HaiVerdictSplit` gained an opt-in `baseline`
  (portrait only): a ghost hairline above the spark line from the first frame, the same device as
  the pitch explainer's portrait scenes. Earlier reels don't set it and are unchanged.

4K probe stills of both beats at the gate's sample points (50%, 85%): Gate V clean (fill
69–75%), GATE T pass. Both re-rendered.

## Render

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/FellowsHandbookUpdate_RohanV.mp4` | 3840×2160 | 136.00 s | `b7ed3eb39bcce276aca18f47e25622898d95a264c54e6aeef33f830d4bfc933c` |
| 9:16 | `vertical/FellowsHandbookUpdate_RohanV.mp4` | 2160×3840 | 136.00 s | `23be8916b05f4967e05342537abc1e9f23734ac61b40ebab7c66376da7f35e7f` |

Gates on the accepted finals: GATE F pass; GATE T pass ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR
(16 landscape and 16 portrait frames sampled). Looked at by eye: [qc-sheet-16x9.png](./qc-sheet-16x9.png),
[qc-sheet-9x16.png](./qc-sheet-9x16.png).

Landscape: accepted on the first final. Portrait: accepted on the fourth (refused twice by GATE T on B05, §5, then by Gate V on B01 and B04, §7). All on 2026-10-05.

Uploaded to Google Drive `2026-10-02/landscape/` and `2026-10-02/vertical/`; md5 of each Drive copy
matches the local master.
