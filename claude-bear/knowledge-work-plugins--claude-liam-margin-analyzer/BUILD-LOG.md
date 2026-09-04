# BUILD-LOG — knowledge-work-plugins--claude-liam-margin-analyzer

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-margin-analyzer/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the `margin-analyzer` Skill,
already fully built — no SCRIPT.md; source `beats[*].narration_text` plus
PEDAGOGY.md served as the locked script). Built entirely fresh this
invocation — only SUBJECT.json existed on pickup.

**Source-facts gap (read before trusting "facts carried over unchanged"):**
the source's `source_skill` path
(`.../knowledge-work-plugins/small-business/skills/margin-analyzer/SKILL.md`)
does not exist anywhere in this workspace — confirmed by `find` across the
whole `books/` tree and across `anthropics/knowledge-work-plugins/`. Worse,
the source's OWN narration and Remotion props never got the skill's
specific task description filled in: five of its seven beats carry a
literal un-substituted `>` placeholder exactly where that description
belongs (B00, B03, BVDT, and BHTF's "I want to >."). Comparing against
sibling batch reels (`forecast`, `crm-cleanup`), which DO have their
descriptions filled in, confirms this is a template-substitution defect
specific to this one source, not a stylistic choice — and the toolkit's
own audit (`anthropics/_audit/audit_results.csv`) already flags this exact
sheet `no-TYPECHECK;no-FACTCHECK`.

Everything else in the source is generic and fully usable, and IS carried
over unchanged: "a skill is a folder Claude reads before it works," "the
pipeline is in a Steps section, executed in order, no branching unless a
step says so," "same input, same output, every run," "the limit is only
what the file says." The one specific fact the source never supplies —
what margin-analyzer actually checks — is not invented outright: per
hai-simple PHASE 1 ("when in doubt, describe behavior generically"), NB01
names it as an inference from the skill's name and its `small-business`
category only ("built, going by its name, for a small business checking
its profit margins"), flagged once (ONE-FLAG LAW, at NB01) and not
asserted as confirmed fact anywhere else in the reel. Full reasoning in
SCRIPT.md's "Source-facts note."

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "invent" → "follow" — the
newcomer's wrong guess that Claude improvises a fresh method each run,
corrected toward the actual model: it follows a written plan). Register
re-registered Teardown → Plain: the source's B03/BVDT "gets it right /
what it bites" framing was merged into a single NB03 beat stating both
directions (repeatable, and limited) as plain mechanism-and-consequence,
per the NO JUDGMENT register check. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design-tell + BVDT verdict + BHTF your-turn + BOUT
outro) — the same shape as the `claude-tag-plugins--claude-liam-config-guide`
sibling's source, so this redo followed that precedent exactly: B00
carries the wrong-guess pedagogy per WRITER LAW instead of a dedicated
beat; B01→NB01, B02→NB02 kept as one beat each; B03+BVDT (both built
around the same missing task-specific placeholder) merged into the single
NB03; BHTF kept, with the source's instruction to "read the margin-analyzer
skill" (a non-public internal skill the viewer cannot actually run)
replaced by a concrete, paste-ready prompt that needs no special access;
BOUT kept. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching
the source exactly. Full audit in SCRIPT.md's "Beat-count note (redo)".

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-tag-plugins--claude-liam-config-guide` sibling. B00 hesitant-writer
correction ("invent" → "follow") verified on screen by direct frame pulls:
"invent" typed and visible in terracotta (about to be deleted) by t≈2s,
mid-correction ("Does Claude / follow a pl|") by t≈5s, settled correct
text "Does Claude follow a plan for my margins?" by t≈8.5s — full clip
9.2s (≥8s TIMING LAW window met).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground). First invocation of `remotion_scenes.py` exceeded the 120s
tool default and was killed by the harness at 2 minutes (exit 143) before
its B00 render reached the ffmpeg conform-to-duration post-step, leaving
an un-conformed 606-frame/20.2s raw render (`BrutalistHesitantWriter`'s
fixed Root.tsx `durationInFrames`) in place instead of the 9.2s clip
matched to the narration. Diagnosed by probing the stray B00.mp4 duration
against the composition's Root.tsx registration, not just trusting the
"filled already (skip)" log line. Fixed per the COMPLETION LAW's
foreground-render rule: re-ran `remotion_scenes.py --only B00 --force`
in the foreground with a longer timeout, which completed the conform step
cleanly (9.2s). All subsequent invocations (batch remotion render,
`render_scenes.py` for Manim, both `compile.py` passes) were run to
completion in the foreground.

NB01–NB03 rendered via `render_scenes.py`. First `type_check.py` pass was
**FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB03** — smallest text run 14px < floor 20px. The
  original third chip label "nothing outside the plan" (25 chars) forced
  the uniform scale-to-fit logic to shrink it below the floor inside the
  3.2-unit-wide chip. First fix attempt (rename to "not covered", 11
  chars) reduced the defect (14px → 16px) but did not clear it — the
  *first* chip, "same steps every run" (21 chars), was now the binding
  constraint at the same font-size tier as its 18-char neighbor, so its
  greater length forced extra scale-down. Root fix, matching the
  `config-guide` sibling's precedent exactly (make all three chips
  roughly equal, short length so none has to fight its neighbors' shared
  font-size tier): renamed all three chips to `["same steps",
  "repeatable", "not covered"]` (10/10/11 chars). Re-rendered NB03 only
  (NB01/NB02 untouched); `beat_sheet.json`'s
  `graphic.production_viz.chips` for NB03 synced to match at each step,
  before recompiling — no post-compile sheet edits left unreconciled.

`type_check.py` went FAIL → **PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-margin-analyzer.mp4`, 7/7
beats filled real (no slate), 80.7s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe (self-verified, not just trusted from compile.py's log): video
  3840×2160 h264, audio (aac) present, duration 80.7s; mp4 mtime
  (1788511117) newer than beat_sheet.json mtime (1788511035)
- Gate V (visual): pulled frames every 8s across the full runtime plus
  targeted checks — B00 (t≈2s "invent" doomed in terracotta, t≈5s
  mid-correction "Does Claude / follow a pl|", settled correct by t≈8.5s),
  NB01 ("A SKILL IS A FOLDER", SKILL.md/reference chips legible,
  SKILL.md accented), NB02 ("STEPS, IN ORDER", three chips + arrows +
  caption legible), NB03 (post-fix: all three chips legible and
  parallel-sized, "not covered" accent underline clean), BCRY (carry-out
  sentence and sparkLine footer read clean), BHTF (correct topic/title/
  @HumanitariansAI handle, paste-ready prompt text legible), and BOUT
  (`OutroSeries`: correct eyebrow "MARGIN-ANALYZER · @HumanitariansAI",
  correct title restate "A Plan, Not a Guess."). No blockers.
- **Noted, not a blocker:** `OutroSeries` renders on a flat WHITE ground
  with a CRIMSON-red underline (hardcoded VOX teardown tokens in
  `OutroSeries.tsx`/`tokens/vox.ts`), not the humanitarians CREAM/
  burnt-orange palette used everywhere else in this reel. Verified this is
  the component's existing, already-accepted behavior — not a regression
  introduced here — by pulling the equivalent frame from the delivered
  `config-guide` sibling's `media/BOUT.mp4`: identical white ground,
  identical crimson underline, and that sibling's own BUILD-LOG.md Gate V
  entry describes it matter-of-factly ("crimson underline") without
  treating it as a defect. `OutroSeries`/`OutroCTA` take no color props
  (they import `VOX` directly), so no per-reel prop fix is available; a
  real fix is a component change out of scope for this one-shot build.
  Logging here so the pattern is visible across reels, not fixing it
  unilaterally mid-factory-run.
- B00 TIMING LAW: `actual_duration_s` 9.19s (≥8s requirement met); the
  "invent" → "follow" correction lands on screen by t≈8.5s, well inside
  the clip.

Metadata file written:
`knowledge-work-plugins--claude-liam-margin-analyzer.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `knowledge-work-plugins` key
directly (no fallback needed). Direct code link per DELIVERY CONTRACT
format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-04 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `knowledge-work-plugins--claude-liam-margin-analyzer-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-margin-analyzer/` (4K
master + description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-margin-analyzer/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4).

**Status: DELIVERED.**
