# SOURCES - Green Because It Wasn't Looking

Single-source reel. Everything comes from the `mycroft` repository at `fbd30b6`
and its companion `fc645e8`, both on `fix/conformance-skip-list`. No web
sources.

| On screen | Beat | Where it came from |
|---|---|---|
| episode 6's Did-not-test entry, quoted | B01 | `logs/attestations/market-sentiment-analysis-part-1-v0.2.0.md` |
| 187 files before | B04, B08 | replayed OLD skip rule from `fc645e8^:scripts/conformance.mjs` |
| 743 files after | B04, B08 | replayed NEW skip rule from `fc645e8:scripts/conformance.mjs` |
| 476 Python revealed | B04, B08 | the difference between the two surfaces |
| 99 recipes | B04, B08 | `git ls-tree -r fbd30b6 -- recipes/` |
| the SKIP / SKIP_PREFIXES split | B05 | `git show fbd30b6:scripts/conformance.mjs`, lines 30-43 |
| 6000 chunk cap, 8191 cmd.exe limit | B06 | same file, lines 129-133 |
| 6.0s / 63s / 3.9s | B06 | commit body of `fc645e8` - author-timed |
| the five break tests | B07 | commit body of `fc645e8` |
| 39 Python, all `scripts/gateway/` | B08 | the OLD surface, listed in full |
| `* text=auto eol=lf`, `*.sh`, `*.bat` | B09 | `git show fbd30b6:.gitattributes`, lines 26, 59, 63-64 |
| 21 extensions declared binary | B09 | counted `*.ext binary` lines in the same file |
| 2120 files, 250 of 250 | B09 | commit body of `fbd30b6` - author-reported |
| +101 / -29 | B09 | `git show --stat fbd30b6` |

## How the surfaces were reproduced

Not by running the checker - by reading both committed versions of
`scripts/conformance.mjs`, lifting their exact constants, and replaying the walk
over `git ls-tree -r fbd30b6`. The full script is quoted in FACTCHECK.md.

Two details decide the numbers, and guessing either one gets it wrong:

- `SKIP` is matched on **directory basenames during the walk**, so `data`,
  `ingest`, `gigo` and `tools` prune every directory of that name at any depth -
  which is how they reached inside `scripts/`.
- The old `DEFAULT_PATHS` did **not** include `data/raw` or `data/verified`.
  `fc645e8` adds them, which is most of the JSON in the new surface.

A first attempt that got either wrong produced 352 files instead of 187. The
figures only matched once the constants were read out of the file rather than
inferred from the commit message.

## Why no second source

A count of files in a tree is not made more true by a second opinion. What *is*
independently sourced is the thing the verdict rests on: the lifecycle of the
claim itself - the commit message says one thing, the tree says another, and the
tree wins. That is P6 of the repository's own constitution: intent lives in the
recipe, truth lives in the run.

## Claims NOT sourced here, and therefore not made

- Nothing about whether the step scripts are *correct* - only that they are now
  compiled.
- Nothing about CI configuration beyond what the commit states.
- No comparison to any other repository or tool.
