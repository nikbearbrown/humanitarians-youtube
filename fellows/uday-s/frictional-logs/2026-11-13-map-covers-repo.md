# Frictional log — the map described a fifth of the repository

**Date:** 2026-11-13 · **Branch:** `main`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Week 1 of the alignment plan: classify every top-level path in `_MANIFEST.md` and
`.ai/manifest.yaml`, and refresh `status.md` and `session-handoff.md`.

## Where the work resisted

- **The branch did not need rebasing.** It had been merged; `origin/main` was 23 commits
  ahead with zero of ours outstanding. I nearly ran a rebase that would have done nothing,
  on a branch that no longer needed to exist. Checking `--left-right --count` first turned
  a rebase into a fast-forward and a branch deletion.

- **My own plan violated the constraint I was given.** I had proposed archiving `_mvtest2`
  and moving `answers*.json`. Both were last touched inside the six-month window and
  neither is mine. The instruction ruled out exactly that, so the work became purely
  additive — which is also strictly better, because every unclassified tree turns out to
  belong to a named contributor.

- **A naive preservation check reported eight lines lost from `status.md`.** They were not
  lost. `subprocess.run(text=True)` decoded git's output as cp1252 while I read the file as
  UTF-8, so every em-dash compared unequal. Decoding git's bytes explicitly as UTF-8 showed
  all 24 original lines present. I would have "fixed" a file that was already correct.

- **The rewrite nearly dropped a real open action.** `session-handoff.md` is a resume
  point, so replacing its contents is correct — but one June item, *run the `eval/` suite
  for real*, was still genuinely open: both runs under `eval/runs/` are named `__example`.
  Listing what the rewrite dropped, rather than assuming staleness, caught it.

- **Inserting into `_MANIFEST.md` could have broken `manifest-check`.** It parses the Tier 1
  set by slicing from the first occurrence of `Tier 1` to the first occurrence of `Tier 2`.
  A new section with either phrase, placed above the existing Tier 2 heading, would have
  silently truncated the set and broken the W3 cross-check against `.ai/manifest.yaml`. The
  inserter asserts both offsets are unchanged and refuses otherwise.

- **Two trees fail conformance, and one failure is ours.** The three Kubernetes manifests
  under `projects/finance-event-signals/deploy/k8s/` are multi-document YAML — entirely
  standard — and `conformance.mjs` calls `yaml.safe_load`, which reads one document.
  The files are valid; our checker is wrong. The other, bare `NaN` in
  `congressional-signals/data/verified/conformance_report.json`, is genuinely invalid JSON
  that Python's `json.dump` emits by default.

## What was done about it

- Classified all 57 top-level entries. Ten contributor subsystems, 1,005 tracked files,
  recorded with `reviewed: false` — listed, not vetted. Keeping those two ideas apart is the
  whole point; collapsing them resolves an open question by writing it down.
- Preserved the 2026-06-15 `status.md` snapshot verbatim beneath the new content and
  verified all 24 lines survived. Carried the eval action forward into the handoff.
- Recorded both conformance failures with their causes and owners, and fixed neither.
- Left `frictional-logs/` out of the committed map on purpose: it is private, and the
  `.gitignore` entry covering it is deliberately local, so naming it in a committed file
  would announce a directory the repository does not know about.

## What was learned

**A map that omits four fifths of the territory still reads as authoritative.** Nothing in
`_MANIFEST.md` said "partial". An agent obeying it would never load `verification-layer/`,
`multi-agents/` or `projects/` and would have no way to discover the omission — the file
looked complete because every row in it was true.

**`reviewed: false` is the useful part of the work, not the caveat.** Writing the paths down
was an hour. Resisting the implication that writing them down had vetted them is what keeps
the record honest, and it is the thing a future reader will rely on.

**Verification code needs verifying too.** My preservation check and the repo's YAML check
failed the same way: both were confidently wrong about correct files. The encoding bug I
caught because the answer looked implausible; the `safe_load` bug had been shipping for
weeks and was only visible because I pointed the checker somewhere it had never run.
