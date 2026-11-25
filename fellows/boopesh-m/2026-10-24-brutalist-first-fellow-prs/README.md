# Brutalist, Shared — Boopesh M.

Week 2 project update (Brutalist team), week of 18–24 October 2026.

## This week's contribution
- **Question:** what changed in the Brutalist toolkit this week, and what does it mean for fellows?
- **Prediction:** a normal week of toolkit commits by the maintainer.
- **What I built:** a 16:9 explainer (2:13) and a native 9:16 Short (0:40) on the week's changes.
- **Observed result:** the git history shows the first three pull requests in the repo's history
  (#1 thumbnails, #3 setup fixes, #4 SEIS speaker series) merged within 7 seconds on Oct 23, plus three
  new Blender skills (Oct 18–21). The toolkit has become something fellows ship code into.
- **Next experiment:** this week's STEM-topic video (second weekly video).

## Human and AI work
- **My decisions, implementation and verification:** chose the weekly-update topic and the voice
  (`am_onyx`, approved after hearing six samples); reviewed the result.
- **AI tools/voices used and what they generated:** Claude (Claude Code) researched the commits and drafted
  the script, beat sheets and Manim scenes, rendered and checked frames. Kokoro `am_onyx` speaks the
  narration (disclosed on screen and in the audio).
- **What I rejected or corrected:** see [FRICTIONAL.md](FRICTIONAL.md) (wording corrected to match the git
  evidence; footer text removed per the review checklist).
- **What remains unverified or failed:** automated speech-to-text check could not run in the build
  container; pronunciation was checked by phonemes and needs a human listen.

## Files
| File | What it is |
|---|---|
| `beat_sheet.json` / `make_sheet.py` | the 16:9 film as code (narration, shots, timing) |
| `scenes.py` | Manim scenes for the 16:9 film |
| `short/` | the native 9:16 Short: its own beat sheet, scenes and paperwork |
| `FACTCHECK.md` | every claim with its commit hash |
| `SHOTLIST.md`, `PROMPTS.md` | shot plan and prompts |
| `PROOF.md` | plain-language review of the finished videos |
| `description.txt` | YouTube description (summary, chapters, hashtags) |
| `assets/` | inputs: real 4K thumbnails from the repo, tool logos |

## Reproduce
- **Brutalist version/commit and date checked:** `a99b5323` (main, 2026-10-23), checked 2026-10-24
- **Commands:**
  ```bash
  python3 make_sheet.py                                   # writes beat_sheet.json
  python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <this folder>
  python3 <brutalist>/runtime/scripts/remotion_scenes.py <this folder> --only B00   # also B10, B80
  <brutalist>/art run <this folder>
  <brutalist>/art final <this folder> --height 2160
  # Short: same steps on short/, final with --height 3840
  ```

## Watch and review
- Landscape Drive link (add) — 3840×2160 — 2:13 — SHA-256: 422523e93bcca5aa68c3568b62b7950c136cc23d59e3c671028bdc764a34b54c
- Vertical Drive link (add) — 2160×3840 — 0:40 — SHA-256: 038e3a478d5522ef60112b530672d0c4fe226d63733704bec9c0e2f3150508b9
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending
