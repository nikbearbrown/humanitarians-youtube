# CHECKS-REPORT — The Formatting Trap

Reel: `claude-gatekeeper-semantic-normalization` · 9 beats · **measured 133.2s (2:13)** vs 2:45 target
**GATE V (16:9): 18 frames · 0 BLOCKER · 0 MAJOR ✓** (after one fix — below)

## Deliverables

| | File | Format |
|---|---|---|
| 16:9 master | `claude-gatekeeper-semantic-normalization-slate.mp4` | 3840×2160 @ 24fps |
| 9:16 companion | `vertical/claude-gatekeeper-semantic-normalization-vertical-slate.mp4` | 1080×1920 @ 24fps |

## Per-beat classification

| Beat | Class | Measured | Pattern |
|---|---|---|---|
| B00 | SHOW | 20.12s | ClaudeComposerAsk |
| B01 | SHOW | 11.97s | BrutalistHesitantWriter — ≥9s ✓ |
| B02 | SHOW | 21.03s | ThreeStageBand (two stages) |
| BASK | SHOW | 8.38s | ClaudeComposerAsk — clears the ≥7s typing floor |
| B03 | SHOW | 17.90s | GuardrailCompare |
| B04 | SHOW | 17.77s | GatekeeperCorpusTable + `flagValues` |
| B05 | SHOW | 13.46s | ClaudeCodeBeat |
| BHTF | SHOW | 14.40s | ClaudeComposerAsk |
| BOUT | SHOW | 8.02s | HaiTitleOutro |

**9 SHOW / 0 HOLD / 0 PUNT.** Slots 9/9. No slates. **Zero new components.**

## Two defects found and fixed

| Where | Defect | Fix |
|---|---|---|
| Beat sheet | **The reel was authored with no ASK→RESULT pair.** B03 shows generated code with no preceding ask beat, which every prior reel honours. Caught after the first audio pass. | `BASK` inserted before B03, audio regenerated. 8 beats → 9. |
| B03 | **GATE V: `low-contrast` MAJOR.** The verdict stamp faded in, putting white text on a part-transparent terracotta fill over cream. Because clips are trimmed to measured audio, the fade occupied most of the stamp's visible life — translucent for the whole beat, crisp only in frames nobody sees. | Filled stamps never fade now: they slide in at full opacity and arm at p≈0.60. Fixed in `GuardrailCompare`, so the Week 4 and Week 6 STEM reels improve too. |

The second is the third distinct way clip-trimming has produced a defect — after tails
being cut outright, and a label ramping later than its own fill.

## The script says "strip the suffix" — its own Scene 4 requires "map the suffix"

Scene 2: the parser "strips out … text suffixes like 'M' or 'K'".
Scene 4: `5.0M` must **PASS** against a five-million ground truth, `4.5M` must **FAIL**.

Those cannot both hold. Stripping gives `5.0` and `4.5` — both fail. Only mapping the
suffix to a multiplier produces the verdicts the script asserts. Narration corrected in
B02; B05 states the rule outright: **MAP the suffix — never strip it.**

### Every value in B04 was produced by running the parser

| Input | Parsed | Verdict |
|---|---|---|
| `$5,000,000.00` · `5.0M` · `exactly 5 million` | `5000000.0` | PASS |
| `4.5M` | `4500000.0` | FAIL · magnitude |
| `DROP TABLE logs;` | `None` | FAIL · data type |

Exactly the verdicts Scene 4 asserts. Also verified: the parser **returns** `None` rather
than raising for `DROP TABLE logs;`, `N/A` and `None`, so the script's "clean, controlled
null" claim is accurate for this implementation.

**Known fragility, not hidden:** `"exactly 5 million"` parses only because `[KMB]`
matches the **m** in "million". `"5 thousand"` would yield `5.0`. Word-form parsing is
not presented as solved.

## Colour decision

The script's green PASS verdicts render as **unfilled ink chips**, not green — one accent
only, and red/green is the pair colour-blind viewers lose. This needed a `flagValues`
prop on `GatekeeperCorpusTable`, which previously flagged any chip that was not `NONE`
and would have painted PASS as an error. Defaulted, so earlier reels are unchanged.

## Open items

1. **The 48 stress-test case count is illustrative** — no real suite size supplied. The
   table rows themselves are real parser output.
2. **Runtime 2:13 vs 2:45 target.** Not padded; duration is an output.
3. **Lane-mix warning (not blocking).** `remotion` carries 9/9 beats.
4. **SKIN LINT warning (expected).** `BOUT` uses `HaiTitleOutro`.
5. **Paperwork.** Built with `ART_FACTS=0`.
6. **`./art final` not run** — no label-free master yet.
