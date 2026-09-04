# BUILD-LOG — knowledge-work-plugins--claude-liam-compose-outreach

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/knowledge-work-plugins/youtube/claude-liam-compose-outreach/beat_sheet.json`,
7 beats, teardown of Anthropic's `compose-outreach` skill — a partner-built
knowledge-work plugin built with Common Room, brand `claude-liam`). Read the
source sheet in full (no SCRIPT.md existed for the source; the source's
`beat_sheet.json` narration and its LENS-AUDIT.md/PEDAGOGY.md were the only
artifacts). Kept the question and every fact: `compose-outreach` is a skill
(a folder Claude reads before it acts, containing `SKILL.md` and a
`references` folder — 2 files total); its named job is "generate
personalized outreach messages using Common Room signals"; its named
triggers are exactly the four phrases from the source ("draft outreach to
[person]," "write an email to [name]," "compose a message for [contact],"
or any outreach-drafting request); its pipeline is linear (read → execute →
return, no branching); and its verdict facts (same input → same output,
every run; limit: only what the file says) survive as the wrong-guess/
break-it pair (S02/S03) rather than a Teardown verdict card. Re-registered
narration from Teardown to Plain (facts unchanged, no design verdict — cut
the source's "what it gets right / what it bites" trade-off framing) and
carried the Humanitarians AI skin (Liam `am_onyx`, `OutroSeries`/`OutroCTA`).
Restructured the source's flat 7-beat anatomy/pipeline/design-tell/verdict
shape onto the full hai-simple 6-move spine (stakes, wrong guess, mechanism,
anchor, both directions, carry-out) — following the established convention
from the prior `knowledge-work-plugins--claude-liam-code-review` redo in
this same loop directory, expanding to 16 beats. No source beat was
AI-video, pantry, or human-drop — the source was already Remotion end to
end (`ClaudeComposerAsk`, `SkillTeardownAnatomy/Pipeline/Mechanism`,
`ClaudeVerdictArtifact`), so every body beat carried over as Remotion with
no NO-GENAI/NO-PANTRY substitution needed.

Built the wrong-guess/anchor material myself since the source's teardown
narration was generic boilerplate shared across the whole skill-teardown
batch (same "Teardown moment... what it gets right / what it bites" frame
appears verbatim-shaped across many sibling reels) and did not itself
contain a wrong-guess or anchor structure. The wrong guess ("Claude
free-styles the personal touch") and its break ("ask it twice — same named
source, not a mood") are grounded directly in the source's own stated fact
"same input, same output, every run." The anchor (a contact's title change)
is an illustrative, clearly-marked hypothetical ("Say a contact's title
changed...") in the same register as the code-review redo's N+1-loop
illustration — not asserted as a literal detail from SKILL.md. `one_flag:
"none"` in the metadata reflects that every claim traces to the source
description or is a marked hypothetical, matching the code-review
precedent's own audit.

1. **GATE T (type_check.py), first pass: FAIL** — 1 `no-wordy-card §8.5`
   violation (S07 `body` prop at 13 words, over the 12-word pull-quote
   limit). Fixed by shortening `body` to "Personalize using Common Room
   signals — not a hunch." (narration_text left untouched — only the
   on-screen card text changed). Re-ran: **GATE T: PASS**, 0 FAILs.
2. Generated Kokoro audio for all 16 beats (`generate_audio_kokoro.py`,
   voice `am_onyx`, no `--voice` flag — voice comes from the per-beat field
   already set) — measured durations written back into `actual_duration_s`.
   B00 measured 11.73s, comfortably inside the WRITER LAW's required ≥9s
   window (narration + 0.8s lead silence).
3. Rendered all 16 Remotion beats via `remotion_scenes.py` in the
   foreground. The tool call exceeded the 120s inline timeout and the
   harness moved it to background; per this skill's ONE-SHOT warning,
   blocked on it with `TaskOutput` (block=true) rather than ending the turn
   — confirmed via an interim `ls media/` check that files were landing
   steadily (10/16 present partway through) before it returned exit 0 with
   all 16 beats `ok`.
4. `compile.py` — 16/16 slots filled (all VIDEO), content-check/frame-check/
   lane-check all PASS. THE 4K LAW forced the clean master natively to
   3840x2160 (no `--review` flag used). Also ran in the background past the
   120s inline timeout; blocked on it with `TaskOutput` the same way until
   exit 0.
5. Independently reverified rather than trusting compile.py's own report:
   `ffprobe` — 3840x2160, 24fps h264, 131.21s, mono AAC audio track present;
   master mtime (02:45:29) newer than beat_sheet.json mtime (02:43:25);
   `ffmpeg -af volumedetect` — mean_volume **-23.9 dB**, max -2.9 dB,
   independently confirming GATE AUDIO well above the -40 dB floor.
6. Gate V: pulled frames at 6s spacing across the 131s runtime plus two
   extra pulls inside B00 (9.5s, 11.0s) to verify the WRITER LAW correction
   specifically, and two near the tail to check the outro. Read all of
   them: B00's correction lands cleanly by t=11s ("It fetches the personal
   touch, right?" — "invents" struck and replaced by "fetches", well inside
   the beat's 11.7s measured duration); the wrong-guess/break-it pair (S02
   "Free-styled?" / S03 verdict "SAME SOURCE, NOT A MOOD"); the SKILL.md
   anatomy card (S04, SKILL.md + references, 2 files); the named-source
   mechanism card (S07, "One named source" / "Personalize using Common Room
   signals — not a hunch."); the both-directions pair (S10 "REAL SIGNAL" /
   S11 implied "NOT A FAILURE"); the Your Turn composer card (BHTF); and
   both outro beats (BOUT1 title card with Humanitarians AI · Claude Basics
   eyebrow, BOUT2 CTA "More Claude Basics from Humanitarians AI." with
   subscribe pill and handle). All legible, safe inset respected, no text
   overlap. No defects found — no fixes needed this pass.

**Gates:**
- content-check: PASS (16 beats, no violations)
- frame-check: PASS (3840x2160, 16 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after de-wordifying 1 body prop)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: duration 131.21s, 3840x2160; mp4 mtime newer than beat_sheet.json mtime

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
`knowledge-work-plugins--claude-liam-compose-outreach.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
family `knowledge-work-plugins` matches the map's `knowledge-work-plugins`
prefix directly — plus the direct code link per the DELIVERY CONTRACT
format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
