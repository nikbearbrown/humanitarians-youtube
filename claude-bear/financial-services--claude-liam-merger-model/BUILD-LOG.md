# BUILD-LOG — financial-services--claude-liam-merger-model

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-merger-model/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `merger-model`
Skill — an `investment-banking` plugin Skill, financial-services family;
already fully built; no SCRIPT.md existed for the source, so its
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup. Used the
`financial-services--claude-liam-comps-analysis` sibling (same family,
same source shape) as the structural template.

Question, facts, and body argument carried over unchanged: a skill is a
folder Claude reads before it works; the SKILL.md inside it is the full
instruction set (plain language, no hidden logic — "the file is the
program"); the pipeline lives in the file's Steps section, executed one
step at a time in written order, linear, no branching unless a step says
to; and merger-model specifically builds accretion/dilution analysis for
M&A transactions — pro forma EPS impact, synergy sensitivities, purchase
price allocation — as a specification, not a suggestion: same input,
same output, every run, nothing outside the file to fall back on. B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "reason" → "follow" — the
newcomer's wrong guess that Claude reasons through the deal math like an
M&A analyst forming a view, corrected toward the actual mechanism: Claude
follows the written steps). Register re-registered Teardown → Plain: the
source B03's "Here is the Teardown moment... What it gets right:
repeatable results. What it bites: anything outside the spec." framing
was compressed into NB03 as a plain mechanism-and-consequence statement,
dropping the verdict framing per the NO JUDGMENT register check. BVDT's
verdict facts (same input → same output every run; limited to what the
file says) were merged into the single BCRY carry-out sentence rather
than kept as a separate bulleted artifact card, per CARRY-OUT LAW. Close
re-skinned to @HumanitariansAI (`OutroSeries`).

**Source defect found and worked around, not silently carried over,
unlike the comps-analysis sibling's case:** the source `beat_sheet.json`'s
narration for B03, BVDT, and BHTF each contain the merger-model skill's
own description mid-word truncated — "synergy sensiti." (B03), "pro forma
EPS imp." (BVDT), and an ungrammatical splice in BHTF ("I want to build
accretion/dilution analysis for m&a transactions. models pro forma eps
imp.") — evidently a batch script's fixed-character-budget cut applied
mid-word. Unlike the comps-analysis sibling, where the equivalent
template slot was a literal unfilled placeholder with no recoverable
content anywhere in the source, this source's own **B00** narration
carries the complete, untruncated description in full ("Build
accretion/dilution analysis for M&A transactions. Models pro forma EPS
impact, synergy sensitivities, and purchase price allocation. Use when
evaluating a potential acquisition, preparing merger consequences
analysis for a pitch, or advising on deal terms."). This redo recovers
the specific, verifiable facts from that complete copy for NB03 and BHTF
rather than propagating the truncated fragments or inventing unverifiable
mechanics. The source's `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/investment-banking/skills/merger-model/SKILL.md`)
does not resolve on this machine, so nothing beyond what the source's own
B00 already states in full was added. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03's Teardown framing (enriched with the
recovered full description) became NB03; BVDT folded into BCRY; BHTF
kept, its prompt restored to grammatical form using the recovered
description; BOUT kept, re-skinned. Total: B00 + NB01–NB03 + BCRY + BHTF
+ BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`financial-services--claude-liam-comps-analysis` sibling, adapted with
merger-model-specific labels.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; B00 actual duration 11.01s). B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` — the run exceeded the tool's 120s inline timeout and
was moved to background by the harness automatically; blocked on it via
`TaskOutput` before proceeding, per the COMPLETION LAW's foreground-render
rule, never treating a backgrounded render as "handled" without waiting
on it. NB01–NB03 rendered via `render_scenes.py` (foreground, completed
within the timeout).

**B00 TIMING LAW: verified by frame pull, no defect found.** media/B00.mp4
actual duration 11.03s (≥8s floor, comfortable margin). Frame pulls at
t≈2s ("When Claude builds" settled), t≈4.5s (mid-typing, an incidental
typo glyph in terracotta from `mistakeRate` — not the trigger-word swap —
visible and expected), and t≈10.5s (full corrected question "When Claude
builds a merger model, does it follow through the steps?" fully settled
and legible, held for ~0.5s of remaining runtime) confirm the correction
lands on screen well before the clip ends. Parameters copied directly
from the proven-working fix on the `financial-services--claude-liam-comps-analysis`
sibling (42 ms/char, 8% hesitateBetween, 4% mistakeRate, 2%
hesitateWithin, 26% jitter) — this reel's text runs 68 chars vs. that
fix's 66; margin held.

First `type_check.py` pass was **FAIL, 1 defect**:

- **min-size §8.1, NB03** — smallest text run measured 16px, under the
  20px floor. Root cause: the chip label `"accretion/dilution"` (19
  chars, no internal spaces to help wrapping) fell into the 22-char font
  tier in the shared chip-row renderer, but after scale-to-fit within the
  3.2-unit-wide chip box the glyph run still measured under the floor —
  visually confirmed by frame pull (the chip rendered noticeably smaller
  than its two siblings). Fixed by shortening to `"acc/dilution"` (12
  chars, the same top font-size tier as the other two chips). Re-checking
  surfaced a **second** instance of the same defect class at the same
  16px value on chip 2, `"price allocation"` (16 chars, 22-char tier,
  smaller font than the 14-char tier) — shortened to `"PP allocation"`
  (13 chars) to match. Both fixes applied directly to `scenes.py` and
  `beat_sheet.json`'s `graphic.production_viz.chips` (kept in sync, not
  via a full sheet regeneration, which would have discarded measured
  audio durations); NB03 re-rendered both times; recompiled after the
  second fix. `type_check.py` went FAIL→FAIL(same code, second offender
  surfaced only after the first was fixed)→PASS.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `financial-services--claude-liam-merger-model.mp4`, 7/7 beats
filled real (no slate), 88.6s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 2 chip-label defects + fixes above)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect)
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 88.6s; mp4
  mtime (1788328969) newer than beat_sheet.json mtime (1788328787)
- Gate V (visual): pulled frames across the full runtime (B00 at t≈1/6s
  for the WRITER LAW correction window; NB01–NB03 chip rows post-fix;
  BCRY carry-out quote + sparkline; BHTF correct topic/title/
  @HumanitariansAI handle and legible paste-ready prompt; BOUT correct
  eyebrow "MERGER-MODEL · @HumanitariansAI" and title restate). No
  blockers found.
- B00 TIMING LAW: `actual_duration_s` 11.03s (≥8s requirement met); the
  "reason" → "follow" correction fully settles by t≈10.5s and the clip
  runs to 11.03s.

Metadata file written: `financial-services--claude-liam-merger-model.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`financial-services`) matches no
map prefix, so per the fallback rule the skill value `hai-simple` was
matched against the map instead, hitting the `"hai-simple"` key directly
→ "Claude Basics". Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.
