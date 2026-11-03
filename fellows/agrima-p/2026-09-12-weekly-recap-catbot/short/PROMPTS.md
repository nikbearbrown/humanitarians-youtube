# PROMPTS — weekly-recap-catbot/short

No pantry/archival assets used — every non-composer beat is a from-scratch
portrait Manim scene in scenes.py; every composer/code beat's on-screen
content IS the prompt (see beat_sheet.json `shot.remotion.props`), unchanged
from the parent since this is a full-parity reformat.

## The CLI loop this reel documents (same as parent, real, both scripts run)

### B02 — the ask

```
claude "write weekly_recap_v1.py -- log this week:
  the article, the videos, the cat bot idea"
```

### B05 — the change

```
claude "update weekly_recap_v1.py -> weekly_recap_v2.py:
  -> split into DONE THIS WEEK vs STARTING NEXT WEEK"
```

### B09 — the handoff (HANDOFF LAW)

```
claude "write me a weekly_recap.py that logs my actual
  week, split into what's done and what's just starting"
```

## Generated visuals (portrait-adapted, same three cards as the parent)

- **Article-header card**: browser-style dots, "SUBSTACK · ARTICLE" kicker,
  "Rescue, Reinvented" title, byline — built at a comfortable base size
  then uniformly scaled down (not redrawn at tiny sizes) so text/icon
  proportions stay legible in the narrower column.
- **Video-production card**: overlapping 16:9/9:16 frames + play triangle.
- **Cat-bot card**: cat silhouette + "AI" chat-bubble icon.

Same note as the parent: a real screenshot of the article or a Brutalist
terminal session could later replace the generated cards if more literal
proof is wanted; neither is required for this build.
