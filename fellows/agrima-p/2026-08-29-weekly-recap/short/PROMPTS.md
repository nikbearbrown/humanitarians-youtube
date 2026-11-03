# PROMPTS — weekly-recap/short
# No open pantry slots — every beat is Claude-skin Remotion (portrait 916
# compositions) or a from-scratch portrait Manim scene. Kept for GATE F
# completeness; see the parent reel's PROMPTS.md for the underlying build
# prompts this short's story is derived from (unchanged — it's a derivative
# cut, not a re-edit, per THE SHORTS LAW).

No archival/pantry assets are needed. Every non-composer beat is a
from-scratch portrait Manim scene in scenes.py; every composer/code beat's
"prompt"/"code" IS the on-screen content (see beat_sheet.json
`shot.remotion.props` for B00/B02/B03/B05/B06/B09).

Reference — the four prompts this reel's CLI loop is built around (same as
the parent, unchanged):

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

## B09 — the handoff
```
claude "write me a weekly_recap.py that logs my actual
  week, split into what's done and what's just starting"
```
