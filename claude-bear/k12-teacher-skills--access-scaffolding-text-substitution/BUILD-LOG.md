# BUILD-LOG — k12-teacher-skills--access-scaffolding-text-substitution

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/k12-teacher-skills/youtube/access-scaffolding-text-substitution/beat_sheet.json`
(an ELA differentiation walkthrough of the k12-lesson-differentiation
plugin's access-scaffold design, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely fresh
this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: text
substitution (an easier book) closes the grade-level door, while access
scaffolding keeps the exact same passage and layers support around it — a
reading protocol (circle main idea, underline evidence, flag unknown words),
a two-word vocabulary gloss, and a comprehension anchor question — without
lowering the conceptual target; the scaffold/crutch distinction shows only
on removal (a scaffold fades as skill grows, a crutch performs the reading
for the student); and the fading schedule retires one scaffold at a time
until the passage stands unscaffolded. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "simpler" → "scaffolded" — the newcomer's wrong guess that a
struggling reader's problem is the text itself, so the fix is an easier
version, corrected toward the actual mechanism: keep the same text and
scaffold it). Register re-registered Plain (the source was already close to
Plain — no verdict language — so no judgment needed stripping beyond
tightening for pacing). Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source has 8 filled beats (B00 composer-ask +
B01/B02/B02a/B02b four body beats + B03 Claude-prompt verdict artifact + B04
handoff + B05 outro — the sheet's BVDT/BHTF/BOUT entries are unfilled SLATE
placeholders, not part of the built 8-beat video, per `metadata.build:
{"filled": 8, "of": 8}`). This redo kept the same 8-beat shape: B00 carries
the wrong-guess pedagogy per WRITER LAW; B01→NB01 (same-text split), B02→NB02
(what scaffolds do/don't), B02a→NB03 (scaffold-vs-crutch), B02b→NB04 (fading
schedule) kept as one beat each; B03's Claude-prompt suggestion was folded
into BHTF's paste-ready prompt rather than kept as a separate verdict-artifact
beat (B04 already carried a viewer-facing version of the same instruction —
keeping both would repeat one slot twice); B04 kept as BHTF, prompt trimmed to
the do-not-change-the-words constraint; B05 kept as BOUT, re-skinned to the
Humanitarians AI outro. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`K12Fig03TextScaffold` / `ClaudeWindow` / `K12Fig09ScaffoldVsCrutch` /
`K12Fig10FadingSchedule` / `ClaudeVerdictArtifact` / `ClaudeTitleOutro`). The
source's bespoke `K12Fig*` components are not registered in this toolkit's
scene library, so NB01–NB04 were built fresh as GRAPHIC (Manim) beats on the
same generic "chip row" template used by the `claude-plugins-official--
claude-liam-agent-development` sibling (mechanism, colors, and GATE T
exemption notes copied verbatim), carrying the same teaching point per beat
rather than re-slating the source's unavailable components.

B00's `BrutalistHesitantWriter` text/rates were set directly to the
already-verified-safe configuration from the `agent-development` sibling's
FIXED B00 (42ms/char, mistakeRate 4%, hesitateWithin 2%, hesitateBetween 8%)
rather than re-discovering the failure mode: text kept to 59 forward
characters across 4 lines (close to that sibling's 60-char fix, well under
its 67-char failed first attempt). First render succeeded without a second
pass — B00 audio measured 11.14s (comfortably ≥ 8s), and frame pulls at
t≈4.6-5.2s show "simpler" doomed in terracotta, with the corrected question
("My readers can't read this — so give them a scaffolded version?") settled
and fully legible by t≈6.5s and held to the end of the 11.1s clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 8 beats, free/local,
`am_onyx`, single pass, no re-gen needed); B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` (foreground, single pass, no errors); NB01–NB04
rendered via `render_scenes.py` (Manim, foreground, single pass, no errors).
`type_check.py` (GATE T) ran clean on the first pass: **PASS, 0 FAILs**
across all 8 beats (min-size, overflow, contrast, contrast-local,
bbox-overlap, card-clip all 0/8 FAILs).

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `k12-teacher-skills--access-scaffolding-text-substitution.mp4`, 8/8
beats filled real (no slate), 101.75s, 3840×2160 (native 4K — compile.py's
4K LAW). Motion histogram: remotion 4/8 (50%), graphic 4/8 — compile.py
logged its standard ~40%-pantry-cap advisory warning (fixed spine cost of
this skill: cold open + carry-out + your-turn + outro are always REMOTION),
not a gate failure.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 101.75s; mp4
  mtime (1788348852) newer than beat_sheet.json mtime (1788348679)
- Gate V (visual): pulled frames across the full runtime (B00 at t≈4.6-6.5-
  9.5s for the WRITER LAW correction, NB01-NB04 at t≈15/35/48/62s, BCRY at
  t≈74s, BHTF at t≈90s, BOUT at t≈98s) — all chips legible and parallel-
  sized, carry-out sentence + sparkline read clean, BHTF shows correct
  topic/title/@HumanitariansAI handle and the full paste-ready prompt
  legible, BOUT shows correct eyebrow "ACCESS SCAFFOLDING · @HUMANITARIANSAI"
  and title restate with crimson underline, no truncation. No blockers.
- B00 TIMING LAW: `actual_duration_s` 11.14s (≥8s requirement met); "simpler"
  doomed in terracotta by t≈4.6-5.2s, corrected question settled and legible
  by t≈6.5s, held through the remainder of the clip.

Metadata file written: `k12-teacher-skills--access-scaffolding-text-substitution.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per `playlists.json`,
SUBJECT.json's family (`k12-teacher-skills`) does not match any family-prefix
key in the map (no `k12`-specific entry exists); the reel's `skill` field
(`hai-simple`) matches the map's own `"hai-simple"` key exactly, which
resolves to "Claude Basics" — reached before falling through to `_default`
("Claude Across the Curriculum"), per the resolution order in the map's
`_comment`. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `k12-teacher-skills--access-scaffolding-text-substitution-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/k12-teacher-skills--access-scaffolding-text-substitution/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/k12-teacher-skills--access-scaffolding-text-substitution/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4).

**Status: DELIVERED.**
