# BUILD-LOG — knowledge-work-plugins--claude-liam-invoice-chase

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-invoice-chase/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `invoice-chase`
small-business Skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

**Source-fidelity finding, disclosed rather than papered over:** the
source's own recorded `SKILL.md` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-
work-plugins/small-business/skills/invoice-chase/SKILL.md`) is on a
different machine and not present anywhere in this local `books/` tree
(confirmed by `find`/`grep` across the whole `knowledge-work-plugins` book).
Worse: the source `beat_sheet.json`'s own narration for the
invoice-chase-specific material was never filled in — B00, B03, BVDT, and
BHTF all carry a literal, un-substituted `>` template placeholder where a
concrete detail should be (e.g. B03: "Claude's job: >. What it gets right:
repeatable results."). There was therefore nothing invoice-chase-specific
locked to carry over beyond the *generic* mechanism every Anthropic Skill
shares, which the source's B01/B02/BVDT state unconditionally and which
this redo kept: a Skill is a folder Claude reads before acting; SKILL.md is
the whole instruction set in plain language; Claude executes its steps in
order, no branching unless a step says so; same input produces same output,
every run; the Skill can only do what its file specifies. This redo does
not invent invoice-chase's literal steps (due-date thresholds, reminder
cadence, message tone, etc.) to paper over the gap — NB02 states the gap
directly as the reel's one inference flag. Full disclosure in QUESTION.md's
source-fidelity note and SCRIPT.md's one-flag audit.

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "guesses" → "steps" — the newcomer's
wrong guess that chasing an overdue invoice means Claude improvising
case by case, corrected toward the actual mechanism: Claude follows a
written procedure). Register re-registered Teardown→Plain: the source's
B03 "design tell" (itself only a template placeholder in the source) was
replaced with the one concrete, confirmed constraint the source's own BVDT
states unconditionally — bounded to exactly what the file specifies — kept
as NB03. BVDT's verdict facts (same input/same output every run, limited to
what the file says) were merged into the single BCRY carry-out sentence
per CARRY-OUT LAW rather than kept as a separate bulleted artifact card.
BHTF's source prompt template (`"I want to >. Read the invoice-chase skill
and walk me through..."`) could not be carried over verbatim — its `>` was
never filled in, so there was no locked prompt to preserve — and was
replaced with a genuinely paste-ready prompt: writing a SKILL.md for an
invoice-chase process, then requesting the same "walk me through before you
do it" clause the source called out as mattering. Close re-skinned to
@HumanitariansAI (`OutroSeries`), title changed from the source's generic
"Claude, Invoice Chase." to "Steps, Not Guesses." (restating the carry-out),
matching the `claude-plugins-official--claude-liam-agent-development`
sibling's retitling convention.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design-tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03→NB03 kept as one beat, re-registered to Plain;
BVDT folded into BCRY; BHTF kept, with a genuinely runnable replacement
prompt (source's was an unfilled placeholder); BOUT kept. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with invoice-chase-specific labels.

**B00 TIMING LAW — verified clean on first attempt**, unlike the sibling
precedent (which had to shorten its text after a first-attempt overrun).
Chose conservative typing parameters up front (42ms/char, 4% mistakeRate,
2%/8% hesitate rates) per the fix pattern already proven necessary on that
sibling. Audio measured 10.82s (narration: 33 words + 0.8s lead_silence).
Frame-pulled at t=1s, 2.5s, 4s, 6s, 9s: "guesses" sits doomed in terracotta
at t≈2.5s, the corrected "Does Claude need the right steps to chase an
invoice?" is fully settled and legible by t≈4s, and holds to the end of the
10.83s clip — comfortably past the ≥8s TIMING LAW floor.

**GATE T — two real defects caught by Gate V's manual frame read (not the
automated §8 checks alone) and fixed at the root, not sampling noise:**

1. **min-size §8.1, NB02** — automated GATE T failure: smallest text run
   17px < 20px floor. Root cause: the middle chip's label, "execute in
   order" (17 chars), fell into the 22px font-size bucket and, combined
   with BOLD weight (it's the accented chip) and scale-to-fit shrinking to
   clear the chip's 82%-width margin, rendered under the floor. Fixed by
   shortening the label to "execute" (7 chars, jumps to the 26px bucket) —
   re-rendered NB02 only.
2. **Bold-weight multi-word space collapse, NB03 — NOT caught by the
   automated §8.1/8.4 checks, only by eyeballing the actual frame per Gate
   V's "pull frames and READ them" instruction.** First content pass used
   the accented (BOLD) chip label "what's written"; a frame pull at t≈48s
   showed it rendering as "what'swritten" — the inter-word space
   collapsing to near-zero at BOLD weight in this environment's EB Garamond
   substitution. Suspected the apostrophe first and swapped to "as written"
   — frame-pulled again, same collapse ("aswritten"), which disproved that
   theory: comparing against NB01's bold "SKILL.md" and NB02's bold
   "execute" (both single-token, both clean) against NB03's own non-bold
   two-word chips "same output" / "no improvising" (both clean, spaces
   intact) isolated the actual cause — BOLD weight + a multi-word label is
   what collapses the space, independent of punctuation. Fixed by
   switching the accented chip to a single word, "specified" — re-rendered
   NB03 only, frame-pulled a third time to confirm clean spacing.

`type_check.py` went FAIL (1, the NB02 min-size defect) → PASS, 0 FAILs
after the NB02 fix; the NB03 bold-collapse defect was never flagged by the
automated kerning check (3 beats checked, 0 FAILs throughout) — it was only
visible by reading the actual rendered frame, confirming Gate V's frame-pull
requirement is load-bearing here, not redundant with GATE T.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, one pass, no re-generation needed); NB01–NB03 rendered via
`render_scenes.py` (re-run twice more, each time skipping the two beats
already correct via the script's own `dest.exists()` guard, only
re-rendering the one fixed beat); B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` (foreground, one pass, no re-render needed — all four
Remotion beats were correct on first render). Compiled three times
(`compile.py --force`) as each Manim fix landed, each recompile completing
in the foreground before the next check.

Result: `knowledge-work-plugins--claude-liam-invoice-chase.mp4`, 7/7 beats
filled real (no slate), 85.4s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (after 1 defect fixed — see above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio stream present, duration 85.4s; mp4
  mtime (1788498525) newer than beat_sheet.json mtime (1788498436)
- Gate V (visual): pulled frames across the full runtime (t=5, 17, 32, 48,
  61, 73, 83s) plus targeted B00 checks (t=1/2.5/4/6/9s — correction lands
  and holds) and the two NB02/NB03 re-checks after each fix. All beats
  legible, no overlap, no truncation, correct @HumanitariansAI branding on
  BHTF/BOUT. No blockers remaining.
- B00 TIMING LAW: `actual_duration_s` 10.82s (≥8s requirement met); the
  "guesses" → "steps" correction lands on screen by t≈4.0s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-invoice-chase.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly to
"Extending Claude — Skills, Plugins & Connectors" (no prefix-matching
ambiguity, unlike the `claude-plugins-official` sibling which matched via
`startswith`). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
