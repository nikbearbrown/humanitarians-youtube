# SOURCES — Unbuilt Is Not Broken

Single-source reel. Everything comes from the `mycroft` repository at `6428457`
on `chore/recipe-lifecycle-frontmatter`, with companions `83793ff` and
`0536907`. No web sources.

| On screen | Beat | Where it came from |
|---|---|---|
| 725 findings | B00, B01, B04 | commit body of `83793ff` — author-reported, the pre-change state cannot be re-run |
| 554 unbuilt steps across 94 recipes | B01, B04 | checker output, run read-only |
| 171 defects after severity | B01, B04 | commit body of `83793ff` |
| 80 defects after frontmatter | B04 | checker output |
| 90 recipes with no defects | B04 | checker output |
| 97 recipes | B04, B08 | checker output |
| 91 recipes with no canonical scripts | B05 | checker footnote: 6 have at least one, "the other 91 have nothing to compare against" |
| the survey that said 42 | B05 | commit body of `6428457` — author-reported |
| the generator's refusal, fired 0 times | B07 | commit body of `6428457` |
| 98 from my grep vs 97 from the checker | B08 | run directly during fact-checking |
| `recipes/vendor-intelligence-brief.yaml` | B08 | `git grep -l '^status:' -- recipes/ \| grep -v '\.md$'` |
| 91 files / 728 insertions / 0 deletions / `@@ -0,0 +1,8 @@` | B06, B09 | `git show --stat` and `git show --unified=0` |
| the todo-marker exclusion | B09 | commit body of `6428457`, and the gate tests in the recipes |

## Why the checker was run, and why `gate` still is not

`check` reads recipe files and script sources, prints a summary, and exits. It
does not execute the scripts it inspects — the previous episodes established
that it parses them instead — and it has no write path. Running it is the
strongest evidence available and it is safe.

`gate` writes a decision record into the repository. It was not run in episode 9
and it was not run here. That restriction cost episode 9 one figure, and it
costs nothing this week.

## The one verification done independently rather than taken on trust

The commit claims "0 bodies altered across 91 files", verified by reconstructing
each original. I did not reconstruct anything. I checked the diff's shape:

```
git show --stat    6428457   →  91 files changed, 728 insertions(+)
git show --unified=0 6428457 | grep -c '^-[^-]'              →  0
git show --unified=0 6428457 | grep '^@@' | grep -cv '^@@ -0,0 +1,'  →  0
```

Zero deleted lines anywhere, and every hunk inserting at line 1. That
establishes a pure prepend from the diff alone, without trusting the commit's
own reconstruction. 728 ÷ 91 = 8 lines per file exactly.

## Three figures that were checked and then left out

`0536907`'s numbers — 531 Python files under `scripts/`, 73 of 157 under
`data/`, and 956 files conforming — could not be reproduced from the committed
tree (raw counts give 652 and 106, and the third needs a build run). They are
recorded in FACTCHECK.md and appear in no frame. That commit is background in
this reel, not evidence.

## Claims NOT sourced here, and therefore not made

- Nothing about whether any of the 91 recipes is worth building.
- Nothing about `npm run verify`, which was not run.
- No comparison to any other repository.
