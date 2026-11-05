# The Number I Was Proudest Of — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 2:15 (10 beats) · **Destination:** `fellows/janvi-c/2026-08-24-progress-proudest-number/`

## This week's contribution

- **Question:** What does our headline number actually measure?
- **Prediction:** I had built the whole paper around 94.2% agreement as its headline result.
- **What I built/tried:** I finished JBI's required sections and wrote a new Gene Ontology section (API, category gate, silent fallback, why GO over NCIt, MeSH and HGNC); sorted my professor's ten-item critique into three groups and fixed the first group: "verified" → "curated" paper-wide, the generator named (GPT-4o-mini, OpenAI), "independently verified" → internal quality control by two co-authors with domain expertise; demoted 94.2% to a routing statistic with 5.8% human adjudication as the lead; built a pipeline funnel with arithmetic checks (8,053 + 108 = 8,161); added reproducibility details (dump and API dates, model versions, temperatures) and an ethics paragraph. 25 hours.
- **Observed result:** "Verified" was the paper's whole claim, not one sentence, and my professor saw the pattern I had missed. Self-review catches local problems; outside review catches systemic ones.

## Human and AI work

**My decisions, implementation and verification:** All the revisions are mine; the critique, the routing-statistic reading of 94.2% and the ethics gap came from my professor. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- CRITIQ helped me make the fixes systematically; it did not find the problems.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: "Verified" as the paper's claim, and 94.2% agreement as the headline.

**What remains unverified or failed:** The line "In week one I'd fixed one oversold sentence" comes from my Week 1 notes, not the Week 4 file. The funnel tiers on screen are schematic.

**Known toolkit issues hit:** ./setup stops at its ElevenLabs guard because of files under youtube/; worked around without editing tracked files. faster-whisper needed PyAV < 16.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `a187fab76609eef27f0652433b066d14caba6940` (2026-10-21), checked 2026-10-28.
- **Beat sheet:** `beat_sheet.json` (16:9 landscape, 3840×2160).
- **Custom scene code:** `scenes.py`. It loads logo SVGs from `assets/logos/` (humanitarians, openai); those assets are kept locally by Janvi and are not in this repo.
- **Not in this repo:** rendered media and build paperwork (fact-check, shot list, prompts, transcript), kept locally by Janvi and available on request.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/janvi-c/2026-08-24-progress-proudest-number
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1v9faB8emcDDAUufOuv8T61P64qWPDUAt/view?usp=drivesdk) | 3840×2160 | 2:15 | `30282f176327cafee1715e1b6b8c3eb81c7e823777d91b7b4f9cf914274fb5d2` |

Drive filename: `progress_TheNumberIWasProudestOf_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_04_Aug24_Aug30)
