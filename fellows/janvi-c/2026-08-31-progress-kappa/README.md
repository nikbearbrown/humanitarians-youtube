# From 94.2 Percent to 0.49 — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 2:10 (10 beats) · **Destination:** `fellows/janvi-c/2026-08-31-progress-kappa/`

## This week's contribution

- **Question:** How much of our 94.2% raw agreement between three AI judges is more than chance?
- **What I built/tried:** I restored the paused Supabase audit table (10,049 rows intact) to get each judge's individual tags; built agreement_metrics.py (~800 lines) for Fleiss' kappa, pairwise Cohen's kappa and the dissenter in 2/1 splits; and added Section 4.3 to the paper.
- **Observed result:** Keywords: Fleiss' kappa 0.4884 (moderate, N = 8,967 valid); acronyms: 0.3847 (fair, N = 885). Mistral–Claude 0.6559; both pairs with GPT-4o-mini near 0.4; GPT-4o-mini is the dissenter in 55.8% of keyword splits. Writing it up caught two of my own errors (5.8% → 6.5% with the 8,967 denominator; ~74% → ~67% chance agreement), and the abstract now says accuracy against expert ground truth was not measured.

## Human and AI work

**My decisions, implementation and verification:** The database restore, the script, the analysis and the paper fixes are mine; the chance-baseline critique came from the reviewer. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: 94.2% raw agreement as the headline claim; my 5.8% denominator and the ~74% chance figure (it was the acronym figure applied to keywords).

**What remains unverified or failed:** Accuracy against expert ground truth was not measured. The judge's name GPT-4o-mini comes from my Week 1 notes (the Week 5 file says "OpenAI").

**Known toolkit issues hit:** ./setup stops at its ElevenLabs guard because of files under youtube/; worked around without editing tracked files. faster-whisper needed PyAV < 16.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `a187fab76609eef27f0652433b066d14caba6940` (2026-10-21), checked 2026-10-28.
- **Beat sheet:** `beat_sheet.json` (16:9 landscape, 3840×2160).
- **Custom scene code:** `scenes.py`. It loads logo SVGs from `assets/logos/` (claude, humanitarians, mistral, openai, supabase); those assets are kept locally by Janvi and are not in this repo.
- **Not in this repo:** rendered media and build paperwork (fact-check, shot list, prompts, transcript), kept locally by Janvi and available on request.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/janvi-c/2026-08-31-progress-kappa
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
| Video | [Watch on Drive](https://drive.google.com/file/d/10uZYEdVnxDE-uFFLDQcz7827LoYsh2Sw/view?usp=drivesdk) | 3840×2160 | 2:10 | `791e4660a6ab1a3f70427c5e112387e70a45200490be868d4d857bb60b2aca01` |

Drive filename: `progress_From94PercentTo049_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_05_Aug31_Sep6)
