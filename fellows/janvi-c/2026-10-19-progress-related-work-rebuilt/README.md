# Related Work, Rebuilt — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:41 (10 beats) · **Destination:** `fellows/janvi-c/2026-10-19-progress-related-work-rebuilt/`

## This week's contribution

- **Question:** Professor Gultepe said Related Work described our own system instead of prior work: how do I rebuild it, and is the paper ready to send?
- **What I built/tried:** I searched Google Scholar, ACL Anthology, PubMed, NeurIPS and arXiv; checked each new reference on its publisher's page; wrote one-line "what it shows" summaries; corrected the project spelling to Medhavy in the paper; ran a scripted final check; and built a 72-row response workbook.
- **Observed result:** 12 new references (including Remy 2023, Panickssery 2024, Ji 2023, Feinstein & Cicchetti 1990 and Wilson 1927), 36 references in total; all 72 comments addressed, zero numbers lost, 8 items in order, abstract 293 words, retired values absent. The paper, the response workbook and the data workbook went to all three professors.

## Human and AI work

**My decisions, implementation and verification:** The search, the publisher-page checks, the summaries, the scripted check and the response workbook are mine. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-28 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-28.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- CRITIQ applied the edits; I wrote the one-line summaries so it could not overstate what each source shows, and it also removed 3 older citations that overstated their sources.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: a Related Work section that described our own system, and the old project spelling in the paper.

**What remains unverified or failed:** The professors' review of the final paper had not come back when this video was made.

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

REEL=../humanitarians-youtube/fellows/janvi-c/2026-10-19-progress-related-work-rebuilt
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1Awi5bWAP7plbNmGfM5_WJxZMM4OSp3f-/view?usp=drivesdk) | 3840×2160 | 1:41 | `adc60f268f867fd0c8548127d15618ccca97702c6df9197031ec685700e46e7d` |

Drive filename: `progress_RelatedWorkRebuilt_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_12_Oct19_Oct25)
