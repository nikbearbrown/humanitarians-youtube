# BUILD-LOG — knowledge-work-plugins--claude-liam-brand-voice-enforcement

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-brand-voice-enforcement/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `brand-voice-enforcement`
Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup (a prior filmloop worker log at
`skills/make/hai-simple/loop/.filmloop/knowledge-work-plugins--claude-liam-
brand-voice-enforcement.w44071.out` was checked and was empty — no partial
artifacts to reuse).

**Source-material gap, handled honestly:** the source reel's own narration
carries unfilled `>` placeholders in four beats (B00, B03, BVDT, BHTF) where
the specific brand-voice rules the Skill checks were never written into the
original build. The source's `metadata.source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-
work-plugins/partner-built/brand-voice/skills/brand-voice-enforcement/
SKILL.md`) points at a machine this build has no access to, and a workspace-
wide search confirmed no copy of that Skill's actual SKILL.md exists
anywhere under `books/`. Per the redo contract's "facts must be true and
current... when in doubt, describe behavior generically," those `>` gaps
were filled with the generic, load-bearing mechanism the source's own
B01/B02 already commit to confidently (a skill is a folder with a SKILL.md
Claude reads before acting; steps run linearly; the check compares a draft
against whatever the file lists) rather than invented specifics about any
particular brand's rules. No claim is made about brand-voice-enforcement's
actual rule list anywhere in this reel — see the .md's "Deliberately not
claimed" section and SCRIPT.md's source-material note.

Question, facts, and body argument carried over: a skill is a folder Claude
reads before it works; the SKILL.md holds the full instruction set in plain
language with no hidden logic; the Steps section runs linearly, no
branching unless a step says otherwise; the check compares a draft against
whatever rules the file lists and flags mismatches; same input produces
same output every run; the limit is exactly what the file says. B00
replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "know" → "check" — the newcomer's
wrong guess that Claude already knows a brand's voice from training,
corrected toward the actual mechanism: it checks a draft against an
explicit written spec). Register re-registered Teardown→Plain: the source's
B03 "gets it right / where it bites" framing (repeatable results / anything
outside the spec) was redistributed as a plain mechanism description across
NB03 (what the check catches) and BCRY (the limit), per the NO JUDGMENT
register check. BVDT's verdict facts were merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03 compressed into NB03; BVDT folded into BCRY;
BHTF kept — but since the source's own your-turn prompt was itself an
unfilled `>` placeholder ("I want to >. Read the brand-voice-enforcement
skill..."), rather than inventing a call to a specific Anthropic skill a
general viewer likely doesn't have installed, this redo writes a concrete,
paste-ready prompt that exercises the identical mechanism (an explicit,
closed rule list; check only what's listed) using materials any viewer
already has; BOUT kept. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with brand-voice-enforcement-specific labels.

**B00 TIMING LAW:** text kept short (3 lines, 33 characters — "Does
Claude\nalready know\nmy brand's voice?") at a moderate charMs (42) from the
start, applying the fix pattern already documented on the agent-development
sibling proactively rather than discovering a timing failure by a failed
first render. Kokoro narration measured 8.73s; `lead_silence_s: 1.0` is set
in the beat sheet as the documented design target but confirmed NOT
mechanically applied anywhere in this toolkit version (`remotion_scenes.py`
extends strictly to `actual_duration_s`; only `repair_b00_audio.py`, an
unrelated Seedance-repair script, reads `lead_silence_s` at all) — so it is
inert metadata here, same as on the sibling. The rendered clip is 8.7s,
clearing the WRITER LAW's stated `media/B00.mp4 >= 8s` verification floor.
Frame-pulled at t=1.3s/1.6s: "know" sits doomed in terracotta; by t=3.0s it
has corrected to "check"; the full corrected question "Does Claude already
check my brand's voice?" is settled and legible and holds through the end
of the 8.7s clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, one pass, no retries needed); NB01–NB03 rendered via
`render_scenes.py` (Manim, all 3 succeeded first pass); B00/BCRY/BHTF/BOUT
rendered via `remotion_scenes.py` (the full-sheet run exceeded the tool's
120s default timeout and was moved to background by the harness
automatically — blocked on it via `TaskOutput` before proceeding, per the
COMPLETION LAW's foreground-render rule; all 4 beats reported `ok`).
`type_check.py` ran clean: **GATE T: PASS, 0 FAILs** on the first pass, no
defects to fix.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-brand-voice-enforcement.mp4`,
7/7 beats filled real (no slate), 78.9s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO (compile.py): PASS — mean_volume **-24.1 dB** (ffmpeg
  volumedetect), max -2.7 dB
- Independent ffprobe/ffmpeg re-verification (COMPLETION LAW): video
  3840×2160 h264, audio aac present, duration 78.94s; mp4 mtime
  (1788369716) newer than beat_sheet.json mtime (1788369609); mean_volume
  -24.1 dB, well above the -40 dB floor
- Gate V (visual): pulled frames every 5s across the full 78.9s runtime
  plus targeted frame pulls at t=1.0/1.3/1.6/1.9/2.2/2.5/3.0/8.0s for B00
  (confirmed "know" doomed in terracotta at 1.3-1.6s, corrected to "check"
  by 3.0s, final question settled and held to the 8.7s end). NB01-NB03
  chips all legible and parallel-sized, one accent per beat. BCRY (quote +
  sparkline "Check the file. Not the vibe." read clean). BHTF (correct
  topic/title/@HumanitariansAI handle, paste-ready prompt text legible).
  BOUT (OutroSeries: correct eyebrow "BRAND VOICE ENFORCEMENT ·
  @HumanitariansAI", correct title restate, crimson underline, no
  overlap/truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 8.73s narration (rendered clip 8.7s,
  clears the >=8s requirement); the "know" -> "check" correction lands on
  screen by t~=3.0s and the full corrected question stays legible for the
  remainder of the clip.

Metadata file written:
`knowledge-work-plugins--claude-liam-brand-voice-enforcement.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key match in the map, resolving
directly to "Extending Claude — Skills, Plugins & Connectors" (no fallback
needed). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
