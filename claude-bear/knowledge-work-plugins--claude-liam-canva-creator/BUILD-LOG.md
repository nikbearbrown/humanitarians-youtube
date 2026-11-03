# BUILD-LOG — knowledge-work-plugins--claude-liam-canva-creator

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/knowledge-work-plugins/youtube/claude-liam-canva-creator/
beat_sheet.json`, 7 beats, `small-business/skills/canva-creator/SKILL.md`,
brand `claude-liam`, `@NikBearBrown`). SUBJECT.json's `source_sheet`/
`source_dir` pointed at that local path, which does exist — but only as the
built output. Read it in full.

**Source defect found and logged (not silently patched):** the source's own
narration and Remotion props carry unresolved template placeholders —
literal `>` characters — at exactly the three places where the specific
canva-creator constraint should read (B00's `output`, B03's `body`, BHTF's
`command`). The `small-business/skills/canva-creator/SKILL.md` this reel
was originally built from lives on Bear's machine
(`/Users/bear/Documents/CoWork/bear-textbooks/...`) and is not present in
this checkout — only `anthropics/knowledge-work-plugins/youtube/` (built
output) exists locally, confirmed via `find` for the `skills/` tree.
Searched `_audit/rows_0.csv`, `_audit/REBUILD-WORKLIST.csv`, `_audit/
sheets.txt`, `SKILL-EXPLAINERS-BATCH-LOG.md`, and `BUILD-SKILL-EXPLAINERS-
LOG.md` for a recoverable copy of the real constraint text — the audit
files independently confirm the defect (`_audit/rows_0.csv` flags this
exact sheet `T:no-FACTCHECK`) but none carries the missing text.

**The call made (logged in full in QUESTION.md/CARRY-OUT.md):** rather than
block on an unrecoverable source, or invent a specific claim about Canva's
UI, the three `>` placeholders are filled with a generic, low-risk
description consistent with the skill's own name and its `small-business`
category — a "creator" skill for a design tool fills in an existing
template (text, colors, logo) rather than laying out a new design from a
blank page. This is stated throughout as "the constraint this SKILL.md
sets," never as a verified claim about Canva's product surface, per PHASE
1's "when in doubt, describe behavior generically" and the honesty rule
against inventing UI.

Kept beat count (7) and every fact that IS verifiable and generic: a
Claude Skill is a folder read before Claude acts; `SKILL.md` is the full
instruction set in plain language; Claude executes the file's steps in
order, linearly; the same written steps produce the same output every run;
the skill's job is bounded exactly by what the file specifies. Remapped
the source's B03/BVDT Teardown "what it gets right / what it bites" framing
into a both-directions mechanism statement (B03) and a single carry-out
sentence (BCRY) — same underlying facts, no verdict on the design.
Constructed an anchor pair (B01 → B03, the template card) that the source
did not explicitly signpost, to satisfy hai-simple's inherited ANCHOR LAW:
planted with the template card locking into frame beside the "match the
template" callout, paid off with the same card filling correctly and then
failing to match a mismatched request.

B00 WRITER LAW: naive guess "scratch" → corrected to "a template" (the
newcomer's default read of a "Canva Creator" skill is that it designs
freely; the file instead names a fixed template to fill). 29-word narration
+ `lead_silence_s: 0.8`; measured 9.81s (clears the TIMING LAW ≥9s window
narrowly). Verified on a frame pull mid-typing that the writer's text reads
"Claude, Canva Creator — it designs from a template, righ|" — correction to
"a template" confirmed visible on screen before the beat ends.

Build sequence, all foreground, waited on exit code before proceeding:

1. `generate_audio_kokoro.py` — 7/7 beats, cost $0.00, durations written
   back as ground truth (B00 9.81s, B01 16.43s, B02 13.5s, B03 16.6s, BCRY
   7.85s, BHTF 17.47s, BOUT 3.29s).
2. `remotion_scenes.py` — B00 (BrutalistHesitantWriter), BCRY (WantQuote),
   BHTF (ClaudeComposerAsk), BOUT (OutroCTA) — all `ok`, exit 0. (Ran long
   enough to auto-background under the tool's 120s timeout; polled its
   output file directly in the foreground rather than ending the turn, per
   the one-shot-invocation rule — never treated the background move as a
   reason to stop and wait for a later notification.)
3. Wrote `scenes.py` (CNVB01Scene/CNVB02Scene/CNVB03Scene, humanitarians
   palette) and `render_scenes.py` for the 3 GRAPHIC beats, modeled on the
   sibling `claude-code--claude-liam-plugin-structure` reel's pattern.
   `render_scenes.py` — 3/3 rendered clean, exit 0.
4. `compile.py` — 7/7 slots filled, content-check/frame-check/lane-check
   PASS, THE 4K LAW forced 3840×2160, GATE AUDIO PASS mean_volume -24.2 dB.
5. `type_check.py` (GATE T) — **first pass FAILED**: B03 min-size §8.1, a
   16px slot-label text run below the 20px floor. Fixed by bumping the
   `text`/`colors`/`logo` slot-label `font_size` from 16→22 and the
   "a different shape" request-card label from 20→22 in `scenes.py`;
   re-rendered only B03 via `render_scenes.py` (B01/B02 skipped, already
   present); recompiled (`compile.py` re-ran B03 only, other 6 beats
   untouched). Re-ran `type_check.py` — **PASS, 0 FAILs**, all 7 beats
   §8.10 SKIP.
6. Independently reverified with ffprobe/ffmpeg rather than trusting
   compile.py's own report: master mtime (1788397018) newer than
   beat_sheet.json mtime (1788396705); h264 3840×2160 + aac streams
   present, duration 85.96s; `ffmpeg -af volumedetect` mean_volume
   **-24.2 dB**, max -2.8 dB — independently confirms GATE AUDIO.
7. Gate V: pulled frames at 6s spacing across the full runtime plus one
   extra pull at 84s to catch the outro (the 6s grid landed its last frame
   inside BHTF), and read all of them directly — B00's writer-open
   correction, B01's folder/SKILL.md/anchor-planted template card, B02's
   numbered-step pipeline with the three input cards, B03's anchor payoff
   (template filling correctly, then a mismatched request finding no slot),
   BCRY's carry-out quote card, BHTF's Your Turn composer card with the
   full paste-ready prompt, and BOUT's outro/subscribe card all read
   legibly, safe inset respected, no text overlap. No defects found this
   pass (the one B03 min-size defect was caught by Gate T in step 5 and
   fixed before this frame pull).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after one fix — see step 5)
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: duration 85.96s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking note (compile.py):** motion histogram remotion:4 graphic:3 —
structural, matches hai-simple's mandated shape (B00 writer + BCRY + BHTF
Your Turn + BOUT outro all REMOTION by skill contract, 3 GRAPHIC body
beats). Manim clips were time-stretched by compile.py to fill their
measured audio durations (B01 9.2s→16.4s at 1.78x, B02 11.1s→13.5s at
1.22x, B03 10.9s→16.6s at 1.52x); spot-checked in the Gate V frame pull, no
visible artifacting (static-camera Manim compositions).

Metadata file written: `knowledge-work-plugins--claude-liam-canva-creator.md`
(channel @HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's family `knowledge-work-plugins` matches the map's
`knowledge-work-plugins` prefix directly — plus the direct code link per
the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.
