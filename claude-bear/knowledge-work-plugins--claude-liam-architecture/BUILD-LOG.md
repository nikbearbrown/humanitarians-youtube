# BUILD-LOG — knowledge-work-plugins--claude-liam-architecture

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-architecture/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `architecture`
Claude Skill — create or evaluate an architecture decision record — already
fully built; no SCRIPT.md in the source, so source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works; the SKILL.md is the full instruction
set in plain language, no hidden logic; the pipeline lives in the Steps
section and executes linearly, no branching unless a step says otherwise;
this particular skill's one job is creating or evaluating an architecture
decision record across four named scenarios (choosing between technologies,
documenting a trade-off, reviewing a design proposal, designing a new
component from constraints); and the payoff/limit pair — repeatable
execution, but only within what the file specifies. B00 replaced the
source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "judgment" → "its SKILL.md" — the
newcomer's wrong guess that Claude's architecture calls come from its own
judgment about good design, corrected toward the actual mechanism: a
written instruction file). Register re-registered Teardown→Plain: the
source's B03 "Here is the Teardown moment... What it gets right: repeatable
results. What it bites: anything outside the spec." was compressed to a
plain mechanism-and-scope description (NB03: the skill's one job and its
exact boundary), stripped of "gets it right / where it bites" verdict
language. BVDT's verdict facts (repeatable execution; the limit that only
the file's spec is covered) were merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02 kept
as one beat each; B03 compressed into NB03 (the mechanism/scope fact, verdict
language stripped); BVDT folded into BCRY; BHTF kept — the source's prompt
text was garbled by truncation ("I want to create or evaluate an
architecture decision record (adr). use when choosing betw.") and was
rebuilt here as a concrete, ungarbled, paste-ready prompt carrying the same
request (create an ADR, choosing between two technologies) plus the
source's own flagged clause ("walk me through what you will do before you
do it"); BOUT kept. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row" Manim
template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with architecture-specific labels.

**B00 TIMING LAW — verified clean, no defect.** Text "Does Claude use /
judgment / to write a good / architecture call?" (4 lines, 59 forward-typed
chars), trigger "judgment" → replacement "its SKILL.md", mistakeRate 4%,
hesitateWithin 2%, hesitateBetween 8%, charMs 42 (the already-fixed rates
from the agent-development sibling) — audio measured 10.13s. First
`remotion_scenes.py` invocation covering all 4 REMOTION beats hit the tool's
120s timeout mid-run; the interrupted process had written a raw B00.mp4
before being killed, but at 20.24s — the composition's natural (untrimmed)
typing-performance length, not yet reconciled against the 10.13s audio clock
by the script's extend/trim step. Caught before compiling (duration
mismatch spotted via ffprobe, not assumed correct from file presence alone);
deleted and re-rendered B00 alone (`--only B00`, single-beat invocation to
avoid the timeout), producing the correctly time-locked 10.13s clip.
Verified by frame pull: "judgment" sits doomed in terracotta at t≈2s, and
the full corrected question "Does Claude use its SKILL.md to write a good
architecture call?" is settled and legible by t≈9.5s, comfortably inside the
10.1s clip and past the ≥8s TIMING LAW floor.

**BHTF composer-card overflow — one real defect caught and fixed.** First
BHTF command ("I want to create an architecture decision record for
choosing between two technologies for my project. Read the architecture
skill and walk me through what you will do before you do it.", ~190 chars)
wrapped to 4 lines in `ClaudeComposerAsk`'s input area, but that area is
hard-capped at `maxHeight: CMD * 1.45 * 3` (3 wrapped lines) with `overflow:
hidden` — confirmed by reading the component source, not just observing the
symptom. Caught by a frame pull mid-BHTF: the visible card read "...Read the
architecture skill and walk me through what you will do" with "before you do
it." silently clipped off-frame. Fixed by shortening the on-screen command
to "Create an ADR for choosing between two technologies for my project. Walk
me through your plan before you act." (109 chars, 2-line fit) and updating
BHTF's narration to match; re-generated BHTF's audio only (14.34s) and
re-rendered BHTF only (media/B00, NB01–03, BCRY, BOUT untouched).
Reverified by frame pull: the full sentence, including the emphasized
"before you act" clause, is visible on 2 lines with no clipping.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; BHTF regenerated once after the text fix via `--only BHTF`);
B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground; B00 was
re-rendered singly per the TIMING LAW note above; BHTF was re-rendered
singly after its text fix); NB01–NB03 rendered via `render_scenes.py`.
`type_check.py` ran **PASS, 0 FAILs** on the first pass (no GATE T defects
this build). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-architecture.mp4`, 7/7 beats
filled real (no slate), 72.5s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 72.56s; mp4
  mtime (1788365973) newer than beat_sheet.json mtime (1788365896)
- Gate V (visual): pulled frames every 6s across the full runtime plus
  targeted checks of B00 (t≈2s "judgment" doomed in terracotta, t≈9.5s
  settled+correct question, held to the end of the 10.1s clip), NB01–NB03
  (all chips legible and parallel-sized, correct labels/captions/accent
  underline), BCRY (carry-out sentence + sparkline read clean), BHTF
  (correct topic/title/@HumanitariansAI handle, full paste-ready prompt
  legible with no clipping after the fix), and BOUT (OutroSeries: correct
  eyebrow "ARCHITECTURE · @HumanitariansAI", correct title restate, crimson
  underline, no truncation). No blockers remaining.
- B00 TIMING LAW: `actual_duration_s` 10.13s (≥8s requirement met); the
  "judgment" → "its SKILL.md" correction lands on screen by t≈9.5s and the
  full corrected question stays legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-architecture.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly to
"Extending Claude — Skills, Plugins & Connectors" (no fallthrough to the
`hai-simple` skill-key default of "Claude Basics" needed). Direct code link
per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
