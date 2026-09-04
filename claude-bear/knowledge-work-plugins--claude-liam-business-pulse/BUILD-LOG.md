# BUILD-LOG — knowledge-work-plugins--claude-liam-business-pulse

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-business-pulse/beat_sheet.json`
(a Teardown skill-teardown walkthrough of a Claude Skill named
`business-pulse`, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely fresh
this invocation — only SUBJECT.json existed on pickup.

**Source data defect found and handled.** The source `beat_sheet.json`'s B03
and BVDT `narration_text` fields contain an unfilled batch-template
placeholder — a literal `>` where the skill's specific one-line task
description should have been (e.g. "Claude's job: >."). Confirmed this is a
data gap unique to this source file, not a deliberate omission or a
formatting convention: the sibling `claude-liam-forecast` source has the
equivalent line filled in full ("Generate a weighted sales forecast with
best/likely/worst scenarios..."). The real `business-pulse` SKILL.md is not
present on this machine (`source_skill` in the source metadata points at
`/Users/bear/Documents/CoWork/bear-textbooks/...`, Bear's machine, not this
one) — confirmed by search, no local copy exists anywhere under
`anthropics/knowledge-work-plugins/`. Per PHASE 1's "when in doubt, describe
behavior generically" rule, this redo does not invent the missing specific.
No claim is made about exactly which numbers or reports business-pulse
produces. Every fact this reel states about business-pulse is the generic
Claude Skills mechanism the source's intact beats (B01 anatomy, B02
pipeline) already fully support: a skill is a folder holding one SKILL.md
instruction file, Claude reads it before acting, a Steps section is
executed in order, linear, no branching unless a step says so. The name
"business-pulse" is used only as the named example throughout, exactly as
the source does, never elaborated with invented specifics. This is a
documented editorial call, not a blocker: the source's non-broken content
fully supports a complete, honest, teachable reel without the missing
fill-in.

Question, facts, and full body argument carried over unchanged from the
source's intact beats: a skill is a folder Claude reads before it works;
SKILL.md is the full instruction set in plain language with no hidden code;
"the file is the program"; the pipeline lives in a Steps section, executed
linearly, no branching unless a step says so; and the design/verdict fact —
because the skill is a written spec, Claude only does what the file says,
same steps every time (repeatable), and anything not written is outside
what it covers (the limit).

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "app" → "file" — the newcomer's wrong
guess that a named skill like business-pulse is a piece of software Claude
has installed and switches on, corrected toward the actual mechanism: it's
a plain file Claude reads before acting). Register re-registered
Teardown→Plain: the source's B03 "Here is the Teardown moment... What it
gets right / What it bites" framing was stripped of its Teardown wording and
compressed, together with BVDT's separate verdict card, into a single
NB03 mechanism-and-consequence beat — both were building toward the same
fact (the spec is the boundary), so keeping them as two cards would have
restated rather than added, and the Teardown "gets it right / bites"
framing is exactly the design-verdict language Plain's NO JUDGMENT check
forbids. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02 kept
as one beat each; B03+BVDT merged into the single NB03; BHTF kept as the
your-turn handoff but rewritten to a prompt any viewer can run today without
already having the business-pulse skill installed (the source's own prompt
depended on a business-task fill that the source itself never completed —
same broken-placeholder defect as B03/BVDT); BOUT kept. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with business-pulse-specific labels.

B00 params (42ms/char, 4% mistakeRate, 8% hesitateBetween, 4-line/~65-char
text) were carried over directly from that same sibling's already-fixed
timing pattern (its first attempt at 48ms/char/14%/6% ran out of its window
before the final line typed) rather than repeating the original slower
parameters — no timing defect this time. Audio generated fresh
(`generate_audio_kokoro.py`, all 7 beats, free/local, `am_onyx`, no
`--only` reruns needed); B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` (the run exceeded the tool's 120s timeout and was
moved to background by the harness automatically — blocked on it via
`TaskOutput` before proceeding, per the COMPLETION LAW's foreground-render
rule, never treating a backgrounded render as "handled" without waiting on
it); NB01–NB03 rendered via `render_scenes.py` (foreground, completed within
timeout).

Verified B00 by frame pull at t≈0s/2s/4s: "app" sits doomed in terracotta at
t≈2s, the full corrected question "Does opening business-pulse's file tell
Claude what to do?" is settled and legible by t≈4s, and holds to the end of
the 11.9s clip (well past the ≥8s TIMING LAW floor).

`type_check.py` (GATE T): **PASS, 0 FAILs** on the first pass — no fixes
needed. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-business-pulse.mp4`, 7/7 beats
filled real (no slate), 86.5s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 86.5s; mp4
  mtime (1788388299) newer than beat_sheet.json mtime (1788388179)
- Gate V (visual): pulled frames every 8s across the full 86.5s runtime plus
  targeted checks of B00 (t≈0/2/4s: "app" doomed in terracotta, then
  settled+correct "file", held to end of clip), NB01–NB03 (all chips
  legible, arrows/underline/captions clean), BCRY (carry-out quote +
  sparkline read clean), BHTF (correct topic/title/@HumanitariansAI handle,
  paste-ready prompt text legible), and BOUT (OutroSeries: correct eyebrow
  "BUSINESS-PULSE · @HumanitariansAI", correct title restate, crimson
  underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 11.9s (≥8s requirement met); the
  "app" → "file" correction lands on screen by t≈4s and the full corrected
  question stays legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-business-pulse.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly to
"Extending Claude — Skills, Plugins & Connectors" (no prefix-matching
ambiguity, unlike the `claude-plugins-official` sibling). Direct code link
per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `knowledge-work-plugins--claude-liam-business-pulse-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-business-pulse/` (4K
master + description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-business-pulse/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit
`c05f1016`, pushed clean (no rebase conflicts).

**Status: DELIVERED.**
