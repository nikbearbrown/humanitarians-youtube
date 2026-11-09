# Build log

## 2026-11-07

- Toolkit: saved local changes with `git stash`, then fast-forward-only pull found it up to date. Restored the existing installer audio-test guard and set the install font/cache destinations inside the toolkit. The install completed its dependency steps and the readiness check exited 1 with Kokoro synthesis and Whisper smoke checks deliberately skipped. The other readiness rows passed.
- Video repo: `git status` found local untracked episode content, so pull was skipped.
- Inspected the ai-explainer scaffold and four reference episodes. A reference episode put its narrator disclosure in the opener. This episode uses explicit AI wording in the opener.
- Matched beats with `./art scenes` and verified six composition names with `./art scenes --check`. The selected timing table presents the measured result with the paired-world scope visible.
- Human review of `bm_fable` (British English, speed 1) and actual render details are pending.
- The static runtime list recognized all eight bindings and marked their empty video slots SLATE. The safety validator refused the build at the pending voice gate.

## 2026-11-07 final production

- Verified human voice approvals and current fingerprints before local Kokoro generation. All narration uses bm_fable, British English, speed 1.0.
- Generated beat audio in isolated staging, derived the full native portrait plan, rendered the registered compositions at 24 fps, and checked each source clip with ffprobe. Render scaling happened at rasterization, not on a pre-rendered video.
- Assembled with stock art final under a four-core CPU affinity. Checked the final typography and visual gates and sampled every beat. Native 3840 x 2160 landscape (121.29 s) and native 2160 x 3840 portrait (121.29 s), both at 24 fps with H.264 video and AAC audio. Both use the export name RLEnvironment_PoojithK.mp4. The stock final checks and sampled visual review passed.
- Added 14.7 seconds of reading holds to the project timeline with no change to speech speed. The portrait data cards preserve the landscape figures with larger text.
- The source repository contains no generated media. The closing evidence or takeaway card remains part of the episode; the stock skin linter suggested its generic outro as an advisory.

## 2026-11-08 closing revision

- The voice fingerprint and the existing human approvals matched before generation. Regenerated the closing and the affected number-bearing beats with local Kokoro at the approved settings. Checked every narration beat for remaining digits.
- Held the preceding picture for 1.15 seconds after the last word and used a silent, fully settled stock Form A credit for 72 frames at 24 fps.
- Reused the earlier scenes. Rerendered only the affected content clips in each aspect and one shared native credit clip per aspect. Ran stock final gates, frame review and ffprobe for both exports.
- Revised masters: 2:07.29 landscape and 2:07.29 portrait, native 4K at 24 fps.

## 2026-11-08 timing and source revision

- Verified a one-to-one match between the 60 accepted level-and-seed cells and 60 accepted world artifacts. The coverage comparison names level two, the deadline-first policy and twenty matched pairs. The four timing cues follow the revised narration.
- Reused the approved narration for four unchanged beats from the prior master. Locally synthesized the five changed or new beats with the approved voice. Schema, beat lint and the human voice gate passed.
- Verified both native 4K masters at 24 fps, 148.125 seconds. Measured landscape -23.66 LUFS integrated / -4.43 dBTP, vertical -23.66 LUFS integrated / -4.43 dBTP. Type, final-frame, master, loudness and caption checks passed. An independent frame count verified the duration. No visual slots were unfilled.
- Used “Decisions that helped or hurt” on the replay card in both aspects to meet the minimum text size.
- Extended the quiet hold before the credit by one native frame to avoid stock duration rounding. The silent credit remains 72 frames.
