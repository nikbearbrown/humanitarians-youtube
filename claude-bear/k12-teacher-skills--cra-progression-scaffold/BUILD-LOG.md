# BUILD-LOG.md — k12-teacher-skills--cra-progression-scaffold

## 2026-09-02 — Phase 0-3, review cut

Picked up mid-build: SCRIPT.md, CARRY-OUT.md, QUESTION.md, beat_sheet.json
(redo mode, source `anthropics/k12-teacher-skills/youtube/cra-progression-scaffold`),
scenes.py/render_scenes.py, and all 8 beats' Kokoro audio (mp3/timings.json)
already existed from a prior attempt. Verified and continued rather than
rebuilding:

- Audio: all 8 beats already generated (`am_onyx`), durations in
  `mp3/timings.json` matched `actual_duration_s` in beat_sheet.json.
- Manim GRAPHIC beats NB01-NB04: already rendered in `manim/`.
- Remotion beats: B00 and BCRY already rendered; BHTF and BOUT were not —
  rendered both via `remotion_scenes.py` (ran past the tool's 120s
  foreground timeout and was auto-backgrounded by the harness; monitored it
  to completion via the Monitor tool rather than ending the turn, per the
  ONE-SHOT/COMPLETION LAW — never treat an auto-backgrounded render as
  "handled," always block on its actual exit).

**GATE T (type_check.py): FAIL -> PASS, three defects fixed:**

1. **NB01, NB03 chip labels too long** — the generic chip-row template's
   width-fit downscale (`_chip()` in scenes.py) shrank
   `"REPRESENTATIONAL"` (single unbroken word, no compressible spaces) and
   `"EXPERT: circles are NOISE"` below the 20px/1080p floor. Shortened chip
   text (`"REPRESENTATIONAL"` alone, `"ABSTRACT: 5/6"`, `"EXPERT: NOISE"`)
   and widened the fit-to-box fraction in `_chip()` from 0.82 to 0.90.
2. **NB01 "CONCRETE: circles" — genuine legibility defect, not a false
   positive.** It was the only lowercase word across every chip in the
   entire reel; x-height-only lowercase glyphs render shorter than the
   tracked-caps used everywhere else in the template, and after the
   width-fit downscale its measured height fell to 17px. Fixed by making
   it uppercase (`"CONCRETE: CIRCLES"`) for consistency with every other
   chip label — confirmed by direct pixel measurement (debug harness
   against `type_check.py`'s own `visible_text_mask`/`text_run_bboxes`)
   that this, not the REPRESENTATIONAL chip, was the smallest run.
3. **BOUT (OutroSeries) — validator false positive, fixed via content, not
   the validator.** The eyebrow's "·" (middle dot) separator rendered as
   an isolated blob whose aspect ratio (55x35px) just cleared the
   `text_run_bboxes` narrow-glyph filter (w >= h*1.5), so it became the
   *only* detected text-run blob in the frame — which suppressed the
   individual-character fallback that would otherwise have measured the
   real, fully legible 100px+ title text. This is the same middot
   failure class already documented elsewhere in `type_check.py` (line
   ~422, a different check). Per "fix content, never the validator,"
   swapped the eyebrow separator from "·" to " — " (em dash), which the
   flat-rule filter excludes cleanly. Re-rendered BOUT; confirmed via the
   same debug harness that it now measures 41px >= 41px floor.

Root-caused all three with a direct debug script (imported
`type_check.py`'s own `visible_text_mask` / `labeled_blobs` /
`text_run_bboxes` / `check_min_size` against extracted frames) rather than
guessing from the TYPECHECK.md summary line alone — this is what separated
the one genuine legibility defect (NB01 lowercase "circles") from the one
pure validator false positive (BOUT's middot).

**Compile:** `compile.py` -> `k12-teacher-skills--cra-progression-scaffold.mp4`,
129.8s, native 3840x2160 (every beat source was already 4K/1080p-native;
no upscale needed). Exceeded the tool's 120s foreground timeout and was
auto-backgrounded; monitored to completion (exit 0) before proceeding.

**Gate V (visual):** pulled frames every 6s across the full 130s runtime
(22 frames) and read every one. B00's correction ("separate" -> "as three
entry points") lands on screen well before the 9.94s beat ends. All four
manim chip rows (NB01-NB04) read clean and parallel-sized after the GATE T
fixes above. BCRY/BHTF/BOUT (Remotion) show correct title, paste-ready
prompt, and the re-fixed eyebrow — no truncation, no overlap, safe inset
respected throughout. No blockers.

**Audio presence:** `ffmpeg -af volumedetect` on the master ->
mean_volume -23.9 dB, max_volume -2.7 dB (well above the -40 dB floor).

Metadata file written: `k12-teacher-skills--cra-progression-scaffold.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`k12-teacher-skills`) matches no
map prefix; falls through to the `hai-simple` skill-key match (-> "Claude
Basics"), consistent with the `k12-teacher-skills--claude-liam-k12-lesson-differentiation`
sibling. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
