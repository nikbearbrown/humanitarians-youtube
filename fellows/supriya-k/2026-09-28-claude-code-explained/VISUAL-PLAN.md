# VISUAL-PLAN — claude-code-explained

No invented datasets: every number on screen is one of the sourced figures in `FACTCHECK.md`
(139.5 kbps · 15–20% · 55% → 86% · 276 → 341 kbps · 25–28% → full frame · 14.222 → 4.5).

## Per-beat visual plan

| Beat | Shot | Motion | Handle |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | cold open, greeting "Hi, I am Supriya", ask lands answered with 4 output lines (plan · gate · execute · verify) | `folderLabel` |
| B01 | Manim `B01_CannotWatch` | probe readout ticks green line by line; beside it a portrait frame whose text block holds only the top fifth; "~1/5" bracket; crimson 139.5 kbps counter | corner text |
| B02 | Manim `B02_TheLoop` | 4 nodes build clockwise as spoken, each tagged with its real file; terracotta return arrow VERIFY → PLAN on "back to plan" | corner text |
| B03 | `ClaudeComposerAsk` | "The ask," · `rebuilding the layout…` | `folderLabel` |
| B04 | `ClaudeCodeBeat` | `ClaudeComposerAsk916.tsx`, chip `TSX`, spark "Position, not size." | `handle` chip |
| B05 | Manim `B05_FillBefore_After` | two portrait frames; height brackets 55% (crimson) → 86% (teal); kbps counters 276 → 341 | corner text |
| B06 | `ClaudeComposerAsk` | "The revision," · `updating…` | `folderLabel` |
| B07 | `ClaudeCodeBeat` | `short/scenes.py`, chip `PYTHON`, spark "Two lines. Whole frame." | `handle` chip |
| B08 | Manim `B08_WholeFrame` | small centered cluster + crimson "audit: PASS"; grid rescales, content expands edge to edge; tag → teal "Gate V: 0 BLOCKER · 0 MAJOR" | corner text |
| B09 | Manim `B09_FourMoves` | 4-row checklist with owner tags; closing line writes on | corner text |
| B10 | `ClaudeComposerAsk` | "Your turn." · `paste this into Claude…` | `folderLabel` |
| B11 | `ClaudeTitleOutroFilled` | title restate, full-size "Supriya", "Built with Claude." | full-size |

Palette: Claude fidelity tokens (cream `#FAF9F5`, ink `#3D3929`, one terracotta `#D97757`), with
teal `#1F6F5C` / crimson `#BF3339` for pass/fail as in v2. The Manim corner handle is a shared
`handle()` helper: low opacity, lower-right, inside the safe area (LOGO LAW).

## 16:9 checklist (3840×2160)

- [ ] Manim at `-qk`; code type ≥ the 24px floor; no line clipped (`whiteSpace: pre` clips silently).
- [ ] Every reveal lands by p ≈ 0.6 (MISS #5 truncation); check each beat's last frame.
- [ ] `compile.py --height 2160 --vbitrate …`; ffprobe the master.

## 9:16 checklist (2160×3840) — fill at EVERY beat type

- [ ] **Title/composer** (B00/B03/B06/B10): `ClaudeComposerAsk916`; commands ≤ ~110 chars; B00's
      4 output lines visible (COLD OPEN LAW); content spans ≳ 80% of height.
- [ ] **Code** (B04/B07): `ClaudeCodeBeat916` with the `handle` chip; card fills ~85% width.
- [ ] **Manim** (5 beats): portrait classes in `short/scenes.py` with the `frame_width = 4.5`
      lines; `next_to` chains only.
- [ ] **Outro** (B11): `ClaudeTitleOutroFilled916`; endcard `END.png` native 2160×3840,
      `--handle Supriya`.
- [ ] Look at frames per beat type in `short/_qc/`, then Gate V, then ffprobe.
