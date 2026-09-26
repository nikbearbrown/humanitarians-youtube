# Rohan V.

**Role:** Project Manager  
**Project:** Lyrical Literacy  
**GitHub:** [@rohanvijaykumar](https://github.com/rohanvijaykumar)

Humanitarians AI fellow. Weekly STEM explainers for the Lyrical Literacy project.

- **Voice:** Kokoro `af_bella` — my persistent narrator for every episode (FELLOWS-SUBMISSION). Speed `0.95` is recorded only for the 2026-08-21 pair; later builds record none, i.e. the generator default `1.0`
- **Channel chip:** `@HumanitariansAI`
- **Builder:** `ai-explainer` on the `claude-hai` brand (Pragmatist register)

Rebuild with [brutalist.art](https://github.com/nikbearbrown/brutalist.art). Renders — narration, beat clips and the 4K masters — go to Google Drive, one dated folder per week, and each work folder's README links its own. Anything used to *build* a video (captures, pantry stills, sfx) is committed beside it, per the [fellows README](../README.md).

Masters ship at 1080p by default. For 4K: Manim `-qk -r 3840,2160`, `ART_REMOTION_SCALE=2` on Remotion bookends, then `compile.py --height 2160` (16:9) or `--height 3840` (9:16).

## Week of 2026-09-25

One STEM explainer and one progress update, both 16:9 (3840×2160) and native 9:16
(2160×3840). Masters in Drive, [`2026-09-25/`](https://drive.google.com/drive/folders/1bbImyiy_SvbzPU4WDqD_cJVorkMdL8_J)
(`landscape/`, `vertical/`), named per [FELLOWS-SUBMISSION](https://github.com/nikbearbrown/brutalist.art/blob/main/docs/FELLOWS-SUBMISSION.md).

- [How AI Image Generators Turn Noise Into a Picture](./2026-09-25-how-ai-image-generators-turn-noise-into-a-picture/) — diffusion, shown on a toy model I trained on a laptop CPU (`ImageDiffusion_RohanV.mp4`)
- [Testing AI Video Editors, and a Setup Guide for New Fellows](./2026-09-25-testing-ai-video-editors-and-a-setup-guide/) — weekly progress: four agentic editing tools, one hands-on test, the new-fellow guide in progress (`AgenticEditingUpdate_RohanV.mp4`)

First week on the updated Brutalist framework: the required opening line, AI
narration disclosed on screen, typeset math, executable evidence instead of
pictures of it, and GATE T passing on **both** aspects — the portrait cuts were
re-laid to the 9:16 type spec (body 4.0vh, floor 3.2vh) after the first vertical
render failed it.

## Week of 2026-09-18

Two STEM explainers, both audio. Both 16:9 and native 9:16 at 4K.

- [16-bit or 24-bit: What Bit Depth Does](./2026-09-18-what-bit-depth-does/) — bit depth, for someone who has never opened an audio editor
- [Why Your Track Sounds Thin On A Phone](./2026-09-18-why-tracks-sound-thin-on-a-phone/) — mono fold-down, and the ten-second check that catches it

Both reels are **word-clock choreographed**: `align.py` measures when every word
is actually spoken, `cues.json` names an anchor phrase per reveal, and
`sync_cues.py` writes the measured fractions into the beat sheet. 58 cues
authored, 58 resolved. Motion lands on the spoken word rather than on a guessed
fraction of the beat.

Eight new landscape components and eight native `916` portrait siblings. The
9:16 cut is a **re-render, not a crop** — each beat is re-laid-out for a tall
frame (see each reel's `SHOTLIST.md` for what moved and why).

## Week of 2026-09-11

- [Use the Tool First.](./2026-09-11-use-the-tool-first/) — weekly progress report
- [Why Your Track Gets Turned Down](./2026-09-11-why-your-track-gets-turned-down/) — loudness normalisation explainer

## Week of 2026-09-04

- [Unblocking the Team.](./2026-09-04-unblocking-the-team/) — weekly progress report
- [What MP3 Throws Away](./2026-09-04-what-mp3-throws-away/) — lossy compression explainer

## Week of 2026-08-28

- [Agent-First with Brutalist](./2026-08-28-agent-first-brutalist/)
- [Stem Separation: Estimation, Not Extraction](./2026-08-28-stem-separation/)

## Week of 2026-08-21

- [What a Spectrogram Shows](./2026-08-21-what-a-spectrogram-shows/)
- [Sample Rate and the Nyquist Limit](./2026-08-21-sample-rate-and-the-nyquist-limit/)

## Lyrical Literacy tutorial series

My main project work: training videos for new Lyrical Literacy volunteers, who join
with no background in music production, image generation or AI tools. Every screen is
rebuilt from my own captures rather than recorded. 16:9, 4K.

**Suno** — built 2026-08-29 → 2026-08-31, reported in the week of 2026-09-04

- [Suno interface research and series plan](./2026-09-04-suno-interface-research/)
- [Suno, Part One — Your First Song](./2026-09-04-suno-part-1-your-first-song/)
- [Suno, Part Two — The Advanced Tab](./2026-09-04-suno-part-2-the-advanced-tab/)
- [Suno, Part Three — Voices, Remixes and Downloads](./2026-09-04-suno-part-3-voices-remixes-and-downloads/)

**Midjourney** — built 2026-09-06 → 2026-09-09, reported in the week of 2026-09-11

- [Midjourney interface research and series plan](./2026-09-11-midjourney-interface-research/)
- [Midjourney, Part One — Your First Image](./2026-09-11-midjourney-part-1-your-first-image/)
- [Midjourney, Part Two — Writing the Prompt](./2026-09-11-midjourney-part-2-writing-the-prompt/)
- [Midjourney, Part Three — What to Do With One You Like](./2026-09-11-midjourney-part-3-what-to-do-with-one-you-like/)
- [Midjourney, Part Four — The Settings Panel](./2026-09-11-midjourney-part-4-the-settings-panel/)
- [Midjourney, Part Five — Getting the Same Look Twice](./2026-09-11-midjourney-part-5-getting-the-same-look-twice/)
- [Midjourney, Part Six — The Editor, and Where Your Work Lives](./2026-09-11-midjourney-part-6-the-editor-and-where-your-work-lives/)

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
