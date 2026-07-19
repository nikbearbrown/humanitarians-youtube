# BUILD-PROMPT — claude-liam-pptx

Build a claude-explainer teardown reel for the `pptx` Anthropic skill.

## Reel folder
`anthropics/skills/youtube/claude-liam-pptx/`

## Beat sheet
`beat_sheet.json` — 7 beats (B00, B01, B02, B05, BVDT, BHTF, BOUT)

## Persona
- Liam (in for Bear), voice `am_onyx`, engine Kokoro (free)
- Greeting: "Ciao, Liam"

## Scenes
- B00 / BHTF: `ClaudeComposerAsk` (existing)
- B01: `PptxAnatomy` — 3 routing paths + 4-step QA workflow
- B02: `PptxDesign` — 5 design rules + 5 avoidances
- B05: `PptxTell` — central callout + gets-right/bites columns
- BVDT: `ClaudeVerdictArtifact` (existing)
- BOUT: `ClaudeTitleOutro` (existing)

## Build commands (from `books/`)
```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py anthropics/skills/youtube/claude-liam-pptx/
python3 brutalist-art/runtime/scripts/remotion_scenes.py anthropics/skills/youtube/claude-liam-pptx/
python3 brutalist-art/runtime/scripts/compile.py anthropics/skills/youtube/claude-liam-pptx/
```

## QC
- Extract frames from each beat MP4
- Check 8-point rubric: layout, typography, canvas fill, color, animation, text readability, brand tokens, sparkLine
- Write `_qc/REPORT.md` — VERDICT: PASS or list defects
- ffprobe final MP4 for duration and codec
