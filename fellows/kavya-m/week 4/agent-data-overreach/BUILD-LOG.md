# BUILD-LOG — kavya-agent-data-overreach

2026-10-28. Built with Claude Code (AI) at Kavya's request. Local, free path only: Kokoro, Remotion and ffmpeg.

1. **Evidence first.** Wrote and ran `demo/overreach_demo.py` (stdlib `sqlite3`, fake data); stdout
   saved verbatim to `demo/overreach_demo_output.txt`.
2. **Audio.** Kokoro `am_onyx` produced 9 beats, 137.4 s in total; B01 is 9.71 s.
3. **Timing.** Reveals were authored as narration phrases, then resolved to beat fractions after the
   audio was measured. `Harness*` scenes take `durationSeconds` to match their audio.
4. **Landscape.**
   - Previews passed the frame checker, but a visual look showed B05's left items wrapping past the
     card's bottom edge. The on-screen items were compressed ("other customers", "unneeded tables",
     "unlogged lookups"); the narration keeps the full wording.
   - Landscape final passed on the first export: GATE T PASS, Gate V 0 BLOCKER / 0 MAJOR, receipt
     status `ready`.
5. **Vertical.**
   - Applied the standard portrait patch:
     - B01: four short lines, a larger title and the name label.
     - B02: labels only.
     - B03/B04: short prompt path and no blank lines.
   - Gate V and a visual check then flagged three long texts:
     - B03: the spark line wrapped behind the terminal; now "Wider than the task.".
     - B03/B04: the window titles wrapped; now "wide credential" / "scoped credential".
     - B02: "Enforced in the tool" wrapped and pushed the footer past the bottom edge. The label is now
       "Tool-enforced", the spark line is "A scoped credential.", and the footer was dropped in portrait
       (the narration says it).
   - The first vertical `./art final` was blocked by GATE T §8.3 on B01. At the clip midpoint the writer
     shows the words it is about to delete in terracotta `#D97757`, which is 2.74:1 on cream (floor 4.5:1).
     Portrait B01 now uses the doctrine's darker terracotta `#A44A32` (about 5.5:1) as its `accent`.
   - Vertical final: GATE T PASS, Gate V 0 BLOCKER / 0 MAJOR, receipt status `ready`.
6. **Toolchain notes for this Windows machine:**
   - ffmpeg is not on PATH; use `runtime/bin/ffmpeg-master-latest-win64-gpl/bin`.
   - Scripts need `PYTHONUTF8=1`.
