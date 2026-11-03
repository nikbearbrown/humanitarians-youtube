# BUILD-LOG — healthcare--claude-liam-icd10-cm-skill

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/healthcare/youtube/claude-liam-icd10-cm-skill/beat_sheet.json` — a
fully-built, Teardown-register skill explainer (7 beats, `claude-liam` /
@NikBearBrown, no SCRIPT.md on the source). Its `beats[*].narration_text`
served as the locked narration per the redo contract, same disposition as
the `doc-extract` / `fhir` / `fraud-detection` healthcare siblings in this
same batch (see `HAILOOP-LOG.md`). Never touched the source reel's folder.
Only `SUBJECT.json` was present on pickup; everything else was built fresh
this invocation.

**Facts kept unchanged:** the skill is `icd10-cm-skill`; it extracts billable
ICD-10-CM diagnosis codes from a clinical note "the way a professional coder
builds the claim"; used when a user says "code this encounter," "assign
ICD-10 codes," "what diagnosis codes apply," "code this chart," or turns
clinical documentation into claim-ready diagnosis codes; a skill is a folder
Claude reads before acting, and `SKILL.md` is the full instruction set
(2 files total: `README.md` 1k, `SKILL.md` 8k); the pipeline reads a Steps
section and executes linearly, no branching unless a step says so; same
input produces the same output every run; the limit is only what the
`SKILL.md` specifies. Source's own `AUDIT.md` had already passed every
content/accuracy check (fixing only truncation and a stale model-name
artifact), so no further factual correction was needed against the source.

**Register: Teardown -> Plain.** The source's B03 ("Here is the Teardown
moment... What it gets right: repeatable results. What it bites: anything
outside the spec.") and BVDT ("Verdict"/"Know the limit: only what the file
says") explicitly judge the design's trade-offs. Plain states the identical
constraint as fact (this reel's B03: "Not a diagnosis, not clinical
judgment... ask Claude to decide what's wrong with the patient, and that's
outside the skill") and lands it as the carry-out (BCRY) instead of a
verdict artifact — same fact, judgment removed.

**B00 WRITER LAW:** the natural newcomer misreading of "extract billable
ICD-10-CM diagnosis codes from a clinical note" is that Claude is deciding
what's wrong with the patient — diagnosing, not just coding. That's the same
idea already present in the source's own "bites" clause ("anything outside
the spec" — deciding the diagnosis is outside the spec), restated here as
the wrong guess instead of a verdict. Typed text: "Give Claude a clinical
note / and it diagnoses the patient. / Wait — what does / icd10-cm-skill
actually do?", trigger "diagnoses" -> replacement "codes". B00 audio
measured 10.99s + `lead_silence_s` 0.8 = 11.79s window (TIMING LAW's >=9s
floor cleared with margin), narration 31 words. Verified across four frames
(t=2s, 5s, 8s, 10.5s): at t=2s the writer is still mid-typing the wrong word
("dia|"); by t=5s the correction has fully resolved ("...and it codes the
patient."); by t=10.5s the writer is mid-way through the final corrected
question ("icd10-|") with the beat not yet over — correction and framing
both land inside the beat with margin.

**BVDT -> BCRY:** `ClaudeVerdictArtifact` ("Verdict" artifact card) ->
`WantQuote` (the bare carry-out sentence), matching `simple`'s law that the
verdict-recap position becomes the carry-out line in Plain register. Same
beat slot, same beat count (7 -> 7: B00, B01, B02, B03, BCRY, BHTF, BOUT).
Carry-out: "Coding a diagnosis and making the diagnosis are two different
jobs — icd10-cm-skill only does the first one" — directly resolves B00's
naive framing (confirmed on the BCRY frame pull at t=52s).

**Body beats (B01-B03):** kept the source's own Remotion components
(`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`)
rather than rebuilding as Manim — all three confirmed still registered and
renderable (`./art scenes --check`), and none of the source's beats were
ever `ai-video-prompt`, pantry, or human-drop (NO-GENAI/NO-PANTRY LAW was
already satisfied), so no substitution was owed beyond the two the skill
mandates (B00 writer-open, BOUT HAI-skin). Only the prop text changed:
eyebrow/heading/sparkLine reworded off Teardown language ("DESIGN TELL" ->
"MECHANISM", "the interesting constraint" / verdict framing -> "Just what's
documented, coded." / "Not a diagnosis. Just the code."); B02's
inputLabel/outputLabel changed from generic "YOUR REQUEST"/"RESULT" to
"CLINICAL NOTE"/"BILLABLE CODES" to match this skill's actual I/O, matching
the `doc-extract` sibling's pattern of skill-specific input/output labels.
B03's `body` prop written as a short comma-free phrase ("note in, ICD-10-CM
codes out") from the start, applying the `doc-extract` sibling's own
lesson (avoid separator glyphs / long sentences that trip GATE T §8.5
wordy-card or force auto-shrink into §8.1 min-size) — confirmed no GATE T
issue resulted.

**BHTF:** the source's prompt asked the viewer to "read the icd10-cm-skill
skill," which needs a specific Anthropic healthcare-plugin install a general
viewer won't have — same disposition as the `fhir` / `fraud-detection` /
`clinical-trial-protocol-skill` siblings. Substituted an equivalent
paste-ready exercise needing no install, drilling the exact same boundary
(documented vs. inferred) with a hypothetical, non-patient note: "Here's a
note: chest pain, shortness of breath, history of hypertension, leg swelling
on exam. List every diagnosis that's explicitly written down. Then,
separately, tell me what you'd be tempted to infer — like heart failure —
that you won't code, because it isn't documented." Kept `ClaudeComposerAsk`
with explicit `folderLabel: "@HumanitariansAI"` override (component's
Root.tsx default is `@NikBearBrown`, the same known workaround used across
every sibling redo).

**BOUT:** `ClaudeTitleOutro` (blank subline, `@NikBearBrown`) -> `OutroCTA`
(Humanitarians AI skin, `@HumanitariansAI`), per hai-simple's channel-skin
law.

**Voice:** unchanged — Liam, Kokoro `am_onyx`, "in for Bear." (source already
used this voice; hai-simple's Liam-not-`af_kore` rule needed no change.)

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (7 beats, all REMOTION — no Manim needed). Ran
`generate_audio_kokoro.py` (7/7 beats, am_onyx, $0.00) — measured durations
became the clock. Rendered all 7 Remotion beats via `remotion_scenes.py` —
exceeded the tool's 120s foreground timeout and was moved to background by
the harness automatically; blocked on it via `TaskOutput` (block=true)
before proceeding, per the one-shot COMPLETION LAW's foreground-render rule
— confirmed exit code 0, all 7 beats reporting `ok`.

**GATE T (type_check.py): PASS, 0 FAILs, first pass.** No fixes needed.

Compiled with `compile.py`: 7/7 beats real (no slate), master born natively
4K (3840x2160, `compile.py`'s 4K LAW), 77.6s. `content-check`/`frame-check`/
`lane-check` all PASS. Motion histogram `remotion:7` (100% — structural, not
a defect: this reel's body content is the source's own three Remotion cards,
and hai-simple's mandated bookends — B00/BCRY/BHTF/BOUT — are REMOTION by
skill contract regardless, same disposition as every all-Remotion sibling in
this batch).

**Gate V:** pulled 13 frames across the full 77.6s runtime (t=2, 5, 8, 10.5,
17, 28, 40, 45, 52, 62, 70, 75, 77), read every one directly. B00's
correction ("diagnoses" -> "codes") resolves cleanly by t=5s, well before the
11s beat ends, with the final corrected question still typing at t=10.5s
(full margin). B01/B02/B03 are legible, safe-inset, single-accent, no
overlap — B02's pipeline diagram reads "CLINICAL NOTE" -> "Read SKILL.md" ->
"Execute" -> "Return output" -> "BILLABLE CODES" cleanly. BCRY correctly
shows the resolved carry-out sentence. BHTF correctly shows
`@HumanitariansAI` (not the `ClaudeComposerAsk` default `@NikBearBrown`) and
the full "Your Turn" prompt, wrapped without truncation or overlap. BOUT
shows the OutroCTA subscribe pill and `@HumanitariansAI` handle correctly,
static and legible at both t=75s and t=77s (near clip end). No blockers
found; no re-render needed.

**Audio:** ffprobe confirms an AAC audio stream present, master mtime
(1788347493) newer than beat_sheet.json's (1788347396); independent `ffmpeg
-af volumedetect` pass: mean_volume **-24.0 dB**, max -3.0 dB — comfortably
above the -40 dB floor (also matches `compile.py`'s own GATE AUDIO PASS
reading of -24.0 dB from the same build).

Metadata file written: `healthcare--claude-liam-icd10-cm-skill.md` (channel
@HumanitariansAI). **Playlist: Claude Basics** — `SUBJECT.json`'s `family` is
`"healthcare"`, which has no entry in
`skills/make/hai-simple/loop/playlists.json`'s map, so resolution falls
through to the `hai-simple` skill-prefix key, `"Claude Basics"` — same
resolution as every other `healthcare--*` sibling already logged in
`HAILOOP-LOG.md` (`doc-extract`, `fhir`, `fhir-developer-skill`,
`fraud-detection`, `contracts`, `clinical-note-extract-skill`,
`clinical-trial-protocol-skill`). Description also carries the direct code
link per the DELIVERY CONTRACT format.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4 delivery

Master is already 3840x2160 natively (compile.py's 4K LAW), so the
Fellows-facing 4K file is the same render, copied to the `-4k` filename
`deliver.py` expects.

```
cp healthcare--claude-liam-icd10-cm-skill.mp4 healthcare--claude-liam-icd10-cm-skill-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
