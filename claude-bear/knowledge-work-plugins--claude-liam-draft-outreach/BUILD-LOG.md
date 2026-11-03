# BUILD-LOG — knowledge-work-plugins--claude-liam-draft-outreach

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/knowledge-work-plugins/youtube/claude-liam-draft-outreach/beat_sheet.json`,
7 beats, teardown of Anthropic's `draft-outreach` skill — a partner-built
knowledge-work plugin, brand `claude-liam`). Read the source sheet in full
(no SCRIPT.md existed for the source; its `beat_sheet.json` narration plus
LENS-AUDIT.md/PEDAGOGY.md were the only artifacts, and the actual
`draft-outreach/SKILL.md` referenced by `source_skill` lives only on Bear's
machine, not in this tree — so every fact below traces to what the source
sheet's narration already asserts). Kept the question and every fact:
`draft-outreach` is a skill (a folder Claude reads before it acts,
containing a single `SKILL.md`, 9k — 1 file total, distinguishing it from
the sibling `compose-outreach` redo's 2-file/`references`-folder anatomy);
its named job is "Research a prospect then draft personalized outreach.
Uses web research by default, supercharged with enrichment and CRM"; its
named triggers are exactly the three phrases from the source ("draft
outreach to [person/company]," "write cold email to [prospect]," "reach
out to [name]" — three, not the sibling's four); its pipeline is linear
(read SKILL.md → execute → return output, no branching); and its verdict
facts (same input → same output, every run; limit: only what the file
says) survive as the wrong-guess/break-it pair (S02/S03) rather than a
Teardown verdict card. Re-registered narration from Teardown to Plain
(facts unchanged, no design verdict — cut the source's "what it gets
right / what it bites" trade-off framing) and carried the Humanitarians AI
skin (Liam `am_onyx`, `OutroSeries`/`OutroCTA`). Restructured the source's
flat 7-beat anatomy/pipeline/design-tell/verdict shape onto the full
hai-simple 6-move spine (stakes, wrong guess, mechanism, anchor, both
directions, carry-out), following the established convention from the
prior `knowledge-work-plugins--claude-liam-compose-outreach` redo in this
same loop directory, expanding to 17 beats (one more than that sibling's
16 — the extra beat, S08, carries a genuinely distinct fact this source
has and compose-outreach's didn't: the "supercharged with enrichment and
CRM" optional-layer detail). No source beat was AI-video, pantry, or
human-drop — the source was already Remotion end to end
(`ClaudeComposerAsk`, `SkillTeardownAnatomy/Pipeline/Mechanism`,
`ClaudeVerdictArtifact`), so every body beat carried over as Remotion with
no NO-GENAI/NO-PANTRY substitution needed.

Built the wrong-guess/anchor material myself since the source's teardown
narration was generic boilerplate shared across the whole skill-teardown
batch and did not itself contain a wrong-guess or anchor structure. The
wrong guess ("Claude already knows the company from training") and its
break ("ask about a prospect that just made news — recall can't reach it")
are grounded in one stable, current, generically-true fact about how
Claude works (a training knowledge cutoff means very recent events aren't
in memory) combined directly with the source's own stated fact ("Uses web
research by default"). The anchor (a prospect's funding round) is an
illustrative, clearly-marked hypothetical ("Say the prospect closed a
funding round last week…"), matching the sibling redo's own register.
`one_flag: "none"` in the metadata reflects that every claim traces to the
source description, a marked hypothetical, or the generically-true
training-cutoff fact — matching the sibling's own audit standard.

1. **GATE T (type_check.py): PASS, first pass** — 0 FAILs, 17 beats
   checked (most SKIP — no prose payload in the checked categories; S06's
   Opus5ChecklistCard scored 0.40 on its own internal metric with no FAIL
   raised). No content fixes needed.
2. Generated Kokoro audio for all 17 beats (`generate_audio_kokoro.py`,
   no `--voice` flag — the script does not accept one; voice comes from
   the per-beat field already set to `am_onyx`) — measured durations
   written back into `actual_duration_s`. B00 measured 10.75s, inside the
   WRITER LAW's required ≥9s window (narration + 0.8s lead silence).
3. Rendered all 17 Remotion beats via `remotion_scenes.py`. Each foreground
   invocation timed out at the tool's inline ceiling (120s, then 600s)
   before the full batch finished — per this skill's ONE-SHOT warning,
   never backgrounded it; instead re-invoked the same foreground command
   repeatedly, confirming via `ls media/` between runs that the script
   resumes by skipping already-rendered beats ("filled already (skip)")
   rather than re-rendering from scratch. Took 4 foreground passes (5
   beats, then 4 more, then 5 more, then the final 3) to reach 17/17.
4. **Defect found and fixed before compiling:** the first `compile.py` run
   failed — `media/B00.mp4` had `moov atom not found` (ffprobe confirmed
   truncated/invalid). Root cause: the very first foreground render pass
   was killed mid-write by the tool's own 120s timeout (exit 143) while
   B00 was still being finalized, leaving a corrupt file that the later
   "filled already (skip)" logic didn't catch (it checks presence, not
   validity). Fixed by re-rendering B00 specifically with
   `remotion_scenes.py --only B00 --force`, then independently verified
   every one of the 17 media files with `ffprobe -show_entries
   format=duration` before recompiling — all valid.
5. `compile.py` — 17/17 slots filled (all VIDEO), content-check/frame-check/
   lane-check all PASS. THE 4K LAW forced the clean master natively to
   3840x2160 (no `--review` flag used).
6. Independently reverified rather than trusting compile.py's own report:
   `ffprobe` — 3840x2160, 24fps h264, 131.74s, AAC audio track present;
   master mtime (1788478727) newer than beat_sheet.json mtime (1788478592);
   `ffmpeg -af volumedetect` — mean_volume **-23.9 dB**, max -3.0 dB,
   independently confirming GATE AUDIO well above the -40 dB floor.
7. Gate V: pulled frames at 8s spacing across the 131.7s runtime plus a
   dedicated pull at t=9.5s inside B00 to verify the WRITER LAW correction
   specifically. Read all of them: B00's correction lands cleanly by
   t=9.5s ("It already knows them, right?" — "knows" struck and replaced
   by "checks", well inside the beat's 10.77s measured duration, with a
   clear window before the beat ends); the anatomy card (S04, SKILL.md,
   1 file total — correctly distinct from the sibling's 2-file anatomy);
   the optional-layers card (S08, "Supercharged, not required" / "More
   sources, same habit."); the both-directions pair (S11 "REAL CHECK" /
   S12 "NOT A FAILURE"); the carry-out quote (BCRY); the Your Turn composer
   card (BHTF); and the outro (BOUT2, "More Claude Basics from
   Humanitarians AI." with subscribe pill and handle). All legible, safe
   inset respected, no text overlap. No defects found on this pass.

**Gates:**
- content-check: PASS (17 beats, no violations)
- frame-check: PASS (3840x2160, 17 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: duration 131.74s, 3840x2160; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warnings (compile.py, both expected for this skill):**
- SKIN LINT flagged B00 (`BrutalistHesitantWriter` vs ai-explainer's
  `ClaudeComposerAsk`) and BOUT2 (`OutroCTA` vs `ClaudeTitleOutro`) as
  palette mismatches. Both are the hai-simple skill's deliberate
  COLD OPEN LAW / OUTRO LAW overrides, not defects.
- Motion histogram: remotion 17/17 (100%), over the generic ~40% pantry
  cap. Structural, not a defect: this redo's source was already
  all-Remotion and NO-GENAI/NO-PANTRY LAW requires every beat be Remotion
  or Graphic — there was no pantry/Manim material to substitute in
  without inventing content not in the source.

Metadata file written:
`knowledge-work-plugins--claude-liam-draft-outreach.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
family `knowledge-work-plugins` matches the map's `knowledge-work-plugins`
prefix directly — plus the direct code link per the DELIVERY CONTRACT
format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-03 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects, then packaged
to both delivery targets.

```
cp knowledge-work-plugins--claude-liam-draft-outreach.mp4 \
   knowledge-work-plugins--claude-liam-draft-outreach-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
