# BUILD-LOG — kavya-data-agents-harness

2026-10-28. Built with Claude Code (AI) at Kavya's request. Local, free path only: Kokoro, Remotion and ffmpeg.

1. **Evidence first.** Wrote and ran `demo/harness_demo.py`; stdout saved verbatim to
   `demo/harness_demo_output.txt`. Checked the figures by hand (`FACTCHECK.md` rows 5–12).
2. **Audio.** Kokoro `am_onyx` produced 9 beats, 143.8 s in total; B01 is 9.62 s, above the 9 s minimum.
3. **First landscape render.**
   - Frame review found two defects:
     - B01's overview was still typing when the beat cut.
     - B02's `SkillTeardownPipeline` was undersized and revealed every box at once.
   - Fixes:
     - B01: removed the redundant "Actually —" line, shortened line 2, and set `charMs` 32.
     - B02: new `HarnessParts` scene, with each part revealed at the fraction of the narration where it is spoken.
4. **First `./art final` was refused by Gate V** (0 BLOCKER, 15 MAJOR). The defects were real:
   - B03/B04: `ShellSession` was a thumbnail-sized window on a black stage (underfill and low contrast).
   - B01, B05, B06 and B08: content filled too little of the frame.
   - Fixes:
     - B03/B04: new frame-filling `HarnessTerminal`, with each verbatim stdout line timed to the narration.
     - B01: larger type, plus a title and context cards.
     - B05: reveal order now follows the narration (limits first), with larger type; the copy was
       shortened after a preview showed it overflowing the card.
     - B06/B08: `lectureLayout`.
   - Checker thresholds were not loosened.
5. **Landscape final passed every gate:**
   - GATE T: PASS.
   - Gate V: 0 BLOCKER / 0 MAJOR.
   - Receipt status `ready`; SHA-256 recorded in `README.md`.
6. **Vertical.** `./art vertical` rewired all 9 beats to `916` compositions. The portrait preview found:
   - B03/B04: the terminal window touched the title-safe edge, so it was narrowed to 86%.
   - B06/B08: undersized, because `ClaudeVerdictArtifact916` ignored `lectureLayout`. Support was added.
   - B01: text ran off both edges, because the writer does not wrap. It was broken into four short
     lines; the context cards were dropped (unreadable at phone width) and the name label added.
7. **Vertical GATE T, then Gate V.** GATE T §8.1 measures each word's ink height against 1.9% of 3840.
   Words with only short letters ("runs,", "new") ink at about their x-height, so the portrait text was raised:
   - Writer text: `fontSize` 140.
   - Writer title and name label: `contextTitleSize` / `brandLabelSize` 96 (new opt-in props).
   - Terminal: 2.6% of height, with the title bar the same size.
   - B05: headers and items floored.
   - B01: the portrait text was trimmed to 12 words (§8.5).

   §8.3b read the multi-row terracotta wash in the portrait terminal as dark-on-dark, so portrait marks
   that line with terracotta text and the bar instead. Gate V then caught the terminal window touching the
   bottom title-safe line, and the window was lifted to 6.5%.

   Vertical final: GATE T PASS, Gate V 0/0, receipt `ready`, SHA-256 in `README.md`.
8. **Toolchain notes for this Windows machine:**
   - ffmpeg is not on PATH; use `runtime/bin/ffmpeg-master-latest-win64-gpl/bin`.
   - Scripts need `PYTHONUTF8=1`, or `scene_index.py` and `scene_search.py` crash on cp1252.

Advisory, not fixed: GATE T §8.10 says B06's narration recites the verdict card (score 0.83). B06 is a
recap bookend, where reading the lines is expected.
