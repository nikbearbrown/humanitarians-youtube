# BUILD-LOG — healthcare--claude-liam-clinical-note-extract-skill

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/healthcare/youtube/claude-liam-clinical-note-extract-skill/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic
`clinical-note-extract-skill` Claude Skill, from the `healthcare` book's
plugin set; already fully built, no SCRIPT.md — source `beats[*].narration_text`
plus its `AUDIT.md` served as the locked script/facts). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over: a skill is a folder
Claude reads before it works, containing SKILL.md (plain language, no
hidden logic) plus `assets/`, `references/`, `scripts/`, `workflows/` — six
files/folders total; the skill's job is structured extraction from
clinical notes against a user-defined schema, with a span citation for
every value it reports and an explicit null for every value it can't find;
same note and schema produce the same output every run; the skill only
handles what its file specifies. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "guess" → "cite" — the newcomer's wrong guess that an
extraction skill infers a plausible value the way a person would,
corrected toward the actual mechanism: it only cites a value it can point
to and returns null otherwise). Register re-registered Teardown → Plain:
the source's B03 "gets it right: repeatable results / what it bites:
anything outside the spec" framing was restated in NB03 as a plain
mechanism-and-boundary fact, per the NO JUDGMENT register check. BVDT's
verdict facts (same input → same output every run; limited to what the
file specifies) were merged into NB03/BCRY rather than kept as a separate
bulleted artifact card, per CARRY-OUT LAW. BHTF's prompt was adapted, not
copied verbatim: the source asked the viewer to "read the
clinical-note-extract-skill skill," which requires a plugin install a
general viewer won't have, so this redo substitutes an equivalent,
actually paste-ready prompt exercising the same cite-or-null discipline on
any block of text. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Content correction against the source (not an invented fact):** the
source's B02 narration claimed "the pipeline has 2 steps" and named only
the two sub-checks inside validation (span check, field-type check). The
source's own `AUDIT.md` ("Content accuracy note (narration LOCKED — not
fixable)") documents this as a scripting error: the real `SKILL.md`
defines four steps — Define schema, Extract, Validate, Report — and the
locked narration only ever described the two sub-steps of step 3. Because
this redo writes fresh Plain narration rather than reusing the source's
locked sentences verbatim, NB02 states the real four-step pipeline and
folds the two validation sub-steps in as part of step 3, per AUDIT.md's
own documented correction. See QUESTION.md and SCRIPT.md for the full
note.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 teardown design-tell + BVDT verdict + BHTF
your-turn + BOUT outro). This redo kept the same 7-beat shape: B00 carries
the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat;
B01→NB01, B02→NB02 kept as one beat each (NB02 content-corrected per
above); B03's Teardown framing compressed into NB03 (a plain
mechanism-and-boundary fact); BVDT folded into BCRY; BHTF kept (prompt
adapted, see above); BOUT kept. Full audit in SCRIPT.md's "Beat-count note
(redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim (mechanism,
colors, GATE T exemption notes) from the
`financial-services--claude-liam-kyc-rules` sibling, adapted with
clinical-note-extract-skill-specific labels.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 4-line text) reused directly from the
`financial-services--claude-liam-kyc-rules` sibling's proven working
configuration. `actual_duration_s` (narration) 10.47s + `lead_silence_s`
1.0 gave the writer an 11.47s window; rendered clip extended to 10.5s,
comfortably clearing the ≥8s TIMING LAW floor. Verified by frame pulls at
t=2.0s ("guess" doomed in terracotta, mid-type), t=5.0s (mid-correction,
"cite a value" typing in), t=8.5s and t=10.2s (full corrected question
"Does Claude cite a value from a clinical note?" settled and legible,
holding to the end of the clip) — correction lands and settles well inside
the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00); NB01–NB03 rendered via `render_scenes.py`
(foreground); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` — the
invocation exceeded the tool's 120s timeout and was moved to background by
the harness automatically; blocked on it via `TaskOutput` (block=true)
before proceeding, per the COMPLETION LAW's foreground-render rule, and
confirmed exit code 0 with all four beats reporting `ok` before moving on.

**Gate V finding, fixed:** first frame pull of NB03 showed the accented
chip label "explicit null" rendering with no visible space between the two
words in the bold EB Garamond weight — "explicitnull" — genuinely
ambiguous (unlike the numeral-chip idiom "1file"/"6files" already accepted
non-blocking in the `kyc-rules` sibling's own delivered build, which reads
fine from context; two full dictionary words gluing into a nonsense string
does not). Root cause: bold-weight EB Garamond chip labels with a space
between two words collapse the space in this Manim/Cairo rendering path.
Fixed at the content level, matching the beat's own established style
(its other two chips are already hyphenated — "schema-driven",
"span-cited"): relabeled to "explicit-null" in both `scenes.py` and
`beat_sheet.json`'s `graphic.production_viz.chips`, re-rendered only
NB03.mp4, recompiled with `--force`. Re-verified by frame pull: chip now
reads "explicit-null" cleanly. `type_check.py` re-run: PASS, 0 FAILs (the
automated checker did not flag the original glued text — this was an
editorial/legibility catch during Gate V's human frame review, not a
GATE T failure).

Compiled:
```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```
Result: `healthcare--claude-liam-clinical-note-extract-skill.mp4`, 7/7
beats filled real (no slate), 91.9s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 91.9s; mp4
  mtime (1788335525) newer than beat_sheet.json mtime (1788335395)
- Gate V (visual): pulled frames at t=3/12/20/30/38/46/55/63/72/80/88s
  across the full runtime plus the targeted B00 correction-timing checks
  above. B00 (writer, correction visible and settled, "@HumanitariansAI"
  overlay present per hai's channel-title law), NB01/NB02/NB03 (all chips
  legible post-fix, arrows and captions clean, no overlap), BCRY
  (carry-out quote + sparkline "Cites. Never guesses." read clean), BHTF
  (correct topic "CLINICAL-NOTE-EXTRACT-SKILL · SPAN-LEVEL EXTRACTION
  SKILL", correct title "It Cites the Evidence. It Never Guesses.",
  @HumanitariansAI folder label, paste-ready prompt legible), BOUT
  (OutroSeries: correct eyebrow/title restate, crimson underline, no
  truncation). No blockers after the NB03 fix.

Metadata file written:
`healthcare--claude-liam-clinical-note-extract-skill.md` (channel
@HumanitariansAI, **Playlist: Claude Basics**). Per `playlists.json`,
SUBJECT.json's family (`healthcare`) matches no specific vertical prefix
in the map (no `healthcare-`/`clinical-` entry exists), so resolution
falls through in map order to the `hai-simple` key itself (present in the
map precisely as this general fallback), which resolves to "Claude Basics"
— reached before `_default` ("Claude Across the Curriculum") is ever
considered, matching the disposition of the
`financial-services--claude-liam-kyc-rules` sibling exactly. Direct code
link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
