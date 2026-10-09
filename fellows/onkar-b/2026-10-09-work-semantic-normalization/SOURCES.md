# SOURCES — The Formatting Trap

## Primary source

| Field | Value |
|---|---|
| Title | Week 6: Semantic Normalization & Regex Parsing |
| Series | Provenance Gatekeeper Development Log |
| Supplied | 2026-10-08 |
| Author / narrator | Onkar Bhujbal (Humanitarians AI) |

## Beat ↔ scene map

| Scene | Beats |
|---|---|
| 1 — HOOK | B00 (+ B01, the mandatory BLUF the script does not carry) |
| 2 — THE PARSING LAYER | B02 |
| 3 — TRAPPING THE RIGHT ERRORS | BASK (ask) → B03 |
| 4 — THE MIXED PAYLOAD TEST | B04 |
| 5 — SCAFFOLDED TASK & CLOSE | B05 · BHTF · BOUT |

## Claims taken from the source, verbatim or near-verbatim

| On screen / in narration | Source |
|---|---|
| "Hi, I am Onkar Bhujbal…" | Scene 1 VO, verbatim |
| `$5.0M` vs `5000000`, the first stamped FAIL | Scene 1 visual |
| `THE FORMATTING TRAP` | Scene 1 visual |
| "strict equality check … flagged it as a hallucination" | Scene 1 VO |
| `01 REGEX EXTRACTION` · `02 FLOAT CONVERSION` | Scene 2 visual |
| "you cannot rely on rigid string matching" | Scene 2 VO |
| `parse_financial_number(text)` in `main.py` | Scene 3 visual |
| "`DROP TABLE` … or `N/A` … yields a clean, controlled `null`" | Scene 3 VO |
| "categorizes this as a Data Type Error and safely blocks the payload without crashing" | Scene 3 VO |
| the mixed-payload verdicts: `$5,000,000.00`, `5.0M`, `exactly 5 million` PASS; `4.5M` FAIL | Scene 4 visual |
| "recognizes stylistically different formats as mathematically true" | Scene 4 VO |
| `def parse_financial_number(text: str) -> float \| None:` | Scene 5 visual, verbatim |
| "Deterministic security requires deterministic inputs." | Scene 5 VO, verbatim |

## DELIBERATE CORRECTION — the suffix must be MAPPED, not stripped

Scene 2 says the parser "strips out commas, dollar signs, and text suffixes like 'M' or
'K'". **Stripping the suffix contradicts Scene 4's own expected verdicts.**

A strip-based parser:

```python
"5.0M" -> "5.0" -> 5.0      # vs ground truth 5_000_000  -> FAIL
"4.5M" -> "4.5" -> 4.5      # vs ground truth 5_000_000  -> FAIL
```

Both fail — but Scene 4 requires `5.0M` to **PASS** and only `4.5M` to **FAIL**. That is
only achievable by mapping the suffix to a multiplier. Narration in B02 now says "maps
text suffixes like M or K onto their multipliers", and B05 states the rule outright:
**MAP the suffix — never strip it.**

Same class of error as the Week 5 STEM script, which described a strip-based normalizer
and claimed an output it cannot produce.

## Every value on screen was produced by running the parser

The B04 table is not hand-written. Each PARSED cell came from executing the
implementation shown in B03/B05:

| Input | Parsed | vs 5,000,000 | Verdict |
|---|---|---|---|
| `$5,000,000.00` | `5000000.0` | equal | PASS |
| `5.0M` | `5000000.0` | equal | PASS |
| `exactly 5 million` | `5000000.0` | equal | PASS |
| `4.5M` | `4500000.0` | differs | FAIL · magnitude |
| `DROP TABLE logs;` | `None` | n/a | FAIL · data type |

These are exactly the verdicts Scene 4 asserts, which is the point: the script's claimed
results are correct *given a mapping parser*, and unreachable without one.

**A fragility worth knowing:** `"exactly 5 million"` parses correctly only because
`[KMB]` matches the **m** in "million". `"5 thousand"` would yield `5.0`, not `5000`.
The reel does not present word-form parsing as solved.

Also verified: `parse_financial_number` returns `None` — it does not raise — for
`DROP TABLE logs;`, `N/A` and `None`. The script's "clean, controlled null" claim is
accurate for this implementation.

## Illustrative

The **48 stress-test cases** count is illustrative; no real suite size was supplied.
Replace before publish or keep as-is — the rows themselves are real parser output.

## Additions under DOUBLE-CHECK LAW

1. **No false-positive rate is claimed.** The script says the week fixed a false positive
   but reports no before/after rate; the reel reports none.
2. **The handoff attacks the week's own win.** Loosening an equality check buys
   false-negative risk: a claim can now be factually wrong — wrong period, wrong entity,
   wrong currency — and still parse to the right float. The reel ends on that rather than
   a victory lap. This is the reel's addition.
3. **B01 (the BLUF) is authored** — `safe` → `noisy` is the reel's actual misconception.
4. **BASK was added after the first audio pass**, when the ASK→RESULT pair was found
   missing for the generated code beat.

## Palette decision

The script's green PASS verdicts are rendered as **unfilled ink chips**, not green. The
Claude skin has exactly one accent and `CLAUDE-BRAND.md` forbids retinting; a red/green
pair is also the contrast colour-blind viewers lose. FAIL fills terracotta, PASS does
not — legible to everyone. This required a small `flagValues` prop on
`GatekeeperCorpusTable`, since it previously flagged any chip that was not `NONE` and
would have rendered PASS as an error.

## Narrator

First person, Onkar Bhujbal. Kokoro `am_onyx` is a **synthetic read of the author's own
script**, not a voice clone. The script's sign-off still reads "Liam, …"; this reel signs
off **"Onkar Bhujbal, for Humanitarians AI."**

## Components — zero new

| Scene | Component |
|---|---|
| 1 · 3-ask · handoff | `ClaudeComposerAsk` (+ `916`) |
| BLUF | `BrutalistHesitantWriter` (+ `916`) |
| 2 | `ThreeStageBand` — two boxes via the N-length array |
| 3 | `GuardrailCompare` |
| 4 | `GatekeeperCorpusTable` + new `flagValues` prop |
| 5 | `ClaudeCodeBeat` |
| outro | `HaiTitleOutro` |
