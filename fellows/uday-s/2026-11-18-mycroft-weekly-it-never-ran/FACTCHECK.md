# FACTCHECK — It Never Ran

Episode 13. Subject: `D:\Projects\mycroft` @ **`08b92d3`**, branch
**`fix/conformance-multidoc-yaml`**, pushed and in sync with origin.

**The mycroft tree was treated read-only throughout.** `snickerdoodle gate` was
not run (it writes a decision record). `conformance.mjs` was not run (it
compiles Python and would leave `__pycache__` behind). Every mechanism below was
reproduced in a *standalone* interpreter, outside the repository, from source
read with `git show`.

---

## Verified, and on screen

| Claim | Beat | How it was checked | Result |
|---|---|---|---|
| Branch is `fix/conformance-multidoc-yaml`, HEAD `08b92d3`, pushed | meta | `git rev-parse`, `git branch -r --contains` | ✓ in sync |
| Exactly **4 lines removed** from `scripts/conformance.mjs` | B07, B08 | counted on `git show 08b92d3 -- scripts/conformance.mjs` | ✓ 4 |
| All four dated **2026-10-09**, one author | B06, B07, B08 | `git blame 08b92d3^ -- scripts/conformance.mjs` on each removed line | ✓ 3 of 4 blame directly; the 4th is in the same contiguous hunk, same commit |
| 2026-10-09 is the commit this series covered as "making the check fast" | B06 | episode 7's subject commit, same repo | ✓ |
| `yaml.safe_load` on a two-document file raises `ComposerError: expected a single document in the stream` | B05 | standalone `python -c`, two-doc fixture written to the scratchpad | ✓ reproduced verbatim |
| The shipped runner mangles newlines into the two characters `\` `n` | B04, B05 | reconstructed the `.replace(/\n/g, '\\n')` transform; fed the result to `python -c` | ✓ `SyntaxError: unexpected character after line continuation character` |
| `safe_load_all` without `list()` parses **nothing** and raises nothing | B05 | standalone `python -c` on a deliberately invalid YAML file | ✓ exit 0, no output, no exception |
| The fix wraps it: `list(yaml.safe_load_all(...))` | B05 | `git show 08b92d3:scripts/conformance.mjs`, line 209 | ✓ present, with a comment saying why |
| `execFileSync` imported on a **new** line, not merged into a shared import | B07 | diff of the import block | ✓ |
| The per-file fallback still calls the single-document loader, and was not touched | B07 | diff + `git blame` on the fallback (another contributor, August) | ✓ unchanged |
| **8** contributor subsystems added to `DEFAULT_PATHS` | B09 | diff of the `DEFAULT_PATHS` array | ✓ 8: verification-layer, projects, case-study-workflows, case-studies, multi-agents, provenance-gatekeeper, github-assistant, my_chapters |
| `env`, `.venv`, `venv` added to `SKIP` | B09 | diff of the `SKIP` set | ✓ 3 |
| `congressional-signals/` and `archive/` left out, with reasons in the commit | B09 | commit message body | ✓ both named, both with a stated reason |
| `congressional-signals/` holds the bare `NaN` found in episode 12 | B09 | the same file identified last episode | ✓ same file |
| The commit records "not tested on the Python version CI uses" | B09 | commit message, final line | ✓ |

---

## NOT reproduced — attributed on screen, never claimed as mine

The commit states the checked surface went from **1,039 → 1,853** files.

Replaying the committed `DEFAULT_PATHS` / `SKIP` / `SKIP_PREFIXES` rules over the
tree with `git ls-tree -r` gives:

| | commit | my replay | difference |
|---|---|---|---|
| before | 1,039 | 1,142 | +103 |
| after | 1,853 | 1,955 | +102 |
| **increase** | **814** | **813** | **1** |

The offset is near-constant at both ends and the *increase* agrees to within one
file. The most likely cause is that the real walker reads the filesystem (and so
sees untracked and ignored files that match the rules) while I walked git. I did
not run the walker, because running it writes `__pycache__` into a repository
this series treats as read-only.

**B08 shows both pairs of numbers side by side and says which is which.** The
totals are presented as the commit's. The increase is presented as mine.

`projects/` alone: commit 372, my replay 371 — recorded here, not shown.

---

## Cross-episode continuity, checked

Episode 12 (`b425b19`) ended on three valid Kubernetes manifests failing the
conformance check, and on the claim that the defect was in the checker rather
than the files. That is the premise B01 opens on, and it is accurate: the same
three files, the same checker, the same branch lineage.

---

## Deliberately absent

- No figure for how many YAML files exist repo-wide — not independently counted.
- No runtime or speed figure for the batch path — the batch has never executed,
  so there is nothing to measure.
- No claim that any *result* was wrong during the five weeks. The fallback is
  correct for single-document files; the reel says exactly that and no more.
