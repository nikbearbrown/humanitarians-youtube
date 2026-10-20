# Week 27 topic draw

- Method: enumerated every `claude-for-<topic>/<topic-name>` path across all 65 local branch/remote-tracking refs of humanitarians-youtube (`git for-each-ref`, `git ls-tree` only; no fetch/checkout/push). Snapshot: origin/main at Sun Oct 11 2026.
- Pool: 22 categories, excluding flat `claude-for-legal--*` and lecture-chapter entries.
- Draw: `random.Random(20261016).choice(pool)` -> **claude-for-cancer**
- Next: pick a topic-name inside it not already used there or the near-duplicate `claude-for-cancer-biology` (the 2,456-line raw list of existing topic pairs, `all-existing-topic-pairs.txt`, stays in the working folder).
- Caveat: refs are as last fetched locally; fetching would refresh them but was avoided per the read-only rule.

## Redraw (user requested a different seed)
- `random.Random(27).choice(pool)` -> **claude-for-video-production** (supersedes the seed 20261016 result, `claude-for-cancer`)
- Used topic names in this category: kept in the working folder

## Subject draw (from the six free subjects in CANDIDATES.md)
- `random.Random(2701).choice([Goodhart's law, regression to the mean, Monty Hall, birthday paradox, Benford's law, p-hacking])` -> **birthday paradox**
- Full sweep: single pass over every unique text blob (md/json/txt/py/srt/vtt/ts/tsx/js/csv/html, 56,521 blobs) reachable from all 65 refs, case-insensitive match on birthday paradox/problem/attack/collision, "shared birthday", "same birthday": **0 hits**. Control (`braess`) returned 41 hits, so the sweep works.
- Filenames across all refs containing "birthday": 0. Our Weeks 18-27 (excluding this folder's own notes): 0.
- Caveat: refs as last fetched locally; nothing was fetched.
