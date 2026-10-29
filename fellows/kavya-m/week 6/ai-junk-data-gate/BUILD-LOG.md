# BUILD-LOG — kavya-ai-junk-data-gate

2026-10-29. Script drafted by Kavya Mehta with help from Claude Code. Local, free path only: Kokoro, Remotion and ffmpeg.

1. **Evidence first.**
   - Wrote and ran `demo/junk_gate_demo.py` (stdlib, 20 synthetic rows, half junk).
   - The first run quarantined 9, not 10. Row 202, the first copy of the templated comment, passed,
     because its twin (row 201) was rejected for "no source" before its text was recorded.
   - Kept that result as found, and made the demo print the row that slipped and the true average.
   - Checked the arithmetic by hand: 86 ÷ 20 = 4.30; (34 + 5) ÷ 11 = 3.55; 34 ÷ 10 = 3.40.
2. **Audio.** Kokoro `am_onyx` produced 9 beats, 146.3 s in total; B01 is 11.67 s.
3. **Timing.** Reveals were authored as narration phrases and resolved after the audio was measured.
   Terminal lines are forced to appear top to bottom, so no line appears before the line above it.
4. **Landscape.**
   - All previews passed the frame checker and a visual look.
   - The render chain died before B08 with a Windows "fork: resource temporarily unavailable" error.
     An orphaned ffmpeg (about 3.2 GB) was left from that run. B08 failed once more while it was still
     running, then rendered after it exited.
   - Final passed: GATE T PASS, Gate V 0 BLOCKER / 0 MAJOR, receipt status `ready`.
5. **Vertical.**
   - The portrait patch was applied up front, using what the earlier films taught:
     - B01: four short lines, a larger title, and the darker accent `#A44A32` for contrast.
     - B02: labels only, a short spark line, no footer.
     - B03/B04: short paths and titles, no blank lines.
   - Preview: B05 sat exactly on the 55% fill threshold at its midpoint, so its footer now appears 0.6 s
     earlier in portrait.
   - Vertical final passed on the first export: GATE T PASS, Gate V 0 BLOCKER / 0 MAJOR, receipt status `ready`.
6. **Toolchain notes for this Windows machine:**
   - ffmpeg is not on PATH; use `runtime/bin/ffmpeg-master-latest-win64-gpl/bin`.
   - Scripts need `PYTHONUTF8=1`.
   - Long render chains can exhaust Windows process resources.
