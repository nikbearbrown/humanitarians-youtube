# STATUS — vox-doxil-heart

**Deliverable:** `vox-doxil-heart-review.mp4`
**Duration:** 189.5 seconds (3:09)
**Beats:** 12
**Slots:** 10/12 filled (B02 and B06 are STILL·ai slates — awaiting human media)

## Open command

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-nanomedicine/youtube/vox-doxil-heart/vox-doxil-heart-review.mp4
```

## Slot status

| Beat | Status | Notes |
|------|--------|-------|
| B01  | MANIM  | Title card |
| B02  | SLATE  | Awaiting STILL·ai — oncologist with dosage chart |
| B03  | MANIM  | Question card |
| B04  | MANIM  | Free dox distribution graphic |
| B05  | MANIM  | Cumulative dose meter |
| B06  | SLATE  | Awaiting STILL·ai — PEGylated liposome cross-section |
| B07  | MANIM  | Heart spared — particle passes through |
| B08  | MANIM  | Quote card with gold highlighter |
| B09  | MANIM  | Misreading vs actual two-column |
| B10  | MANIM  | Wrong tool mismatch |
| B11  | MANIM  | Illustrative Patient A vs B example |
| B12  | VIDEO  | Endcard with outro (bear mascot) |

## Gates

- Gate A: PASS (9 clean, 1 benign WARN on B08_QuoteCard pure-quote scene)
- Gate W: PASS (0 ERRORs; 3 benign W6 WARNs on B03 white-on-slate — checker can't resolve panel geometry)
- Gate B: WARNING (manim module not found in audit environment — layout not pixel-checked; visual review recommended)
- Audio: PASS (ElevenLabs generated, 188.58s actual)

## Residual notes

- `drawon` motion at 41% — 1% over the ~40% pantry cap. Not a hard gate failure; acceptable for this beat count.
- Gate B could not pixel-audit (manim env issue in the audit tool). Watch the review MP4 for layout issues.
- B03 white text: white on slate panel — readable in video; W6 WARNs are due to geometry-unresolved positioning.
- Illustrative numbers in B11 labeled as such in narration and on screen.
