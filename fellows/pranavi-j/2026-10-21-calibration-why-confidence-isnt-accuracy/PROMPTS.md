# PROMPTS — Calibration: Why Confidence Isn't Accuracy

## Status: no pantry assets needed — all Manim

All 9 beats are self-contained Manim scenes in `scenes.py` (landscape) and `vertical/scenes.py`
(the native-portrait companion) — no vox stills, no Remotion components, no generated/photographic
images. There is no pantry shopping list for this reel (see `beat_sheet.json`'s
`metadata.gates.shopping_list`: "N/A — all beats are self-contained Manim scenes (scenes.py); no
pantry stills or Remotion assets needed"). This file is kept as the required paperwork-set
placeholder (GATE F) and as a record that no image-generation prompts were ever needed, for either
the landscape master or the vertical companion.

Every on-screen artifact — the two same-confidence answer cards (B02), the 3-test checklist card
(B03), the confidence-bucket chip rows and stated-vs-actual bar pairs (B04/B05), the audit
checklist (B06), and the takeaway/brand cards — is authored directly as Manim
`Text`/`Rectangle`/`Square`/`Line`/`RoundedRectangle` mobjects. Per FACTCHECK.md and SOURCES.md,
this is a general AI/STEM topic explainer: model calibration itself is a well-documented, generic
property of predictive models, and the worked example (a generic "~90% confident" answer bucket)
and its falsifiability case are both fully original, illustrative scenarios with round numbers
chosen for teaching clarity — no real model, vendor, or disclosed benchmark is named, resembled, or
quoted for a specific statistic. No image generation or external source lookup was needed or used.
