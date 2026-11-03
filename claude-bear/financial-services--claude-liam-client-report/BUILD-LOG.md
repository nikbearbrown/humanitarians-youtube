# BUILD-LOG — financial-services--claude-liam-client-report

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-client-report/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `client-report`
financial-services Skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: client-report
is a Skill folder holding one SKILL.md file, written in plain language with
no hidden code, that generates client-facing performance reports with
portfolio returns, an allocation breakdown, and market commentary, timed for
quarterly or annual delivery, triggered on phrases like "client report" /
"performance report" / "quarterly report for [client]"; the pipeline lives
in the file's Steps section — Claude reads the file, runs each step in
order, returns the result, linear with no branching unless a step itself
says so; and the file's coverage is what repeats — the same input produces
the same report every run, but a request outside the file's stated scope has
no instruction to fall back on, so Claude reasons past the file on its own.
B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "app" → "skill" — the newcomer's
wrong guess that a repeatable, domain-specific capability like client-report
implies a built-in finance app or hidden logic, corrected toward the actual
mechanism: it's a plain-text file of instructions Claude reads and follows).
Register re-registered Teardown→Plain: the source's B03 "Here is the
Teardown moment... what it gets right... what it bites" framing was
rewritten in NB03 as a direct both-directions mechanism-and-consequence
description (same input → same report; uncovered request → Claude reasons
past the file) with no verdict language. BVDT's verdict facts (repeatable
execution, same input → same output, the limit being only what the file
specifies) were merged into the single BCRY carry-out sentence rather than
kept as a separate bulleted artifact card, per CARRY-OUT LAW. BHTF was
re-purposed from the source's skill-specific paste-in (named the exact
client-report trigger phrase, not runnable by a general viewer without that
specific financial-services plugin installed) to a generalized, genuinely
paste-ready prompt: asking Claude to draft a SKILL.md for the viewer's OWN
recurring report and separate what repeats from what needs judgment — same
mechanism, no special access required. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design-tell mechanism + BVDT verdict + BHTF your-turn
+ BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each (narration was already close to Plain in the
source, no verdict language to strip); B03's Teardown framing compressed
into NB03 as the reel's both-directions beat; BVDT folded into BCRY; BHTF
kept, generalized to a runnable prompt; BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01-NB03) built on the shared generic "chip row" Manim
template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with client-report-specific labels.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00 (BrutalistHesitantWriter, text "Does Claude's / client-report
app / understand finance, / or just follow steps?", trigger "app" →
"skill") rendered at 12.01s on the first attempt using the rate settings
already validated by the agent-development sibling's fix (42ms/char, 4%
mistakeRate, 8% hesitateBetween) rather than repeating that sibling's
original slower/higher-rate failure — no B00 defect this time. Frame pulls
at t=2.5s and t=10s confirmed the correction ("app" struck in terracotta,
then settled as "skill") lands well inside the clip and the full corrected
question stays legible to the end. BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` (the full-sheet run exceeded the tool's 120s timeout
and was moved to background by the harness automatically — blocked on it via
`TaskOutput` before proceeding, per the COMPLETION LAW's foreground-render
rule); NB01-NB03 rendered via `render_scenes.py` (foreground, all completed
inside the timeout).

First `type_check.py` pass was **FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB03** — smallest text run measured 8px, well under the
  20px floor. Root cause: NB03's original two chip labels ("in the file:
  repeats", "not in the file: judgment", 21 and 26 characters) landed in the
  ≤22-char and >22-char font-size buckets respectively (26/18pt in
  `_chip()`), and at only 2 chips the chip width (3.2, the per-chip max) left
  a tight 0.82-width text budget that forced the longer label's already-small
  18pt run to scale down further to fit — well under the floor. Fixed by
  shortening both labels to `"in scope"` / `"out of scope"` (8/12 chars,
  landing in the ≤14-char 26pt bucket for both) — re-rendered NB03 only
  (NB01/NB02 untouched), and `beat_sheet.json`'s
  `graphic.production_viz.chips` for NB03 was synced to the fixed wording
  directly (not via a full `build_beat_sheet.py` re-run, which would have
  discarded the already-measured audio durations and render stamps) before
  the recompile, per COMPLETION LAW.

`type_check.py` went 1→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `financial-services--claude-liam-client-report.mp4`, 7/7 beats
filled real (no slate), 90.1s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 90.14s; mp4
  mtime (1788273468) newer than beat_sheet.json mtime (1788273340)
- Gate V (visual): pulled frames every ~5-8s across the full runtime
  (t=1,5,10,16,22,26,32,40,48,55,62,68,74,80,86s) plus the two B00 timing
  checks above. B00 correction legible and complete before end of clip;
  NB01-NB03 chips all legible and parallel-sized post-fix (including the
  recompiled NB03); BCRY carry-out sentence and sparkline read clean; BHTF
  correct topic/title/@HumanitariansAI handle, full paste-ready prompt
  legible with no overlap; BOUT (OutroSeries) correct eyebrow "CLIENT REPORT
  · @HumanitariansAI" and title restate. No blockers. Noted, not a defect:
  OutroSeries renders on flat white rather than the humanitarians cream
  ground — same shared-component behavior already logged unremarked across
  the `bond-relative-value`/`buyer-list`/`catalyst-calendar`/`cim-builder`
  siblings in this family.
- B00 TIMING LAW: `actual_duration_s` 12.0s (≥8s requirement met); the
  "app" → "skill" correction lands on screen well before the clip's end and
  the full corrected question stays legible for the remainder.

Metadata file written: `financial-services--claude-liam-client-report.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per `playlists.json`,
SUBJECT.json's family (`financial-services`) matches none of the map's
family prefixes (no `startswith` hit), so the worker fell through to the
`hai-simple` skill-key entry (`"hai-simple": "Claude Basics"`) per the
documented fallback chain, before the final `_default` resort — consistent
with the fallback order used by prior hai-simple redo builds when the source
book's family has no dedicated playlist entry. Direct code link per DELIVERY
CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
