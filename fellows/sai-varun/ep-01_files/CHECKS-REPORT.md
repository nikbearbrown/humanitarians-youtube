# CHECKS-REPORT — hai-uncertain-eye-e01-silent-thief

Written BEFORE the first slate compiles, per PROOF GATE.

## Per-beat classification

11 SHOW / 0 justified-HOLD / 0 PUNT-flagged

| Beat | Class | Artifact named in `shot` |
|---|---|---|
| B00 | SHOW | ClaudeComposerAsk (library) |
| B01 | SHOW | BrutalistHesitantWriter (library) |
| B02 | SHOW | HaiGlaucomaStakes (library — reused from sibling reel) |
| B03 | SHOW | UeNerveBundle (design card → build) |
| B04 | SHOW | UeSilentWindow (design card → build) |
| B05 | SHOW | UeLooksNormal (design card → build) |
| B06 | SHOW | ClaudeComposerAsk (library) |
| B07 | SHOW | UePatternProblem (design card → build) |
| B08 | SHOW | ClaudeVerdictArtifact (library) |
| B09 | SHOW | ClaudeComposerAsk (library) |
| B10 | SHOW | ClaudeTitleOutro (library) |

No beat is a bare CARD. No beat is a PUNT. The four new components are design
cards with full specs in `DESIGN-CARDS.md` — they are authored before the
slate, not slated.

## Teaching arc

    Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
                  SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓

- **FRAMEWORK ✓** — B04 `UeSilentWindow` presents the silent-window model
  (damage accumulating vs. what perception reports, gated at ~40%) as its own
  beat, BEFORE the worked example at B05.
- **WORKED EXAMPLE ✓** — B05 walks a concrete pair of eyes through that
  framework, and the framework returns on screen as an inset at 0.70 so the
  example visibly USES it rather than sitting adjacent to it.
- **FALSIFIABILITY ✓** — B05 is a full beat, not a caveat: it stress-tests the
  obvious approach ("look harder") and shows it failing. The failure mode is
  the beat's whole content.
- **SCAFFOLDED TASK ✓** — B09 carries a real prompt, read aloud verbatim, plus
  a three-part rubric (signal · cost · harm) and an explicit failure test
  ("if it skips the harm, push back").
- **BOOKENDS ✓** — cold open B00, verdict B08, YOUR TURN B09, title-restate
  outro B10.
- **NO-SOURCE-NO-VERDICT ✓** — every claim-bearing beat carries on-screen
  evidence: B02 the two bars + caption, B03 the fiber count label, B04 the
  gated axis, B05 the held two-up, B07 the two lanes. No figure lives in the
  voice alone.

## Legibility contract (SHOW claim beats)

- Artifact named in `shot.remotion.pattern` + `show` block on every beat ✓
- ~15–35% negative space — enforced at build; verified in visual QC
- No un-highlighted element below ~40% opacity — the ghosted fibers in B03 are
  the deliberate exception and are the SUBJECT of the beat (loss made visible),
  not de-emphasised content
- Comparisons held ≥2s — B05 holds the unlabelled two-up for ≥2s by spec

## Law compliance

- **COLD OPEN LAW** ✓ B00 opens directly on `ClaudeComposerAsk`, with output lines.
- **EXECUTIVE-SUMMARY LAW** ✓ B01 is `BrutalistHesitantWriter`; window 11s ≥ 9s;
  `lead_silence_s: 0.8` written explicitly; narration 36 words; the correction is
  the reel's real misconception and the corrected sentence stands alone.
- **ILLUSTRATE LAW** ✓ UI at B00, B06, B08, B09, B10 only. B02–B05 and B07
  illustrate. No two consecutive beats share a visual scheme.
- **ASK→RESULT LAW** ✓ one pair: B06 (the actual generation prompt) → B07 (the result).
- **HANDOFF LAW** ✓ B09 is second-to-last; prompt read aloud verbatim AND discussed.
- **TYPING** ✓ exactly B00, B01, B09 + the B06 ask micro-beat.
- **SPARK-LINE LAW** ✓ every illustration beat carries a ≤4-word spark line.
- **OUTRO LAW** ✓ B10 restates the title with the terracotta period. The
  @NikBearBrown outro lock does not bind (this is @HumanitariansAI), so the
  subline is permitted.
- **LOGO LAW** ✓ HAI corner bug on every beat (inlined in the component `Stage`);
  full-size mark at B10.
- **DOODLE-BANNED LAW** ✓ no DoodleScene / DoodleChart.
- **Number policy** ✓ zero performance figures in this episode. See SOURCES.md.

## Duration

Estimated 156s = **2:36**, inside the 2:00–2:45 target. 483 narration words.
Rate basis: the sibling reel measured 187.4 wpm aggregate on Kokoro `am_onyx`,
with number-heavy beats running 139–170 wpm. At the slow bound this lands ~2:45;
at the fast bound ~2:35.

**Gate:** if measured audio exceeds 2:45, trim B09 (longest and most
compressible) before conforming — do not re-time by hand.
