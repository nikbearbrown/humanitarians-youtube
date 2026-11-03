# BUILD-LOG — cwc-workshops--claude-liam-submit-solution

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/claude-liam-submit-solution/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `submit-solution`
cwc-workshops Skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script, cross-checked
against the skill's own SKILL.md, present unchanged at
`/Users/nik/Documents/Cowork/anthropics/cwc-workshops/agent-decomposition/.claude/skills/submit-solution/SKILL.md`
even though the source reel's own `source_skill` metadata field points at
a Bear-machine path that does not exist here — same defect class as the
`cwc-workshops--claude-liam-forecasting` sibling, resolved the identical
way: the skill content itself is present, unchanged, at the
Cowork-mirrored path). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: submit-
solution guides a workshop attendee through five fixed steps — ask about
their experience (three questions: subagent approach for cycle three,
hardest part of the workshop, one thing they'd change), show the diff (an
empty diff means check whether they edited a different file, not that
they're done) and pull the eval score, commit and push to a
`solution/<name>` branch, open a PR, and confirm. The PR body template has
two sections — a decomposition/technical summary and a workshop-feedback
section — and the skill's own "Don't" list states the interview questions
are not optional color ("that's the point"). B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "git" → "feedback" — the newcomer's wrong guess that
submitting a solution is just a git task, corrected toward the actual
mechanism: it's an interview-then-git task, and the PR is the feedback
form). Register re-registered Teardown → Plain: the source's B03 design-
tell text ("What it gets right: repeatable results. What it bites:
anything outside the spec.") and BVDT's verdict ("Know the limit: only
what the file says.") were merged into a single NB03, keeping the one fact
a general audience needs and can act on — the PR body carries both the
code summary and the feedback, in the same document — and dropping the
"what it bites" framing, which is a design verdict rather than a mechanism
description and fails the NO JUDGMENT register check. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 design tell + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B03+BVDT compressed into NB03 (the one
fact a general viewer needs and can act on: the PR body's two sections);
BHTF kept as the your-turn handoff, rewritten as a fully self-contained
prompt — the source's version named "the submit-solution skill" and
quoted a task string truncated mid-word ("committing their starter-agent
decomposition a."), a generation defect carried over from the source; this
redo's prompt instead states the scenario directly (a finished coding
exercise, submit it as a PR) so it is runnable in any Claude conversation
today, no skill install required, while still testing the same reasoning
(questions before git; both halves in the PR body); BOUT kept. Full audit
in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`cwc-workshops--claude-liam-forecasting` sibling, adapted with
submit-solution-specific labels (chosen short — e.g. "ask"/"diff"/
"commit"/"PR"/"confirm"; "approach"/"hardest part"/"one change"/"git";
"code summary"/"feedback" — to stay clear of the GATE T min-size failure
class that sibling had already hit and fixed on longer bold chip labels).

**B00 TIMING LAW:** narration 28 words + `lead_silence_s` 0.8, audio
measured 9.79s (clears the ≥9s TIMING LAW floor; media/B00.mp4 rendered to
9.8s, past the ≥8s media-file floor). Frame-verified: "git" sits doomed in
terracotta mid-type, corrects to "feedback" by mid-clip, and the full
corrected question — "Claude, submit my solution — it's a feedback task,
right?" — is settled and legible for the remainder of the clip.

**Foreground-render discipline (COMPLETION LAW):** `remotion_scenes.py`
exceeded the Bash tool's 120s default foreground timeout and was moved to
background by the harness mid-run; rather than end the turn on that
signal, the invocation was tracked to completion via `TaskOutput` (blocking
wait) in the same turn before proceeding — exit code 0, all 4 REMOTION
beats (B00, BCRY, BHTF, BOUT) rendered clean on the first pass, no partial
or corrupt files to clean up.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); NB01–NB03 rendered via `render_scenes.py` (foreground, Manim);
B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground, tracked
to completion per above). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `cwc-workshops--claude-liam-submit-solution.mp4`, 7/7 beats filled
real (no slate), 112.4s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).
`type_check.py` (GATE T) passed clean on the first run — **PASS, 0
FAILs** — no chip-label fixes needed (short labels chosen up front, per
the forecasting sibling's known failure mode).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (first pass, no fixes required)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 112.4s; mp4
  mtime (1788242953) newer than beat_sheet.json mtime (1788242861)
- Gate V (visual): pulled frames every 8s across the full runtime plus
  targeted pulls for B00 mid-type (t≈4.5s, "git" doomed) and late (t≈8.5s,
  correction settled to "feedback"), and a dedicated BOUT pull (t=110s,
  past the last 8s-grid sample at 104s which still showed BHTF) — all 7
  beats legible, correctly inset, no text overlap, no truncation. NB01
  ("ask"/"diff"/"commit"/"PR"/"confirm"), NB02 ("approach"/"hardest
  part"/"one change"/"git"), NB03 ("code summary"/"feedback") all read
  clean with a single terracotta accent moment each. BHTF: correct
  topic/title/@HumanitariansAI handle, paste-ready prompt text legible.
  BOUT (OutroSeries): correct eyebrow "SUBMIT-SOLUTION · @HumanitariansAI",
  correct title restate "Feedback Before The Commit.", crimson underline,
  no truncation. No blockers.
- B00 TIMING LAW: `actual_duration_s` 9.79s / rendered clip 9.8s (both
  ≥ the ≥9s/≥8s floors); the "git" → "feedback" correction lands mid-clip
  and the full corrected question stays legible for the remainder.

Metadata file written: `cwc-workshops--claude-liam-submit-solution.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`cwc-workshops`) matches no
prefix in the map's family column; per the redo instruction to also check
the `hai-simple` skill-key prefix, `"hai-simple"` is itself a map key
resolving to `"Claude Basics"` — the same fallback documented in the
`cwc-workshops--claude-liam-forecasting` sibling, so this is a real,
more-specific-than-`_default` match, not the last-resort default. Direct
code link per DELIVERY CONTRACT format included. Chapters computed from
`actual_duration_s` cumulative offsets (B00 0:00, NB01 0:10, NB02 0:28,
NB03 0:54, BCRY 1:17, BHTF 1:29, BOUT 1:48).

**Status: review cut DONE.** Passed every Phase-3 gate.
