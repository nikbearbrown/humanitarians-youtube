# FACTCHECK — "Your Weekly Video, Handled."

Every factual claim the narration makes, with its source and verdict.
Verified 2026-08-28.

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B00 | Fellows owe **four video files every week** | TRUE | Nina H., "Weekly videos: what to make, what to upload, due Fridays", 2026-08-20: "Each video gets uploaded in two formats, 16:9 and 9:16, so that is four files total per week." |
| 2 | B01 | Two videos: one STEM/AI topic, one project progress | TRUE | Same email: "1. One on a STEM or AI topic you are interested in. 2. One on the progress you or your team have made on your project." |
| 3 | B01 | Due **Friday** | TRUE | Same email: "Two videos a week, due Friday." |
| 4 | B01 | Each exported 16:9 and 9:16 | TRUE | Same email, as above. |
| 5 | B01 | Flexibility: passion topic allowed if ≥1 of 4 files in any two-week stretch is a research update | TRUE | Same email: "You can substitute a video on a topic you are passionate about, as long as at least one of the four videos across any two week stretch is an update on your research. That is the floor." |
| 6 | B01 | Videos are **4K** | TRUE | Nik B., "Re: Updated Drive folder for video submissions", 2026-08-24: "The videos at 4K 9:16 and 16:9 versions go there". Toolkit corroborates: `runtime/scripts/run.sh` defaults `HEIGHT=2160` ("4K-native master"); `./art final` passes `--height 2160`. |
| 7 | B02 | The toolkit is cloned from `github.com/nikbearbrown/brutalist.art` | TRUE | Confirmed by the user; the working clone in this session came from that URL. |
| 8 | B02 | Setup installs dependencies and downloads the voice model | TRUE | `setup --install` installs `requirements.txt` + `npm install` in `runtime/remotion`, then curls the Kokoro model. Executed successfully in this session. |
| 9 | B04 | Narration voice runs **locally and free** | TRUE | `runtime/scripts/generate_audio_kokoro.py` header: "Kokoro-82M via kokoro-onnx — free, local, Apache-2.0, no API, no meter". This reel's own audio ran offline at $0.00. |
| 10 | B04 | Audio is measured **first** and becomes the clock | TRUE | Same file: "Durations are GROUND TRUTH for all downstream timing." `CLAUDE.md` rule 2: "Audio-first… their durations are the master clock. Never fix timing by hand." |
| 11 | B05 | Claude cannot watch the video | TRUE | `HOW-TO.md` §1: "Claude cannot watch the video… Taste isn't a step it does slowly — it's a step it can't do at all." |
| 12 | B05 | Only the changed beat recompiles | TRUE | `runtime/scripts/compile.py` docstring: "Rebuild recompiles ONLY slots whose input changed (sha1 manifest)". |
| 13 | B06 | The 9:16 Short is derived from the master | TRUE | `./art shorts <reel>` → `runtime/scripts/shorts.py`: "derive the 9:16 Short (cap check + auto-shorten)". |
| 14 | B07 | Docs go to the `fellows/` folder of the humanitarians-youtube repo | TRUE | Nik B., 2026-08-24: "the code for the videos here https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows". |
| 15 | B07 | Nothing over **25 MB** | TRUE | Confirmed by the user as the submission rule. Consistent with GitHub's own 25 MB web-upload limit and 100 MB hard file limit. |
| 16 | B09 | Video files go to the shared Google Drive folder | TRUE | Nik B., 2026-08-24: "The videos at 4K 9:16 and 16:9 versions go there New Drive folder: https://drive.google.com/drive/folders/1yf3ZJ9NfDJvdDAiuPiWEwKDjdkQMEh0g". |
| 17 | B09 | Drive upload is the only manual step | TRUE (scoped) | Confirmed by the user. Scoped claim: it is the only manual **file-transfer** step; B05 (review/approve) is also human, and the reel says so explicitly at B05 and B10. Not a contradiction — B10 states all three human steps. |
| 18 | B08 | No write access → fork + PR; write access → branch + PR | TRUE | Confirmed by the user as the intended routing for new vs. returning fellows. Both are standard GitHub contribution flows. |

## Links, verified verbatim

| Purpose | URL | Appears in |
|---|---|---|
| Toolkit repo | `https://github.com/nikbearbrown/brutalist.art` | B02 (permission card), B11 (Your Turn prompt) |
| Submission repo | `https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows` | B07 (footer) |
| Drive folder | `https://drive.google.com/drive/folders/1yf3ZJ9NfDJvdDAiuPiWEwKDjdkQMEh0g` | B09 (footer) |

All three transcribed character-for-character from the source emails / the user's confirmation. **No URL is read aloud** — each is shown on screen only, because spoken URLs are unusable to a listener and the narration deliberately carries no personal names other than the presenter's.

## Deliberate omissions

- **No third-party personal names.** At the user's instruction, no individual other than the presenter is named in narration or on-screen copy. The GitHub URLs necessarily contain the repository owner's handle — these are load-bearing paths that must stay exact for the links to resolve, so they remain as-is.
- **No claim about review turnaround or merge timing** — not stated in any source.
- **No claim that the agent uploads to Drive.** It does not; that is the human step.
