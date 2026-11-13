# FACTCHECK — Every Row Was True

Status: **GATE F SIGNED — 2026-11-13. 13 rows PASS, 1 figure NOT REPRODUCED and
therefore NOT SHOWN.**

Subject: `mycroft` @ `b425b19` on `chore/map-covers-repo`.
`git branch -r --contains HEAD` lists `origin/chore/map-covers-repo` and
`git status -sb` reports the branch in sync, so this is the last pushed commit.

## Method

Three read-only routes:

1. **Counted the committed tree** — `git ls-tree -r b425b19 -- <path>/` for each
   of the ten subsystems, and `git ls-tree b425b19` for the top level.
2. **Ran the committed checker** — `node scripts/snickerdoodle.mjs check --all`.
   `check` reads and prints. (`gate` writes a record and has not been run since
   episode 9.)
3. **Reproduced the JSON failure** — ran `JSON.parse` over the committed file in
   a standalone Node process.

## Verified claims

| # | Beat | Claim | Verdict | How checked |
|---|---|---|---|---|
| 1 | B04 | `projects/` 435 tracked files | PASS | `git ls-tree -r` |
| 2 | B04 | `case-study-workflows/` 277 | PASS | same |
| 3 | B04 | `verification-layer/` 154 | PASS | same |
| 4 | B04 | `multi-agents/` 41 | PASS | same |
| 5 | B04 | the remaining six: 39, 17, 14, 12, 10, 6 | PASS | same, each one |
| 6 | B04, B08 | the ten sum to **1,005** | PASS | summed the ten counts — 1005 exactly |
| 7 | B06 | the three k8s manifests are multi-document YAML | PASS | `infra.yaml` 7, `observability.yaml` 8, `pipeline.yaml` 10 `---` separators |
| 8 | B06 | the congressional report contains bare `NaN` literals | PASS | **1,052** occurrences of the bare token |
| 9 | B06 | `JSON.parse` rejects that file | PASS — reproduced | standalone Node: `Unexpected token 'N'` at `"ticker": NaN` |
| 10 | B08, B09 | 97 recipes: **95 DRAFT, 2 RUNNABLE-SAMPLE** | PASS | read the `status:` line from each of the 97 recipe `.md` files, excluding `README.md` and `_shared.md` |
| 11 | B08, B09 | `check --all` = 5 defects, all in `recipes/gru.md` | PASS | ran it; 97 recipes, 5 defects, 96 clean |
| 12 | B09 | `status.md` reported 99 recipes and still listed the lifecycle as open | PASS | the commit's diff to `status.md` |
| 13 | B09 | `npm run verify` passes, 993 files conform | PASS (author-reported) | stated in the commit body; `verify` is a build step and was not run |

## The figure that did NOT reproduce, and is absent from every frame

The commit says the old `_MANIFEST.md` **"classified 12 top-level paths out of
51."**

Counting the top level of the committed tree:

```
git ls-tree b425b19            →  56 entries  (31 trees + 25 blobs)
  excluding dot-entries        →  48
  dot-entries                  →   8
```

**Neither 56 nor 48 is 51.** I could not determine what population the commit's
51 counts — it may exclude certain files, or count something the manifest's own
classification scheme recognises. Rather than guess, the ratio appears in **no
frame**. B08 shows both of my numbers against the claimed one and says so.

The *substance* of the claim — that ten subsystems totalling 1,005 files were
absent from the map — reproduces exactly and is what the reel uses.

## Figures attributed to the commit, not independently reproduced

- **"993 files conform"** and **"manifest check clean"** require running
  `npm run verify`, which is a build step rather than a read. B09 carries it
  with the citation strip naming the commit.
- **"eight scoped CLAUDE.md files"** below the root — stated in the manifest and
  not separately enumerated here.
- **"all 24 of its lines verified present"** for the preserved June snapshot —
  the commit's own verification of its own edit.

## Precision notes

- **"1,005" is tracked files, not files on disk.** Everything counted came from
  `git ls-tree`, so untracked material is excluded by construction.
- **B06 calls one failure ours and one theirs**, which is the commit's own
  diagnosis: `yaml.safe_load` reads a single document and the k8s files are
  valid multi-document YAML, so the checker is wrong; the `NaN` literals are a
  real defect in a producing script.
- **The 1,052 NaN count is mine**, not the commit's — the commit says only
  "bare NaN literals". It is used on screen as evidence the failure is real and
  not a one-off typo.
- **`reviewed: false` is a recorded field, not an inference.** B07 quotes it.

## Claims deliberately NOT made

- **No claim that the ten subsystems contain defects.** Two failures were found
  when the checker was pointed at them; the rest conformed, and `reviewed:
  false` means nobody has judged the work.
- **No claim that any contributor did anything wrong.** The gap is in the map.
- **No claim that `npm run verify` now covers the ten.** It does not; the commit
  records the gap rather than closing it.

## Repo hygiene

Reads only: `git ls-tree`, `git show`, `git grep`, `git rev-parse`,
`git status`, `git branch -r --contains`, one read-only run of the committed
checker, and one standalone `JSON.parse`. No command that writes a record was
executed. Nothing was written to the repository.
