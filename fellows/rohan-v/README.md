# Rohan V.

**Role:** Project Manager  
**Project:** Lyrical Literacy  
**GitHub:** [@rohanvijaykumar](https://github.com/rohanvijaykumar)

Humanitarians AI fellow. Weekly STEM explainers for the Lyrical Literacy project.

- **Voice:** Kokoro `af_bella` at speed `0.95` (locked for the series)
- **Channel chip:** `@HumanitariansAI`
- **Builder:** `ai-explainer` on the `claude-hai` brand (Pragmatist register)

Rebuild with [brutalist.art](https://github.com/nikbearbrown/brutalist.art). Renders — narration, beat clips and the 4K masters — go to Google Drive, one dated folder per week, and each work folder's README links its own. Anything used to *build* a video (captures, pantry stills, sfx) is committed beside it, per the [fellows README](../README.md).

Masters ship at 1080p by default. For 4K: Manim `-qk -r 3840,2160`, `ART_REMOTION_SCALE=2` on Remotion bookends, then `compile.py --height 2160` (16:9) or `--height 3840` (9:16).

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

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
