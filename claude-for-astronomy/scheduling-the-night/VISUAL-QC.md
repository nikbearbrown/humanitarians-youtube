# VISUAL-QC — *Finish What You Start.*

Ep. 17 · `scheduling-the-night` · frames read, both cuts, 2026-11-13

> **A gate passing is not the frame being right — and a gate failing is not the
> frame being wrong.** Both happened here. Four real defects shipped past every
> gate and were found only by looking; the nine MAJORs GATE V still reports are
> a measurement artifact, characterised below with numbers rather than waved off.

---

## What was read

| Pass | Frames | Source |
|---|---|---|
| 16:9 contact sheet | 16 | `_qc/contact_sheet-16x9.png` |
| 16:9 tail sample | 6 | B08–B13 pulled by hand, late in each beat |
| 9:16 contact sheet | 16 | `_qc/contact_sheet-9x16.png` |
| 9:16 targeted crops | 4 | B11 title bar, B12 footer, at native 4K |
| B01 sweep | 9 | one beat at 10/25/40/50/60/70/80/90/97% |
| Post-fix re-reads | 6 | B01 ×2, B03 legend ×1, B11 portrait ×2, B00/B12 footers |

Sampled **late** in each beat: a pale element mid-`FadeIn` is indistinguishable
from a rendering defect.

---

## Defects found — none of which any gate caught

### 1 · B11 and B13 — props named things their schemas do not define

`beat_sheet.json` gave `ClaudeVerdictArtifact` the props `rows` and `title`.
The zod schema defines `artifactTitle`, `artifactHeading`, `artifactLines`.
**zod drops unknown keys silently**, so B11 would have rendered the
component's DEFAULT text — a verdict card about chat vs cowork vs code, under
this episode's narration. `ClaudeTitleOutro` was the same shape:
`subtitle`/`folderLabel` given, `subline`/`handle` defined.

Caught by `remotion_scenes.py`'s own prop lint, which is the one check in this
toolkit that would have found it. The render was killed mid-B11 and restarted.

### 2 · B03 — a legend label welded to its swatch, and smaller than its siblings

Row 3, `shaded: below 20 deg, cannot point`, rendered with its first letter
touching the colour chip **and** at a visibly smaller size than the two rows
above it.

Root cause was in the shared helper, not the scene. `_swatch_row` centres its
label at `at + 0.11` and fits it to `inner = w - 0.46`. A label that fills that
width therefore has its left edge at exactly `at - w/2 + 0.34` — which is the
swatch's **right** edge. Zero gap, by construction. Short labels centre with
slack and look fine, so the bug only shows on the one longest label in the reel.
GATE B sees no collision because the chip and the label are separate mobjects
that merely abut.

Fixed in the helper (`inner = w - 0.44`, centred at `at + 0.22`, reserving 0.10)
and the row shortened to `below 20 deg: cannot point` so no `_fit()` scaling is
needed. B03, B09 and B10 were re-rendered in both aspects.

### 3 · B11 portrait — the title bar truncated to `… - one p…`

`ClaudeVerdictArtifact916`'s card is far narrower than the 16:9 one, so
`Finish What You Start - one page` clipped with an ellipsis. Landscape was
clean, which is exactly why reading **both** cuts is not optional. Portrait now
carries the untagged title.

### 4 · B00 and B12, both aspects — the wrong handle in the composer chrome

Neither composer beat set `folderLabel`, so the component rendered its zod
default: **`@NikBearBrown`**. Every earlier `claude-for-astronomy` episode sets
`@HumanitariansAI` explicitly. Found by diffing this beat sheet against the
siblings, not by any gate — a correct-looking string in the right place is
invisible to geometry and contrast checks alike.

### 5 · B01, both aspects — the lower half of the frame empty for over half the beat

`Ep. 17` and the handle are the only content in B01's lower band, and they were
revealed in the **last** play. GATE V flagged `underfill` at the 50% sample; a
nine-frame sweep showed it was not a transient:

```
10%   (title only)      25%   4%     40%  30%     50%  30%
60%  30%                70%  30%     80%  30%     90%/97%  clear
```

**4.6 s of an 8.4 s beat** at 30% fill against a 55% floor. Every other beat
lays its chrome down first via `chrome()`; B01 draws its own because it has no
title bar, and the order was the bug. The two reveals moved ahead of the card —
same play count, same run_times, so the pacing solve still holds (re-verified:
7 plays / 3.85 s anim in both aspects, unchanged).

---

## The nine MAJORs GATE V still reports

```
16:9   B03_50 B03_85 B05_85 B10_50 B10_85   low-contrast
9:16   B03_50 B10_50                        low-contrast
9:16   B11_50 B11_85                        underfill 53% (floor 55%)
```

**These are not text defects.** `final_frame_check.py` computes one ink colour
as the mean of **every** non-background pixel:

```python
ink_rgb = arr[ink].astype(float).mean(axis=0)
sep = abs(_lum(ink_rgb) - _lum(bg))
```

Ep. 17's plates are pale line-art on cream — thousands of near-background
pixels that pull that mean toward the page. Measured per frame, against the
actual page colour, the type a viewer reads is:

| frame | WCAG text contrast | share of non-bg ink that is pale plate |
|---|---|---|
| B03_50 | **7.0 : 1** | 62% |
| B03_85 | **7.7 : 1** | 61% |
| B05_85 | **5.7 : 1** | 76% |
| B10_50 | **7.9 : 1** | 76% |
| B10_85 | **7.4 : 1** | 78% |

All clear WCAG AA (4.5:1) comfortably; GATE W passed every scene per-element
before any of this. The flag tracks *how much pale plate is on screen*, which
rises with plate area and has no bearing on legibility.

**B11 portrait `underfill 53%`** is an aspect mismatch in the gate, not a layout
fault. `ClaudeVerdictArtifact916` deliberately reserves the top 12% and bottom
25% of the frame for platform UI (its own docstring says so); GATE V measures
against a safe area derived from the 16:9 layout, so a correctly inset portrait
card reads 2 points under the floor. The card was read at 4K and is well set.

**GATE V therefore exits 2 on both masters.** That is recorded here rather than
suppressed, and nothing was passed with `--lenient`.

---

## Verified NOT defects

- `10^2567` and `10^80` render as true typographic superscripts, no stray caret
  glyph — the Ep. 09 failure mode, checked again at native 4K.
- B10's legend keys correctly: greedy really is drawn `SOFT` and the planner
  `ACC` in `airmass_plate()`, so the chips match the plate.
- B07's `GREEN` / `RED` name the g and r bands in words only; no coloured chip
  on screen contradicts them, and the palette has no green.
- Every Manim clip lands 0.19–0.22 s **under** its beat — inside compile.py's
  ±5% silent-retime band, padded with a held frame, never centre-cut.
