# BUILD-LOG — knowledge-work-plugins--claude-liam-journal-entry

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-journal-entry/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `journal-entry`
finance Skill, already fully built — no SCRIPT.md; source `beats[*].
narration_text` served as the locked script). Built entirely fresh this
invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a Skill
is a folder Claude reads before it works; the journal-entry SKILL.md holds
the full instruction set in plain language with no hidden logic; the
Steps section runs linearly, top to bottom, no branching unless a step
says so; the design is a specification, not expertise — same request
produces the same debits, credits, and supporting detail every run, but
Claude has no basis for deciding anything outside what the file
specifies. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold
open with `BrutalistHesitantWriter` (WRITER LAW: "feel" → "file" — the
newcomer's wrong guess that Claude books journal entries by feel/judgment,
the way an accountant would from experience, corrected toward the actual
mechanism: it works from a written file it reads and follows exactly).
Register re-registered Teardown→Plain: the source's B03 "gets it right /
where it bites" framing was stripped of verdict language and kept as a
single plain mechanism-and-consequence description (NB03) rather than a
strengths/gaps inventory. BVDT's verdict facts were merged into the
single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask cold open +
B01/B02 anatomy/pipeline + B03 design tell + BVDT verdict + BHTF
your-turn + BOUT outro). This redo kept the same 7-beat shape: B00
carries the wrong-guess pedagogy per WRITER LAW instead of a dedicated
beat; B01→NB01, B02→NB02 kept as one beat each; B03's design-tell
framing compressed into NB03 (spec-vs-expertise, the one fact a general
viewer needs and can act on); BVDT folded into BCRY; BHTF kept, with the
source's four-way accrual/depreciation/revenue-recognition/audit-doc
prompt narrowed to one concrete, single-scenario runnable request (a
month-end accrual); BOUT kept. Full audit in SCRIPT.md's "Beat-count note
(redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with journal-entry-specific labels.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(auto-backgrounded by the harness past its 120s timeout — blocked on it
via `TaskOutput` before proceeding, per the COMPLETION LAW's
foreground-render rule, never treating a backgrounded render as "handled"
without waiting on it); NB01–NB03 rendered via `render_scenes.py`
(foreground, completed within timeout). `type_check.py` ran clean on the
first pass — **PASS, 0 FAILs** (kerning §8.4 checked on 3 beats, 0 FAILs;
min-size, overflow, contrast, bbox-overlap, card-clip all 0 FAILs across
7 beats).

B00 config (42ms/char, 8% hesitateBetween, 4% mistakeRate, 38-char/4-line
text "Does Claude / book journal / entries by / feel?") reused the
already-fixed values from the agent-development sibling's B00 TIMING LAW
incident directly, rather than starting from that incident's first,
longer/slower config — this text is shorter still (38 vs. that sibling's
60 characters), giving extra render-window margin. First-render outcome:
clean, no re-render needed. Verified by frame pulls at t=3s ("Does Claude
/ book journal" mid-typing), t=6.0s (trigger word "f" typed in terracotta,
about to be replaced), t=6.5s (settled and corrected to "file?"), and
t=9.0s (held, unchanged, near the clip's end) — actual_duration_s 10.1s
(comfortably ≥8s), correction lands on screen by t≈6.5s and stays legible
for the remaining ~3.5s.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-journal-entry.mp4`, 7/7 beats
filled real (no slate), 89.1s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (kerning §8.4 checked 3 beats, 0 FAILs; see
  TYPECHECK.md)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 89.1s; mp4
  mtime (1788500880) newer than beat_sheet.json mtime (1788500775)
- Gate V (visual): pulled frames every ~6s across the full runtime plus
  targeted checks of B00 (t=3.0/6.0/6.5/9.0s — trigger-word correction
  visible and settled well within the clip), NB01 ("A SKILL IS A FOLDER"
  chips legible, arrow flow correct), NB02 ("STEPS, IN ORDER" — the bold
  accented chip "top to bottom" reads tight-kerned but every glyph
  distinguishable, confirmed by a zoomed crop; GATE T's calibrated
  kerning check already passed this beat), NB03 ("SPEC, NOT EXPERTISE" —
  the bold accented chip "outside spec" likewise reads clean on a zoomed
  crop), BCRY (carry-out sentence + sparkline "By file. Not by feel."
  read clean, a direct callback to B00's correction), BHTF (correct
  topic/title/@HumanitariansAI handle, paste-ready prompt text legible),
  and BOUT (OutroSeries: correct eyebrow "JOURNAL ENTRIES ·
  @HumanitariansAI", correct title restate, crimson underline, no
  truncation). No blockers — the two chips that looked cramped at a
  glance were verified legible on inspection, not treated as defects on
  a first impression.
- B00 TIMING LAW: `actual_duration_s` 10.1s (≥8s requirement met); the
  "feel" → "file" correction lands on screen by t≈6.5s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written:
`knowledge-work-plugins--claude-liam-journal-entry.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key match in the map, resolving
directly to "Extending Claude — Skills, Plugins & Connectors" (no
prefix-fallback needed).

Deliverables staged next: 4K render + `deliver.py --push`.
