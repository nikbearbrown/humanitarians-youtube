# Writing a Structured Abstract — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** learning video (STEM/AI concept) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:44 (9 beats) · **Destination:** `fellows/janvi-c/2026-08-17-learning-structured-abstract/`

## This week's contribution

- **Question:** How do you fit a two-phase pipeline and its numbers into a 300-word structured abstract?
- **What I built/tried:** I rewrote our JBI abstract in its five required parts (Objective, Materials and Methods, Results, Discussion, Conclusion), keeping what was done and found and moving design rationale to the methods. For example, a ~25-word sentence naming the three models, their providers and why the providers were mixed became "a three-model cross-provider ensemble".
- **Observed result:** 345 → 285 words, under the 300-word limit, with the findings and numbers kept (10,049 → 8,053 keywords, 927 → 915 acronyms, five tags, three models).

## Human and AI work

**My decisions, implementation and verification:** The abstract, its cuts and the rule behind them are mine. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- CRITIQ gave formatting guidance and a requirements checklist for the JBI reformatting this week.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: the long model-and-provider sentence, replaced by a four-word phrase.

**What remains unverified or failed:** The original long sentence is not quoted on screen (it is not in my source notes). B04's chip row is slightly wider than its card; it passes every gate.

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

REEL=../humanitarians-youtube/fellows/janvi-c/2026-08-17-learning-structured-abstract
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1QFs-MzCQEHh6kHr816tsE_P5GGpLiFgB/view?usp=drivesdk) | 3840×2160 | 1:44 | `13f813aee6f9804f2cf6f4fa07e3978bd757b0b38feb5fd93388218320a8d13d` |

Drive filename: `learning_WritingAStructuredAbstract_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_03_Aug17_Aug23)
