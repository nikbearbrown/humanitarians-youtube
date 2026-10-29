# BUILD-LOG — kavya-semantic-layers-ai-context

2026-10-28. Built with Claude Code (AI) at Kavya's request. Local, free path only: Kokoro, Remotion and ffmpeg.

1. **Evidence first.** Wrote and ran `demo/semantic_demo.py`; stdout saved verbatim to
   `demo/semantic_demo_output.txt`. Checked the figures by hand (`FACTCHECK.md` rows 5–11).
2. **Audio.** Kokoro `am_onyx` produced 9 beats, 145.3 s in total; B01 is 11.09 s.
3. **Timing.** `HarnessParts`, `HarnessTerminal` and `HarnessBoundaryCard` now take `durationSeconds`;
   `Root.tsx` sizes each composition to it with `calculateMetadata`. Each reveal is placed at the fraction
   of the narration where its phrase is spoken.
4. **Landscape.**
   - Every preview passed the frame checker before any 4K render.
   - The first `./art final` was blocked by GATE T §8.1 on B01 (38 px < 41 px). The context cards' small
     detail text contains words with no tall letters ("one", "means"), which measure at x-height. The
     cards were removed; the title and name label fill the frame instead.
   - Re-export passed: GATE T PASS, Gate V 0 BLOCKER / 0 MAJOR, receipt status `ready`.
5. **Vertical.** `./art vertical` rewired all 9 beats to `916` compositions. Then:
   - **Portrait patch:**
     - B01: short lines, at most 12 words.
     - B03/B04: short prompt path and no blank spacer line.
     - B02: part descriptions dropped.
   - **GATE T's size and contrast checks were run on 4× upscaled previews,** calibrated against the
     harness reel's passing previews (which read 70–71 px). B02's part labels measured 58 px, so
     `HarnessParts916` labels now have a floor of 4% of the height (opt-in to portrait only).
   - **B07's low reading was not a real failure:** `ClaudeComposerAsk916` is exempt from §8.1.
   - **Landscape copy differs slightly in two places:**
     - B02 portrait shows labels only, with the descriptions moved to narration.
     - B01 portrait breaks the overview into four lines.
   - **The first vertical `./art final` was blocked by GATE T** on B01 (52 px) and B02 (60 px). GATE T
     measures one frame per beat, at the clip midpoint. Probing that exact frame showed the smallest runs
     were lowercase fragments of B01's context title and B02's spark line. Fixes: B01
     `contextTitleSize` 140 in portrait; `HarnessParts916` spark line floored at 3.9% of the height.
     Re-probed at the midpoints: 77 px and 73 px.
   - **Vertical final:** GATE T PASS, Gate V 0 BLOCKER / 0 MAJOR, receipt status `ready`, SHA-256 in `README.md`.
6. **Toolchain notes for this Windows machine:**
   - ffmpeg is not on PATH; use `runtime/bin/ffmpeg-master-latest-win64-gpl/bin`.
   - Scripts need `PYTHONUTF8=1`.
