# BUILD LOG — hai-simple/behind-the-model--claude-liam-vox-silent-omission

Redo of `anthropics/youtube/behind-the-model/claude-liam-vox-silent-omission`
("Why an Agent That Finishes First Can Be Worse Than One That Stops",
Teardown-register vox-editorial 12-beat body spine, `register: "Teardown"`,
`voice: "am_onyx"` already) as `hai-simple` (Plain register, Humanitarians AI
skin). Source folder untouched. Built entirely fresh — the target reel dir
contained only SUBJECT.json at the start of this invocation.

## What changed vs. source (per redo contract)

- **Register:** Teardown (agent finishes, colleague finds three unopened
  dissenting documents, per-operation mechanism, count-mismatch practice,
  crash vs. silent omission, endcard) → Plain (hai-simple's writer-open +
  one-idea-per-beat body + carry-out + your-turn + outro spine). Source's 12
  body beats (B01–B12) recompressed into 9 beats (B01–B09) carrying the same
  facts and argument.
- **Cold open:** source's `ClaudeComposerAsk` cold open (question typed as a
  command) → `BrutalistHesitantWriter`. Writer types "A confident done from
  Claude means the scan was complete, right?", hesitates on "complete",
  corrects to "partial" — the reel's actual wrong guess (a confident finish
  means a full pass), picked up in B02 and falsified by B03's six-bullet
  brief case.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of
  source's `ClaudeTitleOutro`/`@NikBearBrown` skin.
- **Voice:** unchanged — Liam, Kokoro `am_onyx` (source already used
  `am_onyx`).
- **Facts/argument kept:** a six-bullet brief with a confident recommendation
  shipped while three dissenting documents in an unopened subfolder went
  unread, one of them contradicting the recommendation directly, with no
  error ever appearing; the per-operation success chain (read, summarize,
  next — each step reports only on itself); what falls outside an agent's
  reach (no access, unreadable scan, not listed); crash vs. silent omission
  as the title's core distinction; Maya's twelve-PDF example (nine read,
  three unreadable scans, digest ships with old targets); the inventory
  practice (scope, processed, skipped) and the count mismatch as the
  catching signal; the closing line that a completion report only tallies
  what succeeded, not what existed.
- **New content this redo added, not present in source:** ANCHOR LAW
  required one running example planted early and paid off late — this redo
  makes the source's own six-bullet-brief/folder-tree case the reel's
  anchor, planted at B03 (the folder tree, three dissenting documents
  glowing crimson, never opened) and paid off at B09 (the same folder tree
  returning, the three documents now stamped SKIPPED via an inventory
  check). WRONG-GUESS LAW required the guess stated then falsified by a
  concrete case — B02 states it ("a confident finish means a full pass"),
  B03 falsifies it with the six-bullet-brief case. ONE-FLAG LAW required a
  single inference flag — the source made no such caveat, so B07 adds one:
  the report-only-tallies-successes structure assumes the tool doesn't
  separately surface skips; some do, and you can't tell which from a
  confident "done" alone. BOTH-DIRECTIONS LAW required stating what a
  positive result (matching inventory) and a negative result (one skip) do
  and do not prove — B09 adds both, which the source's flat endcard did not
  separate.
- **Dropped:** none of the source's substantive content — the source's 12
  body beats plus cold open and endcard map onto this redo's 9 body beats
  plus writer-open and carry-out.

## Six-move audit (Plain register, `simple`/`hai-simple` Step 2)

| Move | Beat |
|---|---|
| 1 stakes | B01 |
| 2 wrong guess (+ falsified by a case) | B02 states it; B03 falsifies it |
| 3 mechanism | B04, B05, B06, B08 (one-flag at B07) |
| 4 anchor (planted / paid off) | B03 → B09 |
| 5 both directions | B09 |
| 6 carry-out | BCRY |

## Build

- **Audio first:** `generate_audio_kokoro.py` — 13/13 beats generated, $0.00,
  measured durations written back into `beat_sheet.json` (ground truth).
- **B00 TIMING LAW — one real defect found and fixed.** First cut: 28-word
  narration, `lead_silence_s` 0.8, measured B00 at 8.87s; the replacement
  text ("everything" → "only what it reached", 21 chars) was far longer
  than the trigger word, and a late-frame pull at t=8.7s showed the writer
  still mid-backspace on "everything" — the correction never completed
  on-screen before the clip ended (the exact TIMING LAW failure this
  skill's SKILL.md warns about). Root cause understood by reading
  `BrutalistHesitantWriter.tsx`: the render's `-t <duration>` freeze/trim
  step truncates the animation to the beat's audio duration, and every
  punctuation character (including mid-word apostrophes) and newline forces
  a guaranteed pause on top of per-character typing time — a long
  replacement word plus four lines of text left no margin. Fixed by (1)
  rewriting the on-screen text to a same-length single-word swap
  ("complete" → "partial", matching the proven `vox-fluency-trap` sibling's
  "correct" → "fluent" pattern) and (2) lengthening the narration to 33
  words, remeasured at 9.45s. Re-rendered: `media/B00.mp4` = 9.47s (≥8s
  floor met); frame pulls at t=8.0s and t=9.2s both show "partial, right?"
  fully typed and settled, with headroom before the clip ends.
- **GRAPHIC beats (B01–B09):** authored as Manim scenes (`scenes.py`,
  classes `SOB01Scene`–`SOB09Scene`), Humanitarians palette (`#F3EBDD`/
  `#2F2A26`/`#E4572E`/`#1F4E5F`), rendered via `render_scenes.py` against the
  measured `actual_duration_s` for each beat.
- **REMOTION beats (B00, BCRY, BHTF, BOUT):** rendered via
  `remotion_scenes.py` (foreground — the tool's automatic 120s
  backgrounding kicked in on every call; each was polled to completion via
  `TaskOutput(block=true)` in the foreground of this session before any
  further step, per the one-shot COMPLETION LAW — no render was ever left
  orphaned or unsupervised).
- **Compile:** `compile.py` (foreground, polled via `TaskOutput(block=true)`
  after its own 120s auto-background) → 13/13 beats real (no slate), 4K LAW
  forced the master to 3840×2160 natively, 160.6s. First compile flagged
  B09 with `WARNING: clip 6.4s slowed 3.3x into 20.8s beat — extreme
  slow-mo`. Fixed at the root rather than just logged: lengthened B09's
  Manim scene holds (final `wait()` 1.3s → 7.0s, plus small holds after
  each reveal) so the rendered clip grew from 6.4s to 13.5s, bringing the
  slow-mo ratio down to 1.55x, in line with the other beats (1.79x–2.54x).
  Recompiled: `GATE AUDIO: PASS` mean_volume **-23.9 dB**, max_volume
  -2.7 dB.

## Gate T (pixel type-check) — fixes and exemptions

First pass: **FAIL (2 beats)**.
- **B04** — contrast-local + bbox-overlap: the READ/SUMMARIZE/NEXT pills'
  labels were built INK-on-cream, then only the pill's fill was animated to
  TEAL (`Transform` on the box only) — the INK text stayed on top of a now-
  dark-teal background, 1.45:1 contrast. Real defect, fixed in `scenes.py`:
  added a matching `Transform` on the text mobject to GROUND (cream) in the
  same animation step, so the label turns white exactly as the pill fills.
- **B05** — same defect, same root cause: the boundary chain's pills were
  built already teal-filled from the start with the `_pill()` default
  `text_color=INK`. Fixed by passing `text_color=GROUND` explicitly for
  that chain's pills.
- Re-render + recompile + re-run: **GATE T: PASS** (0 FAILs, 13 beats).

## Gate V (frame QC)

Sweep across the whole 160.6s master covering every beat at least once (13
frame pulls, one per beat plus a resettled B06 check): all beats legible,
safe inset, no text overlap after the B04/B05 fix, Humanitarians AI skin
correct throughout (composer card reads "Opus 4.8" — `modelLabel` set
explicitly, no leaked placeholder — subscribe chip, outro title all read
cleanly).

- **One real defect found and fixed beyond Gate T:** B09's three
  "CONFIRMED:\nSKIPPED" stamp labels (font_size 20, icon buff 1.1)
  overlapped each other horizontally — illegible collision, not caught by
  the automated bbox check because the false-positive exemption logic
  differs from a genuine multi-label collision. Fixed by shortening the
  label to "SKIPPED" (single line) and widening the icon spacing (buff
  1.1 → 1.4). Re-rendered, re-verified clean: the B03/B09 anchor pair (the
  folder tree) is visually recognizable as the same object in both
  appearances, each of the three dissenting documents now individually and
  legibly stamped SKIPPED.
- B06 (crash vs. silent omission): a mid-animation frame pull briefly showed
  overlapping "COMPLETE" text during a `Write`/box-fill transition; a later
  frame pull confirmed the settled state is clean — not a defect, just an
  in-progress animation frame.
- **Motion histogram:** WARNING, graphic 9/13 (69%, over the ~40% pantry
  cap). Non-blocking and structural for this skill: B00 (writer), BCRY,
  BHTF, BOUT are REMOTION by the hai-simple spine itself, and at 9 body
  beats this 13-beat reel necessarily runs higher than 40% on the graphic
  side. Same disposition as prior `behind-the-model--*` hai-simple redos'
  identical histogram warning.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (13/13 beats, no violations).

## Output

`behind-the-model--claude-liam-vox-silent-omission.mp4` — 160.6s,
3840×2160, 13/13 beats real (no slate), audible narration throughout
(mean -23.9 dB, max -2.7 dB). This is the review cut (COMPLETION LAW
satisfied: mp4 mtime newer than beat_sheet.json mtime, mean_volume verified
via ffprobe volumedetect). `compile.py` forces a 4K master by default ("4K
LAW"), so no separate low-res pass exists for this cut.
