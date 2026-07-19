# SHOTLIST — agents-md-classroom

**Build an AGENTS.md with Claude: Teach the AI Your Classroom Rules** · 16:9 · ~118s est. (10 beats)
Source: codex-for-teachers/chapters/03-agents-md.md
Series: CODEX FOR TEACHERS — Reel 01 of 10

All beats are SLATE or Remotion motion graphics. No Manim scenes. No AI image generation.

---

## B00 — SLATE (~8s)
"A 100-line markdown document outperforms a 30-minute calibration session…"
Slate: intro hook text on teardown ground.

## B01 — SLATE (~12s)
"Codex starts every session with no memory of the last…"
Slate: problem statement — session memory gap, 200-line ceiling.

## B02 — REMOTION: NikBearBrownTerminalAsk (~12s)
Command: `claude "Generate a 5-section AGENTS.md…"`
runningText: "generating classroom AGENTS.md…"

## B03 — REMOTION: NikBearBrownCodeBlock (~14s)
filename: `AGENTS.md`
Shows five sections: stack commands, style deviations, verification, architectural decisions, environment quirks.

## B04 — SLATE (~20s)
"Generated AGENTS.md: 147 lines, all 5 sections present…"
Slate: output summary — line count, never-rules specificity, under 200 lines.

## B05 — REMOTION: NikBearBrownTerminalAsk (~10s)
Command: Add `AGENTS.override.md` with conflicting rule; ask which file wins.
runningText: "testing hierarchy…"

## B06 — SLATE (~14s)
"Claude correctly identifies AGENTS.override.md as project-level override…"
Slate: hierarchy explanation — override > AGENTS.md > defaults.

## B07 — SLATE (~12s)
"The discipline is writing decisions for your future self…"
Slate: summary — five sections, never-rules as closed decisions.

## B08 — SLATE (~8s)
"Next: turn any task description into a five-element Codex specification."
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
