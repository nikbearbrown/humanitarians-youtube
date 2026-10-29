# The Outvoting Problem — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** learning video (STEM/AI concept) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:29 (9 beats) · **Destination:** `fellows/janvi-c/2026-09-21-learning-outvoting-problem/`

## This week's contribution

- **Question:** Why can an ensemble with a 98% judge catch only 74% of planted errors?
- **What I built/tried:** I explain the outvoting problem with the three-judge rerun of our planted-error test (200 items: 150 corrupted, 50 controls), comparing each judge's tags with the vote.
- **Observed result:** Alone, the judges caught 98.0%, 68.7% and 64.0%; the ensemble caught 74.0%. In 36 of the 39 misses the two weaker judges agreed on "ship" and outvoted the strong judge: correlated errors.

## Human and AI work

**My decisions, implementation and verification:** The test, the rerun and the outvoting analysis are mine. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Claude Code, Mistral and GPT-4o-mini were the three judges.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: the assumption that adding a strong judge lifts the ensemble to its level.

**What remains unverified or failed:** Alternative vote rules (weighting by measured skill, a strong judge's send-to-review, unanimity) are not tested. The overlap of the two weaker judges' misses is shown without counts (my source gives none).

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

REEL=../humanitarians-youtube/fellows/janvi-c/2026-09-21-learning-outvoting-problem
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1ws1zf9e8PLKXrkpw8sznZ8GOgpQe5YLo/view?usp=drivesdk) | 3840×2160 | 1:29 | `8e6c7614129f49955b2a447a5d0fafc571bf6e8893a24a3a74f4b25b7909e8f2` |

Drive filename: `learning_TheOutvotingProblem_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_08_Sep21_Sep27)
