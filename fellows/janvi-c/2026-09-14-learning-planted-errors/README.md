# Planting Errors to Test a Checker — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** learning video (STEM/AI concept) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:24 (9 beats) · **Destination:** `fellows/janvi-c/2026-09-14-learning-planted-errors/`

## This week's contribution

- **Question:** How do you measure how well a checker catches mistakes when nobody has an answer key?
- **What I built/tried:** I explain the planted-error method with my sensitivity_test.py: 200 approved definitions, 150 corrupted on purpose (30 each of conflation, wrong expansion, disambiguation list, factual error and wrong field), 50 kept as controls, all scored blind.
- **Observed result:** The method gives three measures: caught, slipped through, and controls wrongly flagged (the false positive rate). Our two-judge run: 30.0%, 18.7% and 0.0%. You only learn about the kinds of errors you planted.

## Human and AI work

**My decisions, implementation and verification:** The test design, the corruption types and the analysis are mine. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Mistral and GPT-4o-mini scored the test set.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: relying on author judgment for ground truth.

**What remains unverified or failed:** This run used two judges only (Claude was not available for it); the planted errors cover five types, not every real mistake.

**Known toolkit issues hit:** ./setup stops at its ElevenLabs guard because of files under youtube/; worked around without editing tracked files. faster-whisper needed PyAV < 16.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `a187fab76609eef27f0652433b066d14caba6940` (2026-10-21), checked 2026-10-28.
- **Beat sheet:** `beat_sheet.json` (16:9 landscape, 3840×2160).
- **Custom scene code:** `scenes.py`. It loads logo SVGs from `assets/logos/` (humanitarians); those assets are kept locally by Janvi and are not in this repo.
- **Not in this repo:** rendered media and build paperwork (fact-check, shot list, prompts, transcript), kept locally by Janvi and available on request.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/janvi-c/2026-09-14-learning-planted-errors
python3 runtime/scripts/generate_audio_kokoro.py $REEL
python3 runtime/scripts/align.py $REEL
ART_PALETTE=humanitarians ./art run   $REEL
ART_PALETTE=humanitarians ./art final $REEL --height 2160 --out <landscape-folder>
```

Rendered media (`mp3/`, `media/`, `clips/`, MP4s, QC frames) are produced locally and are not checked into this repo.

**Approvals and checks:** narration approved and fact-check confirmed by Janvi on 2026-10-27. Landscape export passed the toolkit's final gates (GATE T type check, frame checks) with receipt status: `ready`.

## Watch and review

| Version | Drive link | Resolution | Duration | SHA-256 |
|---|---|---|---|---|
| Video | [Watch on Drive](https://drive.google.com/file/d/1vsYg8zG-h2ubt6PaBHqsrv3urT_yM7GL/view?usp=drivesdk) | 3840×2160 | 1:24 | `4224835b817109c0f0b848c239bcaf732f499e0a08694113a194cd646f9c72bb` |

Drive filename: `learning_PlantingErrorsToTestAChecker_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_07_Sep14_Sep20)
