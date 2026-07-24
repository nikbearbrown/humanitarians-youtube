# BUILD-PROMPT — claude-liam-docx

## How this reel was built

Skill: `claude-explainer` · Modifier: `skill-teardown`
Brand: `claude-liam` · Voice: Kokoro `af_kore` · Engine: free/local

## Beat map

| Beat | Pattern | Content |
|---|---|---|
| B00 | ClaudeComposerAsk | Cold open — Olá Kore, docx skill fires on Word doc request |
| B01 | DocxAnatomy | Two paths + quick reference (5 task types) |
| B02 | DocxCreate | 5 critical docx-js rules (all fatal, silent wrong output) |
| B03 | DocxEdit | 3-step unpack→edit→repack + XML pitfalls |
| B05 | DocxTell | Teardown — ZIP insight callout + gets right / bites columns |
| BVDT | ClaudeVerdictArtifact | Verdict — 6 lines |
| BHTF | ClaudeComposerAsk | Handoff — prompt read aloud + what to watch for |
| BOUT | ClaudeTitleOutro | Outro — DOCX · Kore, in for Humanitarians AI |

## Custom Remotion components

- `DocxAnatomy` — anatomy/two-path overview with quick reference table
- `DocxCreate` — 5 critical docx-js rules with additional traps
- `DocxEdit` — 3-step workflow + XML pitfalls + auto-repair callout
- `DocxTell` — teardown moment with ZIP insight + gets right/bites

## Build command

```bash
cd books
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  anthropics/skills/youtube/claude-liam-docx/

python3 brutalist-art/runtime/scripts/remotion_scenes.py \
  anthropics/skills/youtube/claude-liam-docx/

python3 brutalist-art/runtime/scripts/compile.py \
  anthropics/skills/youtube/claude-liam-docx/
```
