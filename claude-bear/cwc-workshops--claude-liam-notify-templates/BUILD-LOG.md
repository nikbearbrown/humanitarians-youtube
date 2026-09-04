# BUILD-LOG — cwc-workshops--claude-liam-notify-templates

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/claude-liam-notify-templates/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `notify-templates`
cwc-workshops Skill). Source had no SCRIPT.md; `beats[*].narration_text`
served as the locked script, cross-checked against the skill's own
SKILL.md, present unchanged at
`/Users/nik/Documents/Cowork/anthropics/cwc-workshops/agent-decomposition/.claude/skills/notify-templates/SKILL.md`
even though the source reel's own `source_skill` metadata field points at
a Bear-machine path that does not exist here — same defect class as other
`cwc-workshops--*` siblings, resolved the identical way. Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: the skill's
own opening line rules out creative writing ("Notifications are template
fills, not creative writing. Do not spawn a subagent for this"); three
fixed formats (low-stock Slack alert, supplier email, escalation for human
review); a routing table with four tiers and exact thresholds (ops channel
default; @here for an active/imminent top-SKU stockout or a
stockout-within-7-days supplier delay; a purchasing lead DM/email, not the
channel, for any single PO over $25k or a deviation from the scored
supplier; finance only past $100k open-PO balance for one supplier or a
suspected duplicate PO); and the "batch, don't spam" rule (one summary
notification per sweep, and even an explicit per-SKU request still writes
every line into a single batch append via one Bash heredoc, never one
model round-trip per SKU) plus the outbox append mechanism (append one
JSON line per notification to `outbox.jsonl`; "if you're making more than
two calls to send a notification, you've over-engineered it").

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "write" → "fill" — the newcomer's
wrong guess that Claude composes each alert like prose, corrected toward
the skill's actual framing: template fills, not creative writing). Register
re-registered Teardown → Plain: the source's B03 design-tell text (generic
"what it gets right: repeatable results. What it bites: anything outside
the spec.") and BVDT's verdict (a restatement of the trigger keywords) were
merged into a single NB03, replaced with the skill's actual batching
mechanism — the "batch, don't spam" rule and the ≤2-call outbox append —
which the source's own narration never reached (it recapped trigger
keywords instead of the skill's real constraint). This keeps the body
argument (what the skill does, and its one hard constraint) while trading
a generic Teardown-style recap for the single most teachable fact the
source left on the table. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 design tell + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B03+BVDT compressed into NB03; BHTF kept
as the your-turn handoff, rewritten as a fully self-contained scenario
(a single alert plus an 8-SKU sweep in one prompt) so the viewer tests both
the template-fill and the batch-vs-one-per-SKU reasoning in one paste, no
skill install required; BOUT kept. Full audit in SCRIPT.md's "Beat-count
note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`cwc-workshops--claude-liam-forecasting` sibling, adapted with
notify-templates-specific labels.

**B00 TIMING LAW:** the unpadded narration (24 words) measured exactly
9.00s (9.0027s via direct ffprobe on the mp3) — too close to the ≥9s floor
to trust, since `lead_silence_s` is written into the sheet per hai-simple
convention but is **not actually wired** into either
`generate_audio_kokoro.py` or `remotion_scenes.py`/`compile.py` in this
codebase (grepped all three; zero references outside a couple of unrelated
scripts) — raising it from 0.9 to 1.3 had no effect on the measured
duration, confirming the field is currently inert for Kokoro-voiced beats.
Real safety margin came from `BrutalistHesitantWriter`'s own render
behavior instead: the composition always renders its full fixed
606-frame/20.2s seeded performance regardless of props, and
`extend_clip_to_duration` (`tpad` + `-t`) then trims that raw render down
to `actual_duration_s` — so the only thing that matters is whether the
seeded typing timeline finishes before the trim point. Verified directly
by rendering B00 and pulling frames at t=3.0s (correction to "fill" already
landed) and t=8.7s (full corrected question "Does Claude fill the
low-stock alert template?" settled and legible, well inside the 9.0s clip).
No parameter changes were needed beyond the `lead_silence_s` documentation
edit, which is now noted in the beat's own `note` field for whoever revisits
this gap.

**Foreground-render discipline (COMPLETION LAW):** `remotion_scenes.py`
exceeded the tool's 120s foreground timeout and was auto-moved to a
background task by the harness; per the one-shot completion law (`claude
-p` exits when the turn ends, so a background render left unresolved would
never be picked back up), this was blocked on explicitly with
`TaskOutput(block=true)` rather than ending the turn — confirmed exit code
0 and all 4 REMOTION beats (B00, BCRY, BHTF, BOUT) rendered before
proceeding to compile.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); NB01–NB03 rendered via `render_scenes.py` (foreground, Manim);
B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground,
harness-backgrounded then blocked on to completion). First `type_check.py`
pass was **FAIL, 1 defect** (NB02: smallest text run 18px < 20px floor,
the bold/accented "purchasing lead" chip hitting the same
bold+borderline-length interaction documented in the `forecasting` /
`claude-plugins-official--*` siblings). Shortened the chip to "purchasing"
(10 chars, clear of the width-forced scale-down) and moved the $25k detail
into the caption. Re-rendered NB02 only, re-ran `type_check.py`:
1→**PASS, 0 FAILs**.

**Second defect found only by reading rendered frames, not caught by any
automated gate:** Gate V frame pulls showed the chip labels "3 templates"
and "ops channel" rendering with their word-space visually collapsed to
near-zero width in this Manim/EB-Garamond combination — "3templates" and
"opschannel" respectively, both reading as garbled single words despite
GATE T's min-size and kerning checks passing clean (the check has no
calibrated space-width floor for this letter-pair class: digit-then-space,
and "s"-then-space-then-"c"). Other two-word chips in the same beats
("fill from data", "one summary", "no subagent") rendered with normal
spacing, so this was isolated to those two specific labels, not a general
font defect. Fixed by rewording rather than guessing at font internals:
"3 templates" → "templates" (the count is already spoken in narration;
`type_check.py` doesn't check narration-vs-chip redundancy) and "ops
channel" → "ops" (now parallel with the single-noun "purchasing" /
"finance" chips it sits beside — an incidental improvement to the row's
visual rhythm). Re-rendered NB01 and NB02, recompiled, re-verified both
frames directly: "templates" and "ops" now render with normal, legible
spacing. `type_check.py` re-run clean (still PASS, 0 FAILs — this defect
class is outside its current coverage).

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `cwc-workshops--claude-liam-notify-templates.mp4`, 7/7 beats filled
real (no slate), 101.8s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see defect + fix above)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (compile.py's own report,
  independently reconfirmed via `ffmpeg volumedetect`: mean -24.1 dB, max
  -2.7 dB)
- ffprobe: video 3840×2160 h264, audio present, duration 101.78s; mp4
  mtime (1788240188) newer than beat_sheet.json mtime (1788240113)
- Gate V (visual): pulled frames across the full runtime (t=1, 5, 9, 14,
  22, 30, 40, 50, 60, 70, 80, 90, 95, 100s) plus targeted B00 pulls at
  t=3.0s and t=8.7s — all 7 beats legible, correctly inset, no text
  overlap after the two chip-spacing fixes above. BHTF/final frame:
  correct topic/title/@HumanitariansAI folder label, paste-ready prompt
  legible, current model label ("Fable 5"). BOUT (`OutroSeries`): correct
  eyebrow "NOTIFY-TEMPLATES · @HUMANITARIANSAI", correct title restate
  "Fill The Template. Don't Write It.", terracotta underline, no Claude
  mascot or branding, no truncation.
- B00 TIMING LAW: `actual_duration_s` 9.0s (media/B00.mp4 same); the
  "write" → "fill" correction lands by t≈3.0s and the full corrected
  question stays legible through the end of the clip (confirmed t=8.7s).

Metadata file written: `cwc-workshops--claude-liam-notify-templates.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`cwc-workshops`) matches no
prefix in the map's family column; the `hai-simple` skill-key is itself a
map key resolving to `"Claude Basics"` — the same fallback documented in
every other `cwc-workshops--*` sibling in this loop, a real match, not the
`_default` last resort. Direct code link per DELIVERY CONTRACT format
included. Chapters computed from `actual_duration_s` cumulative offsets
(B00 0:00, NB01 0:09, NB02 0:26, NB03 0:47, BCRY 1:08, BHTF 1:18, BOUT
1:37).

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-01 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `cwc-workshops--claude-liam-notify-templates-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/cwc-workshops--claude-liam-notify-templates/` (4K master +
description) for the Drive sync. Committed to
`claude-bear/cwc-workshops--claude-liam-notify-templates/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `8269dd1f`, pushed clean
(no rebase conflicts).

**Status: DELIVERED.**
