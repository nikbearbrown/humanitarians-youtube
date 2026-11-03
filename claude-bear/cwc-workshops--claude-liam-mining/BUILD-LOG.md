# BUILD-LOG — cwc-workshops--claude-liam-mining

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/claude-liam-mining/beat_sheet.json` (a
Teardown skill-teardown-format reel built from the `agent-battle` workshop's
toy "mining" Claude Skill). Question, facts, and body argument carried over
unchanged: a Claude "skill" is a folder Claude reads before it acts;
"mining" is one file, `SKILL.md`, whose entire content is one sentence
("where diamonds spawn in Minecraft 1.20"); Claude reads that sentence and
acts on it directly (linear, no branching); same question gets the same
answer every run; a question outside the one sentence gets nothing extra.
B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("knows" → "reads" — the newcomer's
actual misconception, picked back up at B02's wrong-guess beat). Register
re-registered Teardown → Plain: the source's B03 design-tell beat ran a
Popper move ("what it bites: anything outside the spec") and BVDT ran a
Plato move (artifact vs. world) as design judgment on whether "mining" is a
*good* skill; both were dropped and their facts folded into B05 as plain
consistency/limit statements, no verdict language. Close re-skinned to
`WantQuote` / `ClaudeComposerAsk` / `OutroCTA` with @HumanitariansAI and
Liam's sign-off. No source beat was ai-video-prompt, pantry, or a
human-drop slot — NO-GENAI/NO-PANTRY LAW required no substitution beyond
B00. Source ran 7 beats (B00/B01/B02/B03/BVDT/BHTF/BOUT); this redo runs 9
(B00–B05 body, BCRY/BHTF/BOUT) — the split adds the wrong-guess beat (B02)
and a dedicated both-directions beat (B05) that Plain register requires and
the Teardown source folded into fewer beats. Full six-move + beat-count
audit in SCRIPT.md.

Built from scratch this session: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (9 beats), scenes.py + render_scenes.py (Manim "chip row"
template — text and layout code copied verbatim from the verified sibling
reel `books--claude-liam-data/scenes.py`, whose `_chip()` root-caused three
GATE T defects; reusing it here starts from a known-passing baseline).

Pipeline run in full:
1. `generate_audio_kokoro.py` — 9/9 beats, `am_onyx`, actual_duration_s
   written back. B00 measured 9.15s (TIMING LAW floor is 8s — met).
2. `render_scenes.py` — 5/5 GRAPHIC beats (B01–B05) rendered via Manim, no
   failures.
3. `remotion_scenes.py` — 4/4 REMOTION beats (B00, BCRY, BHTF, BOUT)
   rendered, all foreground, exit 0.
4. `compile.py` — `cwc-workshops--claude-liam-mining.mp4`, 9/9 beats real
   (no slate), 84.58s, 3840×2160.

**Gates:**
- content-check: PASS (9 beats, no violations)
- frame-check: PASS (3840×2160, 9 beats, no violations)
- lane-check: PASS (cut=master, no lane violations)
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio present, duration 84.58s; mp4 mtime
  newer than beat_sheet.json mtime (COMPLETION LAW satisfied)
- Gate V (visual): pulled 14 frames at 6s spacing across the full runtime
  plus targeted pulls around B00 and the BHTF→BOUT transition, and read them
  directly — B00's correction ("knows" → "reads") is legible partway through
  typing; every chip beat reads cleanly (no overlap, safe inset respected);
  the B03→B05 anchor pair reuses the SKILL.md/1 SENTENCE composition so the
  payoff reads as the same object returning; the brief white frame at the
  BHTF→BOUT cut is the OutroCTA card's own white background fading in, not a
  compile defect; BHTF/BOUT carry the @HumanitariansAI handle and Liam
  sign-off correctly. No blockers.
- B00 TIMING LAW: `actual_duration_s` 9.15s (≥8s requirement met); the
  "knows" → "reads" correction lands on screen and is confirmed by frame pull.

**Non-blocking warning (compile.py):** motion histogram graphic:5
remotion:4 — graphic at 55%, over the ~40% pantry cap in MOTION.md.
Structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as REMOTION
against a compact 5-beat GRAPHIC body that mirrors the source's own thin
3-body-beat argument (source: one file, one sentence, linear pipeline) plus
the wrong-guess and both-directions beats Plain register adds — the ratio
follows beat count on a short, source-thin reel, not a choice made in this
build. Logged per the honesty rule rather than padding beat count to dodge
the warning.

Metadata file written: `cwc-workshops--claude-liam-mining.md` (channel
@HumanitariansAI). Per playlists.json, `SUBJECT.json`'s `skill` field
(`hai-simple`) has a direct map entry → **Playlist: Claude Basics**, and the
content (what a Claude Skill is) matches that playlist exactly — no
override needed. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
