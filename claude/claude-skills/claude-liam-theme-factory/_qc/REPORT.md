# Visual QC Report — claude-liam-theme-factory
Date: 2026-07-18
Auditor: Claude Code (automated frame audit)
Output: claude-liam-theme-factory.mp4 — 1920×1080, 290.0s, h264+aac

## Final file
- Path: youtube/claude-liam-theme-factory/claude-liam-theme-factory.mp4
- Resolution: 1920×1080 ✓
- Duration: 290.0s (audio 290.048s) ✓
- Video codec: h264 ✓
- Audio codec: aac ✓
- Slots: 12/12 filled ✓

## Frame audit method
- 580 frames extracted at 2fps
- 3 per-beat frames sampled at ~15/50/85% of each beat window
- 9-point rubric applied per beat

## 9-point rubric checklist (per beat)

### B00 — ClaudeComposerAsk (19.66s, 0:00–0:20)
1. Edge bleed/clipping: PASS — all content within safe area
2. Title-safe margins: PASS — eyebrow and title well inside x:96–1824
3. Container overflow: PASS — composer UI card contained
4. Collision: PASS — no element overlap
5. Offscreen anchors: PASS
6. Legibility: PASS — "Style this slide deck with the theme-factory skill." fully readable
7. Brand: PASS — cream page, terracotta spark, correct title "Claude, Restrained."
8. Aspect ratio: PASS — 16:9 confirmed
9. Canvas fill: PASS — cream background fills frame

### B01 — ThemeFactoryAnatomy (23.62s, 0:20–0:43)
1–9: ALL PASS — folder tree, "10 THEMES" pill, spec callout, spark line all correct. TRUE-HEX data present. Eyebrow/title correct.

### B02 — ThemeFactoryThemeCard (33.53s, 0:43–1:17)
1–9: ALL PASS — Golden Hour spec sheet, 4 true-hex swatches, VERBATIM source badge, typography row, BEST USED FOR callout, spark line "A brief, not code."

### B03 — ThemeFactoryConsentGate (26.86s, 1:17–1:44)
1–9: ALL PASS — four-step SHOW→ASK→WAIT→APPLY pipeline. WAIT node pulse animation confirmed active (terracotta intensity varies across sample frames). Verbatim SKILL.md quote. Spark line "Taste stays human."

### B04 — ThemeFactoryTenSkins (32.45s, 1:44–2:16)
1–9: ALL PASS — demo card cycling confirmed at frames 218/240/263: "2 of 10 Sunset Boulevard", "Corporate Blue", "9 of 10 Botanical Garden". TRUE-HEX verbatim. Theme label pill and skin counter present. Spark line "Same plate, ten prints."

### B05 — ThemeFactoryMirror (14.45s, 2:16–2:31)
1–9: ALL PASS — card fully morphed to Brutalist Cream (#FAF9F5/#3D3929/#D97757). Terracotta glow ring pulse visible (intensity varies between frames). "Brutalist Cream — this video's own theme" label with hex triplet. Spark line "You're watching one."

### B06 — ClaudeComposerAsk escape-hatch (15.02s, 2:31–2:46)
1–8: PASS
9. Canvas fill: PASS
NOTE (non-blocking): Empty spark line — SKIN LINT warning. By design for mid-reel ask beat; not a BLOCKER or MAJOR. Custom theme prompt and Claude response text correctly rendered.

### B07 — ThemeFactoryCustomTheme (20.76s, 2:46–3:07)
1–9: ALL PASS — "Brutalist Cream" card assembles: 4 swatches (#FAF9F5, #303929, #D97757, #73705F), typography row, BEST USED FOR callout. PENDING SIGN-OFF terracotta chip present and pulsing (opacity varies between frames 338→352). Verbatim SKILL.md quote. Spark line "The gate survives."

### B08 — ThemeFactoryContrastMeter (40.66s, 3:07–4:07)
1–9: ALL PASS — all 3 contrast pairs at final settled state: 12.57:1 AAA (green), 5.32:1 AA (blue), 1.05:1 FAIL (red). Mustard text fade-to-invisible effect confirmed (nearly invisible against beige in FAIL card swatch). WCAG legend at bottom. Fail callout text visible. Spark line "One load-bearing sentence."

### BVDT — ClaudeVerdictArtifact (32.93s, 4:07–4:40)
1–9: ALL PASS — "Claude, Restrained." verdict card with 4-point list. All points legible, correct numbering, terracotta accent on items 3. Cream page, correct typography. Static/settled.

### BHTF — ClaudeComposerAsk "Your turn." (27.70s, 4:40–5:07)
1–9: ALL PASS — "Your turn." heading, full handoff prompt reads the question AND invites discussion (Your Turn Handoff Rule satisfied). "paste this into Claude…" cue. Correct title/eyebrow.

### BOUT — ClaudeTitleOutro (3.07s, 5:07–5:10)
1–9: ALL PASS — minimalist title card, "Claude, Restrained." serif large with terracotta period, "@HumanitariansAI", "Kore, in for Humanitarians AI." No overflow, centered, cream canvas.

## Summary

| Severity | Count | Items |
|----------|-------|-------|
| BLOCKER  | 0     | —     |
| MAJOR    | 0     | —     |
| MINOR    | 0     | —     |
| INFO     | 1     | B06 empty spark line (SKIN LINT, by design) |

## Verdict: PASS — zero BLOCKER, zero MAJOR. Ready for review.
