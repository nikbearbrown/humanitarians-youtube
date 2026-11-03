# SHOTLIST — Memory API (Medhavy Hub)

Seven beats. Every visual in B01–B06 is `memory-api-deck.html` rendered as-is by
headless Chrome at a 3840×2160 viewport — not a re-implementation. B00 is the
one card built for the reel, using the deck's own CSS and markup classes.

Durations are **measured narration**, not planned. The deck's own `data-dur`
windows are listed beside them; where they disagree, the narration won.

## 16:9 master — 171.32 s (2:51.32), 4111 frames @ 24 fps, 3840×2160

| Beat | Act | Measured | `data-dur` | Drift | Motion | On screen |
|---|---|---:|---:|---:|---|---|
| B00 | SIGN-IN | 7.98 s | — | added | slam | Paper fill with the deck rail present · `MEMORY API` slams in (Archivo Black) · sign-in lede rises beneath, accent on the key phrase |
| B01 | SCENE 1 — THE PROBLEM | 21.21 s | 26 s | −4.79 | slam | Kicker rises `MEDHAVY HUB / MEMORY API` · `THE TUTOR FORGETS` slams in · lede rises with "stranger" in accent |
| B02 | SCENE 2 — TWO TABLES | 31.59 s | 30 s | **+1.59** | wipe | `TWO TABLES` wipes in · `chat_memory_turns` box rises white · `learner_profiles` box rises filled black · note: different lifetimes, different jobs |
| B03 | SCENE 3 — THE KEY | 36.43 s | 34 s | **+2.43** | slam | `ONE STRING HOLDS IT UP` wipes in · keyline slams with `hub:` in accent and `user_abc123` beside it · three callouts stack: BOTH TABLES, `hub:` PREFIX, THE WHOLE TRICK |
| B04 | SCENE 4 — ROLLING WINDOW | 21.95 s | 26 s | −4.05 | step-reveal | `IT FORGETS ON PURPOSE` wipes in · message tape rises as U/A pairs · oldest four tip over and fall away · `KEEP 24 TURNS → 48 ROWS. DELETE THE REST.` |
| B05 | SCENE 5 — BUILT ≠ WIRED | 33.02 s | 30 s | **+3.02** | slam | `BUILT ≠ WIRED` wipes in · two-panel status grid slams · verify-before-shipping stamp lands on the right panel in alert red, rotated · note: built and waiting, not necessarily live |
| B06 | SCENE 6 — RECAP | 19.14 s | 24 s | −4.86 | slam | `THE SHAPE OF IT` wipes in · `02 / 48 / 01` end grid slams · closing lede rises with the subject string highlighted |
| | **total** | **171.32 s** | **170 s** | **+1.32** | | |

Three beats overrun their deck window and three undershoot it. Holding to
`data-dur` would cut the narration off mid-sentence on B02, B03 and B05; holding
the short beats open would add ~13.7 s of silence. Resolved per the script's own
instruction — *"Adjust if your read runs long."* The total lands 1.32 s over a
170 s deck against a 2:50 target.

If per-scene `data-dur` fidelity matters more than an unhurried read, the three
overrunning beats fit at `--speed 1.06 / 1.08 / 1.11`.

## 9:16 short — 171.32 s, 2160×3840

Same seven beats, nothing cut: `shorts.py` measured 171.3 s against its 180 s
cap and took the "full reformat, no beats cut" path.

| Aspect | Treatment |
|---|---|
| Layout | **Letterboxed, not cropped.** The deck is scaled to 2160 wide and padded on its own paper white |
| Why | The default centre-cut keeps a 1214 px strip of a 3840 px frame — 68% of the width discarded. On B02 that left the headline gone, the left box empty, and `LEARNER_PROFI` truncated mid-word. Every two-column layout in the deck (`grid2`, `statusgrid`, `endgrid`, `keyline`) breaks the same way |
| Mechanism | `pantry/<beat>-916.*` overrides — `shorts.py`'s own documented human slot, which wins over every other path. Re-run reported `pantry override` on all seven beats |
| Endcard | Removed (`--no-endcard`). The default card is the toolkit's `@nikbearbrown` design — dark charcoal, serif, terracotta rule — wrong channel for a Medhavy Hub deck, and it was being upscaled 1080×1920 → 2160×3840. The reel already ends on its own RECAP |

Known cost: letterboxing leaves the deck occupying about a third of the vertical
frame. That is the honest price of a 16:9 deck in a 9:16 slot; the alternative
loses two thirds of every slide.

## Capture notes

Entrances are sampled at true 24 fps until they settle (1.3–3.3 s per scene);
after that the deck is static, so the settled frame is captured once and held.
The deck's progress rail is **not** captured — it advances across the whole
scene — and is composited afterwards by ffmpeg across each beat's real measured
duration, so it still reaches 100% exactly at scene end.

Each frame is a pure function of `t`: animations are frozen in CSS from frame
one, then seeked by rewriting `animation-delay` to `(original − t)` with
`setProperty(..., 'important')`, because the deck declares `.d1`–`.d7` with
`!important`. Deterministic and re-runnable.

## Motion labels

`slam` carries 5 of 8 beats (62%) on the endcard build, over the toolkit's ~40%
diversity cap. The labels are read off the deck's own animation classes
(`.slam`, `.wipe`, `.rise`), so they are accurate; relabelling to satisfy the
linter would misdescribe the deck. Left standing.
