# BUILD-LOG — knowledge-work-plugins--claude-liam-customer-pulse

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-customer-pulse/beat_sheet.json`
(a Teardown skill-teardown walkthrough of a Claude Skill named
`customer-pulse`, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup (an earlier
`.filmloop` worker log for this slug exists but is empty — no artifacts
left behind to reuse).

**Source data defect found and handled.** The source `beat_sheet.json`'s
B03 and BVDT `narration_text` fields contain an unfilled batch-template
placeholder — a literal `>` where the skill's specific one-line task
description should have been (e.g. "Claude's job: >."). Confirmed this is
a data gap unique to this source file, not a deliberate omission or a
formatting convention: sibling sources such as `claude-liam-forecast` have
the equivalent line filled in full, and the sibling hai-simple redo
`knowledge-work-plugins--claude-liam-business-pulse` (built 2026-09-02)
hit the identical defect in its own source. The real `customer-pulse`
SKILL.md is not present on this machine (`source_skill` in the source
metadata points at `/Users/bear/Documents/CoWork/bear-textbooks/...`,
Bear's machine, not this one) — confirmed by search; no local copy exists
anywhere under `anthropics/knowledge-work-plugins/`. A sibling skill,
`customer-pulse-check`, does have its placeholder filled in on this
machine ("Synthesizes themes from PayPal disputes, HubSpot tickets, and
review exports into a top-3 fixable issues list with drafted response
templates") — that text describes a *different*, adjacent skill and is not
borrowed here; per PHASE 1's "when in doubt, describe behavior
generically" rule, this redo does not invent the missing `customer-pulse`
specific and does not cross-attribute the sibling's confirmed facts to it.
Every fact this reel states about customer-pulse is the generic Claude
Skills mechanism the source's intact beats (B01 anatomy, B02 pipeline)
already fully support: a skill is a folder holding one SKILL.md
instruction file, Claude reads it before acting, a Steps section is
executed in order, linear, no branching unless a step says so. The name
"customer-pulse" is used only as the named example throughout, exactly as
the source does, never elaborated with invented specifics.

Question, facts, and full body argument carried over unchanged from the
source's intact beats: a skill is a folder Claude reads before it works;
SKILL.md is the full instruction set in plain language with no hidden
code; "the file is the program"; the pipeline lives in a Steps section,
executed linearly, no branching unless a step says so; and the
design/verdict fact — because the skill is a written spec, Claude only
does what the file says, same steps every time (repeatable), and anything
not written is outside what it covers (the limit).

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "app" → "file" — the newcomer's
wrong guess that a named skill like customer-pulse is a piece of software
Claude has installed and switches on, corrected toward the actual
mechanism: it's a plain file Claude reads before acting). Register
re-registered Teardown→Plain: the source's B03 "Here is the Teardown
moment... What it gets right / What it bites" framing was stripped of its
Teardown wording and compressed, together with BVDT's separate verdict
card, into a single NB03 mechanism-and-consequence beat — both were
building toward the same fact (the spec is the boundary), so keeping them
as two cards would have restated rather than added, and the Teardown
"gets it right / bites" framing is exactly the design-verdict language
Plain's NO JUDGMENT check forbids. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03+BVDT merged into the single NB03; BHTF kept as
the your-turn handoff but rewritten to a prompt any viewer can run today
without already having the customer-pulse skill installed (the source's
own prompt depended on a customer-task fill that the source itself never
completed — same broken-placeholder defect as B03/BVDT, re-pointed to a
customer-feedback pulse-check framing that matches the skill's name); BOUT
kept. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`), copied verbatim
(mechanism, colors, GATE T exemption notes) from the sibling
`knowledge-work-plugins--claude-liam-business-pulse` reel, adapted with
customer-pulse-specific labels. B00 params (42ms/char, 4% mistakeRate, 8%
hesitateBetween, 4-line/~65-char text) were likewise carried over from
that same sibling's already-fixed timing pattern.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`) — B00 measured 12.07s (well past the ≥8s TIMING LAW floor).
Remotion beats (B00/BCRY/BHTF/BOUT) rendered via `remotion_scenes.py`; the
run exceeded the tool's 120s foreground timeout and was moved to
background by the harness automatically — blocked on it via `TaskOutput`
before proceeding to the next step, per the COMPLETION LAW's
foreground-render rule (never treating a backgrounded render as "handled"
without waiting on its exit). All 4 Remotion beats rendered clean on the
first attempt. NB01–NB03 rendered via `render_scenes.py` (foreground,
completed within timeout, no failures).

**First-pass GATE T caught one real defect and it was fixed before
compiling further:** NB01's first chip label, `"customer-pulse/"` (15
chars, including the trailing slash), fell into the chip renderer's
mid-size font bucket and, after the fit-to-box scale-down, rendered at
16px — under the 20px floor. Fixed by dropping the trailing slash
(`"customer-pulse"`, 14 chars exactly), which moves the label into the
renderer's largest font bucket (26px before scaling); re-rendered NB01
only (`render_scenes.py` skips beats whose output already exists, so the
other two GRAPHIC beats were untouched) and recompiled. Second GATE T pass:
**PASS, 0 FAILs.**

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-customer-pulse.mp4`, 7/7 beats
filled real (no slate), 87.3s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (after the NB01 chip-label fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 87.26s; mp4
  mtime (1788443137) newer than beat_sheet.json mtime (1788443083)
- Gate V (visual): pulled frames every 8s across the full run plus a
  finer 1s-step pass around t=18–29s to double-check an apparently blank
  8s-grid sample inside NB01's span — the finer pass showed the NB01
  diagram fully present and legible at every second in that window, so the
  earlier blank frame was a sampling artifact of the coarse fps filter,
  not a render gap. Confirmed: B00 (naive "app" framing settles to the
  corrected "file" question well before the clip ends), NB01–NB03 (all
  chip labels legible incl. the fixed "customer-pulse" label, arrows/
  underline/caption clean), BCRY (carry-out quote + sparkline read
  clean), BHTF (correct topic/title/@HumanitariansAI handle, customer
  pulse-check prompt text legible), and BOUT (OutroSeries: correct
  eyebrow "CUSTOMER-PULSE · @HumanitariansAI", correct title restate,
  crimson underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 12.07s (≥8s requirement met); the
  "app" → "file" correction lands and the full corrected question stays
  legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-customer-pulse.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly
to "Extending Claude — Skills, Plugins & Connectors" (no prefix-matching
ambiguity). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
