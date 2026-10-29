# My Paper Had Fake Citations — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** progress video (weekly project update) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 1:51 (10 beats) · **Destination:** `fellows/janvi-c/2026-09-28-progress-fake-citations/`

## This week's contribution

- **Question:** Are the remaining references [13]–[24] in our paper real and correct?
- **What I built/tried:** I checked [13]–[24] against Google Scholar, Crossref, arXiv and the venues' own proceedings; found replacement papers; corrected every error; added DOIs; and ran a full consistency pass of the paper.
- **Observed result:** [14] was fabricated (0 matches in the BEA 2023 proceedings on the ACL Anthology); [13], [15] and [19] had wrong details. Across all 24: 2 fabricated and 7 with incorrect details, 37.5%. Replacements: Mendes et al. "DBpedia Spotlight" (I-Semantics 2011) and Sarsa et al. "Automatic generation of programming exercises" (ICER 2022). DOIs on all 24; consistency pass complete; a summary of every change sent to all three professors.

## Human and AI work

**My decisions, implementation and verification:** The audit, the replacements, the corrections and the consistency pass are mine. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for.
- CRITIQ was used for the reference-section replacement.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: the fabricated references [6] and [14], and seven incorrect entries.

**What remains unverified or failed:** None.

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

REEL=../humanitarians-youtube/fellows/janvi-c/2026-09-28-progress-fake-citations
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1IhFNCNlWhCDOs8klpzEoi8jlv93T92m-/view?usp=drivesdk) | 3840×2160 | 1:51 | `38bd8fa592379b6957bf57c2c5b1d1badbc9510990e929df5662c60d4d6b7475` |

Drive filename: `progress_MyPaperHadFakeCitations_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_09_Sep28_Oct4)
