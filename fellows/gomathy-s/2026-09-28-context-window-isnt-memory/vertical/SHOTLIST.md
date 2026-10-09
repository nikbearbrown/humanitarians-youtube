# SHOTLIST — claude-liam-context-window (12-beat / 60s cut)
## Total: 1:03 (63.16s) · 12 beats

Reworked from the 9-beat/154.5s long cut to match the Brutalist first-project
spec (60s, 12 beats) — same thesis, facts, sources, Bella voice, `@HumanitariansAI`.

| Beat | Act | Pattern | Duration (s) | Notes |
|---|---|---|---|---|
| B00 | OPEN | `ClaudeComposerAsk` | 5.50 | Cold open; hook on the memory misconception ("that's not memory failing — it's a budget") |
| B01 | BLUF | `BrutalistHesitantWriter` | 3.19 | Single-line correction: "Claude's memory" → "a fixed budget." Stakes line cut for length. |
| B02 | I | `FormBCard` | 3.89 | System prompt / Tool definitions / Conversation history |
| B03 | I | `FormBCard` | 4.06 | Your message / Claude's reply |
| B04 | II | Manim `B04_TokenSplit` | 6.02 | Tokens ≠ words; running-total bar |
| B05 | II | `FormBCard` | 4.68 | Code / Numbers / Jargon / Non-English text — cost more per word |
| B06 | III | `AttritionChain` | 7.10 | Room-remaining climb to ceiling + "context rot" restored as a tendency |
| B07 | III | `FormBCard` | 5.04 | Error / Summary / Dropped turns — depends on the app |
| B08 | IV | `ScaleComparison` | 5.06 | Relative window-size scale; filling more costs more |
| B09 | CLOSE | `ClaudeVerdictArtifact` | 6.79 | Summary restates the thesis verbatim: "a context window is a fixed, shared budget — not memory" |
| B10 | CLOSE | `ClaudeComposerAsk` | 6.07 | YOUR TURN; one-line check ("does it say what to drop first?") |
| B11 | CLOSE | `OutroCTA` | 5.76 | Title + `@HumanitariansAI` handle |

## What was dropped or merged from the 9-beat/154.5s long cut

| Change | Why |
|---|---|
| 5-layer `ClaudeScienceLayerStack` (one beat, long cut) → two `FormBCard` beats (B02, B03) | `ClaudeScienceLayerStack` has a **fixed 30s native render** with no duration override; its reveal timing can't complete inside a ~4s beat (compile.py *truncates* clips longer than the target, it doesn't speed them up — confirmed by render, not assumed). `FormBCard` reveals fast enough for beats this short. Real cost: loses the "stacking into one container" visual metaphor for a flatter list-of-things card. |
| 4-row token-cost comparison table (exact counts, growing bars) → `FormBCard` list (B05) | No time to build the comparison chart in ~4.5s. Keeps the claim, drops the on-screen counter evidence. |
| Three-outcome elaboration (why apps error / summarize / drop) → three words in one breath (B07) | No individual explanation of each mechanism — named, not explained. |
| Handoff's 3-point rubric → one check question (B10) | "Does it say what to drop first?" replaces the fuller three-question rubric from the long cut. |
| Verdict's four enumerated points → two sentences restating the thesis (B09) | Per this pass's explicit instruction: the summary must restate "a context window is a fixed shared budget, not memory" plainly, not itemize every supporting fact. |
| "Context rot" named term | Cut from the long cut's B00, then **restored** as a one-line tendency in B06 per this pass's instruction — kept in the final cut. |

## Doctrine tension (disclosed, not hidden)
At ~5s/beat average, this cut cannot fully satisfy `nopunt`'s whole-sheet
teaching-arc checklist the way the 154.5s long cut did:
- **FRAMEWORK** and **BOOKENDS** still hold.
- **WORKED EXAMPLE** — B06's ceiling climb is the closest thing to one, but
  it no longer walks concrete turn-by-turn numbers on screen the way the long
  cut's B04 did.
- **FALSIFIABILITY** — B04/B05 gesture at "tokens aren't uniform" but don't
  stress-test the framework the way the long cut's dedicated beat did.
- **SCAFFOLDED TASK** — weakened from a 3-point rubric to 1 question.

This is a real, accepted cost of the 60s/12-beat format, not an oversight.
