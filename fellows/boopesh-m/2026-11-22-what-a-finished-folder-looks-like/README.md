# What a Finished Folder Looks Like — Boopesh M.

Weekly Humanitarians AI progress video for the week of **Nov 15–21, 2026** (America/New_York),
in two native 4K formats: a 16:9 film (2:20.0) and its own 9:16 Short (0:45.5).
Narration is an AI voice (Kokoro `am_onyx`) reading my script.

## This week's contribution
- **Question.** When fellows add a piece of work, how much of the standard paperwork comes with it?
- **Prediction.** Beat sheets would be nearly universal and the review files (proof, description) rare.
- **What I built.** `code/week_stats.py`: reads the git history of `humanitarians-youtube`
  (main @ `2a32d04e`), counts merged PRs (first-parent “Merge pull request #N” merges plus
  squash merges), finds new dated work folders by diffing the main snapshots at the start and
  end of the week, and checks each folder for nine pieces by file name.
- **Observed result.** 18 merged PRs; 54 new work folders from 19 fellows. Beat sheet in 51,
  FRICTIONAL log 45, README 43, FACTCHECK 39, SHOTLIST/PROMPTS/code 35 each, description 12,
  PROOF 4. No folder had all nine; 8 folders had eight, and all 8 lacked only PROOF. The week
  before, recounted with the same code: 20 PRs, 54 folders, 34 frictional logs (published:
  19 / 53 / 32 — PR #402 merged after that count; undated folders are now skipped).
- **Next experiment.** Check content, not just presence: does a FRICTIONAL.md carry a dated
  entry for the week, and does a FACTCHECK.md have a claim table?

Example folders shown (by folder name): `rohan-v/2026-11-20-how-auto-tune-works`,
`likhith-r/2026-11-14-word2vec-king-man-woman-queen`.

## Human and AI work
- **My decisions, implementation and verification:** the story angle, the nine-piece list,
  dated-folder rule, which folders to show; approving the `am_onyx` voice (2026-10-24, re-approved 2026-11-23).
- **AI tools/voices used and what they generated:** Claude Code wrote the stats script, the
  beat-sheet generator, both Manim scene files and this paperwork, and ran every gate; Kokoro
  `am_onyx` generated the narration; Remotion rendered the Claude-composer bookends.
- **What I rejected or corrected:** see FRICTIONAL.md (the recount gap was traced to two
  causes rather than one; text-box and edge-bleed gate failures fixed in the scenes).
- **What remains unverified or failed:** my previous videos' details come from my own record
  (the machine was wiped); “fork attempt failed” is my report; the narration was checked by
  phonemizer, not re-listened to by a person in this build. See FACTCHECK.md.

## Reproduce
- **Brutalist version/commit and date checked:** `brutalist.art` @ `a99b5323` (2026-10-23), not
  upgraded; `./setup` checked 2026-11-23 (audio, Manim, Remotion, compile ready; LaTeX blocked, unused).
- **Source commit used for this export:** `humanitarians-youtube` main @ `2a32d04e`.
- **Beat sheet and custom scene files:** `make_sheet.py` → `beat_sheet.json`, `short/beat_sheet.json`;
  `scenes.py`, `short/scenes.py`; data `code/week_stats.py` → `code/results.json`, `code/run.log`.
- **Commands:**
  ```bash
  export PATH=/opt/brut/bin:$PATH ART_CHROME=<headless shell> ART_CHROME_MODE=headless-shell
  python3 code/week_stats.py                    # results.json + run.log (deterministic)
  python3 make_sheet.py                         # both beat sheets; keeps approvals + measured audio
  cd <brutalist.art>
  python3 runtime/scripts/generate_audio_kokoro.py <reel>        # and <reel>/short
  python3 runtime/scripts/remotion_scenes.py <reel> --only B00   # B80; <reel>/short --only B00
  ./art run <reel> --height 1080 ; ./art run <reel>/short --height 1920
  python3 runtime/scripts/type_check.py <reel>                   # and <reel>/short
  ./art final <reel> --height 2160 --out <landscape dir>
  ./art final <reel>/short --height 3840 --out <vertical dir>
  # delivery copy: video stream copied, audio two-pass loudnorm I=-14 TP=-1 LRA=11, AAC 320k
  ```
- **Approvals and checks:** voice approval record in `beat_sheet.json → metadata.approvals.voice`
  (and short/), bound to fingerprint `9fbee75c…c85e`: Boopesh's re-approval for this week in chat on
  2026-11-23 ("Yes, approve am_onyx"; first approved 2026-10-24). Gate results in BUILD-LOG.md.

## Watch and review
Landscape Drive link — 3840×2160 — 2:20.0 — SHA-256 (delivery `FinishedFolder_BoopeshM.mp4`, −14 LUFS): `081fdea008a811975bbff48b4f8f283cae8ad69ac4ae4cac7a99d1eac8a44558` · (master `finished-folder-master.mp4`): `f0f52f802f5f197f21a6b89d27c8e864e0b0f0663049a36ad17d7e53ac6d572d` · Drive link: _to be added_
Vertical Drive link — 2160×3840 — 0:45.5 — SHA-256 (delivery `FinishedFolder_BoopeshM.mp4`, −14 LUFS): `b4e732dd0132475f9d369da34de38cfbf0af45d57209eef0f405de2cc6609f4c` · (master `finished-folder-short-master.mp4`): `8af9016b75631c3884107ef9cf71d1c655a11b559356ae5701d60353bcc48d52` · Drive link: _to be added_
Sources/large assets Drive link: none (no large source assets)
PM review status: pending
YouTube 4K processing check: pending upload
Professors' publication decision: pending
