# BUILD-PROMPT — chapter14-json-fix
# Video 2 of Chapter 14. Does NOT replace chapter14-second-read.

## Standalone rebuild

```bash
cd /Users/noviadsilva/Documents/HumanitarianAI/brutalist.art-main

python3 "/Users/noviadsilva/Documents/HumanitarianAI/Fact Checking Project/medhavi-cancer-main/youtube/chapter14-json-fix/_write_sheet.py"

python3 runtime/scripts/generate_audio_kokoro.py \
  "/Users/noviadsilva/Documents/HumanitarianAI/Fact Checking Project/medhavi-cancer-main/youtube/chapter14-json-fix"

ART_STRICT=0 ./art run \
  "/Users/noviadsilva/Documents/HumanitarianAI/Fact Checking Project/medhavi-cancer-main/youtube/chapter14-json-fix" \
  --height 1080

./art shorts \
  "/Users/noviadsilva/Documents/HumanitarianAI/Fact Checking Project/medhavi-cancer-main/youtube/chapter14-json-fix" \
  --handle @Medhavy
```

## Key decisions
- **Video 2.** Weekly update for the professor. Video 1 stays: `youtube/chapter14-second-read/`.
- Clock **3:00–3:20**. Bella (`af_bella`). Hello Novia. `@Medhavy`.
- Spine from SOURCE.md §4: why the row broke → why other rows → JSON `evidence[]`.
- Interactive: three mid-reel questions (B03, B07, B14), each answered on the next beat.
