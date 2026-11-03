# SOURCES.md — grading-the-machine

Primary source: `08_grading_the_machine.md` (the authored script with
inline `[VISUAL: …]` stage directions, narration lightly revised — see
"Corrections applied to narration" below) and `08_narration_tts_ready.txt`
(the condensed narration actually spoken, split by beat). Both live in
this folder.

## Scope (per established series convention)

Like STEM2, STEM6, and STEM7, this is a **general conceptual explainer**,
not a first-person account of this project's own implementation. Per the
channel's standing note, STEM videos don't need to match the real product
code (`D:\Code\mycroft\verification-layer`). Every claim below is checked
against standard practice for AI confidence scoring and evaluation, not
against a specific file or line reference.

## Corrections applied to narration

Per the standing house style convention (first raised on STEM6, now
applied proactively): two instances of a repeated "X, and the reason is
worth sitting with" / "doesn't X; it just Y" contrastive construction
were lightly rewritten for natural spoken cadence — no factual or
structural content changed:

| # | Location | What changed |
|---|---|---|
| 1 | B02 (LLM-as-a-judge) | "It doesn't, and the reason is worth sitting with: a highly capable judge model..." → "It doesn't — because a highly capable judge model..." |
| 2 | B04 (never suppress) | "doesn't protect anyone; it just replaces a visible warning with silent incompetence" → "protects nobody — it just trades a visible warning for silent incompetence" |

## Factual claims (DOUBLE-CHECK LAW)

| Beat | Claim | Verdict | Basis |
|------|-------|---------|-------|
| B01 | Self-reported confidence is produced by the same model/process that produced the answer, with no separate error-checking module | ✓ | Correct and precise — a single forward pass (or a single model appending a confidence token) has no architecturally distinct "honesty checker"; it's the same weights, same failure modes |
| B01 | Self-reported confidence measures textual fluency/tone more reliably than it measures correctness | ✓ | Well-attested LLM behavior: models are not reliably calibrated when self-reporting confidence, and fluency of the stated confidence doesn't track ground-truth accuracy |
| B02 | An LLM judge evaluates whether reasoning *sounds* plausible, not whether it's genuine | ✓ | Correct characterization — a judge model has no privileged access to whether a chain of reasoning was the actual process that produced the answer versus a fluent post-hoc rationalization; both are equally well-formed text to a plausibility check |
| B02 | A fluent rationalization and genuine reasoning are not distinguishable by a plausibility-only judge | ✓ | Follows directly from the above — "is this coherent" and "is this how the answer was actually derived" are different questions, and a judge scoring only the first cannot answer the second |
| B02 | "Serious systems... walked away from this approach" | ⚠ **stated generally, no specific system named** | The script makes this claim without citing a specific project; narration keeps it general ("serious systems") rather than naming an unverified specific case, avoiding an unsupported specific claim |
| B03 | A computed score built from fixed, programmatic penalties on observable conditions doesn't take fluent prose as an input | ✓ | Correct by construction — a scoring function that only reads structured signals (fetch success/failure, simulated-vs-live flags, retry counts) has no code path where the text's persuasiveness affects the number |
| B03 | The specific example (base 1.0, -0.1 per issue, final 0.8) | ⚠ **illustrative** | A constructed worked example from the source script's own `[VISUAL]` direction, not a measurement from a real run — declared here per DOUBLE-CHECK LAW, consistent with prior episodes' own worked-example precedent |
| B04 | Suppressing or softening a low-confidence result removes the user's ability to discount it appropriately | ✓ | Standard human-factors/safety-design principle: a hidden or buried caveat cannot inform a decision the user doesn't know needs discounting |
| B05 | Penalty constants in a first-pass computed scoring system are typically argued from first principles rather than empirically calibrated | ✓ | Reasonable, general claim about any new computed-scoring system — a first version of fixed deduction values necessarily starts as a design choice before real-outcome data exists to calibrate against |
| B05 | A computed, inspectable score is a precondition for calibration in a way a self-reported or judge-based score is not | ✓ | Correct — you can only backtest/adjust a scoring function's constants if the function is written down explicitly; a plausibility judgment (self-reported or LLM-judged) has no such constants to adjust |
| B06 | The three-way comparison (self-graded/AI-judged/computed) | ✓ | Direct synthesis of B01/B02/B03's already-verified claims, not a new claim |
| B09 | The next problem concerns an agent being instructed by content it's merely reading | ✓ | Matches this channel's own next-scripted reel, `youtube/STEM9/09_the_agent_that_was_told_what_to_do.md`, confirming the tease is a real, already-scripted follow-up |

## Anti-staleness check (DOUBLE-CHECK LAW)

No model name, vendor, version number, or benchmark score appears in the
narration. Every mechanism described (self-reported confidence, LLM-as-
judge, computed scoring, suppression, calibration) is a general design
pattern, not tied to a specific product generation, so the reel should
not date.

## Simplifications (declared)

- **The worked ledger example (B03/B05) is illustrative**, not a logged
  trace from a real run — declared above and in-scene.
- **"Serious systems walked away from this approach" (B02) is kept
  general**, not attributed to a specific named project, since the
  source script doesn't cite one and inventing a specific citation would
  fail DOUBLE-CHECK LAW.
- **The penalty values (-0.1 per issue) are a stand-in**, not a claim
  about what any real system's actual constants are or should be.

## Content carried and cut

| Source | Status | Note |
|---|---|---|
| Title card (report card, "A+" stamped "GRADED BY WHOM, EXACTLY?") | Not built as a literal beat | Carried thematically into B00's composer framing; B00 is locked to `ClaudeComposerAsk` per COLD OPEN LAW |
| "The First Bad Idea" section | Carried | B01 |
| "The Second Bad Idea" section | Carried | B02, including the CATEGORY ERROR stamp from the source's own `[VISUAL]` direction |
| "The Approach That Actually Holds Up" section | Carried | B03 |
| "Never Suppress a Low Score" section | Carried | B04 |
| "The Honest Caveat" section | Carried | B05, the falsifiability/limits beat |
| End card (three stacked panels) | Carried | Becomes B06, the framework beat, matching the source's own closing visual almost exactly |
| Closing aphorism ("a lower bar than guaranteed correct...") | Carried | Folded into B06's landing line |
| Key Takeaways (6 bullets) | Carried, condensed to 3 | The three-way comparison in B06/B07 covers takeaways 1–3 directly; takeaways 4–6 (never suppress, still calibrating, opinion-to-equation) are each their own dedicated beat (B04, B05) rather than compressed into the recap |

## Palette retint (declared, per STEM2/STEM6/STEM7 precedent)

The source script's `[VISUAL]` directions call for a yellow caution
highlight (B05) and a green "PLAUSIBLE ✓" stamp (B02). Per the Claude
fidelity palette (no blue, no green, no yellow — see `graphics_lib.py`'s
header comment), these are retinted to **terracotta** (the house accent),
carried by label, icon, and position rather than a second/third hue.

## Free pipeline — no paid spend

Kokoro `am_onyx` (local, free) is the planned narration engine. No
ElevenLabs, no FLUX, no paid services. No publishing — the master stays in
this folder. **Audio has not yet been generated as of this writing — see
PEDAGOGY.md, GATE P is PENDING.**
