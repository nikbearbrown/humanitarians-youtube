# BUILD-PROMPT — The Gatekeeper Needs Ground Truth

Single paste-ready Claude Code prompt that builds this reel end to end.
Run from the toolkit root: `G:/Onkar/brutalist.art-main/brutalist.art-main`.

Appropriate under `--dangerously-skip-permissions` only once the seatbelt rules
hold (regenerable outputs, no paid calls). This reel makes **no paid API calls** —
Kokoro, Manim and Remotion are local and free.

---

```
Build the reel at G:/Onkar/youtube/claude-hai-gatekeeper-ground-truth end to end.

Doctrine: read skills/make/ai-explainer/SKILL.md in full before touching anything,
plus the reel's own CHECKS-REPORT.md, SOURCES.md and BUILD-LOG.md. This is a
claude-explainer on the @HumanitariansAI chip, narrated by Liam (Kokoro am_onyx).
Never publish.

GATE 0 — environment
  ./art doctor
  Stop and report if Python, ffmpeg/ffprobe, the Kokoro model, or
  runtime/remotion/node_modules are missing. Do not work around a missing
  dependency: this is the Fellow Tier, everything needed is free.

GATE 1 — scene index
  ./art scene-index
  Six components were added for this reel and are registered in Root.tsx but are
  NOT yet in scenes.json:
    GatekeeperCorpusTable, GatekeeperTaxonomy, GatekeeperIngestFlow,
    GatekeeperVerifyLoop, GatekeeperScoreboard, GatekeeperTitleOutro
  Then verify each one renders:
    ./art scenes --check GatekeeperCorpusTable      (and the other five)
  A component that fails --check is a blocker, not a slate.

GATE 2 — audio (the master clock)
  python3 runtime/scripts/generate_audio_kokoro.py \
    G:/Onkar/youtube/claude-hai-gatekeeper-ground-truth
  Every beat gets mp3/beat-<BID>.mp3. An empty mp3/ is a FAILED BUILD — report the
  reason, never ship a silent cut. Write the measured durations back to
  actual_duration_s on each beat; those are the real clock from here on.
  Hard check: B01 must land >= 9s of audio window. If it is short, lengthen the
  narration — never speed the typing. B01 also carries lead_silence_s: 0.8.

GATE 3 — review cut
  ./art run G:/Onkar/youtube/claude-hai-gatekeeper-ground-truth
  Render Remotion ONLY via runtime/scripts/remotion_scenes.py. Never hand-roll
  npx remotion render.

GATE 4 — VISUAL QC (mandatory; the mp4 probe is a file check, not QC)
  Full spec: CLAUDE-CODE-VISUAL-QC-CHECK.md at the toolkit root.
    ffmpeg -i <mp4> -vf fps=2 _qc/frames/%05d.png
    plus each beat at ~15/50/85% of its span from the beat sheet
  Then actually Read the PNGs and audit the 9-point rubric: edge bleed, title-safe
  margins, container overflow, collision, offscreen anchors, legibility, brand bug
  placement, aspect, and CANVAS FILL.
  Specific things to look at on this reel:
    B02 — the four-column table must not collide at the VARIANCE column; the
          50+ counter must not crowd the bottom safe edge (SAFE.b = 1026).
    B03 — three cards at ~549px each: confirm the rule text and the mono
          claim/truth lines wrap rather than clip.
    B06 — the travelling doc_01 token must stay inside SAFE at both ends of
          its path.
    B07 — four nodes at ~399px each: 'QUARANTINE' is the longest label; confirm
          it fits at 44px or the card wraps cleanly.
    B09 — RESULT bar must hold >= 2s before the cut.
    BOUT — the HAI mark must resolve from
           public/logo-outro/humanitarians/humanitarians-logo-1.svg.
  Log every defect and fix in _qc/REPORT.md. Fix ROOT CAUSES in the scene source
  and re-render until zero BLOCKER and zero MAJOR. A build that was never visually
  inspected is not done.

GATE 5 — type lock
  python3 runtime/scripts/type_check.py (writes TYPECHECK.md)
  No success may be reported while TYPECHECK.md has any FAIL.

GATE 6 — master
  ./art final G:/Onkar/youtube/claude-hai-gatekeeper-ground-truth \
    --out G:/Onkar/youtube/claude-hai-gatekeeper-ground-truth
  4K (2160p), no review label. Output: claude-hai-gatekeeper-ground-truth.mp4

KNOWN HOLD — B05
  The real ingest.py was never supplied, so B05 renders as a PIPELINE slate by
  design (DOUBLE-CHECK LAW: do not fabricate a code listing). If the human has
  since dropped the file at media/B05.code.txt, set the ClaudeCodeBeat `code` prop
  from it (trim to ~16 lines: read path, encode call, collection.add call),
  re-render, and update CHECKS-REPORT.md to 12 SHOW / 0 HOLD. Otherwise leave the
  slate and say so in the report.

KNOWN OPEN — B02/B03 illustrative rows
  Only doc_01 is from the source. If real corpus rows have been supplied, swap
  them in and update SOURCES.md. Otherwise leave them and keep them flagged.

REPORT
  Finish with: beats filled vs slated, measured runtime vs the 234s estimate,
  _qc/REPORT.md verdict, TYPECHECK.md verdict, and the master's path. Do not
  publish, do not upload, do not create a staging folder.
```
