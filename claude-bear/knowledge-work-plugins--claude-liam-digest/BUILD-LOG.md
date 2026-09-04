# BUILD-LOG — knowledge-work-plugins--claude-liam-digest

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-digest/beat_sheet.json`
(7-beat Teardown "skill-teardown" sheet for the Anthropic `digest` skill,
brand `claude-liam`, @NikBearBrown).

**Source note:** the source sheet's narration already carries real,
specific facts about the skill — generate a daily or weekly digest of
activity across all connected sources; used when catching up after time
away, starting the day, or reviewing a week's decisions and document
updates grouped by project; defaults to `--daily` if no flag is specified
(the source's B03 "design tell") — see QUESTION.md. No reconstruction was
needed. Used the `knowledge-work-plugins--claude-liam-analyze` sibling reel
(identical source shape: cold open / anatomy / pipeline / design-tell /
verdict / handoff / outro) as the structural template — its scaffold
conventions (TEAL-border Manim cards, `render_scenes.py`, humanitarians
palette) were reused directly.

**The call:** register re-registered Teardown -> Plain. Source's BVDT
framed "know the limit: only what the file says" as a verdict — Teardown
language — removed; Plain states only the mechanism (reads one file,
follows its steps, defaults to daily unless told otherwise) and its two
failure directions as properties of the practice, never a verdict on the
skill's design. B00 replaced the source's `ClaudeComposerAsk` cold open
with `BrutalistHesitantWriter` per WRITER LAW: "watching" -> "waiting" —
the naive assumption that Claude keeps continuous watch over connected
sources, corrected to: it waits, dormant, until asked. Added a wrong-guess
beat (B01: continuous awareness vs. a written ask-then-default procedure,
falsified by "come back from a week away, ask without saying weekly, and
what surfaces is Friday — six days never make it in") and an anchor (B02 ->
B03: Monday, a week away, unnamed window, traveling asked -> reads file ->
steps run -> returned "Friday only", then paid off into "still unset, same
one-day default" / "said weekly, all seven days") per this factory's PHASE
1 structure requirement — the source's Teardown shape (anatomy / pipeline /
design tell / verdict) carried neither. The source's own design-tell fact
(default to `--daily`) became the reel's falsifying case AND its
both-directions payoff, rather than a flatly stated constraint. Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Kept the
source's 7-beat count (B00, B01, B02, B03, BCRY, BHTF, BOUT). No source
beat was AI-VIDEO, pantry, or a human-drop slot — every source beat was
already REMOTION (`ClaudeComposerAsk`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW required no beat replacement
beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 9.77s (clear of the >=9s TIMING LAW floor)
   on the first narration draft (30 words + `lead_silence_s: 0.8`).
   Durations: B00 9.77s, B01 21.12s, B02 25.60s, B03 20.35s, BCRY 8.83s,
   BHTF 16.26s, BOUT 4.27s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `DIGB01Scene` /
   `DIGB02Scene` / `DIGB03Scene`, ported from the `analyze` sibling's
   TEAL-border card convention plus a new recurring "week strip" anchor
   visual — 7 boxes, lit boxes terracotta) and `render_scenes.py`; rendered
   B01/B02/B03 clean on the first pass, foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`, foreground. The
   shell tool's default 120s timeout moved the render to background
   automatically; per the one-shot COMPLETION LAW this was NOT treated as
   a hand-off — blocked on `TaskOutput` (590s budget) in the same turn
   until it exited (code 0) before proceeding. All four beats rendered
   clean on the first pass.
4. `compile.py` — first pass -> 7/7 real (no slate), 3840x2160 (THE 4K
   LAW), mean_volume -24.0 dB (GATE AUDIO pass on the first compile).
5. GATE T (`type_check.py`) FAILED on the first pass (2 pixel beats: B01
   kerning, B03 min-size) — fixed content, not the validator, across four
   iterations:
   - B01 kerning "max inter-glyph gap 36px > threshold 13px": traced by
     directly importing `type_check.py`'s own `check_kerning_sanity` /
     `extract_frame` / `best_video` functions and replaying the exact pixel
     analysis locally (rather than guessing) — the checker samples the
     single peak-ink row of the whole frame, and that row was the scene's
     title, "ALWAYS AWARE, OR ASKED?". The word "ALWAYS" (and, at a smaller
     size, "ALWAYS AWARE" used as a card label) produces an anomalous
     Pango/Montserrat-Bold glyph-run split at this font size that the pixel
     scanner misreads as an oversized kerning gap — confirmed a red herring
     by cropping and zooming the actual rendered frame (letters read
     perfectly evenly spaced to the eye). Fixed by rewording the title to
     "TRACKING EVERYTHING, OR ASKED?" and the struck card label to "AWARE
     ALL WEEK" (both avoid the word "ALWAYS"); re-verified PASS by
     re-running the checker's own function against the new render before
     doing a full recompile.
   - B03 min-size "smallest text run 14px < floor 20px": the condensed
     THE-ANCHOR-RETURNS row was scaling its labels down together with the
     cards via `row.animate.scale(0.6)`, dropping the labels' effective
     font size below the floor even though the composition read fine
     on-screen. Fixed by scaling only the chrome (cards + connector lines)
     and re-planting fresh, fixed-size labels afterward — never scaling a
     `Text()` mobject below its final legible size — then bumping the
     remaining borderline (`font_size=20`) labels to 22 for margin.
   Re-ran `type_check.py` after each fix; GATE T PASSED clean (0 FAILs) on
   the fifth attempt.
6. Gate V (visual, manual): pulled 12 evenly-spaced frames across the full
   107.2s runtime (`fps=1/9`) and read every one directly. B00's writer
   mid-type ("was Claude|"), B01's struck "AWARE ALL WEEK" figure beside
   the lit "ASK, THEN DEFAULT DAILY" card and the falsifying caption "week
   away, no flag: Friday only", B02's four-stop anchor with the traveling
   "MONDAY, WEEK AWAY" token landing on a week-strip with only the last box
   lit, B03's condensed anchor-return splitting into "STILL UNSET / SAME
   DEFAULT (checkmark)" vs "SAID WEEKLY / ONE DAY? (struck)" with both week
   strips fully legible, BCRY's carry-out quote, BHTF's Your Turn composer
   card (@HumanitariansAI, correct topic/prompt), and BOUT's `OutroCTA`
   (@HumanitariansAI, Subscribe) all render legibly with no overlap, no
   clipping, no contrast issues. No defects found.
7. Audio presence: independently verified with `ffprobe` (aac stream, mono,
   48000 Hz present) and `ffmpeg -af volumedetect` on the final master ->
   mean_volume **-24.0 dB**, max -2.9 dB. Master mtime (1788468186) is
   newer than beat_sheet.json mtime (1788467660).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), fifth pass (two content fixes: B01 kerning
  false-positive traced to the word "ALWAYS" at this font/weight; B03
  min-size from scaling labels below the floor)
- Gate V: PASS, first pass — no defects found across 12 sampled frames
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 107.2s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

**Playlist resolution:** family `knowledge-work-plugins` matches the
`knowledge-work-plugins` key in
`skills/make/hai-simple/loop/playlists.json` directly, resolving to
**Extending Claude — Skills, Plugins & Connectors**.

Metadata file written:
`knowledge-work-plugins--claude-liam-digest.md` (channel @HumanitariansAI,
Playlist: **Extending Claude — Skills, Plugins & Connectors**, plus the
direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-03 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp knowledge-work-plugins--claude-liam-digest.mp4 \
   knowledge-work-plugins--claude-liam-digest-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/knowledge-work-plugins--claude-liam-digest/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/knowledge-work-plugins--claude-liam-digest/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `84436e03`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
