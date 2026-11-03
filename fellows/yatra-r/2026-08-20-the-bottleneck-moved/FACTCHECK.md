# FACTCHECK — The Bottleneck Moved.

DOUBLE-CHECK LAW + REBUILD LAW record. Written before audio lock.

## The governing decision

This reel makes **an argument from a stated model**, not an empirical report. That is a
deliberate choice, and it is the reason the reel can be built honestly with no external
source: rather than cite market statistics I cannot verify, the reel reasons from a
premise the viewer can check against their own data, and says so out loud.

The consequence is a hard authoring rule, applied to every beat:

> **No measured external figure appears anywhere in this reel** — not in narration,
> not on a card, not on an axis. Every magnitude on screen is an *ordinal ranking*,
> labelled as ordinal in the frame it appears in.

This satisfies the REBUILD LAW clause "exact data when published; orderings/anchors only
when not; never an invented figure". An unlabelled bar chart of invented percentages
would have violated it. A labelled ordinal ranking does not.

## Claim ledger

| # | Beat | Claim as spoken | Verdict | Basis / fix applied |
|---|---|---|---|---|
| 1 | B00 | "Output is up roughly 5x and reach is flat" | ✓ as framing | Spoken by the *prompt's fictional author*, not the narrator — it is the premise of the ask, not an assertion about the market. Left as-is. |
| 2 | B01 | AI collapsed the cost of producing marketing content "effectively to zero" | ✓ | Directional and defensible: marginal cost per generated draft/variant/image is near zero once tooling is in place. No rate or figure claimed. |
| 3 | B01 | It did not collapse the cost of being worth someone's attention | ✓ | Definitional, not empirical — attention is rivalrous and its supply is unchanged by generation speed. Carries the argument. |
| 4 | B02 | Ranking: produce < distribute < be believed | ✓ as ordinal | Axis explicitly labelled "ORDINAL RANKING, not a measurement"; `slideMeta` repeats it. Values 8/64/92 encode rank and spacing only. |
| 5 | B02 | "everyone got the same machine" | ✓ | Narration only; the on-screen artifact is the ranking, which does not depend on it. Softened from an earlier "everyone has the same machine". |
| 6 | B04 | Funnel stages: published → seen → read → remembered → acted on | ✓ as ordinal | `slideMeta` reads "ORDINAL SHAPE ONLY · illustrative, not measured data". Survival values encode monotone decline, not measured rates. |
| 7 | B04 | "not one of those stages cares how fast the thing was written" | ✓ | The load-bearing claim. Defensible: no stage of the funnel is a function of authoring speed. Shown, not just said — the top doubles and the tail holds. |
| 8 | B05 | A volume cutoff exists, past which more output costs trust | ⚠ **contestable — and labelled as such** | This is the reel's most falsifiable claim. It is deliberately framed as a *test*, not a finding: the beat states the observation that would disprove it. No threshold value is asserted. |
| 9 | B05 | "a small brand posting twice a week gains by posting five times" | ⚠ minor | Illustrative instance, not a measured result. Kept because it is hedged ("some volume", "below the cutoff") and is what makes the cutoff concrete. |
| 10 | B06 | "a team frees up twenty hours a week" | ✓ as hypothetical | Explicitly a worked example. The number is the example's premise, not a finding — the framework, not the 20, is what the beat teaches. |
| 11 | B07 | The verdict's three lines | ✓ | Each recapitulates a claim already shown on screen. Verdict beats are exempt from no-source-no-verdict (they recapitulate, not assert). |
| 12 | B07 | "this is a model, not a measurement" | ✓ | **Required.** The caveat is spoken aloud *and* rendered as the last artifact line. Removing it would make the whole reel a DOUBLE-CHECK LAW violation. |

## Dating risk (strip anything that will age)

- No model names, version numbers, vendor names, or product claims appear in the body.
  **Correction, found at visual QC:** this is true of everything this reel authored, but
  not of the frame as a whole. The shipped `ClaudeComposerAsk` component renders a model
  chip in its composer chrome — on these renders it reads **"Fable 5"** — so a model name
  IS on screen in the three composer beats (B00, B03, B08). It is component chrome, not a
  claim the reel makes, and the narration never refers to it. Logged rather than removed:
  editing it means changing a shared fidelity component used by other reels. It does mean
  the bookends will date faster than the body.
- No dates, no counts that drift, no "as of" figures.
- The only proper noun in the body is Claude, at B03, as the tool being prompted.
- Expected shelf life: the argument survives any model generation, because it is about
  which costs a generation tool touches — not about what any tool can currently do.

## Register check (the rewrite requirement)

The DOUBLE-CHECK LAW's real test: could this script have been read off a source? No —
there is no source. The Teardown move here is the mirror-image sin the genre is prone to:
the reel refuses to celebrate the productivity gain *and* refuses to dismiss it, and lands
on the one structural consequence (the bottleneck moved) with its own falsifier attached.

## Corrections applied during authoring

1. Cut a B02 line asserting a specific cost-per-asset drop — replaced with the ordinal
   ranking and its label.
2. Cut a funnel beat that named percentage drop-offs per stage — replaced with the
   monotone ordinal shape plus the "illustrative, not measured" `slideMeta`.
3. Hardened B05 from an assertion into a falsifiable test, and moved the falsifier into
   the spoken narration rather than leaving it on screen only.
4. Added the caveat line to B07's artifact so the limitation survives into the recap.
