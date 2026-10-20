# Rohan V.

**Role:** Project Manager  
**Project:** Lyrical Literacy  
**GitHub:** [@rohanvijaykumar](https://github.com/rohanvijaykumar)  
**Supervisor:** Nina H.  
**Agreement period:** 1 Oct 2026 — 31 Jan 2027 (renewal approved; previous agreement 11 Aug — 30 Sep 2026)

## Executive summary

Project Manager for Lyrical Literacy. I coordinate the project and build its onboarding
material: the Suno (3 parts) and Midjourney (6 parts) tutorial series and, since 30 Sep, the
Lyrical Literacy Fellows Handbook (v1.0, item 1 of my renewal plan, delivered a month early).
I also make two Brutalist videos a week, one STEM and one progress, each in 16:9 and native
9:16 at 4K, with a Frictional log in every work folder. Next: testing AI video editors for
Lyrical Literacy (November), then an editing pipeline (by mid-December).

## Quick review

- [Renewal request](./RENEWAL.md) (sent 2026-09-28, approved) · [renewal index](./renewal-requests/README.md)
- [Weekly hours](./weekly-hours/README.md): one file per week · [summary table](./HOURS.md)
- [Research and project plan](./research-plan.md), with status
- Latest week: [2026-10-16](#week-of-2026-10-16)

## How this folder is built

- **Voice:** Kokoro `af_bella`, my one narration voice for every episode
- **Channel chip:** `@HumanitariansAI`
- **Builder:** `ai-explainer` on the `claude-hai` brand (Pragmatist register)

Rebuild with [brutalist.art](https://github.com/nikbearbrown/brutalist.art). Renders (narration, beat clips and the 4K masters) go to Google Drive, one dated folder per week, and each work folder's README links its own. Anything used to *build* a video (captures, pantry stills, sfx, evidence data) is committed beside it, per the [fellows README](../README.md).

Every master is 4K: `./art final <reel>` (3840×2160) and `./art final <reel>/vertical --height 3840` (2160×3840).

## Week of 2026-10-16

A STEM explainer and a progress update, both 16:9 (3840×2160) and native 9:16 (2160×3840). Masters in
Drive, [`2026-10-16/`](https://drive.google.com/drive/folders/17pJ6dCN9-GP_vnSmeY3U5a4KKg59V85g) (`landscape/`, `vertical/`), named per
[FELLOWS-SUBMISSION](https://github.com/nikbearbrown/brutalist.art/blob/main/docs/FELLOWS-SUBMISSION.md).
Hours: [20](./weekly-hours/2026-10-12-weekly-hours.md).

- [How Apps Find a Song's Tempo](./2026-10-16-how-apps-find-a-songs-tempo/): onsets, autocorrelation and the octave error, on a tempo detector I built and tested on 40 Western grooves, cross-checked against librosa (`TempoDetection_RohanV.mp4`)
- [Homes of Hope Songs: Proof of Concept Progress](./2026-10-16-homes-of-hope-song-proof-of-concept/): the English + Hindi proof of concept for Lyrical Literacy × Homes of Hope, under 90 s (`HomesOfHopePoC_RohanV.mp4`)

## Week of 2026-10-09

Two STEM explainers this week (no progress video), both 16:9 (3840×2160) and native 9:16
(2160×3840), each built on a program I wrote and measured, with listening clips. Masters in Drive,
[`2026-10-09/`](https://drive.google.com/drive/folders/1JXFqKVB5WenIxrkxeeEGG_0JOfO8Z0_b) (`landscape/`, `vertical/`), named per
[FELLOWS-SUBMISSION](https://github.com/nikbearbrown/brutalist.art/blob/main/docs/FELLOWS-SUBMISSION.md).
Hours: [20](./weekly-hours/2026-10-05-weekly-hours.md).

- [How Shazam Finds a Song](./2026-10-09-how-shazam-finds-a-song/): spectrogram peaks, hashes and offset voting, on a fingerprinter I built and tested in cafe noise (`SongFingerprinting_RohanV.mp4`)
- [How AI Music Generators Turn Text Into Audio](./2026-10-09-how-ai-music-turns-text-into-audio/): audio tokens, a codec and a next-token model I built and measured; how the prompt steers (`AIMusicTokens_RohanV.mp4`)

## Week of 2026-10-02

**Submitted late:** built and sent on Monday 5 Oct; I forgot to submit on Friday 2 Oct. One
STEM explainer and one progress update, both 16:9 (3840×2160) and native 9:16 (2160×3840).
Masters in Drive, [`2026-10-02/`](https://drive.google.com/drive/folders/1P5rUqd8BM9Y9-MWwsTVTNtMLx_0FmiEe) (`landscape/`, `vertical/`), named per
[FELLOWS-SUBMISSION](https://github.com/nikbearbrown/brutalist.art/blob/main/docs/FELLOWS-SUBMISSION.md).
Hours: [20](./weekly-hours/2026-09-28-weekly-hours.md).

- [How Pitch Correction Works](./2026-10-02-how-pitch-correction-works/): detection, snapping and retune speed, on a corrector I wrote and re-measured, with listening clips (`PitchCorrection_RohanV.mp4`)
- [Writing the Lyrical Literacy Fellows Handbook](./2026-10-02-writing-the-lyrical-literacy-fellows-handbook/): weekly progress: the handbook v1.0, shown through crops of the real document (`FellowsHandbookUpdate_RohanV.mp4`)

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
