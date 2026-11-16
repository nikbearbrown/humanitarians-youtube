Gavia has a new look. Is a redesign just taste? Part of it is arithmetic.

This week on Gavia, the offline loon app: an audit of the interface against WCAG 2.2 AA and the Humanitarians AI brand found 11 issues and proposed 5 changes, built on a branch so they can be judged side by side.

The five proposed changes:
- Inter, bundled inside the app (the old fonts came from Google, and Gavia's offline security policy blocked them, so it showed a system serif)
- The Humanitarians AI palette, light and dark, with the decorative corner glow removed
- One style for the main button
- The smallest sentence text raised to 12 px
- Named file inputs and larger small targets

Contrast is a ratio: (L_light + 0.05) / (L_dark + 0.05), where L is relative luminance. WCAG asks 4.5:1 for text.
- Faintest old grey, #88979D on #F6F8F9: (0.9357 + 0.05) / (0.2980 + 0.05) ≈ 2.83:1
- New grey, #5E6265 on #FFFFFF: (1.0000 + 0.05) / (0.1205 + 0.05) ≈ 6.16:1

The automated checker, axe-core 4.10.2, on six screens (three pages, light and dark):
- Before: 6 failures (4 low contrast, 2 unnamed inputs) and 106 contrast checks it couldn't decide, because the glow hid the background
- After: 0 and 0

Status: all five changes are proposals on a branch. None ships until approved.

The screenshots come from Gavia's browser preview: the loon box and the 84% are a made-up sample, not a model run.

Try it yourself: paste your app's colour tokens into an assistant, ask which text and background pairs fall under 4.5:1, and check the worst pair by hand with the formula.

Gavia, the project in this reel: https://github.com/nikhil-kunapareddy/gavia

Chapters:
0:00 A new look, before and after
0:22 Contrast is arithmetic
0:34 What the checker saw
0:44 Verdict and your turn

Sources:
WCAG 2.2, contrast ratio and relative luminance — https://www.w3.org/TR/WCAG22/
axe-core 4.10.2 — https://github.com/dequelabs/axe-core
Gavia 0.5.0 (commit 5dd8471, the "before") — https://github.com/nikhil-kunapareddy/gavia (the redesign branch is not published yet)

Images:
App screens — Gavia's browser preview on a Mac, before and after, captured at 2x
Loon photo (inside the app screens) — Glennice Burns, Unsplash

Hosted by Sai. Voice: Kokoro am_onyx, free and local. AI-generated narration; motion graphics built with Remotion; the equations typeset locally as SVG. The audit and the proposed changes were drafted with Claude Code. Contrast and axe results were re-run locally for this video. No image was generated. No human-performed audio or video.

Gavia: https://github.com/nikhil-kunapareddy/gavia
Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: Gavia, UI redesign, design audit, accessibility, WCAG 2.2, colour contrast, axe-core, Figma, Inter, offline app, Humanitarians AI, weekly progress, Computational Skepticism

#Accessibility #UXDesign #WCAG #OpenSource #HumanitariansAI #WeeklyUpdate
