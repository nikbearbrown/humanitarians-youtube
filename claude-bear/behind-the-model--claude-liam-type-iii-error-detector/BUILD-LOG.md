# BUILD LOG — hai-simple/behind-the-model--claude-liam-type-iii-error-detector

Redo of `anthropics/youtube/behind-the-model/claude-liam-type-iii-error-detector`
("Type III Error Detector — Wrong Problem, Right Solution", Teardown register,
CLI-explainer style, 10 beats — B00 intro, B01–B06 body [PROBLEM/ASK/CODE/OUTPUT/
CHANGE/OUTPUT-revised], B07 SUMMARY, B08 NEXT STEPS, YOURTURN, B09 outro,
~118s estimated) as `hai-simple` (Plain register, Humanitarians AI skin).
Source folder untouched. Built from scratch — the target reel dir contained
only SUBJECT.json at the start of this invocation.

## What changed vs. source (per redo contract)

- **Register:** Teardown/CLI-walkthrough → Plain. The source is a "write a
  script, run it, revise it" CLI demonstration; this cut explains the same
  reframing/distinctness test directly, with no terminal or code beat — no
  script is written or run on screen (hai-simple's spine has no CLI slot).
- **Cold open:** source's `NikBearBrownOpen` title-card ask → `BrutalistHesitantWriter`.
  Writer types "Did Claude / get the answer / wrong?", hesitates on "answer",
  corrects to "problem" — the reel's actual wrong guess (checking the answer
  vs. checking the problem), picked up and falsified starting at B02/B03.
- **Close:** source's terminal next-steps beat + `ClaudeTitleOutro`/`@NikBearBrown`
  → `WantQuote` carry-out → `ClaudeComposerAsk` your-turn → `OutroCTA` +
  `@HumanitariansAI`, Liam sign-off.
- **Style:** source's CLI/terminal beats (`NikBearBrownTerminalAsk`,
  `NikBearBrownCodeBlock`) and Manim table-scene body → bespoke Manim GRAPHIC
  beats per NO-GENAI/NO-PANTRY LAW — no terminal chrome, no JSON/code display,
  drawn figures only (matches the established `behind-the-model` hai-simple
  precedent, e.g. `claude-liam-irreversible-action-gate`).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** the Type III definition (Howard Raiffa; solving the
  wrong problem correctly, source B01) and its anchor (cut support-ticket
  volume → hide the contact button, technically correct, source B01/B04) carry
  forward unchanged. The reframing/distinctness test — state the problem
  several honest ways, write a candidate answer per framing, test every
  answer against every framing (source B02/B03/B04) — is explained directly
  rather than via a script-generation walkthrough. The convergence warning
  (an answer that satisfies every framing signals the framings never
  differed, source B04's "row three is not distinct") and the revision that
  breaks a collapse (adding a fourth "constraints" framing, source B05/B06)
  both carry forward as B04 and B06. Source B07's "necessary but not
  sufficient" limit is split into the two BOTH-DIRECTIONS beats (B05:
  divergence isn't proof of the right problem; B06: convergence isn't a dead
  end) rather than restated as a single summary beat. Source B08 (next steps:
  run your own problem through the script) folded into the your-turn handoff.

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this compression was AI-VIDEO, pantry, or a human-drop
slot. GATE L (`./art scenes "…"` for the anchor/comparison/table-style visual
needs) returned no reusable hit close enough to the support-ticket reframing
content, so all six body beats are bespoke Manim — the established path for
this exact series (matches `claude-liam-irreversible-action-gate` and
siblings). The four Remotion patterns (`BrutalistHesitantWriter`, `WantQuote`,
`ClaudeComposerAsk`, `OutroCTA`) are the same registered components used
throughout the family. Body beats: `#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`,
the humanitarians palette.

## B00 WRITER LAW verification

`media/B00.mp4` measured 8.32s (clears the >=8s floor; narration 28 words +
`lead_silence_s` 0.8). Pulled frames at t=6.5s and t=7.8s: both show the fully
corrected line "Did Claude / get the problem / wrong?" — the "answer"→"problem"
swap is on screen and legible well before the beat ends.

## Real defect found and fixed during Gate V (not just re-run)

Gate V frame review (contact sheet + targeted crops of B04/B06) caught a
rendering defect GATE T's structural checks didn't: the `_cross()` helper drew
an "✕" (U+2715) `Text` glyph in Montserrat, which on this machine's font stack
fell back to a broken tofu render — a checkmark visually mangled into what
read as stacked "27/15" digits, most visible in B06's "distinct — some pass,
some fail" row. Root cause fixed, not patched: `_cross()` now draws an X from
two crossing `Line` mobjects (the same reliable approach already used for the
strike-throughs elsewhere in `scenes.py`), which renders identically
regardless of font glyph coverage. Re-rendered B04 and B06 only (B01/B02/B03/
B05 never used `_cross()`), re-verified both frames clean, recompiled.

## Gates passed

- **GATE T** (`type_check.py`): PASS on first pass, 0 fail / 10 skip (no
  pixel-level Manim beats registered in `type_check.py`'s scene table for
  this reel — see the Gate V note above for the defect structural checks
  couldn't catch).
- **Audio generation** (`generate_audio_kokoro.py`): 10/10 beats, free,
  `am_onyx`. Measured durations written back (B00 8.32s, total narration
  ~118s before tail silence).
- **Manim render** (`render_scenes.py`): 6/6 body beats rendered clean on
  first pass (before the Gate V cross-glyph fix required B04/B06 re-render).
- **Remotion render** (`remotion_scenes.py`): 4/4 beats (B00, BCRY, BHTF,
  BOUT) rendered clean, all extended to their measured audio duration.
- **Compile** (`compile.py --review`): 10/10 slots filled, `content-check`
  PASS, `frame-check` PASS, `lane-check` PASS. Motion histogram warned
  GRAPHIC beats at 60% (over the ~40% pantry cap) — expected for this format
  (6 body beats GRAPHIC, 4 bookend beats REMOTION) and not a hard gate.
- **GATE AUDIO**: PASS, mean_volume -24.0 dB (well above the -40 dB floor),
  max_volume -2.9 dB.
- Output: `behind-the-model--claude-liam-type-iii-error-detector-slate.mp4`,
  127.5s, newer than `beat_sheet.json`.

## Metadata

`behind-the-model--claude-liam-type-iii-error-detector.md` written per the
post-skill YouTube metadata format. Playlist resolved from
`skills/make/hai-simple/loop/playlists.json`: SUBJECT.json family
`behind-the-model` → **"Behind the Model"** (not the bare "Claude").

## Status at end of this invocation

Review cut (slate) DONE: audible, all beats filled, all automated gates
green. Proceeding to Phase 4 (4K render + `deliver.py --push`) in this same
invocation.
