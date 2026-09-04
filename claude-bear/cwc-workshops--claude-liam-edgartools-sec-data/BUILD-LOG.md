# BUILD-LOG — cwc-workshops--claude-liam-edgartools-sec-data

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/claude-liam-edgartools-sec-data/beat_sheet.json`
(Teardown register, skill-teardown cut of the Anthropic `edgartools-sec-data`
skill). Source was a 7-beat sheet (B00 ClaudeComposerAsk, B01 SkillTeardownAnatomy,
B02 SkillTeardownPipeline, B03 SkillTeardownMechanism, BVDT ClaudeVerdictArtifact,
BHTF, BOUT) whose own AUDIT.md flagged the body as "3 beats / ~113 words; below
the 5-beat/180-word threshold." Built fresh in this reel dir; the source folder
was never touched.

Question/facts unchanged from source: `edgartools-sec-data` is a folder Claude
reads before acting; SKILL.md is the whole instruction set in plain language;
Claude reads the file then executes its Steps in order (linear); the skill
covers exactly four things — company lookup, filings, XBRL financial
statements, and filing sections like Item 1A risk factors — and nothing
outside that. Plain register's mandatory structure (wrong-guess planted+
broken, anchor planted+paid-off, both-directions, one-flag) required
re-segmenting those same facts into 15 beats instead of the source's 7 — no
new facts invented, only one-idea-per-beat pacing. Logged in SCRIPT.md's
"Deliberately not claimed" section.

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW): naive claim "it knows finance now" ->
corrected to "the file", landing on "What does it actually do?". BVDT's
implicit endorsement ("Repeatable. Spec-bounded.") was dropped from BCRY,
which states the fact and stops (no verdict). Close carries the
Humanitarians AI skin (`OutroSeries`) per hai-simple SKILL.md. No source beat
was ai-video-prompt, pantry, or a human-drop slot — every body beat (S01-S10)
is GRAPHIC via a reel-local Manim `scenes.py`/`render_scenes.py` pipeline
(same pattern as the sibling `cwc-workshops--agent-decomposition-skills-vs-tools`
reel); B00/BCRY/BHTF/BOUT are REMOTION. NO-GENAI/NO-PANTRY LAW required no
substitution.

**Two real defects found and fixed this invocation (not present in the
authored beat sheet — found only by rendering and reading actual frames):**

1. **B00's writer animation never completes within its own audio window.**
   Discovered by pulling a frame near the end of the first render (my
   original 4-line/85-char text): the correction and second line were only
   half-typed at t=9.8s of a 9.98s clip. Investigating further, the sibling
   reel `cwc-workshops--agent-decomposition-skills-vs-tools`'s published,
   "DONE" B00 has the *exact same* defect — its last frame is frozen mid-
   correction ("Just add more|", never reaching "fewer" or its second line),
   confirmed by direct frame inspection of that reel's `media/B00.mp4`. Root
   cause: `BrutalistHesitantWriter`'s Root.tsx registration has a **fixed
   606-frame (20.2s) composition duration** regardless of props, so the raw
   render is always ~20s long; `remotion_scenes.py`'s `extend_clip_to_duration`
   is supposed to trim it to the beat's `actual_duration_s` via
   `ffmpeg -t`, but that step silently failed at least twice in this
   session (prints "ok...extended" unconditionally, without checking the
   subprocess return code) leaving the raw ~20s clip in place until compile.py's
   slow-mo path would have (invisibly) stretched or mis-timed it. Fixed by:
   shortening B00's text (2 lines, 71 chars) and speeding up the typing
   params (`charMs` 55->45, `hesitateBetween` 25->10, `mistakeRate` 8->4),
   then manually re-invoking `extend_clip_to_duration` and verifying by frame
   pull at t=3s (mistake visible in accent color), t=6.5s (already corrected),
   and t=9.8s (final question fully typed, cursor at end) — full sequence
   confirmed inside the 9.98s window with margin. **Not fixed in the sibling
   reel** — out of scope for this invocation (never touch another reel's
   folder), but worth a NEEDS-BEAR.md-style flag for whoever revisits it:
   check `extend_clip_to_duration`'s return code / that BrutalistHesitantWriter
   text budgets stay well under the beat's audio length.
2. **BHTF's "Your Turn" composer showed `@NikBearBrown`, not
   `@HumanitariansAI`.** Found via Gate V frame pull. Root cause:
   `ClaudeComposerAsk`'s Root.tsx `defaultProps` hardcodes
   `folderLabel: '@NikBearBrown'`; my beat_sheet.json's BHTF props (copied
   from the sibling reel's own BHTF, which has the same omission) never set
   `folderLabel`, so the wrong handle rendered — a Claude-wash the
   hai-simple SKILL.md explicitly refuses ("HAI keeps its own skin"). Fixed
   by adding `"folderLabel": "@HumanitariansAI"` to BHTF's props, re-rendering,
   and reverifying by frame pull (now reads `@HumanitariansAI`). BOUT
   (`OutroSeries`) already carried the correct handle from authoring.

**Also fixed:** S08 (anchor payoff) first compiled with a WARNING — its raw
Manim clip (2.7s) was slowed 4.0x to fill a 10.7s beat ("extreme slow-mo").
Lengthened S08Scene's own animation (added holds between each sub-reveal) to
raise its raw duration to 8.5s, dropping the stretch to 1.26x; recompiled
clean, no warning.

**Gates:**
- content-check: PASS (14 beats, no violations)
- frame-check: PASS (3840x2160, 14 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py): PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840x2160 h264, audio (aac, 48kHz) present, duration 123.5s;
  mp4 mtime (1788233813) newer than beat_sheet.json mtime (1788233750)
- Gate V (visual): pulled frames at beat midpoints and near-end (settled)
  points across the full runtime. B00 correction/final-question verified
  complete (see above). S03/S08 anchor pair identical composition, teal
  vs. crimson match/no-match added correctly. S09/S10 mirrored construction
  clean (card slots into outline vs. doesn't). BCRY carry-out clean serif
  card. BHTF now correct handle. BOUT clean, `@HumanitariansAI` eyebrow, no
  Claude mascot. **Minor, non-blocking:** in S02/S04, the "FINANCE EXPERT"
  halo label's letters touch the circle's arrow tips/stroke at a few points
  — legible throughout, judged cosmetic rather than a Gate V blocker (same
  severity class as the MINOR findings the source reel's own AUDIT.md logged
  for its B01/B03).
- Advisory: compile.py flagged `graphic` motion share at 71% (10/14 beats),
  over the ~40% pantry-cap guidance in MOTION.md — same situation as the
  sibling reel, inherited from re-segmenting the source's own beat structure
  (all body beats are GRAPHIC/Manim); logged per honesty rules rather than
  silently overridden.

Metadata file written: `cwc-workshops--claude-liam-edgartools-sec-data.md`
(channel @HumanitariansAI, **Playlist: Claude Basics** — SUBJECT.json's
family `cwc-workshops` has no entry in playlists.json; falls through to the
`hai-simple` skill-key entry per the map's documented fallback order).
Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-31 — Phase 4, DELIVERED

Master was already native 3840x2160 (compile.py's 4K LAW forced it directly
off the full-length render — no separate low-res draft pass), so
`<slug>-4k.mp4` is a copy of the same master (matches the sibling
`cwc-workshops--agent-decomposition-skills-vs-tools` reel's precedent: same
byte-identical pattern when no upscale is needed).

Ran `python3 skills/make/hai-simple/loop/deliver.py <REEL> --push`:
- Outbox: `DELIVERY/cwc-workshops--claude-liam-edgartools-sec-data/` (4K mp4 +
  description) — `DELIVERY` is a live symlink straight into the Drive
  `Claude_Bear` folder, so this already IS the Fellows-facing location, no
  separate sync step needed.
- Repo: `humanitarians-youtube/claude-bear/cwc-workshops--claude-liam-edgartools-sec-data/`
  — README.md (= description), beat_sheet.json, SCRIPT.md, SUBJECT.json,
  BUILD-LOG.md, CARRY-OUT.md, QUESTION.md. No mp3/mp4 present in the repo
  copy (verified). Committed and pushed to `origin/main`
  (`199b1f79`).

**Status: DELIVERED.**
