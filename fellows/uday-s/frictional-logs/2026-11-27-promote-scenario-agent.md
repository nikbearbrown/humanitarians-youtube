# Frictional log — promoting the scenario stress testing agent

**Date:** 2026-11-27 · **Branch:** `chore/promote-scenariostresstestingagent`

## What was tried

Run the agent, review its output, get a human sign-off, and change its status from DRAFT
to RUNNABLE-SAMPLE.

## Where the work resisted

- **The sign-off could not be mine.** The rule is that a named human clears a gate. I ran
  and reviewed; the approval went to Uday as a question, and only his answer changed the
  label. Doing the review and the approval in one breath is exactly the self-clearing the
  constitution forbids.
- **Running in place would have damaged committed data.** Last month this agent's scripts
  rewrote their verified artifacts with Windows backslash paths and CRLF. Ran on a `git
  archive` scratch copy instead, which is also what the author did.
- **The no-delete hook blocked `rm -rf` on an empty temp folder.** Correctly — it matches
  the command, not the intent. Used a fresh folder name.
- **"The run changed 9 committed files" looked alarming and meant nothing.** A normaliser
  for CRLF, path separators and timestamps showed 0 real differences. A raw diff on Windows
  would have suggested the pipeline was not reproducible.
- **36/37 looked like a regression.** It is a test comparing paths with `/` on a platform
  that writes `\`. All four files were in the right folder.
- **Three gate tests cannot fail.** `|| true`, `find -exec` swallowing exit codes, and a
  literal `[DATE]`. Proved the `find` one with a deliberately broken file. Checked each
  gate's substance by hand rather than trusting its exit code.
- **A heredoc ate backslashes again** in the comparison script. Moved it to a file.
- **The author's reason for DRAFT was a judgment, not a defect.** Two legacy `[TODO: DEV]`
  lines. Presented with evidence; the signer decided.

## What was done

Frontmatter only: `status` and `last_gate`. Body, scripts and artifacts untouched;
`recipe_version` kept at 0.4.0 so the evidence binds to the version reviewed. RUN_LOG entry
with a ran/saw/expected table, the judgment calls and the known issues. Status and handoff
updated: 94 DRAFT, 3 RUNNABLE-SAMPLE.

## What was learned

**A gate test's exit code is a claim too.** Three of six here pass no matter what. The
review only means something because each gate was checked against what it is *for*.

**On Windows, compare meaning, not bytes.** Two of today's alarms were the platform.
