# BUILD-LOG — knowledge-work-plugins--claude-liam-legal-risk-assessment

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-legal-risk-assessment/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `legal-risk-
assessment` Claude Skill, from a `knowledge-work-plugins` book legal plugin
set — already fully built, no SCRIPT.md; source `beats[*].narration_text`
served as the locked script, undamaged — not a truncated `>` placeholder).
Built entirely fresh this invocation — only SUBJECT.json existed on
pickup. The source's `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/legal/skills/legal-risk-assessment/SKILL.md`)
is not present on this machine (same situation as the
`knowledge-work-plugins--claude-liam-compliance-check` and `-audit-support`
siblings); the source sheet's own narration already carried the facts
needed, so no reconstruction was required.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works, containing one file (SKILL.md)
written in plain language, no hidden logic; the instructions live in a
Steps section, executed in order, no branching unless a step says so;
`legal-risk-assessment`'s specific job is to assess and classify legal
risks using a severity-by-likelihood framework with escalation criteria —
used when evaluating contract risk, assessing deal exposure, classifying
issues by severity, or determining whether a matter needs senior counsel or
outside legal review; same input produces the same output every run; the
skill only handles what its file specifies. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "score" → "sort" — the newcomer's wrong guess that Claude
itself renders a legal risk verdict, corrected toward the actual
mechanism: the skill only sorts issues onto a severity-by-likelihood grid
and flags escalation, handing the legal call to a person). Register
re-registered Teardown → Plain: the source's B03 "gets it right:
repeatable results / what it bites: anything outside the spec" framing was
restated in NB03 as a plain mechanism-and-boundary fact (what the skill
sorts and flags, and what it declines to decide), per the NO JUDGMENT
register check. BVDT's verdict facts (same input → same output every run;
limited to what the file specifies) were merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW. BHTF's prompt was adapted, not copied verbatim: the
source asked the viewer to "read the legal-risk-assessment skill," which
requires a plugin install a general viewer won't have, so this redo
substitutes an equivalent, actually paste-ready prompt exercising the same
sort-before-escalate habit without depending on any specific Skill file.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

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
`knowledge-work-plugins--claude-liam-compliance-check` sibling, adapted
with legal-risk-assessment-specific labels.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 4-line text) reused directly from the `compliance-check`/
`audit-support` siblings' proven working configuration. `actual_duration_s`
(narration) 12.01s + `lead_silence_s` 1.0 gave the writer a 13.01s window;
rendered clip extended to 12.0s, comfortably clearing the ≥8s TIMING LAW
floor. Verified by frame pulls at t=2s ("score" mid-type, terracotta accent
visible, not yet corrected) and t=8s (full corrected question "Does Claude
sort my contract's legal risk?" settled and legible) — correction lands and
settles well inside the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00); NB01–NB03 rendered via `render_scenes.py`
(foreground, clean first pass); B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` — the invocation exceeded the tool's 120s timeout and
was moved to background by the harness automatically; blocked on it via
`TaskOutput` (block=true) before proceeding, per the COMPLETION LAW's
foreground-render rule, and confirmed exit code 0 with all four beats
reporting `ok` before moving on.

**GATE T (type_check.py): PASS, 0 FAILs on the first automated run** — but
a manual Gate V frame pull at t=30s/48s caught a real legibility defect the
checker missed: NB02's accented middle chip ("rated") and NB03's accented
middle chip ("sorted") both rendered with colliding/overlapping glyphs (the
"t"/"e" letterforms smearing into an unreadable blob) in the bold EB
Garamond weight — the same class of checker-blind-spot defect the
`compliance-check` sibling hit with "surfaced" and `journal-entry-prep`
hit with its long chip labels (a bold-weight kerning collapse the
automated checker's kerning/min-size tables don't cover for every
glyph-pair). **Root-caused and fixed:** replaced both words with the
`compliance-check` sibling's own already-proven-safe accent words —
"rated" → "checked" (NB02), "sorted" → "flagged" (NB03, chips also
reshuffled to "parsed issue" / "flagged" / "sent to counsel" to keep the
sentence readable with the new word) — matching the exact pattern already
verified clean elsewhere in this reel family. Re-rendered NB02 and NB03
only (`render_scenes.py`, NB01 cached-skip), recompiled with `--force`,
re-ran `type_check.py` (still PASS, 0 FAILs) and re-pulled both fixed
frames to confirm clean, non-colliding glyphs before accepting the cut.

Compiled:
```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-legal-risk-assessment.mp4`,
7/7 beats filled real (no slate), 99.56s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (post NB02/NB03 fix)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect,
  independently re-verified via ffprobe/ffmpeg after the fix + recompile)
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 99.56s; mp4
  mtime newer than beat_sheet.json mtime post-fix
- Gate V (visual): pulled frames at t=2/8/12/20/30/40/48/58/70/78/88/96s
  across the full runtime, plus targeted crops of the NB02/NB03 defect and
  its fix. B00 (writer, "score"→"sort" correction visible and settled,
  "@HumanitariansAI" overlay present per hai's channel-title law), NB01
  (chips legible, arrows and caption clean), NB02 (post-fix:
  "identify"→"checked"→"escalated", all legible, no glyph collision), NB03
  (post-fix: "parsed issue"→"flagged"→"sent to counsel", all legible, no
  collision), BCRY (carry-out quote + sparkline "Sorts. Never scores." read
  clean), BHTF (correct topic "LEGAL-RISK-ASSESSMENT · ANTHROPIC SKILL",
  correct title "It Sorts the Risk. It Doesn't Score It.", @HumanitariansAI
  folder label, paste-ready prompt legible), BOUT (OutroSeries:
  "LEGAL-RISK-ASSESSMENT · @HumanitariansAI" eyebrow, correct title
  restate, crimson underline, no truncation). No remaining blockers.

  Noted, not a new defect: OutroSeries renders on flat white rather than
  the true humanitarians cream/terracotta palette — the same componentry
  gap already logged unremarked on multiple `knowledge-work-plugins`
  siblings (the component exposes only `eyebrow`/`line` props, no palette
  prop).

Metadata file written:
`knowledge-work-plugins--claude-liam-legal-risk-assessment.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `knowledge-work-plugins` key
directly (an exact, direct prefix match — no fallthrough to `hai-simple`
or `_default` needed). Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
