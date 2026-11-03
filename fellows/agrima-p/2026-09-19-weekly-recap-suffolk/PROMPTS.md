# PROMPTS — weekly-recap-suffolk

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
  the article, the videos, the Suffolk lecture"
```

## B05 — the change

```
claude "update weekly_recap_v1.py -> weekly_recap_v2.py:
  -> split into DONE THIS WEEK vs STARTING NEXT WEEK"
```

## B09 — the handoff (HANDOFF LAW — read aloud and discussed)

```
claude "write me a weekly_recap.py that logs my actual
  week, split into what's done and what's just starting"
```

## Generated visuals (per the user's explicit request — no stock footage)

- **Article-header card** (B04/B07): browser-style dots, a
  "SUBSTACK · ARTICLE" kicker, the title "No Face, No Problem," and a
  byline — a mock header, not a real screenshot.
- **Video-grid card** (B04/B07): a 2x2 grid of four mini video frames, each
  with a small play triangle, labeled "16:9 + 9:16" — representing the four
  videos produced this week.
- **Suffolk-lecture card** (B04/B07): a presentation-slide icon (with two
  bullet lines) sitting on a simple podium shape, labeled "lecture · with
  Yatra."

If the user later wants more literal proof for any of these, they could
send: (1) a screenshot of the published Substack article, (2) a short
screen recording of an actual Brutalist build session in a terminal, or
(3) the actual presentation draft for the Suffolk lecture. None was
requested or required for this build.
