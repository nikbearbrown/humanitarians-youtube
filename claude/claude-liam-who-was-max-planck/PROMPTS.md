# PROMPTS — Who was Max Planck? (claude-liam)

Beat-prefixed prompts for open slots. All beats are machine-buildable;
no human-drop required for first cut.

## B02 — E = hν Manim scene
```
Render B02_Graphic from scenes.py:
  manim -qh --fps 24 -r "1920,1080" scenes.py B02_Graphic
Output slotted to: manim/B02.mp4
Scene: E = hν equation on cream (#FAF9F5) canvas, terracotta (#D97757) energy ladder,
ink (#3D3929) labels. Animates: Write(eq) → FadeIn(definitions) → FadeIn(ladder) → FadeIn(footer).
```

## B04 — Planck vs Rayleigh-Jeans Manim scene
```
Render B04_Graphic from scenes.py:
  manim -qh --fps 24 -r "1920,1080" scenes.py B04_Graphic
Output slotted to: manim/B04.mp4
Scene: spectral radiance vs wavelength for 5000K blackbody.
Planck curve (terracotta, peaks ~580nm, falls correctly).
Rayleigh-Jeans (slate gray, diverges at short λ, clipped at y=3.2 with upward arrow).
"Ultraviolet Catastrophe" annotation. Animates: axes → Create(RJ) → labels → Create(Planck) → Planck label.
```

## B00, B03, B06, B08, B09 — Remotion renders
```
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
  physics-modern-physics/youtube/claude-liam-who-was-max-planck
Renders: ClaudeComposerAsk (B00, B03, B08), ClaudeWindow (B06), ClaudeTitleOutro (B09)
All props are set in beat_sheet.json → shot.remotion.props
```
