# QC REPORT — claude-liam-brand-guidelines

**Date:** 2026-07-18  
**Compiled MP4:** `../claude-liam-brand-guidelines.mp4`  
**Duration:** 3:05 (185.1s) — target ~3:00 ✓  
**Video:** 1280×720 @ 24fps  
**Audio:** AAC 24000Hz mono ✓  
**Frames sampled:** 370 at 2fps + beats at ~15/50/85%  

---

## 9-Point Rubric

| Check | Result |
|---|---|
| Edge bleed / clipping | PASS — no content touches frame edge |
| Title-safe margins | PASS — eyebrows clear top margin; spark lines clear bottom |
| Container overflow | PASS — all cards fit within their bounds |
| Element collision | PASS — no overlapping text or cards |
| Offscreen anchors | PASS — all nodes/cards fully visible |
| Legibility | PASS — all body text readable at render size |
| Brand / palette | PASS — cream PAGE, terracotta SPARK, correct INK tones throughout |
| Aspect ratio | PASS — 16:9 at 1280×720 |
| Canvas fill | PASS (see per-beat notes) |

---

## Per-Beat Results

| Beat | Pattern | Canvas Fill | Result | Notes |
|---|---|---|---|---|
| B00 | ClaudeComposerAsk | Good | PASS | "Hola, Kore" greeting; command + 3 output lines visible; @HumanitariansAI label |
| B01 | BrandGuidelinesAnatomy | Good | PASS | Folder tree left, 3 spec cards right, quote box, spark line; content ~13–66% height |
| B02 | BrandGuidelinesPipeline | Good | PASS | 3 nodes centered at H/2, orange+gray arcs, insight bar bottom, spark line |
| B03 | BrandGuidelinesPalette | Good | PASS | SELF-DEMO: exact hex values from SKILL.md as live swatches; 4 main + 3 accents |
| B04 | BrandGuidelinesTypography | Good | PASS | SELF-DEMO: Poppins/Lora specimens, 24pt threshold badge, fallback chain bar |
| B05 | BrandGuidelinesDesignTell | Acceptable | PASS | Central callout + ✓/✗ columns; lower 40% open but spark line anchors |
| BVDT | ClaudeVerdictArtifact | Acceptable | PASS | Correct props: "Claude, Branded." + 5 lines; card centered per component design |
| BHTF | ClaudeComposerAsk | Good | PASS | "Your turn." + full handoff prompt readable in composer |
| BOUT | ClaudeTitleOutro | Good | PASS | "Claude, Branded." · @HumanitariansAI · brand-guidelines · Anthropic Skills |

---

## Defects Fixed During Build

| Defect | Severity | Fix |
|---|---|---|
| BVDT props wrong (title/subtitle/verdict/lines) | BLOCKER | Read ClaudeVerdictArtifact schema; corrected to artifactTitle/artifactHeading/artifactLines in beat_sheet.json |
| B01 BrandGuidelinesAnatomy canvas fill | MAJOR | Rewrote scene: content start H*0.21, larger fonts, bigger cards, added bottom quote box |
| B02 BrandGuidelinesPipeline canvas fill | MAJOR | Rewrote scene: nodes centered at H*0.50, GAP = (W - 3*NODE_W)/4, percentage-based layout |

---

## VERDICT: PASS

Zero BLOCKER defects. Zero MAJOR defects. Two MINOR (B05/BVDT lower-canvas open area) — within acceptable tolerance for their beat types.
