# PROMPTS — death-of-the-generic-resume
# Beat-prefixed generation prompts. No open pantry slots — this reel is
# built entirely from self-generated Manim/Remotion visuals (ai-explainer
# chassis, not deep-explainer's pantry/vox lane), so there is nothing to
# source or shop for. Kept for GATE F completeness.

Every non-composer beat (B01–B12) is a from-scratch Manim scene in
scenes.py, authored directly against the beat's narration and
`shot.visual_intent`. The two composer beats' "prompt" IS the on-screen
content (see beat_sheet.json `shot.remotion.props.command` for B00/B13)
and is not a separate generation task.

For reference, the two prompts a viewer would actually paste into Claude
Code, framing this reel's two Claude-composer beats:

## B00 — the cold open ask

```
claude "help me put into words a pattern I keep noticing every time I apply for a job"
```

## B13 — the handoff (HANDOFF LAW — read aloud and discussed in narration)

```
claude "here's a job rejection I got less than a minute after
  applying. Help me think through what an automated filter
  might have caught — and what's probably just noise."
```
