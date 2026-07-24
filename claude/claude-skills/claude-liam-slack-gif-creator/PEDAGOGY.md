# PEDAGOGY — claude-liam-slack-gif-creator

Skill: `slack-gif-creator` · Modifier: `skill-teardown`

## PREDICT (viewer question before watching)
"Can't Claude just write a Python GIF script? Why does a Slack GIF need its own skill?"

## What the viewer will learn
1. Slack has exact specs that matter: emoji GIFs must be 128×128, under 3 seconds, 48–128 colors; message GIFs at 480×480 — the skill bakes these in and validates compliance before delivery
2. Three utilities abstract the hard parts: GIFBuilder (frame assembly + optimization), validators (Slack compliance check), easing functions (7 motion curves for smooth animation)
3. The animation logic itself uses PIL ImageDraw primitives directly — the skill provides knowledge and utilities, not rigid templates

## CONFIRM (what the reel reveals)
- TRIGGER: "make me a GIF of X for Slack", "animate this for Slack", "Slack emoji GIF"
- Two format tracks: emoji (128×128, ≤3s) and message (480×480)
- Core workflow: GIFBuilder → add frames with PIL primitives → save with color optimization
- 8 animation concepts: shake, pulse, bounce, spin, fade, slide, zoom, explode/particles
- Validator checks Slack compliance; easing functions: linear/ease_in/ease_out/bounce_out/elastic_out/back_out/ease_in_out

## LAWS CHECKED
- ✅ TRIGGER is clear: "make me a GIF for Slack" / "animate this for Slack"
- ✅ SELF-DEMO: B02 shows animation concepts verbatim from SKILL.md
- ✅ HANDOFF LAW: BHTF narration reads prompt aloud AND explains what to watch for
- ✅ ILLUSTRATE LAW: UI only at B00 and BHTF bookends
- ✅ ASK→RESULT law: B00 shows ask + TRIGGER + result

## VERDICT: PASS
