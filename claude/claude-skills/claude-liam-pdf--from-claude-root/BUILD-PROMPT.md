# BUILD-PROMPT — claude-liam-pdf

Skill teardown reel for the Anthropic `pdf` skill.
Channel: claude-liam · Voice: Kokoro af_kore · Format: 16:9 · Modifier: skill-teardown

## What this video covers
The PDF skill is a library router: pypdf (manipulation), pdfplumber (extraction), reportlab
(creation). OCR requires a two-step pipeline: pdf2image + pytesseract. Key gotcha: never
use Unicode subscripts in reportlab — use XML markup tags instead.

## Beat map
- B00: ClaudeComposerAsk cold open — "Hola, Kore" greeting, table+merge request, skill fires
- B01: PdfAnatomy — 3 libraries mapped to domains + 4 CLI tools + 2 specialist files
- B02: PdfOperations — 8-row quick reference + OCR pipeline + reportlab gotcha callout
- B05: PdfTell — teardown: library router insight + gets-right/bites card columns
- BVDT: ClaudeVerdictArtifact — 6-line verdict
- BHTF: ClaudeComposerAsk handoff — "Your Turn" with OCR path check instructions
- BOUT: ClaudeTitleOutro — "PDF · Kore, in for Humanitarians AI"

## Build commands (run from books/)
```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  anthropics/skills/youtube/claude-liam-pdf/

python3 brutalist-art/runtime/scripts/remotion_scenes.py \
  anthropics/skills/youtube/claude-liam-pdf/

python3 brutalist-art/runtime/scripts/compile.py \
  anthropics/skills/youtube/claude-liam-pdf/
```
