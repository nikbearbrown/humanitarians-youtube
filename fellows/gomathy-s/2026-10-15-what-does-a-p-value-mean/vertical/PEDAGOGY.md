# PEDAGOGY — What Does a P-Value Actually Mean? (claude-hai, 12 beats / ~63.5 s)

Verdict: PASS — reviewed and approved by Gomathy. Self-check written by the builder after the review cuts; author reviewed and accepted the known weaknesses listed below. Applies to both cuts — vertical/ carries the same narration and on-screen text.

Thesis: a p-value is how likely data at least this extreme would be if there
were no real effect (the null and the model both true). It is not the chance
you're right, not the size or importance of the effect, and p < 0.05 alone
proves nothing. Primary source: the ASA's 2016 statement (Wasserstein & Lazar).

Audience (`claude-hai`): students getting started with AI and with reading
research. Spine question (when to lean on a tool and when not to) lands in
B07–B08: don't let one number decide; report what the p-value can't tell you.

## Act structure

| Beat | Role | Self-check |
|---|---|---|
| B00 | Cold open, ask lands answered (COLD OPEN LAW) | ✓ hook is a number students meet in papers ("p is zero point zero three"); spoken only, ILLUSTRATIVE |
| B01 | BLUF via hesitant writer | ✓ correction is the reel's misconception: "the chance you're right" → "how likely data this extreme is / if there's no real effect." ✗ ~6.2 s, not the ≥ 9 s the law asks for (same trade as knowledge-cutoff) |
| B02 | Framework: assume the null and the model | ✓ framework before any example; "null hypothesis" named on its first use |
| B03 | Framework: the shaded share | ✓ "at least this extreme" drawn as a tail, ILLUSTRATIVE |
| B04 | Worked example: coin, 11/1024 | ✓ computed in `scenes.py`; one-sided, logged in SOURCES.md (two-sided ≈ 2%) |
| B05 | What it doesn't measure | ✓ ASA principles 2 and 5, numbered on the card |
| B06 | Counter-example: huge study, tiny effect, tiny p vs small study, big effect, large p | ✓ the falsifiability beat: shows the misreading failing, with computed numbers |
| B07 | No bright line | ✓ principles 3 and 6 |
| B08 | Report with it | ✓ principle 4; effect-size / CI row flagged INFERENCE |
| B09 | Summary (verdict bookend) | ✓ restates the definition and the two "nots" |
| B10 | Your turn: prompt + one check | ~ prompt read aloud in a shortened form (narration: "explain this result's p-value plainly, and what it doesn't tell me"; screen adds "Here's a result from my field: [paste it]."); check: "does it give effect size?" |
| B11 | Title-restate outro | ✓ "What Does a P-Value Actually Mean?" Bella, in for Gomathy |

## Register (Plain)

- One idea per beat; "null hypothesis" defined in B02 before B03/B09 use "the null".
- Hedges only where the source is inference (B01/B09 "no real effect" paraphrase; B08 CI row).
- No "statistically significant" on screen; no dates or model names. UI chip "Claude".

## Evidence discipline

Every claim beat has its card or diagram on screen; ASA principle numbers sit
on the B05/B07/B08 cards. All example numbers are computed (FACTCHECK.md) and
labelled ILLUSTRATIVE on screen.

## Known weaknesses (for the reviewer)

1. B01 timing below the executive-summary law (~6.2 s vs ≥ 9 s).
2. "If there's no real effect" compresses "the null and the model are true";
   the model half returns only on the B02 and B09 cards.
3. B03 sketches a one-tailed picture; two-sided tests are not shown.
4. B10 narration paraphrases the on-screen prompt rather than reading it verbatim.
5. Runtime ~63.5 s, not 60 s (audio at Kokoro speed 1.08; B06 lengthened on review; see BUILD-LOG.md).
