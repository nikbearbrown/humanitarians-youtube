# BUILD-LOG — kavya-opentelemetry-ai-agents

2026-10-28. Built with Claude Code (AI) at Kavya's request. Local, free path only: Kokoro, Remotion and ffmpeg.

1. **Evidence first.**
   - The OpenTelemetry SDK is not installed. Installing it would mean downloading a package, which was
     not done.
   - Instead, `demo/otel_demo.py` holds a small stdlib tracer shaped like OpenTelemetry's span model,
     with GenAI semantic-convention names. The video says this aloud and on screen.
   - Ran it and saved stdout verbatim to `demo/otel_demo_output.txt`. Checked the arithmetic by hand:
     610 + 11 + 1,780 + 2 = 2,403 ms.
2. **Audio.** Kokoro `am_onyx` produced 9 beats, 137.5 s in total; B01 is 9.84 s.
3. **Timing.** Every reveal was authored as a narration phrase and resolved to beat fractions after the
   audio was measured. `Harness*` scenes take `durationSeconds` to match their audio.
4. **Landscape.**
   - Previews passed the frame checker, but a visual look showed B04's 13-line span tree clipping its
     last line. On screen, B04 drops the repeated `question:` line and the blank spacer; all shown
     lines are verbatim.
   - Landscape final passed on the first try: GATE T PASS, Gate V 0 BLOCKER / 0 MAJOR, receipt status `ready`.
5. **Vertical.**
   - Applied the portrait patch learned on the earlier films:
     - B01: four short lines, a larger title and the name label.
     - B02: labels only.
     - B03/B04: short prompt path and no blank lines.
     - B04: also drops the repeated "scripted" line, which B03 and B05 already show, so the tree fits.
   - Gate V flagged B01: "is the agent's flight recorder." overran the left title-safe edge. The
     portrait correction was shortened to "a flight recorder".
   - Vertical final passed on the first export: GATE T PASS, Gate V 0 BLOCKER / 0 MAJOR, receipt status `ready`.
6. **Toolchain notes for this Windows machine:**
   - ffmpeg is not on PATH; use `runtime/bin/ffmpeg-master-latest-win64-gpl/bin`.
   - Scripts need `PYTHONUTF8=1`.
