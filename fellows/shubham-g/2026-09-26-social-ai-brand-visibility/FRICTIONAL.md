# FRICTIONAL — 2026-09-26-social-ai-brand-visibility

_Entries drafted with Claude Code from the build session record; reviewed and appended by Shubham G. (review pending)._

## 2026-09-26 — toolkit setup on Windows
- **Tried / expected:** install the toolkit prerequisites and run `./setup` and `./art smoke`.
- **Resisted:** Windows had no bash, real Python, Node or ffmpeg. Installed Git for Windows, Python 3.12, Node 24 LTS, FFmpeg and MiKTeX. `./setup` stopped at its ElevenLabs guard because example reels mention the name (false positive). `./art smoke` failed because the bundled `_smoke` slug breaks the slug rule in build_safety.py. Python read beat sheets as cp1252 (fixed with `PYTHONUTF8=1`). compile.py's ffmpeg font path broke on `C:\` paths (patched).
- **Claude's contribution:** diagnosed each failure and proposed/made the fixes; I chose the native-Windows install route over WSL.
- **Now understood / open:** the pipeline runs natively on Windows with the patches in TOOLKIT-CHANGES.md.

## 2026-09-26 — script and first render
- **Tried / expected:** a 2–3 minute explainer from my five-lever brief, with no invented numbers.
- **Resisted:** the beat lint rejected my chip under the `claude-hai` brand (fixed by registering `claude-shubh`); `npx` wasn't found from Python on Windows; every review frame failed QC because of the running timecode burn-in (used `ART_NO_DRAWTEXT=1`).
- **Decided:** narrator "Shubh" in Kokoro Bella; drop the reference link; label illustrative charts.
- **Claude's contribution:** script, beat sheet, six new scenes; I set the constraints and choices.

## 2026-09-26 — gates and the 9:16 version
- **Resisted:** GATE T's type floor failed repeatedly (captions, spark lines, labels), terracotta text failed WCAG 4.5:1, and ink-outlined cards were read as overlapping text. The 9:16 cut needed its own portrait layouts: GATE T's portrait floor is about 72 px at 3840 px tall.
- **Did next:** raised type sizes, moved the accent colour to shapes only, softened card borders, and wrote native portrait components with shorter portrait labels.
- **Open:** my own watch-through; PM review; Drive upload.
