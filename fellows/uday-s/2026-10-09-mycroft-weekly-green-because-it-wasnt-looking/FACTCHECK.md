# FACTCHECK - Green Because It Wasn't Looking

Status: **GATE F SIGNED - 2026-10-09. 13 rows PASS, 1 row FAILS AND IS SHOWN FAILING.**

Subject: `mycroft` @ `fbd30b6` on `fix/conformance-skip-list`, with its companion
`fc645e8`. `git branch -r --contains fbd30b6` lists
`origin/fix/conformance-skip-list` and `git status -sb` reports the branch in
sync, so this is the last pushed commit.

## Read from the COMMITTED tree, never the working tree

`git status --porcelain` reports **2117 modified files** in this checkout - the
line-ending renormalisation showing as unstaged. Every figure below came from
`git show <sha>:<path>` and `git ls-tree -r <sha>`, so the working-tree state
cannot have influenced any of them. Nothing was written to the repository.

## The recount

The commit message claims five figures. Rather than trust them, both versions of
the skip rule were re-implemented from the committed `scripts/conformance.mjs`
and replayed against `git ls-tree -r fbd30b6`:

```python
OLD_SKIP = {'.git','node_modules','.build','output','images','d3','data','MD',
            'PSD','epub','front-back','wayback-machine',
            'mycroft-main','ingest','gigo','tools'}          # fc645e8^
OLD_DIRS = ['prompts','brand','recipes','scripts']

NEW_SKIP     = {'.git','node_modules','.build','__pycache__','output','images',
                'd3','MD','PSD','epub','front-back','wayback-machine'}
NEW_PREFIXES = ['data/mycroft-main','scripts/mycroft-main',
                'docs/mycroft-main','data/private']           # fc645e8
NEW_DIRS     = ['prompts','brand','recipes','scripts','data/raw','data/verified']
```

Result:

```
OLD: 187 files {'md':127,'yaml':2,'json':9,'js':10,'py':39}
NEW: 743 files {'md':133,'json':82,'yaml':3,'js':10,'py':515}
py revealed: 476          (515 - 39)
```

| # | Beat | Claim in the commit message | Verdict | Recounted |
|---|---|---|---|---|
| 1 | B04 | the old run checked 187 files | PASS | 187, exactly |
| 2 | B04 | the new run checks 743 files | PASS | 743, exactly |
| 3 | B04 | 476 Python files were hidden | PASS | 515 - 39 = 476, exactly |
| 4 | B04 | the executable surface of 99 recipes | PASS | 99 `.md` files under `recipes/` |
| 5 | B08 | **"checked 187 files and zero Python"** | **FAIL** | **39 Python files, not zero** |

### The one that fails, and why it is on screen

The old surface contained **39 `.py` files, every one of them under
`scripts/gateway/`** - a single subsystem, and 17 of the 39 are that subsystem's
own `tests/` directory. Not one recipe step script was among them.

So the claim that carries the argument - that no pipeline code was ever compiled
- holds exactly. The headline number does not. B08 shows four ticks and one
cross, and says out loud that the wrong figure is in the author's own commit
message. The series' rule since episode 6 is to recount rather than trust the
message; this is the first week the recount caught something.

## Figures from the companion commit

| # | Beat | Claim | Verdict | How checked |
|---|---|---|---|---|
| 6 | B06 | cmd.exe caps a command line at 8191 characters | PASS | stated in the code comment at `scripts/conformance.mjs:129` |
| 7 | B06 | chunks are capped at 6000 characters | PASS | `const ARG_BUDGET = 6000` at line 133 |
| 8 | B06 | 187 files in 6.0s to 743 files in 3.9s | PASS (author-timed) | the file counts reproduce; the timings are the author's measurements and are not independently reproducible here |
| 9 | B06 | unbatched removal would have been ~11x slower (6s to 63s) | PASS (author-timed) | same - a measurement, not a count |
| 10 | B09 | 21 extensions declared binary | PASS | counted the `*.ext binary` lines in `git show fbd30b6:.gitattributes` - 21 |
| 11 | B09 | `*.sh` pinned LF, `*.bat`/`*.cmd` pinned CRLF | PASS | lines 59, 63, 64 |
| 12 | B09 | `* text=auto eol=lf` repo-wide | PASS | line 26 |
| 13 | B09 | .gitattributes changed +101 / -29 | PASS | `git show --stat fbd30b6` |
| 14 | B09 | 2120 files normalised; 250 of 250 sampled hash identically | PASS (author-reported) | stated in the commit body; the sampling run is not reproducible from the repo alone |

## Claims marked as author-reported, not recounted

Rows 8, 9 and 14 are **measurements**, not counts: wall-clock timings and a
sampling run. They cannot be reproduced from the committed tree, so they are
attributed on screen and in narration to the commit rather than presented as
independent verification. The same applies to the commit's statement that **two
market-sentiment pull requests passed CI** without CI compiling their scripts -
that is a claim about PR history, it is spoken in narration as the commit's
account, and no figure for it appears on screen.

## Precision notes

- **"476 Python files" is a difference, not a directory count.** A raw count of
  `.py` under `ingest|gigo|tools|data` gives 483; that is not the same quantity
  and is not used. 476 is what the new rule reveals that the old rule hid.
- **`ingest`, `gigo` and `tools` were never top-level scan roots.** They were
  basename matches biting *inside* `scripts/`, which is the whole point of B05.
- **The timings are single-machine.** No claim is made that they generalise.

## Claims deliberately NOT made

- **No claim that the repository is now well tested.** The checker compiles and
  parses; it does not run a test suite, and the reel does not imply one exists.
- **No claim that the market-sentiment recipe is correct.** Episode 6's verdict
  stands untouched.
- **No security claim.** A skipped path is a coverage gap here, not a
  vulnerability, and the reel does not dress it as one.

## Repo hygiene

Read-only throughout: `git show`, `git ls-tree`, `git rev-parse`,
`git branch -r --contains`. No writes, no checkouts, no renormalisation.
