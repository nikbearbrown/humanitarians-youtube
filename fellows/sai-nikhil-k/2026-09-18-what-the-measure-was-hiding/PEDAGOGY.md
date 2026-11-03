# PEDAGOGY — What the Measure Was Hiding

**Reel** `weekly_updates/09-18-2/` · **slug** `claude-sai-what-the-measure-was-hiding`
**Subject** Prot2Vec, v0.2.0 + v0.3.0 · **week of** 2026-09-18
**Host** Sai, in his own name (attribution override — see below)
**Voice** Kokoro `am_onyx`, free and local · **Chassis** all-Remotion, no Manim, no paid anything

---

## The ONE idea

> Prot2Vec exists to catch results that are secretly measuring something else.
> This week it shipped three new ways to do that — and then caught its own.

The release has an obvious headline (nine representations, thirteen projections,
thirty-one metrics) and a real subject underneath it. Most of what was added is
*defensive*: a control that fits nothing, a chance-corrected overlap, and a group
of metrics whose only job is to ask "is this just encoding sequence length?"

In the same release the project discovered that its own coverage report had been
excluding whole function bodies — including the body of `evaluate()`, the
function that computes every metric. The aggregate percentage still looked
respectable. That is precisely the failure mode the tool was built to find,
occurring inside the tool.

The reel refuses to flatten this into "we added more methods."

## Act structure

| Beat | Act | Pattern | Why this pattern |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open; the week's ask typed on screen, three headline counts as result lines. |
| B01 | THE OBJECT | `ClaudeScienceChipGrid` | Nine named representations are a *set*. A grid is the honest shape for a set. |
| B02 | THE FLOOR | `TypesetMath` | The chance floor is an equation. It is set as one, with real fraction bars and a bound summation — not described in prose. |
| B03 | TWO KINDS | `DivergentFates` | One observation, two causes that look identical. A fork that *diverges* is the shape of that argument. |
| B04 | THE INSTRUMENT | `ExecutedData` | Measured rows from a computation actually run, not an illustration of one. |
| B05 | THE FORK | `BinaryBranch` | A genuine design decision with two answers and a resolver. |
| B06 | VERDICT | `ClaudeVerdictArtifact` | One-page recap, four bare sentences. |
| B07 | HANDOFF | `ClaudeComposerAsk` | A prompt the viewer can paste, read aloud and discussed. |
| B08 | OUTRO | `LogoOutro` | `@HumanitariansAI` card. **Not** `ClaudeTitleOutro`, whose handle is hardcoded. |

## ILLUSTRATE LAW check

Claude UI appears at **B00**, **B07** and the verdict/outro only. Body beats run

`ChipGrid → TypesetMath → DivergentFates → ExecutedData → BinaryBranch`

— five body beats, five distinct patterns, no two consecutive the same. ✓

Every body beat carries an ordered `show` block. None of them would survive as a
static slide with a voiceover: B02 reveals its algebra in three stages, B03
splits, B04 fills a table row by row, B05 resolves a fork. ✓

## 9:16 constraint

Every pattern used here has a registered portrait sibling in `Root.tsx` —
`ClaudeComposerAsk916`, `ClaudeScienceChipGrid916`, `TypesetMath916`,
`DivergentFates916`, `ExecutedData916`, `BinaryBranch916`,
`ClaudeVerdictArtifact916`, `LogoOutro916` — so the vertical cut rewires with no
new TSX. `ClaudeScienceLayerStack` and `ClaudeScienceSourceFlow`, the guide's
default B01/B02 patterns, still have **no** portrait sibling and are avoided for
that reason alone.

`TypesetMath` stacks its rows independently in portrait; the equations are the
one thing to inspect closely in the vertical QC pass.

Narration carries no positional reference ("the top row", "the third one"),
because the same mp3 plays over both aspects.

## Evidence and honesty

Two computations were **run**, not illustrated, and both are preserved:

- `evidence/coverage_exclusion.py` → `coverage_exclusion.out`. Drives
  coverage 7.8.2's parser over the real v0.3.0 tree under both exclude patterns.
  Produces every number in B04.
- `evidence/lcmc_chance.py` → `lcmc_chance.out`. Runs Prot2Vec's own shipped
  `neighborhood_preservation` and `local_continuity_meta_criterion` on seeded
  random data to confirm the chance term B02 typesets.

No screenshot was requested, no terminal was photographed, and no figure was
generated. Everything else — counts of embedders, reducers, metrics, tests — was
counted out of the source by hand. See `FACTCHECK.md` for each one.

**Nothing about performance appears anywhere.** No runtime, no memory, no
speedup, no accuracy on a real dataset, no adoption figure. None was supplied.
The changelog's "84% coverage" is deliberately omitted because it could not be
reproduced without the optional deep-learning extras.

## Attribution override

Established 2026-07-31 and carried through 09-04-01, 09-04-02, 09-11-1 and
09-11-2: this series is **hosted by Sai in his own name**, not by
Liam-in-for-Bear. B00 says "This is Sai"; B08 signs off "Sai." The IN-FOR-BEAR
LAW of `WEEKLY-VIDEO-GUIDE.md` is deliberately suspended here. The voice remains
Kokoro `am_onyx`.

Prot2Vec is Sai's own project, so no third party is named on screen or in
narration.

## Expected build noise (not bugs)

- `./art run` will print a SKIN LINT line asking for `ClaudeTitleOutro` at B08.
  It is wrong for this channel — `ClaudeTitleOutro`'s handle is hardcoded to
  `@NikBearBrown` and cannot carry `@HumanitariansAI`.
- `./art scenes --check` may report the `*916` siblings as NOT RENDERABLE. The
  `scenes.json` index lags `Root.tsx`; all eight were confirmed present as real
  `<Composition id=…>` registrations.
- B08's narration is held to six words so it finishes inside the 4.0s logo card
  before its fade, which `remotion_scenes.py` would otherwise freeze-extend.

---

## Human review checklist

Work down this list before signing. Nothing below has been done by the
assistant.

- [ ] Read the full narration (below). Does it say what the week was?
- [ ] B00: is "This is Sai" in the right place and the greeting correct?
- [ ] B02: is the algebra right, and is `k/(n−1) = 10/89` the floor you want shown?
- [ ] B04: is the coverage story characterised fairly — report, not execution?
- [ ] B03: are the two tracks fair, given no real confound has been caught yet?
- [ ] Is any figure on screen one you would defend in public? (`FACTCHECK.md`)
- [ ] B07: is the handoff prompt one you would actually paste?
- [ ] Is anything here better left out of a public video?

After STEP 3, the math frames must be inspected in both aspects at each reveal
and at 15/50/85% of B02, with the result recorded in `FACTCHECK.md` and `_qc/`.

---

## Full narration, as it will be spoken

### B00 · ASK — `ClaudeComposerAsk` · ~19.7s (64 words)

> Prot2Vec is a benchmark harness for protein sequence embeddings. This week it
> went from two representations to nine, from two projections to thirteen, and
> from ten metrics to thirty-one. This is Sai. The interesting part is not the
> breadth. It is that the release added three new ways to catch a result that is
> secretly measuring something else — and then caught its own.

### B01 · THE OBJECT — `ClaudeScienceChipGrid` · ~20.0s (65 words)

> So, what is it. You hand it sequences with group labels. It runs every
> embedding method against every dimensionality reducer and scores all of them
> with the same metrics, so the comparison is actually like for like. Nine ways
> to turn a sequence into a vector, from counting amino acids to calling a
> protein language model. Six of the nine need no PyTorch at all.

### B02 · THE FLOOR — `TypesetMath` · ~19.1s (62 words)

> Here is the metric that sets the tone for the whole release. Neighbourhood
> preservation asks what fraction of each point's true nearest neighbours
> survive the projection. But that number has a floor. Even a projection
> carrying no information keeps some neighbours by luck — k over n minus one of
> them. So the release ships the chance-corrected version, and subtracts the
> floor.

### B03 · TWO KINDS — `DivergentFates` · ~18.5s (60 words)

> And this is the failure the harness exists to catch. Two protein families
> separate cleanly on screen. That can mean the representation found real
> homology. Or it can mean the representation encoded sequence length, and
> length happens to differ between those families. In a scatter plot those two
> look identical. The confound group added this week refuses to let them.

### B04 · THE INSTRUMENT — `ExecutedData` · ~21.2s (69 words)

> Then the same release caught its own instrument. Coverage had been told to
> ignore any line that is just an ellipsis — the abstract-method placeholder.
> The pattern was never anchored. So it also matched a type annotation, tuple of
> string, ellipsis, and coverage discards the entire statement a matching line
> belongs to. Sixty-one statements quietly left the report. Forty-seven of them
> sat in the module that scores everything else.

### B05 · THE FORK — `BinaryBranch` · ~17.2s (56 words)

> Breadth also changes what a single bug costs. NMF refuses signed input. A
> manifold method can fail on a disconnected neighbour graph. At four pairs
> those are exceptions; across a full matrix they are ordinary. Previously any
> one of them discarded every pair that had already succeeded. That was the fork
> this week actually turned on.

### B06 · VERDICT — `ClaudeVerdictArtifact` · ~15.1s (49 words)

> So: two releases, one week. The breadth is the headline. The defences are the
> release. And the coverage bug is the part worth keeping, because it is the
> same mistake the whole tool exists to find — a number that looked fine while
> quietly measuring less than it claimed.

### B07 · HANDOFF — `ClaudeComposerAsk` · ~22.5s (73 words)

> Your turn, and you can run this against anything you are about to publish.
> Here is a benchmark result. Before you tell me whether the score is good, tell
> me what a random control would have scored on the same data, what the result
> becomes if the representation encodes only length, and whether the tooling I
> used to check my own work is itself being checked. Then tell me which one I
> forgot.

### B08 · OUTRO — `LogoOutro` · ~1.8s (6 words)

> What the measure was hiding. Sai.

**Total: 504 words** → ~155s at 195 wpm (the conservative slow end), about 2:35.
Under the 180s Shorts cap, so a 9:16 cut needs no beats dropped. Audio remains
the master clock; these are predictions, not durations.

---

VERDICT: PASS    — reviewer: Sai Nikhil Kunapareddy  date: 09-18-2026
