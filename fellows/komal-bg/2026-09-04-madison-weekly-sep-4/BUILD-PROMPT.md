# BUILD-PROMPT — Madison Weekly — Sep 4. (Komal · 4K + 9:16)

```
Build the claude-liam narrated weekly "Madison Weekly — Sep 4."
(slug: madison-weekly-sep-4) — creator cut for Komal.

Ground truth:
1. fellows/komal-bg/2026-09-04-madison-weekly-sep-4/beat_sheet.json
2. PEDAGOGY.md + NARRATION-GATE-P.md + FACTCHECK.md + SOURCES.md
3. brutalist.art/skills/make/ai-explainer/SKILL.md + CLAUDE-BRAND.md
4. runtime/remotion/src/scenes/MadisonWeeklySep4Illu.tsx (registered in Root.tsx)

Hard stops:
- Team videos are SOURCE only. Do not splice them into media/.
- No audio until PEDAGOGY.md shows VERDICT: PASS.
- Kokoro am_onyx only. Spoken: "Liam, in for Komal" + Madison's weekly update.
- keep_review_labels must stay false — never ship a --review cut.
- Master is 4K: ./art final --height 2160. Also render the 9:16 short.

Steps after GATE P PASS:
1. python3 runtime/scripts/generate_audio_kokoro.py <reel>
2. python3 runtime/scripts/remotion_scenes.py <reel>
3. ./art final <reel>
4. ./art shorts <reel> --handle Komal --no-endcard
5. remotion_scenes.py <reel>/short --force ; compile.py <reel>/short --height 1920
6. Visual QC. Never publish.
```
