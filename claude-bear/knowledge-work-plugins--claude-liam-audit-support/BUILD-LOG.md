# BUILD-LOG — knowledge-work-plugins--claude-liam-audit-support

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-audit-support/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `audit-support`
Claude Skill, from a `knowledge-work-plugins` book finance plugin set —
already fully built, no SCRIPT.md; source `beats[*].narration_text` and its
`_std/AUDIT.md` served as the locked script). Built entirely fresh this
invocation — only SUBJECT.json existed on pickup. The source's
`source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/finance/skills/audit-support/SKILL.md`)
is not present on this machine (same situation as the
`financial-services--claude-liam-kyc-rules` sibling and others); the
source sheet's own narration already carried the facts needed, so no
reconstruction was required.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works, containing one file (SKILL.md)
written in plain language, no hidden logic; the instructions live in a
Steps section, executed in order, no branching unless a step says so;
`audit-support`'s specific job is to support SOX 404 compliance with
control testing methodology, sample selection, and documentation
standards — used when generating testing workpapers, selecting audit
samples, classifying control deficiencies, or preparing for internal or
external audits; same input produces the same output every run; the skill
only handles what its file specifies. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "pass" → "support" — the newcomer's wrong guess that Claude
renders the audit opinion itself, corrected toward the actual mechanism:
the skill only tests the sample against the criteria and hands the
opinion to a person). Register re-registered Teardown → Plain: the
source's B03 "gets it right: repeatable results / what it bites: anything
outside the spec" framing was restated in NB03 as a plain
mechanism-and-boundary fact (what the skill tests and classifies, and what
it declines to decide), per the NO JUDGMENT register check. BVDT's verdict
facts (same input → same output every run; limited to what the file
specifies) were merged into the single BCRY carry-out sentence rather than
kept as a separate bulleted artifact card, per CARRY-OUT LAW. BHTF's
prompt was adapted, not copied verbatim: the source asked the viewer to
"read the audit-support skill," which requires a plugin install a general
viewer won't have, so this redo substitutes an equivalent, actually
paste-ready prompt exercising the same test-before-opine habit without
depending on any specific Skill file. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 teardown design-tell + BVDT verdict + BHTF
your-turn + BOUT outro). This redo kept the same 7-beat shape: B00 carries
the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat;
B01→NB01, B02→NB02 kept as one beat each; B03's Teardown framing
compressed into NB03 (a plain mechanism-and-boundary fact); BVDT folded
into BCRY; BHTF kept (prompt adapted, see above); BOUT kept. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim (mechanism,
colors, GATE T exemption notes) from the
`financial-services--claude-liam-kyc-rules` sibling, adapted with
audit-support-specific labels.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 4-line text) reused directly from the
`financial-services--claude-liam-kyc-rules` sibling's proven working
configuration. `actual_duration_s` (narration) 12.78s + `lead_silence_s`
1.0 gave the writer a 13.78s window; rendered clip extended to 12.8s,
comfortably clearing the ≥8s TIMING LAW floor. Verified by frame pulls at
t=2.0s ("pass" doomed in terracotta, mid-type), t=5.0s ("support" already
settled after the correction), t=9.0s and t=12.0s (full corrected question
"Does Claude support a company's SOX 404 audit?" settled and legible,
holding to the end of the clip) — correction lands and settles well
inside the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00); NB01–NB03 rendered via `render_scenes.py`
(foreground); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` — the
invocation exceeded the tool's 120s timeout and was moved to background by
the harness automatically; blocked on it via `TaskOutput` (block=true)
before proceeding, per the COMPLETION LAW's foreground-render rule, and
confirmed exit code 0 with all four beats reporting `ok` before moving on.

**GATE T (type_check.py): PASS, 0 FAILs on the first automated run** — but
a manual Gate V frame pull at t=30–36s caught a real legibility defect the
checker missed: NB02's accented middle chip, originally labelled "test
control" (bold, EB Garamond), rendered with the "n"/"t" glyphs of
"control" colliding into an unreadable "co­ntrol" smear — a bold-weight
kerning collapse on that specific letter pair, the same class of
checker-blind-spot defect the kyc-rules sibling hit with a dotted "i" (the
automated checker's kerning/min-size tables don't cover every glyph-pair
and weight combination). **Root-caused and fixed:** replaced the two-word
label with a single word, "tested" — matching the pattern already proven
safe elsewhere in this same beat set (NB03's accented "classified" and the
kyc-rules sibling's "risk-rated" are both single bold tokens that render
clean). Re-rendered NB02 only (`render_scenes.py`, beat cached-skip on
NB01/NB03), recompiled with `--force`, re-ran `type_check.py` (still PASS,
0 FAILs) and re-pulled the fixed frame to confirm clean spacing with no
glyph collision before accepting the cut.

Compiled:
```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-audit-support.mp4`, 7/7 beats
filled real (no slate), 96.3s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (post NB02 fix)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 96.3s; mp4
  mtime (1788367472) newer than beat_sheet.json mtime (1788367374)
- Gate V (visual): pulled frames at t=3/20/30/32(fixed)/36/45/55/63/75/88/95s
  across the full runtime plus the targeted B00 correction-timing checks
  above. B00 (writer, correction visible and settled,
  "@HumanitariansAI" overlay present per hai's channel-title law), NB01
  (chips legible, arrows and caption clean), NB02 (post-fix: "select
  sample" → "tested" → "write it up", all legible, no overlap), NB03
  (chips legible, "checked by auditor" avoided the dotted-i failure class
  proactively per the kyc-rules precedent), BCRY (carry-out quote +
  sparkline "Classifies. Never opines." read clean), BHTF (correct topic
  "AUDIT-SUPPORT · SOX 404 COMPLIANCE SKILL", correct title "It Tests and
  Classifies. It Doesn't Decide.", @HumanitariansAI folder label,
  paste-ready prompt legible), BOUT (OutroSeries: "AUDIT-SUPPORT ·
  @HumanitariansAI" eyebrow, correct title restate, crimson underline, no
  truncation). No remaining blockers.

Metadata file written:
`knowledge-work-plugins--claude-liam-audit-support.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `knowledge-work-plugins` key
directly (an exact, direct prefix match — no fallthrough to `hai-simple`
or `_default` needed, unlike the `financial-services` sibling). Direct
code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to
`knowledge-work-plugins--claude-liam-audit-support-4k.mp4` rather than
re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-audit-support/` (4K
master + description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-audit-support/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) to the
humanitarians-youtube clone.

**Status: DELIVERED.**
