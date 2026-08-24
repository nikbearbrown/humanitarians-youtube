# BUILD-PROMPT — What's Komal Building? (Loon Conservatory, Week 1)

```
Build the fellows-report sandwich "What's Komal Building? — Loon Conservatory, Week 1"
(slug: weekly-report) — house framing for Komal.

Ground truth:
1. loon-book/youtube/weekly-report/beat_sheet.json
2. PEDAGOGY.md + NARRATION-GATE-P.md + FACTCHECK.md + SOURCES.md
3. brutalist.art/skills/make/ai-explainer/SKILL.md + CLAUDE-BRAND.md

Hard stops:
- No house audio until PEDAGOGY.md shows VERDICT: PASS.
- Kokoro af_bella only on B00–B03, B05–B06.
- B04 is the fellow's unedited report: own video + own audio. No Kokoro.
- Advisor-notes beats stay omitted (mentors provide those separately).
- Review cut is 1080p. Do not treat a --review cut as a publishable master.

Steps after GATE P PASS:
1. Restore pantry/report-raw.mp4 as media/B04.mp4
2. Extract its audio to mp3/beat-B04.mp3
3. python3 runtime/scripts/generate_audio_kokoro.py <reel> --only B00 B01 B02 B03 B05 B06
4. python3 runtime/scripts/remotion_scenes.py <reel>
5. python3 runtime/scripts/compile.py <reel> --review --height 1080
6. Visual QC on the contact sheet; fix; re-render. Never publish.
```
