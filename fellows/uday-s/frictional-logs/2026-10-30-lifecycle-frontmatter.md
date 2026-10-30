# Frictional log — lifecycle frontmatter on 91 recipes

**Date:** 2026-10-30 · **Branch:** `chore/recipe-lifecycle-frontmatter`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Add the `status` / `todos_open` / `last_gate` / `attestation` / `recipe_version` block the
constitution requires to the 91 recipes that had none.

## Where the work resisted

- **A first survey said 42 of them had built scripts**, which would have made `status:
  DRAFT` a mislabel for nearly half the batch. It was the wrong query: it matched any
  `scripts/**/*.py` the recipe mentions, which includes the legacy n8n node scripts that
  exist as 74-line scaffolds. Asking the right question — scripts named in the **Script
  Locations** table, i.e. the six canonical steps — returned zero for all 93. DRAFT is
  correct, and now it is a measured claim rather than a default.

- **`todos_open: 0` would have been a lie in 94 of 97 cases.** The real counts are 0, 4, 5,
  6, 7 or 8 depending on the recipe. Writing a convenient zero across the batch is exactly
  the unevidenced claim this frontmatter exists to prevent.

- **A naive TODO count reads two too high.** Gate 1's test greps for `[TODO: DEFINE]` and
  gate 5's for `[TODO: APPROVE]`, so those marker strings appear inside backticked test
  commands in every recipe built from the template. A count that includes them would have
  put `todos_open: 8` on recipes with 6 open items.

## What was done about it

- Wrote the generator to **refuse** any recipe with canonical scripts on disk rather than
  stamp DRAFT on it. The refusal path was never triggered, which is the point: it was there
  in case the survey was wrong again.

- Counted open todos per recipe, excluding markers inside backticked commands.

- Set `last_gate` and `attestation` to null after checking that only two recipes have gate
  decisions and only one has an attestation.

- Verified the edit was a pure prepend: reconstructed each original by stripping the added
  block and compared against the committed version. **0 bodies altered across 91 files.**

## What this unblocked

`check --all` went from **171 defects to 80**, and from 0 clean recipes to **90**. The 91
`no-lifecycle-status` findings are closed, and what remains is the real contract work: the
flag mismatches in the 6 built recipes, plus three one-off structural findings.

Every number `check` reports is now about recipes that claim something.

## What was learned

**The first survey asked a question that looked right.** "Does this recipe reference a
script that exists" and "are this recipe's canonical steps built" differ by the scaffolds,
and the difference was 42 recipes — enough to mislabel half the batch. The answer only
changed when the query was narrowed to the table that actually defines the steps.

**A bulk edit to 91 files needs a refusal path more than it needs a dry run.** The dry run
confirmed the count; the refusal would have caught a wrong premise. It cost four lines and
never fired, which is the best outcome available to it.
