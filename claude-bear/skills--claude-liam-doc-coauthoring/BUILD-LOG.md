# BUILD-LOG — skills--claude-liam-doc-coauthoring

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/skills/youtube/claude-liam-doc-coauthoring/beat_sheet.json`
(Teardown/claude-explainer + skill-teardown source, already fully built, no
SCRIPT.md — source `beats[*].narration_text` plus SOURCES.md/PEDAGOGY.md
served as the locked script). Question, facts, and full body argument
carried over unchanged: the three-stage doc-coauthoring workflow (Stage 1
context gathering — five meta-questions plus a full context dump, exit
condition = edge cases askable without basics explained; Stage 2 per-section
clarify/brainstorm/curate/gap-check/draft/refine loop with a three-iteration
quality gate and a near-completion slop cut; Stage 3 reader testing with a
context-free fresh Claude, automatic sub-agent in Claude Code vs. manual in
claude.ai). B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "for" → "with" — the newcomer's wrong
guess that this is Claude writing a doc *for* you, corrected to the reel's
real subject, writing *with* you). Register re-registered Teardown→Plain:
the source's B05 "teardown moment" (context-bleed insight, what the skill
gets right / what it costs) and BVDT verdict were the two beats that could
not survive as-is — their factual halves were kept and re-homed as NB08
(what Stage 3 structurally proves) and NB09 (the two real limits: workflow
length, and str-replace/direct-edit fragility), stated as mechanism and
limits rather than a design verdict; BVDT's bullet recap was re-expressed as
BCRY's single carry-out sentence. A new concrete anchor was authored for
this cut (source had none): a technical spec on a payments API that reads
fine to its author because the author already knows what "the settlement
window" means — planted at NB01, paid off at NB07 when the fresh Claude
stalls on the identical undefined term, confirmed visually recurring at
Gate V (the "SETTLEMENT WINDOW" chip is pixel-identical in both beats).
Close re-skinned to `WantQuote` / `ClaudeComposerAsk` / `OutroCTA` with
@HumanitariansAI and Liam's sign-off.

Source's 9-beat claude-explainer+skill-teardown chassis (B00 cold open, B01
anatomy/trigger/doc-types, B02–B04 the three stages, B05 teardown moment,
BVDT verdict, BHTF handoff, BOUT outro) was expanded, not compressed, to
this skill's 13-beat spine (B00, NB01–NB09, BCRY, BHTF, BOUT): B01's
trigger/doc-type anatomy was dropped as its own beat (a taxonomy list has no
payoff in a 2–3 minute Plain cut; the video opens directly on the anchor
scenario instead), but Stage 2 (source's single B03) carried enough
distinct mechanism — the six-step loop, the three-iteration quality gate,
and the near-completion slop cut — to warrant splitting into NB04/NB05 for
one-idea-per-beat pacing rather than compressing it. Full audit in
SCRIPT.md's "Beat-count note (redo)" section. No source beat was
ai-video-prompt, pantry, or a human-drop slot — the source was already
entirely REMOTION (`DocCoauthoringAnatomy`/`Stage1`/`Stage2`/`Stage3`/
`Tell`, all custom Claude-palette components, `beat_id`s B01-B05) — but
those components hardcode `CLAUDE.*` tokens with no palette prop (confirmed
by grep before authoring), so hai-simple's CHANNEL SKIN law (humanitarians
palette throughout the reel, not just B00/outro — confirmed against the
already-built `books--claude-liam-what-plugins-are` sibling, which made the
same call for the same reason) required rebuilding the body as GRAPHIC/manim
chip-row beats in the humanitarians palette rather than reusing the source
components as-is. NO-GENAI/NO-PANTRY LAW required no beat substitution
beyond B00.

All 9 GRAPHIC beats built on one shared generic "chip row" Manim template
(`scenes.py`/`render_scenes.py`, one title + up to 3 labeled chips +
optional arrows/accent/strike + caption, parametrized per beat from a
`BEAT_CONTENT` table) — same pattern as the `books--claude-liam-*` siblings,
copied and adapted rather than re-invented. THE ANCHOR: NB01 ("The spec
reads great — to you" — plants the "SETTLEMENT WINDOW" chip) → NB07 ("The
reader stops here" — the identical "SETTLEMENT WINDOW" chip recurs
alongside "FRESH CLAUDE" and "UNDEFINED"), confirmed visually recurring at
Gate V. B00 hesitant-writer correction ("for" → "with") verified on screen:
final corrected question "Can Claude write my technical doc with me?"
legible by t≈9s, clip duration 10.0s (≥8s TIMING LAW window met with
`lead_silence_s: 0.8`).

Audio generated fresh (`generate_audio_kokoro.py`, all 13 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground; the harness auto-backgrounded both this and the compile step
past their 120s tool timeout — blocked on `TaskOutput` for each before
proceeding, never treated the auto-background as a hand-off); all 9 GRAPHIC
beats rendered via `render_scenes.py`, first pass, no re-renders needed.
`type_check.py` (GATE T): **PASS, 0 FAILs**, first pass — no defect
iteration needed this build. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `skills--claude-liam-doc-coauthoring.mp4`, 13/13 beats filled real
(no slate), 152.3s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (13 beats, no violations)
- frame-check: PASS (3840×2160, 13 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -2.7 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 152.25s; mp4
  mtime (1788537972) newer than beat_sheet.json mtime (1788537843)
- Gate V (visual): pulled 13 frames across the full runtime and read each
  directly — legible everywhere, safe inset respected, no text overlap,
  @HumanitariansAI handle correct on BHTF/BOUT, anchor pair (NB01
  "SETTLEMENT WINDOW" chip → NB07 same chip) visibly recurring as designed.
  One cosmetic observation, not a defect: NB03's accented "EXIT: EDGE CASES"
  chip renders slightly lighter/thinner than the same-beat's other chips at
  a glance (peak ink-pixel sampling confirms the glyph color itself matches
  the other accented chips' ink value — this reads as an anti-aliasing/
  scale artifact from the longer bold label at this chip width, not a color
  or legibility defect; every other accented chip in the reel, including
  the recurring anchor chip, renders at full ink density). Logged per the
  honesty rule rather than silently waved through.
- B00 TIMING LAW: `actual_duration_s` 10.0s (≥8s requirement met); the
  "for" → "with" correction lands on screen by t≈9s.

**Non-blocking warning (compile.py):** motion histogram graphic:9
remotion:4 — graphic at 69%, over the ~40% pantry cap in MOTION.md. This is
structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as REMOTION
against a 9-beat GRAPHIC body — the ratio follows beat count, not a choice
made in this build, same as every other hai-simple sibling with a body this
size. Logged per the honesty rule rather than reworking beat count to dodge
the warning.

Metadata file written: `skills--claude-liam-doc-coauthoring.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per playlists.json, SUBJECT.json's family ("skills") has no
literal map entry, and the skill-name fallback ("hai-simple" → "Claude
Basics") would misfile this — the reel's entire subject is a specific
Anthropic Skill (`doc-coauthoring`), the exact content category the map's
`claude-skills` key already routes to "Extending Claude — Skills, Plugins &
Connectors". Followed that content-matching precedent (already established
and logged on the `books--claude-liam-what-plugins-are` family for an
analogous no-literal-match case) rather than falling through to
`_default` or the skill-name match. Direct code link per DELIVERY CONTRACT
format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
