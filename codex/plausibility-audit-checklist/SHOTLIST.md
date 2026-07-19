# SHOTLIST — plausibility-audit-checklist

**Build a Plausibility Audit Checklist with Claude: Name the Five Capacities** · 16:9 · ~118s est. (10 beats)
Source: codex-for-teachers/chapters/06-five-supervisory-capacities.md
Series: CODEX FOR TEACHERS — Reel 09 of 10

All beats are SLATE or Remotion motion graphics. No Manim scenes. No AI image generation.

---

## B00 — SLATE (~8s)
"When a build goes wrong, it is not a mystery. It is one of five named failures…"
Slate: intro hook text on teardown ground.

## B01 — SLATE (~12s)
"Five supervisory capacities: PA, PF, TO, IJ, EI…"
Slate: problem statement — build log as narrative vs. diagnostic.

## B02 — REMOTION: NikBearBrownTerminalAsk (~12s)
Command: Python script reading build log, capacity report, markdown table, unlabeled steps. Standard library.
runningText: "building audit script…"

## B03 — REMOTION: NikBearBrownCodeBlock (~14s)
filename: `capacity_audit.py`
Shows argparse, re.findall for labels, context extraction, markdown table, unlabeled detection.

## B04 — SLATE (~20s)
"Script run on 13-step build log: PA 3, PF 1, TO 2, IJ 4, EI 2, none 1…"
Slate: output — capacity table correct against chapter ground truth, step 8 gap detected.

## B05 — REMOTION: NikBearBrownTerminalAsk (~10s)
Command: add --missing flag, print only unlabeled steps, suggest absent capacity by keyword.
runningText: "adding --missing flag…"

## B06 — SLATE (~14s)
"Step 8 flagged. Keyword analysis suggests EI absent — logic in loop-closing step…"
Slate: suggestion specific enough to act on in next session.

## B07 — SLATE (~12s)
"Naming the capacities as they fire makes the practice visible, durable, and teachable…"
Slate: summary — audit script as diagnostic artifact, --missing closes the loop.

## B08 — SLATE (~8s)
"Next: research what the bias literature actually says about AI grading."
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
