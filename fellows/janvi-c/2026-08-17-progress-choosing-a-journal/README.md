# Choosing a Journal That Will Say Yes — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 2:07 (10 beats) · **Destination:** `fellows/janvi-c/2026-08-17-progress-choosing-a-journal/`

## This week's contribution

- **Question:** Which journal can our paper go to for free, and what does it take to fit its guidelines?
- **What I built/tried:** I researched journals with CRITIQ and confirmed article-fee (APC) coverage under Northeastern's open access agreements with the SciFree tool; compared five options (JAMIA, JBI, Education and Information Technologies, ACM conferences and an AI-in-education journal) by fit and fee coverage; and, after my professor chose JBI, reformatted the paper: JBI section order, a five-part structured abstract cut from 345 to 285 words (limit 300), five highlights under 85 characters, MeSH keywords, Vancouver citations [1]–[22] checked for gaps, body about 3,900 words. 23 hours.
- **Observed result:** The dedicated bioinformatics journals were not free under our agreements; JBI was chosen as the practical option over an aspirational one.

## Human and AI work

**My decisions, implementation and verification:** The journal research, the comparison and the full reformatting are mine; the journal decision was my professor's; the rule that publication be free was Professor Brown's. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- CRITIQ (its first use this term) did journal analysis, formatting guidance and a requirements checklist; I confirmed fee coverage myself in Northeastern's SciFree tool.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: followed the move away from the CS-methodology framing (not novel enough) and ruled out the dedicated bioinformatics journals (not free under our agreements).

**What remains unverified or failed:** The line "the pipeline Thejus and I built" is not in the Week 3 source notes. Pronunciations are Kokoro IPA overrides set by ear.

**Known toolkit issues hit:** ./setup stops at its ElevenLabs guard because of files under youtube/; worked around without editing tracked files. faster-whisper needed PyAV < 16.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `a187fab76609eef27f0652433b066d14caba6940` (2026-10-21), checked 2026-10-28.
- **Beat sheet:** `beat_sheet.json` (16:9 landscape, 3840×2160).
- **Custom scene code:** `scenes.py`. It loads logo SVGs from `assets/logos/` (claude, humanitarians); those assets are kept locally by Janvi and are not in this repo.
- **Not in this repo:** rendered media and build paperwork (fact-check, shot list, prompts, transcript), kept locally by Janvi and available on request.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/janvi-c/2026-08-17-progress-choosing-a-journal
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1hsqMhFGjsP0m71gi4lAh1rqQzyMdQQFE/view?usp=drivesdk) | 3840×2160 | 2:07 | `04e3678f42780354d04b21ed451dcd6c3f43483d63a9555bc57eb3e80f144fc3` |

Drive filename: `progress_ChoosingAJournal_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_03_Aug17_Aug23)
