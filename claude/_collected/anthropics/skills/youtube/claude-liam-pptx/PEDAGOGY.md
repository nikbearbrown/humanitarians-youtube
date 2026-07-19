# PEDAGOGY — claude-liam-pptx

Skill: `pptx` · Modifier: `skill-teardown`

## PREDICT (viewer question before watching)
"Can't Claude just write python-pptx to make slides? Why does this need its own skill?"

## What the viewer will learn
1. The skill routes to three different tools: markitdown (read), editing.md workflow (edit template), pptxgenjs (create from scratch)
2. Design is mandatory, not optional — the skill specifies color palettes, layout patterns, typography, and explicit avoidances
3. QA requires visual inspection with subagents — "assume there are problems; your first render is almost never correct"

## CONFIRM (what the reel reveals)
- TRIGGER: "deck", "slides", "presentation", .pptx filename — anything touching a pptx file
- 3 paths: read → markitdown; edit template → editing.md workflow; create scratch → pptxgenjs
- Design rules: one dominant color (60-70%), commit to a visual motif, dark/light sandwich structure, never accent lines under titles
- QA mandate: content QA (markitdown + grep for placeholders) + visual QA (subagents with fresh eyes)

## LAWS CHECKED
- ✅ TRIGGER is clear: "deck" / "slides" / "presentation" / .pptx filename
- ✅ SELF-DEMO: B02 shows verbatim design rules and avoidances from SKILL.md
- ✅ HANDOFF LAW: BHTF narration reads prompt aloud AND explains what to watch for
- ✅ ILLUSTRATE LAW: UI only at B00 and BHTF bookends
- ✅ ASK→RESULT law: B00 shows ask + TRIGGER + result

## VERDICT: PASS
