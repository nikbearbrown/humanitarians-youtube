# BUILD-PROMPT — The Reversal Curse

Single paste-ready Claude Code prompt that builds this reel end to end.
Run from the toolkit root: `G:/Onkar/brutalist.art-main/brutalist.art-main`.

This reel makes **no paid API calls** — Kokoro, Manim and Remotion are local and free.

---

```
Build the reel at G:/Onkar/youtube/claude-stem-reversal-curse end to end, 16:9 master
plus the 9:16 companion.

Doctrine: read skills/make/ai-explainer/SKILL.md in full before touching anything, plus
this reel's CHECKS-REPORT.md, SOURCES.md and BUILD-LOG.md. This is a claude-explainer on
the @HumanitariansAI chip, channel claude-stem, narrated in the FIRST PERSON by Onkar
Bhujbal (Kokoro am_onyx). Never publish.

SHELL PREAMBLE — every shell needs this on Windows:
  export PATH="/c/Users/Tapan/AppData/Local/Programs/Python/Python312:/c/Users/Tapan/AppData/Local/Programs/Python/Python312/Scripts:/c/Users/Tapan/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.0.1-full_build/bin:$PATH"
  export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
Without PYTHONUTF8 the scripts die on 'charmap' codec errors.

GATE 0 — environment
  ./art doctor
  Stop and report if Python, ffmpeg/ffprobe, the Kokoro model, or
  runtime/remotion/node_modules are missing. This is the Fellow Tier: everything needed
  is free. Never work around a missing dependency.

GATE 1 — scene index
  ./art scene-index
  Then verify every pattern this reel uses is renderable:
    ./art scenes --check ReversalTrainingGraph
    ./art scenes --check ReversalTrainingGraph916
    ./art scenes --check ReversalBidirectionalTest
    ./art scenes --check ReversalBidirectionalTest916
    ./art scenes --check ThreeStageBand
    ./art scenes --check HaiTitleOutro
  A pattern that fails --check is a blocker, not a slate.

GATE 2 — audio (the master clock)
  python3 runtime/scripts/generate_audio_kokoro.py \
    G:/Onkar/youtube/claude-stem-reversal-curse
  An empty mp3/ is a FAILED BUILD — report the reason, never ship a silent cut. Write
  measured durations back to actual_duration_s; those are the real clock from here on.
  Hard checks:
    - B01 must land >= 9s (EXECUTIVE-SUMMARY LAW). It also carries lead_silence_s: 0.8.
      If short, lengthen the narration — never speed the typing.
    - B00, B03 and BHTF each type a long command. If any of their audio is under ~7s the
      typing will not finish on screen; lengthen the narration rather than cutting the
      prompt, because HANDOFF LAW requires BHTF's prompt to be read verbatim.

GATE 3 — review cut
  ART_FACTS=0 ./art run G:/Onkar/youtube/claude-stem-reversal-curse
  (Drop ART_FACTS=0 once FACTCHECK.md / SHOTLIST.md / PROMPTS.md exist.)
  Render Remotion ONLY via runtime/scripts/remotion_scenes.py. Never hand-roll
  npx remotion render.

GATE 4 — VISUAL QC (mandatory; the mp4 probe is a file check, not QC)
  Full spec: CLAUDE-CODE-VISUAL-QC-CHECK.md at the toolkit root.
    ffmpeg -i <mp4> -vf fps=2 _qc/frames/%05d.png
    plus each beat at ~15/50/85% of its span from the beat sheet
  Then actually Read the PNGs and audit the 9-point rubric.
  Specific things to look at on this reel:
    B00  — three output lines, each long. Confirm none wraps past the composer card
           or clips at the right edge.
    B02  — three stage names are long ("CONDITIONAL PROBABILITY",
           "UNIDIRECTIONAL WEIGHTS"). Confirm they fit their panels at 56px or wrap
           cleanly rather than clipping.
    B04  — the dashed reverse edge must RETRACT to nothing before the cut; that
           retraction is the whole point of the beat. Also confirm the highlighted
           subject/object boxes do not push the sentence outside the card.
    B05  — the right-hand arrow must show arrowheads at BOTH ends. If only one head
           renders, the beat's entire claim is broken. Check the verdict strip clears
           the title-safe bottom edge.
    B06  — the code block is 10 lines; confirm no line clips at the card's right edge.
    BOUT — the HAI mark must resolve from
           public/logo-outro/humanitarians/humanitarians-logo-1.svg.
  Known trap on this toolkit: a full-safe-width element must not be translated
  horizontally during an entrance — it bleeds past a title-safe edge either way.
  Animate opacity or vertical offset instead.
  Log every defect and fix in _qc/REPORT.md. Fix ROOT CAUSES in the scene source and
  re-render until zero BLOCKER and zero MAJOR.

GATE 5 — type lock
  python3 runtime/scripts/type_check.py (writes TYPECHECK.md)
  No success may be reported while TYPECHECK.md has any FAIL.

GATE 6 — the 9:16 companion
  ./art vertical G:/Onkar/youtube/claude-stem-reversal-curse
  9:16 is a DIFFERENT BEAT SHEET, never a centre-crop (RENDER-TARGETS.md §3).
  B04 and B05 have responsive 916 variants that stack their columns.
  B02 (ThreeStageBand), B06 (ClaudeCodeBeat) and BOUT (HaiTitleOutro) have NO portrait
  variant and WILL be flagged. Do not silently crop them. Either build the 916 variants
  — stack the three stages vertically for B02, reflow per RENDER-TARGETS.md — or report
  the flagged beats and stop. Run the same GATE 4 visual QC on the portrait cut; it is
  a separate render with its own defects.

GATE 7 — master
  ./art final G:/Onkar/youtube/claude-stem-reversal-curse \
    --out G:/Onkar/youtube/claude-stem-reversal-curse
  4K (2160p), no review label. Output: claude-stem-reversal-curse.mp4

KNOWN OPEN ITEMS — read CHECKS-REPORT.md before assuming these are bugs
  - The script asks for 24 fps. Every registered composition is fps={30}; changing it is
    a toolkit-wide edit, not a per-reel prop. The master is 4K/30 unless told otherwise.
  - The script's Scene 4 asks for a red→green arrow flip. Deliberately built as one
    arrowhead vs two in the single-accent Claude palette (BUILD-LOG D2). Do not "fix"
    this by adding a green.
  - The sign-off says "Onkar Bhujbal, for Humanitarians AI." The supplied script's last
    line still reads "Liam, ..." — superseded by the author's instruction (BUILD-LOG D3).
  - Runtime lands ~2:03 against a 2:30 target. Do not pad to hit the target; duration is
    an output (duration-planner).

REPORT
  Finish with: beats filled vs slated, measured runtime vs target, _qc/REPORT.md verdict
  for BOTH aspects, TYPECHECK.md verdict, which beats the vertical pass flagged, and the
  master's path. Do not publish, do not upload, do not create a staging folder.
```
