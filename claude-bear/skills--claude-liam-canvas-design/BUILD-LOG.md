# BUILD-LOG — skills--claude-liam-canvas-design

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/skills/youtube/claude-liam-canvas-design/beat_sheet.json` (a
Teardown skill-teardown walkthrough of the Anthropic `canvas-design` Skill,
already fully built — no SCRIPT.md; source `beats[*].narration_text` plus
its PEDAGOGY.md/SOURCES.md served as the locked script and verbatim-quote
record). Built entirely fresh this invocation — only SUBJECT.json existed
on pickup.

Question, facts, and full body argument carried over unchanged: canvas-design
is a two-step pipeline in one skill file — step one, Claude writes a design
philosophy naming an aesthetic movement (e.g. Geometric Silence) across four
to six paragraphs covering form/space/color/composition; step two, Claude
reads that philosophy back and generates the canvas itself, a single PDF or
PNG page aimed at museum/magazine quality, with no revision loop on the
brief (the skill's own "coffee table book" framing); the philosophy names
five visual dimensions (space and form, color and material, scale and
rhythm, composition and balance, visual hierarchy) plus a repeated
craftsmanship mandate; the canvas output for Geometric Silence specifically
is grid-based, negative-space-heavy, minimal-type, described by the skill
as "Swiss formalism meets Brutalist material honesty"; and the skill's
final step opens with a pre-written line — "The user ALREADY said it isn't
perfect enough" — so a refinement pass runs on every canvas regardless of
actual quality. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold
open with `BrutalistHesitantWriter` (WRITER LAW: "immediately" → "eventually"
— the newcomer's wrong guess that asking Claude for a poster returns a
picture right away, corrected toward the actual mechanism: a picture does
come back, but only after Claude writes a design philosophy first). Register
re-registered Teardown→Plain: source's B05 "ultimate design freedom" +
"pre-approves the human's critique" Teardown analysis was compressed to the
single most teachable, general-audience fact (NB05: the final-step critique
line is pre-written into the skill and always runs) rather than kept as a
"gets it right / where it bites" evaluative pairing, per the NO JUDGMENT
register check. BVDT's verdict facts (two-act ordering + the pre-baked
critique) were merged into the single BCRY carry-out sentence rather than
kept as a separate bulleted artifact card, per CARRY-OUT LAW. Close
re-skinned to @HumanitariansAI (`OutroSeries`), with a new title
("Philosophy Before Canvas.") reflecting the carry-out rather than the
source's bare topic title.

**Beat count discipline:** source is 9 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03/B04 self-demo philosophy/canvas + B05 teardown design
tell + BVDT verdict + BHTF your-turn + BOUT outro). This redo kept the same
9-beat shape: B00 carries the wrong-guess pedagogy per WRITER LAW instead of
a dedicated beat; B01→NB01, B02→NB02, B03→NB03, B04→NB04 kept as one beat
each; B05's Teardown framing compressed into NB05 (the single fact a general
viewer needs and can act on); BVDT folded into BCRY; BHTF kept, with the
source's already-generic, already-runnable prompt ("I have a concept for a
poster — a meditation retreat in the mountains...") carried over unchanged;
BOUT kept, re-skinned. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`CanvasDesignAnatomy` / `CanvasDesignPipeline` / `CanvasDesignPhilosophy` /
`CanvasDesignCanvas` / `CanvasDesignTell` / `ClaudeVerdictArtifact`), so
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00's mandated
cold-open swap. Source's own SOURCES.md declares its B04 (the rendered
Geometric Silence canvas) a SELF-DEMO — a Remotion demonstration of the
philosophy's stated visual principles, not a screenshot of actual skill
output; this redo's NB04 narration preserves that same boundary (states the
philosophy's stated visual principles, never claims to show captured skill
output), so no inference flag is needed there either (see SCRIPT.md
One-flag audit).

All 5 GRAPHIC beats (NB01–NB05) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with canvas-design-specific labels.

**GATE T — one real defect caught and fixed, not a QC-sampling trap.** First
`type_check.py` pass was **FAIL, 1 defect**: NB05's smallest text-run
measured 19px, 1px under the 20px §8.1 floor. Root cause investigated by
direct measurement (a standalone script computing each NB05 chip's Manim
`Text` bounding box at the same font/weight/box parameters used in
production) rather than guessed: all three NB05 chip labels rendered at
`scale=1.0` (no width/height compression triggered at all), meaning the
smallest-run failure came from the base font-size tier itself, not from
per-label text-shortening headroom the way earlier siblings' fixes worked —
so the fix here was raising `scenes.py`'s shared font-size tiers (26/22/18
→ 29/24/19 px-equivalent) rather than rewording a chip label, since the
labels were already short (≤14 chars) and well under their box's width
constraint. Re-rendered all 5 NB01–NB05 beats (the shared tier change
affects every chip-row beat, not just NB05) and recompiled. `type_check.py`
went 1→**PASS, 0 FAILs**.

Audio generated fresh (`generate_audio_kokoro.py`, all 9 beats, free/local,
`am_onyx`, clean first pass, $0.00); `remotion_scenes.py` (4 beats) exceeded
the tool's 120s default foreground timeout and was auto-backgrounded by the
harness — blocked on it via `TaskOutput(block=true)` before proceeding, per
the COMPLETION LAW's foreground-render rule, never treating a backgrounded
render as "handled" without waiting on its real exit code (confirmed exit
0, all 4 beats OK). `render_scenes.py` (5 Manim beats) ran to completion in
the foreground within the tool timeout on both the first pass and the
post-fix re-render. `compile.py` (both the first compile and the post-fix
`--force` recompile) also exceeded the 120s foreground timeout and was
auto-backgrounded each time — both blocked to real completion via
`TaskOutput(block=true)` before proceeding.

Compiled:
```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```
Result: `skills--claude-liam-canvas-design.mp4`, 9/9 beats filled real (no
slate), 163.9s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (9 beats, no violations)
- frame-check: PASS (3840×2160, 9 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO (compile.py): PASS — mean_volume -23.9 dB
- Independent ffprobe/ffmpeg verification (not just compile.py's own
  summary line): video h264 3840×2160, audio aac present, duration
  163.833–163.938s; `ffmpeg -af volumedetect` mean_volume **-23.9 dB**, max
  -2.9 dB (both well clear of the -40 dB floor); mp4 mtime (1788534214)
  newer than beat_sheet.json mtime (1788533682).
- Gate V (visual): pulled frames at 2fps across the full runtime plus
  targeted checks — B00 (t≈2.9s "immediately" doomed in terracotta mid-
  delete, t≈6.0s still mid-correction, t≈10.0s fully corrected question
  "Does asking Claude for a poster return a picture eventually?" settled
  and legible), NB01 ("TWO STEPS, ONE SKILL" — philosophy→canvas→poster
  chips, accent underline on "canvas," caption legible), NB02 ("LINEAR, NO
  LOOPS" — request→philosophy.md→canvas.pdf, accent on "canvas.pdf"),
  NB03 ("FIVE DIMENSIONS, NAMED" — all three chips legible post font-size
  fix, "craftsmanship" bold+underlined), NB04 ("90% VISUAL, 10% TEXT" —
  grid/negative space/minimal type, all legible), NB05 ("THE FINAL STEP
  RUNS FIRST" — all three chips legible post fix, no truncation), BCRY
  (carry-out sentence + sparkline read clean, correct italic serif
  treatment), BHTF (correct topic "CANVAS DESIGN · ANTHROPIC SKILL",
  correct segment "Philosophy Before Canvas.", correct @HumanitariansAI
  handle, paste-ready prompt text legible), and BOUT (OutroSeries: correct
  eyebrow "CANVAS DESIGN · @HumanitariansAI", correct title restate,
  crimson underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 11.07s (≥8s requirement met, ≥9s
  window also met); the "immediately"→"eventually" correction begins by
  t≈2.9s and the full corrected question is settled and legible from
  t≈10.0s through the end of the 11.1s clip.

**Advisory (not a gate, logged for honesty):** `compile.py` printed a
motion-mix WARNING — `'graphic' carries 5/9 beats (55%) — over the ~40%
pantry cap` (MOTION.md) — because all 5 body beats (NB01–NB05) are
GRAPHIC/Manim rather than a REMOTION/GRAPHIC mix. This is advisory only:
content-check, frame-check, lane-check, GATE T, and GATE AUDIO all PASS,
and none of hai-simple's SKILL.md gates name a motion-mix cap as blocking.
The ratio follows directly from preserving the source's 9-beat shape and
its 5 distinct body facts (two-step pipeline, linear no-loop shape, five
philosophy dimensions, the canvas output, the pre-written final step) as
5 separate beats, per the redo contract's beat-count-preservation mandate;
converting one to REMOTION would have meant either dropping a source fact
or inventing a new registered component outside GATE L's library-first
scope. Logged rather than silently accepted.

Metadata file written: `skills--claude-liam-canvas-design.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). SUBJECT.json's `family` is `"skills"`, which has no literal
prefix match in `playlists.json` (every map key — `claude-skills`,
`claude-agent-skills`, `claude-plugins`, etc. — is longer than the string
`"skills"` itself, so no `"skills".startswith(key)` check can succeed; the
skill-key fallback `hai-simple`→"Claude Basics" would misfile a reel whose
actual subject is an Anthropic Agent Skill's two-step pipeline and design
philosophy). Same override already established by the
`skills--claude-liam-brand-guidelines` sibling (built earlier the same day,
same `family: "skills"` value, same reasoning logged in its own BUILD-LOG):
resolved directly to the map's `claude-skills`/`claude-agent-skills`
semantic bucket by content match rather than falling through to the
generic default, since "the bare Claude" default is explicitly disallowed
and "Claude Basics" is a worse content fit than the skills/plugins
playlist for a reel about a named Anthropic Skill's internal mechanism.
Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-04 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `skills--claude-liam-canvas-design-4k.mp4` rather than
re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/skills--claude-liam-canvas-design/` (4K master + description)
for the Drive sync. Committed to
`claude-bear/skills--claude-liam-canvas-design/` (README.md = description,
beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md, QUESTION.md,
BUILD-LOG.md — no mp3/mp4) as commit `4a701cb9`, pushed clean (no rebase
conflicts).

**Status: DELIVERED.**
