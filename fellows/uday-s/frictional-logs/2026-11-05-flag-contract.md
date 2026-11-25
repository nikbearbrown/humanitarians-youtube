# Frictional log — the Flags column was load-bearing and nobody had checked it

**Date:** 2026-11-05 · **Branch:** `chore/recipe-lifecycle-frontmatter` · **Commit:** `0358ab9`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Fix the flag contract: `check` reported `documented-not-built` and `built-not-documented`
at 6/6 of measurable recipes, 100% of what it could compare.

## Where the work resisted

- **I had been calling this a documentation defect for two weeks.** It is not. `run` uses
  the Flags column to decide passthrough, so an advertised flag the script lacks reaches
  argparse and fails. I reproduced it before touching anything:
  `run scenariostresstestingagent --step validate-data-shape --sample` →
  `error: argument --sample-dir: expected one argument`. argparse **prefix-matched**
  `--sample` onto `--sample-dir`. The clean crash was luck; with an argument following,
  the flag would have absorbed it and the step would have run on the wrong input.

- **The obvious fix could have made things worse.** Reconciling the table means dropping
  `--sample` from recipes whose scripts lack it, after which `run --sample` stops crashing
  and *silently proceeds*. If those scripts could reach the network, I would have converted
  a loud failure into a sample run that quietly went live — the exact trade this framework
  exists to prevent. Had to establish they cannot before applying: 70 built scripts, zero
  network imports, both external endpoints rendered as handoffs rather than called.

- **There is no template to fix.** `_shared.md` has no Step Commands table; whatever
  generated the 97 recipes is not in the repo. So "fix it once upstream" was not available,
  and fixing all 97 was wrong — for an unbuilt step the column is a specification, and
  nobody knows what the future script will accept.

- **The fix voided an attestation, including one of mine.** market-sentiment's v0.2.0
  attestation states as its own point 5 that any edit to the recipe or its scripts voids
  it. Correcting the recipe triggered exactly that.

- **A shell heredoc ate the script — the fourth time this session.** A stray `cat >` with
  no input blocked on stdin for two minutes. Wrote the generator to a file instead.

- **Testing someone else's script damaged their committed data.** My verification run of
  `scenariostresstestingagent-validate-data-shape.py` rewrote its verified artifacts with
  Windows backslash paths and CRLF. Reverted.

## What was done about it

- Reconciled 24 rows across 6 recipes to the flags each script actually implements, leaving
  unbuilt steps' specifications alone.

- Bumped `recipe_version` on all six. For market-sentiment: set `attestation: null` and
  appended the voiding to the v0.2.0 record rather than re-pointing it, noting that no
  script changed, so every row of its Tested table still describes current behaviour.

- Regenerated the market-sentiment report and run log, because editing the recipe changed
  its SHA-256 and the report cites that hash as the head of the trace chain. Verified both
  links by hand afterwards.

- Re-ran the previously crashing step (exit 0) and the full six-step pipeline on the clean
  corpus (exit 0). The defective corpus still stops at validate-data-shape, which is the
  designed hard stop, not a regression.

**85 defects → 5**, all five in `recipes/gru.md`.

## What was learned

**"Documentation defect" was my own mislabel, and it set the priority wrong.** I ranked this
as tidy-up for two weeks. One command would have shown it was a crash. The cheapest thing
available — running the failure before theorising about it — was the thing I kept skipping.

**Check what a fix removes, not just what it adds.** Reconciling the table deletes a crash.
Deleting a crash is only an improvement if nothing was depending on it to stop. Here it was
safe, but I only know that because I looked; the version of me that "just fixed the docs"
would have had the same diff and no idea whether it was safe.

**An attestation that survives its own edit rule is worthless.** The honest move cost a
version bump and a null field. The dishonest one — quietly re-point it at v0.2.1 — would
have been one line and nobody would ever have noticed. That asymmetry is the whole reason
the rule is written down.
