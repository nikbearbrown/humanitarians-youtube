# Figures You Can Read on Paper — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:50 (10 beats) · **Destination:** `fellows/janvi-c/2026-10-12-progress-figures-for-print/`

## This week's contribution

- **Question:** Professor Gultepe could not read the figures in print: how do I make every figure and table work on paper?
- **What I built/tried:** I set global print rules (at least 16px text on a 1000px canvas, no titles inside images, paper terms only); rebuilt Figures 1, 2 and S1; drew Figures 3 and 4 in matplotlib at 300 dpi; took the dashboard screenshots with Playwright and assembled them into four panels; built Table 2 (item disposition) and Table 3 (all results, with four new Wilson 95% intervals) and a 7-sheet data workbook; and did the Batch 5 image swaps.
- **Observed result:** Two checking rounds (3 issues in round 1, all fixed in round 2); Table 2 walks 10,055 matched articles to 8,053 shipped keywords; the workbook has ~87 live formulas and recalculated with zero errors; exactly 8 main-text items, in order.

## Human and AI work

**My decisions, implementation and verification:** The rules, the figure and table rebuilds, the workbook and the image swaps are mine. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-28 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-28.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: unreadable figures, titles inside images, and old labels.

**What remains unverified or failed:** The film shows the figures as labelled cards, not the figures themselves (the figure files are not in my source folder).

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

REEL=../humanitarians-youtube/fellows/janvi-c/2026-10-12-progress-figures-for-print
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1uVnaDR2EXHbRldk_keBmN84_XmPDkWO_/view?usp=drivesdk) | 3840×2160 | 1:50 | `531e65773bd60e40c798c66661e94d63416cb5c009e97a821ef549b462a95f1c` |

Drive filename: `progress_FiguresYouCanReadOnPaper_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_11_Oct12_Oct18)
