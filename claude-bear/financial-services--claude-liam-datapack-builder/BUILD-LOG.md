# BUILD-LOG — financial-services--claude-liam-datapack-builder

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-datapack-builder/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `datapack-builder`
financial-services CIM/filings-ingest Skill, already fully built — no
SCRIPT.md; source `beats[*].narration_text` served as the locked script).
Built entirely fresh this invocation — only SUBJECT.json existed on
pickup. Same source shape as the `financial-services--claude-liam-
cim-builder` sibling (built earlier the same day) — used as the direct
structural template.

Question, facts, and full body argument carried over unchanged:
datapack-builder builds financial services data packs from CIMs, offering
memorandums, SEC filings, web search, or MCP servers, extracting,
normalizing, and standardizing the data into investment-committee-ready
Excel workbooks with consistent structure, proper formatting, and
documented assumptions, for M&A due diligence, private equity analysis,
investment committee materials, and standardizing reporting across
portfolio companies — explicitly not for simple financial calculations or
for reworking an already-completed data pack; a skill is a folder Claude
reads before it works, and the SKILL.md inside is the full instruction
set, in plain language, with no hidden logic; the instructions live in a
Steps section that Claude executes linearly, in order, with no branching
unless a step says so; and the skill's limit is that it only does what
those steps specify — same input, same output, every run. The
`source_skill` path it names does not exist on this machine (different
machine's home directory), but the source beat_sheet.json's own narration
already stated the skill's scope in enough detail to redo faithfully — no
reconstruction needed (see QUESTION.md).

**The call:** register re-registered Teardown → Plain. Source's B03 framed
the skill's scope as a "design tell" verdict ("what it gets right" / "what
it bites") — Teardown judgment language — removed; NB03 states only the
mechanism (a fixed spec, executed the same way every run) and its plain
consequence (nothing outside the spec is in scope, including the
calculations themselves), never a verdict on the skill's design. B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW: "calculate" → "extract" — the
newcomer's wrong guess that the skill runs the financial analysis itself
the way an analyst would, corrected toward the actual mechanism: it
extracts and standardizes data from your sources into a workbook. This
correction is directly grounded in the source's own explicit scope line
("do not use for simple financial calculations").

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design-tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat — the source's Teardown shape carries no
separate wrong-guess or anchor beat to redistribute, and like the
`cim-builder` sibling, this source's body is thin enough, and stays on one
running example throughout, that no separate anchor beat was invented
either); B01→NB01, B02→NB02 kept as one beat each; B03's design-tell
framing compressed into NB03 as a plain mechanism-and-scope statement;
BVDT's verdict facts folded into the single BCRY carry-out sentence per
CARRY-OUT LAW rather than kept as a separate bulleted artifact card; BHTF
kept, with the source's prompt carried over (de-truncated — the source
narration cut the phrase to "from various sources including .", restored
here to a concrete, paste-ready example: a CIM, an offering memorandum, and
SEC filings, for an investment committee review); BOUT kept, re-skinned to
the Humanitarians AI outro (`OutroSeries`, one beat, not split into
OutroSeries + OutroCTA, to hold the source's exact count). Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact` / `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`), copied verbatim from the
`financial-services--claude-liam-cim-builder` sibling, adapted with
datapack-builder-specific labels and chip content.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, local, `am_onyx`. Clean on
   the first pass, no regeneration needed. Durations: B00 12.91s, NB01
   13.16s, NB02 8.38s, NB03 25.96s, BCRY 7.25s, BHTF 19.80s, BOUT 4.59s
   (+1.0s tail).
2. `render_scenes.py` — all 3 Manim scenes rendered clean on the first
   pass.
3. `remotion_scenes.py` (foreground) — all 4 Remotion beats
   (B00/BCRY/BHTF/BOUT) rendered clean on the first pass. The call exceeded
   the tool's 120s timeout and was moved to background by the harness
   automatically; blocked on it via `TaskOutput` before proceeding, per the
   COMPLETION LAW's foreground-render rule — never treated the backgrounded
   render as "handled" without waiting on its exit code.
4. **B00 TIMING LAW verified by frame pull, not just duration**: media/B00.mp4
   is 12.9s (clears the ≥8s floor with margin). Pulled a frame at t=4.5s —
   "calculate" sits mid-correction in terracotta with the cursor — and at
   t=11.5s — the full corrected question "Does the datapack-builder skill
   extract my financials?" is settled and legible with real margin before
   the clip ends. No timing defect; no B00 re-render needed.
5. First `compile.py --force` → 7/7 beats filled real, GATE AUDIO PASS
   -24.1 dB, 93.0s, 3840×2160 native 4K.
6. `type_check.py` (GATE T) → **FAIL, 1 pixel-beat FAIL**: NB03's
   min-size §8.1 check flagged a 19px text-run (floor 20px at 1080p
   logical, the beat clip's native pre-upscale resolution) — root-caused
   by calling `check_min_size`/`text_run_bboxes` directly against the
   flagged frame: the isolated blob was the "wo" pair inside the "one
   workbook" chip label, an x-height-only letter run (no ascenders/
   descenders) that happened to render 1px under floor at EB Garamond
   font_size 26. Fixed by renaming the chip label "one workbook" →
   "one file" (verified the fix directly via `check_min_size` before
   burning another full compile cycle: 21px, PASS). Re-rendered NB03,
   recompiled, re-ran GATE T → **PASS, 0 FAILs**.
7. Gate V (visual, manual): pulled 21 frames across the full 93.0s runtime
   plus the two targeted B00 timing-check frames. Two frames (t=8.0s,
   t=26.1s, t=40.0s) initially looked blank using a fast `-ss <t> -i`
   seek — re-extracted with frame-accurate `-i <file> -ss <t>` ordering
   and confirmed real content underneath (an ffmpeg keyframe-seek
   artifact, not a rendering defect; not logged as a finding). All other
   frames read clean: B00's correction reads with margin; NB01–NB03's chip
   rows are legible, correctly labeled, one accent moment each
   (SKILL.md → plain language → **the program**; Steps section → in order
   → **linear**; filings in → one file → **not the math**); BCRY's
   carry-out quote and sparkline read clean; BHTF's composer card shows
   the correct topic/title/@HumanitariansAI handle and the full
   paste-ready prompt; BOUT's title restate is legible. No blockers found.
8. Audio presence: `ffmpeg -af volumedetect` on the final master → mean
   volume **-24.1 dB**, max -2.8 dB. `ffprobe` confirms h264 3840×2160
   video + aac audio present. Master mtime (1788279693) is newer than
   beat_sheet.json mtime (1788279594).

**Noted, not a defect introduced here:** `OutroSeries` renders on flat
white rather than the humanitarians cream ground in BOUT — same
shared-component behavior already logged unremarked for the
`cim-builder`/`bond-relative-value` siblings. Not fixed here, per the same
precedent.

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (1 real defect found and fixed: NB03 chip label
  "one workbook" → "one file", an x-height-glyph-run min-size false
  boundary, not a design defect)
- Gate V: PASS — no blockers found (two ffmpeg fast-seek false-blank
  frames identified and re-verified as non-issues)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 93.0s; mp4
  mtime newer than beat_sheet.json mtime
- B00 TIMING LAW: `actual_duration_s` 12.9s (≥8s requirement met with
  margin); the "calculate" → "extract" correction lands on screen by
  t≈11.5s with margin

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to the `hai-simple` skill-key literal match,
resolving to **Claude Basics** — same resolution as every other
`financial-services--*` sibling in this family.

Metadata file written: `financial-services--claude-liam-datapack-builder.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
