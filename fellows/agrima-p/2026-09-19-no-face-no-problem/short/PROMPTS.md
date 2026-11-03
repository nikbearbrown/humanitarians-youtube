# PROMPTS — no-face-no-problem/short

No pantry/archival assets used — every non-composer beat is a from-scratch
portrait Manim scene in scenes.py; every composer beat's "prompt" IS the
on-screen content (see beat_sheet.json `shot.remotion.props.command` for
B00/B08).

## B00 — the cold open ask

```
claude "help me understand why faceless AI accounts are
  suddenly everywhere — and why people trust them"
```

## B08 — the handoff (HANDOFF LAW — read aloud and discussed)

```
claude "help me fact-check the next faceless account I
  watch before I trust what it's telling me"
```

## Generated visuals (portrait-adapted, 5 of the parent's 8 Manim beats)

- **B00B presenter card** — unchanged content, portrait layout.
- **B01 stock-footage card** — skyline/wave/flame motifs scaled to fit
  inside the frame border (same fix applied to the parent after a real
  overflow bug was caught in frame review), with the TikTok-style caption.
- **B04 niche grid** — the five niche cards arranged in a 2-column grid
  instead of a single row, to fit the portrait width.
- **B05 trust-stat card** — the stat plus the plain-text on-screen
  skepticism flag (no unicode glyph, matching the parent's fix), wrapped to
  two lines to fit the narrower card.
- **B06 watch-time meter** — a narrower meter (3.2 units vs. 6.0 in the
  parent) with the same completion/saves/shares tags and crossed-out face
  icon.

## Dropped beats (no portrait scene needed)

B02 (the strategy), B03 (the voice gap), and B07 (the closing reflection)
were dropped by shorts.py's auto-plan to fit the 3:00 Shorts cap — see
SHOTLIST.md and FACTCHECK.md.
