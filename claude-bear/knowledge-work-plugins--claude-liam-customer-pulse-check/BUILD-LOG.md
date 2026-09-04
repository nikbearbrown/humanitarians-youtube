# BUILD-LOG — knowledge-work-plugins--claude-liam-customer-pulse-check

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-customer-pulse-check/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `customer-pulse-check`
Claude Skill, from the `knowledge-work-plugins` book — already fully built,
no SCRIPT.md; source `beats[*].narration_text` served as the locked
script). Built entirely fresh this invocation — only SUBJECT.json existed
on pickup. The source's `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/customer-pulse-check/SKILL.md`)
is not present on this machine (same situation as several
`knowledge-work-plugins` siblings); the source sheet's own narration is
intact and specific — not a truncated batch placeholder — so it carried
the facts needed directly, no reconstruction required.

Question, facts, and full body argument carried over unchanged:
customer-pulse-check synthesizes themes from PayPal disputes, HubSpot
tickets, and review exports into a top-3 fixable issues list with drafted
response templates, and accepts an optional since-date argument; a skill is
a folder Claude reads before it works, containing one file (SKILL.md)
written in plain language, no hidden logic; the instructions live in a
Steps section, executed in order, no branching unless a step says so; same
input produces the same output every run; the skill only handles what its
file specifies. B00 replaced the source's `ClaudeComposerAsk` typed-ask
cold open with `BrutalistHesitantWriter` (WRITER LAW: "send" → "draft" —
the newcomer's wrong guess that Claude resolves the customer's complaint
end to end, corrected toward the actual mechanism: the skill only finds
the pattern and drafts a reply, and sending it stays a person's call).
Register re-registered Teardown → Plain: the source's B03 "gets it right:
repeatable results / what it bites: anything outside the spec" framing was
restated in NB03 as a plain mechanism-and-boundary fact (what the skill
finds and drafts, and what it declines to decide), per the NO JUDGMENT
register check. BVDT's verdict facts (same input → same output every run;
limited to what the file specifies) were merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW. BHTF's prompt was adapted, not copied verbatim: the
source asked the viewer to "read the customer-pulse-check skill," which
requires a plugin install a general viewer won't have, so this redo
substitutes an equivalent, actually paste-ready prompt exercising the same
find-before-draft-before-send habit without depending on any specific
Skill file. Close re-skinned to @HumanitariansAI (`OutroSeries`).

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
customer-pulse-check-specific labels.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 4-line text) reused directly from the `audit-support` sibling's
proven working configuration. `actual_duration_s` (narration) 11.01s +
`lead_silence_s` 0.8 gave the writer an 11.81s window; rendered clip
extended to 11.0s, comfortably clearing the ≥8s TIMING LAW floor. Verified
by frame pulls at t=2.0s ("send" doomed in terracotta, mid-type), t=5.0s
(correction to "draft" already settled), t=9.0s and t=11.0s (full corrected
question "Does Claude draft replies to unhappy customers?" settled and
legible, holding to the end of the clip) — correction lands and settles
well inside the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00); NB01–NB03 rendered via `render_scenes.py`
(foreground); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` — the
invocation exceeded the tool's 120s timeout and was moved to background by
the harness automatically; blocked on it via `TaskOutput` (block=true)
before proceeding, per the COMPLETION LAW's foreground-render rule, and
confirmed exit code 0 with all four beats reporting `ok` before moving on.

**GATE T (type_check.py): PASS, 0 FAILs on the first automated run** — but
a manual Gate V frame pull at t=33s caught a real legibility defect the
checker missed: NB02's accented middle chip, originally labelled "grouped"
(bold, EB Garamond), rendered with the "gr"/"ouped" glyphs colliding into
an unreadable smear — the same bold-weight kerning-collapse class of
checker-blind-spot defect already documented for the `audit-support`
sibling's "co­ntrol" collision (the automated checker's kerning/min-size
tables don't cover every glyph-pair and weight combination). **First fix
attempt ("sorted") also collided** ("so"/"rted" bunching) — same defect
class, different letter pair. **Root-caused and fixed on the second
attempt:** replaced with "ranked" (matches the mechanism: rank the top
three), re-rendered NB02 only, recompiled with `--force`, re-ran
`type_check.py` (still PASS, 0 FAILs) and re-pulled the frame to confirm
clean spacing with no glyph collision before accepting the cut.

Compiled:
```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-customer-pulse-check.mp4`,
7/7 beats filled real (no slate), 89.5s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (post NB02 fix)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 89.5s; mp4
  mtime (1788444168+) newer than beat_sheet.json mtime
- Gate V (visual): pulled frames at t=2/5/9/11/18/25/33(fixed twice)/42/
  55/61/70/78/85/88s across the full runtime plus the targeted B00
  correction-timing checks above. B00 (writer, correction visible and
  settled, "@HumanitariansAI" overlay present per hai's channel-title
  law), NB01 (chips legible, arrows and caption clean), NB02 (post-fix:
  "pulled" → "ranked" → "drafted", all legible, no overlap), NB03 (chips
  legible, "top 3 themes"/"drafted"/"sent by a person" all clean), BCRY
  (carry-out quote + sparkline "Drafts. Never sends." read clean), BHTF
  (correct topic "CUSTOMER-PULSE-CHECK · ANTHROPIC SKILL", correct title
  "It Drafts the Reply. It Never Sends It.", @HumanitariansAI folder
  label, paste-ready prompt legible), BOUT (OutroSeries: "CUSTOMER-
  PULSE-CHECK · @HumanitariansAI" eyebrow, correct title restate, crimson
  underline, no truncation). No remaining blockers.

Metadata file written:
`knowledge-work-plugins--claude-liam-customer-pulse-check.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `knowledge-work-plugins` key
directly (an exact, direct prefix match — no fallthrough to `hai-simple`
or `_default` needed). Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-03 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to
`knowledge-work-plugins--claude-liam-customer-pulse-check-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-customer-pulse-check/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-customer-pulse-check/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) to the
humanitarians-youtube clone.

**Status: DELIVERED.**
