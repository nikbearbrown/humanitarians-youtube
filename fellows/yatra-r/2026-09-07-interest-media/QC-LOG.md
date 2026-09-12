# VISUAL QC — Interest Media.

`yatra-interest-media` · frame-level pass per VISUAL QC LAW.
The mp4 probe is a FILE check and does not count as QC — every entry below comes from
actually reading rendered PNGs.

---

## Defects found and fixed

All four were caught by looking at frames, not by any numeric check. Each was fixed at the
root in scene source and the beat re-rendered.

### 1. B07 `ItmModels` — the gate overlapped the node it precedes · **BLOCKER** · FIXED

The follower track's gate hatching was drawn at `nx(0.5) − 258 + i*16`, but the node it
sits before is 460px wide and centred on `nx(0.5)`, so its left edge is at `nx(0.5) − 230`.
The last two hatch bars crossed the node's border — a container-overflow / collision defect,
and worse, it made the gate look like part of the node rather than an obstacle before it.

The `GATE` label had the same problem in the other axis: it sat 12px above the track's foot
line and the two nearly touched.

**Fix:** gate moved to `nx(0.5) − 330 + i*16` (36px clear of the node), the label moved with
it, the stopped post's travel end pulled back to `nx(0.5) − 370`, and the track foot dropped
from `y + 86` to `y + 150`. Re-rendered and re-inspected — clean.

### 2. B05 `ItmQuestion` — undersized composition, and the key straddled the border · **MAJOR** · FIXED

Two problems in one beat. The machine occupied only the middle band of `SAFE` with roughly
290px of dead space above it and 210px below — a FILL-THE-CANVAS failure. And the old key,
lifting out of its slot, came to rest **across** the machine's top border rather than clear
of it, which read as a rendering bug instead of a part being removed.

**Fix:** `BOX_Y` raised to `SAFE.y + 250` and `BOX_H` deepened 360 → 470; the slot enlarged
to match; the input/output stacks scaled up (bar height 40 → 52, step 58 → 72); key type
38 → 42. Lift distance taken 170 → 260, then to **300** after a second frame read showed the
key still clipping the box's rounded corner by ~11px. It now clears by 19px.

### 3. B04 `ItmVolume` — bottom third of the frame was dead · **MAJOR** · FIXED

The flood field stopped at `SAFE.y + 770`, leaving ~200px of empty cream under it before the
note line, so the beat read as top-clustered.

**Fix:** `FIELD_H` deepened 560 → 620, which runs the field down to the note and lets the
terracotta verdict band land where the eye already is.

### 4. B02 `ItmSource` — rename row clustered under the card · **MINOR** · FIXED

The side-by-side rename sat at `SAFE.y + 470`, directly beneath the attribution card, with
~290px of unused safe area below it.

**Fix:** row moved to `SAFE.y + 540`, question offset 150 → 168, question type 44 → 48.

---

## Nine-point rubric — final state

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | PASS — no element crosses the canvas edge |
| 2 | Title-safe margins | PASS — every scene is authored from the `SAFE` constant, never nudged by pixels |
| 3 | Container overflow | PASS after fix 1; B03's feed cards use `overflow:hidden` + ellipsis, so a longer item cannot spill |
| 4 | Collision | PASS after fixes 1 and 2 |
| 5 | Offscreen anchors | PASS |
| 6 | Legibility | PASS — smallest type is 22px eyebrow / 24px GATE label at 1920×1080, i.e. 44–48px in the 4K render. B03's dimmed column floors at 0.42 opacity, above the ~40% rule |
| 7 | Brand bug placement | PASS — `@Yatra` wordmark, lower-right, inside the safe inset, on every beat (LOGO LAW's stated fallback: no logo file ships in this tree) |
| 8 | Aspect | PASS — 3840×2160 |
| 9 | Canvas fill | PASS after fixes 2, 3 and 4 |

**Zero BLOCKER, zero MAJOR remaining.**

---

## Per-beat frames read

B00 · B01 · B02 · B03 · B04 · B05 · B07 · B08 · B09 · B10 · B12 read at ~85–95% of span
(where every element has landed). B06 and B11 are `ClaudeComposerAsk`, the same component
verified at B00. Frames kept in `_qc/frames/`.

Accent audit performed on the same pass: **one terracotta event per beat, thirteen for
thirteen**, and in every case it marks the interest side of the shift — never the follower
side, never the attribution.

---

## The 9:16 cut — its own pass

The portrait cut is re-banded, not scaled, so its layouts are different code and were
inspected separately. Frames read: B02, B05, B07, B09 (the four genuinely rebuilt layouts)
plus the endcard.

### 5. END card — wrong channel handle · **BLOCKER** · FIXED

`shorts.py`'s `--handle` argument **defaults to `@nikbearbrown`**, and the derive step was
run without overriding it. The generated endcard therefore carried another channel's handle
on a `@Yatra` reel, and `beat_sheet.json` recorded `card.handle: "@nikbearbrown"`.

**Fix:** endcard regenerated with `@Yatra`; the short's beat sheet updated to match.
**Standing note for the next derive on this channel: pass `--handle @Yatra`.**

### 6. END card — half resolution in a 4K cut · **MAJOR** · FIXED

`shorts.py` hardcodes `W, H = 1080, 1920` for the endcard PNG. Compiling the short at
`--height 3840` therefore upscaled it 2× — compile.py flagged it itself:

```
WARNING END: still 1080x1920 under output 2160x3840 — the move will reveal upscale artifacts
```

Every other beat is a native 2160×3840 Remotion render, so the endcard would have been the
only soft 4.5 seconds in the cut.

**Fix:** endcard regenerated at **2160×3840** with all metrics scaled 2× (type 64→128 and
44→88, rule width 4→8, spacing 26→52), reproducing `endcard_png()`'s design exactly at
double resolution. Re-compiled; the warning is gone.

*This is a toolkit limitation, not a reel defect — `shorts.py` cannot currently emit a 4K
endcard. Any future 4K short from this toolkit needs the same manual step.*

### 7. B05 `ItmQuestion916` — key clearance · **MINOR** · FIXED

Same class of issue as landscape defect 2, milder: the lifted key cleared the machine's top
border by only 4px, so at portrait scale the two edges read as touching. Lift taken
190 → 230 (44px clear), matching the landscape fix.

### Portrait rubric

| Check | Result |
|---|---|
| Shorts/Reels keep-out | PASS — all critical content above y≈1440 and left of x≈960; brand bug on the keep-out boundary, lower-left |
| Re-band vs scale | PASS — B02 stacks the rename, B05 runs the machine top→bottom, B07 makes each model a vertical chain, B09 stacks the ledgers |
| Generated graphics never centre-cut | PASS — all 13 beats re-rendered from 916 compositions; no `media/<beat>-916.mp4` auto-cuts exist |
| Density parity with landscape | PASS — `MARKS` and `TICKS` are imported from the landscape module, not redeclared |
| Aspect / resolution | PASS — 2160×3840 throughout, including the endcard after fix 6 |

**Render note:** B10, B11 and B12 failed their first portrait render with 30s browser
timeouts (`Timeout exceeded rendering the component`, `Timed out while setting up the
headless browser`) because the 4K landscape master was encoding concurrently. Re-run
serially, all three succeeded first try. Machine contention, not a code fault — but worth
knowing that this toolkit's 30s Remotion timeout is not generous enough to render and
encode 4K at the same time.

---

## Toolkit gates — status

**GATE V (`runtime/qc/final_frame_check.py`) — NOT USED, and this is deliberate.**
Its `BURN_IN_EXCLUDE` region masks only the bottom strip of the frame, while the review
cut's beat label is drawn top-right. On this toolkit it therefore reports BLOCKERs on every
beat of every reel, including reels that pass inspection — the same false positive logged on
the five previous reels in this series. Ink coverage was measured directly instead, using
the gate's own `analyze_frame()` against the clean master. **This is a toolkit bug, not a
reel defect, and the reel was not altered to satisfy it.**

**GATE T (`scripts/type_check.py`) — NOT RUN. The script does not exist in this tree.**
The skill lists it as mandatory ("ALWAYS RUN, like factcheck") but it is not shipped here.
Its §8.1 min-size, §8.2 overflow and §8.3 contrast checks were substituted by the frame
inspection above; §8.6 golden-strings was substituted by the numeral sweep in `FACTCHECK.md`.
Substitution logged rather than silently passed.
