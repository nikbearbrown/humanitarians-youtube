# SOURCES - The Lucky Case

Single-source reel plus one standalone reproduction. Everything comes from the
mycroft repository at 0358ab9 on chore/recipe-lifecycle-frontmatter. No web
sources.

| On screen | Beat | Where it came from |
|---|---|---|
| the Flags cell feeding the runner's command | B01 | commit body of 0358ab9 and the committed runner source |
| the failing command and its error | B04 | commit body, verbatim |
| CASE A - the prefix alone, clean crash | B05 | REPRODUCED standalone in a fresh python3 interpreter |
| CASE B - the prefix plus a word, silent absorption | B05 | REPRODUCED standalone, same way |
| six built recipes carrying identical boilerplate | B06 | commit body; the six are the six touched by the diff |
| 24 rows removed, 24 added | B06 | git show --unified=0 0358ab9 -- recipes/ |
| 82 scripts named, 70 on disk, 0 with network imports | B07 | parsed the six recipes, tested each path against git ls-tree, searched each of the 70 |
| 9 network-importing scripts repo-wide, none in the 70 | B07 | same pattern over scripts/, excluding the quarantined tree |
| the attestation voided, version 0.2.1 | B08 | recipe frontmatter at 0358ab9, and the appended "Voided" section |
| 5 defects, all in gru.md, 96 of 97 clean | B09 | node scripts/snickerdoodle.mjs check --all, and check gru |

## The reproduction that matters most

The commit's central warning is that a clean crash was the lucky outcome, and
that a value-taking flag can absorb the next argument instead. That is a claim
about argparse, not about this repository, so it was checked the strongest way
available: a two-argument parser in a fresh interpreter, importing nothing from
the repo.

    CASE A   parse_args(["--sample"])
             -> error: argument --sample-dir: expected one argument

    CASE B   parse_args(["--sample", "data/real.json"])
             -> sample_dir = 'data/real.json'
                input      = None          # no error raised

Case A's text matches the commit character for character. Case B is the
dangerous one and it needed a correction in the making: argparse REFUSES to
consume a token beginning with "-" as a value, so an example using another flag
still crashes. The absorption only happens when the following token looks like
an ordinary value, which is why the reel's example is a path.

## The population check, done the right way round this time

A repo-wide grep for network imports under scripts/ returns 9 files. That is a
true number about the wrong set. The claim concerns the 70 scripts the six built
recipes actually name, and across those the answer is 0. Both are shown in B07.

In episode 10 the same distinction went the other way: a grep over recipes/
returned 98 where the checker said 97. That is why this one was scoped before it
was run rather than after.

## Claims NOT sourced here, and therefore not made

- Nothing about the two external endpoints beyond the 0-of-70 import result.
- Nothing about the pre-change 85 figure beyond attributing it to the commit.
- No comparison to any other repository or runner.
