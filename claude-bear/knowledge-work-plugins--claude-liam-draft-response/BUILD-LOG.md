# BUILD-LOG — knowledge-work-plugins--claude-liam-draft-response

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-draft-response/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `draft-response`
Claude Skill — draft a professional customer-facing response tailored to
the situation and relationship — already fully built; no SCRIPT.md in the
source, so source `beats[*].narration_text` served as the locked script).
Built entirely fresh this invocation — only SUBJECT.json existed on
pickup. Used the same-day sibling
`knowledge-work-plugins--claude-liam-architecture` (also a redo of a
skill-teardown source, same family, built 2026-09-02) as the structural
template: its `scenes.py`/`render_scenes.py` chip-row Manim template was
copied verbatim (mechanism, colors, GATE T exemption notes) and adapted
with draft-response-specific labels.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works; the SKILL.md is the full instruction
set in plain language, no hidden logic; the pipeline lives in the Steps
section and executes linearly, no branching unless a step says otherwise;
this particular skill's one job is drafting a customer-facing reply across
five named situations (a product question, an escalation or outage, a
delay or won't-fix, a declined feature request, a billing issue); and the
payoff/limit pair — repeatable execution, but only within what the file
specifies. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold
open with `BrutalistHesitantWriter` (WRITER LAW: "empathy" → "its
SKILL.md" — the newcomer's wrong guess that Claude's customer-facing tone
comes from its own empathy or judgment, corrected toward the actual
mechanism: a written instruction file). Register re-registered
Teardown→Plain: the source's B03 "Here is the Teardown moment... What it
gets right: repeatable results. What it bites: anything outside the spec."
was compressed to a plain mechanism-and-scope description (NB03: the
skill's one job and its exact boundary), stripped of "gets it right /
where it bites" verdict language. BVDT's verdict facts (repeatable
execution; the limit that only the file's spec is covered) were merged
into the single BCRY carry-out sentence rather than kept as a separate
bulleted artifact card, per CARRY-OUT LAW. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03 compressed into NB03 (the mechanism/scope fact,
verdict language stripped); BVDT folded into BCRY; BHTF kept — the
source's prompt text was garbled by truncation ("I want to draft a
professional customer-facing response tailored to the situation and
rela.") and was rebuilt here as a concrete, ungarbled, paste-ready prompt
anchored to a specific scenario (an escalation) plus the source's own
flagged clause ("walk me through what you will do before you do it"); BOUT
kept. Full audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`knowledge-work-plugins--claude-liam-architecture` sibling, adapted with
draft-response-specific labels.

**B00 TIMING LAW — verified clean, no defect.** Text "Does Claude use /
empathy / to draft a good / customer reply?" (4 lines, 58 forward-typed
chars), trigger "empathy" → replacement "its SKILL.md", mistakeRate 4%,
hesitateWithin 2%, hesitateBetween 8%, charMs 42 (the already-fixed rates
from the architecture sibling) — audio measured 10.24s. `remotion_scenes.py`
hit the harness's foreground command timeout partway through the initial
4-beat batch render (B00/BCRY/BHTF/BOUT); moved to background
automatically by the tool, then waited on synchronously (polling the
background task's own output file with a foreground loop, per the
COMPLETION LAW's "never end the turn on a backgrounded render" rule) until
it exited 0 — all 4 beats completed cleanly in that run, so no partial or
mistimed B00 clip was produced this time (unlike the architecture
sibling's B00 incident). Verified by frame pull: "empathy" sits doomed in
terracotta mid-typing, and the full corrected question "Does Claude use its
SKILL.md to draft a good customer reply?" is settled and legible by t≈9.5s,
comfortably inside the 10.2s clip and past the ≥8s TIMING LAW floor.

**BHTF composer-card clipping — one real defect caught and fixed.** First
BHTF command ("Draft a customer-facing response to an escalation for my
team. Walk me through your plan before you act.", 104 chars — close in
length to the architecture sibling's working 109-char command) still
clipped in `ClaudeComposerAsk`'s input area, which is hard-capped at
`maxHeight: CMD * 1.45 * 3` (3 wrapped lines) with `overflow: hidden`.
Caught by a frame pull mid-BHTF: the visible card read "Draft a
customer-facing response to an escalation for my team. Walk m" with
"e through your plan before you act." silently clipped off-frame — the
long compound word "customer-facing" plus "escalation" forced the wrap
earlier than raw character count alone predicted (confirmed by reading the
component's auto-fit font-size logic in `ClaudeComposerAsk.tsx`, which
sizes the command font from total string length rather than per-line
length when the command has no explicit `\n`). Fixed by shortening the
on-screen command to "Draft a reply to an escalation for my team. Walk me
through your plan before you act." (85 chars, 2-line fit) and updating
BHTF's narration to match; re-generated BHTF's audio only
(`--only BHTF`, 12.48s) and re-rendered BHTF only (media/B00, NB01–03,
BCRY, BOUT untouched). Reverified by frame pull at the end of the beat's
window: the full sentence, including the emphasized "before you act"
clause, is visible on 2 lines with no clipping.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; BHTF regenerated once after the text fix via `--only BHTF`);
B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground; BHTF was
re-rendered singly after its text fix, `--only BHTF`); NB01–NB03 rendered
via `render_scenes.py`. `type_check.py` ran **PASS, 0 FAILs** both before
and after the BHTF fix (no GATE T defects this build). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-draft-response.mp4`, 7/7
beats filled real (no slate), 72.5s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.1 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 72.46s; mp4
  mtime (1788480187) newer than beat_sheet.json mtime (1788480120)
- Gate V (visual): pulled frames every 6s across the full runtime plus
  targeted checks of B00 (early frame "Does Claude" typing, t≈9.5s settled
  and correct final question, held to the end of the 10.2s clip),
  NB01–NB03 (all chips legible and parallel-sized, correct
  labels/captions/accent underline — "A SKILL IS A FOLDER" /
  "READ THEN EXECUTE" / "ONE FILE, ONE JOB"), BCRY (carry-out sentence +
  sparkline read clean), BHTF (correct topic/title/@HumanitariansAI
  handle, full paste-ready prompt legible with no clipping after the fix,
  confirmed with frames at beat-start, mid-typing, and beat-end), and BOUT
  (OutroSeries: correct eyebrow "DRAFT-RESPONSE · @HumanitariansAI",
  correct title restate, crimson underline, no truncation). No blockers
  remaining after the BHTF fix.
- B00 TIMING LAW: `actual_duration_s` 10.24s (≥8s requirement met); the
  "empathy" → "its SKILL.md" correction lands on screen by t≈9.5s and the
  full corrected question stays legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-draft-response.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly
to "Extending Claude — Skills, Plugins & Connectors" (no fallthrough to
the `hai-simple` skill-key default of "Claude Basics" needed). Direct code
link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
