# 72 Comments, One Plan — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 2:05 (10 beats) · **Destination:** `fellows/janvi-c/2026-10-05-progress-72-comments/`

## This week's contribution

- **Question:** How do I apply Professor Gultepe's second review (6 big-picture points and 72 comments) without losing content or breaking numbers?
- **Prediction:** Applying all 72 comments in one pass would risk content loss and number errors.
- **What I built/tried:** I wrote a script that extracts all 72 comments with their anchor text and section; sorted them into four types; wrote six batched CRITIQ prompts under shared hard rules; traced every article count to its origin; answered the methods questions from the repository; and ran batches 1–3.
- **Observed result:** ~81,000 (substring matches), 10,055 (exact matches) and 10,049 (after 6 duplicates removed) traced; 71,000 had no data source (derived by subtraction) and went on the do-not-use list. From the code: a rule-based artifact checker (up to 2 retries), GPT-4o-mini generation, and a GO gate with 3 categories set and 2 reachable. CRITIQ introduced 2 errors in batch 1, and I caught both.

## Human and AI work

**My decisions, implementation and verification:** The revision plan, the extraction script, the number trace, the repository answers and the checks of CRITIQ's output are mine. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-28 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-28.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- CRITIQ applied the batched edits; it introduced 2 errors in batch 1 (reviewer names inside a definition, and the VEGF lookup attributed to the wrong stage), which I caught.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: the unsourced 71,000, and the two errors CRITIQ introduced.

**What remains unverified or failed:** Batches 4–6 were not yet run when this video was made; they followed in Weeks 11 and 12.

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

REEL=../humanitarians-youtube/fellows/janvi-c/2026-10-05-progress-72-comments
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1E7rLFkDKeDDa5Prch66emsmRy3LWS7rg/view?usp=drivesdk) | 3840×2160 | 2:05 | `b01fed5c535567bc46f67c7ec122bc3bf07f0a34806308feb6e0ae127adfb46a` |

Drive filename: `progress_72CommentsOnePlan_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_10_Oct5_Oct11)
