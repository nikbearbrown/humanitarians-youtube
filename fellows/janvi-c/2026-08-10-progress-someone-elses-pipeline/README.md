# Writing Someone Else's Pipeline — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 2:21 (10 beats) · **Destination:** `fellows/janvi-c/2026-08-10-progress-someone-elses-pipeline/`

## This week's contribution

- **Question:** How do you write the methodology for a pipeline you didn't build?
- **Prediction:** Reading the merge code, I assumed that "the Wikipedia entry wins" on a collision was about pipeline quality.
- **What I built/tried:** I cloned my teammate Thejus's keyword-popup generation repository, used Claude Code to summarize its eight stages (00–07), traced and tested how Gene Ontology is used, and wrote about 2,500 words on it; then I merged our two papers into one draft (a shared introduction, results connected to the 8,968 popups that reached consensus for inclusion, consistent terms, and one stage numbering: 00–07 generation, 10–25 QA). About 22 hours.
- **Observed result:** My inferred reason was wrong: when I checked with Thejus, the real reason was definition completeness (Wikipedia entries usually carry a fuller definition). Code shows what was built, not why.

## Human and AI work

**My decisions, implementation and verification:** The generation pipeline (stages 00–07) and its design decisions are Thejus's; my work was reviewing and documenting it, testing the Gene Ontology API, and merging the two papers. I decided what the paper says, from the code and from Thejus. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Claude Code generated the repository summary (REPO_SUMMARY.md) and searched the codebase for the Gene Ontology function; Claude helped draft about 60–70% of the prose in the 2,500-word generation sections, while the content decisions were mine.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: my "pipeline quality" reading of the merge rule, corrected after checking with Thejus.

**What remains unverified or failed:** The Week 2 content file arrived after the render; the fact-check was re-checked against it on 2026-10-27 (paperwork only, no re-render). B02's on-screen stage cards 02–05 follow the earlier pipeline report's numbering, which differs from the Week 2 file (02 Category Filtering, 03 Rule-Based Cleaning, 04 LLM Rewriting, 05 Abbreviation Scanning + GO Enrichment); B02 was not re-rendered. Pronunciations are Kokoro IPA overrides set by ear. B02's Claude Code mark is shown monochrome in ink after GATE T §8.3 read the terracotta mark as low-contrast accent text.

**Known toolkit issues hit:** ./setup stops at its ElevenLabs guard because of files under youtube/; worked around without editing tracked files. faster-whisper needed PyAV < 16.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `a187fab76609eef27f0652433b066d14caba6940` (2026-10-21), checked 2026-10-27.
- **Beat sheet:** `beat_sheet.json` (16:9 landscape, 3840×2160).
- **Custom scene code:** `scenes.py`. It loads logo SVGs from `assets/logos/` (claude, claude-code, github, humanitarians, mistral, openai, wikipedia); those assets are kept locally by Janvi and are not in this repo.
- **Not in this repo:** rendered media and build paperwork (fact-check, shot list, prompts, transcript), kept locally by Janvi and available on request.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/janvi-c/2026-08-10-progress-someone-elses-pipeline
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1QazCs9NLC1Iykw1t3Fu5aR8PLusGs0E-/view?usp=drivesdk) | 3840×2160 | 2:21 | `85e0bc13a60787183cd3d1fe38092d65b09e5c55ffdf22986e23a5da56eb120f` |

Drive filename: `progress_WritingSomeoneElsesPipeline_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_02_Aug10_Aug16)
