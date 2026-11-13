# PROMPTS — weekly-recap-never-forgets

No pantry/archival assets used — every non-composer beat is a from-scratch
Manim scene in scenes.py; every composer/code beat's on-screen content IS
the prompt (see beat_sheet.json `shot.remotion.props.command`).

## B00 — the cold open ask

```
claude "help me build a real log of what I actually did this week"
```

## B02 — the ask

```
claude "write weekly_recap_v1.py -- log this week:
  the article, the videos, the meeting"
```

## B05 — the change

```
claude "update weekly_recap_v1.py -> weekly_recap_v2.py:
  -> tag each item by category, print a shipped-count"
```

## B09 — the handoff (HANDOFF LAW — read aloud and discussed)

```
claude "write me a weekly_recap.py that logs my actual
  week, tagged by category and counted"
```

## Generated visuals (per the user's explicit request — no stock footage)

- **Article-header card** (B04/B07): browser-style dots, a
  "SUBSTACK · ARTICLE" kicker, the title "The AI That Never Forgets," and a
  byline — a mock header, not a real screenshot.
- **Video-grid card** (B04/B07): a 2x2 grid of four mini video frames, each
  with a small play triangle, labeled "16:9 + 9:16" — representing the four
  videos produced this week.
- **Meeting card** (B04/B07): a simple calendar icon (tabbed top, a single
  marked date) labeled "Team Meeting" / "attended."

If the user later wants more literal proof for any of these, they could
send: (1) a screenshot of the published Substack article, (2) a short
screen recording of an actual Brutalist build session in a terminal, or
(3) a photo or note from the team meeting. None was requested or required
for this build.
