# BUILD-LOG — financial-services--claude-liam-kyc-rules

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-kyc-rules/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `kyc-rules` Claude
Skill, from the `financial-services` book's `kyc-screener` plugin — already
fully built, no SCRIPT.md; source `beats[*].narration_text` served as the
locked script). Built entirely fresh this invocation — only SUBJECT.json
existed on pickup.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works, containing one file (SKILL.md)
written in plain language, no hidden logic; the instructions live in a
Steps section, executed in order, no branching unless a step says so;
`kyc-rules`'s specific job is to apply the firm's KYC/AML rules grid to an
already-parsed onboarding record — assign a risk rating, list every rule
outcome with the rule cited, and flag what's missing or escalation-worthy;
it runs only after `kyc-doc-parse` has already produced that parsed
record; it decides nothing, it scores and routes; same input produces the
same output every run; the skill only handles what its file specifies. B00
replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "approve" → "score" — the
newcomer's wrong guess that Claude makes the accept/reject call, corrected
toward the actual mechanism: the skill only scores the file against the
rules grid and hands the decision to a person). Register re-registered
Teardown → Plain: the source's B03 "gets it right: repeatable results /
what it bites: anything outside the spec" framing was restated in NB03 as
a plain mechanism-and-boundary fact (what the skill scores and routes, and
what it declines to decide), per the NO JUDGMENT register check. BVDT's
verdict facts (same input → same output every run; limited to what the
file specifies) were merged into the single BCRY carry-out sentence rather
than kept as a separate bulleted artifact card, per CARRY-OUT LAW. BHTF's
prompt was adapted, not copied verbatim: the source asked the viewer to
"read the kyc-rules skill," which requires a plugin install a general
viewer won't have, so this redo substitutes an equivalent, actually
paste-ready prompt exercising the same score-before-decide habit without
depending on any specific Skill file. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 teardown design-tell + BVDT verdict + BHTF
your-turn + BOUT outro). This redo kept the same 7-beat shape: B00 carries
the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat;
B01→NB01, B02→NB02 kept as one beat each; B03's Teardown framing compressed
into NB03 (a plain mechanism-and-boundary fact); BVDT folded into BCRY;
BHTF kept (prompt adapted, see above); BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim (mechanism,
colors, GATE T exemption notes) from the
`financial-services--claude-liam-break-trace` sibling, adapted with
kyc-rules-specific labels.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 4-line text) reused directly from the
`financial-services--claude-liam-break-trace` sibling's proven working
configuration. `actual_duration_s` (narration) 10.65s + `lead_silence_s`
1.0 gave the writer an 11.65s window; rendered clip extended to 10.7s,
comfortably clearing the ≥8s TIMING LAW floor. Verified by frame pulls at
t=2.0s ("approve" doomed in terracotta, mid-type), t=4.5s (mid-correction,
"score a new clien[t]" typing), t=8.5s and t=10.3s (full corrected question
"Does Claude score a new client's KYC file?" settled and legible, holding
to the end of the clip) — correction lands and settles well inside the
clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00); NB01–NB03 rendered via `render_scenes.py`
(foreground); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` — the
invocation exceeded the tool's 120s timeout and was moved to background by
the harness automatically; blocked on it via `TaskOutput` (block=true)
before proceeding, per the COMPLETION LAW's foreground-render rule, and
confirmed exit code 0 with all four beats reporting `ok` before moving on.

**GATE T (type_check.py) first pass: FAIL, 1 defect (NB03, min-size §8.1),
root-caused iteratively rather than guessed at:**

1. First finding (17px < 20px floor): direct frame inspection (mid-clip
   frame, chip row) showed the accented middle chip's original label
   ("scored and flagged", 19 chars, bold) visibly shrunk smaller than its
   neighbors to fit the fixed chip width — a genuine over-length label, not
   a font-rendering artifact. **Fixed:** shortened to a single connected
   word carrying the same fact and no forced width-scaling — "risk-rated"
   (10 chars, fits the `len<=14` font-size tier without shrinking).
2. Re-check still FAILed (16px < 20px). Rather than keep guessing at font
   sizes, extracted the checker's exact mid-clip sample frame and ran its
   own `visible_text_mask`/`labeled_blobs`/`text_run_bboxes` pipeline
   directly (numpy) to rank every detected text-run bbox by height. The
   smallest run (16px, 27×16px) localized to x≈1415–1442, y≈505–521 —
   inside the third ("reviewed by staff") chip. Cropping and zooming that
   exact region showed the isolated dot of the 'i' in "reviewed" had
   detached from its stem into its own tiny connected-component blob (the
   same glyph-dot failure class documented on sibling reels for italic
   text, here triggered by this serif's dot rendering at this size even
   upright). **Fixed at the root:** replaced "reviewed by staff" with
   "checked by staff" — no dotted letter in the label, same meaning.
   Re-verified directly against `type_check.check_min_size()` before
   re-running the full checker: PASS, min text-run height 21px >= floor
   20px.

`type_check.py` went FAIL→**PASS, 0 FAILs** on the full re-run. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `financial-services--claude-liam-kyc-rules.mp4`, 7/7 beats filled
real (no slate), 93.2s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see defect + fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -3.1 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 93.2s; mp4
  mtime (1788324048) newer than beat_sheet.json mtime (1788323919)
- Gate V (visual): pulled frames at t=5/15/25/35/45/55/65/75/85/91s across
  the full runtime plus the targeted B00 correction-timing checks above.
  B00 (writer, correction visible and settled, "@HumanitariansAI" overlay
  present per hai's channel-title law), NB01/NB02/NB03 (all chips legible
  post-fix, arrows and captions clean, no overlap; t25 caught a natural
  fade-in transition frame, not a defect), BCRY (carry-out quote + sparkline
  "Scores. Never decides." read clean), BHTF (correct topic "KYC-RULES ·
  AML RISK SCREENING SKILL", correct title "It Scores and Routes. It
  Doesn't Decide.", @HumanitariansAI folder label, paste-ready prompt
  legible), BOUT (OutroSeries: "KYC-RULES · @HumanitariansAI" eyebrow,
  correct title restate, crimson underline, no truncation). No blockers.

Metadata file written: `financial-services--claude-liam-kyc-rules.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`financial-services`) matches no
specific vertical prefix in the map (no `finance-`/`financial-` entry
exists), so resolution falls through in map order to the `hai-simple` key
itself (present in the map precisely as this general fallback), which
resolves to "Claude Basics" — reached before `_default` ("Claude Across
the Curriculum") is ever considered, matching the disposition of the
`financial-services--claude-liam-break-trace` sibling exactly. Direct code
link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `financial-services--claude-liam-kyc-rules-4k.mp4` rather than
re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/financial-services--claude-liam-kyc-rules/` (4K master +
description) for the Drive sync. Committed to
`claude-bear/financial-services--claude-liam-kyc-rules/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4).

**Status: DELIVERED.**
