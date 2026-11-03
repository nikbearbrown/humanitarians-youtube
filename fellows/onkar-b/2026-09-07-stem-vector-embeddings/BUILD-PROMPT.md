# BUILD-PROMPT — The Geometry of Meaning

Paste-ready Claude Code prompt that rebuilds this reel end to end.
Run from the toolkit root: `G:/Onkar/brutalist.art-main/brutalist.art-main`.
No paid API calls — Kokoro, Manim and Remotion are local and free.

---

```
Build the reel at G:/Onkar/youtube/claude-stem-geometry-of-meaning end to end, 16:9
master plus the 9:16 companion.

Doctrine: read skills/make/ai-explainer/SKILL.md in full, plus this reel's
CHECKS-REPORT.md, SOURCES.md and BUILD-LOG.md. claude-explainer, channel claude-stem,
chip @HumanitariansAI, narrated FIRST PERSON by Onkar Bhujbal (Kokoro am_onyx).
Never publish.

SHELL PREAMBLE — required on Windows, every shell:
  export PATH="/c/Users/Tapan/AppData/Local/Programs/Python/Python312:/c/Users/Tapan/AppData/Local/Programs/Python/Python312/Scripts:/c/Users/Tapan/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.0.1-full_build/bin:$PATH"
  export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
Without PYTHONUTF8 the scripts die on 'charmap' codec errors.

GATE 0 — environment
  ./art doctor
  Stop if Python, ffmpeg/ffprobe, the Kokoro model or runtime/remotion/node_modules are
  missing. Fellow Tier: everything needed is free. Never work around a missing dep.

GATE 1 — scene index
  ./art scene-index
  Verify every pattern this reel uses:
    EmbeddingScatter2D · EmbeddingScatter2D916
    SimilarityBlindspot · SimilarityBlindspot916
    ThreeStageBand · ThreeStageBand916
    ClaudeComposerAsk916 · BrutalistHesitantWriter916
    ClaudeCodeBeat916 · HaiTitleOutro · HaiTitleOutro916
  A pattern failing --check is a blocker, not a slate.

GATE 2 — audio (the master clock)
  python3 runtime/scripts/generate_audio_kokoro.py \
    G:/Onkar/youtube/claude-stem-geometry-of-meaning
  Empty mp3/ is a FAILED BUILD. Hard checks on measured durations:
    - B01 >= 9s (EXECUTIVE-SUMMARY LAW); it also carries lead_silence_s: 0.8.
    - B00, B03 and BHTF each type a long command. Any of them under ~7s and the typing
      will not finish on screen — lengthen the NARRATION, never shorten the prompt
      (HANDOFF LAW requires BHTF's prompt be read verbatim).

GATE 3 — review cut
  ART_FACTS=0 ./art run G:/Onkar/youtube/claude-stem-geometry-of-meaning
  Render Remotion ONLY via runtime/scripts/remotion_scenes.py. Never hand-roll
  npx remotion render.

GATE 4 — VISUAL QC (mandatory; the gate passing is NOT sufficient)
  This reel's five known defects ALL survived a clean 0-BLOCKER GATE V pass. Sample
  frames and READ them:
    ffmpeg -i <mp4> -vf fps=2 _qc/frames/%05d.png
    plus each beat at ~15/50/85% of its span
  Look specifically at:
    B04 — does the DOG-WOLF link cross either label? is the link caption on screen and
          not clipped off the top? are point labels inside the plot border? do the
          CANINE/FELINE captions collide with a point label? is the plot filling the
          safe square?
    B05 — is the bar's fill consistent with the printed 0.82? do "hot" and "cold" both
          light terracotta before the cut?
    B02 — "N-DIMENSIONAL MAPPING" is long; confirm it fits its panel.
    B06 — 11 code lines; confirm none clips at the card's right edge.
    BOUT — the HAI mark must resolve from
           public/logo-outro/humanitarians/humanitarians-logo-1.svg.
  Standing trap: a full-safe-width element must not be translated horizontally during an
  entrance — it bleeds past a title-safe edge. Animate opacity or vertical offset.
  Second standing trap: every animation must FINISH BY ~p0.80. compile.py conforms each
  clip to measured audio and silently trims the tail.
  Log defects and fixes in _qc/REPORT.md. Fix root causes in the scene source and
  re-render until zero BLOCKER and zero MAJOR.

GATE 5 — type lock
  python3 runtime/scripts/type_check.py   (writes TYPECHECK.md)
  No success may be reported while TYPECHECK.md has any FAIL.

GATE 6 — the 9:16 companion
  ./art vertical G:/Onkar/youtube/claude-stem-geometry-of-meaning
  python3 runtime/scripts/remotion_scenes.py <reel>/vertical
  python3 runtime/scripts/compile.py <reel>/vertical --review --height 1920
  All 9 beats have 916 variants, so nothing should be flagged. If anything IS flagged,
  do NOT let it centre-cut — build the variant or stop and report.
  Run GATE 4 again on the portrait cut: it is a separate render with its own defects,
  and compile.py --review does NOT run GATE V.

GATE 7 — master
  ./art final G:/Onkar/youtube/claude-stem-geometry-of-meaning \
    --out G:/Onkar/youtube/claude-stem-geometry-of-meaning

DO NOT "FIX" THESE — they are deliberate, see BUILD-LOG.md
  - X-axis reads WILD (left) <-> DOMESTIC (right), which is the reverse of the script's
    caption. The script's own coordinates and VO require it (SOURCES.md §1).
  - 0.82 on B05 is the author's illustrative figure, not a measurement.
  - The reel signs off "Onkar Bhujbal, for Humanitarians AI." The script's last line
    still says "Liam, ..." — superseded by the author's instruction.
  - Runtime ~2:05 vs a 2:30 target. Do not pad; duration is an output.

REPORT
  Beats filled vs slated, measured runtime vs target, _qc verdict for BOTH aspects,
  TYPECHECK.md verdict, any beats the vertical pass flagged, and the master's path.
  Do not publish, do not upload, do not create a staging folder.
```
