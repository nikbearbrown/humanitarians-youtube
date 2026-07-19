# Branding and AI — 9:16 Short Batch Summary
**Date:** 2026-07-18  
**Pipeline:** Free only (Kokoro TTS, no ElevenLabs, no higgsfield)  
**Constraint:** No publishing, no uploading, no git commit

## All 12 Short Cuts — COMPLETE

| Slug | Duration | Cap OK |
|---|---|---|
| archetype-drift-case-studies | 153.8s | ✓ |
| boondoggle-score-calculator | 146.8s | ✓ |
| brand-archetype-classifier | 174.6s | ✓ |
| brand-attribution-problem | 150.5s | ✓ |
| brand-metrics-performance-dashboard | 153.0s | ✓ |
| brand-signal-collapse-detector | 164.8s | ✓ |
| brand-voice-consistency-auditor | 150.7s | ✓ |
| creative-engineer-market-repricing | 161.7s | ✓ |
| four-verb-career-signal-audit | 144.8s | ✓ |
| madison-multi-agent-architecture-mapper | 156.1s | ✓ |
| pipeline-contract-resilience-audit | 149.2s | ✓ |
| self-as-project-brand-runner | 151.3s | ✓ |

All 12 under 175s headroom. Hard cap 180s — all clear.

## Portrait Layout Fixes Applied

Seven BrandB01* Remotion components required portrait fixes before 916 compile:

| Component | Fix applied |
|---|---|
| BrandB01SignalCollapse | title/subtitle/footer min(w,h), CHART_Y/H isPortrait, annotation maxWidth, removed whiteSpace:nowrap |
| BrandB01VoiceConflict | title/subtitle/footer min(w,h), CONTENT_TOP isPortrait |
| BrandB01PipelineGap | title/footer min(w,h), FLOW_START_Y/BOX_H isPortrait, column header tops isPortrait |
| BrandB01AttributionConfusion | title/subtitle/footer min(w,h), CHART_Y/H_PX isPortrait |
| BrandB01DualTrack | title/footer min(w,h), CHART_H/TOP_Y isPortrait, subtitle top isPortrait |
| BrandB01RepricingGap | title/footer min(w,h), CHART_Y/H isPortrait, subtitle fontSizes min(w,h) |
| BrandB01SeamFailure | title/footer min(w,h) |

**Universal fix pattern:** `Math.round(height * 0.0XX)` → `Math.round(Math.min(width, height) * 0.0XX)`  
This resolves portrait overflow (1920px height scale) without breaking landscape (min-dimension = height = 1080 either way).

## Output Locations

Each short cut is at:
```
branding-and-ai/youtube/<slug>/short/<slug>-short.mp4
```

## Next Step (human decision)

Flip each short from Unlisted → Public in YouTube Studio.  
Channel: @NikBearBrown · Playlist: "Branding and AI"
