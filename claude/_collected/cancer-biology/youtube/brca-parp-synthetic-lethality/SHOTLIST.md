# SHOTLIST — brca-parp-synthetic-lethality

| Beat | Type | Source | Description |
|------|------|--------|-------------|
| B00 | Remotion | NikBearBrownOpen | Intro card: "Synthetic lethality — context is everything." |
| B01 | SLATE | null | Problem card: PARP inhibitors fail most solid tumors; geometry mismatch |
| B02 | Remotion | NikBearBrownTerminalAsk | Terminal: claude BRCA/PARP research prompt |
| B03 | Remotion | NikBearBrownCodeBlock | Code: synthetic_lethality_matrix.py |
| B04 | Manim | B04_SyntheticLethality | 2x2 grid: BRCA x PARP, LETHAL cell in CRIMSON |
| B05 | Remotion | NikBearBrownTerminalAsk | Terminal: add MTAP-PRMT5 pair |
| B06 | Manim | B06_SyntheticLethality2 | Extended grid with MTAP-PRMT5 Phase 2 row |
| B07 | SLATE | null | Summary: geometric relationship defined |
| B08 | SLATE | null | Next steps: verify HR deficiency, reversion status |
| B09 | Remotion | NikBearBrownOutro | Outro card |

## Remotion beats requiring render
B00, B02, B03, B05, B09

## Manim beats requiring render
B04 (B04_SyntheticLethality), B06 (B06_SyntheticLethality2)

## Slate beats (source:null)
B01, B07, B08
