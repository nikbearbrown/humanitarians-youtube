# BUILD LOG — hai-simple/behind-the-model--correlated-failure-research

Redo of `anthropics/youtube/behind-the-model/correlated-failure-research`
("Correlated Failure in AI Auditing — Consensus Is Not Verification", Teardown-register
CLI 10-beat spine, `register: "Teardown"`, `voice: "am_onyx"` already) as `hai-simple`
(Plain register, Humanitarians AI skin). Source folder untouched. Target reel dir
contained only SUBJECT.json at the start of this invocation.

## Note on provenance: adapted from a content-identical sibling build

Before authoring, I found `anthropics/youtube/hai-simple/behind-the-model--claude-liam-
correlated-failure-research/` — a `hai-simple` redo completed the same day (2026-09-05)
of a **different** source directory
(`behind-the-model/claude-liam-correlated-failure-research`). I diffed the two Teardown
sources' `narration_text` fields beat-for-beat: B01–B08 are **word-for-word identical**
between that source and this reel's source (`behind-the-model/correlated-failure-
research`); only B00's title-card line differs cosmetically ("Nik Bear Brown. Build it
with a CLI, then take it apart." vs. "This is Liam, in for Bear. Nik Bear Brown. Build it
with a CLI, then take it apart.") — irrelevant here since hai-simple always replaces B00
with the hesitant writer. Given the source facts and argument are identical, I adapted
that sibling's already-gated `beat_sheet.json`, `scenes.py` (Manim), `render_scenes.py`,
`SCRIPT.md`, `CARRY-OUT.md`, and `QUESTION.md` for this reel — updating only slug
references, the `source_sheet` path, and the B00 Remotion `seed` (changed to
`hai-correlated-failure-2` so the writer's random jitter isn't identical run-to-run).
This is asset reuse of verified, content-matching work (AGENTS.md: "prefer existing
verified assets and templates over regeneration"), not fabrication — every beat below was
actually rendered and verified in *this* reel's own directory this run.

## What changed vs. source (per redo contract)

- **Register:** Teardown (CLI-explainer PROBLEM/ASK/CODE/OUTPUT/CHANGE/OUTPUT/SUMMARY/
  NEXT-STEPS spine, terminal-ask beats) → Plain (hai-simple's writer-open + one-idea-per-
  beat body + carry-out + your-turn + outro spine). Body recompressed from the source's
  10-beat CLI structure into 8 body beats (B01–B08) carrying the same facts and argument.
- **Cold open:** source's `NikBearBrownOpen` title card → `BrutalistHesitantWriter`.
  Writer types "Three AI judges agree. That means it's verified, right?", hesitates on
  "verified", corrects to "consensus" — the reel's actual wrong guess (agreement among AI
  judges is mistaken for verification), picked up in B02 and falsified by B03's order-swap
  demo.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of source's
  `NikBearBrownOutro`/`ClaudeTitleOutro`.
- **Voice:** unchanged — Liam, Kokoro `am_onyx` (the source already used `am_onyx`).
- **Facts/argument kept:** the ensemble-theory independence requirement; the three
  documented LLM-as-judge biases (positional, verbosity, self-enhancement); the
  positional-bias order-swap demo (source's B05/B06 terminal beats) — promoted to the
  reel's anchor, planted at B03 and paid off at B08; the audit-pairing fix (retrieval /
  code execution / validator, in place of an LLM-on-LLM check); the summary claim that
  more AI agreement is more shared consensus, not more verification. The source's
  Bishop-textbook citation for the ensemble-theory result was dropped from the narration
  (kept as the underlying fact — cross-checking requires independent failure modes — but
  stated generically rather than by section number, appropriate for a general-audience
  Plain-register explainer; QUESTION.md documents this).
- **New content this redo carries, not present verbatim in source:** ONE-FLAG LAW
  requires a single inference flag; B07 carries it — a check only counts as independent
  if it doesn't itself quietly run on the same kind of model underneath (a search index
  or validator built by an AI can reintroduce the exact blind spot it was meant to
  catch). BOTH-DIRECTIONS LAW requires stating what a negative result (disagreement)
  does not prove either; B08 carries this (disagreement between correlated judges
  doesn't confirm either verdict).

## NO-GENAI / NO-PANTRY LAW

No beat in this build is AI-VIDEO, pantry, or a human-drop slot. Every beat is REMOTION
(B00, BCRY, BHTF, BOUT) or bespoke GRAPHIC/Manim (B01–B08), rendered fresh in the
humanitarians palette (`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`).

## Pipeline run this invocation

1. `generate_audio_kokoro.py` — 12/12 beats generated, am_onyx, measured durations written
   back (identical to the sibling build's, as expected given identical narration text).
2. `render_scenes.py` (Manim, reused `scenes.py`) — B01–B08 rendered fresh into
   `manim/*.mp4` in this reel's own directory. All 8 succeeded first pass.
3. `remotion_scenes.py` (foreground) — B00, BCRY, BHTF, BOUT rendered fresh into
   `media/*.mp4`. All 4 succeeded first pass, durations extended to match audio.
4. `compile.py` — forced 4K master (4K LAW), 12/12 beats filled, no slates.
   `content-check` PASS, `frame-check` PASS, `lane-check` PASS.

## Gates

- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **12.8s** (≥9s floor, ≥8s render floor). Verified via frame pull at
  t=11.5s: the writer has typed "Three AI judges agree. That means it's consensus,
  right?" — the correction from "verified" to "consensus" is fully settled on screen.
- **GATE AUDIO:** PASS — `ffprobe`/`ffmpeg volumedetect` on the actual master:
  duration 172.938s, mean_volume **-23.8 dB**, max_volume -2.9 dB (well above the -40 dB
  floor). Master mtime is newer than `beat_sheet.json`.
- **Gate V (frame QC):** contact sheet at 10s intervals across the full 172.9s master
  (17 frames) plus targeted pulls (B00 late frame, BCRY, BOUT) — reviewed directly.
  All body beats legible, safe inset, no text overlap, humanitarians palette correct
  throughout. BCRY carry-out card, BHTF composer card, and BOUT outro (subscribe chip +
  @HumanitariansAI handle) all read cleanly.
- **GATE T (pixel type-check):** PASS, 0 FAILs, on first run — the reused Manim scene
  classes (`CFB01Scene`–`CFB08Scene`) were already added to `type_check.py`'s
  bbox-overlap/kerning exemption lists during the sibling build's Gate T pass (documented
  false-positive classes: pill/card border rings, multi-element compound peak bands),
  and those exemptions are global to the shared script, so they applied here without
  further action.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (12/12
  beats, no violations).
- **Motion histogram:** WARNING, graphic 8/12 (66%, over the ~40% pantry cap).
  Non-blocking and structural for this skill: B00 (writer), BCRY, BHTF, BOUT are REMOTION
  by the hai-simple spine itself, and at 8 body beats this 12-beat reel necessarily runs
  higher than 40% on the graphic side. Same disposition as the sibling build and other
  precedents' identical histogram warning.

## Output

`behind-the-model--correlated-failure-research.mp4` — 172.9s, 3840×2160, 12/12 beats
real (no slate), audible narration throughout (mean -23.8 dB, verified via ffprobe/
ffmpeg directly, not just compile.py's self-report). This is the review cut (COMPLETION
LAW satisfied: mp4 newer than beat_sheet.json, mean_volume verified). `compile.py` forces
a 4K master by default ("4K LAW"), so no separate low-res pass exists for this cut.

## Delivery

Master born natively 3840x2160 via `compile.py`'s 4K LAW, copied directly to `-4k.mp4`
(no separate 4K re-render needed). Delivered via `deliver.py --push`: staged
`DELIVERY/behind-the-model--correlated-failure-research/` (4K mp4 + description) for the
Drive sync, and committed the text artifacts (README.md, beat_sheet.json, SCRIPT.md,
SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md, QUESTION.md — no mp3/mp4) to
`humanitarians-youtube/claude-bear/behind-the-model--correlated-failure-research/`
(commit `527b03d5`). Playlist: **Behind the Model** (direct family-prefix match in
`playlists.json`).
