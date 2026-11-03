# BUILD-LOG — claude-quickstarts--macos-computer-use-coordinate-roundtrip

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-quickstarts/youtube/macos-computer-use-coordinate-roundtrip/beat_sheet.json`
(a Teardown-register scaffold built from `computer-use-best-practices/computer_use/image.py`;
its own metadata claimed 4/8 beats filled as MANIM, but no `manim/` directory
existed on disk anywhere in that source folder — the claimed fills were never
actually rendered, so this was effectively an unbuilt scaffold, same situation
as the `claude-quickstarts--browser-coordinate-scaling` sibling redo). Question
and mechanism carried over unchanged: macOS Retina screenshots exceed the API's
image budget (long edge ≤ 1568px, tile count ≤ 1568 across 28×28 tiles);
`target_image_size()` resizes first, and the inverse (`real = model × native/sent`)
recovers the real click. B00 replaced the source's `ClaudeComposerAsk` cold open
with `BrutalistHesitantWriter` (WRITER LAW: "exact" → "scaled"). Register
re-registered Teardown → Plain (source narration carried no design judgment to
remove). Close/outro re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Source's B05 verdict/recap beat dropped as a restatement (matches the
sibling's precedent); source's B06/B07 collapsed into BHTF/BOUT. No source beat
was `ai-video-prompt`, pantry, or a human-drop slot (B00 was already
`ClaudeComposerAsk`, unbuilt), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00.

**Factual correction made during this redo (logged per honesty rules):** the
source scaffold's own B00 paired a native 2560×1600 screen (aspect 8:5 = 1.6)
with a sent size of 1456×819 (aspect 16:9 = 1.778) — two different aspect
ratios, which `target_image_size()` cannot produce since it preserves the
native aspect ratio by construction. That 1456×819 figure is actually the
*browser tool's* fixed 16:9 target (`CLAUDE_ACTUAL_WIDTH`/`HEIGHT`, verified
against the sibling `claude-quickstarts--browser-coordinate-scaling` reel's
own SOURCES.md), not this macOS reference implementation's output. Carrying
that number forward would have asserted a false claim on screen, so this redo
derived a fresh, internally consistent worked example instead: applying the
documented constraints (aspect preserved, long edge ≤1568px, tile count ≤1568
across 28×28 tiles) to a native 2560×1600 screen gives sent = 1344×840 exactly
(tile count 48×30 = 1440 ≤ 1568, long edge 1344 ≤ 1568, aspect 1344/840 = 1.6
= 2560/1600). Worked click (630, 420) → inverse (1200, 800), exact integers
(630/21 = 30, 420/21 = 20, 2560/1344 = 1600/840 = 40/21) — no rounding. Full
derivation in SOURCES.md.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`. Measured durations:
   B00 12.91s, B01 31.62s, B02 18.75s, B03 27.95s, B04 26.50s, BCRY 10.56s,
   BHTF 24.85s, BOUT 5.55s.
2. Wrote `scenes.py` (4 Manim scenes, B01–B04) sized to the measured
   durations, and `render_scenes.py`; rendered all four in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (the shell auto-backgrounded it past its 120s default timeout; polled the
   process directly with an until-loop rather than ending the turn, then read
   the completed output before proceeding — never treated the background move
   as done until the exit was observed).
4. B00's TIMING LAW checked directly: measured duration 12.91s (well over the
   ≥9s window), and a late frame pull (11.5s) confirmed the writer's
   correction ("exact" → "scaled") completes and rests legibly as "my screens
   scaled spot right?" before the beat ends.
5. `compile.py` → first pass, 8/8 real (no slate), 159.7s, 3840×2160
   (THE 4K LAW), GATE AUDIO PASS -24.0 dB.
6. **Gate V (visual) caught one real layout bug, fixed at the root:** B04's
   boundary-case note card ("already fits the budget → sent = native, nothing
   to invert") was sized 1.5×1.6 Manim units — too narrow for its own caption
   text at font_size 18; a frame pull showed the leading "a" of "already" and
   trailing "t" of "invert" clipped by the card's border on both sides. Fixed
   by widening the card to 2.5×1.7, shortening the caption to four short
   lines ("already fits / the budget → / nothing to / invert"), and
   re-centering it 0.3 units left of its original position for extra margin
   from the frame edge. Re-rendered B04 only, recompiled, and verified on a
   fresh frame pull (t=12s into manim/B04.mp4) that all four lines sit fully
   inside the card with clean margin on every side.
7. Full Gate V pass: pulled a frame at the temporal midpoint of every one of
   the 8 beats (using each beat's measured `actual_duration_s`, not a blind
   fixed-interval grid) plus the late-B00 correction frame, and read all of
   them directly. B00's correction lands and rests legibly. B01→B02→B04's
   anchor triple (native 2560×1600 / sent 1344×840, same button dot) is
   visually recognizable as the same rectangle pair across all three
   appearances, per ANCHOR LAW — B02's raw-pixel miss (cross mark, "nowhere
   close to the button") and B04's scaled hit (check mark, "(1200, 800)")
   read as clear opposites of the same setup. B03's formula card and BCRY/
   BHTF/BOUT are centered, legible, no overlap, safe inset respected, HAI
   skin correct throughout (@HumanitariansAI, no Claude branding, "Fable 5 /
   High" is `ClaudeComposerAsk`'s own default label — unchanged from the
   already-shipped sibling reel's identical usage). No blockers remaining.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py): PASS (0 FAILs, all 8 beats checked)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio aac present, duration 159.70s; mp4
  mtime (10:50:04) newer than beat_sheet.json mtime (10:32:14)

**Non-blocking warning (compile.py):** motion histogram remotion:4 graphic:4
— remotion at 50% of beats, over the ~40% pantry cap. Structural, not a
defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn)
+ BOUT (outro) all REMOTION by skill contract, against 4 GRAPHIC body beats
for this 8-beat reel — same ratio, same already-accepted warning, as the
sibling `claude-quickstarts--browser-coordinate-scaling` reel.

**Zero inference flags:** the mechanism and constraints (aspect-preserving
binary search, 1568px edge cap, 1568-tile cap, 28×28 tiling) are a direct
read of `image.py`/`constants.py`, carried from the source scaffold's own
SOURCES.md. The specific worked numbers in this reel are this reel's own
arithmetic applying those documented constraints exactly, not a new claim
about Claude's internals — per ONE-FLAG LAW, no flag is needed. Full
derivation and citations in SOURCES.md.

Metadata file written: `claude-quickstarts--macos-computer-use-coordinate-roundtrip.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `hai-simple` prefix,
since `claude-quickstarts` has no direct entry in the map — plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
