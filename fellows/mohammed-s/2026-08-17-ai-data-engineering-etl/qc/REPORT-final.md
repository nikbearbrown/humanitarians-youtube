# VISUAL QC — final pass · `ai-data-engineering-etl`

Both masters, after the fix-and-re-render cycle. Gate V (`runtime/qc/final_frame_check.py`)
sampled 20 frames per cut; every flagged frame was then opened and looked at, per
VISUAL QC LAW — the mp4 probe is a file check and never counts as QC.

## Result

| Cut | BLOCKER | MAJOR | Verdict |
|---|---|---|---|
| 16:9 3840x2160 | **0** | 5 (all `underfill`) | ship |
| 9:16 2160x3840 | **0** | 8 (all `underfill`) | ship |

Zero BLOCKERs in both cuts. Every remaining MAJOR is the same automated
`underfill` heuristic, adjudicated by eye below.

## Defects found and FIXED this pass

| # | Cut | Beat | Defect | Fix |
|---|---|---|---|---|
| 1 | 9:16 | B03 | **Collision.** The `SOURCE · ORDERS → TARGET · FCT_ORDERS` header was half-buried under the first schema card — caused by my own earlier active-band change pulling the cards upward into it. Gate V never flagged this; it only measures edge-bleed and fill. Found by looking at the frame. | Re-stacked the portrait column: tally 0.083→0.098, header 0.128→0.140, cards 0.140→0.160, verdict/footnote re-seated. |
| 2 | both | B01, B03, B05, B06 | **Title-safe breach (8 BLOCKERs).** `EtlSpark` sat at y=62 portrait / y=44 landscape, above the SAFE916 (96) and SAFE (54) top insets. | Inset moved to 108 / 62 in `etlShared.tsx`. |
| 3 | 16:9 | B05 | **Underfill at 39%.** Type undersized for the frame. | ITEM_FONT 38→43, TITLE_FONT 48→54, MARK 42→48, row rhythm 0.1037→0.113, columns widened. Now 40% at mid-beat and visually full at 90%. |

Eight beats were re-rendered and both masters recompiled after these fixes.

## Remaining `underfill` MAJORs — adjudicated, not suppressed

The heuristic measures the ink bounding box against the safe area and wants >=55%.
It cannot distinguish deliberate whitespace from a layout defect. Each was opened:

- **B09 outro, 7% (16:9) / 18% (9:16)** — a poster title card. Sparseness *is*
  the design (OUTRO LAW: title restate, poster serif, terracotta period). Not a defect.
- **B07 verdict artifact, 46% both cuts** — the stock `ClaudeVerdictArtifact`
  card with its standard margins. Body type is 28px in comp space, i.e. 28px
  effective at the 1080p delivery floor — above the ~24px legibility floor.
  Verified by reading the scene source, not by eyeballing the frame. Not a defect.
- **B05 at the 50% sample, 21-40%** — a progressive-disclosure beat: the right
  column does not appear until p=0.56, so a frame sampled at p=0.50 is *supposed*
  to be half empty. At p=0.90 the frame reads full. Sampling artefact, not a defect.
- **B01/B06 portrait, 42-46%** — the bottom ~25% is the toolkit's documented 9:16
  active-band reserve (content kept inside y 230-1440 for platform UI), which the
  stock 916 scenes also leave empty. Intentional.

None of these is a real defect, and "fixing" them would mean inflating title
cards and violating the reserve. Logged rather than actioned.

## Frames read this pass

9:16 B03 @88% (collision fix confirmed) · 9:16 B06 @90% · 16:9 B05 @90% ·
16:9 B07 @85% · 16:9 B08 @80% + B09 @85% (handoff + outro).
Earlier passes covered all five custom scenes as stills in both aspects, plus
9:16 B00 and B01 from the live renders.

## Integrity

All 20 beat clips probed: readable, correct resolution (3840x2160 / 2160x3840),
each within one frame of its measured narration. Masters: 119.99s, h264 + AAC,
10/10 slots filled, zero slates.
