# Why Substring Matching Fails — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** learning video (STEM/AI concept) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:53 (9 beats) · **Destination:** `fellows/janvi-c/2026-08-10-learning-substring-vs-exact/`

## This week's contribution

- **Question:** Why did one switch, from substring to exact category matching, take a Wikipedia filter from about 81,000 articles to about 10,000?
- **What I built/tried:** I documented my teammate Thejus's Wikipedia extraction filter (468 oncology category terms) and his switch from substring to exact matching, for our paper and as the worked example of a general method. The pipeline and the decision are his; the documentation is mine.
- **Observed result:** Substring matching kept about 81,000 articles, partly through false matches such as "SERS" inside "Composers"; exact matching kept about 10,000 with far fewer false matches, but it misses plurals and reworded names.

## Human and AI work

**My decisions, implementation and verification:** I read Thejus's filter code and documented the filter and his decision in our paper. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Claude Code summarized Thejus's repository this week (REPO_SUMMARY.md), and Claude helped draft the prose of the generation sections; the content decisions were mine.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: showed the on-screen counter as "~10,000", matching the narration's "about ten thousand".

**What remains unverified or failed:** The Week 2 content file arrived after the render; the fact-check was re-checked against it on 2026-10-27 (paperwork only, no re-render). The on-screen counter reads "~10,000" where that file gives "~10,049" (a rounding, not a contradiction).

**Known toolkit issues hit:** ./setup stops at its ElevenLabs guard because of files under youtube/; worked around without editing tracked files. faster-whisper needed PyAV < 16.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `a187fab76609eef27f0652433b066d14caba6940` (2026-10-21), checked 2026-10-27.
- **Beat sheet:** `beat_sheet.json` (16:9 landscape, 3840×2160).
- **Custom scene code:** `scenes.py`. It loads logo SVGs from `assets/logos/` (humanitarians, wikipedia); those assets are kept locally by Janvi and are not in this repo.
- **Not in this repo:** rendered media and build paperwork (fact-check, shot list, prompts, transcript), kept locally by Janvi and available on request.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/janvi-c/2026-08-10-learning-substring-vs-exact
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1DptDFCucgNNQFWHMcXEcDV9KO8_DRH0F/view?usp=drivesdk) | 3840×2160 | 1:53 | `4f1ba62971d844733546cc798f41efb0c3297cc1a886e21acf80129583f33b56` |

Drive filename: `learning_WhySubstringMatchingFails_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_02_Aug10_Aug16)
