# BUILD-PROMPT — factcheck-handoff
# Handoff reel. Does NOT replace the Chapter 14 videos.
# LOCAL ONLY. Do not push to GitHub until Novia signs off.

```bash
cd /Users/noviadsilva/Documents/HumanitarianAI/brutalist.art-main

python3 "/Users/noviadsilva/Documents/HumanitarianAI/Fact Checking Project/medhavi-cancer-main/youtube/factcheck-handoff/_write_sheet.py"

python3 runtime/scripts/generate_audio_kokoro.py \
  "/Users/noviadsilva/Documents/HumanitarianAI/Fact Checking Project/medhavi-cancer-main/youtube/factcheck-handoff"

ART_STRICT=0 ./art run \
  "/Users/noviadsilva/Documents/HumanitarianAI/Fact Checking Project/medhavi-cancer-main/youtube/factcheck-handoff" \
  --height 2160
```

## Key decisions
- Bella (`af_bella`). Hello Novia. `@Medhavy`.
- Source: `SOURCE.md` = `FACTCHECK_HANDOFF.md`.
- No URLs spoken. No GitHub upload in this pass.
- Manim IDs: `B09_ZeroNotSafe`, `B12_WhatIsDone`. Never the word "chapter" on a Manim slide.
