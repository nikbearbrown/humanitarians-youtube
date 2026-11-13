# BUILD-LOG — p-value

Landscape 16:9, 12 beats, review cut `p-value-slate.mp4`, built 2026-10-15.
Kokoro `af_bella` at speed 1.08, Plain register, `claude-hai` channel (Bella in
for Gomathy, `@HumanitariansAI`, kicker "Irreducibly Human"). No toolkit files
edited; everything here lives in this folder. Not committed.

## Pre-build check

No existing beat sheet in `~/Brutalist/reference/humanitarians-youtube`
(origin/main `03f161a6`, and the local `gomathy-s` branch) explains p-values.
22 sheets mention the term in passing; the only title hit,
"Build a Hypothesis-Testing Drill with Claude Code", is about case-interview
hypotheses, not statistical testing. No open PR title matches.

## Lessons carried over (knowledge-cutoff, claude-liam-context-window)

| Lesson | Applied here |
|---|---|
| Only patterns that passed `./art final` with a working portrait path | `ClaudeComposerAsk`, `FormBCard`, ink-only Manim, `OutroSeries` (landscape) / Manim title card (portrait) |
| Terracotta text fails GATE T §8.3 at largeText size | `runningText: ""` on both composer beats, both orientations; no terracotta text anywhere |
| `modelLabel` default chip read "Fable 5" | `modelLabel: "Claude"` on B00 and B10, both orientations, from the first render |
| Remotion hesitant writer can't hit the portrait floor | B01 authored in Manim for BOTH orientations |
| FormBCard916 crashes without icons; long subs break title-safe | every FormBCard916 item has `icon: "BOX"`; every sub ≤ 26 chars (asserted when the sheet was generated) |
| Manim kerning collapses word spaces at small sizes | `_label()` lays out at 4× (2× for long lines) then scales |
| GATE V on a portrait review cut false-flags the burn-ins | see vertical/BUILD-LOG.md |

## Decisions

- **Audio speed 1.08.** At 1.0 the approved 179-word script measured 65.2 s.
  1.08 brings it to 62.4 s without cutting approved lines; faster would crowd
  the pauses. Rerun with `generate_audio_kokoro.py <reel> --speed 1.08` to reproduce.
- **"p-value" pronunciation** checked two ways: Kokoro phonemizes it /pˈiːvˈæljuː/
  ("pee value") in every phrasing used, and a faster-whisper transcript of the
  generated mp3s reads "p-value" in B01, B03, B10, B11. No respelling.
- **Word trims after review** (to stay near 175 words; meaning unchanged):
  B00 "A study reports p equals … What does that mean?" → "A study says p is
  zero point zero three. Meaning?"; B02 "Start by assuming" → "First, assume";
  B04 dropped "of the time"; B05 "— or how big or important the effect is" →
  ", nor the effect's size or importance". (B06 was also trimmed, then
  replaced on review — see "B06 narration change" below.)
- **Math** is MathTex (LaTeX present) in B04 and B06, never a Text string. B04
  boxes "≈ 0.011" on "about one percent", which also satisfies GATE A's
  shape-variety check (the first B04 draft failed it: coins only, no change).
  The box is a `RoundedRectangle` sized to the term, because the GATE A stub
  treats a `SurroundingRectangle` around text as text.
- **No `metadata.channel_title`**, matching knowledge-cutoff (which passed
  final without it); `folderLabel` carries `@HumanitariansAI`.
- **B01 ~6.2 s**, not ≥ 9 s (EXECUTIVE-SUMMARY LAW): same trade as the prior
  60 s reels.

## Gates (landscape)

- GATE F: paperwork present (FACTCHECK, SHOTLIST, PROMPTS). GATE L: clean.
- GATE A: B04 failed once (shapes never change), fixed as above. B01 advisory
  "text-only" (by design, hesitant writer).
- GATE W: all four scenes clean.
- GATE B (strict): B03 failed once ("Shaded share = p-value" bottom at y −3.44,
  past −3.4); moved to y −2.95. Re-run: all four clean.

## B06 narration change (on review, 2026-10-15)

New line (both orientations): "A huge study can give a tiny effect a tiny p.
A small study can give a big effect a large p." Total narration now 186 words.

- Audio: only B06 regenerated (`--only B06 --speed 1.08`), 4.80 s → 5.93 s;
  landscape and vertical mp3s byte-identical. Whisper word timings: second
  sentence starts at 3.04 s; "large" reads as /lˈɑːɹdʒ/.
- Scenes: B06 retimed in both `scenes.py` files to 5.93 s (title 0.4, first
  card 0.6, hold 2.0, second card 0.6 at 3.0 s, hold 2.33). Only B06 re-rendered.
- `vertical/mp3/timings.json` held only B06 after the `--only` run
  (`shorts.py` doesn't copy timings); restored from the landscape file, whose
  mp3s are identical.

## GATE T — B06 ≈ false positive (landscape)

GATE T §8.1 first failed B06 at 37 px, then 38 px after raising the meta and
per-group labels to size 34. The blobs it measured were the two strokes of
"≈" in the MathTex p-values (bbox 133 × 38 px, two stacked), not text; at
MathTex size 72 they sit just above the checker's fragment threshold (34.6 px).
Set to size 64 (B04's ≈ at 68 already passed). Checker untouched.

## B06 visual changes after the narration change

- Clean-clip GATE V (vertical) flagged B06 at 50% as underfill once the retime
  put the second card at 3.0 s. Both orientations now draw both card outlines
  at the start and fill each card on its own sentence.
- That left no shape change after the opening frame (GATE A "shapes never
  change"), so each p-value is now underlined on its spoken "tiny p" (~2.0 s)
  and "large p" (~4.9 s). Same sequence in 16:9 and 9:16.

## Review cut status (2026-10-15)

`p-value-slate.mp4` — 3840×2160, 63.7 s.
- GATE T: PASS, 0 FAIL. §8.10 advisory scores (no exit effect): B02 0.57,
  B05 0.62, B07 0.29, B08 0.45, B09 0.50.
- GATE V (`ART_STRICT=1`, no `--lenient`): 24 frames, 0 BLOCKER / 0 MAJOR.
- Frames read by eye at 15/50/85% of every beat (`_qc/`): no clipping,
  collisions or terracotta text; math typeset. Open, same as knowledge-cutoff:
  B11 `OutroSeries` renders on its own white ground with a thin red underline
  (component tokens).
- `[art] WARNING: build stamp failed` — known toolkit stamp bug, non-blocking.
- Not exported: no `./art final` run. Not committed.

## Final master (2026-10-15)

PEDAGOGY.md verdict PASS (Gomathy, after reviewing both cuts). Clean master built with `./art final`:
`brutalist.art/renders/p-value.mp4` — 3840×2160, 24 fps, H.264 + AAC, 63.71 s, + `.verified.json` (status ready).

- GATE T (art final pre-flight): PASS, 0 FAIL.
- GATE V: `./art final` does not run it, so `final_frame_check.py` (strict, no
  `--lenient`) was run on the clean master: 24 frames, 0 BLOCKER / 0 MAJOR.
- Frames read by eye (one per beat at 85%): no burn-ins, no clipping or collisions.
- `[art] WARNING: build stamp failed` — known toolkit stamp bug, non-blocking.
- No toolkit files edited. Not committed.
