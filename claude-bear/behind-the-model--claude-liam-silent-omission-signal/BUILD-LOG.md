# BUILD-LOG — behind-the-model--claude-liam-silent-omission-signal

## 2026-09-05 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/behind-the-model/claude-liam-silent-omission-signal/beat_sheet.json`
— metadata `register: "Teardown"`, `brand: "claude-liam"`, build `cut:
"review"`, 4 of 9 array entries filled (B01-B04 rendered as Manim video;
B00/B05/B06/YOURTURN/B07 left as unfilled slates, plus 3 further unfilled
BOOKEND slates — BVDT/BHTF/BOUT — carrying only placeholder text, never
reconciled with the earlier beats). Followed
`hai-simple/claude-basics--screenshot-prompt-caching` as the concrete
precedent — same source shape (4 filled body beats + an unfilled verdict +
duplicated/unreconciled handoff beats + abandoned bookend slates).

Question and body facts carried over unchanged: an agent asked to
summarize a folder processes only what it can reach and presents that as
complete, with no error/warning/count; agents optimize toward task
completion so a tool-call failure stays internal unless the task explicitly
asks for it to be surfaced; the recognition sign is an absent processed-
count where a complete run would carry one ("eight documents found, eight
processed"); the fix is a required inventory artifact (items in scope,
processed, skipped, denied); neither direction is guaranteed by the count
alone (a match doesn't prove the rest is right, a mismatch doesn't always
mean something important was lost).

B00 replaced the source's B00 (which was itself a stray "Your turn, paste
this" ask misplaced as the cold open, with no wrong-guess framing) with
`BrutalistHesitantWriter` (WRITER LAW: "flag" -> "skip" — the newcomer's
assumption that a missing file gets flagged, corrected to: it gets silently
skipped). Register re-registered Teardown -> Plain (the source narration
itself carried no verdict on anyone's design choices beyond stating the
mechanism, so no judgment needed removing). Source's B05 (verdict) folded
into a dedicated BCRY (carry-out); source's B06 (mid-reel actionable
paste-prompt) and YOURTURN (concept-audit paste-prompt) folded into one
BHTF, keeping B06's actionable inventory instruction since it is the one a
viewer can actually run today. The 3 abandoned bookend slates (BVDT/BHTF/
BOUT) were not carried forward — their content duplicates B05/YOURTURN and
were never filled in the source. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. No source beat was `ai-video-prompt`,
pantry, or a human-drop slot (B01-B04 were already Manim video; B00/B05/
B06/YOURTURN/B07 were already `ClaudeComposerAsk`/Remotion shapes, just
unfilled and under the wrong register/skin), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00 (covered by WRITER LAW anyway).

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`. Durations: B00
   10.01s, B01 14.68s, B02 15.85s, B03 13.55s, B04 26.26s, BCRY 13.59s,
   BHTF 20.99s, BOUT 3.46s.
2. Wrote `scenes.py` (4 Manim scenes, B01-B04) sized to the measured
   durations, and `render_scenes.py`; rendered all four in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (the first invocation exceeded the tool's 300s timeout and was
   auto-backgrounded; blocked on it by polling the task's output file until
   exit 0, per the COMPLETION LAW/ONE-SHOT warning — never ended the turn
   waiting on it).
4. B00 verified directly: `media/B00.mp4` = 10.03s (>= 8s TIMING LAW);
   pulled a frame at t=8.5s showing "flag" already corrected to "skip" and
   held, comfortable margin before the clip ends.
5. `compile.py` -> `behind-the-model--claude-liam-silent-omission-signal.mp4`,
   8/8 real (no slate), 3840x2160 (THE 4K LAW), 119.4s.

**GATE T (type_check.py) — two real min-size defects found and fixed, plus
one non-obvious false-positive class traced and fixed at the root:**

- First pass: 2 FAILs (B03, B04) at "smallest text run 11px/10px < floor
  20px". B03's cause was plain undersized labels/checkmark glyph (font_size
  18-30) — fixed by bumping to 24-26 (60 for the isolated checkmark glyph,
  which needs much more headroom than a word run). That alone cleared B03
  but B04 stayed at exactly 10px across three subsequent fixes (removing a
  `DashedVMobject` "blank" placeholder that turned out to be unrelated, and
  replacing an isolated "=" glyph in the struck claims with the word
  "MEANS" — both good hygiene, matching the isolated-punctuation false-
  positive class documented in the `screenshot-prompt-caching` BUILD-LOG,
  but neither was the actual cause here). Root cause, found by extracting
  the checker's exact sampled frame and running `check_min_size` /
  `text_run_bboxes` directly against it: the terracotta (`TERRA`) strike-
  through `Line` drawn across "MISMATCH MEANS SOMETHING IMPORTANT LOST" was
  a *different* color than the ink-colored text it crossed, so the
  ink-color mask saw the line as a non-text gap that visually bisected each
  letter into a ~10px top stub and ~10px bottom stub — two "text-run"-
  shaped fragments per letter, both under the floor. Fixed by coloring both
  strike lines (B04's claim1/claim2) `INK` instead of `TERRA`, so the mask
  treats line and letters as one continuous connected region (full letter
  height) rather than splitting them. Re-ran GATE T: PASS (0 FAILs).
- This is a new false-positive/defect class worth naming for future builds:
  **a strikethrough (or any line) drawn across text in a color the ink mask
  doesn't recognize will bisect every letter it crosses into two tiny
  sub-floor fragments.** Match the line's color to the text it strikes, or
  don't cross the letters at all.

**Gate V (visual):** pulled frames across the full 119.4s runtime with
*accurate* seeking (`-ss` after `-i`) after a first pass with fast seeking
(`-ss` before `-i`) produced a badly corrupted-looking B01 frame at t=20s —
confirmed by direct comparison against the raw `manim/B01.mp4` render (clean
at the equivalent timestamp) and a re-extraction of the same master
timestamp with accurate seeking (also clean) that the corruption was purely
an ffmpeg fast-seek artifact from my own frame-pulling, not a defect in the
compiled video. With accurate seeking: B00's correction ("flag" -> "skip")
lands with margin; B01's confident report card + uncounted ghost documents
read cleanly; B02's two-lane completion-vs-internal-log diagram reads
cleanly; B03's anchor (8 found/8 processed vs. a blank actual count) and
B04's payoff (the same card pair, now 8/6/2 with the 2-item gap called out,
plus the two struck both-directions claims) are visually recognizable as
the same object per ANCHOR LAW. Caught one cosmetic-only nit past GATE T:
B04's "6processed /2skipped" ran together with no space (a `buff=0.04` too
tight in the `VGroup.arrange`) — bumped to `buff=0.12`, re-rendered,
recompiled, reconfirmed GATE T PASS and re-pulled the frame to confirm the
spacing. BCRY's carry-out card, BHTF's Your Turn prompt (Fable 5 model chip
visible, paste-ready instruction legible), and BOUT's @HumanitariansAI
outro/subscribe card all render legibly with safe inset respected. No
blockers remaining.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840x2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the fixes above
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840x2160 h264, audio aac present, duration 119.4s; mp4
  mtime (1788600651) newer than beat_sheet.json mtime (1788599759)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:4 — remotion at 50% of beats, over the ~40% pantry cap. Structural,
not a defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF
(Your Turn) + BOUT (outro) all REMOTION by skill contract, against 4
GRAPHIC body beats for this 8-beat reel — same disposition as every other
8-beat hai-simple reel in this family. Logged per the honesty rule rather
than reworking beat count to dodge the warning.

Metadata file written: `behind-the-model--claude-liam-silent-omission-signal.md`
(channel @HumanitariansAI, Playlist: **Behind the Model** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `behind-the-model`
family prefix — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
