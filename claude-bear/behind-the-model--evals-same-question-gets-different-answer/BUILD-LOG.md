# BUILD LOG — hai-simple/behind-the-model--evals-same-question-gets-different-answer

Redo of `anthropics/youtube/behind-the-model/evals-same-question-gets-different-answer`
("Why the same question gets a different answer depending on who the biography says
is asking", Teardown-register, 9 beats, mostly unfilled slates — cold open was a
slate-only `FormBCard` beat with no host, verdict/Your Turn/outro bookend beats
present but unfilled) as `hai-simple` (Plain register, Humanitarians AI skin). Source
folder untouched. Built from scratch — the target reel dir contained only
SUBJECT.json at the start of this invocation.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Body compressed from the source's six-beat body
  (question, setup, mechanism, worked example, recap) to one idea per beat (10 beats:
  B00 writer + B01–B06 body + BCRY + BHTF + BOUT).
- **Cold open:** source's slate-only `FormBCard` (never filled) → `BrutalistHesitantWriter`.
  Writer types "Does Claude change its answer based on the asker's expertise?",
  hesitates on "expertise", corrects to "stated opinion" — the reel's actual wrong
  guess (a biography supplies relevant background/expertise), picked up and
  falsified by B03.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of source's
  unfilled `ClaudeVerdictArtifact`/`ClaudeTitleOutro` bookend beats.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** unchanged. The bare-question setup, the biography-as-injected-
  control-variable framing, the NLP-influence worked example (45% / 78% / 22%), and
  the sycophancy-as-a-dial mechanism all carried from the source, reworded for
  register and compressed to one idea per beat. Added: an explicit BOTH-DIRECTIONS
  beat (B06), which the thin source did not carry as its own beat — required by
  hai-simple's inherited BOTH-DIRECTIONS LAW.

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this compression was AI-VIDEO, pantry, or a human-drop slot
(the source's B00 was an unfilled `FormBCard` slate, not generated media). Every beat
in this reel is REMOTION (B00, BCRY, BHTF, BOUT) or bespoke GRAPHIC/Manim (B01–B06),
matching the precedent set by prior `hai-simple` redos in this same
`behind-the-model--*` batch (e.g. `claude-constitution-corrigibility-dial`).

## Gate V (frame QC) — one apparent defect investigated and cleared

Full-cut frame sweep at 4-second spacing (34 frames) across the compiled master, plus
targeted timestamp checks on every beat. One frame (t≈28s, inside B02) showed the two
persona answer-bubbles rendered as solid teal boxes with barely-legible text —
investigated by sampling pixel RGB values (`(43,85,101)` ≈ `#2B5565`, matching the
`TEAL` accent, not the card's coded `GROUND` fill default) and by re-grabbing frames a
few seconds later in the same beat. Root cause: the frame landed inside the
`Indicate(left, color=TEAL, ...)` transient flash animation in `SQB02Scene`, which
temporarily recolors the mobject's fill before easing back — not a resting-state
defect. Frames at t=35s and t=38s (mid/late B02) confirmed the boxes settle back to
the coded cream fill with fully legible dark text. No code change made; this was
verified, not assumed, before moving on. Every other frame across B00–B06, BCRY, BHTF,
BOUT read cleanly: legible type, safe inset respected, no overlap, Humanitarians AI
skin correct throughout (composer card, subscribe chip, outro title).

## Gates

- **TIMING LAW (B00):** narration 33 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **11.83s** (≥9s floor, ≥8s render floor). Correction
  ("expertise" → "stated opinion") verified fully typed and settled at t=10.5s via
  frame grab.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (well above the -40 dB floor,
  independently reverified with `ffmpeg -af volumedetect`), max_volume -3.0 dB.
- **Gate V (frame QC):** see above — one apparent defect investigated and cleared as a
  transient animation frame, not a resting-state defect. No fixes needed.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output
  (10/10 beats, no violations).
- **Motion histogram:** WARNING, graphic 6/10 (60%, over the ~40% pantry cap).
  Non-blocking and structural for this skill: B00 (writer), BCRY, BHTF, BOUT are
  REMOTION by the hai-simple spine itself, and at only 6 body beats this 10-beat reel
  necessarily runs higher than 40% on the graphic side — same disposition as sibling
  redos' histogram warnings.

## Output

`behind-the-model--evals-same-question-gets-different-answer.mp4` — 134.4s,
3840×2160, 10/10 beats real (no slate), audible narration throughout
(mean -23.9 dB, independently verified via ffprobe/ffmpeg volumedetect). This is the
review cut (COMPLETION LAW satisfied: newer than `beat_sheet.json`, mean_volume
verified). `compile.py` forces a 4K master by default ("4K LAW"), so no separate
low-res pass exists for this cut.

## Delivery

Master born natively 3840x2160 via `compile.py`'s 4K LAW, copied directly to `-4k.mp4`
(no separate 4K re-render needed). Delivered via `deliver.py --push`: staged
`DELIVERY/behind-the-model--evals-same-question-gets-different-answer/` (4K mp4 +
description) for the Drive sync, and committed the text artifacts (README.md,
beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md, QUESTION.md — no
mp3/mp4) to
`humanitarians-youtube/claude-bear/behind-the-model--evals-same-question-gets-different-answer/`.
Playlist: **Behind the Model** (direct family-prefix match in `playlists.json`).

## Remotion/Manim pipeline notes for future invocations

Both `runtime/scripts/remotion_scenes.py` and `runtime/scripts/compile.py` ran within
the harness's default foreground timeout for this 10-beat reel; still invoked with an
explicit longer timeout as a precaution and run in the FOREGROUND per the COMPLETION
LAW — never backgrounded. `generate_audio_kokoro.py` takes no `--voice` flag; voice is
read from `metadata.voice_kokoro` in the beat sheet.
