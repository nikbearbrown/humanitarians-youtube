# SHOTLIST — grading-tool-survey

**Build the Grading Tool Phase 1 with Claude: Survey Before You Grade** · 16:9 · ~118s est. (10 beats)
Source: codex-for-teachers/chapters/08-grading-tool-build.md
Series: CODEX FOR TEACHERS — Reel 04 of 10

All beats are SLATE or Remotion motion graphics. No Manim scenes. No AI image generation.

---

## B00 — SLATE (~8s)
"The first build step is the safest one — and the one everyone skips…"
Slate: intro hook text on teardown ground.

## B01 — SLATE (~12s)
"Phase 1 of the grading tool is the survey pass…"
Slate: problem statement — read-only guarantee, --dry-run flag.

## B02 — REMOTION: NikBearBrownTerminalAsk (~12s)
Command: implement survey.py — .py/.ipynb/.zip, table output, --dry-run, standard library.
runningText: "building survey phase…"

## B03 — REMOTION: NikBearBrownCodeBlock (~14s)
filename: `survey.py`
Shows pathlib iteration, zipfile inspection, formatted table, argparse, sys.exit(0).

## B04 — SLATE (~20s)
"survey.py generated: standard library only (verified)…"
Slate: output — 5 test submissions, all mtimes unchanged, read-only guarantee holds.

## B05 — REMOTION: NikBearBrownTerminalAsk (~10s)
Command: add --format filter flag to list only Python submissions.
runningText: "extending with format filter…"

## B06 — SLATE (~14s)
"Extended survey.py: --format py lists only Python submissions…"
Slate: extension verified read-only post-change, AGENTS.md never-rules protect the constraint.

## B07 — SLATE (~12s)
"Phase 1 is the conducting discipline before stakes are real…"
Slate: summary — list, report, exit; --dry-run makes the guarantee testable.

## B08 — SLATE (~8s)
"Next: generate-evaluate-select — why one Claude response is a default, not a choice."
Slate: next-steps bridge card.

## B09 — REMOTION: NikBearBrownOutro (~8s)
Standard outro props.

---

## Slot inventory

| Slot | Need | Status |
|------|------|--------|
| B00 | Intro slate | vox_compile auto-generates |
| B01 | Problem slate | vox_compile auto-generates |
| B02 | Remotion: NikBearBrownTerminalAsk | Remotion render needed |
| B03 | Remotion: NikBearBrownCodeBlock | Remotion render needed |
| B04 | Output slate | vox_compile auto-generates |
| B05 | Remotion: NikBearBrownTerminalAsk | Remotion render needed |
| B06 | Output slate | vox_compile auto-generates |
| B07 | Summary slate | vox_compile auto-generates |
| B08 | Next-steps slate | vox_compile auto-generates |
| B09 | Remotion: NikBearBrownOutro | Remotion render needed |

All open Remotion slots → `media/<BID>.mp4` via `vox_remotion.py`.
