# Is the Third Judge Necessary? — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:55 (10 beats) · **Destination:** `fellows/janvi-c/2026-09-14-progress-third-judge/`

## This week's contribution

- **Question:** Could we drop the most frequent dissenter (GPT-4o-mini) and keep just Mistral and Claude, and how often does the ensemble catch wrong definitions?
- **What I built/tried:** I ran ablation_test.py on 10,048 valid keyword rows, and sensitivity_test.py: 200 approved definitions, 150 corrupted in five ways (30 each), 50 controls, scored blind.
- **Observed result:** Mistral and Claude agree on 73.8%; with two judges the review queue grows from 585 to 2,631 (4.5-fold), and 2,046 items (20.4%) change action, all of them tie-breaks by GPT-4o-mini. Dropping it saves 33% of API cost but ships 1,799 fewer items, so it is not redundant: it is the tiebreaker. Two-judge sensitivity run (Claude unavailable): strict detection 30.0%, sent to review 51.3%, pass-through 18.7%, 0.0% of controls flagged.

## Human and AI work

**My decisions, implementation and verification:** Both experiments, both scripts and the analysis are mine. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Mistral and GPT-4o-mini scored the corrupted set.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: dropping the third judge.

**What remains unverified or failed:** The sensitivity result used two judges only; the three-judge rerun followed in Week 8. "Most frequent dissenter" comes from my Week 5 analysis.

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

REEL=../humanitarians-youtube/fellows/janvi-c/2026-09-14-progress-third-judge
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1XbHtB3tJc5IzrX9tQ8886VvGYoNQmY80/view?usp=drivesdk) | 3840×2160 | 1:55 | `3fee72a94bfd17b744e0e3f17bfa2012f5a2d17ecd5f9293eb057f17b7e05688` |

Drive filename: `progress_IsTheThirdJudgeNecessary_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_07_Sep14_Sep20)
