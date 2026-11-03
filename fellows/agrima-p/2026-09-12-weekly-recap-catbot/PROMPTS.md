# PROMPTS — weekly-recap-catbot

No pantry/archival assets used — every non-composer beat is a from-scratch
Manim scene in scenes.py; every composer/code beat's on-screen content IS
the prompt (see beat_sheet.json `shot.remotion.props`).

## The CLI loop this reel documents (real, both scripts actually run)

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

### B09 — the handoff (HANDOFF LAW — read aloud and discussed)

```
claude "write me a weekly_recap.py that logs my actual
  week, split into what's done and what's just starting"
```

## Generated visuals (per the user's explicit request — no stock footage)

- **Article-header card** (B04/B07): browser-style dots, a "SUBSTACK ·
  ARTICLE" kicker, the title "Rescue, Reinvented," and a byline — a mock
  header, not a real screenshot.
- **Video-production card** (B04/B07): an overlapping wide (16:9) and tall
  (9:16) frame pair with a play triangle, labeled "16:9 + 9:16."
- **Cat-bot card** (B04/B07): a simple geometric cat silhouette (circle head,
  triangle ears, dot eyes, whisker lines) paired with a terracotta
  chat-bubble icon marked "AI."

If the user later wants more literal proof for either of the first two
cards, they could send: (1) a screenshot of the published Substack article
(swap into the article-header card), or (2) a short screen recording of an
actual Brutalist build session in a terminal (swap into the video-production
card). Neither was requested or required for this build.
