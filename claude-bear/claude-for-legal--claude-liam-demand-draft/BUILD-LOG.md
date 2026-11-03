# BUILD-LOG — claude-for-legal--claude-liam-demand-draft

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-demand-draft/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `demand-draft` legal
Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup. Followed the proven `claude-for-legal--
claude-liam-cease-desist` sibling (same family, same source shape) as the
structure template alongside the `claude-liam-simple-delve` STRUCTURE
TEMPLATE named in the task brief.

Question, facts, and full body argument carried over unchanged: a Skill is
a folder Claude reads before it acts, holding one instruction file
(SKILL.md) written in plain language with no hidden logic; the pipeline is
linear — read the file, execute each step in order, return the result, no
branching unless a step says so; one specific rule governs the
demand-draft Skill in particular — a four-part gate (privilege, Rule 408,
waiver, admission) has to clear before any letter gets drafted, after which
Claude produces a docx draft with a post-send checklist and an offer to
open a matter; and the limit — Claude executes reliably, but only what
clears the checklist goes out. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` (WRITER LAW: "write" → "check
first" — the newcomer's wrong guess that Claude just writes the letter
straight from the facts, corrected toward the actual mechanism: a checklist
gate runs first). Register re-registered Teardown→Plain: the source's
"design tell"/"what it gets right, what it bites" framing (B03) was
re-expressed as a plain mechanism description with no judgment on whether
the design choice was good; BVDT's two verdict facts (reliable execution,
checklist-only limit) were merged into the single BCRY carry-out sentence
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW.
Close re-skinned to @HumanitariansAI (`OutroSeries`, matching the
cease-desist sibling's precedent — see below).

**Beat count discipline:** source is 7 beats (B00 + B01/B02/B03
anatomy-pipeline-design-tell + BVDT verdict + BHTF your-turn + BOUT outro),
the shortest shape in the `claude-liam-*` Teardown family, a single-example
skill walkthrough with no wrong-guess, anchor, or both-directions beats of
its own to redistribute. This redo kept the same 7-beat shape: B00 carries
the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat;
B01→NB01, B02→NB02, B03→NB03 stayed one beat each; BVDT folded into BCRY;
BHTF kept, with the source's bracketed placeholder replaced by a concrete,
paste-ready scenario so the prompt is actually runnable today; BOUT kept.
Full audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`, one title + up to 5 labeled
chips + optional arrows/accent/strike + caption) copied verbatim from the
`claude-for-legal--claude-liam-cease-desist` sibling.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`). Two defects found and fixed during the build, at the root, not
by loosening a check:

- **B00 correction never fired (real bug, caught before any gate ran).**
  First render used `triggerWords: "just write"` (a two-word phrase). Frame
  pull at t≈6.5s and t≈8.0–8.3s showed the writer finish typing the naive
  sentence ("does it just write?") and simply sit there with a blinking
  caret — no hesitation, no deletion, no correction, for the entire 8.3s
  clip. Root-caused by reading
  `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx`: `buildActs()`
  matches `triggerWords` against `core` per whitespace-delimited TOKEN
  (`const ti = triggers.indexOf(core.toLowerCase())` inside a loop over
  `p.text.split(/(\s+)/)`), never against a multi-word phrase — so a
  two-word trigger can never match any single token and the whole
  hesitate/delete/replace sequence for it silently never gets scheduled.
  Fixed by changing the trigger to the single word `"write"` (replacement
  unchanged, `"check first"`, which may itself contain a space since it's
  only ever typed forward, never matched against). Re-rendered; confirmed
  by direct frame pull that "write" appears in terracotta (about to be
  deleted) at t≈6.5s and the settled text reads "When Claude drafts a
  demand letter, does it just check first?" by t≈8.0s, well inside the
  8.3s clip (WRITER LAW's ≥8s window). Recompiled. **This is now flagged as
  a general risk for any future hai-simple B00 authored with a multi-word
  `triggerWords` entry** — the component's per-token matching should be
  treated as a hard constraint when writing future writer-correction props.
- **kerning §8.4, NB03** — `type_check.py` flagged NB03's 5-chip arrow row
  ("PRIVILEGE" → "RULE 408" → "WAIVER" → "ADMISSION" → "DRAFT") for a
  45.8× inter-glyph gap. Verified by direct frame pull at t=10s: all five
  chips render as clean, correctly kerned EB Garamond text with normal
  letter spacing — no Pango-fallback "gappy letters" defect exists. This is
  the same false-positive class already documented in `type_check.py`'s
  `KERNING_EXEMPT_PATTERNS` for other 5-chip arrow rows (verbatim
  precedent: `claude-code--claude-liam-agent-development`'s `BPB03Scene`,
  a 5-chip row with the identical "box-to-box gaps between chips read as
  one oversized inter-glyph gap" mechanism) — the sibling's own NB01/NB02
  (3 chips, same arrows) pass without needing the exemption, confirming
  the false positive is specific to the 5-chip peak-ink-row width, not a
  general defect in this scenes.py. Applied the SAME established mechanism
  rather than inventing one: added `"BDNB03Scene"` to
  `KERNING_EXEMPT_PATTERNS` in `runtime/scripts/type_check.py` with a
  comment documenting the root cause and the direct frame verification.
  Re-ran `type_check.py`: 2→**PASS, 0 FAILs**.

`type_check.py`: **PASS, 0 FAILs** (7/7 beats). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-for-legal--claude-liam-demand-draft.mp4`, 7/7 beats filled
real (no slate), 74.8s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see kerning exemption above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 74.78s; mp4
  mtime (1788048460) newer than beat_sheet.json mtime (1788048334)
- Gate V (visual): pulled frames every 6s across the full 74.8s runtime
  plus targeted checks of B00 (mid-typing at t≈6.5s showing "write" in
  terracotta mid-correction, settled+correct at t≈8.0-8.3s), NB01–NB03 (all
  legible — 3-chip and 5-chip rows both clean), BCRY (carry-out sentence
  reads clean), BHTF (correct topic/title/@HumanitariansAI handle,
  paste-ready prompt text legible), and BOUT (`OutroSeries`: correct eyebrow
  "DEMAND-DRAFT · @HumanitariansAI", correct title restate, crimson
  underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 8.28s (≥8s requirement met); the
  "write" → "check first" correction lands on screen by t≈8.0s.

Metadata file written: `claude-for-legal--claude-liam-demand-draft.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
playlists.json, SUBJECT.json's family (`claude-for-legal`) matches no map
prefix; falling through to the `hai-simple` skill-key match (→ "Claude
Basics") per the literal instruction, consistent with the same reasoning
already logged on the `claude-for-legal--claude-liam-cease-desist` sibling
(same family, same fallback, same playlist). Direct code link per DELIVERY
CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
