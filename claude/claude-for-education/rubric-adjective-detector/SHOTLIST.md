# SHOTLIST — rubric-adjective-detector

**Build a Rubric Adjective Detector with Claude** · 16:9 · ~113s est. (10 beats)
Source: claude-for-education-a-practitioners-guide/chapters/07-rubrics-exemplars-and-criteria.md
Series: CLAUDE FOR EDUCATION — Reel 01 of 09

All beats are SLATE or Remotion motion graphics. No Manim scenes. No AI image generation.

---

## B00 — REMOTION: NikBearBrownOpen (~10s)
Brand open. 5 topic lines: Nik Bear Brown / Brutalist + Educational AI / Rubric Adjective Detector / Observable vs Vague Criteria / Build with Claude CLI

## B01 — SLATE (~12s)
"The rubrics most teachers use are written in a language Claude can game perfectly…"
Slate: problem hook — rubric cell with quality adjective. No CLI yet.

## B02 — REMOTION: NikBearBrownTerminalAsk (~15s)
Command: pipe rubric.md to claude, classify observable vs vague, rewrite vague as observable.
runningText: "running rubric audit…"

## B03 — REMOTION: NikBearBrownCodeBlock (~15s)
filename: `rubric_audit.py`
Shows subprocess call, three-column output parsing, formatted diff.

## B04 — SLATE (~14s)
"The output shows the classification…"
Slate: two-column before/after. Vague criterion in amber, observable rewrite in black.

## B05 — REMOTION: NikBearBrownTerminalAsk (~15s)
Command: pipe rewritten rubric back through Claude, ask for top-scoring student submission.
runningText: "generating top-score submission…"

## B06 — SLATE (~10s)
"The vague rubric produces an essay that sounds insightful…"
Slate: side-by-side submission comparison.

## B07 — SLATE (~12s)
"Vague rubric criteria don't fail because they are unclear to humans…"
Slate: teardown summary. 'Vague = AI-gameable. Observable = verifiable.'

## B08 — SLATE (~6s)
"Next: Audit a Prompt for Cognitive Labor Transfer…"
Slate: next reel teaser card.

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
| B04 | Output slate | vox_compile auto-generates |
| B05 | Remotion: NikBearBrownTerminalAsk | Remotion render needed |
| B06 | Output slate | vox_compile auto-generates |
| B07 | Summary slate | vox_compile auto-generates |
| B08 | Next-steps slate | vox_compile auto-generates |
| B09 | Remotion: NikBearBrownOutro | Remotion render needed |
