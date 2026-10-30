# Frictional log — my own conformance change broke the build, three weeks later

**Date:** 2026-10-30 · **Branch:** `fix/conformance-data-python` · **Commit:** `0536907`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Rebase `feat/gate-records` and recommend next steps. The Stop hook blocked instead:
19 files failing conformance, all `SyntaxError: 'return' outside function`.

## Where the work resisted

- **The failures were mine, delayed.** Three weeks ago I added `data/raw` to conformance's
  default surface so gate 3's JSON check would run repo-wide. That also pointed `py_compile`
  at every `.py` under `data/`. Nothing broke at the time because the offending files did
  not exist yet.

- **The files are not broken.** They are n8n Code-node bodies extracted as provenance —
  `# n8n code node: WatchList`, then a bare top-level `return [...]`. That is exactly right
  for a fragment and a SyntaxError for a module. Another contributor added 103 of them on
  a later branch, and my change compiled them.

- **The hook named 19; the real number is 73.** Of 157 `.py` files under `data/`, 73 fail
  for this reason. The hook reports only what the default surface reaches, so the visible
  count understated it by a factor of nearly four.

## What was done about it

- Stopped compiling `.py` under `data/raw` and `data/verified`, on the principle that
  Python there is extracted provenance rather than source. Python source lives in
  `scripts/`, which is still checked in full — 531 files.

- Left JSON, YAML and Markdown under `data/` checked. That is gate 3's machine half and the
  only reason `data/` is on the default surface.

- Checked the fix had not simply made the check quieter: appended a syntax error to a step
  script (still caught, still named) and truncated a run envelope (still caught). Both
  failure paths intact, 956 files conforming.

## What was learned

**A verification change has a blast radius that arrives later.** The surface I widened was
correct for the files that existed then. The defect was latent for three weeks and surfaced
through someone else's unrelated work — which is the worst way to find out, because it
reads as their breakage.

**Pass rate was the wrong question.** 84 of those files compile. It would have been easy to
treat the 73 as bugs to fix rather than a category error in what was being asked. A fragment
that happens to compile is still not a module, and the 84 were passing by accident.

**The hook's count was not the finding.** 19 was what the default surface reached; the real
population was 157 files with 73 failing. Taking the reported number as the scope would have
produced a fix sized to the symptom.
