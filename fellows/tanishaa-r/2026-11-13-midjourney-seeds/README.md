# Why the Same Prompt Gives Four Different Images — Tanishaa

## This week's contribution
- **Question:** why does one Midjourney prompt give four different images, and what does a seed actually control? (My assigned Midjourney topic for the team's video content.)
- **Prediction:** reusing a seed would keep a consistent look across different assets.
- **What I built:** a 2¾-minute explainer, with a small real toy generator (`demo/seed_demo.py`, NumPy) that turns seeded noise into a landscape. It's labeled on screen as a toy, not Midjourney.
- **Observed result:** in the toy, the same seed twice gave identical pictures (0 pixels different); four random seeds gave four different ones; keeping the seed and changing one word kept the layout and changed the colours. But Midjourney's own Seeds page says seeds are "Not for Saving Styles": for a consistent look across assets it recommends style references, omni references and personalization. My prediction was wrong, and the video says so.
- **Next experiment:** run the same three-way test in Midjourney itself (no seed, a fixed seed twice, one word changed) and compare it with the toy.

## Human and AI work
- **My decisions, implementation and verification:** the topic (from the team's split), choosing the corrected ending after the fact-check, choosing no Midjourney screenshots, script approval. _[Tanishaa: add what you reviewed or changed.]_
- **AI tools/voices used and what they generated:** Claude (Claude Code) drafted the script, wrote the toy demo, the fact-check, the beat sheets and MjScenes.tsx, and ran the build. Kokoro `af_bella` (a local AI voice) speaks all narration, which is disclosed in the opening.
- **What I rejected or corrected:** _[Tanishaa: add anything you changed.]_ The fact-check found that "reusing the seed is how you keep a consistent look" contradicts Midjourney's docs; the ending was changed to "seed = same image; references = same look".
- **What remains unverified or failed:** no real Midjourney output is shown; Midjourney's behaviour is quoted from its Seeds page (read 2026-11-13). The toy splits layout (from noise) and colour (from words) more cleanly than a real model does.

## Reproduce
- Brutalist commit `a99b5323fe346786c3e5991b09a5cc784a6b0da2` (2026-10-23), checked 2026-11-13.
- Steps: `python demo/seed_demo.py` (copy its PNGs to `runtime/remotion/public/midjourney-seeds/`) → `python3 build_sheet.py` → `generate_audio_kokoro.py . --speed 0.95` → `python word_times.py` → `python3 build_sheet.py` → `remotion_scenes.py` → `python add_bug.py B00 B10` → `./art final`; vertical: `./art vertical`, edit B09/B10 and the portrait `qc` regions, render, `add_bug.py --dir vertical B00 B10`, `./art final vertical --height 3840`.
- Media (MP4/MP3) is on Drive, not GitHub: [week folder 13-11-2026](https://drive.google.com/drive/folders/1U8_ewZfbnmSDZF3BNg6Z896sAiY9p8Of).

## Watch and review
| Version | Drive link | Resolution | Duration | SHA-256 |
|---|---|---|---|---|
| Landscape `MidjourneySeeds_TanishaaR.mp4` | [Drive week folder](https://drive.google.com/drive/folders/1U8_ewZfbnmSDZF3BNg6Z896sAiY9p8Of) (`landscape/`) | 3840×2160 | 2:43.1 | `c6012e66bb886bc744588d898f1c5074d9b0b750bd6adf7a26930ab1448f7699` |
| Vertical `MidjourneySeeds_TanishaaR.mp4` | [Drive week folder](https://drive.google.com/drive/folders/1U8_ewZfbnmSDZF3BNg6Z896sAiY9p8Of) (`vertical/`) | 2160×3840 | 2:43.1 | `0c82b43e27763131a11d5120d41e88551111965e1d5a51db4e5ef19d1e73fa7b` |

- Review status: pending
- YouTube 4K check: pending
- Publication decision: pending
