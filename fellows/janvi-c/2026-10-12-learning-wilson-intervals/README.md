# Confidence Intervals for Small Tests — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** learning video (STEM/AI concept) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:32 (9 beats) · **Destination:** `fellows/janvi-c/2026-10-12-learning-wilson-intervals/`

## This week's contribution

- **Question:** How much could a percentage from a 150-item test move?
- **What I built/tried:** I computed four new Wilson 95% confidence intervals for Table 3, in the paper's data workbook.
- **Observed result:** Claude detection 94.3%–99.3%; Mistral 60.9%–75.5%; GPT-4o-mini 56.1%–71.2%; pass-through 15.0%–27.8%.

## Human and AI work

**My decisions, implementation and verification:** The interval computations and the workbook are mine. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-28 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-28.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: reporting single percentages without a range.

**What remains unverified or failed:** An interval covers sample-size uncertainty only, not bias or errors that were never planted. No formula is shown on screen.

**Known toolkit issues hit:** ./setup stops at its ElevenLabs guard because of files under youtube/; worked around without editing tracked files. faster-whisper needed PyAV < 16.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `a187fab76609eef27f0652433b066d14caba6940` (2026-10-21), checked 2026-10-28.
- **Beat sheet:** `beat_sheet.json` (16:9 landscape, 3840×2160).
- **Custom scene code:** `scenes.py`. It loads logo SVGs from `assets/logos/` (claude, humanitarians, mistral, openai); those assets are kept locally by Janvi and are not in this repo.
- **Not in this repo:** rendered media and build paperwork (fact-check, shot list, prompts, transcript), kept locally by Janvi and available on request.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/janvi-c/2026-10-12-learning-wilson-intervals
python3 runtime/scripts/generate_audio_kokoro.py $REEL
python3 runtime/scripts/align.py $REEL
ART_PALETTE=humanitarians ./art run   $REEL
ART_PALETTE=humanitarians ./art final $REEL --height 2160 --out <landscape-folder>
```

Rendered media (`mp3/`, `media/`, `clips/`, MP4s, QC frames) are produced locally and are not checked into this repo.

**Approvals and checks:** narration approved and fact-check confirmed by Janvi on 2026-10-28. Landscape export passed the toolkit's final gates (GATE T type check, frame checks) with receipt status: `ready`.

## Watch and review

| Version | Drive link | Resolution | Duration | SHA-256 |
|---|---|---|---|---|
| Video | [Watch on Drive](https://drive.google.com/file/d/1V63cv1GyKz2hLoi6jU2qdCkO9yb0xK5o/view?usp=drivesdk) | 3840×2160 | 1:32 | `10e6413aea92766a3489273a0965a054182c27bc3a5ac960d2b2b679d689e1ea` |

Drive filename: `learning_ConfidenceIntervalsForSmallTests_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_11_Oct12_Oct18)
