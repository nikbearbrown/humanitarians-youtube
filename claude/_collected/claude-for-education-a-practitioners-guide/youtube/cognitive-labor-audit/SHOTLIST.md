# SHOTLIST — cognitive-labor-audit

**Audit a Prompt for Cognitive Labor Transfer with Claude** · 16:9 · ~113s est. (10 beats)
Source: claude-for-education-a-practitioners-guide/chapters/04-lesson-planning-and-activity-design.md
Series: CLAUDE FOR EDUCATION — Reel 02 of 09

Beats: Remotion motion graphics + ONE Manim scene (B04_CognitiveLaborChart). No AI image generation.

---

## B00 — REMOTION: NikBearBrownOpen (~10s)
Brand open. 5 topic lines: Nik Bear Brown / Brutalist + Educational AI / Cognitive Labor Audit / Who Does the Thinking? / Build with Claude CLI

## B01 — SLATE (~12s)
"Most instructional prompts don't ask students to think…"
Slate: problem hook — the invisible difference. No CLI yet.

## B02 — REMOTION: NikBearBrownTerminalAsk (~15s)
Command: pipe prompt.txt to claude, audit cognitive labor, return ratio.
runningText: "running cognitive audit…"

## B03 — REMOTION: NikBearBrownCodeBlock (~15s)
filename: `cognitive_audit.py`
Shows subprocess call, re.findall ratio extraction, print output.

## B04 — MANIM: B04_CognitiveLaborChart (~14s)
Horizontal bar chart. Four learning objectives as rows. Bars animate to show student/AI/shared split. Summary ratio bar appears at bottom with legend.

## B05 — REMOTION: NikBearBrownTerminalAsk (~15s)
Command: rewrite prompt to shift cognitive labor to student (predict before Claude, then compare), re-audit.
runningText: "shifting labor to student…"

## B06 — SLATE (~10s)
"The revised prompt shifts the ratio from forty to seventy-five percent…"
Slate: before/after ratio comparison.

## B07 — SLATE (~12s)
"Cognitive labor is zero-sum in the moment…"
Slate: teardown summary.

## B08 — SLATE (~6s)
"Next: Build an Assessment Vulnerability Map…"
Slate: next reel teaser.

## B09 — REMOTION: NikBearBrownOutro (~8s)
Standard outro props.

---

## Slot inventory

| Slot | Need | Status |
|------|------|--------|
| B00 | Remotion: NikBearBrownOpen | Remotion render needed |
| B01 | Problem slate | vox_compile auto-generates |
| B02 | Remotion: NikBearBrownTerminalAsk | Remotion render needed |
| B03 | Remotion: NikBearBrownCodeBlock | Remotion render needed |
| B04 | Manim: B04_CognitiveLaborChart | Manim render (vox_run.sh) |
| B05 | Remotion: NikBearBrownTerminalAsk | Remotion render needed |
| B06 | Output slate | vox_compile auto-generates |
| B07 | Summary slate | vox_compile auto-generates |
| B08 | Next-steps slate | vox_compile auto-generates |
| B09 | Remotion: NikBearBrownOutro | Remotion render needed |
