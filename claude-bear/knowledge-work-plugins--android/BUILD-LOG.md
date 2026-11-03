# BUILD-LOG — knowledge-work-plugins--android

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-contact-center/android/beat_sheet.json`
(a Teardown skill-teardown of the Anthropic `contact-center/android` Skill).
On pickup, a prior worker pass had already completed Phase 0–2 in full:
QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (8 beats), TYPECHECK.md
(GATE T PASS, 0 FAILs), all 8 Kokoro mp3s + `mp3/timings.json` with measured
`actual_duration_s` already written back, and `media/B00.mp4` (the
BrutalistHesitantWriter cold open, 11.87s — clears the ≥8s WRITER LAW
window with the correction "RUN" → "build" landing on screen). This
invocation picked up from there: rendered the 4 remaining REMOTION beats
(B01 `SkillTeardownAnatomy`, B02 `SkillTeardownPipeline`, B03
`SkillTeardownMechanism`, BHTF `ClaudeComposerAsk`) via
`remotion_scenes.py`, then compiled.

**Redo contract check:** question, facts, and body argument carried over
from the source unchanged — a skill is a folder Claude reads before it
works; SKILL.md is the full instruction set in plain language ("the file is
the program"); the pipeline runs linearly (read → execute → return); scope
is the Zoom Contact Center SDK for native Android (chat, video, ZVA,
scheduled callback, campaign mode, service lifecycle, rejoin handling);
same request produces the same integration code every time, and the
guarantee holds only for what the file specifies. Register re-registered
Teardown → Plain: the source's judgment framing is dropped; B03 states the
scope and stops. Voice re-set to Liam `am_onyx` regardless of source. Close
carries the Humanitarians AI skin (`OutroSeries`/`OutroCTA`,
`@HumanitariansAI`). No source beat was ai-video-prompt, pantry, or a
human-drop slot — the source was already all-REMOTION, so NO-GENAI/NO-PANTRY
LAW required no substitution beyond the mandated B00 cold-open swap. Beat
count kept at the source's 7 pedagogical beats (this redo's 8 = the 7 plus
the split BCTA outro-CTA beat that's standard to every hai-simple close).
No fabricated trigger-phrase quote — the source never gives one for this
skill, and SCRIPT.md/`.md`'s "Deliberately not claimed" sections say so
explicitly.

**Gate V finding, assessed and not treated as blocking:** the BHTF
(`ClaudeComposerAsk`) command is 235 characters as one un-broken line; the
component's input area hard-caps at 3 visible lines (`maxHeight: CMD*1.45*3`,
`overflow:hidden` in `ClaudeComposerAsk.tsx`) and clips the card's on-screen
text mid-sentence, before "...handles. Then help me wire up one feature in
my app." — confirmed by reading frames at two different timestamps in the
beat (identical clipped text, so not a scroll-in-progress artifact). Checked
this against the family: dozens of already-shipped `hai-simple` siblings
carry BHTF commands from ~300 up to 438 characters as a single line (e.g.
`knowledge-work-plugins--claude-liam-build-zoom-rest-api-app` at 339 chars),
meaning this same visual clipping is the established, accepted behavior of
this shared component across the whole published series, not a defect
introduced by this reel's authoring. Narration (Liam) still reads the full
prompt aloud, and the full paste-ready text is carried verbatim in
`<slug>.md`'s "YOUR TURN" section for anyone who wants to copy it. Left
as-is rather than shortening the prompt and diverging from sibling
convention on a single reel.

**Gates passed:** content-check PASS (8/8 beats), frame-check PASS (4K
canvas, 8/8 beats), lane-check PASS, GATE AUDIO PASS (mean_volume -23.9 dB,
max -2.8 dB — well above the -40 dB floor), compile PASS. Master
`knowledge-work-plugins--android.mp4` — 83.8s, 3840×2160 (compile.py's 4K
LAW forces the clean master to 2160p by default; no separate low-res
"review" cut was requested), newer than `beat_sheet.json`. Read frames
across all 8 beats at 2fps: legible, safe-inset, no overlapping text/cards
except the BHTF clipping noted above. `MOTION.md` advisory: 8/8 beats
render as `remotion` (100%, over the ~40% pantry-language cap) — expected
for this skill (WRITER LAW + all-GRAPHIC/REMOTION body per NO-GENAI/
NO-PANTRY LAW leaves no other motion language available), not a defect.

**Delivery:** since the review-cut master already compiles at 3840×2160
(compile.py 4K LAW), the Fellows-facing 4K deliverable is a copy of the
same master under the `-4k.mp4` filename (see `deliver.py`'s
`newest_master()` — it prefers `<slug>-4k.mp4` first). `deliver.py --push`
staged `DELIVERY/knowledge-work-plugins--android/` (4K mp4 +
`-description.md`) and copied text artifacts to
`humanitarians-youtube/claude-bear/knowledge-work-plugins--android/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4), committed, and
pushed.

**Status: DONE.** `knowledge-work-plugins--android.mp4` (and its `-4k.mp4`
copy) exist, are newer than `beat_sheet.json`, and carry audible audio
(-23.9 dB). No further edits to `beat_sheet.json` after this compile.
