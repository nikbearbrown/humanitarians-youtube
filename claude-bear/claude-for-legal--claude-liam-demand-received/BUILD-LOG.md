# BUILD-LOG — claude-for-legal--claude-liam-demand-received

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-demand-received/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `demand-received`
legal Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup. Followed the `claude-for-legal--claude-liam-
demand-draft` sibling (same family, same source shape: anatomy/pipeline/
design-tell/verdict/handoff/outro) as the structure template alongside the
`claude-liam-simple-delve` STRUCTURE TEMPLATE named in the task brief —
scenes.py, render_scenes.py, and the beat_sheet.json metadata block were
adapted from that sibling directly.

Question, facts, and full body argument carried over unchanged: a Skill is
a folder Claude reads before it acts, holding one instruction file
(SKILL.md) written in plain language with no hidden logic; the pipeline is
linear — read the file, execute each step in order, return the result, no
branching unless a step says so; the specific mechanism unique to
demand-received is its triage sequence — extract the letter's key fields,
cross-check them against the portfolio, assess merit, present response
options with a recommendation — and when escalation is warranted, hand off
to matter-intake or demand-intake instead of resolving it alone. B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "reply" → "triage it" — the
newcomer's wrong guess that Claude just replies to the demand letter
directly, corrected toward the actual mechanism: it triages first).
Register re-registered Teardown→Plain: the source's "design tell"/"what it
gets right, what it bites" framing (B03) was re-expressed as a plain
mechanism description with no judgment on whether the design choice was
good; BVDT's two verdict facts (reliable triage execution, escalation-only
limit) were merged into the single BCRY carry-out sentence rather than kept
as a separate bulleted artifact card, per CARRY-OUT LAW. Close re-skinned
to @HumanitariansAI (`OutroSeries`, matching every delivered sibling's
precedent).

**Beat count discipline:** source is 7 beats (B00 + B01/B02/B03
anatomy-pipeline-design-tell + BVDT verdict + BHTF your-turn + BOUT outro),
the shortest shape in the `claude-liam-*` Teardown family, a single-example
skill walkthrough with no wrong-guess, anchor, or both-directions beats of
its own to redistribute. This redo kept the same 7-beat shape: B00 carries
the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat;
B01→NB01, B02→NB02, B03→NB03 stayed one beat each; BVDT folded into BCRY;
BHTF kept, with the source's truncated bracketed narration replaced by a
concrete, paste-ready scenario so the prompt is actually runnable today;
BOUT kept. Full audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`, one title + up to 5 labeled
chips + optional arrows/accent/strike + caption) copied verbatim from the
`claude-for-legal--claude-liam-demand-draft` sibling, chip content swapped
to the triage sequence (NB03: EXTRACT → CROSS-CHECK → ASSESS MERIT →
RECOMMEND → ESCALATE, accent on ESCALATE). Chip labels kept short (≤14
chars) and titles/captions kept free of em dashes, per the demand-intake
sibling's documented kerning-false-positive lesson — this paid off: GATE T
passed clean with **zero** exemptions needed on the first run.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`). B00 measured 9.66s (≥8s WRITER LAW threshold met with margin).
B00's `triggerWords` was authored as the single token `"reply"` from the
start (not the two-word phrase that bit the `demand-draft` sibling before
its fix) — direct frame pull at t≈9.2s confirms the writer settles cleanly
on "A demand letter arrives. Does Claude just triage it?" with no leftover
terracotta, and a t≈6s pull shows the mid-hesitation/deletion state firing
correctly. No defects found this build — GATE T and Gate V both passed on
the first render, no re-renders needed.

`type_check.py`: **PASS, 0 FAILs** (7/7 beats, no kerning exemptions
required). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `claude-for-legal--claude-liam-demand-received.mp4`, 7/7 beats
filled real (no slate), 79.6s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs, 0 exemptions needed
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (compile.py's own ffmpeg
  volumedetect gate)
- ffprobe: video 3840×2160, duration 79.581s; mp4 mtime (1788051312) newer
  than beat_sheet.json mtime (1788051199)
- Gate V (visual): pulled 13 frames every 6s across the full 79.6s runtime
  plus targeted pulls of B00 at t≈6s (mid-hesitation, "o" in terracotta
  mid-deletion) and t≈9.2s (settled, correct: "A demand letter arrives.
  Does Claude just triage it?"), and a targeted BOUT pull at t≈77.5s.
  NB01–NB03 (3-chip and 5-chip rows both clean and legible), BCRY (carry-out
  sentence reads clean), BHTF (correct topic/title/@HumanitariansAI handle,
  paste-ready prompt text legible), and BOUT (`OutroSeries`: correct eyebrow
  "DEMAND-RECEIVED · @HumanitariansAI", correct title restate, crimson
  underline, no truncation — renders on flat white rather than the
  humanitarians cream ground, the same already-documented shared-component
  quirk noted on every delivered sibling in this family, not something this
  build needs to fix). No blockers.
- B00 TIMING LAW: `actual_duration_s` 9.66s (≥8s requirement met with
  margin); the "reply" → "triage it" correction lands on screen by t≈9.2s.

Metadata file written: `claude-for-legal--claude-liam-demand-received.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per playlists.json,
SUBJECT.json's family (`claude-for-legal`) matches no map prefix; the
`hai-simple` skill-key fallback resolves to "Claude Basics", consistent
with every delivered sibling in this family. Direct code link per DELIVERY
CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + `deliver.py`) in this same invocation.
