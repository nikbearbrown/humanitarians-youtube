# BUILD-LOG — knowledge-work-plugins--claude-liam-documentation

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a 7-beat Teardown "skill-teardown" sheet
(`anthropics/knowledge-work-plugins/youtube/claude-liam-documentation/beat_sheet.json`,
teardown of Anthropic's `documentation` skill, brand `claude-liam`,
all-Remotion source: `ClaudeComposerAsk` + `SkillTeardownAnatomy` +
`SkillTeardownPipeline` + `SkillTeardownMechanism` + `ClaudeVerdictArtifact`).
Read the source sheet in full. Its `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/engineering/skills/documentation/SKILL.md`)
is unreachable on this machine (points at Bear's other machine, and no local
copy exists anywhere under `books/`); every fact used here is what the
source beat_sheet's own `narration_text` already stated verbatim: the skill
is `documentation` ("write and maintain technical documentation"), its
trigger phrases ("write docs for", "document this", "create a README",
"write a runbook", "onboarding guide," or any technical-writing request), a
skill is a folder Claude reads before it acts containing one file
(`SKILL.md`), the pipeline is linear (read → execute steps in order →
return, "no branching unless the step says so"), and the design tell:
documentation is "a specification written as an instruction set" — right
for repeatable results, biting on "anything outside the spec."

Followed the same-family `claude-liam-code-review` sibling as the exact
structural precedent (same 7-beat source shape, same redo pattern):
expanded the source's compressed 7 beats into the full 16-beat hai-simple
spine (stakes / wrong-guess+break-it / mechanism / anchor-planted+payoff /
both-directions / carry-out / your-turn / outro). The anchor is an
illustrative runbook request — "write a runbook for restarting the payment
service" — rendered via `BrutalistTerminalOpen` (command + a three-item
checklist: Prerequisites, Steps, Rollback) at S05, reused as the IDENTICAL
composition at S09 (same command string, same checklist array; only the
`topic` label changes, "HOLD ON TO THIS" → "SAME SHAPE AGAIN") per ANCHOR
LAW. Flagged in SCRIPT.md as illustrative: the runbook's three sections are
a generically-true example of runbook contents, not an invented
Claude-specific structure — the source never named specific document
sections, only that the file "recognizes" named shapes. `one_flag: none`
in metadata reflects that every other claim is stated fact from the
source's narration, not inference.

No source beat was AI-video, pantry, or human-drop — the source was
already all-Remotion end to end, so no NO-GENAI/NO-PANTRY LAW substitution
was needed beyond the required B00 → `BrutalistHesitantWriter` swap and the
outro → `OutroSeries`/`OutroCTA` HAI skin.

**B00 WRITER LAW** ("whatever" → "what the file says"): 29-word narration +
`lead_silence_s: 0.8`, measured 9.86s, clearing the ≥9s TIMING LAW window.
Frame-verified at t=8.5s: the deleted word "whatever" is gone and the
correction is mid-type ("Just write what the |"), landing well inside the
9.86s beat.

1. **GATE T (type_check.py), first pass:** one non-blocking §8.10 advisory
   — S06's narration recited its `Opus5ChecklistCard` items near-verbatim
   (score 1.00, "discuss it, don't read it"). Reworded S06 narration from
   listing all five shapes to discussing the count and mechanism ("The file
   doesn't cover just any writing — it names five specific shapes, each
   with its own trigger phrase"), leaving the card's item list untouched.
   Re-ran: **GATE T: PASS**, 0 FAILs, advisory cleared (0.00).
2. `generate_audio_kokoro.py` — 16/16 beats generated, Kokoro `am_onyx`,
   cost $0.00, durations written back as ground truth (9.86s–2.09s range).
3. Rendered all 16 Remotion beats via `remotion_scenes.py` in the
   foreground. Exceeded the tool's 120s interactive timeout and was moved
   to background by the harness; per this skill's ONE-SHOT warning, blocked
   on it with `TaskOutput(block=true)` (not fire-and-forget) rather than
   ending the turn, polling interim `media/` output to confirm real
   progress (8/16, then 15/16 files present) before it returned exit 0:
   all 16 beats `ok`, no failures.
4. `compile.py` — 16/16 slots filled (all VIDEO), content-check/frame-check/
   lane-check all PASS. THE 4K LAW forced the clean master natively from
   720p to 2160p (no `--review` flag used). Exceeded the tool's 120s
   timeout and was moved to background; blocked on it with
   `TaskOutput(block=true)` until exit 0 rather than ending the turn.
5. Independently reverified rather than trusting compile.py's own report:
   `ffprobe` — 3840x2160, 116.54s, h264+aac; master mtime newer than
   beat_sheet.json mtime; `ffmpeg -af volumedetect` — mean_volume
   **-23.9 dB**, max -3.0 dB, independently confirming GATE AUDIO well
   above the -40 dB floor.
6. Gate V: pulled 19 frames at 6s spacing across the full 116.5s runtime,
   plus targeted pulls at B00 (t=8.5s, correction mid-type), S05/S09
   (t=45s/t=68s/t=73s, confirming the anchor's identical
   `BrutalistTerminalOpen` composition — same command, same checklist), and
   both outro cards (t=112s/t=115s). Read all of them directly: the
   writer-open correction landing inside its window, the wrong-guess/
   break-it pair (S02/S03, verdict pill "SAME EVERY TIME"), the SKILL.md
   anatomy card (S04), the five-shape checklist (S06), the linear pipeline
   (S07/S08), the anchor plant and identical payoff (S05/S09), the
   both-directions pair (S10 "REAL SIGNAL" / S11 "NO GUARANTEE"), the
   carry-out quote (BCRY), the Your Turn composer card (BHTF), and the
   outro title + CTA cards (BOUT1/BOUT2) with the Humanitarians AI skin.
   All legible, safe inset respected, no text overlap. No defects found —
   no fixes needed this pass.

**Gates:**
- content-check: PASS (16 beats, no violations)
- frame-check: PASS (3840x2160, 16 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after rewording S06's §8.10 advisory)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: duration 116.54s, 3840x2160; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warnings (compile.py, both expected for this skill):**
- SKIN LINT flagged B00 (`BrutalistHesitantWriter` vs ai-explainer's
  `ClaudeComposerAsk`) and BOUT2 (`OutroCTA` vs `ClaudeTitleOutro`) as
  palette mismatches. Both are the hai-simple skill's deliberate
  COLD OPEN LAW / OUTRO LAW overrides, not defects.
- Motion histogram: remotion 16/16 (100%), over the generic ~40% pantry
  cap. Structural, not a defect: this redo's source was already all-Remotion
  and NO-GENAI/NO-PANTRY LAW requires every beat be Remotion or Graphic —
  there was no pantry/Manim material to substitute in without inventing
  content not in the source.

Metadata file written:
`knowledge-work-plugins--claude-liam-documentation.md` (channel
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
cp knowledge-work-plugins--claude-liam-documentation.mp4 \
   knowledge-work-plugins--claude-liam-documentation-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
