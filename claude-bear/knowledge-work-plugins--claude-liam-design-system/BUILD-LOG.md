# BUILD-LOG — knowledge-work-plugins--claude-liam-design-system

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-design-system/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `design-system`
Claude skill — audit, document, or extend a design system — already fully
built; no SCRIPT.md in the source, so source `beats[*].narration_text`
served as the locked script, per the `claude-liam-architecture` sibling's
precedent). Built entirely fresh this invocation — only SUBJECT.json
existed on pickup. The source SKILL.md itself
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/design/skills/design-system/SKILL.md`,
named in the source sheet's metadata) is on a path not present in this
tree; the source reel's own narration served as the fact record instead,
same as the architecture redo did for its source skill.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works; the SKILL.md is the full instruction
set in plain language, no hidden logic; the pipeline lives in the Steps
section and executes linearly, no branching unless a step says otherwise;
this particular skill's one job is auditing, documenting, or extending a
design system across four named scenarios (naming inconsistencies,
hardcoded values, component documentation of variants/states/accessibility,
designing a new pattern that fits what's there); and the payoff/limit pair
— checks against the existing system, never invents a fresh look. B00
replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "taste" → "its SKILL.md" — the
newcomer's wrong guess that Claude keeps a design system consistent using
its own good taste, corrected toward the actual mechanism: a written
instruction file). Register re-registered Teardown→Plain: the source's B03
"Here is the Teardown moment... What it gets right: repeatable results.
What it bites: anything outside the spec." was compressed to a plain
mechanism-and-scope description (NB03: the skill's one job and its exact
boundary), stripped of "gets it right / where it bites" verdict language.
BVDT's verdict facts (repeatable execution; the limit that only the file's
spec is covered) were merged into the single BCRY carry-out sentence rather
than kept as a separate bulleted artifact card, per CARRY-OUT LAW. Close
re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03 compressed into NB03 (the mechanism/scope fact,
verdict language stripped); BVDT folded into BCRY; BHTF kept — the source's
prompt text was garbled by truncation ("I want to audit, document, or
extend your design system. use when checking for naming inco.") and was
rebuilt here as a concrete, ungarbled, paste-ready prompt carrying the same
request (audit a design system for naming inconsistencies and hardcoded
values) plus the source's own flagged clause ("walk me through what you
will do before you do it"); BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`knowledge-work-plugins--claude-liam-architecture` sibling, adapted with
design-system-specific labels.

**GATE T catch #1 — NB03 chip label too small.** First `type_check.py` pass
FAILed: NB03's third chip, labelled "nothing invented" (16 chars), scaled
down under `_chip()`'s width/height fit and landed at 18px < the 20px
(1.9%-of-1080px) floor — longer than the architecture sibling's proven
"nothing else" (12 chars) at the same tier. Fixed by shortening the label
to "nothing else" (matching the sibling's already-passing choice) in both
`scenes.py`'s `BEAT_CONTENT` and beat_sheet.json's `production_viz.chips`;
deleted and re-rendered `manim/NB03.mp4`; re-ran `type_check.py` → GATE T
PASS, 0 FAILs.

**B00 defect caught by frame pull — real, not cosmetic.** First B00 build
used `triggerWords: "good taste"` (a two-word phrase) with
`replacementWords: "its SKILL.md"`. `remotion_scenes.py` rendered clean
(10.9s, no tool error) and GATE T/GATE AUDIO both passed on the first
compile — the defect was invisible to every automated gate and would have
shipped as a silently-broken cold open. Caught only by pulling frames
across the full B00 clip and reading them: the on-screen text finished
typing "Does Claude use good taste to keep a design system consistent?" by
~t=8s and stayed exactly that way, uncorrected, through the final frame at
t=10.8s — the WRITER LAW correction never fired.

Root cause, found by reading `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx`
line 130: `buildActs()` splits the input text into whitespace-separated
tokens and matches `triggerWords` against a single token's core text
(`const ti = triggers.indexOf(core.toLowerCase())`) — a multi-word trigger
phrase like "good taste" can never equal any single token, so the
replacement branch is silently never taken for it. The architecture
sibling's precedent (`triggerWords: "judgment"`) worked specifically
because it was one word; this build's structurally analogous two-word
phrase carries the identical prop shape but a different, broken outcome —
which is exactly why the WRITER LAW mandates a frame-pull verification of
the actual correction landing on screen, not just a duration check.

Fixed by narrowing to a single-word trigger: dropped "good" from the
on-screen text and narration entirely (on-screen text now "Does Claude
use\ntaste\nto keep a design\nsystem consistent?", narration "...using
taste. It doesn't — a written file does..."), `triggerWords: "taste"`,
`replacementWords: "its SKILL.md"` unchanged. Regenerated B00's audio only
(10.56s, `--only B00`), deleted and re-rendered `media/B00.mp4` only
(`--only B00`, 10.6s). Reverified by frame pull: "taste" sits doomed in
terracotta at t≈3s, corrected to "its SKILL.md" by t≈5s, and the full
corrected question ("Does Claude use its SKILL.md to keep a design system
consistent?") stays settled and legible through t≈10.3s — comfortably past
the ≥8s TIMING LAW floor. SCRIPT.md's B00 section carries this defect/fix
note for future redos using a multi-word trigger.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; B00 regenerated once after the trigger-word fix via `--only
B00`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground;
B00 re-rendered singly after its fix, `--only B00`); NB01–NB03 rendered via
`render_scenes.py` (NB03 re-rendered singly after the chip-label fix).
`type_check.py` FAILed once (NB03 min-size, fixed above) then PASSED, 0
FAILs. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-design-system.mp4`, 7/7 beats
filled real (no slate), 80.7s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (after the NB03 chip-label fix)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 80.71s; mp4
  mtime (1788465553) newer than beat_sheet.json mtime (1788465413)
- Gate V (visual): pulled frames across the full runtime plus targeted
  checks of B00 (t≈3s "taste" doomed in terracotta, t≈5s corrected to "its
  SKILL.md", held legible to t≈10.3s — the correction defect above, fully
  reverified after the fix), NB01 (chips legible, correct labels/caption/
  accent underline), NB02 (chips legible, correct labels/caption/accent
  underline), NB03 (chips legible post-fix, correct labels/caption/accent
  underline), BCRY (carry-out sentence + sparkline read clean), BHTF
  (correct topic/title/@HumanitariansAI handle, full paste-ready prompt
  legible with no clipping), and BOUT (OutroSeries: correct eyebrow
  "DESIGN-SYSTEM · @HumanitariansAI", correct title restate, crimson
  underline, no truncation). No blockers remaining.
- B00 TIMING LAW: `actual_duration_s` 10.56s (≥8s requirement met); the
  "taste" → "its SKILL.md" correction lands on screen by t≈5s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written:
`knowledge-work-plugins--claude-liam-design-system.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly to
"Extending Claude — Skills, Plugins & Connectors" (no fallthrough to the
`hai-simple` skill-key default of "Claude Basics" needed). Direct code link
per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
