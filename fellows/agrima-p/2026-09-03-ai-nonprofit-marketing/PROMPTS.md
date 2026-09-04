# PROMPTS — ai-nonprofit-marketing
# No open pantry slots — this reel is built entirely from self-generated
# Manim/Remotion visuals sourced from the article. No archival/screenshot
# assets needed; the user confirmed none exist for this topic.

Every non-composer beat (B00B, B01–B09) is a from-scratch Manim scene in
scenes.py, authored directly against the beat's narration and
`shot.visual_intent`. The two composer beats' "prompt" IS the on-screen
content (see beat_sheet.json `shot.remotion.props.command` for B00/B10)
and is not a separate generation task.

For reference, the two prompts a viewer would actually paste into Claude
Code, framing this reel's two Claude-composer beats:

## B00 — the cold open ask

```
claude "help me understand how AI is actually helping nonprofit marketing teams"
```

## B10 — the handoff (HANDOFF LAW — read aloud and discussed)

```
claude "help me find one AI tool my team could
  actually start using this week for donor outreach"
```
