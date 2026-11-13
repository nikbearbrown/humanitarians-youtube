# Frictional log — The Button That Broke Every Next Question

Written contemporaneously during this build, not reconstructed afterward. Entries are dated to
when they actually happened (same session, 2026-11-12).

## 2026-11-12 — Building the live verification harness

- The real bug and fix span two files and two different kinds of logic: `App.jsx`'s selection-cap
  logic (two functions, `handleToggle`/`handleSelectAll`) and `ChatInterface.jsx`'s error-reason
  extraction (a `catch` block) — unlike this fellow's two most recent reports (a single SQL string,
  a single n8n `jsCode` block), this harness needed to extract and run two independent pieces of
  real logic from two different real files and prove both.
- Decided against re-implementing the selection logic from a description and instead spliced the
  REAL, extracted literal source text (`handleToggle`/`handleSelectAll` bodies, copied character-
  for-character from `App.jsx`) into a small Node `vm` driver script that supplies only the ambient
  bindings (`feeds`, `MAX_SELECTABLE_FEEDS`, a `setSelected` shim) the real component already has in
  scope via React state/props — same discipline as this fellow's 2026-10-27 report's
  `verify_effective_severity.mjs` (extract-and-splice, never re-describe). First draft of the driver
  used a different approach (re-implementing the cap/no-cap behavior directly with an `if
  (toggleBody.includes(...))` branch instead of actually executing the extracted text) — caught this
  on review as a shortcut that would make the harness's own claim ("extracts and runs the real
  logic") false; rewrote it to literally splice the extracted `const handleToggle = ...`/
  `const handleSelectAll = ...` text into the vm script and call the real function names, not a
  re-implementation gated by a string check.
- `requireOnce()` (confirming each extracted block occurs exactly once in the real file before
  trusting it) caught nothing wrong this time — both files matched on the first read — but kept the
  check anyway, same as the sibling reports' harnesses, since a silent mismatch here would mean the
  whole B02-B05 narrative quotes code that no longer exists.
- Confirmed via `git -C /Users/pranavijs/mycroft status --short` before and after writing/running
  the harness: identical pre-existing, unrelated diffs both times (two unrelated
  `package-lock.json` files, from other, unrelated Project 29 components, not from this session) —
  `App.jsx`, `ChatInterface.jsx`, and `logs/RUN_LOG.md` are NOT listed as modified, confirming they
  were already committed from the real E1 engineering work done before this video session, not
  altered by this session's read-only harness.
- Caught a real number-conflation risk while writing `FACTCHECK.md`: `E1-VERIFICATION.md`'s
  narrative describes the live, real-world "Select All" overselect as "close to 100" feeds (the
  frontend's own `limit: 100` fetch cap), but its verification table's captured 422 message uses a
  completely different, smaller test input — 15 `feed_ids` — to produce a concrete real validation
  string. The harness's Test 1 runs the pre-fix `handleSelectAll` against a synthetic 411-row list
  (matching the live DB's full row count, not the ~100-feed fetch) specifically to demonstrate "no
  cap at all" unambiguously (result: selects all 411) — a deliberately more extreme input than the
  real browser scenario, chosen for clarity, not a claim that a real session selects 411. Kept this
  distinction explicit in `FACTCHECK.md` item #3/#7 and in the script's own narration ("close to a
  hundred," never "411" or "15" out of context) rather than letting three different numbers (100,
  411, 15) blur into one in the video.

## 2026-11-12 — Audio-first build (Kokoro)

- `generate_audio_kokoro.py` ran clean on the first attempt (voice model already present from this
  fellow's prior episodes). Measured durations came in close to the draft beat sheet's pre-audio
  estimates for most beats, but noticeably longer for the two-bug B03 (estimated 28s, measured
  28.73s — close) and B06 (estimated 32s, measured 29.14s) — kept the real measured numbers as the
  timing target throughout every beat, per the audio-first rule, never padding scenes to hit the
  original estimate.
- B00's silent track: `ffmpeg -f lavfi -i anullsrc ... -t 4.05` measured 4.104s on `ffprobe` (mp3
  frame-boundary rounding, same effect this fellow's prior reports documented) — used the real
  measured value (4.10, rounded) as B00's `actual_duration_s`/timing target, same as every prior
  episode in this series.
- Total measured audio across all 9 beats: 154.34s (B00 4.10 + B01 14.06 + B02 15.34 + B03 28.73 +
  B04 18.38 + B05 29.59 + B06 29.14 + B07 13.49 + B08 1.51).

## 2026-11-12 — Authoring scenes.py (landscape + vertical)

- Wrote a standalone timing checker (AST-parses every `run_time=`/`self.wait()` literal per `Scene`
  class and sums it against `beat_sheet.json`'s measured `actual_duration_s`, kept in the session
  scratchpad, not part of this project folder — same checker pattern this fellow's sibling reels
  documented building) BEFORE rendering anything. Both the landscape `scenes.py` and the hand-
  authored `vertical/scenes.py` matched every beat's measured duration to the millisecond on the
  FIRST pass for both aspects — no arithmetic slip this build, unlike the sibling reel's vertical
  B05 (see that project's own FRICTIONAL.md for comparison).
- Applied every systemic portrait fix this fellow's prior reports' vertical builds already
  documented (the buff=0.68 safe-area floor for 2-line `title.to_edge(UP)`, `next_to(panel, DOWN,
  ...)` instead of an independent `to_edge(DOWN)` for any caption following a variable-height panel
  stack, a height cap via `scale_to_fit_height()` on any multi-panel vertical stack, and generous
  internal buffs/enlarged type for canvas-fill) proactively from the first draft of
  `vertical/scenes.py`, rather than waiting for GATE B/V to re-discover them on this reel's own
  content — this beat sheet has an unusually tall B03 (3 stacked panels: code, backend limit, error)
  that would have been the most likely place for a height-cap omission to actually overflow.
- `static_scene_check.py --class <Name>` ran clean (0 warn/error) on all 9 landscape scenes and all
  9 vertical scenes on the first pass — no GATE A defects this build.

## 2026-11-12 — Manim render / compile (landscape)

- First `./art run` (landscape, native 4K/2160-height default) pass: GATE A clean on all 9 scenes
  going in. GATE B (`manim_layout_audit.py`, strict mode) found 2 real layout warnings on the first
  full pass, both titles pinned too close to the top safe edge: `B03_TwoBugsOneClick`'s title at
  y=3.45 (half-extent is ±3.4) and, after fixing B03 and re-running, `B04_CapAndRealReason`'s title
  at y=3.50 — both real, confirmed directly from `layout_audit.md`'s own reported bounding boxes
  against the documented ±3.4 safe half-height, not false positives. B03 also had its closing
  caption's bottom edge at y=-3.50, same issue on the opposite edge. Root cause for all three: these
  two beats both have unusually TALL stacked content (B03 has 3 panels; B04 has 2 diff blocks), so
  the original `to_edge(UP, buff=0.5)`/`to_edge(DOWN, buff=0.5)` margins — copied from the sibling
  reel's shorter beats — left no room once this reel's own text was substituted in. Fixed by
  widening both buffs (B03's title to 0.7, caption to 0.65; B04's title to 0.75) rather than
  shrinking the panels/type that this project's canvas-fill requirement needs to stay large.
  Re-ran `static_scene_check.py` on each fixed class (clean) before re-rendering just those two
  beats (deleted the stale per-beat `.mp4`s first so `./art run` wouldn't reuse cached output).
  GATE B clean on the second full pass.
- **GATE V (landscape, true final master) — a real underfill, not a false positive:** built the
  true final master manually (`ffmpeg -f concat ...`, same command pattern as every sibling reel —
  `./art final`'s own embedded GATE V has no `--lenient` escape hatch) and ran
  `final_frame_check.py . --mp4 deliverables/landscape/FeedSelectionCap_SaiPranaviJ.mp4 --lenient`
  from inside the reel folder. First true-master pass: **BLOCKER=0, MAJOR=2**, both `underfill`
  findings on `B05_HarnessTable` ("content fills only 38% of the safe area (min 55%)", sampled at
  both the 50% and 85% marks of that beat) — a lower fill ratio than the sibling reel's own B05
  underfill (which measured 50%), because this beat's content (4 short rows + a 2-line message
  swap + a one-line total) is intrinsically smaller than the sibling's 4-tile row. Extracted and
  visually inspected both flagged frames (`ffmpeg -ss <t> ... -frames:v 1 -update 1 ...`) before
  changing anything — confirmed genuine: the block was correctly centered (not top-anchored, unlike
  the sibling reel's root cause), but every individual piece (row text, message panel, totals) was
  sized too modestly and too narrow relative to the safe width, leaving large empty margins on both
  sides and a big gap below. Fixed by enlarging every font size in the beat (rows 16->21-23pt,
  message lines 16->21pt, totals 26->34pt, title 27->32pt) AND setting each panel's width to
  `max(content.width + pad, 11.0)` instead of a pure content-fit width, so the panels span most of
  the safe width rather than floating narrow and centered. Re-ran `static_scene_check.py` (clean),
  re-rendered just B05 — GATE B then caught a NEW, smaller real defect from the same fix: the now-
  taller block's title top edge (y=3.58) and totals bottom edge (y=-3.58) both pushed past the
  +/-3.4 safe half-height. Added a height-cap guard (`if block.height > 6.6:
  block.scale_to_fit_height(6.6)`) — the same systemic pattern this file's own vertical companion
  already used for ITS tallest beats — rather than reverting the enlargement. Applied the identical
  enlarge-plus-height-cap fix proactively to `vertical/scenes.py`'s own B05 before ever rendering
  that aspect, instead of waiting to rediscover the same underfill there.

## 2026-11-12 — Manim render / compile (vertical)

- `./art vertical` scaffolded `vertical/beat_sheet.json`, correctly picking up the hand-authored
  `vertical/scenes.py` already written (same scene class names as the landscape parent, `shot.manim`
  pointing at it, not rewired to a `shot.remotion.pattern` 916 composition) — no Remotion re-render
  step needed. The command's own printed "ONDA CHECK BLOCKED"/"needs native portrait scene916"
  warnings turned out to be a generic message `shorts.py` prints for every beat regardless of lane —
  confirmed harmless by checking the actual written `vertical/beat_sheet.json` (every beat still
  `shot.type: GRAPHIC` with the correct `manim.scene`/`module: scenes.py`) before treating it as a
  real blocker, same as the sibling reel's own documented check.
- Applied the landscape B05 underfill fix (enlarged fonts/panel widths, height-capped block)
  proactively to `vertical/scenes.py`'s own B05 before this aspect's first render — but the first
  `./art run vertical --height 3840` pass still hit a real, SMALLER GATE B warning on B05: the
  block's title top edge (y=3.48) and totals bottom edge (y=-3.48) both pushed just past the
  portrait safe half-height (+/-3.4), because the vertical file's initial height cap (7.0) was
  looser than the value the landscape fix converged on (6.6) and the narrower portrait canvas has
  less horizontal room to "absorb" the same enlarged font sizes, so the block grew taller instead.
  Tightened the cap to 6.6 (matching landscape) and the inter-element buff from 0.3 to 0.26.
  Re-ran `static_scene_check.py --class B05_HarnessTable` (clean) and re-rendered just that beat
  before re-running the full vertical pass — clean on the second attempt (`layout_audit.md`: 3
  snapshots, 0 errors, 0 warnings).

## 2026-11-12 — Personal accuracy re-check (not prompted by any gate)

- Before trusting either true-final master, re-read the real `models.py` line B03 quotes on screen
  (`feed_ids: List[int] = Field(min_items=1, max_items=10)`) directly from the file on disk and
  found the scene had typed a plausible-LOOKING but not-verbatim approximation
  (`feed_ids: list[int] = Field(..., max_items=10)` — lowercase `list`, an invented `...` positional
  arg instead of the real `min_items=1`). This is exactly the kind of error this project's own house
  rule ("verbatim where quoted as real code, never paraphrased") exists to catch, and no automated
  gate checks it (GATE A/B/V only check layout/timing/fill, not string accuracy against the source
  file) — caught by a deliberate side-by-side re-read, not by any tool. Fixed both `scenes.py` and
  `vertical/scenes.py` to the exact real line (wrapped across 2 lines in each, to fit the safe
  width/the portrait column).
- The same re-read caught a second, related defect in B04's `ChatInterface.jsx` diff: the real
  post-fix `reason` line is `detail.map(d => d.msg || JSON.stringify(d)).join('; ')`, but the scene
  had silently dropped the `|| JSON.stringify(d)` fallback without any truncation marker — not
  flagged as elided, just quietly wrong. Fixed the landscape version to the full, real 4-line
  ternary verbatim. The vertical version's existing abbreviation was worse — an entirely
  paraphrased `const reason = ...detail` that wasn't close to the real source at all — rewritten to
  the real tokens across 7 narrower lines, marking the one deliberately-omitted fragment
  (`|| JSON.stringify(d)`) with an explicit `...`, the same honest-truncation convention this
  fellow's sibling reels use for a real line too long to fit a narrow panel (never silently dropping
  part of a real line without saying so).
- Re-ran `static_scene_check.py` and the AST timing checker on all 4 touched scenes (both aspects'
  B03 and B04) before re-rendering any of them — all clean, all still exactly matching their
  measured audio durations (text changes don't affect `run_time`/`wait` literals). Re-rendered B03
  then B04 for both aspects and rebuilt both true final masters a second time from the corrected
  clips before re-running GATE V.

## 2026-11-12 - GATE V (vertical, true final master): a real, severe defect across ALL 9 beats

- Built the true vertical master the same way as the landscape one and ran
  final_frame_check.py . --mp4 ../deliverables/vertical/FeedSelectionCap_SaiPranaviJ.mp4 --lenient
  from inside vertical/. Result: BLOCKER=0, MAJOR=18 -- every single sampled frame across all 9
  beats flagged underfill, with fill ratios of 5-10% (far below the 55% minimum), not just one
  beat. A ratio that low and that uniform across every beat, including ones already confirmed
  visually correct in isolation earlier in this build (B00's title card), was the signature of a
  systemic rendering bug, not nine independent content-sizing mistakes -- extracted and inspected a
  real frame (ffmpeg -ss 2 ... on B00) before touching anything, and confirmed it directly: the
  title card's bordered panel (authored at width=3.9 Manim units, meant to span nearly this file's
  whole ~4.5-unit portrait frame width) rendered as a small box occupying roughly a third of the
  real 2160-pixel-wide frame, dead-center, with huge empty margins on all sides.
- Root cause: this file's own module docstring (written at the START of this build, before any
  vertical beat was authored) already described the sibling reel's portrait-geometry fix in prose
  ("Manim keeps frame_height fixed at 8 regardless of aspect... MAX_W = 3.6 is this file's general
  content-width budget") -- but the actual fix code (a short block patching config.frame_width,
  since manim's CLI derives frame_width from the pixel aspect ratio only once at startup, before
  the -r/--resolution flag is applied, so a bare -r 2160,3840 render leaves frame_width at the 16:9
  default even for a portrait render) was never copied into this file. The docstring stated the
  premise the code needed but never carried it out. No GATE A/B check catches this: GATE A's stub
  doesn't model frame geometry at all, and GATE B's layout audit measures positions in Manim's own
  coordinate space, which was internally self-consistent (everything correctly centered and
  non-overlapping relative to a 14.222-wide frame) -- it never flagged a problem until GATE V
  measured actual rendered pixels against the real safe-area box.
- Fixed by adding the exact patch from this fellow's sibling reel's vertical/scenes.py (copied
  verbatim, not reinvented) immediately after the manim import, before any scene class. This
  required re-rendering ALL 9 vertical beats, not just the 2 already touched for the
  verbatim-accuracy fix above, since every beat was authored under the same wrong assumption and
  was therefore wrong in the same systemic way. Confirmed static_scene_check.py still passes clean
  on all 9 classes (the stub doesn't model frame geometry either, so this fix is invisible to it
  both ways) before clearing every cached vertical render (vertical/media/, vertical/clips/*.mp4,
  vertical/manim/*.mp4, the stale slate) and re-running ./art run .../vertical --height 3840 from
  scratch.
- Rebuilt the true vertical master after the frame_width fix: final_frame_check.py --lenient
  dropped from 18 MAJOR to 2 (B08_BrandOutro, 53% fill against the 55% minimum) -- a real, small,
  separate defect from the systemic one just fixed. First personal frame-inspection attempt at this
  beat (ffmpeg -ss 153.2, picked without computing the beat's actual start time) caught the
  Create()/FadeIn() animation only ~80% complete -- a half-faded border and washed-out text that
  looked alarming but was never what GATE V actually sampled (GATE V always samples at the settled
  50%/85% marks of each beat, well after this beat's 0.45s intro animation finishes). Recomputed the
  real beat boundaries from the cumulative beat_sheet.json durations (B08 starts at 152.83s) before
  re-sampling at the correct 153.585s/154.11s marks, where the beat was already fully rendered and
  correctly colored -- discarded the first inspection as a self-inflicted false alarm, not a real
  finding, rather than chasing a bug that did not exist. Fixed the real underfill by enlarging type
  and spacing; re-rendered, rebuilt the true master a second time: BLOCKER=0, MAJOR=0.

## Closing note

Every entry above is real and dated to when it happened during this single build session
(2026-11-12: research/verification, audio generation, scene authoring, render/compile for both
aspects, and five real defects found and fixed -- the landscape B05 underfill, two verbatim-
accuracy errors in B03/B04 caught by a personal re-read rather than any automated gate, a missing
portrait config.frame_width patch that affected all 9 vertical beats identically, and a small B08
vertical underfill. Nothing here was back-filled after the fact; the config.frame_width miss in
particular was caught only because GATE V's real-pixel measurement on the true final master was
trusted over the internally-consistent-but-wrong layout audit, and because the resulting symptom
(uniform, severe underfill on every single beat) was read as a systemic-bug signature rather than
patched beat-by-beat.
