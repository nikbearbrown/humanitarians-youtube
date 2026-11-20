# SOURCES — Every Row Was True

Single-source reel. Everything comes from the `mycroft` repository at `b425b19`
on `chore/map-covers-repo`. No web sources.

| On screen | Beat | Where it came from |
|---|---|---|
| "every row accurate" / "the map was partial" | B01 | commit body of `b425b19` |
| the ten subsystems and their counts | B04 | `git ls-tree -r b425b19 -- <path>/`, each one |
| 1,005 total | B04, B08 | the sum of those ten counts |
| none of the ten inside `DEFAULT_PATHS` | B05 | commit body, and `scripts/conformance.mjs` |
| eight scoped `CLAUDE.md` files below the root | B05 | `_MANIFEST.md` as committed |
| three k8s manifests are multi-document YAML | B06 | counted `---` separators: 7, 8, 10 |
| `yaml.safe_load` vs `safe_load_all` | B06 | `_MANIFEST.md`, and `scripts/conformance.mjs` |
| bare `NaN` and the `JSON.parse` rejection | B06 | the committed file, and a standalone `JSON.parse` |
| 97 recipes — 95 DRAFT, 2 RUNNABLE-SAMPLE | B08, B09 | read the `status:` line from all 97 recipe `.md` files |
| 5 defects, all in `gru.md` | B08, B09 | `node scripts/snickerdoodle.mjs check --all` |
| status.md claimed 99 recipes, lifecycle open | B09 | the commit's diff to `status.md` |
| 993 files conform | B09 | commit body — `npm run verify` is a build step and was not run |

## The two counts done the careful way

**The recipe split.** A naive `git grep '^status:' -- recipes/` over-counts: it
matches a `.yaml` file that is not a recipe (the error episode 10 was about) and
a line carrying a trailing comment. Restricting to the 97 recipe `.md` files,
excluding `README.md` and `_shared.md`, and taking the first `status:` line from
each gives exactly **95 DRAFT and 2 RUNNABLE-SAMPLE**.

**The subsystem totals.** Each of the ten was counted separately with
`git ls-tree -r` rather than inferred from a single glob, and the ten were then
summed. The sum is 1,005, matching the commit.

## The figure that is in no frame

The commit says the old map "classified 12 top-level paths out of 51". The top
level of the committed tree holds **56** entries — 31 directories and 25 files —
or **48** excluding the eight dot-entries. Neither is 51, and I could not
establish what population 51 counts. It appears nowhere in the video; B08 shows
both of my numbers beside the claimed one.

This is the fourth week running that a figure in a commit message did not
reproduce. In each case the substance held and the specific number did not,
which is the argument for recounting rather than quoting.

## Claims NOT sourced here, and therefore not made

- Nothing about the quality of any contributor subsystem — `reviewed: false`
  means nobody has judged them, including me.
- Nothing about `npm run verify` beyond attributing its result to the commit.
- No comparison to any other repository.
