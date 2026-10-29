# Agreement Is Not Accuracy — Janvi

**Project:** Medhavy (AI-powered learning platform; cancer biology textbook keyword popups) · **Video type:** learning video (STEM/AI concept) · **Skill:** ai-explainer · **Voice:** Kokoro `af_bella` (AI narrator, chosen by Janvi) · **Duration:** 2:04 (9 beats) · **Destination:** `fellows/janvi-c/2026-08-01-learning-agreement-not-accuracy/`

## This week's contribution

- **Question:** When three AI judges agree on a definition, what does that agreement actually tell you?
- **What I built/tried:** I used my three-model ensemble QA pipeline for the Medhavy cancer biology textbook's keyword popups as the worked example of a general method: judges from three providers (Mistral Small, GPT-4o-mini and Claude 3.5 Sonnet), five tags, and a 2-of-3 majority vote on tags rather than averaged scores, because the judges scored on different scales (averages about 65, 76 and 56).
- **Observed result:** The ensemble measures inter-model agreement, not accuracy. Across 10,049 audit rows, 94.2% were resolved by majority vote and 5.8% had no majority and went to human review. It is useful triage at scale, but there is no gold standard, a blind spot shared by all three judges is invisible to the vote, and there is a self-preference risk (GPT-4o-mini helped generate some definitions and also judged them).

## Human and AI work

**My decisions, implementation and verification:** I built the QA pipeline (three judges, the five-tag taxonomy, majority vote) and chose tag voting over score averaging; the numbers come from my own Supabase queries. My teammate Thejus built the definition-generation pipeline. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; I approved the narration verbatim before rendering on 2026-10-27 (PEDAGOGY.md); and I confirmed every row of FACTCHECK.md on 2026-10-27.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the narration and beat sheet from my weekly notes, wrote the fact-check/shot-list/prompt drafts, wrote the Manim scenes and made the fixes the render checks asked for. The B02 and B05 scenes were reused from my Week 1 progress video.
- Kokoro TTS (`af_bella`, local, free) generated all narration. The video says aloud that the voice is an AI narrator and the work is mine.
- brutalist.art (Manim + Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** Kept the greeting as "Hi" ("Hi, Janvi" card; spoken "Hi, I am Janvi and this video is about …"); kept the @HumanitariansAI outro (OutroSeries) instead of the @NikBearBrown outro the lint suggests; spelled the project "Medhavy" throughout (some of my source notes say "Medhavi"); kept the wording law (agreement, consensus, curated; never verified or accurate for what the judges did). For this reel: narration supplied verbatim; no line changed by the fact-check.

**What remains unverified or failed:** Pronunciations of Medhavy, Thejus and Janvi are Kokoro IPA overrides set by ear. B01's judge logos were shrunk after GATE T §8.3 read the terracotta Claude mark as low-contrast accent text. The narration names the third judge as Claude 3.5 Sonnet, as the paper did in Week 1; the final paper no longer uses that name.

**Known toolkit issues hit:** ./setup stops at its ElevenLabs guard because of files under youtube/; worked around without editing tracked files. faster-whisper needed PyAV < 16.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `a187fab76609eef27f0652433b066d14caba6940` (2026-10-21), checked 2026-10-27.
- **Beat sheet:** `beat_sheet.json` (16:9 landscape, 3840×2160).
- **Custom scene code:** `scenes.py`. It loads logo SVGs from `assets/logos/` (claude, humanitarians, mistral, openai, supabase); those assets are kept locally by Janvi and are not in this repo.
- **Not in this repo:** rendered media and build paperwork (fact-check, shot list, prompts, transcript), kept locally by Janvi and available on request.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/janvi-c/2026-08-01-learning-agreement-not-accuracy
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
| Video | [Watch on Drive](https://drive.google.com/file/d/1oJ3guPt_l5UuijoaNkziL_MFi7Ciiztm/view?usp=drivesdk) | 3840×2160 | 2:04 | `bf364d6df2547dff9ce5156f381d25b2b2420bf62e140c3e2eb3364182078328` |

Drive filename: `learning_AgreementNotAccuracy_JanviC.mp4` (Drive folder HAI Brutalist Videos / Medhavy_Janvi / Janvi_Week_01_Aug1_Aug9)
