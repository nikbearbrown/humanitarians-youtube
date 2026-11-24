# VISUAL-PLAN — Week 15: Reading the Student

4K 16:9 (3840×2160 at scale=2 from 1920×1080). Two-skin palette: claude skin on UI beats (B00/B09); humanitarians tokens on body beats (B01–B08). Accent roles: **CRIMSON = recall misses / paraphrase gap, TEAL = never-guessed / precision, SLATE = fields / scale, GOLD = the recall-ceiling finding, SAGE = the LLM fix.**

| Beat | Component | Visual |
|------|-----------|--------|
| B00 | ClaudeComposerAsk | composer ask + folder summary (shared claude scene) |
| B01 | W15Guarantees | two cards (never guess = teal, never miss = gold) + shared-vocab rule band |
| B02 | W15Backends | two cards (rule-based = slate, LLM = sage) + "one interface" rule band |
| B03 | W15TheTest | gold-standard column (6 projects) + metrics column (precision/recall/F1/audit) |
| B04 | W15Concrete | big 1.0 badge + 4 field rows (materials/techniques/assays/disease) with tp counts |
| B05 | W15RecallCeiling | per-field recall bar chart (4 teal at 1.0, 2 crimson short) + 3 paraphrase chips |
| B06 | W15NeverGuessed | 3 stat tiles (0 invented / 67/67 grounded / 4 empty) + big 0.97 precision |
| B07 | W15Polysemy | 2 crimson cards ("cell cycle regulation" / "tissue organization") with surface forms |
| B08 | W15ParserBoundary | two columns THE FIX (sage) / THE LIMITS (crimson) + falsifiability stamp |
| B09 | ClaudeTitleOutro | title restate + handle + sign-off (shared claude scene) |

Shared helper block identical to Week14Reorder.tsx (clamp/remap/ease/useP/accentOf/onAccent/Spark/SparkLine/CornerBug/Check/Cross). CW=1920, CH=1080, SAFE=100. Each body beat: SparkLine top, CornerBug bottom-right. durationInFrames = round(actual_duration_s × 30) after audio measured.
