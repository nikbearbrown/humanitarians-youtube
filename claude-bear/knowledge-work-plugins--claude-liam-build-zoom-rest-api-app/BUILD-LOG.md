# BUILD-LOG — knowledge-work-plugins--claude-liam-build-zoom-rest-api-app

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-rest-api-app/beat_sheet.json`
(Teardown, skill-teardown chassis for the Anthropic `build-zoom-rest-api-app`
skill — B00 cold open + B01 anatomy + B02 pipeline + B03 design tell + BVDT
verdict + BHTF your-turn + BOUT outro, `PEDAGOGY.md`: "Batch build — skill
teardown format", already fully built, no separate SCRIPT.md — source
`beats[*].narration_text` served as the locked script). Built entirely fresh
this invocation — only SUBJECT.json existed on pickup.

Question, facts, and body argument carried over unchanged: the skill's own
description ("Reference skill for Zoom REST API... endpoint selection,
resource-management patterns, OAuth requirements, rate-limit awareness, or
API error debugging"); a skill is a folder Claude reads before it works, the
SKILL.md is the full instruction set, the file is the program; the pipeline
runs linearly through the Steps section; same input, same output every run,
limited to what the file specifies. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"know" → "read" — the newcomer's wrong guess that naming a skill hands
Claude general Zoom API knowledge, corrected toward the actual mechanism:
Claude *reads* a file). Register re-registered Teardown→Plain: the source's
B03 "what it gets right: repeatable results / what it bites: anything
outside the spec" — a trade-off framing that is exactly Teardown's design
judgment — was split and re-expressed without judgment as two separate
Plain-register moves: the anchor payoff (NB05, "ask twice, same answer")
and the both-directions beat (NB06, "inside the file, outside the file").
Close re-skinned to `WantQuote` / `ClaudeComposerAsk` / `OutroCTA` with
@HumanitariansAI and Liam's sign-off.

**Beat-count note (redo):** source is 7 beats; hai-simple's spine wants a
distinct wrong-guess beat and a both-directions pair, which the thin
4-body-beat source did not carry as separate beats. B01 (anatomy) and B02
(pipeline) carried over near-verbatim (NB01, NB04) — their register was
already Plain, no verdict, no trade-off. A wrong-guess beat (NB02) and an
anchor-plant/break beat (NB03) were added, built entirely from the skill's
own description text (the five named capabilities: endpoint selection,
resource-management patterns, OAuth requirements, rate-limit awareness, API
error debugging) rather than invented, giving the reel a concrete case for
the naive "already knows the API" guess to break against. Net: B00 (writer)
+ 6 body beats (NB01–NB06) + BCRY/BHTF/BOUT = 10 beats, up from the
source's 7 — the increase adds no new facts, only makes the wrong-guess and
both-directions moves explicit as their own beats instead of leaving them
folded into the design-tell beat's judgment framing. Full audit in
SCRIPT.md's "Beat-count note (redo)" and "Six-move audit" sections.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (ClaudeComposerAsk,
SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism,
ClaudeVerdictArtifact, ClaudeTitleOutro) — NO-GENAI/NO-PANTRY LAW required
no substitution beyond B00. The four new/reworked body beats (NB02, NB03,
NB05, NB06) reuse the source's own `SkillTeardownMechanism` REMOTION
pattern — a generic text-card component, not source-locked — so no new
component authoring was needed (GATE L: library hit via `./art scenes
--check`, not a miss).

**GATE T defect, fixed at the root:** first `type_check.py` pass FAILed 4/10
beats — `no-wordy-card §8.5`: NB02/NB03/NB05/NB06's `body` props exceeded
the 12-word pull-quote limit (the on-screen card should show structure, not
full sentences; the narration carries the complete sentence, the card a
short label). Fixed by de-wordifying each card's `body` to a short
structured label (e.g. NB03: "Endpoint selection. Resource-management
patterns. OAuth requirements. Rate-limit awareness. API error debugging."
— the five-item list, trailing sentence cut) while narration was left
untouched. Re-ran `type_check.py`: **GATE T: PASS**.

**B00 WRITER LAW defect, caught by Gate V and fixed before compile:** first
render of B00 showed the typing landing on "read" directly with only a
random per-character typo (a "q") flashing terracotta — the semantic
correction ("know" → "read") never appeared on screen. Root cause: the
`BrutalistHesitantWriter` component scans the literal `text` prop for
tokens matching `triggerWords`, then dramatizes swapping them for
`replacementWords` — so the trigger word must appear IN `text` itself. The
sheet had been authored with `text` already containing the corrected word
("read") and `triggerWords: "know"`, which never matched anything, so the
animation never fired. Fixed by setting `text` to the pre-correction, naive
framing ("Does Claude\nalready know\nthe Zoom API?") with `triggerWords:
"know"` / `replacementWords: "read"` — B00 was re-rendered alone
(`--only B00 --force`) and the reel recompiled (`--force`). Re-verified by
direct frame pull: "know" types fully in terracotta by t≈2.1–3.3s, then
corrects through "rea…" to the final "Does Claude / already read / the
Zoom API?" by t≈8s — well within B00's 10.86s duration (≥8s TIMING LAW
window met).

Audio generated fresh (`generate_audio_kokoro.py`, all 10 beats, free/
local, `am_onyx`, cost $0.00); all 10 beats rendered via `remotion_scenes.py`
(B00 twice — see above). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-build-zoom-rest-api-app.mp4`,
10/10 beats filled real (no slate), 108.1s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW forced the master from a 720p base).

**Gates:**
- content-check: PASS (10 beats, no violations)
- frame-check: PASS (3840×2160, 10 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see de-wordify fix above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264 24fps, audio (aac) present, duration
  108.14s; mp4 mtime (1788382431, then 1788382806 after the B00 refix)
  newer than beat_sheet.json mtime (1788382329, then 1788382703) at every
  compile
- Gate V (visual): pulled frames at 9s spacing across the full runtime plus
  targeted sub-second checks of B00 (naive "know" visible in terracotta by
  t≈2.1–3.3s, correction complete by t≈8s), NB01–NB06 (legible, safe inset
  respected, no text overlap, five-item lists render cleanly), BCRY (full
  carry-out sentence legible mid-beat), BHTF (correct topic/segment/
  command/@HumanitariansAI folder chip), BOUT (correct title, correct
  @HumanitariansAI handle, HAI outro skin). No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.86s (≥8s requirement comfortably
  met); the "know"→"read" correction lands on screen well before the end
  of the beat.

**Non-blocking warning (compile.py):** motion histogram remotion:10/10
(100%) — over the ~40% pantry cap in MOTION.md. Structural: hai-simple's
mandated shape fixes B00/BCRY/BHTF/BOUT as REMOTION, and this reel's thin
source (a 7-beat skill-teardown chassis, already 100% REMOTION before the
redo) left no GRAPHIC/Manim beats to carry over — every body beat reuses
the source's own REMOTION `SkillTeardown*` component family rather than
authoring new Manim scenes for a redo that changes register, not visual
language. Same disposition as prior `books--claude-liam-*` siblings that
inherited an all-REMOTION source. Logged per the honesty rule rather than
reworking beat count or authoring unnecessary Manim scenes to dodge the
warning.

Metadata file written:
`knowledge-work-plugins--claude-liam-build-zoom-rest-api-app.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors** — per playlists.json, `knowledge-work-plugins` maps directly
to this playlist). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to
`knowledge-work-plugins--claude-liam-build-zoom-rest-api-app-4k.mp4` rather
than re-rendering.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged
`DELIVERY/knowledge-work-plugins--claude-liam-build-zoom-rest-api-app/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-build-zoom-rest-api-app/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit
`caa4a472`, pushed clean (no rebase conflicts).

**Status: DELIVERED.**
