# SHOTLIST — Tokenization: Why AI Can't Count the Letters in Its Own Words
## Total: 121.036s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.056s | Silent title card: "Tokenization: Why AI Can't Count the Letters in Its Own Words" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 14.09s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_TwoTasksHook (scenes.py) | 13.70s | Two task cards side by side: "Count letters" (often wrong) vs "Write an essay" (reliable) |
| B03 | MECHANISM | manim | GRAPHIC | B03_TokenSplitDiagram (scenes.py) | 21.46s | The illustrative word "strawberry" visibly split into 3 colored token chunks (STRAW / BER / RY), caption "model sees these chunks — not the letters inside" |
| B04 | WORKED-EXAMPLE | manim | GRAPHIC | B04_MiscountedTally (scenes.py) | 18.05s | Same 3-chunk split, per-chunk tally of letter R, model's miscounted total (2) vs the true count (3), mismatch (≠) visible |
| B05 | FALSIFIABILITY | manim | GRAPHIC | B05_SpelledOutFix (scenes.py) | 17.88s | Same word spelled letter-by-letter (S-T-R-A-W-B-E-R-R-Y), each letter its own token, count now matches the true total (3), green checkmark |
| B06 | SCAFFOLDED-TASK | manim | GRAPHIC | B06_AuditChecklist (scenes.py) | 18.55s | The 3-question rubric as a checklist card: whole-word task? / needs character-level detail? / would spelling it out help? |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 11.74s | Statement card: fluent writing and letter-counting failure aren't contradictory — same system, wrong resolution |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." |

## Illustrative word choice (per FACTCHECK.md — generic, no real model named/benchmarked)

"strawberry", counting the letter "R" — long enough to plausibly BPE-split into 3 sub-word
chunks, has a repeated letter worth counting (3 R's), and mirrors the well-known "how many R's"
class of example BEAT-SHEET.md references, without naming or benchmarking any specific real
model. The SAME word and SAME 3-chunk split (STRAW / BER / RY) are reused across B03/B04/B05 per
the Legibility Contract ("not a different, easier word" for the falsifiability case).

- True letter-level R count: 1 (straw) + 1 (ber) + 1 (ry) = 3
- Illustrative miscounted tally (B04): STRAW->1, BER->1, RY->0 (model treats "RY" as one opaque
  chunk and misses the R inside it) = 2 ≠ 3
- Spelled-out fix (B05): S-T-R-A-W-B-E-R-R-Y, each letter its own token, count = 3, matches truth

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No pantry stills, no
  Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`, plus a new
  `token_chunk()` idiom specific to this reel's word-splitting beats) copied from this fellow's
  closest siblings `2026-09-29-the-keyword-that-cried-wolf` and
  `2026-09-22-the-all-clear-that-wasnt-all-there` for house-style consistency.
- B03/B04/B05 are this reel's most legibility-critical beats: the SAME word and SAME token split
  must read as the same visual object across all three, so the falsifiability case (B05) reads as
  a genuine resolution of B04's mismatch, not a different example.
- B06 restates the 3-question rubric as a concrete checklist, not a repeat of B03's mechanism
  diagram.

## Vertical companion
`vertical/scenes.py` documents the native-portrait redesign of all 9 beats built via
`./art vertical` — side-by-side layouts (B02's two task cards, B04's chunk-row-plus-tally-boxes)
are restacked top-to-bottom for the narrow canvas.

## QC status
See `BUILD-LOG.md` for GATE A/W/V results and per-beat visual-inspection findings.
