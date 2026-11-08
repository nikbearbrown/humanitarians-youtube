# What Is RAG? — Tanishaa R.

STEM/AI explainer, week of 2026-11-06. Narrated by Bella (Kokoro `af_bella`, an AI voice; disclosed in the opening line). Channel: @HumanitariansAI.

## This week's contribution
- **Question:** what is retrieval-augmented generation (RAG), and when should a student actually use it?
- **What I expected:** most people think RAG makes a model smarter. It doesn't; it hands the model the right text before it answers.
- **What I built:** a 2:37 explainer in 16:9 and native 9:16. The worked example runs a real keyword search (`demo/rag_demo.py`) over a made-up syllabus (`demo/syllabus.md`).
- **What happened:** the search ranked "§3 Late labs" first (score 0.392; output in `demo/retrieval_output.json`). Plain keyword search missed the "Extensions" section, which is the gap embeddings (beat B04) are meant to close.
- **Next experiment:** swap the keyword search for a real embedding model and see whether "Extensions" makes the top three.

## Human and AI work
- **My decisions, work and checks:** topic choice; length (2–3 min); narrator voice (Bella); script approval; reviewed the preview cuts. _[Tanishaa: add anything else you reviewed or changed.]_
- **AI tools and voice, and what they made:** Claude (Claude Code) drafted the script, wrote the beat sheets, the demo code and the RAG scenes (`scenes/RagScenes.tsx`), and ran the build and checks. Kokoro `af_bella` speaks all narration.
- **What I rejected or corrected:**
  - Asked for a longer cut (2 min → 2–3 min), so the script gained the embeddings beat.
  - Changed the intro greeting from "Hej, HAI" to "Hi, Tanishaa".
  - Caught a lag between the narration and the on-screen items in the "use it when / skip it when" beat. It was fixed by timing every reveal to measured word timestamps (`word_times.py` → `timing/words.json`).
- **Still unverified or failed:**
  - B04's map positions are schematic, not computed embeddings; the screen says so.
  - The 9:16 version shows less text than the 16:9 version (first sentences only, short footnotes) because phone-size type fits fewer words.
  - Audio loudness is −20.9 LUFS, quiet for YouTube.
  - How Bella pronounces "Tanishaa" has not been checked by me yet.

## Reproduce
- **Brutalist version:** commit `a99b5323fe346786c3e5991b09a5cc784a6b0da2` (2026-10-23), checked 2026-11-05.
- **Source commit for the export:** this folder's commit in `humanitarians-youtube/fellows` (the commit that adds it).
- **Beat sheets:** `beat_sheet.json` (16:9) and `vertical/beat_sheet.json` (9:16). `build_sheet.py` regenerates the 16:9 sheet from the approved script.
- **Custom scenes:** `scenes/RagScenes.tsx` (six scenes, each with a `…916` portrait version); how to register them is in `scenes/ROOT-REGISTRATION.md`.
- **Timing:** `timing/timings.json` (measured beat lengths) and `timing/words.json` (measured word starts used for on-screen cues).
- **Steps:**
  1. `python3 build_sheet.py`
  2. `python3 runtime/scripts/generate_audio_kokoro.py <reel>`
  3. `python word_times.py`
  4. `python3 build_sheet.py` (again, so cues use the measured words)
  5. `python3 runtime/scripts/remotion_scenes.py <reel>`
  6. `python add_bug.py B00 B01 B07 B08`
  7. `./art final <reel>`
  8. For 9:16: `./art vertical <reel>`, then `remotion_scenes.py <reel>/vertical`, then `python add_bug.py --dir vertical B00 B01 B07 B08`, then `./art final <reel>/vertical --height 3840`.
- **Inputs:** none outside this folder (no pantry stills, captures or third-party media).

## Watch and review
| Version | Drive link | Resolution | Duration | SHA-256 |
|---|---|---|---|---|
| Landscape `WhatIsRAG_TanishaaR.mp4` | _pending upload_ | 3840×2160 | 2:36.9 | `174e935eda1937315b62c66480ee9160ecfe5429ecce95453e671565dd7a9c3f` |
| Vertical `WhatIsRAG_TanishaaR.mp4` | _pending upload_ | 2160×3840 | 2:36.9 | `f1362df8688b4db868fa215f393b9a920f95a820202cb32db648421a5dcdd5c5` |

- Review status: pending
- YouTube 4K check: pending
- Publication decision: pending

Video and audio files are on Drive, not in this repository.
