# BUILD-LOG — healthcare--claude-liam-fhir-developer-skill

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/healthcare/youtube/claude-liam-fhir-developer-skill/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic
`fhir-developer-skill` Claude Skill, from the `healthcare` book's plugin
set; already fully built, no SCRIPT.md — source `beats[*].narration_text`
plus its `AUDIT.md`/`REBUILD-LOG.md`/`LENS-AUDIT.md` served as the locked
script/facts). Built entirely fresh this invocation — only SUBJECT.json
existed on pickup.

Question, facts, and full body argument carried over: a skill is a folder
Claude reads before it works, containing SKILL.md (plain language, no
hidden logic) plus `references/` and `scripts/` — three items total; the
skill's pipeline lives in SKILL.md's Steps section and runs linearly (read
a step, execute it, return the result — no branching unless a step itself
says so); the skill's job is to validate FHIR resources and return the
exact HTTP status code for what's wrong (422 for an invalid enum value,
412 for an ETag mismatch on a conditional update); the status code is the
spec, so the same input produces the same code every run. B00 replaced the
source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "pass-fail" → "the exact code" —
the newcomer's wrong guess that a validator has one binary outcome, gate
through or reject, corrected toward the actual mechanism: every rejection
carries a specific code for a specific reason). Register re-registered
Teardown → Plain: the source's B03 "gets it right: repeatable results /
what it bites: anything outside the spec" framing was restated in NB03 as
a plain mechanism-and-boundary fact, per the NO JUDGMENT register check.
BHTF's prompt was adapted, not copied verbatim: the source asked the
viewer to "read the fhir-developer-skill skill," which requires a plugin
install a general viewer won't have, so this redo substitutes an
equivalent, actually paste-ready prompt exercising the same
specific-reason-not-pass/fail discipline on any schema-validation task.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

**No content correction needed against the source** (unlike the
`healthcare--claude-liam-clinical-note-extract-skill` sibling built earlier
today): this source's own `AUDIT.md` records every Phase-1 accuracy check
as PASS, with no open accuracy note, so all facts were carried over as
documented.

**Beat count:** source is 6 beats (B00 composer-ask + B01 anatomy + B02
pipeline + B03 teardown design-tell + BHTF your-turn + BOUT outro) — no
BVDT verdict beat; the source's own REBUILD-LOG.md records BVDT was
already stripped at build time (body < 5 beats / < 180 words, below the
verdict threshold). This redo is 7 beats: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03's Teardown framing compressed into NB03 (a
plain mechanism-and-boundary fact); BHTF kept (prompt adapted, see above);
BOUT kept. The one net addition versus the source is **BCRY**, the
carry-out beat, mandated by simple's CARRY-OUT LAW (a Plain-register hard
requirement for a single, separately-held carry-out sentence beat) — a
structural requirement of the format, not new invented content, since the
source satisfied its own format's close via BVDT before that beat was
stripped for brevity. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim (mechanism,
colors, GATE T exemption notes) from the
`healthcare--claude-liam-clinical-note-extract-skill` sibling (itself from
`financial-services--claude-liam-kyc-rules`), adapted with
fhir-developer-skill-specific labels. NB03's three chips
("422-invalid-enum", "412-etag-mismatch", "code-is-the-spec") were written
pre-hyphenated from the start, applying the `clinical-note-extract-skill`
sibling's own Gate V lesson (bold EB Garamond multi-word chip labels glue
into unreadable strings in this Manim/Cairo path) proactively rather than
discovering it again.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 4-line text) reused directly from the
`financial-services--claude-liam-kyc-rules` /
`healthcare--claude-liam-clinical-note-extract-skill` siblings' proven
working configuration. `actual_duration_s` (narration) 11.41s + `lead_silence_s`
1.0 gave the writer a 12.41s window; rendered clip extended to 11.4s,
comfortably clearing the ≥8s TIMING LAW floor. Verified by frame pulls at
t=2.0s ("pass-fail" doomed in terracotta, mid-type), t=5.0s (mid-correction,
"the exact code on" typing in), t=9.0s and t=11.0s (full corrected question
"Does Claude just return the exact code on a bad FHIR request?" settled
and legible, holding to the end of the clip) — correction lands and
settles well inside the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00); NB01–NB03 rendered via `render_scenes.py`
(foreground, manim); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground) — all four beats returned `ok` in a single synchronous run,
well inside the tool timeout this time.

**Gate V:** pulled frames at t=3/8/15/22/30/38/45/52/60/68/75/82/88s
across the full runtime plus the targeted B00 correction-timing checks
above. No blockers on first pass. B00 (writer, correction visible and
settled, "@HumanitariansAI" overlay present per hai's channel-title law),
NB01/NB02/NB03 (all chips legible, arrows and captions clean, no overlap —
no word-glue repeat of the sibling's caught bug thanks to the
pre-hyphenated labels), BCRY (carry-out quote + sparkline "Not pass-fail.
The exact code." read clean), BHTF (correct topic "FHIR-DEVELOPER-SKILL ·
HTTP STATUS CODE SPECIFICATION", correct title "It Doesn't Just Pass or
Fail. It Names the Problem.", @HumanitariansAI folder label, paste-ready
prompt legible), BOUT (OutroSeries: correct eyebrow/title restate,
crimson underline, no truncation).

Compiled:
```
python3 runtime/scripts/compile.py <REEL_DIR>
```
Result: `healthcare--claude-liam-fhir-developer-skill.mp4`, 7/7 beats
filled real (no slate), 91.4s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (`type_check.py`): PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: video 3840×2160 h264, audio present, duration 91.4s; mp4 mtime
  (1788344535) newer than beat_sheet.json mtime (1788344406)
- Gate V (visual): PASS, no blockers (see above)

Metadata file written:
`healthcare--claude-liam-fhir-developer-skill.md` (channel
@HumanitariansAI, **Playlist: Claude Basics**). Per `playlists.json`,
SUBJECT.json's family (`healthcare`) matches no specific vertical prefix
in the map (no `healthcare-`/`fhir-` entry exists), so resolution falls
through in map order to the `hai-simple` key itself (present in the map
precisely as this general fallback), which resolves to "Claude Basics" —
reached before `_default` ("Claude Across the Curriculum") is ever
considered, matching the disposition of both the
`financial-services--claude-liam-kyc-rules` and
`healthcare--claude-liam-clinical-note-extract-skill` siblings exactly.
Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `healthcare--claude-liam-fhir-developer-skill-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/healthcare--claude-liam-fhir-developer-skill/` (4K master
+ description) for the Drive sync. Committed to
`claude-bear/healthcare--claude-liam-fhir-developer-skill/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `6b3b1b5c`, pushed clean
(no rebase conflicts, branch up to date with origin/main).

**Status: DELIVERED.**
