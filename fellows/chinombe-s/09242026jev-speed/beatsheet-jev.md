# Beat Sheet — Why Jev Is Fast

**Channel:** claude-hai · **Persona:** Simba · **Voice:** Kokoro `af_bella`
**Format:** ai-explainer, general topic — vendor-claim caveats throughout · Two cuts this build.

## 16:9 long cut — 4:14 (254.11s, Kokoro ground truth)

| Beat | Act | Timestamp | Duration | Pattern | Note |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 22.0s | `ClaudeComposerAsk` | Cold open — ms vs. seconds |
| B01 | SUMMARY | 0:22 | 17.9s | `ClaudeStatement` | BLUF — the split |
| B02 | STRUCTURE | 0:40 | 22.3s | `AutoregressiveLoop` | How a general LLM decodes |
| B03 | STRUCTURE | 1:02 | 15.3s | `ParallelPass` | How Jev decodes |
| B04 | REASONING | 1:18 | 36.3s | `GuardCards` | Three enabling factors (3rd card unverified) |
| B05 | RESULTS | 1:54 | 23.8s | `DataTable` | TypeSafe's own numbers |
| B06 | REASONING | 2:18 | 27.5s | `FactStack` | The caveat, in the company's own words |
| B07 | FINDINGS | 2:45 | 18.4s | `FindingPair` | Tom's Hardware's skepticism |
| B08 | FINDINGS | 3:04 | 24.4s | `FindingPair` | Not apples to apples |
| B09 | SUMMARY | 3:28 | 26.4s | `ClaudeVerdictArtifact` | Verdict — mechanism real, magnitude unverified |
| B10 | NEXT STEPS | 3:54 | 16.2s | `ClaudeComposerAsk` | Your Turn |
| B11 | OUTRO | 4:10 | 3.8s | `ClaudeTitleOutro` | Sign-off |

## 9:16 Shorts cut — 0:45 (44.64s, Kokoro ground truth)

THE SHORTS LAW derivative: single cycle, no revision, condensed subset (hook, the ParallelPass mechanism diagram, the headline numbers, verdict, outro), pointing back to the long cut.

| Beat | Act | Timestamp | Duration | Pattern | Note |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 9.7s | `ClaudeComposerAsk916` | Condensed hook |
| B01 | STRUCTURE | 0:10 | 9.3s | `ParallelPass916` | How Jev decodes, portrait |
| B02 | RESULTS | 0:19 | 9.9s | `DataTable916` | Headline numbers |
| B03 | SUMMARY | 0:29 | 9.9s | `ClaudeVerdictArtifact916` | Verdict |
| B04 | OUTRO | 0:39 | 6.0s | `ClaudeTitleOutro916` | Points back to the long cut |

## GATE L note

Searched `/home/claude/tk/runtime/remotion/src/scenes/` before authoring anything new. All three diagram beats (B02–B04) reuse existing components as-is:

- **B02** `AutoregressiveLoop` — same component built for `hai-prefill-decode`'s decode framing. Direct fit for general-LLM autoregressive decoding.
- **B03** `ParallelPass` — same component built for `hai-prefill-decode`'s prefill framing, repurposed here for Jev's single-pass typed output. Legitimate reuse: both are "one forward pass, multiple outputs at once" shapes.
- **B04** `GuardCards` — reused for the three enabling factors, third card deliberately `ok:false` as a visual foreshadow that the "can't produce a type error" claim is company-stated, not independently verified (unpacked in B06–B08).

All three 916 compositions (`ParallelPass916`, `AutoregressiveLoop916`, `ClaudeComposerAsk916`, `DataTable916`, `ClaudeStatement916`) already existed in `Root.tsx` from prior builds — no new Root.tsx entries were needed for this reel.

**Component bug found and fixed during QC**: `GuardCards.tsx`'s card layout math (`cardTop`, `cardGap`, `cardH`) was hardcoded for exactly 2 cards — a 3rd card's bottom edge fell at `1.04×` frame height in landscape, overflowing past the frame and colliding with the sparkLine. Fixed by computing `cardGap`/`cardH` from `cards.length` and the available vertical space between `cardTop` and a bottom limit that reserves room for the sparkLine. Verified via `tsc --noEmit` (clean) and a re-render + re-QC of B04 (all three cards now fit cleanly). This is a general component fix — it will also correct any future reel that passes `GuardCards` more than 2 cards.

## Sources

Same four sources as `SCRIPT-jev-speed.md`: TypeSafe AI's own blog and homepage, Tom's Hardware's coverage, and Wikipedia's background/funding page — see that file for full citations.
