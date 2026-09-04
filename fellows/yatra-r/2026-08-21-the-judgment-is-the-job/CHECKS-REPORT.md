# CHECKS-REPORT — The Judgment Is the Job.

Written before the first compile, per the PROOF GATE in
`skills/make/ai-explainer/SKILL.md`. Classification rules: `skills/make/nopunt/SKILL.md`.

```
10 SHOW / 0 justified-HOLD / 0 PUNT-flagged
Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

| Beat | Lane | Composition | Class | Why it is not a PUNT |
|---|---|---|---|---|
| B00 | BOOKEND | `ClaudeComposerAsk` | SHOW | Types the ask, arms the send, lands three result lines. COLD OPEN LAW satisfied. |
| B01 | BODY | `JdgDiverge` | SHOW | The BLUF *is* a split; one node visibly splits and the two tracks diverge on the spoken word. |
| B02 | BODY | `JdgSplit` | SHOW | Two columns fill item by item as each is named; the divide draws first. |
| B03 | ASK-MICRO | `ClaudeComposerAsk` | SHOW | ASK→RESULT receipt — the actual prompt behind B04. 21 words: micro-beat, exempt from the 45–70 body budget by design. |
| B04 | BODY | `JdgOptions` | SHOW | The wall populates faster than the voice can list it, then ONE card takes a terracotta ring on the spoken word. |
| B05 | BODY | `JdgBranch` | SHOW | Two branches draw with B02's columns ghosted behind them — the example USES the framework on screen. |
| B06 | BODY | `JdgStakes` | SHOW | Four rows land on their spoken phrases, each with a marker and a one-line why. |
| B07 | BOOKEND | `ClaudeVerdictArtifact` | SHOW | Four lines stagger, one per spoken clause. |
| B08 | BOOKEND | `ClaudeComposerAsk` | SHOW | Prompt types as it is read aloud verbatim; the rubric stacks in as each check is spoken. |
| B09 | BOOKEND | `ClaudeTitleOutro` | SHOW | Title restate + handle, no subline. |

No bare CARDs. No PUNTs. No HOLDs — this reel needs no archival photograph, so nothing
legitimately waits on a human.

## Teaching-arc checklist (nopunt § Whole-sheet)

- **FRAMEWORK beat** ✓ — B02 presents the execution/judgment ledger *before* the first
  example at B04/B05.
- **WORKED EXAMPLE** ✓ — B05 walks two job descriptions through that ledger with the B02
  columns ghosted on screen, so the example visibly uses the framework rather than sitting
  beside it.
- **FALSIFIABILITY** ✓ — B06 is a full beat, not a passing caveat: four categories the
  model says the machine cannot own, plus a self-test the viewer can fail ("none of these
  in your work → exposed").
- **SCAFFOLDED viewer task** ✓ — B08 carries a real prompt *and* a three-item rubric, plus
  the failure signal ("if it says everything was judgment, you flattered yourself").
- **Four bookends** ✓ — B00 cold open · B07 verdict · B08 YOUR TURN · B09 title restate.
- **No source, no verdict** ✓ — every claim beat carries its artifact on screen, and the
  reel asserts no measured figure at all. The limitation is spoken aloud and rendered on
  the verdict card. See `FACTCHECK.md`.

## Coverage of the human's four requested areas

| Requested | Where it lands |
|---|---|
| AI writing ad copy, taglines, social content | B00 result lines · B02 left column (headlines, taglines, a month of social variants, translations) |
| AI generating visual ad creative | B03 → B04, the one ASK→RESULT pair: the brief, then the wall of concepts |
| What this means for copywriters and designers | B05, as two job descriptions rather than one prediction |
| Where human creativity / oversight still matters | B06, the four things the machine cannot own — given the falsifiability slot, i.e. the reel's most load-bearing beat |

## Constraint compliance (no invented statistics)

Enforced three ways, so it cannot rot: **structurally** (none of the three new scenes has
a prop that renders a numeric datum), **automatically** (a numeral audit over every
on-screen string ran before the first render — one hit, reviewed and justified in
`FACTCHECK.md`), and **editorially** (the verdict card says so out loud).

## Legibility contract

- Every beat names its on-screen artifact in `shot.show`. ✓
- Long strings on `JdgBranch` were kept deliberately short: the previous reel's QC found
  `BinaryBranch` overflows its fixed-width boxes with sentence-length copy.
- `SafeStage` maps the two reused deckPatterns scenes onto the title-safe box — the fix
  the previous reel's QC produced, now shared. **Verified on B01's first render: ink
  x[301, 3644] against a safe right edge of 3648, coverage 0.93, Gate V clean.**
- Comparisons held ≥2s — specified in the `show` blocks of B02, B04, B05, B06.

## Known-good vs known-bad components carried forward

The previous reel established by frame-level QC that `ScaleComparison`, `AttritionChain`
and `Threshold` either crash or print measured-looking numbers. All three are **excluded
by design** here — fatal under this reel's no-numbers rule. The two qualitative patterns
(`DivergentFates`, `BinaryBranch`) are reused; everything else is purpose-built.

## Carried into visual QC

1. `JdgOptions` packs 12 cards in a 4×3 grid; card label type is 28px against a ~24px
   floor. Needs a look — if any label wraps or clips, the fix is fewer cards, not smaller
   type.
2. `JdgStakes` sets a 44px label plus a 28px why-line per row across four rows. Check the
   rows don't crowd at the measured duration.
3. Mono labels persist in the two reused deckPatterns scenes (B01, B05) — a known,
   accepted deviation from the claude type stack, unchanged from last reel.
4. GATE T cannot run (`type_check.py` is not shipped in this toolkit), so type sizes are
   checked by eye against the floor.
