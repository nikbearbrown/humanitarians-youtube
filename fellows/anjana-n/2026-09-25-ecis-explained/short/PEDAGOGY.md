# PEDAGOGY — ECIS Episode 8 (9:16 Short derivative)

This is a derivative cut of `anjana-s/2026-09-25-ecis-explained` (Episode 8),
produced by `runtime/scripts/shorts.py` — same signed script, same evidence,
reformatted to 9:16 and shortened to fit the 3:00 Shorts cap (211.8s parent →
~155s). The parent's GATE P sign-off (`PEDAGOGY.md`, `VERDICT: PASS`) covers
every beat's content; nothing here re-argues that evidence.

## What's different from the parent — and why the cut was made by hand

The episode's three new signals — linguistic analytics (B02), market impact
(B03) and pre-signal drift (B04) — are what "reading between the lines" means.
They are also three of the four longest beats, which is exactly what a
duration-driven auto-plan reaches for first. The cut was specified manually,
`--drop B01 B05 B08`, so all three survive intact:

- **B01 (the seven-episode recap) dropped.** A "previously on" is the one beat
  whose job is context a Short viewer doesn't have and can't use in 155 seconds.
  B00's cold-open ask already states the premise — the system reads the words,
  not the delivery — which is all the rest of the cut depends on.
- **B05 (the infrastructure upgrade) dropped.** At 36.0s it is the longest beat
  in the episode, and it is the only one that isn't about signal quality:
  SQLite→PostgreSQL, TimescaleDB, materialized views. It earns its place in the
  long version — a system quietly outgrowing its database is a real thing worth
  showing — but a viewer who came for "how they said it" doesn't need the
  plumbing, and cutting it buys back a fifth of the runtime in one move.
- **B08 (the your-turn handoff) dropped.** A pasteable prompt does not survive
  the format; nobody copies one off a vertical video. Standard for this series'
  Shorts.
- **B07 (the verdict) kept.** This episode adds three distinct things, and the
  verdict card is where they are named side by side.
- **B09's outro narration was rewritten** — the only new text, the only audio
  regenerated. The auto-generated draft spliced truncated narration fragments
  into a sentence that did not parse (the same failure as Episodes 5, 6, 7 and
  the transformer-layer reel). Rewritten to name what was actually cut: the
  origin story, the database rebuild, and the prompt.
- **7 beats rewired to portrait `916` compositions** via the Onda check. Reflow
  moves per component: B01 R2 (restack — unused in this cut), B02 R2 (the
  feature vector moves below the instruments and lies horizontally), B03 R3
  (each measurement widens to full frame; the magnitude bars stay TRUE to
  proportion so the 0.5% bar is still a stub), B04 R3 (the price chart keeps its
  sideways time axis — time has to run sideways — with the two labels stacked
  above it instead of beside each other), B06 R2 (the three addition cards stack
  full-width under a compressed pipeline band).
- **Endcard generated with `--handle ""`** at cut time — the durable fix — and
  pre-built at 2160×3840, because `shorts.py`'s `endcard_png()` hardcodes
  1080×1920 and upscales badly against a 4K master.

## Evidence discipline

No new factual claims. The thirteen human-confirmed rows and the illustrative
placeholders all carry over from the parent unchanged. Dropping B05 removes the
five infrastructure claims from this cut entirely; nothing was softened or
restated.

VERDICT: PASS
