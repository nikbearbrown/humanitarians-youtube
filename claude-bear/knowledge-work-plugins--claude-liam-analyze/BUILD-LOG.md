# BUILD-LOG — knowledge-work-plugins--claude-liam-analyze

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-analyze/beat_sheet.json`
(7-beat Teardown "skill-teardown" sheet for the Anthropic `analyze` skill,
brand `claude-liam`, @NikBearBrown).

**Source note:** the source sheet's narration already carries real,
specific facts about the skill — answer data questions from quick lookups
to full analyses; used when looking up a single metric, investigating
what's driving a trend or drop, comparing segments over time, or preparing
a formal data report for stakeholders — see QUESTION.md. The
`source_skill` path it names (a different machine's home directory) does
not exist locally, but no reconstruction was needed. Used the
`financial-services--claude-liam-dd-meeting-prep` sibling reel (same
source shape: anatomy/pipeline/design-tell/verdict skill-teardown) as the
structural template — its scaffold conventions (TEAL-border Manim cards,
`render_scenes.py`, `scenes.py` docstring guidance) were reused directly.

**The call:** register re-registered Teardown -> Plain. Source's B03/BVDT
framed "what it gets right / what it bites" as a design-tell verdict —
Teardown language — removed; Plain states only the mechanism (read the
question, match it to one of four shapes, run the file's steps in order,
return one answer) and its two failure directions as properties of the
practice, never a verdict on the skill's design. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER
LAW: "instinct" -> "the file" — the naive assumption that a sharp data
analysis comes from Claude's own feel for the numbers, corrected to: it
reads the question against a file. Added a wrong-guess beat (B01: an
analyst's private feel for what's interesting vs. a four-shape
question-to-steps procedure, falsified by "ask it something outside those
four shapes and it has no procedure tailored to reach for") and an anchor
(B02 -> B03: weekly signups drop twelve percent, traveling asked ->
matched -> stepped -> returned "organic search fell," then paid off into
"run twice, same driver" / "a marketing-budget question outside the four
shapes has nothing tailored to reach for") per this factory's PHASE 1
structure requirement — the source's Teardown shape (anatomy / pipeline /
design-tell / verdict) carried neither. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Kept the source's 7-beat count (B00,
B01, B02, B03, BCRY, BHTF, BOUT). No source beat was AI-VIDEO, pantry, or a
human-drop slot — every source beat was already REMOTION
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so
NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 10.13s (clear of the >=9s TIMING LAW
   floor) on the first narration draft (30 words + `lead_silence_s: 0.8`).
   Durations: B00 10.13s, B01 26.79s, B02 20.48s, B03 18.88s, BCRY 12.76s,
   BHTF 18.84s, BOUT 3.63s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `ANLB01Scene` /
   `ANLB02Scene` / `ANLB03Scene`, ported from the `dd-meeting-prep`
   sibling's already-fixed TEAL-border card convention) and
   `render_scenes.py`; rendered B01/B02/B03 clean on the first pass,
   foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`, foreground. The
   shell tool's default 120s timeout moved the render to background
   automatically; per the one-shot COMPLETION LAW this was NOT treated as
   a hand-off — blocked on `TaskOutput` (590s budget) in the same turn
   until it exited (code 0) before proceeding. All four beats rendered
   clean on the first pass; confirmed BHTF's explicit
   `folderLabel: "@HumanitariansAI"` override rendered correctly.
4. `compile.py` — same background-timeout situation, same TaskOutput
   block-until-exit handling. First pass -> 7/7 real (no slate),
   3840x2160 (THE 4K LAW), mean_volume -24.1 dB (GATE AUDIO pass on the
   first compile). B01's 26.8s beat (longer than its ~11.4s raw Manim
   render) required a 2.35x slowdown to fill — noted for Gate V review, no
   legibility issue found.
5. GATE T (`type_check.py`) PASSED clean on the first pass — 0 FAILs
   across all 7 beats (all §8.10 checks SKIP, as expected for
   non-drawtext beats).
6. Gate V (visual, manual): pulled 12 evenly-spaced frames across the full
   112.5s runtime plus three targeted late-beat frames (B00 at t=9.5s to
   confirm the writer's correction; B03 at t=74s to catch the struck
   "TAILORED?" word past its fade-in; BOUT at t=110s, since the coarse
   9s-interval sampling missed it) and read every one directly. B00's
   correction ("instinct" -> "the file") is fully typed and settled by
   t=9.5s of a 10.1s beat; B01's struck analyst's-feel figure and lit
   four-shape procedure card read cleanly, including the "shape not
   listed — no procedure" caption outside the card border; B02's
   four-stop anchor (ASKED/MATCHED/STEPPED/RETURNED, with the traveling
   "SIGNUPS DROP 12%" token beside each TEAL-bordered card) is legible at
   every step, landing on "organic search fell"; B03's condensed
   anchor-return and both-directions split (struck-through "TAILORED?"
   fully rendered and settled by ~t=74s of an 18.9s beat) read cleanly;
   BCRY's carry-out quote, BHTF's Your Turn composer card (confirmed
   `@HumanitariansAI`, not the hardcoded default), and BOUT's `OutroCTA`
   (confirmed `@HumanitariansAI`, no Claude mascot) all render legibly
   with no overlap, no clipping, no contrast issues. No defects found.
7. Audio presence: independently verified with `ffprobe` (aac stream,
   48000 Hz present) and `ffmpeg -af volumedetect` on the final master ->
   mean_volume **-24.1 dB**, max -2.8 dB. Master mtime (1788364272) is
   newer than beat_sheet.json mtime (1788364147).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), first pass
- Gate V: PASS, first pass — no defects found
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: duration 112.5s; mp4 mtime newer than beat_sheet.json mtime

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
`knowledge-work-plugins--claude-liam-analyze.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors**, plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
