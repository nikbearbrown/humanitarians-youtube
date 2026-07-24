# QC Report — claude-liam-algorithmic-art

**Final video**: `claude-liam-algorithmic-art.mp4`  
**Spec**: 1920×1080, 30fps, 304.8s (9143 frames)  
**Audit date**: 2026-07-17  
**Method**: ffmpeg -vf fps=2 → 610 sample frames, read at key beats

---

## 8-Point Rubric

| Check | Result |
|-------|--------|
| Edge bleed / clipping | PASS — all content within safe area |
| Title-safe margins | PASS — eyebrows at 7% inset; elements clear screen edge |
| Container overflow | PASS — viewer card and grid tiles all contained |
| Element collision | PASS — no overlap between plaque, spark line, citation |
| Offscreen anchors | PASS — no elements anchored off-screen |
| Legibility | PASS — serif 26–40px at 1080p reads cleanly |
| Brand / palette | PASS — cream #FAF9F5, ink #3D3929, terracotta #D97757 only |
| Aspect ratio | PASS — 16:9 (1920×1080) confirmed |

---

## Beat-Level Findings

### B00 — ClaudeComposerAsk (cold open)
PASS. Title "Claude, Seeded." and eyebrow visible. @HumanitariansAI chip. Fade-in
correct.

### B01 — AlgArtPipeline
PASS. Three-node flow diagram centered, terracotta arrow, detail chips below nodes.
"The handoff is the invention." spark line.

### B02 — AlgArtOrganicTurbulence
**FIXED** — wrap artifact (vertical edge lines) was present in first compile.
Cause: particle trails crossing toroidal boundary drew a continuous SVG path
across the canvas. Fix: break path (M instead of L) when consecutive points jump
>W/2 or >H/2. After fix: clean curling trails, correct terracotta hot particles,
"ORGANIC TURBULENCE · SEED 42" name card visible.

### B03 — AlgArtMovementGallery
**FIXED** — FieldDynamics vignette showed severe grid-line artifacts (same root
cause as B02). After fix: four vignettes all render cleanly:
- QuantumHarmonics: dot grid with phase oscillation
- RecursiveWhispers: golden-ratio branching tree from bottom center
- FieldDynamics: edge-born particle trails, no wrap artifacts
- StochasticCrystallization: Voronoi cell revelation

### B04 — AlgArtHiddenSeed
PASS. φ annotation ring visible at ~38% 45%. Jazz quote at bottom left. Flow
field running cleanly (seed 256). "Only those who know." spark line.

### B05 — ClaudeCodeBeat
PASS. Code block with Art Blocks seed pattern. B05 runs at 2.11× slow rate
(10s composition fills 21.2s audio) — acceptable, code beat is static.

### B06 — AlgArtSeedGrid
**FIXED** — wrap artifacts in TileViz trails. After fix: 3×3 grid clean, seed 42
terracotta ring correct, "a series of prints from the same plate" caption visible.

### B07 — AlgArtFixedVariable
**FIXED** — wrap artifact in SystemA flow field canvas. After fix: clean particle
trails in canvas, FIXED sidebar intact, VARIABLE label on canvas, "Fixed outside.
Free inside." spark line.

### B08 — AlgArtQualityDial
PASS. Four phrases stacking with terracotta tick counters. Caveat text appears
after all phrases. "Framing the register." spark line.

### BVDT — ClaudeVerdictArtifact
PASS. Four numbered verdict points. "What the skill actually does" heading.
BVDT runs at 2.96× slow rate (12s composition fills 35.7s audio) — notable;
the card is static text so the slowdown is invisible.

### BHTF — ClaudeComposerAsk (your turn)
PASS. "Your turn." greeting. Full prompt visible in composer box. "@HumanitariansAI"
chip. "paste this into Claude…" running text. BHTF runs at 1.71× slow rate
(15s composition fills 25.8s audio) — acceptable.

### BOUT — ClaudeTitleOutro
PASS. "Claude, Seeded." title restate, "@HumanitariansAI" handle, "Kore, in for Humanitarians AI."
subline. 2.75s — clips from 6.1s composition.

---

## Defects Fixed

| Beat | Defect | Root Cause | Fix |
|------|--------|------------|-----|
| B02 | Wrap artifact — vertical edge lines in flow field | SVG path L across toroidal boundary | Path break (M) when point jump >W/2 or H/2 |
| B03 | Grid-line artifacts in FieldDynamics vignette | Same root cause | Same fix applied to FieldDynamics path builder |
| B06 | Wrap artifacts in seed grid TileViz | Same root cause | Same fix in TileViz path builder |
| B07 | Wrap artifacts in SystemA canvas | Same root cause | Same fix in SystemA path builder |
| ALL | Resolution 1280×720/24fps instead of 1920×1080/30fps | compile.py defaults to 720p/24fps | Recompile with --height 1080 --fps 30 |

---

## Residual Warnings (non-blocking)

- **100% Remotion**: All 12 beats are Remotion scenes. compile.py warns about the
  ~40% pantry cap. Intentional: this video's subject IS generative Remotion art;
  every beat is a living figure. No fix needed.
- **BVDT slow rate 2.96×**: Composition is 12s; audio is 35.7s. The card is static
  text — slowdown is invisible. To fix: increase BVDT composition durationInFrames
  to ≥1080 (36s at 30fps) in Root.tsx and re-render. Acceptable for review cut.
