# BUILD-PROMPT — Quiet Tech. (Komal · 4K)

```
Build the claude-liam ai-explainer "Quiet Tech."
(slug: claude-liam-luxury-quiet-tech) — creator cut for Komal.

Ground truth:
1. humanitarians-youtube/claude-for-branding/youtube/claude-liam-luxury-quiet-tech/beat_sheet.json
2. PEDAGOGY.md + NARRATION-GATE-P.md + FACTCHECK.md + SOURCES.md
3. brutalist.art/skills/make/ai-explainer/SKILL.md
4. runtime/remotion/src/scenes/LuxuryAiIllu.tsx (registered in Root.tsx)

Hard stops:
- No audio until PEDAGOGY.md shows VERDICT: PASS.
- Kokoro am_onyx. Spoken sign-off: "Liam, in for Komal."
- keep_review_labels false — never ship a --review cut as the master.
- Master is 4K: ./art final defaults to --height 2160.

Steps after GATE P PASS:
1. python3 runtime/scripts/generate_audio_kokoro.py <reel>
2. python3 runtime/scripts/remotion_scenes.py <reel>
3. ./art final <reel>
4. Visual QC on frames. Never publish.
```
