# FACTCHECK — Learning Brutalist

| Beat | Claim | Verdict | Source / basis | Fix applied |
|---|---|---|---|---|
| B00 | Brutalist is the toolkit HAI fellows use to make videos; Bella is an AI narrator; Claude drafted the script and Tanishaa approved it. | TRUE | brutalist.art/CLAUDE.md ("video toolkit for Humanitarians AI fellows"); script v2 approved in chat 2026-11-06. | Says "Claude drafted and I approved", not "I wrote". |
| B01 | Every video starts as a beat sheet; narration is generated first and its measured length is the clock for every picture. | TRUE | brutalist.art/HOW-TO.md §1 ("audio-first … durations become the master clock"). | none |
| B02 | Her Mac lacked the usual developer tools; Claude Code installed everything in one self-contained environment; setup came back ready except LaTeX, which only matters for math equations. | TRUE | 2026-11-05 install: no Homebrew, Node or ffmpeg system-wide; micromamba env `brutalist`; `./setup` ready except "Manim equation beats" (no LaTeX/dvisvgm). HOW-TO.md: LaTeX is "only for Manim equation beats". | none |
| B03 | Claude Code runs commands and writes scene code; Kokoro makes the voice locally for free; Remotion and Manim draw graphics from code; ffmpeg joins the beats. | TRUE | README.md ("Free by default — Kokoro, Manim, Remotion"); What Is RAG BUILD-LOG (Kokoro cost $0.00; RagScenes.tsx written by Claude Code); compile uses ffmpeg. | none |
| B04 | A video isn't done until it passes two automatic checks: text (size, contrast, overlap) and every frame for layout problems. | TRUE | GATE T (type_check.py: min-size, contrast, overlap) and GATE V; `./art final` blocks on either. | none |
| B05 | What Is RAG is about two and a half minutes; the vertical version needed its own portrait layouts with fewer words. | TRUE | what-is-rag master 156.9 s; BUILD-LOG 2026-11-06 ("native portrait layouts", "SHOW LESS"). Frames on screen are real, from both masters at 57 s. | none |
| B06 | The checks passed but the list lagged the narration; Tanishaa caught it by watching; fixed by timing reveals to measured words. | TRUE | BUILD-LOG 2026-11-06 sync fix (B06 around 1:52; faster-whisper word times). Frame on screen is real (118 s). | The timeline diagram is schematic, not measured offsets. |
| B07 | Takeaway (advice). | opinion, labeled as advice | — | none |

Nothing in the narration dates the film beyond "What Is RAG"; no version numbers are spoken.
