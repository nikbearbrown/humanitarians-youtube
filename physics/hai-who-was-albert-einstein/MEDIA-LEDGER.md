# MEDIA LEDGER — hai-who-was-albert-einstein

Source reel: /Users/bear/Documents/CoWork/bear-textbooks/books/physics-modern-physics/youtube/who-was-albert-einstein/
Source has: beat_sheet.json only. No media/, no mp3/, no clips/, no scenes.py.

## Classification

All beats in the source reel have no rendered media — beat_sheet.json only, no
media/*.mp4|mov|png|jpg, no manim/ output. Every beat is therefore:

**CLAUDE-GENERATED VISUAL** — visual produced from code or structured props
(Remotion component, Manim scene spec, or CARD beat rendered by compile.py slate).

No HUMAN-PROVIDED MEDIA exists in this reel. The human-media ownership rules
and SHA-256 preservation requirements do not apply to any beat.

## Beat Classification Table

| Beat ID | Act | Shot Type | Generating Scene / Component | Notes |
|---------|-----|-----------|------------------------------|-------|
| B00 | WHAT THIS IS | CARD | compile.py slate → CARD kind=header | HAI pragmatist open, no Remotion pattern needed |
| B01 | THE PROBLEM | CARD | compile.py slate → CARD kind=question | No source media |
| B02 | THE MODEL | GRAPHIC | Manim B02_Graphic (E=hf threshold scene) | Manim scene spec only; no scenes.py |
| B03 | SPECIAL RELATIVITY | GRAPHIC | Manim B04_Graphic (E=mc² bar chart scene) | Manim scene spec only; no scenes.py |
| B04 | WHERE EINSTEIN WAS WRONG | CARD | compile.py slate → CARD kind=verdict | No source media |
| B05 | DOWNSTREAM APPLICATIONS | REMOTION | ClaudeWindow (artifact view) | Reused source pattern |
| B06 | BIOGRAPHICAL FACTS | CARD | compile.py slate → CARD kind=endcard | No source media |
| B_CLI | WORKED EXAMPLE | CARD | compile.py slate → CARD kind=exercise | New HAI CLI exercise beat |
| B07 | OUTRO | REMOTION | OutroCTA | HAI brand outro |

## Manim beats (B02, B03)

No scenes.py was present in the source reel and none was copied by brand_variant.py.
These beats will compile as SLATE (request cards) until a scenes.py is provided and Manim runs.
Per the task instructions: "If not present: skip Manim."

## Human-Media Rule Status

NOT APPLICABLE — no human-provided media in source or variant.
All visual adaptation is register/palette rewrite of generated content only.
