# Frictional log — repo-wide line endings, and the drift that wasn't drift

**Date:** 2026-10-09 · **Branch:** `fix/conformance-skip-list`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Two tasks that looked independent: clear the manifest drift reporting six generated files
out of sync, and widen the `.gitattributes` line-ending rules from two folders to the
whole repository.

## Where the work resisted

- **The drift was not drift.** Before promoting the rebuilt files, the diff looked wrong:
  22 lines removed and 22 added, showing visually identical text on both sides. A
  byte-level comparison settled it — `AGENTS.md` had 101 CRLF on disk against 79 in the
  build, `CLAUDE.md` 10 against 0, and both were **byte-identical once normalised**.
  `--promote` would have rewritten six files to fix nothing, and the drift would have
  returned on the next checkout.

- **So the two tasks were one root cause**, and in the wrong order. Fixing line endings
  first made the promote unnecessary.

- **The repository was already correct.** Of 300 sampled tracked files, **0** had CRLF in
  the committed blob and **277** had CRLF in the working tree. Nothing needed fixing in
  git; the damage was entirely on checkout, which is why `git add --renormalize` touched
  only 4 files and looked like a no-op.

- **Exempting the quarantined tree made it worse.** Marking `data/mycroft-main/**` as
  `-text` to preserve vendored bytes did the opposite: because those files are already
  stored LF-normalised, `-text` made git adopt the working tree's CRLF and staged ~30
  files as changed. The rule intended to protect them would have rewritten them.

- **`git add --renormalize .` swept in `.gitignore`**, which carries a local-only entry
  that must never be committed.

## What was done about it

- Diagnosed before acting. Compared bytes rather than trusting the diff, which turned a
  six-file rewrite into a one-line policy change.

- Wrote a repo-wide `.gitattributes`: `* text=auto eol=lf` as the default, explicit `text`
  declarations so intent does not depend on content sniffing, explicit `binary` for 21
  extensions, `*.sh` pinned to LF because a CRLF shebang makes the interpreter
  unreachable, and `*.bat`/`*.cmd` pinned to CRLF for the one case that genuinely needs it.

- Dropped the `-text` exemption and recorded why in the file itself, so the next person
  does not re-derive it. Three vendored CSVs normalise along with everything else — the
  smaller and more consistent outcome than thirty files flipping to CRLF.

- Normalised 2120 files on disk, so hashes match **now** rather than after the next clone.
  Verified by sampling 250 tracked text files: **250/250** now hash identically to their
  committed blobs.

- Unstaged `.gitignore` immediately and re-checked it at every commit.

**The drift cleared itself.** `manifest-check` passed with no promote, and `npm run verify`
returned exit 0 — the first clean run in this project.

## What was learned

**A diff that shows identical text on both sides is telling you the difference is invisible,
not that it is absent.** That is the signature of line endings, and it is worth one byte-level
check before accepting the obvious interpretation. The obvious interpretation here was "six
files were hand-edited", which would have been a false accusation and a pointless rewrite.

**Two tasks framed separately were one cause and one fix.** Had they been done in the given
order, the promote would have appeared to work, and the drift would have come back silently
on the next machine — the worst outcome, since it would then look intermittent.

**A protective rule can be the thing that does the damage.** `-text` on the quarantined tree
read as obviously safe and was the single most destructive edit attempted today. The repo's
existing state, not the rule's wording, decided what it actually did.

**Per-recipe scoping was a symptom.** The file had grown two per-recipe blocks, each added
when that recipe hit the hash problem, with a third on the way. Each was locally correct and
collectively a sign the rule belonged one level up.
