# Almost Ready to Submit — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:47 (10 beats) · **Destination:** `fellows/janvi-c/2026-10-26-progress-ready-to-submit/`

## This week's contribution

- **Question:** In the final week of my contract, what does the paper still need before it can be submitted?
- **What I built/tried:** I prepared a clean manuscript (tracked changes accepted, comment markers removed, two final wording fixes, full verification suite), checked the journal's submission requirements, drafted the missing materials, and compiled the 13-week documentation record.
- **Observed result:** The paper renders at 30 pages; abstract 293 words (limit 300); 8 figures and tables (limit 8); body ~7,600 words (guideline 6,000, accepted by my professor). Gaps: Statement of Significance, graphical abstract and generative AI declaration, all started, plus a cover letter and co-author details. No fee under Northeastern's agreement. Renewal proposed: November 1, 2026 to February 20, 2027.

## Human and AI work

**My decisions, implementation and verification:** The manuscript clean-up, the requirements check, the drafts, the standup update and the documentation are mine. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-28 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-28.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: two final wording fixes (Introduction and Abstract).

**What remains unverified or failed:** The three submission gaps are drafts, not finished; Professor Gultepe's final review had not come back when this video was made.

**Known toolkit issues hit:** ./setup stops at its ElevenLabs guard because of files under youtube/; worked around without editing tracked files. faster-whisper needed PyAV < 16.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `a187fab76609eef27f0652433b066d14caba6940` (2026-10-21), checked 2026-10-28.
- **Beat sheet:** `beat_sheet.json` (16:9 landscape, 3840×2160).
- **Custom scene code:** `scenes.py`. It loads logo SVGs from `assets/logos/` (claude, github, humanitarians, mistral, openai); those assets are kept locally by Janvi and are not in this repo.
- **Not in this repo:** rendered media and build paperwork (fact-check, shot list, prompts, transcript), kept locally by Janvi and available on request.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/janvi-c/2026-10-26-progress-ready-to-submit
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1ug3U3o8_H9ddXKTi8A4FGY70xFYebWuK/view?usp=drivesdk) | 3840×2160 | 1:47 | `1292d8bd65b2f59081c6ae969305cc13255710932f130f09546f52a5b0a51b73` |

Drive filename: `progress_AlmostReadyToSubmit_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_13_Oct26_Oct31)
