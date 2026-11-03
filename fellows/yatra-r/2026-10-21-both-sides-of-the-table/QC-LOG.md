# VISUAL QC — Both Sides of the Table.

`yatra-both-sides-of-the-table` · frame-level pass per VISUAL QC LAW.
The mp4 probe is a FILE check and does not count as QC — every entry below comes from
actually reading rendered PNGs.

---

## Defect found and fixed

### 1. B05 `TblTable` — the table read as an empty box, and the exchange missed it · **MAJOR** · FIXED

This beat's entire argument is an *arrangement*: four seats, and the only live exchange
running between the two machines while both humans wait. The render succeeded and every
element was present, but the frame showed the argument failing to land:

- the table was drawn at `MID_Y − 46`, **above** the machine-seat row, so it floated
  between the human row and the machine row as a large empty white rectangle with nothing
  in or on it — it read as a missing element, not as furniture;
- the terracotta machine-to-machine traffic ran at `MID_Y + 132`, i.e. **below** the
  table rather than across it. The exchange that the whole beat is about did not visibly
  happen *at* the table.

**Fix:** the table now sits on the machine row (`MID_Y + 86`, height 100), spanning
between the two machine seats, so the traffic line crosses its surface. The traffic label
moved to `MID_Y + 206` to clear the table it now sits under.

The portrait sibling (`TblTable916`) was checked at the same time and did **not** need
this fix — its vertical layout already runs the traffic down *through* the table.

---

## Nine-point rubric — final state

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | PASS |
| 2 | Title-safe margins | PASS — every scene authored from the `SAFE` constant |
| 3 | Container overflow | PASS — multi-line labels (B08's 66%, B09's 41%) wrap inside their columns |
| 4 | Collision | PASS after fix 1 |
| 5 | Offscreen anchors | PASS |
| 6 | Legibility | PASS — smallest type is the 22px eyebrow and 25px source lines at 1920×1080 (50px in the 4K render) |
| 7 | Brand bug placement | PASS — `@Yatra`, lower-right, inside the safe inset, every beat |
| 8 | Aspect | PASS — 3840×2160 |
| 9 | Canvas fill | PASS |

**Zero BLOCKER, zero MAJOR remaining.**

---

## Citation discipline — audited on the frames, not just in the props

This reel carries **eight figures from five publishers**, so the citation rendering was
checked visually beat by beat rather than trusted to the types alone:

| Beat | Figure on screen | Citation on screen | Accent? |
|---|---|---|---|
| B02 | `86%` | Gartner, via CI CoPilot, October 2026 | no — ink (adoption never glows) |
| B03 | `4 in 5` | Greenhouse, via CI CoPilot, October 2026 | no — ink |
| B06 | `63%` + `+13 POINTS IN SIX MONTHS` | Greenhouse, May 2026 | delta chip only |
| B07 | `38%` | Greenhouse, May 2026 | yes — the withdrawal |
| B08 | `26%` **and** `66%` | **two separate lines, one under each column** | yes — both |
| B09 | `41%` + `SELF-REPORTED` | SelectSoftwareReviews, 2026 | yes — hidden layer |

Verified on the B08 frame specifically, because it is the beat most likely to mislead:
the two figures sit side by side with **their own citations beneath their own columns**,
the unfilled remainder of each track is left **visibly empty and unlabelled**, and the
closing line reads *"Different samples, different questions. They are shown side by side,
not added together."*

Verified on the B06 frame: the disclosure *"Only the change was published — the earlier
figure is not shown here because it wasn't supplied"* renders on screen. No earlier value
is drawn or implied anywhere.

Verified on the B09 frame: the hidden layer renders as a **label describing what the text
is for**, not as a working injection string. No invented candidate or employer appears.

Every source line renders in `MUTE`. No citation takes the accent anywhere in this reel.

---

## Frames read

B01 · B02 · B05 · B06 · B07 · B08 · B09 · B10 at ~90–95% of span. B00, B04 and B12 are
`ClaudeComposerAsk`; B11 and B13 are the shared verdict/outro components, proven across
eight prior reels. Frames kept in `_qc/frames/`.

---

## Toolkit gates — status

**GATE V — NOT USED.** Reports false BLOCKERs on every reel built in this tree (its
`BURN_IN_EXCLUDE` masks the bottom strip while the review cut's label is drawn top-right).
Ink coverage measured with its own `analyze_frame()` on the clean master instead.

**GATE T — NOT RUN; `scripts/type_check.py` does not exist in this tree.** Substituted by
the frame inspection above and the numeral sweep in `FACTCHECK.md`. Logged, not silently
passed.

**Render environment.** Both toolkit-level render failures hit during this build are
documented in `BUILD-PROMPT.md` and in the sibling reel's QC log: orphaned
`chrome-headless-shell` processes after a machine sleep, and Remotion's 30s per-frame
timeout being too low for `--scale=2` frames of full-bleed EB Garamond. The second is now
mitigated by the `ART_TIMEOUT` knob added to `runtime/scripts/remotion_scenes.py`
(default 120000).
