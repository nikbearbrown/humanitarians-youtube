# BUILD-LOG — insider-buying-noise

Landscape 16:9, 12 beats, review cut `insider-buying-noise-slate.mp4` (64.7 s),
built 2026-11-10. Kokoro `af_bella` at speed 1.08, Plain register, `claude-hai`
channel (Bella in for Gomathy, `@HumanitariansAI`, kicker "Irreducibly Human").
Title: "Most Insider Trades Aren't Buys" (the working title "Most Insider
Buying Is Noise" was dropped: 83% of qualifying buys pass the filters). No
toolkit files edited; everything lives in this folder. Not committed.

## Data

Only committed Mycroft files at `mycroft-work` commit fed487c (read with
`git show`; read at 8924c76 and rewritten to fed487c on 2026-11-11 with identical
file contents, commit-message trailers removed). The working tree's uncommitted ENRICH/returns work and the
edited `status.md` are not used. Every number and its file: `SOURCES.md`.

## Patterns reused (passed final in p-value)

| Pattern | Here |
|---|---|
| `ClaudeComposerAsk`, largeText, `runningText: ""`, `modelLabel: "Claude"` | B00, B10 |
| `FormBCard` (subs ≤ 26 chars, asserted by the sheet generator) | B04, B08, B09 |
| Ink-only Manim, `_label()` 4× layout, MathTex for math | B01–B03, B05–B07 |
| Hesitant writer in Manim | B01 |
| `OutroSeries` (landscape) | B11 |

## Narration / runtime

| Version | Words | Runtime @1.08 |
|---|---|---|
| approved first draft | 198 | 80.8 s |
| user trim (B02–B07, B10) | 180 | 72.5 s (71.2 s @1.12) |
| cuts 1–3 + new B05 + B10 check line (user, 2026-11-10) | 172 | 65.8 s audio → 66.0 s cut |
| pre-final rewording of B04, B06, B07, B08 + B08 card (user, 2026-11-10) | 170 | 64.45 s audio → 64.7 s cut |

Per-beat audio (s): B00 4.34 · B01 6.02 · B02 3.91 · B03 2.90 · B04 4.25 ·
B05 5.93 · B06 5.40 · B07 5.59 · B08 5.69 · B09 6.67 · B10 8.28 · B11 5.47.

Pre-final rewording: only B04, B06, B07 and B08 were regenerated
(`generate_audio_kokoro.py --only B04 B06 B07 B08 --speed 1.08`); the other eight
mp3s are untouched. B06 final wait 1.84 → 1.65 s and B07 1.94 → 1.89 s in both
`scenes.py` files; B04/B08 cards re-rendered (B08 item 1 is now "Filters fixed
first / Before any returns"). Rebuild: GATE V 0/0, GATE T PASS.

## Gate results

| Gate | Result |
|---|---|
| F (paperwork) | pass |
| L (beat-mix lint) | clean |
| A (static) | first run: ERROR B02 (`rate_functions.ease_out_cubic` not in the checker's stub) and B03 (label x computed from `.width`, out of frame under the stub) → `smooth`, `aligned_edge=RIGHT`. Re-run: warnings only (B01, B02, B06 "text-only") |
| W (WCAG/margins) | pass |
| B (layout audit, strict) | CLEAN, all six scenes |
| compile | first attempt REFUSED: B00 "narration duration disagrees". I had regenerated `beat_sheet.json` after the audio run, which dropped `actual_duration_s`. Fixed by re-running `generate_audio_kokoro.py --speed 1.08`, not by hand |
| V (strict) | first cut: MAJOR underfill B06 (30% / 36%). B06 relaid out: two columns plus a full-width 999,542 bar with the 6.5% filled. Re-run: 0 BLOCKER / 0 MAJOR |
| T | PASS, 12/12 (min text-run 46 px vs 41 px floor) |

Eye check: frames at 15/50/85% of every beat, read on a contact sheet. All
text legible, the funnel numbers agree beat to beat, no terracotta text. The
B04 FormBCard clip is center-cut 6.0 → 4.7 s; all three items are already on
screen at 15%. Known non-blocking: `[art] WARNING: build stamp failed`.

## Final master (2026-11-10, approved by Gomathy)

`./art final <reel> --out <reel>` (height 2160) → `insider-buying-noise.mp4`,
3840 × 2160, 24 fps, H.264 + AAC, 64.67 s. GATE T PASS; compile's built-in
GATE V passed; strict GATE V on the master: 24 frames, 0 BLOCKER, 0 MAJOR.
Frames read by eye: clean, no review burn-ins. Not committed.
