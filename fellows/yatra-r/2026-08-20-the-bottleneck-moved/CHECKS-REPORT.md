# CHECKS-REPORT — The Bottleneck Moved.

Written BEFORE the first slate compiles, per the PROOF GATE in
`skills/make/ai-explainer/SKILL.md`. Classification rules: `skills/make/nopunt/SKILL.md`.

```
10 SHOW / 0 justified-HOLD / 0 PUNT-flagged
Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

| Beat | Lane | Pattern | Class | Why it is not a PUNT |
|---|---|---|---|---|
| B00 | BOOKEND | ClaudeComposerAsk | SHOW | Types the ask, arms the send, lands three result lines. COLD OPEN LAW satisfied — the ask lands answered. |
| B01 | BODY | DivergentFates | SHOW | The BLUF *is* a split; the node visibly splits and the two tracks diverge on the spoken word "apart". |
| B02 | BODY | ScaleComparison | SHOW | Three ordinal bars grow to their ranks as each is named; the band brackets only the cheap one. |
| B03 | ASK-MICRO | ClaudeComposerAsk | SHOW | ASK→RESULT LAW receipt — the actual generation prompt behind B04, typed live. 22 words: micro-beat, exempt from the 45–70 body budget by design. |
| B04 | BODY | AttritionChain | SHOW | Stages light in narration order, each narrower; the top doubles and the tail visibly does not move. |
| B05 | BODY | Threshold | SHOW | The cutoff line snaps in on the spoken word; verdict flips YES→NO across it. |
| B06 | BODY | BinaryBranch | SHOW | Both branches draw with the B02 bars ghosted behind them — the example USES the framework on screen, not adjacent to it. |
| B07 | BOOKEND | ClaudeVerdictArtifact | SHOW | Four lines stagger, one per spoken clause; caveat lands last under a terracotta rule. |
| B08 | BOOKEND | ClaudeComposerAsk | SHOW | Prompt types as it is read aloud verbatim; the three-item rubric stacks in as each check is spoken. |
| B09 | BOOKEND | ClaudeTitleOutro | SHOW | Title restate + handle + slug-seeded mascot (translation/axis-scale only). |

No beat is a bare CARD. No beat is a PUNT. No HOLDs — this reel needs no archival
photograph, so nothing legitimately waits on a human.

## Teaching-arc checklist (nopunt § Whole-sheet)

- **FRAMEWORK beat** ✓ — B02 presents the three-cost framework (produce / distribute /
  be believed) *before* the first example at B06.
- **WORKED EXAMPLE** ✓ — B06 walks 20 freed hours through that framework with the B02
  bars ghosted on screen, so the example visibly uses the framework.
- **FALSIFIABILITY** ✓ — B05 is a full beat, not a caveat in passing: it names the
  volume cutoff and states the observation that would falsify the model ("if your reach
  keeps scaling past that point, this model doesn't fit you").
- **SCAFFOLDED viewer task** ✓ — B08 carries a real prompt *and* a three-item rubric
  (sorts every asset / disagrees somewhere / names unaccounted hours), plus the failure
  signal ("if it agrees with everything, you gave it too little"). Not "ask Claude about X".
- **Four bookends** ✓ — B00 cold open · B07 verdict · B08 YOUR TURN · B09 title restate.
- **No source, no verdict** ✓ — with a caveat that is itself on screen. This reel asserts
  no measured external figure. Every magnitude is an ordinal ranking, labelled as such in
  the `slideMeta`/`axisLabel` of B02, B04 and B05, and the limitation is stated aloud and
  on the verdict page at B07. See `FACTCHECK.md`.

## Legibility contract (per claim beat)

- Every SHOW beat names its on-screen artifact in `shot.show`. ✓
- ~15–35% negative space — the four rhetorical patterns are built to it; **verify at
  visual QC**, since they are registered at 1280×720 and scale onto the 1920×1080 stage.
- No un-highlighted element below ~40% opacity — pattern defaults; **verify at QC**.
- Comparisons held ≥2s — specified in the `show` blocks of B02, B04, B05, B06.

## Open items — status at build time

1. **FILL-THE-CANVAS.** ✅ **Resolved.** The five patterns were registered generically at
   1280×720. They are now wrapped as reel-local 1920×1080 compositions — `BnkSplit`,
   `BnkCosts`, `BnkFunnel`, `BnkCutoff`, `BnkBranch` in
   `runtime/remotion/src/scenes/BottleneckMoved.tsx` — so they lay out at full canvas
   natively rather than being scaled up. Each composition's `durationInFrames` is its
   beat's *measured* Kokoro length × 30fps, so no animation gets trimmed mid-motion.
   Gate V's ink-coverage floor (55% of SAFE) still has to confirm this by eye.
2. **Palette retint.** ✅ **Not needed — no action taken.** On inspection
   `deckPatterns.tsx` already uses the claude stage values (`BG #F2F0E9`, `INK #3D3929`,
   `ACCENT #D97757`, `WARN #A44A32`). The retint this report originally anticipated would
   have been a no-op at best. Recorded so a later author doesn't "fix" a correct palette.
3. **LOGO LAW.** ✅ **Resolved.** No logo file ships for `@NikBearBrown` in this tree, so
   the law's stated fallback applies: the handle renders as a low-opacity (0.3) EB Garamond
   wordmark in the lower-right, positioned from the shared `SAFE` constant — never
   pixel-nudged.
4. **Type family — open, deliberately deferred to QC.** `deckPatterns` sets its labels in
   JetBrains Mono, but the claude brand reserves mono for terminal/output lines and wants
   serif/UI-sans elsewhere. Changing it means either editing a shared file used by other
   reels or forking the patterns reel-locally. Neither is justified on a guess — VISUAL QC
   LAW says look at the frames first. Carried into `_qc/REPORT.md` as a named check.

## Post-build verdict (after frame-level QC)

The authoring gate above passed before the first compile. What visual QC then found is
recorded in full in `_qc/QC-LOG.md` — 10 defects fixed (3 of them by replacing shipped
components that printed invented-looking numbers), 3 accepted with reasons, and Gate V's
20 `edge-bleed` BLOCKERs identified as a false positive in the toolkit's own gate wiring
(it inspects the `--review` cut and flags that cut's own burn-in).

Headline: **the five body beats this reel authored all clear Gate V's canvas-fill floor**
(B02 measures 0.98 coverage of SAFE against a 0.55 minimum). The two `underfill` MAJORs
are on shipped fidelity bookends (verdict artifact, title outro), where FILL-THE-CANVAS
LAW and the do-not-retint fidelity rule genuinely conflict.

## Corrections made during the build

- **B05 prop shape was wrong.** `Threshold`'s `modes[]` requires
  `{label, sub, limit, resolves}`; the sheet had `{label, size, unit}`. Caught by validating
  every prop payload against the TypeScript contracts in `deckPatterns.tsx` before the
  first render, not by a failed render. Fixed.
- All 10 prop payloads now validate against their component types; `npx tsc --noEmit`
  is clean.
