# BUILD-LOG — knowledge-work-plugins--claude-liam-campaign-plan

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/knowledge-work-plugins/youtube/claude-liam-campaign-plan/beat_sheet.json`,
7 beats, brand `claude-liam`, register `Teardown`, `source_skill` pointing
at a `.../marketing/skills/campaign-plan/SKILL.md` on Bear's other
machine — not present in this tree). Read the source's own narration text
in full (it already carries the skill's task and trigger-phrase language
verbatim, since B00/B03/BVDT quote it), plus its metadata; there was no
SCRIPT.md alongside the source sheet to cross-check against. Started with
only `SUBJECT.json` present on pickup — built entirely fresh this
invocation, using the `knowledge-work-plugins--claude-liam-account-research`
sibling as the exact structural precedent (identical source shape:
skill-teardown, 7 beats, B00 already REMOTION `ClaudeComposerAsk` — not
AI-video/pantry — so NO-GENAI/NO-PANTRY LAW required no substitution beyond
the mandated WRITER LAW swap).

Kept beat count (7) and every fact: `campaign-plan`'s `SKILL.md` is the
whole instruction set, one file, the file is the program; the task,
verbatim from source: generate a full campaign brief with objectives,
audience, messaging, channel strategy, content calendar, and success
metrics — always those six pieces; the skill fires only on matching
trigger language (product launch, lead-gen push, awareness campaign,
week-by-week content calendar, translating a marketing goal into a
structured plan); execution is a linear pipeline (read → execute each step
→ return) with no branching unless a step says so; the payoff is
repeatability (same six-piece shape, every run); the limit is exact
(anything outside the spec isn't covered). Remapped the source's B03
Teardown "gets right / bites" framing into a both-directions mechanism fact
(B03: matching triggers run the pipeline; non-matching requests never start
it) with the design-judgment removed, and its BVDT verdict recap into a
single BCRY carry-out sentence per CARRY-OUT LAW. Added the newcomer
wrong-guess move the Teardown source didn't need (Plain register requires
it): that Claude invents a bespoke marketing strategy from creative
judgment, falsified in B01 by the same-shape case (two unrelated products —
a fitness app and a coffee subscription — produce the identical six-piece
output). New anchor (B02→B03): the literal request "plan a launch campaign
for a new fitness app" walked through READ/EXECUTE/RETURN, run again
unchanged, contrasted with a non-matching request ("write one tweet for
this product") that never enters the pipeline.

B00 WRITER LAW: naive guess "Claude must **invent** the whole strategy,
right?" corrected to "assemble" (the newcomer's default assumption — Claude
exercises creative marketing judgment — is exactly what the reel exists to
correct). 35-word narration (WRITER LAW's ceiling) + `lead_silence_s: 0.8`.

**Three defects found and fixed before the cut passed gates — logged
honestly, not rounded up:**

1. **WRITER LAW timing near-miss (typo-catch didn't resolve in time).**
   First render of B00 with the initial writer props (`mistakeRate: 4,
   hesitateWithin: 2, hesitateBetween: 12, charMs: 48, jitter: 26`) measured
   10.41s of Kokoro audio (35-word narration already at the WRITER LAW
   ceiling, so narration could not be lengthened further). Frame-pulled the
   final frame and found the clip ended mid-typo on the trailing "right?"
   word — a random `mistakeRate` typo-catch on an unrelated character
   ("rightl|", the doomed "l" never got backspaced to "?") froze uncorrected
   at the clip's end. The main pedagogical correction ("invent"→"assemble")
   had already resolved cleanly by that point; only the incidental typo
   simulation ran out of window. Fixed by retuning the writer's own props to
   compress the performance since narration duration was already at the
   word ceiling and couldn't be extended: `mistakeRate` 4→0 (eliminates typo
   risk entirely — not needed for this beat's job), `hesitateWithin` 2→1,
   `hesitateBetween` 12→6, `charMs` 48→40, `jitter` 26→20. Re-rendered
   (10.43s), re-pulled the final frame: "You ask for a campaign plan.
   Claude must assemble the whole strategy, right?" fully typed and settled
   with the caret blinking cleanly, no doomed characters. Verified
   media/B00.mp4 = 10.43s (clears the ≥8s floor) AND the correction is
   visible on screen, not just the numeric floor.
2. **GATE T min-size FAIL, B02 (two rounds).** First `type_check.py` run
   failed B02 at 15pt Manim font sizes for the trigger-phrase list and
   six-piece slot labels (measured 8-10px, floor 20px) — fixed by bumping
   those to 20pt and B01's slot labels to 20pt with wider cards, which
   cleared B01 but B02 still failed at the same "8px" figure. Traced with
   the checker's own functions directly (not just re-running the full
   pipeline blind): extracted the exact mid-clip frame `type_check.py`
   samples (`extract_frame`, t=dur×0.5 of the raw `manim/B02.mp4`) and ran
   `check_min_size` against it in isolation. Found the actual blob: the
   literal straight double-quote glyph (`"`) opening the typed anchor query
   ("plan a launch campaign...") formed its own small isolated blob
   (~8-9px tall, disconnected from the following letter by monospace
   kerning) that happened to pass the checker's text-run width:height
   filter. Fixed by dropping the quote marks from the typed query entirely
   (the "THE ANCHOR" label already sets context; no semantic loss).
   Re-rendered, re-verified with the same isolated-function technique
   before re-running the full pipeline: PASS, min text-run height 137px.
3. **GATE T contrast FAIL, B02 (surfaced after the min-size fix).** With
   min-size cleared, a second, previously-hidden §8.3 failure surfaced on
   the same beat: "THE ANCHOR" label text, colored terracotta (`#E4572E`,
   the humanitarians CRIMSON), measured 2.74:1 contrast against the cream
   ground at the checker's sampled frame — below the 4.5:1 WCAG floor.
   Confirmed via the checker's own `check_contrast` function run in
   isolation against both this reel's `manim/B02.mp4` and the
   `account-research` sibling's `manim/B02.mp4` (identical design pattern,
   same terracotta hex): the sibling's single sampled frame happened not to
   contain "THE ANCHOR" prominently, so it passed by sampling luck rather
   than genuine compliance — a latent, unfixed defect in the shared design
   pattern that this build's frame timing happened to expose. Rather than
   attempt to retint the house terracotta or paper over the underlying
   color-contrast problem, fixed locally per the checker's own suggested
   remedy: switched "THE ANCHOR" label text from terracotta to ink, keeping
   the beat's one terracotta accent moment on the (already-passing,
   non-text) bracket/brace element instead of on readable prose. Re-ran the
   isolated function pair (min-size + contrast) on the freshly rendered
   clip before the full pipeline: both PASS (137px, 10.09:1). This is a
   latent defect worth flagging for the shared Manim "THE ANCHOR" pattern
   used across the `knowledge-work-plugins` family — not fixed upstream in
   this invocation, since scope is this one reel.

Built via the standard hai-simple pipeline, in the foreground throughout,
per COMPLETION LAW (no background render steps left unattended):

1. `generate_audio_kokoro.py` — 7/7 beats, free, measured durations written
   back (B00 10.41s; B01 17.88s; B02 21.10s; B03 18.99s; BCRY 9.00s; BHTF
   17.43s; BOUT 3.18s).
2. Custom Manim `scenes.py` (`CPB01Scene`/`CPB02Scene`/`CPB03Scene`) via
   `render_scenes.py`, foreground. GATE L checked first (`./art scenes
   "skill folder SKILL.md instructions trigger phrase fixed spec pipeline
   read execute return same six pieces"`) — the only hits
   (`SkillTeardownPipeline`/`BrandGuidelinesPipeline`/`BrandGuidelinesAnatomy`
   and siblings) are Teardown-branded, claude-palette Remotion components,
   same disposition as every prior sibling in this family — not a fit for
   Plain-register humanitarians-palette body beats. Bespoke Manim,
   humanitarians palette (`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). Two
   re-renders of B02 for the GATE T fixes above.
3. `remotion_scenes.py` — the harness auto-backgrounded both the initial
   4-beat call and the later B00-only forced re-render (each exceeded the
   tool's 120s timeout); blocked on both via `TaskOutput` (block=true)
   before proceeding, per the one-shot COMPLETION LAW's foreground-render
   rule, confirmed exit code 0 each time with all beats reporting `ok`.
4. `compile.py` (foreground, backgrounded/blocked-on by the harness on
   later re-runs for the same reason) — 7/7 slots filled, content-check/
   frame-check/lane-check all PASS, GATE AUDIO PASS mean_volume -24.2 dB.
   THE 4K LAW forced the master natively to 3840×2160. Compiled four times
   total across the fix cycle (B00 typing fix, B01/B02 min-size fix, B02
   contrast fix); final compile clean.
5. Independently reverified with ffprobe/ffmpeg rather than trusting
   compile.py's own report: master mtime (1788395590) newer than
   beat_sheet.json mtime (1788393929); h264 3840×2160 + aac streams
   present, duration 99.00s; `ffmpeg -af volumedetect` mean_volume
   **-24.2 dB**, max -2.4 dB.
6. GATE T (`type_check.py`): PASS, 0 FAILs, after the two B02 fixes above
   (traced and verified in isolation via the checker's own functions before
   each full-pipeline re-run, to avoid burning render cycles on guesses).
7. Gate V: pulled frames every ~10s across the full 99.0s runtime (10
   frames) plus two targeted pulls into media/B00.mp4 to verify the writer
   correction, and read all of them directly — B00's naive-question →
   correction (fully settled, no stray typo), B01's same-shape falsification
   (two products, identical six-piece output), B02's anchor plant
   (SKILL.md, trigger match, READ/EXECUTE/RETURN lighting), B03's anchor
   payoff (same query rerun, non-matching query staying dark), BCRY's
   carry-out quote card, BHTF's Your Turn composer (mid-type and settled),
   and BOUT's outro/subscribe card all read legibly with safe inset
   respected and no text overlap. BOUT/OutroCTA renders on flat white
   rather than the humanitarians cream ground, and BHTF/ClaudeComposerAsk
   shows the component's default "Fable 5 / High" model label since it
   wasn't overridden — both the same shared-component quirks already
   logged unfixed on every sibling in this factory, not new.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after 2 fixes on B02 — min-size from an isolated
  quote-mark glyph blob, then contrast from terracotta body text on cream)
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max -2.4 dB
- ffprobe: duration 99.00s; mp4 mtime newer than beat_sheet.json mtime
- WRITER LAW timing: media/B00.mp4 = 10.43s (≥8s floor) and the correction
  ("invent" → "assemble") is visible on screen, fully settled by the final
  frame, after 1 fix (writer props retuned to compress the performance
  since narration was already at the 35-word ceiling)

Metadata file written: `knowledge-work-plugins--claude-liam-campaign-plan.md`
(channel @HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's family `knowledge-work-plugins` matches the map's
`knowledge-work-plugins` prefix directly — plus the direct code link per
the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.

```
cp knowledge-work-plugins--claude-liam-campaign-plan.mp4 \
   knowledge-work-plugins--claude-liam-campaign-plan-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Result: outbox staged at
`DELIVERY/knowledge-work-plugins--claude-liam-campaign-plan/` (4K mp4 +
description); repo copy staged at
`humanitarians-youtube/claude-bear/knowledge-work-plugins--claude-liam-campaign-plan/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media); committed and pushed to
github.com/nikbearbrown/humanitarians-youtube (commit `f7e2a089`).

**Status: DELIVERED.**
