# PROMPTS — weekly-recap
# No open pantry slots — this reel is built entirely from self-generated
# Manim/Remotion visuals plus two real, actually-run Python scripts. Kept
# for GATE F completeness.

Every Manim beat (B01, B04, B07, B08) is a from-scratch scene in scenes.py,
authored directly against the beat's narration and `shot.visual_intent`.
Every composer/code beat's on-screen content IS the prompt/code shown — see
beat_sheet.json `shot.remotion.props` for B00/B02/B03/B05/B06/B09.

For reference, the four prompts a viewer would actually paste into Claude
Code, framing this reel's CLI loop:

## B00 — the cold open ask

```
claude "help me build a real log of what I actually did this week"
```

## B02 — the ask (cycle 1)

```
claude "write weekly_recap_v1.py -- log this week:
  the article, the video, what's next"
```

## B05 — the change (cycle 2, the required revision)

```
claude "update weekly_recap_v1.py -> weekly_recap_v2.py:
  -> split into DONE THIS WEEK vs STARTING NEXT WEEK"
```

## B09 — the handoff (HANDOFF LAW — read aloud and discussed)

```
claude "write me a weekly_recap.py that logs my actual
  week, split into what's done and what's just starting"
```
