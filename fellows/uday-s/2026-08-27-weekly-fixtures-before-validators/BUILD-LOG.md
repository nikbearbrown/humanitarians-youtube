# BUILD-LOG — weekly-fixtures-before-validators

Skill: `cli-explainer` (build reel), applied as a **weekly work report**.
Subject: `D:/Projects/mycroft` @ `9ef4e7f`. Built 2026-08-27.

## Decisions that deviate from the chassis default — and why

**Channel = @HumanitariansAI, not the claude-liam default.** Chosen by the
author. Two consequences, both deliberate:

1. **Register and voice.** The chassis default for cli-explainer is Teardown /
   Kokoro `am_onyx`. The @HumanitariansAI channel maps to the Pragmatist
   register and `af_bella`, so the reel uses those. The Teardown habit of
   judging the design is dropped in favour of the Pragmatist habit of saying
   when the method applies and when it does not — which is also why B08 exists.
2. **OUTRO-LOCK overridden.** `OUTRO-LOCK.md` hardcodes the `@NikBearBrown`
   handle and a slug-seeded mascot for claude-liam reels. This reel is not a
   claude-liam reel, so `ClaudeTitleOutro` carries `@HumanitariansAI` and a
   `Mycroft · weekly` subline instead. Logged here rather than silently passed,
   per the PROOF GATE.

**IN-FOR-BEAR LAW not applied.** It binds claude-liam reels. B00 does not say
"this is Liam, in for Bear" — the narration reports the author's own week.

## GATE L — library-first

Searched before authoring, per the gate:

- `./art scenes "a checklist of file paths being verified one by one, each row resolving to pass or fail"`
- `./art scenes "a catalogue table of numbered defects grouped into classes"`
- `./art scenes "a list of steps where most are unfinished TODO and one becomes done"`

Top candidates were all reel-specific components from other films
(`HaiBrutalistE03Install`, `BrandRepricingTable`, `CwcEvalScoring` …) — leads,
not hits, and none carries the props these beats need. Confirmed the three
bookend components ARE renderable and used them unchanged:

```
ClaudeComposerAsk   RENDERABLE  16:9  props: command, topic, segment, greeting, runningText, output
ClaudeCodeBeat      RENDERABLE  16:9  props: title, code, sparkLine
ClaudeTitleOutro    RENDERABLE  16:9  props: title, handle, subline
```

**A miss is never a licence to slate.** B01, B04, B07, B08 and B09 are
parametric data animations, so they were authored as Manim scenes in
`scenes.py` (output-beat option 1), not slated and not punted. The misses are
logged to the toolkit's `TEMPLATE-MISSES.md` by the search itself.

## Environment notes (Windows)

- **No LaTeX in any scene.** `dvisvgm` is not installed on this machine, so
  `MathTex`/`Tex` would fail at render time. All type is `Text`/Pango. Nothing
  in this reel needs an equation, so this cost nothing.
- **Fonts registered at runtime.** The toolkit's `./setup --install` copies
  EB Garamond into `~/.local/share/fonts`, a path Windows ignores, so Pango
  could not see the brand faces. `scenes.py` calls `manimpango.register_font()`
  over `runtime/fonts/**.ttf` at import instead of requiring a system font
  install. `ART_FONT_DIR` overrides the toolkit path if the reel moves machines.
- Three Windows portability bugs in the toolkit itself were fixed to get this
  far (MSYS path translation in `run.sh`, ffmpeg filtergraph escaping in
  `compile.py`, and cp1252 stdout in the entry points). They live in the
  toolkit repo, not here.

## Audio-first

Narration generated and measured before a single frame was drawn. Manim scene
durations were written to match the MEASURED durations, not the estimates.

```
B00  7.85   B01 15.45   B02 13.61   B03 22.68
B04 21.06   B05 10.39   B06 18.92   B07 22.72
B08 18.50   B09 16.04   B10 12.59   B11  2.92
                                    total 182.73s (3:03)
```

Timing is never fixed by hand: change the narration, regenerate audio, recompile.

## Gate history

**GATE F — paperwork set.** Failed on the first render attempt: the reel had
`CHECKS-REPORT.md` and `SOURCES.md` but not `FACTCHECK.md`, `SHOTLIST.md` and
`PROMPTS.md`. Written, then passed. The gate is right to be strict here — the
fact-check is what separates a work report from a press release about yourself.

**GATE A — static pre-flight.** Failed twice, both times legitimately.

- `B01_TodoSteps`: *"shapes never change — 1 distinct shape-state across 5
  frames."* The beat was pure typography animated only by opacity, and the
  checker excludes `Text` from shape distinctness on purpose. Fixed by giving
  the beat the geometry its content implies: six **hollow status boxes** that
  are drawn one at a time and never fill, plus a six-cell ledger bar with
  nothing in it. The emptiness is now visual rather than merely stated.
- `B07_ProvenanceRun`: same failure, same cause. Fixed by resolving each of the
  14 rows into a bordered **verdict chip** (drawn, not faded) and replacing the
  text tally with a **proportional bar** — 8 / 3 / 1 / 2 segments sized to the
  counts.

Neither fix games the checker: in both cases the gate correctly identified a
beat that was telling rather than showing, which is exactly the SHOW-DON'T-TELL
law it exists to enforce.

Final static-check state, all five scenes:

```
B01_TodoSteps          [OK]   8 distinct shape-states
B04_DefectCatalogue    [OK]   2
B07_ProvenanceRun      [OK]  16
B08_WrongEntity        [OK]   2
B09_WeekLedger         [OK]   3
```

**GATE B — post-render, pixel-true.** Failed once on `B01_TodoSteps`: the body
block collided with the kicker's subtitle (44% text-on-text overlap) and the
kicker itself sat 0.05 units outside the ±3.4 safe box. Fixed globally rather
than locally — the kicker moved to `buff=0.72`, and every scene now routes its
body through a `fit()` helper that scales content into a declared
`BODY_TOP..BODY_BOTTOM` band instead of trusting hand-placed coordinates. `B07`
was restructured from 14 single-column rows (which would have overflowed) to
two columns of seven. All five scenes then audited **CLEAN**.

**GATE V — frame-level visual QC.** Two findings, one real and one an artefact.

*The artefact:* GATE V prefers `*-slate.mp4`, the REVIEW cut, which carries the
timecode burn-in at `x=w-text_w-16:y=16` — outside title-safe by construction.
That trips `edge-bleed` on every sampled frame, so the headline "24 BLOCKER"
is measuring the review overlay, not the reel. Against the CLEAN cut:

```
weekly-fixtures-before-validators.mp4    365 frames    BLOCKER 0
```

*The real one:* `underfill` — frames below the 55% canvas-fill floor. First
pass: 62 frames. Every one sat at the START of a Manim beat, during the
staggered build-in. B07 was the worst offender, spending 8.7 of its 22.7
seconds revealing one row at a time — that is a genuine pacing defect, not a
false positive, so it was fixed: B04 and B07 now land their STRUCTURE (class
labels / the 14 paths) in ~1.5s and resolve the DATA into it afterwards.

```
              underfill frames    low-contrast
first pass          62                 2
after the fix       38                 1        (BLOCKER 0 throughout)
```

**Residual, accepted and not silenced.** 38 frames (~19s of 183s, ~10%) remain
under the fill floor. All of them are build-in ramps in B01/B04/B07/B08/B09 and
the house `ClaudeTitleOutro` (B11), which is a deliberately sparse title card.
Driving this to zero would mean abandoning staggered reveals altogether — but
`stagger-in`, `build` and `resolve` are named motion languages in this
toolkit's own MOTION.md and are declared per beat in the sheet. The 55% floor
and a build-in animation are in tension by construction. Recorded here as an
accepted deviation with reasoning, per the PROOF GATE, rather than passed
silently or hidden behind `ART_STRICT=0`.

## Open

- **Master resolution.** The compiled cut is 1080p because `--height 1080` was
  used for QC speed. The underlying assets are 4K (Manim at 2160p24, Remotion
  at `--scale=2`), so `./art final <reel>` will produce a true 4K master from
  the same slots without re-rendering any beat.
- Nothing here ever publishes; the master stays in this folder.

---

# REVISION 2 — 2026-08-27, author request

Four changes: a spoken name in the intro, PROOF-rubric compliance, a male
voice, and the reel folder moved out of the subject repo.

## 1. Name in the intro

B00 now opens *"I'm Uday Sonawane, and this is my week on Mycroft."* No
"state your name" rule exists in either repo — I searched both — so the wording
was confirmed with the author rather than inferred. The name also rides the
composer `segment` and the outro subline, so it is on screen as well as spoken.

## 2. PROOF compliance — what actually had to change

Scored against `brutalist.art/PROOF.md`. Five of the six rubric criteria were
already met by the previous cut. **One was not, and it was the load-bearing
one:**

> *Explicit framework — the organizing idea is shown as a structure BEFORE the
> examples, not narrated after.* PROOF's Phase-2 gate: "confirm the framework
> graphic lands in the first ~20s, ahead of any example."

The previous cut had no framework graphic at all. B01 stated a *principle*
("if nothing is broken, passing is not evidence") in voiceover — which is a
slogan, not a framework. PROOF's own pushback layer names this exact failure:
"That's not a framework yet — it's a slogan. A framework is a set of axes a
viewer could score a new case on."

So a new beat was written: **B02 — THE METHOD**, four numbered cards.

```
1  ENUMERATE          what kinds of wrong can this data be?
2  PLANT              one instance of each, with an exact locator
3  NAME THE CATCHER   which check must surface it
4  FREEZE             pin timestamps, so two runs stay comparable
```

These are axes a viewer can apply to a suite that has nothing to do with market
sentiment, which is the test PROOF sets. The later beats were then re-narrated
to reference the method by step number, so the framework is *used*, not just
displayed: B03 is steps 1+2, B04 is step 3, B05 is steps 1+4, B07 is step 4,
and B09 is the case that **breaks** step 1.

**Timing check.** PROOF wants the framework inside the first ~20s. Measured:
B00 (7.98s) + B01 (11.07s) = **19.05s**, so B02 opens at 19.05s, before the
first example at 31.20s. Verified against the audio, not estimated.

Also strengthened for PROOF's `/cta` rule — "never accept a vague pointer" and
"what does a good vs. bad answer look like": B11 now states both on screen and
in narration (GOOD: a fixture + line for every check · BAD: "all tests pass").

## 3. Male voice

`voice_kokoro` af_bella → **am_onyx**. Register stays Pragmatist; am_onyx is
normally the Teardown/nbb voice, so this is a deliberate pairing, not the
chassis default. Changing voice re-times the entire reel — every narration
duration changed, so all six Manim scenes were re-written to the new measured
clock and every beat re-rendered. Nothing was hand-timed.

## 4. Folder moved out of mycroft

`mycroft/youtube/<slug>/` → `D:/Projects/youtube/<slug>/`.

This **deliberately breaks** the toolkit's "videos travel with their book" rule
(CLAUDE.md rule 3), at the author's explicit request. Consequence to know: the
reel no longer sits inside the repo it documents, so the subject commit is no
longer implied by location. `beat_sheet.json` therefore carries `source_repo`
and `source_commit` explicitly, and `SOURCES.md` records the derivations — that
metadata is now the only link between the reel and what it describes. Keep it
accurate or the provenance chain is broken.

## Beat map change

```
old (12)                     new (13)
B00 INTRO                    B00 INTRO         + name spoken
B01 PROBLEM                  B01 PROBLEM       tightened, so the framework fits <20s
   —                         B02 FRAMEWORK     NEW — the reusable method
B02 CLI                      B03 CLI
B03 CODE                     B04 CODE
B04 OUTPUT                   B05 OUTPUT
B05 CLI                      B06 CLI
B06 CODE                     B07 CODE
B07 OUTPUT                   B08 OUTPUT
B08 FALSIFIABILITY           B09 FALSIFIABILITY
B09 SUMMARY                  B10 SUMMARY
B10 NEXT STEPS               B11 NEXT STEPS    + GOOD/BAD answer test
B11 OUTRO                    B12 OUTRO         + name in subline
```

Total 182.23s (3:02), 13 beats. GATE A and GATE W clean on all six scenes
before render.
