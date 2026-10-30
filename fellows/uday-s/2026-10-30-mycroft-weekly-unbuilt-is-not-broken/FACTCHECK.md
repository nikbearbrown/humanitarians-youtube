# FACTCHECK — Unbuilt Is Not Broken

Status: **GATE F SIGNED — 2026-10-30. 13 rows PASS, 1 self-inflicted error FOUND
AND PUT ON SCREEN, 3 figures NOT REPRODUCED and therefore NOT SHOWN.**

Subject: `mycroft` @ `6428457` on `chore/recipe-lifecycle-frontmatter`, with
companions `83793ff` and `0536907`. `git branch -r --contains HEAD` lists
`origin/chore/recipe-lifecycle-frontmatter` and `git status -sb` reports the
branch in sync, so this is the last pushed commit.

## Method

Two read-only routes:

1. **Ran the committed checker.** `node scripts/snickerdoodle.mjs check --all`.
   As in episode 8, `check` only reads files and prints — it does not execute
   the scripts it inspects and it does not write. (Episode 9's `gate` writes a
   record, which is why that one was never run.)
2. **Counted the committed tree.** `git ls-tree`, `git grep`, `git show`.

## Verified claims

| # | Beat | Claim | Verdict | How checked |
|---|---|---|---|---|
| 1 | B04 | 97 recipes | PASS | checker output |
| 2 | B04 | 80 defects after this commit | PASS | checker output |
| 3 | B04 | 90 recipes with no defects | PASS | checker output |
| 4 | B04, B01 | 554 unbuilt steps, named and not counted | PASS | checker output: "554 step(s) across 94 recipe(s) are not built — NOT counted above" |
| 5 | B01, B04 | 725 findings before severity, 171 after | PASS (author-reported) | commit body of `83793ff`; the pre-change state cannot be re-run without reverting |
| 6 | B05 | 91 recipes have zero canonical step scripts on disk | PASS | checker's own footnote: 6 recipes have at least one script, "the other 91 have nothing to compare against" |
| 7 | B05 | a first survey said 42 of them had built scripts | PASS (author-reported) | commit body of `6428457` |
| 8 | B06, B09 | 91 files changed, 728 insertions, 0 deletions | PASS | `git show --stat 6428457` |
| 9 | B09 | every hunk is `@@ -0,0 +1,8 @@` — a pure prepend | PASS | `git show --unified=0 6428457` — zero lines matching `^-`, and zero hunk headers that are not `@@ -0,0 +1,8 @@` |
| 10 | B09 | 728 / 91 = exactly 8 lines per file | PASS | arithmetic on row 8 |
| 11 | B09 | gate 1 greps for `[TODO: DEFINE]` and gate 5 for `[TODO: APPROVE]`, so a naive count reads two high | PASS | commit body, and the gate tests are in the recipes |
| 12 | B08 | the checker reports 97 recipes | PASS | checker output |
| 13 | B08 | `git grep -l '^status:' -- recipes/` returns 98 | PASS | run directly; the extra file is named below |

## The error I made while fact-checking, which is on screen

Counting how many recipes carry a `status:` line, I ran:

```
git grep -l '^status:' 6428457 -- recipes/   →  98
```

The checker says **97**. The difference is
**`recipes/vendor-intelligence-brief.yaml`** — a non-markdown file under
`recipes/` that happens to contain a `status:` line and is not a recipe. The
checker counts `.md` files excluding `_shared.md` and `README.md`: 99 − 2 = 97.

That is the **same error as the commit's own "42"**: matching a *folder* instead
of a *list*. It happened in the same week, while making a video about it. B08 is
that, on screen, with the file named.

Reconciliation, for completeness: 91 recipes gained frontmatter in this commit,
6 already had it, 91 + 6 = 97. Before the commit `git grep` returned 7 — the
same 6 recipes plus the `.yaml` file.

## Figures NOT reproduced, and therefore NOT on screen

Three numbers in the commit bodies could not be reproduced from the committed
tree, so none of them appears in any frame:

- **"531 files" of Python under `scripts/`** (`0536907`). A raw count at this
  commit gives **652**. 531 is what conformance *checks* after its
  location-based exclusions, which is a different quantity — the same situation
  as episode 7's "582 scripts".
- **"73 of the 157 .py files under data/"** (`0536907`). A raw count gives
  **106** under `data/`. The commit says those files "arrived afterwards, in
  another contributor's branch", so 157 appears to be a working-tree count at a
  state this branch does not contain.
- **"956 files conform"** (`0536907`). Reproducing it means running
  `npm run verify`, which is a build step rather than a read; it was not run.

The whole of `0536907` is therefore background in this reel, not evidence. No
figure from it is shown.

## Precision notes

- **"725 → 171 → 80" spans two commits.** 725→171 is `83793ff` (severity);
  171→80 is `6428457` (frontmatter). B04 shows all three figures in one chain
  and the narration attributes the two steps separately.
- **The 42 cannot be re-run** — it was a survey taken before the commit, not a
  committed artifact. It is the commit's own account, and the reel says "the
  first survey came back".
- **"0 bodies altered" is verified structurally, not by reconstruction.** The
  commit says it reconstructed each original and compared. I did not do that; I
  showed the diff contains zero deletions and every hunk inserts 8 lines at
  line 1, which establishes the same thing from the diff alone.
- **`todos_open` real counts are 0, 4, 5, 6, 7 or 8** per the commit. The
  on-screen frontmatter block in B06 uses 6 as an illustrative value and is
  labelled as one file's frontmatter, not as a universal.

## Claims deliberately NOT made

- **No claim that the 91 recipes are good, or that DRAFT is a bad state.** The
  reel's point is the opposite: DRAFT is the honest label.
- **No claim that the repository got better this week** beyond the specific
  counts shown.
- **No claim about `npm run verify` passing**, since it was not run.

## Repo hygiene

Reads only: `git show`, `git ls-tree`, `git grep`, `git rev-parse`,
`git status`, `git branch -r --contains`, and one read-only run of the committed
checker. Nothing was written to the repository.
