# BUILD-LOG — knowledge-work-plugins--claude-liam-compliance-check

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-compliance-check/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `compliance-check`
Claude Skill, from a `knowledge-work-plugins` book legal plugin set —
already fully built, no SCRIPT.md; source `beats[*].narration_text` served
as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup. The source's `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/legal/skills/compliance-check/SKILL.md`)
is not present on this machine (same situation as the
`knowledge-work-plugins--claude-liam-audit-support` sibling and others);
the source sheet's own narration already carried the facts needed, so no
reconstruction was required.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works, containing one file (SKILL.md)
written in plain language, no hidden logic; the instructions live in a
Steps section, executed in order, no branching unless a step says so;
`compliance-check`'s specific job is to run a compliance check on a
proposed action, product feature, or business initiative, surfacing
applicable regulations, required approvals, and risk areas — used when
launching a feature that touches personal data, when marketing or product
proposes something with regulatory implications, or when the applicable
approvals and jurisdictional requirements need to be known before
proceeding; same input produces the same output every run; the skill only
handles what its file specifies. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "clear" → "flag" — the newcomer's wrong guess that Claude
itself signs off on the feature, corrected toward the actual mechanism:
the skill only surfaces what applies and hands the approval to a person).
Register re-registered Teardown → Plain: the source's B03 "gets it right:
repeatable results / what it bites: anything outside the spec" framing
was restated in NB03 as a plain mechanism-and-boundary fact (what the
skill surfaces and flags, and what it declines to decide), per the NO
JUDGMENT register check. BVDT's verdict facts (same input → same output
every run; limited to what the file specifies) were merged into the
single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW. BHTF's prompt was adapted, not copied
verbatim: the source asked the viewer to "read the compliance-check
skill," which requires a plugin install a general viewer won't have, so
this redo substitutes an equivalent, actually paste-ready prompt
exercising the same surface-before-approve habit without depending on any
specific Skill file. Close re-skinned to @HumanitariansAI (`OutroSeries`).

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
`knowledge-work-plugins--claude-liam-audit-support` sibling, adapted with
compliance-check-specific labels.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 4-line text) reused directly from the
`knowledge-work-plugins--claude-liam-audit-support` sibling's proven
working configuration. `actual_duration_s` (narration) 11.26s +
`lead_silence_s` 1.0 gave the writer a 12.26s window; rendered clip
extended to 11.3s, comfortably clearing the ≥8s TIMING LAW floor. Verified
by frame pulls at t=2s ("clear" mid-type, terracotta accent visible, not
yet corrected) and t=9s (full corrected question "Does Claude flag my
feature for launch?" settled and legible, holding to the end of the clip)
— correction lands and settles well inside the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00); NB01–NB03 rendered via `render_scenes.py`
(foreground); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` — the
invocation exceeded the tool's 120s timeout and was moved to background by
the harness automatically; blocked on it via `TaskOutput` (block=true)
before proceeding, per the COMPLETION LAW's foreground-render rule, and
confirmed exit code 0 with all four beats reporting `ok` before moving on.

**GATE T (type_check.py): PASS, 0 FAILs on the first automated run** — but
a manual Gate V frame pull at t=35s caught a real legibility defect the
checker missed: NB02's accented middle chip, originally labelled
"surfaced" (bold, EB Garamond), rendered with the "r"/"f" glyphs colliding
into an unreadable smear — the same class of checker-blind-spot defect the
`knowledge-work-plugins--claude-liam-audit-support` sibling hit with
"control" (a bold-weight kerning collapse the automated checker's
kerning/min-size tables don't cover for every glyph-pair). **Root-caused
and fixed:** replaced the two-syllable label with a single safe word,
"checked" — no "rf" letter-pair, matching the pattern already proven safe
elsewhere in this reel set (this reel's own "flagged" and the
audit-support sibling's "tested" are both single bold tokens that render
clean). Re-rendered NB02 only (`render_scenes.py`, beat cached-skip on
NB01/NB03), recompiled with `--force`, re-ran `type_check.py` (still PASS,
0 FAILs) and re-pulled the fixed frame to confirm clean spacing with no
glyph collision before accepting the cut.

Compiled:
```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-compliance-check.mp4`, 7/7
beats filled real (no slate), 95.6s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (post NB02 fix)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 95.6s; mp4
  mtime (1788414921, then re-stamped on the NB02 recompile) newer than
  beat_sheet.json mtime
- Gate V (visual): pulled frames at t=2/9/15/35(fixed)/45/55/65/75/85/90/93s
  across the full runtime plus the targeted B00 correction-timing checks
  above. B00 (writer, correction visible and settled, "@HumanitariansAI"
  overlay present per hai's channel-title law), NB01 (chips legible,
  arrows and caption clean), NB02 (post-fix: "identify action" →
  "checked" → "write it up", all legible, no overlap), NB03 (chips
  legible, "flagged"/"approved by legal" clean, no glyph collision), BCRY
  (carry-out quote + sparkline "Surfaces. Never approves." read clean),
  BHTF (correct topic "COMPLIANCE-CHECK · ANTHROPIC SKILL", correct title
  "It Surfaces the Risk. It Doesn't Approve.", @HumanitariansAI folder
  label, paste-ready prompt legible), BOUT (OutroSeries: "COMPLIANCE-CHECK
  · @HumanitariansAI" eyebrow, correct title restate, crimson underline,
  no truncation). No remaining blockers.

Metadata file written:
`knowledge-work-plugins--claude-liam-compliance-check.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `knowledge-work-plugins` key
directly (an exact, direct prefix match — no fallthrough to `hai-simple`
or `_default` needed). Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
