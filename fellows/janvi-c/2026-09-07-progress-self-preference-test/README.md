# Testing My Judge for Bias — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:47 (9 beats) · **Destination:** `fellows/janvi-c/2026-09-07-progress-self-preference-test/`

## This week's contribution

- **Question:** Does GPT-4o-mini, which writes our keyword definitions and is one of the three judges, score its own writing more kindly?
- **What I built/tried:** I built self_preference_test.py (--generate, --score, --report): 200 keywords (seed 42), an alternative definition for each from Mistral (ministral-8b-latest) in the same two-sentence popup format, and both sets scored blind by GPT-4o-mini with the same five-tag rubric in separate passes; then chi-square, Welch's t-test and McNemar.
- **Observed result:** Approval was 55.5% (111/200) for its own definitions vs 62.5% (125/200) for Mistral's; mean score 82.77 vs 85.00. Chi-square p = 0.1547 and Welch's p = 0.1154 are not significant; McNemar p = 0.0196 is significant in the opposite direction. No evidence of self-preference, but general leniency. I updated the paper's Section 5.4, Limitations and Highlight 5.

## Human and AI work

**My decisions, implementation and verification:** The experiment design, the script, the analysis and the paper rewrite are mine; the conflict-of-interest concern came from the reviewer. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Mistral (ministral-8b-latest) wrote the alternative definitions and GPT-4o-mini scored both sets.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: the speculative "potential self-preference bias" section, replaced with the test results.

**What remains unverified or failed:** One sample of 200, one other model, one rubric; leniency is not correctness.

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

REEL=../humanitarians-youtube/fellows/janvi-c/2026-09-07-progress-self-preference-test
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1z2nuyOIj1S14yxbY4w2ADj3v9EpVbdp5/view?usp=drivesdk) | 3840×2160 | 1:47 | `c06d344ef0a0d3cf188ccd3918d19d8fd96d819af34a0b6e3dd1ce78a35a12fb` |

Drive filename: `progress_TestingMyJudgeForBias_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_06_Sep7_Sep13)
