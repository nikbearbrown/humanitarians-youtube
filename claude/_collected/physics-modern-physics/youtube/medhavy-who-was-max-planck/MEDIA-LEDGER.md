# MEDIA LEDGER — medhavy-who-was-max-planck

Generated: 2026-07-16 (repaired build — replaced wrong MedhavyCard structure)
Canonical source: claude-liam-who-was-max-planck/

## Canonical source

All Manim renders and Remotion renders are derived from:
  /Users/bear/Documents/CoWork/bear-textbooks/books/physics-modern-physics/youtube/claude-liam-who-was-max-planck/

The canonical source is read-only. This variant does not modify it.

## Beat Classification Table

| Beat ID | Type | Source | Asset path | Notes |
|---------|------|--------|-----------|-------|
| B00 | REMOTION render | New render (variant) | media/B00.mp4 | ClaudeComposerAsk, greeting "Hallo, Medhavy", folderLabel "@Medhavy" |
| B01 | CARD/SLATE | None — slate | (slate in clips/) | CARD beat, pending gen-AI clip from human |
| B02 | MANIM | Copied from canonical | manim/B02.mp4 | E=hν energy ladder — claude-liam-who-was-max-planck/manim/B02.mp4 |
| B03 | REMOTION render | New render (variant) | media/B03.mp4 | ClaudeComposerAsk, folderLabel "@Medhavy" |
| B04 | MANIM | Copied from canonical | manim/B04.mp4 | Planck vs Rayleigh-Jeans spectral plot — claude-liam-who-was-max-planck/manim/B04.mp4 |
| B05 | CARD/SLATE | None — slate | (slate in clips/) | CARD beat, pending gen-AI clip from human |
| B06 | REMOTION render | New render (variant) | media/B06.mp4 | ClaudeWindow, quantum century timeline |
| B07 | CARD/SLATE | None — slate | (slate in clips/) | CARD beat, pending gen-AI clip from human |
| B08 | REMOTION render | New render (variant) | media/B08.mp4 | ClaudeComposerAsk, greeting "Your turn.", folderLabel "@Medhavy" |
| B09 | REMOTION render | New render (variant) | media/B09.mp4 | ClaudeTitleOutro, handle "@Medhavy" |

## SHA-256 of copied Manim assets

To verify provenance, run:
  shasum -a 256 manim/B02.mp4 manim/B04.mp4
  shasum -a 256 ../claude-liam-who-was-max-planck/manim/B02.mp4 ../claude-liam-who-was-max-planck/manim/B04.mp4

## Human-provided media (pending)

B01, B05, B07 are CARD/SLATE beats. Drop gen-AI clips into pantry/ as B01.mp4, B05.mp4, B07.mp4
and re-run compile.py to upgrade them from slates to VIDEO slots.

## Repairs made

Previous build used MedhavyOpen (B00), MedhavyConceptCard (B01–B06), MedhavyOutro (B07) —
8 beats, no Manim simulations, no Claude UI beats. Replaced with correct 10-beat Claude-explainer
structure matching claude-liam-who-was-max-planck. Manim files copied from canonical.
Remotion beats re-rendered with Medhavy persona (greeting, folderLabel). Audio regenerated
with af_kore voice in Wonder register narration.
