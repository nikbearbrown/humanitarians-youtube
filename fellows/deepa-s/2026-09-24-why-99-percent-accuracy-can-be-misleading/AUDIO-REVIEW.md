# Mandatory Audio Listening Gate

Status: PENDING — Deepa must listen before audio is locked. No human approval has been invented.

The approved narration has been generated for all nine beats using local Kokoro am_onyx, at speed 1.0. Spoken text remains identical to the approved plan, including the exact opening and the Liam-for-Deepa sign-off. The overview includes its required 0.8-second lead silence in the audio itself.

## Review file

[Listen to the complete narration](audio-review/AccuracyExplainer_DeepaShenoy_NarrationReview.wav)

Absolute Finder path:

`/Users/deepashenoy/Downloads/brutalist.art-main/fellows/deepa-s/2026-09-24-why-99-percent-accuracy-can-be-misleading/audio-review/AccuracyExplainer_DeepaShenoy_NarrationReview.wav`

Duration: 98.315 seconds (about 1 minute 38 seconds). This is the narration review, not a final-video duration claim.

Please listen to the entire track and approve the voice, pronunciation of **Deepa Shenoy**, pacing, and intelligibility. Report any pronunciation or delivery changes with a timestamp. Audio approval is separate from the already-approved script and plan.

## Completed technical checks

All nine MP3 clips decoded successfully, contain non-silent audio, and have no full-scale PCM samples. The concatenated WAV also fully decoded. RMS and sample peaks are measured below; they are not LUFS or true-peak measurements. These numerical checks do not establish correct pronunciation, natural delivery or absence of audible synthesis artifacts; human listening is still required. No video QC has occurred.

| Beat | Review start | Decoded duration | RMS dBFS | Sample peak dBFS |
|---|---:|---:|---:|---:|
| B00 | 0.00s | 8.21s | -23.64 | -4.02 |
| B01 | 8.21s | 9.99s | -23.81 | -1.98 |
| B02 | 18.21s | 7.94s | -23.32 | -5.45 |
| B03 | 26.14s | 19.20s | -24.54 | -0.98 |
| B04 | 45.34s | 3.39s | -22.21 | -4.63 |
| B05 | 48.74s | 14.59s | -24.36 | -5.04 |
| B06 | 63.33s | 10.01s | -24.2 | -1.54 |
| B07 | 73.33s | 17.79s | -24.5 | -3.69 |
| B08 | 91.13s | 7.19s | -23.57 | -4.96 |

The review uses decoded PCM concatenation rather than MP3 stream concatenation, avoiding repeated encoder-padding gaps. Report and SHA-256 values: audio-review/audio-checks.json. Reproduction: prepare_audio_review.py. Technical preparation reads/writes local audio only.

## Why production pauses here

skills/make/explainer/SKILL.md, Workflow step 3, under “each gate is the user's”: **“audio — Kokoro per beat (free, local), measure, lock. GATE: hear it.”** The next step is visual rendering. Deepa requested stops at mandatory human gates; the agent cannot listen and sign on her behalf.

After Deepa approves this audio, proceed with the authorized scene implementation and native landscape/portrait production. Continue automated checks and fixes; stop at the next mandatory human review, including “watch the cut”. No uploads or publication.

## Video status

Landscape MP4: not rendered; video QC not run.
Vertical MP4: not rendered; video QC not run.
No final MP4 paths exist yet. Planned Drive filenames remain AccuracyExplainer_DeepaShenoy.mp4 in separate landscape/ and vertical/ folders.
