# One Word That Oversold My Paper — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 2:27 (8 beats) · **Destination:** `fellows/janvi-c/2026-08-01-progress-qa-paper-oversell/`

## This week's contribution

- **Question:** What does my QA pipeline actually measure, now that I have to write it up as a technical paper?
- **What I built/tried:** I wrote the complete first draft of a ~4,500-word technical paper (22 hours) documenting the three-model ensemble QA pipeline I built over 10 weeks in Term 1 for the Medhavy cancer biology textbook's keyword popups, and submitted it to Professor Brown.
- **Observed result:** My first-draft results sentence oversold the system: "The ensemble verified 8,053 keywords with 94.2% agreement across three independent models, demonstrating high reliability of the verification process." The ensemble measures inter-model agreement, not correctness, so I rewrote it to "The ensemble achieved 94.2% inter-model agreement, with 8,053 keywords reaching consensus for inclusion in the production set."

## Human and AI work

**My decisions, implementation and verification:** I built the QA pipeline (three judges, the five-tag taxonomy, majority vote) and wrote the paper's content and design reasoning; I decided what the paper claims; the numbers came from my own Supabase queries; and I caught the overselling sentence in my own review. My teammate Thejus built the definition-generation pipeline. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration (with my fixes to B00, B01 and B07) before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Claude (Anthropic) helped draft and refine the paper's prose; I supplied the content and design reasoning and decided what the paper says.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: fixed the narration in B00, B01 and B07; cut a "later critique" line (it referred to a review that came after Week 1); chose "had no majority and were flagged for human review" over "went to human review"; shortened the film to 8 beats.

**What remains unverified or failed:** Pronunciations of Medhavy, Thejus and Janvi are Kokoro IPA overrides set by ear. The narration names the third judge as Claude 3.5 Sonnet, as the paper did in Week 1; the final paper no longer uses that name.

**Known toolkit issues hit:** ./setup stops at its ElevenLabs guard because of files under youtube/; worked around without editing tracked files. faster-whisper needed PyAV < 16. OutroCTA's built-in Subscribe/handle text fails GATE T §8.1 and has no size prop, so this film uses the other standard HAI outro, OutroSeries. compile.py adds no corner logo, so the HAI logo is drawn lower-right inside every Manim scene.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `a187fab76609eef27f0652433b066d14caba6940` (2026-10-21), checked 2026-10-27.
- **Beat sheet:** `beat_sheet.json` (16:9 landscape, 3840×2160).
- **Custom scene code:** `scenes.py`. It loads logo SVGs from `assets/logos/` (claude, humanitarians, mistral, openai, supabase); those assets are kept locally by Janvi and are not in this repo.
- **Not in this repo:** rendered media and build paperwork (fact-check, shot list, prompts, transcript), kept locally by Janvi and available on request.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/janvi-c/2026-08-01-progress-qa-paper-oversell
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1GgFXsNjUBILEGIJAiKB3hIXwNkpSTSk8/view?usp=drivesdk) | 3840×2160 | 2:27 | `169de8fe3c72b8a447ef53cc593d20e2c94590040d8e950df2f687205497e075` |

Drive filename: `progress_OneWordThatOversoldMyPaper_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_01_Aug1_Aug9)
