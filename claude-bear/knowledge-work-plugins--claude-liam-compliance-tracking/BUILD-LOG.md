# BUILD-LOG — knowledge-work-plugins--claude-liam-compliance-tracking

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-compliance-tracking/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `compliance-tracking`
Skill, already fully built — no SCRIPT.md on the source; source_skill path
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/operations/skills/compliance-tracking/SKILL.md`
not present on this machine, same situation as the `audit-support`/
`command-development` siblings — the source's own `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: the skill's
job ("track compliance requirements and audit readiness"), its six trigger
phrases ("compliance", "audit prep", "SOC 2", "ISO 27001", "GDPR",
"regulatory requirement"), the skill-as-folder anatomy (one file, SKILL.md,
plain language, no hidden logic), the linear read→execute→return pipeline
(no branching unless a step says so), and the verdict facts (same input →
same output every run; limited to only what the file specifies). B00
replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "certify" → "track" — the newcomer's
wrong guess that asking Claude about compliance means Claude renders a
compliance judgment from its own knowledge, corrected toward the actual
mechanism: it tracks requirements and preps the audit trail from a written
file). Register re-registered Teardown → Plain: source B03's "gets it
right / where it bites" framing and BVDT's verdict facts were merged into a
single plain mechanism-and-boundary statement (NB03) plus the BCRY
carry-out sentence, per CARRY-OUT LAW — no design judgment retained. Close
re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design-tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each — both stayed close to the source's own generic
"skill = folder" / "linear pipeline" narration, since (unlike the
`command-development` sibling, whose source Skill had concrete
locations/fields/argument-syntax detail to specialize into NB01/NB02) this
source's B02 never named compliance-tracking-specific pipeline sub-steps,
so none were invented — the compliance-tracking-specific facts (job,
triggers, verdict) were placed entirely in NB03 instead; B03+BVDT compressed
into NB03 + BCRY; BHTF kept, with the source's paste-ready prompt text
completed from the full, untruncated trigger list found in the source's own
B00 narration (the locked sheet's JSON truncated the BHTF prompt
mid-sentence — `"trigger with \"compliance\", \"a."` — a data defect in the
source file itself, not a content decision, fixed by using facts already
present elsewhere in the same source sheet rather than inventing new ones)
and reworded into a concrete, paste-ready prompt a viewer can run today
(mirroring the `audit-support` sibling's equivalent "enumerate before
opining" substitution); BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly. Full audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`knowledge-work-plugins--claude-liam-audit-support` sibling, adapted with
compliance-tracking-specific labels.

**One GATE T defect caught and fixed on first pass.** NB03's original chip
labels ("tracks requirements" 19 chars, "preps for audit" 15 chars, "only
what's written" 19 chars) landed in the fs=22 font tier per `scenes.py`'s
`_chip()` sizing rule (fs=26 at ≤14 chars, fs=22 at ≤22 chars, else 18), but
the longest labels' post-layout aspect scale-down pushed the smallest text
run to 18px, under the 20px (1.9%-of-1080-logical) floor —
`type_check.py`'s first pass: **FAIL, 1 defect (NB03 min-size §8.1)**.
Fixed by shortening all three chips into the safe ≤14-char / fs=26 tier
("requirements" 12, "audit prep" 10, "written page" 12 — "written page"
paired with the beat's existing caption "reach stops at the page" to keep
the same meaning without the redundant longer phrase), matching NB01/NB02's
already-passing chip lengths. Edited directly in `scenes.py` and
`build_beat_sheet.py` (for future regeneration parity) plus the
already-generated `beat_sheet.json`'s NB03 `chips` field (not a full
`build_beat_sheet.py` re-run, which would have discarded the measured audio
durations); `manim/NB03.mp4` deleted and re-rendered individually via
`render_scenes.py` (which skips beats whose output already exists) before
recompiling. Second `type_check.py` pass: **PASS, 0 FAILs**.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00, B00 measured 11.78s narration); B00/BCRY/BHTF/BOUT
rendered via `remotion_scenes.py` (foreground call exceeded the tool's 120s
timeout and was moved to background by the harness automatically — blocked
on it via `TaskOutput` before proceeding, per the COMPLETION LAW's
foreground-render rule; same for the recompile after the NB03 fix); NB01–
NB03 rendered via `render_scenes.py` (stayed under the foreground timeout
both passes).

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-compliance-tracking.mp4`,
7/7 beats filled real (no slate), 92.1s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see NB03 chip-label defect + fix above)
- GATE AUDIO (compile.py): PASS — mean_volume **-24.1 dB**
- Independent ffprobe/ffmpeg re-verification: video 3840×2160 h264, audio
  (aac) present, duration 92.125s; volumedetect mean_volume -24.1 dB, max
  -3.0 dB (audible, well above the -40 dB floor); mp4 mtime (1788416480)
  newer than beat_sheet.json mtime (1788416391)
- Gate V (visual): pulled frames across the full runtime (t=0/1.0/1.3/1.6/
  1.9/2.2/2.5/2.8/3/6/8/9/10.5/11.5s targeted on B00, ~10-15s spacing
  elsewhere) plus targeted checks of B00 (the "certify" doomed word visible
  in terracotta at t≈1.6-2.2s, correction settles to "Does Claude track a
  company's SOC 2 compliance?" fully legible by t≈8s of the 11.8s clip —
  well inside the clip, satisfying TIMING LAW), NB01–NB03 (all chips
  legible post-fix, arrows/accent/caption correct, no space-collapse or
  truncation), BCRY (carry-out sentence + sparkline "Tracks. Never
  certifies." read clean), BHTF (correct topic "COMPLIANCE-TRACKING ·
  ANTHROPIC SKILL", correct title restate, @HumanitariansAI handle, prompt
  text legible), and BOUT (OutroSeries: correct eyebrow
  "COMPLIANCE-TRACKING · @HumanitariansAI", correct title restate, crimson
  underline, no truncation). No blockers (noted, not a new defect:
  OutroSeries renders on flat white rather than the true humanitarians
  cream/terracotta palette, same componentry gap already logged unremarked
  on multiple `knowledge-work-plugins` siblings — the component exposes
  only `eyebrow`/`line` props, no palette prop).
- B00 TIMING LAW: `actual_duration_s` 11.78s narration + 1.0s lead_silence =
  12.78s total window (≥9s requirement comfortably met); rendered clip
  extended to 11.8s by remotion_scenes.py; the "certify" → "track"
  correction lands on screen by t≈2.2s and the full corrected question
  stays legible through the end of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-compliance-tracking.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `"knowledge-work-plugins"`
prefix directly, consistent with every other `knowledge-work-plugins`
sibling built to date (e.g. `claude-liam-audit-support`). Direct code link
per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
