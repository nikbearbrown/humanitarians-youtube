# BUILD-LOG — knowledge-work-plugins--claude-liam-month-end-prep

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-month-end-prep/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, `source_skill` pointing at the month-end-prep small-business
skill on Bear's machine, unreachable from this one). 7 beats: B00 cold open
(ClaudeComposerAsk), B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF handoff, BOUT outro — all already REMOTION, so NO-GENAI/
NO-PANTRY LAW required no substitution beyond the WRITER LAW swap at B00.

**Known source defect, logged rather than papered over:** the source
sheet's per-skill description field was never filled in for month-end-prep
specifically — B03's narration literally reads `"Claude's job: >."` and
BHTF's reads `"I want to >."`, unfilled template placeholders. Checked
four sibling reels from the same batch (`close-management`,
`journal-entry-prep`, `journal-entry` all got their descriptions filled;
only `month-end-prep` and `month-heads-up` show this gap, and
`month-heads-up`'s did get filled — so the gap is specific to this one
skill's batch run). Rather than invent business-specific close-checklist
content the source never stated, this redo carries forward only the facts
the source *does* state about the mechanism — a Skill is a folder with a
SKILL.md Claude reads before it acts, the Steps section executes linearly,
and running it is deterministic (same file, same steps, every run) but
bounded (nothing beyond what the file says). QUESTION.md and CARRY-OUT.md
both log this decision explicitly.

Facts carried over unchanged from the source's B01/B02/BVDT: a Skill is a
folder Claude reads before it works; month-end-prep's folder holds a
SKILL.md (full instruction set, plain language) plus a reference folder —
"the file is the program"; the pipeline lives in the Steps section, read
and executed in order, linear, no branching unless a step says so; same
input, same output, every run; the boundary is exactly what the file says.

Given this reel's beat count (7, matching the source exactly per the
redo-mode "keep beat count" rule), the body beats compress the source's
three Teardown beats (B01 anatomy, B02 pipeline, B03 design tell) into
three GRAPHIC beats (B01, B02, B03) built fresh in Manim, following
hai-simple's Plain-register spine (stakes/wrong-guess → mechanism/anchor
planted → anchor payoff/both directions) instead of the source's anatomy/
pipeline/tell structure. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` (WRITER LAW: "learn" → "read" —
the newcomer's assumption that Claude *learns* a skill like month-end-prep
through repeated use, corrected to the fact that it reads the same file
fresh every run, no training step). Register re-registered Teardown →
Plain: the source's B03 framed the facts as "what it gets right" / "where
it bites" — Teardown trade-off language — restated here as a determinism-
and-boundary fact with no verdict on the skill's design quality. Source's
BVDT verdict recap folded into a dedicated BCRY carry-out beat per
CARRY-OUT LAW. Close re-skinned to `OutroCTA` / @HumanitariansAI. Anchor:
B01 → B03, the month-end-prep folder (SKILL.md + reference), run
identically in January and June, producing identical checklists both
times — with a "fills the gap itself" bubble struck through to state the
negative direction (nothing invented beyond the file).

Built end to end this invocation:

1. GATE T (`type_check.py`) — PASS before any audio/render spend (0 FAILs,
   all 7 beats §8.10 SKIP).
2. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, $0.00. Durations:
   B00 10.07s, B01 17.60s, B02 14.95s, B03 18.45s, BCRY 8.15s, BHTF 16.34s,
   BOUT 3.09s.
3. Wrote `scenes.py` (3 Manim scenes, B01–B03, reel-unique names
   `MEPB01Scene`/`MEPB02Scene`/`MEPB03Scene`) and `render_scenes.py`;
   rendered all three in the foreground — no failures on first pass.
4. `remotion_scenes.py` (4 REMOTION beats) exceeded the tool's 120s
   foreground window on the first attempt; B00 finished rendering but the
   post-render `extend_clip_to_duration` ffmpeg pass was killed mid-write,
   leaving `media/B00.mp4` at its raw 20.24s render length (with a
   truncated 1.57s `_ext_B00.mp4` stray temp file) instead of trimmed to
   the 10.07s audio window. Re-ran `remotion_scenes.py` in the foreground
   with a longer timeout per the one-shot COMPLETION LAW (never end a turn
   on a render step); it correctly skipped the already-filled B00 and
   rendered BCRY/BHTF/BOUT clean, all `ok`, exit 0.
5. **Caught and fixed directly, not assumed:** verified B00's actual
   content before treating the "filled already" skip as safe. Frame pulls
   at t=1.0–3.0s confirmed "learn" appears in terracotta accent (about to
   be deleted) and is replaced by "read" by t≈2.5s; frame pulls at t=4.0s
   and t=9.5s confirmed the full corrected question ("How does Claude read
   a skill like month-end-prep?") is settled and legible well before the
   10.07s audio mark, cursor resting at the end (WRITER LAW "end ON the
   question"). Since the correction and full question complete by ~9.5s,
   trimming the raw 20.24s render to exactly 10.07s (the same
   tpad+trim ffmpeg command `extend_clip_to_duration` uses) was safe and
   was applied manually; re-verified media/B00.mp4 at 10.1s, well above
   the ≥8s TIMING LAW floor.
6. Stamped B00's `build` record to VIDEO and B01–B03 to MANIM in
   beat_sheet.json (compile.py recomputes these from file state on compile
   regardless, but kept the sheet consistent before compiling).

Compiled directly (`compile.py`, no `--force`, first compile):
`knowledge-work-plugins--claude-liam-month-end-prep.mp4`, 7/7 real (no
slate), 89.7s, 3840×2160 (THE 4K LAW — clean master forced to 4K
automatically).

**Gate V (visual):** pulled 15 frames at 6s intervals across the full
89.7s runtime plus targeted early-frame pulls on B00 (t=1.0–4.0s, t=9.5s)
to verify the correction. Read directly, no defects: B00's naive question
and its "learn"→"read" correction read cleanly, ending on the complete
corrected question with the cursor resting. B01's THE ANCHOR (the
month-end-prep folder opening to SKILL.md, accented, plus reference/)
reads cleanly. B02's steps-in-order diagram with JAN/JUN both pointing at
the identical step list reads cleanly. B03's THE ANCHOR RETURNS (same
folder, JAN/JUN producing identical checklists, "fills the gap itself"
struck through) reads cleanly. BCRY's carry-out card, BHTF's Your Turn
composer card (the real "walk me through each step, point to the line"
prompt, with the watch-for), and BOUT's outro/subscribe card all render
legibly with safe inset respected. **Noted, not a defect introduced here:**
`OutroCTA` renders on a flat-white ground rather than the humanitarians
cream (`#F3EBDD`) — same shared-component behavior already logged
unremarked in sibling hai-simple reels (e.g. `redshift-api`,
`email-sequence`); out of this reel's scope to fix.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe (independently re-verified, not just trusted from compile.py
  output): video 3840x2160 h264, audio aac present; duration 89.66s; mp4
  mtime (1788522457) newer than beat_sheet.json mtime (1788522371)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

Metadata file written: `knowledge-work-plugins--claude-liam-month-end-prep.md`
(channel @HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins
& Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's family `knowledge-work-plugins` is an exact key match in the
map) — plus the direct code link per the DELIVERY CONTRACT format.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
