# BUILD-LOG — healthcare--claude-liam-fhir

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/healthcare/youtube/claude-liam-fhir/beat_sheet.json` — a fully-built,
Teardown-register skill explainer (7 beats, `claude-liam` / @NikBearBrown, no
SCRIPT.md on the source, already audited/rebuilt once per its own REBUILD-LOG.md/
AUDIT.md). Its `beats[*].narration_text` served as the locked narration per the
redo contract, same disposition as the `healthcare--claude-liam-doc-extract`
sibling redo. Never touched the source reel's folder.

**Facts kept unchanged:** the skill is `fhir`; a skill is a folder Claude reads
before it works, and `SKILL.md` holds the full instruction set in plain
language; the pipeline reads a Steps section and executes it linearly (no
branching unless a step says so); the skill's job is to connect to a hospital's
FHIR R4 server (Epic, Oracle Health/Cerner, MEDITECH, athenahealth, or any
SMART-on-FHIR endpoint), pull a patient's clinical data and notes, and extract
structured findings; asking for more than structured retrieval (a diagnosis,
clinical judgment) is outside the skill's spec.

**Register: Teardown -> Plain.** The source's B03 ("Here is the Teardown
moment... What it gets right: repeatable results. What it bites: anything
outside the spec.") and BVDT ("Verdict" artifact, "the limit is the spec, and
that is the point") judge the design's trade-offs. Plain states the identical
constraint as fact (this reel's B03: "Not a diagnosis, not clinical judgment —
just the data, structured. Ask for more than that, and that's a different
skill.") and lands it as the carry-out (BCRY) instead of a verdict artifact —
same fact, judgment removed.

**B00 WRITER LAW:** the source's own "bites" clause (anything outside the spec)
already implies the newcomer's misconception — that connecting Claude to a live
EHR means it reads and diagnoses the patient, rather than just pulling
structured data out. Typed text: "Connect Claude to the EHR / and it diagnoses
the patient. / Wait — what does / fhir actually do?", trigger "diagnoses" ->
replacement "pulls records for". B00 audio measured 9.83s + `lead_silence_s`
0.8 = ~10.6s window (TIMING LAW's >=9s), narration 31 words. Verified on a frame
at t=7.5s: the correction has already resolved ("...and it pulls records for
the patient.") with the writer mid-way into "Wait —" — correction and framing
both land inside the beat with margin.

**BVDT -> BCRY:** `ClaudeVerdictArtifact` ("Verdict" artifact card) ->
`WantQuote` (the bare carry-out sentence), matching `simple`'s law that the
verdict-recap position becomes the carry-out line in Plain register. Same beat
slot, same beat count (7 -> 7: B00, B01, B02, B03, BCRY, BHTF, BOUT).
Carry-out: "Pulling a patient's record out of the system, and making sense of
what it means, are two different jobs — fhir only does the first one" —
directly resolves B00's naive framing.

**Body beats (B01-B03):** kept the source's own Remotion components
(`SkillTeardownAnatomy`, `FlowDiagram`, `SkillTeardownMechanism`) rather than
rebuilding as Manim — all three confirmed still registered and renderable
(`./art scenes --check`), and none of the source's beats were ever
`ai-video-prompt`, pantry, or human-drop (NO-GENAI/NO-PANTRY LAW was already
satisfied), so no substitution was owed beyond the two the skill mandates (B00
writer-open, BOUT HAI-skin). B02's `FlowDiagram` node props were carried over
verbatim from the source, including its own prior Gate-V truncation fix
("Epic · Cerner · MEDITECH" -> "any SMART endpoint" on the FHIR R4 Server
node) — re-verified legible on this build's frame pull, no new truncation.
Only the B01/B03 prop text changed: eyebrow/heading/sparkLine reworded off
Teardown language ("DESIGN TELL" -> "MECHANISM", "the interesting constraint"
-> "Just the data, structured.") and B03's body prop rewritten as a plain
comma list ("Epic, Cerner, MEDITECH, athenahealth, any SMART-on-FHIR") rather
than a full sentence, following the doc-extract sibling's fix for the
no-wordy-card §8.5 pull-quote limit before it could recur.

**BHTF:** kept `ClaudeComposerAsk`, explicit `folderLabel: "@HumanitariansAI"`
override (component's Root.tsx default is `@NikBearBrown`, the same known bug
worked around in sibling redos), and rewrote the command text in full — the
source's own prompt read fine but the redo restates it plainly for Plain
register, no truncation.

**BOUT:** `ClaudeTitleOutro` (blank subline, `@NikBearBrown`) -> `OutroCTA`
(Humanitarians AI skin, `@HumanitariansAI`), per hai-simple's channel-skin law.

**Voice:** unchanged — Liam, Kokoro `am_onyx`, "in for Bear." (source already
used this voice; hai-simple's Liam-not-`af_kore` rule needed no change.)

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (7 beats, all REMOTION — no Manim needed). Ran
`generate_audio_kokoro.py` (7/7 beats, am_onyx, $0.00) — measured durations
became the clock.

**Rendering:** `remotion_scenes.py` ran in the foreground; the harness's own
120s default tool-timeout moved the long-running render to a tracked
background task mid-invocation (not an orphaned/unsupervised process — same
session, polled to completion via a foreground wait loop before proceeding,
per the one-shot-invocation lesson: never end the turn on an unconfirmed
render). First pass: 6/7 beats ok, **BHTF failed** on a transient
`NodeWebSocketTransport`/renderer crash (WebSocket closed mid-render, not a
content or prop error). Retried with `--only BHTF`; second attempt succeeded
cleanly. All 7 media files confirmed present before moving to compile.

Compiled with `compile.py`: 7/7 beats real (no slate), master born natively 4K
(3840x2160, `compile.py`'s 4K LAW), 78.9s. `content-check`/`frame-check`/
`lane-check` all PASS. Motion histogram `remotion:7` (100% — structural, not a
defect: hai-simple's mandated bookends and this source's own three body
Remotion cards account for the whole reel).

**GATE T (type_check.py): PASS, 0 FAILs** on the first pass — the B03
body-prop lesson from the doc-extract sibling (plain comma list, no
separator glyphs) was applied up front, avoiding the wordy-card/min-size
failure loop that reel hit.

**Gate V:** pulled 13 frames at 6s spacing across the full 78.9s runtime, plus
a dedicated late-B00 frame (t=7.5s) for the correction check and a dedicated
BOUT frame (t=77.5s); read every one directly. B00's correction ("diagnoses"
-> "pulls records for") has resolved with the writer still mid-"Wait —" at
t=7.5s — full margin inside the 9.8s beat. B01/B02/B03 are legible,
safe-inset, single-accent, no overlap; B02's FlowDiagram nodes all render
without truncation. BCRY and BHTF both correctly show `@HumanitariansAI` (not
the `ClaudeComposerAsk`/default-outro `@NikBearBrown`). BOUT shows the OutroCTA
subscribe pill and handle correctly. No remaining blockers.

**Audio:** ffprobe confirms an AAC mono stream present (48kHz), master mtime
(1788343052) newer than beat_sheet.json's (1788342955); `ffmpeg -af
volumedetect`: mean_volume **-24.0 dB**, max -3.0 dB — comfortably above the
-40 dB floor.

Metadata file written: `healthcare--claude-liam-fhir.md` (channel
@HumanitariansAI). **Playlist: Claude Basics** — `SUBJECT.json`'s `family` is
`"healthcare"`, which has no entry in
`skills/make/hai-simple/loop/playlists.json`'s map, so resolution falls
through to the `hai-simple` skill-prefix key, `"Claude Basics"` — matching the
established convention for every other healthcare-family skill-teardown redo
in this batch (`doc-extract`, `contracts`, and siblings). Description also
carries the direct code link per the DELIVERY CONTRACT format.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4
(4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4 delivery

Master is already 3840x2160 natively (compile.py's 4K LAW), so the
Fellows-facing 4K file is the same render, copied to the `-4k` filename
`deliver.py` expects.
