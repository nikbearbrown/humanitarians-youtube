# BUILD LOG — hai-simple/knowledge-work-plugins--claude-liam-crm-maintenance

Redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-crm-maintenance` (Teardown
register, 7-beat skill-teardown of an Anthropic skill named `crm-maintenance`) as
`hai-simple` (Plain register, Humanitarians AI skin). Source folder untouched.

## Source defect found on read — total, not partial

The `crm-cleanup` and `call-prep` siblings in this batch each had a template-truncation
bug where a `>`-prefixed skill-description placeholder got cut off mid-sentence in three
of seven beats, but the complete sentence survived intact in each source's own B00. This
source has the same `>` placeholder pattern in B00, B03, BVDT, and BHTF — but here it is
**empty everywhere, including B00**: "The skill is crm-maintenance. >. A SKILL.md tells
Claude exactly how," "Claude's job: >. What it gets right: repeatable results," "The
SKILL.md is the spec — >. Same input, same output," "Paste this into Claude: 'I want to
>. Read the crm-maintenance skill.'" No beat in the source's seven carries the skill's
actual domain-specific description — there is nothing to recover. The `source_skill`
path the source's own metadata points at
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/crm-maintenance/SKILL.md`)
does not exist on this machine; searches of the local `knowledge-work-plugins` clone and
batch logs turned up only build-status rows, never the SKILL.md text. Per the NO-INVENTION
rule, this build states only the anatomy (SKILL.md + reference/), pipeline (Steps section,
linear), and the bounded-spec scope guarantee that the source's readable text actually
supports — never an invented CRM-specific action. Full detail in `QUESTION.md`.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Source's Teardown framing ("what it gets right / what
  it bites," verdict) dropped; B03 states the bounded-spec scope and stops.
- **Cold open:** source's `ClaudeComposerAsk` ask → `BrutalistHesitantWriter`. Writer
  types the newcomer's wrong-guess word "MAINTAIN" (implying Claude tidies the CRM
  continuously, on its own initiative), hesitates, corrects to "check" → lands "Does
  Claude check my CRM by itself?". Picked up directly by B03's stated scope and BCRY's
  carry-out.
- **Beat count:** kept the source's shape in substance (B00 → B01 anatomy → B02 pipeline
  → B03 mechanism → BCRY carry-out → BHTF handoff → BOUT outro), source's single outro
  split into hai-simple's fixed two-part Humanitarians AI outro (`OutroSeries` +
  `OutroCTA`) — 8 beats total, same precedent as this family's other redos.
- **Facts/argument:** unchanged and generalized — anatomy (SKILL.md + reference/,
  2 files), pipeline (Steps section, linear execution), and scope (bounded spec, run once
  per request, same result every time, silent outside the file) reworded only for
  register. No domain-specific CRM action is claimed (see Source defect above).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is new and complete ("Read the crm-maintenance
  skill in this folder. Before you run it, tell me exactly which steps it will execute,
  in order, and tell me plainly if anything I ask falls outside what the file covers.") —
  the source's own handoff was truncated mid-sentence around its own cut-off placeholder.

## NO-GENAI / NO-PANTRY LAW

Every beat is REMOTION (`BrutalistHesitantWriter`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `WantQuote`, `ClaudeComposerAsk`,
`OutroSeries`, `OutroCTA`) — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. `compile.py`'s motion-histogram WARNING (`remotion` 8/8 = 100%, over the
~40% pantry cap) is expected and accepted for the same reason every prior all-REMOTION
sibling in this family logged it: this reel is a file/pipeline/scope explainer, not a
worked-example narrative, and has no illustrative-figure beats to draw as Manim/GRAPHIC.

## Gates

- **TYPECHECK / GATE T:** first pass FAILed — B03's `SkillTeardownMechanism.body` prop
  was 13 words, over the §8.5 12-word pull-quote limit ("One spec-bound routine, run once
  per request — nothing standing in the background."). Fixed to "One spec-bound routine,
  run once per request. Nothing runs in the background." (12 words). Re-run: PASS, 0
  FAILs, all 8 beats.
- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **13.29s**, well clear of the ≥8s/≥9s-window floor. Frame pull at
  t=9s (of 13.29s) confirms the corrected question "Does Claude check my CRM by itself?"
  fully on screen, correction already landed.
- **GATE AUDIO:** PASS, mean_volume **-23.8 dB** (well above the -40 dB floor), max
  -3.0 dB — verified independently via `ffprobe`/`ffmpeg volumedetect` on the compiled
  master.
- **Gate V (frame QC):** sampled frames across B00 (early + late), B01, B02, B03, BCRY,
  BHTF, BOUT, BCTA at full 3840×2160: all legible, correctly kerned, no text overlap,
  safe inset respected, `@HumanitariansAI` handle correct throughout, HAI outro skin
  correct (OutroSeries title restate + OutroCTA subscribe/handle).
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` (8/8 beats, no
  violations).

## Output

`knowledge-work-plugins--claude-liam-crm-maintenance.mp4` — 83.4s, 8/8 beats real (no
slates), native 3840×2160 (compile.py's 4K LAW forces this even without `--review`, since
all beats are Remotion-rendered natively at 4K), audible narration throughout (mean_volume
-23.8 dB, independently verified, mp4 newer than beat_sheet.json). COMPLETION LAW
satisfied.

**Playlist:** Extending Claude — Skills, Plugins & Connectors. `SUBJECT.json`'s
`family: "knowledge-work-plugins"` matches the `knowledge-work-plugins` prefix in
`playlists.json`'s map directly (no fallback needed).

## Phase 4 (4K + delivery)

- **4K master:** the Phase-3 compile already wrote the master natively at 3840×2160.
  Copied it to `knowledge-work-plugins--claude-liam-crm-maintenance-4k.mp4` so
  `deliver.py`'s `newest_master()` picks it as the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/knowledge-work-plugins--claude-liam-crm-maintenance/` (4K master +
  description, syncs to Drive `Claude_Bear/` on this machine's Drive-for-desktop mount);
  repo `humanitarians-youtube/claude-bear/knowledge-work-plugins--claude-liam-crm-maintenance/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md + CARRY-OUT.md +
  QUESTION.md — no media).

**Status: DELIVERED.**
