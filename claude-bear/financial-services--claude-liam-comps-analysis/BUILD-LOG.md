# BUILD-LOG — financial-services--claude-liam-comps-analysis

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-comps-analysis/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `comps-analysis`
Skill — a `market-researcher` plugin Skill, financial-services family —
already fully built; no SCRIPT.md existed for the source, so its
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and body argument carried over unchanged: a skill is a
folder Claude reads before it works; the SKILL.md inside it is the full
instruction set (plain language, no hidden logic — "the file is the
program"); the pipeline lives in the file's Steps section, executed one
step at a time in written order, linear, no branching unless a step says
to; and the consequent fact that comps-analysis is a specification rather
than a suggestion — same input produces the same output every run, and
outside what the file specifies there's nothing to fall back on. B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "reason" → "follow" — the
newcomer's wrong guess that Claude reasons through a Skill's task like an
analyst, corrected toward the actual mechanism: Claude follows the
written steps). Register re-registered Teardown → Plain: the source B03's
"what it gets right: repeatable results / what it bites: anything outside
the spec" strengths/gaps framing was compressed into NB03 as a plain
mechanism-and-consequence statement, dropping the verdict framing per the
NO JUDGMENT register check. BVDT's verdict facts (same input → same
output every run; limited to what the file says) were merged into the
single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Source defect found and worked around, not silently carried over:** the
source `beat_sheet.json`'s narration for B00, B03, BVDT, and BHTF contains
a literal unfilled template placeholder character (`│`) where a
comps-analysis-specific clause was evidently meant to be substituted by
whatever batch script generated the source, and never was. Confirmed by:
the source dir's `PEDAGOGY.md` logs only "Batch build — skill teardown
format" (no verdict detail); the source sheet's `metadata.source_skill`
path (`/Users/bear/Documents/CoWork/.../comps-analysis/SKILL.md`) does not
exist on this machine, so the missing clause could not be recovered.
Rather than inventing unverifiable comps-analysis-specific mechanics
(which financial multiples it pulls, which data sources it hits) to fill
the gap, every beat's teaching point was kept at the level the source
actually supports without the placeholder text (folder, SKILL.md, Steps
section, linear execution, determinism, the file-bound limit), and BHTF's
placeholder ("I want to │. Read the comps-analysis skill...") was filled
with a generic, plausible, paste-ready task ("I want to run a comps
analysis on a public company") rather than a specific one, since the
source never specified which task the missing clause named. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03's Teardown framing compressed into NB03; BVDT
folded into BCRY; BHTF kept, with its placeholder filled per above; BOUT
kept, re-skinned. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats,
matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with comps-analysis-specific labels.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; B00 actual duration 10.94s). B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` (foreground; the run exceeded the tool's 120s timeout
and was moved to background by the harness automatically — blocked on it
via `TaskOutput` before proceeding, per the COMPLETION LAW's
foreground-render rule, never treating a backgrounded render as "handled"
without waiting on it); NB01–NB03 rendered via `render_scenes.py`
(foreground, completed within the timeout).

**B00 TIMING LAW: verified by frame pull, no defect found this time.**
media/B00.mp4 actual duration 10.97s (≥8s floor, comfortable margin).
Frame pulls at t≈2s ("When Claude runs" settled), t≈4.5s (mid-typing
"rea|" of "reason", doomed word visibly in terracotta), and t≈9.5s (full
corrected question "When Claude runs a comps analysis, does it follow
through the steps?" settled and legible, held for ~1.4s of remaining
runtime) confirm the correction lands on screen well before the clip
ends. Parameters were copied directly from the proven-working fix on the
`claude-plugins-official--claude-liam-agent-development` sibling (42
ms/char, 8% hesitateBetween, 4% mistakeRate) rather than that sibling's
failed first attempt, despite this reel's text running 66 chars vs. that
fix's 60 — margin held.

First `type_check.py` pass was **FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB03** — smallest text run measured 14px, well under the
  20px floor. Root cause: NB03's third chip label, `"outside the file:
  nothing"` (24 chars), fell into the smallest font-size bucket in the
  shared chip-row renderer (labels >22 chars render at font_size 18),
  and after scale-to-fit within the chip box the glyph strokes measured
  under the floor. Fixed by shortening the label to `"nothing else"` (12
  chars, the same top font-size bucket as its siblings) and re-rendering
  NB03 only; `beat_sheet.json`'s `graphic.production_viz.chips` for NB03
  was synced to match directly (not via a full `build_beat_sheet.py`
  re-run, which would have discarded already-measured audio durations and
  render stamps) before recompiling, per COMPLETION LAW.

`type_check.py` went 1→PASS. Compiled once, then **Gate V (visual QC),
reading actual frames rather than trusting the type-check pass, caught a
second, more serious defect that GATE T's automated checks do not
measure: two chip labels rendered with their inter-word space collapsed
to zero** — `"Steps section"` read as `"Stepssection"` (NB02's first
chip) and the just-fixed `"nothing else"` read as `"nothingelse"` (NB03's
third chip) — both fully legible as single fused words, not a hedge or a
kerning nit, a genuine misread. Isolated with three throwaway Manim test
renders (outside the reel, `/tmp/_boldtest*.py`) before touching
production files: reproduced with both BOLD and NORMAL weight (so not an
accent-styling side effect), and empirically narrowed to a specific
Manim/Pango text-layout bug in this environment where a two-word `Text()`
string collapses its space **specifically when "Steps" or "nothing" is
the first word** ("Steps section", "Steps order", "nothing outside" all
collapsed; "the Steps", "step order", "no fallback", "outside only", and
every other two-word combination tested rendered with a normal space).
Root-cause fix: reworded rather than patched around — NB02's chip 0
changed `"Steps section"` → `"the Steps"` and NB03's chip 2 changed
`"nothing else"` → `"no fallback"` (also a better fit for the narration's
"nothing written down to fall back on"), both confirmed clean in the
isolated test before being applied to `scenes.py` and synced into
`beat_sheet.json`. Re-rendered NB02 and NB03 only, recompiled — `type_check.py`
re-ran PASS (unaffected by this defect class, confirming Gate V's visual
frame-read is doing real work GATE T's automated pass does not cover).

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `financial-services--claude-liam-comps-analysis.mp4`, 7/7 beats
filled real (no slate), 80.3s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 80.3s; mp4
  mtime (1788278064) newer than beat_sheet.json mtime (1788277977)
- Gate V (visual): pulled frames across the full runtime (B00 at t≈2/4.5/9.5s
  for the WRITER LAW correction; NB01–NB03 chips post-fix; BCRY carry-out
  quote + sparkline; BHTF correct topic/title/@HumanitariansAI handle and
  legible paste-ready prompt; BOUT correct eyebrow "COMPS ANALYSIS ·
  @HumanitariansAI" and title restate). Found and fixed the word-space
  collapse defect described above — the only blocker, now resolved. No
  remaining blockers.
- B00 TIMING LAW: `actual_duration_s` 10.97s (≥8s requirement met); the
  "reason" → "follow" correction lands on screen by t≈9.5s (fully settled,
  visible mid-typing by t≈4.5s) and stays legible for the remainder of the
  clip.

Metadata file written: `financial-services--claude-liam-comps-analysis.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`financial-services`) matches no
map prefix (checked in order: no `financial-services`-prefixed key
exists), so per the fallback rule the skill value `hai-simple` was matched
against the map instead, hitting the `"hai-simple"` key directly →
"Claude Basics". Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-01 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `financial-services--claude-liam-comps-analysis-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/financial-services--claude-liam-comps-analysis/` (4K
master + description) for the Drive sync. Committed to
`claude-bear/financial-services--claude-liam-comps-analysis/` (README.md
= description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `323a9b7`, pushed clean
(no rebase conflicts).

**Status: DELIVERED.**
