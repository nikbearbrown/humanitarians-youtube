# BUILD-PROMPT — Madison Weekly — Scope Locked. (Komal · 4K)

```
Build the claude-liam narrated weekly "Madison Weekly — Scope Locked."
(slug: madison-weekly-scope-cvat) — creator cut for Komal.

Ground truth:
1. loon-book/youtube/madison-weekly-scope-cvat/beat_sheet.json
2. PEDAGOGY.md + NARRATION-GATE-P.md + FACTCHECK.md + SOURCES.md
3. brutalist.art/skills/make/ai-explainer/SKILL.md + CLAUDE-BRAND.md
4. 9:16 companion: short/beat_sheet.json

Hard stops:
- No audio until PEDAGOGY.md shows VERDICT: PASS.
- Kokoro am_onyx only. Spoken sign-off: "Liam, in for Komal."
- keep_review_labels must stay false — never ship a --review cut as the master
  (review burns B00/B01… chips bottom-left).
- Master is 4K: Remotion already uses --scale=2; compile with --height 2160
  (./art final defaults to this). Also render the 9:16 short.

Steps after GATE P PASS:
1. python3 runtime/scripts/generate_audio_kokoro.py <reel>
2. python3 runtime/scripts/remotion_scenes.py <reel>
3. ./art run <reel>          # optional previz; do not treat as master
4. ./art final <reel>        # clean 4K master → <slug>-cut.mp4 (height 2160)
5. Visual QC LAW on frames; fix; re-render. Never publish.
```
