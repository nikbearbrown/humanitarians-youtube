# Learning Brutalist — Tanishaa

## This week's contribution
- **Question:** what does it actually take for a new fellow to make a video with Brutalist, and which tools does it rely on?
- **Prediction:** the hard part would be the tools themselves: installing them and learning what each one does.
- **What I built:** a 2-minute walkthrough (16:9 and a native 9:16 version) that covers how Brutalist builds a video in steps, the setup on my Mac, what each tool does (Claude Code, Kokoro, Remotion and Manim, ffmpeg), and the two automatic checks. It also covers what I learned from my first real build, What Is RAG. The B05 and B06 frames on screen are real frames from that video.
- **Observed result:** setup was mostly fine, since one micromamba environment held everything. The real lesson came after the build. Both automatic checks passed, but when I watched the preview, the list on screen showed each item after Bella said it. The checks can't catch that, so the person watching has to. It was fixed by timing each reveal to measured word timestamps (faster-whisper), and this video uses that method from the start.
- **Next experiment:** a project update on Lyrical Literacy, built with the same pipeline.

## Human and AI work
- **My decisions, implementation and verification:** chose the topic (changed it from a weeks 1–2 recap to learning Brutalist and its tools), approved the v2 script, watched the landscape cut and approved it before the vertical was built. _[Tanishaa: add what you reviewed or changed, and your notes on the vertical.]_
- **AI tools/voices used and what they generated:** Claude (Claude Code) drafted the script, wrote the beat sheet, wrote the new scenes (`LbScenes.tsx`: six landscape scenes, their portrait versions, and a phone-size takeaway card), wrote the fact-check and shot list, and ran the build and checks. Kokoro `af_bella` (a local AI voice) speaks all narration, which is disclosed in the opening. faster-whisper measured the word times.
- **What I rejected or corrected:** rejected the v1 topic (weeks 1–2 recap) and asked for this one. While building, Claude also fixed these problems:
  - A callout that overlapped a footnote.
  - Terracotta text that failed the contrast check.
  - The toolkit's standard takeaway card, whose text was too small on a phone. It was replaced in the vertical with a new card.
- **What remains unverified or failed:**
  - The B06 timeline (Bella vs. screen) is a diagram, not the measured offsets.
  - Kokoro and Manim have no logo in `icons/logos`. Kokoro is shown as a drawn waveform, and Manim is named in text.
  - In the vertical, the text inside the RAG screenshots (B05, B06) is excluded from the type-size check. Only the designed text is measured.
  - Audio loudness is -20.8 LUFS, which is quiet for YouTube.

## Reproduce
- Brutalist version/commit and date checked: `a99b5323fe346786c3e5991b09a5cc784a6b0da2` (2026-10-23), checked 2026-11-08. It also needs these local, uncommitted additions:
  - `runtime/remotion/src/LbScenes.tsx` and `RagScenes.tsx`
  - their entries in `Root.tsx`
  - the exemption entries in `runtime/scripts/type_check.py`
  - `public/learning-brutalist/` and `public/logos/`
- Landscape steps: `python3 build_sheet.py` → `generate_audio_kokoro.py` → `python word_times.py` → `python3 build_sheet.py` (again, with measured cues) → `remotion_scenes.py` → `python add_bug.py B00 B07` → `./art final`.
- Vertical steps: `./art vertical` → set B07 to `LbTakeaway916` and add `qc.typography_regions` on B05/B06 in `vertical/beat_sheet.json` (re-running `./art vertical` overwrites these) → `remotion_scenes.py` → `python add_bug.py --dir vertical B00` → `./art final vertical --height 3840`.
- On this Mac, Remotion needs `ART_CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ART_CHROME_MODE=chrome-for-testing`.
- Full log: `BUILD-LOG.md`. Media (MP4/MP3) goes to Drive, not GitHub.

## Watch and review
| Version | Drive link | Resolution | Duration | SHA-256 |
|---|---|---|---|---|
| Landscape | _[Tanishaa: add Drive week folder link]_ (`landscape/`) | 3840×2160 | 1:59.4 | `dfd6ac281729f24d0f61ffaeaf8c515f26842535c3f3bc550dbc4835293c8652` |
| Vertical | _[Tanishaa: add Drive week folder link]_ (`vertical/`) | 2160×3840 | 1:59.4 | `cd02736ae4103867403bf858c7147baff4f42e4fcb0d68fac766a41faefdb5a9` |

- Review status: pending
- YouTube 4K check: pending
- Publication decision: pending
