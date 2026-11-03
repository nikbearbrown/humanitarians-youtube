# BUILD-LOG — financial-services--claude-liam-lbo-model

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-lbo-model/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `lbo-model`
Skill — a `model-builder` plugin Skill, financial-services family —
already fully built; no SCRIPT.md existed for the source, so its
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and body argument carried over unchanged: a skill is a
folder Claude reads before it works; the SKILL.md inside it is the full
instruction set (plain language, no hidden logic — "the file is the
program"); the pipeline lives in the file's Steps section, executed one
step at a time in written order, linear, no branching unless a step says
to; and the skill's own description names three concrete actions — it
fills in formulas, validates the calculations against each other, and
checks formatting against a professional standard — and does so on
whatever LBO template it's handed, because it reads the template's own
structure first rather than assuming one fixed layout. B00 replaced the
source's `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter`
(WRITER LAW: "design" → "fill" — the newcomer's wrong guess that Claude
designs an LBO model's structure and deal assumptions from scratch like
an analyst, corrected toward the actual mechanism: Claude fills in and
checks an existing template). Register re-registered Teardown → Plain:
the source B03's "what it gets right: repeatable results / what it
bites: anything outside the spec" strengths/gaps framing was dropped;
NB03 instead states the skill's own three named actions plus the
template-independence fact as a plain mechanism statement, per the NO
JUDGMENT register check. BVDT's verdict facts (same input → same output
every run; limited to what the file says) were merged into the single
BCRY carry-out sentence rather than kept as a separate bulleted artifact
card, per CARRY-OUT LAW. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Source defect found and worked around, not silently carried over:**
unlike the `claude-liam-comps-analysis` sibling (which had a literal
unfilled `│` placeholder), this source's B00/B03/BVDT narration was
already complete — its frontmatter description clause is fully formed
throughout and was usable as-is for NB01–NB03. The defect here is
narrower and localized to BHTF: the source's your-turn prompt reads "I
want to this skill should be used when completing lbo (leveraged buyout)
model templates. Read the lbo-model skill..." — a batch script evidently
substituted the skill's own frontmatter description directly into the "I
want to ___" task slot instead of a real task, producing broken grammar
(confirmed against the source dir's `PEDAGOGY.md`, which logs only
"Batch build — skill teardown format", and the source sheet's
`source_skill` path, which does not exist on this machine, so the
specific intended task cannot be recovered). Filled with a generic,
plausible, paste-ready task ("I want to fill in an LBO model template for
a leveraged buyout deal") consistent with the source's generic,
no-setup-required intent, rather than inventing unverifiable lbo-model-
specific mechanics. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03's Teardown framing compressed into NB03; BVDT
folded into BCRY; BHTF kept, with its broken clause filled per above;
BOUT kept, re-skinned. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`financial-services--claude-liam-comps-analysis` sibling, adapted with
lbo-model-specific labels. Chip wording was chosen from the start to
avoid that sibling's two known Manim/Pango word-space-collapse triggers
("Steps" or "nothing" as a chip label's first word) — used "the Steps"
rather than "Steps section", and no chip begins with "nothing" — so no
mid-build rename was needed here.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; B00 actual duration 11.09s). Manim beats (NB01–NB03) rendered
via `render_scenes.py` (foreground, completed within the timeout). Remotion
beats (B00/BCRY/BHTF/BOUT) rendered via `remotion_scenes.py` (foreground,
completed within the timeout) — all four extended to their measured audio
duration by the script's freeze-extend step.

**B00 TIMING LAW: verified by frame pull, no defect found.** media/B00.mp4
actual duration 11.1s (≥8s floor, comfortable margin). Frame pulls at
t≈2s ("When Claude runs / the LBO model skill," settled, caret blinking
mid-line), t≈5s (mid-typing, "design" fully typed and visibly terracotta,
about to be deleted), and t≈9.5s (full corrected question "When Claude
runs the LBO model skill, does it fill the model?" settled and legible,
held for the remaining ~1.6s of runtime) confirm the correction lands on
screen well before the clip ends. Parameters copied directly from the
proven-working fix on the `financial-services--claude-liam-comps-analysis`
sibling (42 ms/char, 8% hesitateBetween, 4% mistakeRate) rather than
re-deriving fresh values.

`type_check.py` (GATE T) ran **PASS, 0 FAILs, on the first pass** — no
defect found or fixed this build (unlike the comps-analysis sibling's
min-size + word-space-collapse fixes, which this build's chip wording
avoided proactively per the note above).

Compiled once:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `financial-services--claude-liam-lbo-model.mp4`, 7/7 beats filled
real (no slate), 86.0s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs, first pass
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -3.1 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 86.0s; mp4
  mtime (1788325492) newer than beat_sheet.json mtime (1788325360)
- Gate V (visual): pulled frames across the full runtime (B00 at t≈5.5s;
  NB01 "A SKILL IS A FOLDER" chips at t≈17.5s; NB02 "STEPS, IN ORDER" chips
  at t≈30s — no word-space collapse; NB03 "FILLS, VALIDATES, FORMATS" 4-chip
  row at t≈40s, correct accent on "any template"; BCRY carry-out quote +
  sparkline at t≈55s; BHTF correct topic/title/@HumanitariansAI handle and
  legible, grammatical paste-ready prompt at t≈68s; BOUT correct eyebrow
  "LBO MODEL · @HumanitariansAI" and title restate at t≈83s). No blockers
  found — no re-render needed.
- B00 TIMING LAW: `actual_duration_s` 11.1s (≥8s requirement met); the
  "design" → "fill" correction is visible mid-typing by t≈5s and fully
  settled, legible, by t≈9.5s, well before the clip ends.

Metadata file written: `financial-services--claude-liam-lbo-model.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`financial-services`) matches no
map prefix (checked in order: no `financial-services`-prefixed key
exists), so per the fallback rule the skill value `hai-simple` was matched
against the map instead, hitting the `"hai-simple"` key directly →
"Claude Basics" — same result as the `financial-services--claude-liam-
comps-analysis` sibling. Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `financial-services--claude-liam-lbo-model-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/financial-services--claude-liam-lbo-model/` (4K master +
description) for the Drive sync. Committed to
`claude-bear/financial-services--claude-liam-lbo-model/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `e771a264`, pushed
clean (no rebase conflicts).

**Status: DELIVERED.**
