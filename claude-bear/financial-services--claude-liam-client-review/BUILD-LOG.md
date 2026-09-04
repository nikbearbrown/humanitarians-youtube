# BUILD-LOG — financial-services--claude-liam-client-review

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-client-review/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `client-review`
financial-services Skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged:
client-review is a Skill folder holding one SKILL.md file, written in
plain language with no hidden logic, that prepares client review meetings
with a portfolio performance summary, allocation analysis, talking points,
and action items, pulling account data into a concise meeting-ready format
before quarterly reviews, annual checkups, or ad-hoc client meetings,
triggered on phrases like "client review" / "meeting prep for [client]" /
"quarterly review"; the pipeline lives in the file's Steps section — Claude
reads the file, runs each step in order, returns the result, linear with
no branching unless a step itself says so; and the file's coverage is what
repeats — the same account data produces the same meeting-ready packet
every run, but a request outside the file's stated scope has no
instruction to fall back on, so Claude reasons past the file on its own.

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "app" → "skill" — the newcomer's
wrong guess that a repeatable, domain-specific capability like client-review
implies a built-in portfolio analysis app that decides what matters,
corrected toward the actual mechanism: it's a plain-text file of
instructions Claude reads and follows, which assembles a fixed packet
rather than exercising judgment on the portfolio). Register re-registered
Teardown→Plain: the source's B03 "Here is the Teardown moment... what it
gets right... what it bites" framing was rewritten in NB03 as a direct
both-directions mechanism-and-consequence description (same account data →
same packet; uncovered request → Claude reasons past the file) with no
verdict language. BVDT's verdict facts (repeatable execution, same input →
same output, the limit being only what the file specifies) were merged
into the single BCRY carry-out sentence rather than kept as a separate
bulleted artifact card, per CARRY-OUT LAW. BHTF was re-purposed from the
source's skill-specific paste-in (named the exact client-review trigger
phrase, not runnable by a general viewer without that specific
financial-services plugin installed) to a generalized, genuinely
paste-ready prompt: asking Claude to draft a SKILL.md for the viewer's OWN
recurring meeting and separate what repeats from what needs judgment — same
mechanism, no special access required. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

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

All 3 GRAPHIC beats (NB01-NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`financial-services--claude-liam-client-report` sibling, adapted with
client-review-specific labels and content.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`). B00 (BrutalistHesitantWriter, text "Does Claude's / client-review
app / analyze the portfolio, / or build the packet?", trigger "app" →
"skill") rendered at 12.8s on the first attempt using the rate settings
already validated by the client-report/agent-development siblings (42ms/char,
4% mistakeRate, 8% hesitateBetween) — no B00 timing defect. Frame pulls at
t=2.5s and t=11.5s confirmed the correction ("app" replaced by "skill")
lands well inside the clip and the full corrected question stays legible to
the end. All Remotion beats (B00/BCRY/BHTF/BOUT) rendered via
`remotion_scenes.py` in one foreground pass (no timeout); NB01-NB03 rendered
via `render_scenes.py` (foreground, all completed inside the timeout).

First `type_check.py` pass was **FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB01** — smallest text run measured 19px, 1px under the
  20px floor. The tool's generic message pointed at "a caption/label," but
  direct inspection of the failing bbox (isolating it from the full sorted
  list, not the last-iterated crop) showed it was the lowercase "i" in the
  chip label "client-review" rendering with its dot detached from the stem
  at the chip's default 26pt font size — an EB Garamond/Manim
  anti-aliasing artifact, not an actual legibility problem (the word reads
  clearly to a human at every beat's on-screen size). Ruled out the
  caption text and the trailing "/" in the original "client-review/" label
  as candidates first (both visually and via direct bbox coordinates)
  before finding the real cause. Fixed by raising `_chip()`'s font-size
  brackets from 26/22/18 to 30/24/20pt across all three chip-row beats,
  clearing the floor by 3-5px margin on every beat. Re-rendered all three
  Manim beats (NB01-NB03, since the shared `_chip()` helper affects all of
  them) and recompiled before re-running `type_check.py`, per COMPLETION
  LAW (no gate re-run on a stale render).

`type_check.py` went 1→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `financial-services--claude-liam-client-review.mp4`, 7/7 beats
filled real (no slate), 96.5s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 96.48s; mp4
  mtime (1788275016) newer than beat_sheet.json mtime (1788274438)
- Gate V (visual): pulled frames across the full runtime
  (t=1,6,15,20,27,40,55,62,70,78,85,90,95s) plus the two B00 timing checks
  above. B00 correction legible and complete before end of clip; NB01-NB03
  chips all legible post-fix, arrows/underlines clean, no overlap; BCRY
  carry-out sentence and sparkline read clean; BHTF correct topic/title/
  @HumanitariansAI handle, full paste-ready prompt legible with no overlap;
  BOUT (OutroSeries) correct eyebrow "CLIENT REVIEW · @HumanitariansAI" and
  title restate "Same Data, Same Packet." No blockers. Noted, not a defect:
  OutroSeries renders on flat white rather than the humanitarians cream
  ground — same shared-component behavior already logged unremarked across
  multiple siblings in this family (client-report, bond-relative-value,
  buyer-list, catalyst-calendar, cim-builder).
- B00 TIMING LAW: `actual_duration_s` 12.8s (≥8s requirement met); the
  "app" → "skill" correction lands on screen well before the clip's end and
  the full corrected question stays legible for the remainder.

Metadata file written: `financial-services--claude-liam-client-review.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per `playlists.json`,
SUBJECT.json's family (`financial-services`) matches none of the map's
family prefixes (no `startswith` hit), so the worker fell through to the
`hai-simple` skill-key entry (`"hai-simple": "Claude Basics"`) per the
documented fallback chain, before the final `_default` resort — consistent
with the fallback order used by prior hai-simple redo builds (e.g. the
client-report sibling) when the source book's family has no dedicated
playlist entry. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-01 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `financial-services--claude-liam-client-review-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/financial-services--claude-liam-client-review/` (4K master
+ description) for the Drive sync. Committed to
`claude-bear/financial-services--claude-liam-client-review/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `6328ae46`, pushed clean
(no rebase conflicts).

**Status: DELIVERED.**
