# BUILD-LOG — healthcare--claude-liam-doc-extract

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/healthcare/youtube/claude-liam-doc-extract/beat_sheet.json` — a
fully-built, Teardown-register skill explainer (7 beats, `claude-liam` /
@NikBearBrown, no SCRIPT.md on the source). Its `beats[*].narration_text`
served as the locked narration per the redo contract, same disposition as
the `books--claude-liam-building-plugins` sibling redo. Never touched the
source reel's folder.

**Facts kept unchanged:** the skill is `doc-extract`; a skill is a folder
Claude reads before it works, and `SKILL.md` holds the full instruction set
in plain language; the pipeline reads a Steps section and executes it
linearly (no branching unless a step says so); the skill's only job is to
turn a document (PDF, DOCX, XLSX, PPTX, RTF, or plain text/markdown/HTML)
into plain text — not a summary, not an analysis; asking for more than
extraction is outside the skill's spec.

**Dropped as maintainer trivia, not viewer argument:** the source B00's
clause about `fhir` invoking `scripts/extract.ts` directly and the contracts
MCP server bundling its own copy of the extractor for self-containment
("port fixes to both"). That's a note for whoever edits the skill's source,
not a fact a general first-time viewer needs to answer "what does this
skill do" — cut for Plain-register compression, not for accuracy.

**Register: Teardown -> Plain.** The source's B03 ("Here is the Teardown
moment... What it gets right: repeatable results. What it bites: anything
outside the spec.") and BVDT ("Verdict" artifact, "Know the limit") judge
the design's trade-offs. Plain states the identical constraint as fact
(this reel's B03: "Not a summary, not an analysis — just the words, pulled
out. Ask for more than that, and that's a different skill.") and lands it
as the carry-out (BCRY) instead of a verdict artifact — same fact, judgment
removed.

**B00 WRITER LAW:** the source's implicit misconception is that "extract
text from a document" means the skill reads/understands it for you
(summarizes a contract, answers what's inside) — the source's own B03/BVDT
"bites" clause ("anything outside the spec") is the same idea already
present, restated here as the naive framing instead of a verdict. Typed
text: "A document skill just / summarizes the PDF. / Wait — what does / it
actually do?", trigger "summarizes" -> replacement "extracts text from".
B00 audio measured 8.58s + `lead_silence_s` 0.8 = 9.38s window (TIMING LAW's
>=9s), narration 24 words. Verified on a frame at t=7.5s: the correction has
already resolved ("...extracts text from the PDF.") and the writer is
mid-way through the final question line — correction and framing both land
inside the beat with margin.

**BVDT -> BCRY:** `ClaudeVerdictArtifact` ("Verdict" artifact card) ->
`WantQuote` (the bare carry-out sentence), matching `simple`'s law that the
verdict-recap position becomes the carry-out line in Plain register. Same
beat slot, same beat count (7 -> 7: B00, B01, B02, B03, BCRY, BHTF, BOUT).
Carry-out: "Turning a document into text, and understanding that text, are
two different jobs — doc-extract only does the first one" — directly
resolves B00's naive framing.

**Body beats (B01-B03):** kept the source's own Remotion components
(`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`)
rather than rebuilding as Manim — all three confirmed still registered and
renderable (`./art scenes --check`), and none of the source's beats were
ever `ai-video-prompt`, pantry, or human-drop (NO-GENAI/NO-PANTRY LAW was
already satisfied), so no substitution was owed beyond the two the skill
mandates (B00 writer-open, BOUT HAI-skin). Only the prop text changed:
eyebrow/heading/sparkLine reworded off Teardown language ("DESIGN TELL" ->
"MECHANISM", "the interesting constraint" / "this is the part worth
knowing" -> "Just the words, extracted." / "Not a summary. Just the text.").

**BHTF:** kept `ClaudeComposerAsk`, explicit `folderLabel: "@HumanitariansAI"`
override (component's Root.tsx default is `@NikBearBrown`, the same known
bug worked around in sibling redos), and rewrote the command text — the
source's own prompt carried a mid-sentence truncation ("rtf, or plain t.")
already flagged as locked/unfixable in the source's own AUDIT.md; the redo
contract only locks facts, not a truncation artifact, so it's written out
in full here.

**BOUT:** `ClaudeTitleOutro` (blank subline, `@NikBearBrown`) ->
`OutroCTA` (Humanitarians AI skin, `@HumanitariansAI`), per hai-simple's
channel-skin law.

**Voice:** unchanged — Liam, Kokoro `am_onyx`, "in for Bear." (source
already used this voice; hai-simple's Liam-not-`af_kore` rule needed no
change.)

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (7 beats, all REMOTION — no Manim needed). Ran
`generate_audio_kokoro.py` (7/7 beats, am_onyx, $0.00) — measured durations
became the clock. Rendered all 7 Remotion beats via `remotion_scenes.py`
(foreground, waited on the task's exit code — no orphaned background
renders, per the one-shot-invocation lesson).

**GATE T (type_check.py) first pass: 1 FAIL.** B03's `SkillTeardownMechanism`
`body` prop ("Extract plain text from a document file — PDF, DOCX, XLSX,
PPTX, RTF, or plain text, markdown, HTML.", a full sentence) tripped
no-wordy-card §8.5 at 18 words > the 12-word pull-quote limit — "the screen
should show structure, not sentences." **Fixed at the root**: first pass
shortened to a dot/arrow-separated label ("PDF · DOCX · ... → PLAIN TEXT"),
which the checker still counted at 14 words (each `·`/`→` glyph surrounded
by spaces counts as its own whitespace-split token) and additionally
tripped a new min-size §8.1 fail (36px < 41px floor — the longer string
forced the component's auto-shrink-to-fit-width). **Second fix**: dropped
the separator glyphs and the arrow entirely, plain comma list only ("PDF,
DOCX, XLSX, PPTX, RTF, TXT/MD/HTML" — 6 whitespace tokens), which needed no
auto-shrink. Re-rendered B03 only, recompiled, re-ran GATE T: **PASS, 0
FAILs.**

Compiled with `compile.py . --force`: 7/7 beats real (no slate), master born
natively 4K (3840x2160, `compile.py`'s 4K LAW), 73.6s. `content-check`/
`frame-check`/`lane-check` all PASS. Motion histogram `remotion:7` (100% —
structural, not a defect: this reel has no body-mechanism content dense
enough to warrant Manim graphics beyond the source's own three Remotion
cards, and hai-simple's mandated bookends — B00/BCRY/BHTF/BOUT — are
REMOTION by skill contract regardless).

**Gate V:** pulled 12 frames at 6s spacing across the full 73.6s runtime,
plus a dedicated late-B00 frame (t=7.5s) for the correction check and a
dedicated BOUT frame (t=71.5s); read every one directly. B00's correction
("summarizes" -> "extracts text from") has resolved with the writer still
mid-question at t=7.5s — full margin inside the 8.6s beat. B01/B02/B03 are
legible, safe-inset, single-accent, no overlap. BCRY and BHTF both correctly
show `@HumanitariansAI` (not the `ClaudeComposerAsk`/default-outro
`@NikBearBrown`). BOUT shows the OutroCTA subscribe pill and handle
correctly. No remaining blockers.

**Audio:** ffprobe confirms an AAC mono stream present (48kHz), master mtime
(1788341109) newer than beat_sheet.json's (1788341017); `ffmpeg -af
volumedetect`: mean_volume **-24.0 dB**, max -2.9 dB — comfortably above the
-40 dB floor.

Metadata file written: `healthcare--claude-liam-doc-extract.md` (channel
@HumanitariansAI). **Playlist: Claude Basics** — `SUBJECT.json`'s `family`
is `"healthcare"`, which has no entry in
`skills/make/hai-simple/loop/playlists.json`'s map, so resolution falls
through to the `hai-simple` skill-prefix key, `"Claude Basics"`. (First
pass of this file argued for a content-based override to "Extending Claude
— Skills, Plugins & Connectors" on the `books--claude-liam-building-plugins`
sibling's precedent — reverted after checking `HAILOOP-LOG.md`: every other
healthcare-family skill-teardown redo in this same batch
(`clinical-note-extract-skill`, `clinical-trial-protocol-skill`,
`contracts`) is equally "about a Claude Skill" and all of them resolved to
`Claude Basics` via the mechanical `hai-simple` fallback with no override.
Matching the batch's actual established convention beats a one-off
precedent from a different family.) Description also carries the direct
code link per the DELIVERY CONTRACT format.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4 delivery

Master is already 3840x2160 natively (compile.py's 4K LAW), so the
Fellows-facing 4K file is the same render, copied to the `-4k` filename
`deliver.py` expects.

```
cp healthcare--claude-liam-doc-extract.mp4 healthcare--claude-liam-doc-extract-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
