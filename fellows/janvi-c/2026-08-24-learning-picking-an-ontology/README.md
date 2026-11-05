# Picking the Right Ontology — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** learning video (STEM/AI concept) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:58 (9 beats) · **Destination:** `fellows/janvi-c/2026-08-24-learning-picking-an-ontology/`

## This week's contribution

- **Question:** Which biomedical ontology should ground thin abbreviation definitions, and why Gene Ontology?
- **What I built/tried:** I documented in our paper why the pipeline uses Gene Ontology rather than NCIt (diseases and drugs, not gene functions), MeSH (an indexing vocabulary, not functional definitions) or HGNC (gene names, not broader processes), and how it is used: a GO autocomplete search, the label and definition fed into the prompt beside textbook sentences, a category gate (Molecular Biology and Immunology only; acronyms like FDA or WHO are not looked up) and a silent fallback.
- **Observed result:** GO has structured definitions for biological processes and molecular functions, exactly where the abbreviation stubs were thinnest, through a public API with no login.

## Human and AI work

**My decisions, implementation and verification:** The GO lookup is in Thejus's pipeline; I documented the choice and the alternatives in our paper (Sections 2.2 and 3.3) and added references [23] and [24]. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: NCIt, MeSH and HGNC for this job.

**What remains unverified or failed:** The line "the approach was a shared design" comes from me, not from the written source notes.

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

REEL=../humanitarians-youtube/fellows/janvi-c/2026-08-24-learning-picking-an-ontology
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1_Lqsy6x_x06OJ8YLPuJfk0I8ne-RX8ZD/view?usp=drivesdk) | 3840×2160 | 1:58 | `9d9ac1e679c573e7f3d1444fcd3e0460a432372440b92bb461677109b2b6a7aa` |

Drive filename: `learning_PickingTheRightOntology_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_04_Aug24_Aug30)
