# SOURCES — The Tokenization Problem

## Primary source

| Field | Value |
|---|---|
| Title | Week 6: Deterministic Parsing vs. Probabilistic Tokens |
| Series | STEM AI Explainer (built on the `claude-stem` channel) |
| Supplied | 2026-10-08 |
| Author / narrator | Onkar Bhujbal (Humanitarians AI) |

## Beat ↔ scene map

| Scene | Beats |
|---|---|
| 1 — HOOK | B00 (+ B01, the mandatory BLUF the script does not carry) |
| 2 — TOKENS ARE NOT MATH | B02 |
| 3 — DOWNSTREAM DESTRUCTION | B03 |
| 4 — THE DETERMINISTIC SHIELD | B04 (ask) → B05 |
| 5 — SCAFFOLDED TASK & CLOSE | B06 · BHTF · BOUT |

## Claims taken from the source, verbatim or near-verbatim

| On screen / in narration | Source |
|---|---|
| "Hi, I am Onkar Bhujbal…" | Scene 1 VO, verbatim |
| "Why can't a trillion-parameter model write a number?" | Scene 1 visual |
| `THE TOKENIZATION PROBLEM` | Scene 1 visual |
| "integer digits, a comma-separated string, or a dollar sign with a decimal" | Scene 1 VO |
| `01 PROBABILISTIC GUESSING` · `02 TOKEN FRAGMENTATION` | Scene 2 visual |
| "They do not perceive 'five million' as a quantitative value." | Scene 2 VO |
| `$5.0M` → a script expecting `int` → crash | Scene 3 visual |
| "a single unexpected dollar sign will trigger a fatal type error" | Scene 3 VO |
| "You cannot prompt-engineer your way out of this inconsistency." | Scene 3 VO |
| regex layer between LLM and database; strip noise, extract value, convert to float | Scene 4 VO |
| "If the extraction fails, you drop the payload." | Scene 4 VO |
| `TASK: Never trust an LLM to format data.` | Scene 5 visual |

## DELIBERATE CORRECTION — stripping the suffix destroys the magnitude

Scene 4 states that the regex layer turns `$5.0M` into `5000000.0`. **A regex that merely
strips non-numeric characters cannot do that**, because the `M` is non-numeric:

```python
re.sub(r'[^0-9.]', '', "$5.0M")   # -> '5.0'
float('5.0')                       # -> 5.0, not 5_000_000
```

To reach the script's stated output the suffix must be **mapped to a multiplier**, not
removed. The parser shown on screen does that, and was verified by execution:

```python
SUFFIX = {'K': 1e3, 'M': 1e6, 'B': 1e9}
# "$5.0M" -> 5000000.0   ✓ the script's stated result
```

The narration names this explicitly — "stripping the M would leave you with five point
zero" — turning the script's gap into the beat's teaching point.

This is the same class of error as Week 5's `'4.5.'` → `ValueError`. Both scripts
describe a strip-based normalizer; both state outputs a strip-based normalizer cannot
produce.

## Verified by execution, not assumed

- `int('$5.0M')` → `ValueError: invalid literal for int() with base 10: '$5.0M'`.
  The message shown in B03 is byte-for-byte what CPython emits.
- The B05 parser returns exactly `5000000.0` for `$5.0M`.

## Other additions under DOUBLE-CHECK LAW

1. **No model, vendor or parameter count is named.** The script's "trillion-parameter"
   framing is kept in the hook's question only, where it is rhetorical, and no specific
   system is attributed.
2. **B06's four-input test table is the reel's addition.** The script's Scene 5 is a
   slogan; the table makes it runnable and failable.
3. **B01 (the BLUF) is authored** — `knows` → `spells` is the reel's actual
   misconception.
4. **"glowing blue REGEX filter" not rendered blue.** The Claude skin has exactly one
   accent; a blue would be a second. The shield reads as solid ink with a passing stamp.

## Narrator

First person, Onkar Bhujbal. Kokoro `am_onyx` is a **synthetic read of the author's own
script**, not a voice clone. The script's sign-off still reads "Liam, …"; per the
author's standing instruction this reel signs off **"Onkar Bhujbal, for Humanitarians
AI."**

## Components — zero new

| Scene | Component |
|---|---|
| 1 · 4-ask · handoff | `ClaudeComposerAsk` (+ `916`) |
| BLUF | `BrutalistHesitantWriter` (+ `916`) |
| 2 | `ThreeStageBand` — two boxes via the N-length `stages` array |
| 3 | `ThreeStageBand` in **failure mode** (`failIndex: 1`) — the pipeline breaking |
| 4 | `GuardrailCompare` with `stampBlocked: false` — the passing case |
| 5 | `ClaudeCodeBeat` |
| outro | `HaiTitleOutro` |
