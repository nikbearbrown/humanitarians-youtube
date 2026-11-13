# Frictional Log — same-logic-two-languages (Week 25 work video)

**Record provenance:** drafted 2026-10-04 with Claude from this folder's own records (`ANGLE.md`, `FACTCHECK.md`,
`PEDAGOGY.md`, `PROOF-REVIEW.md`), after the work was done rather than while it happened. Reviewed by Tanmay. Every entry points at the record it comes from. The recipe work
itself (what was contributed, keeping others' work safe, the gate decisions) is recorded in the Mycroft repository:
[the recipe page](https://github.com/nikbearbrown/mycroft/blob/main/recipes/contradiction-detection-agent.md) and its gate-decision records.

## 2026-10-04 — Porting the detector, and what my own testing caught

- **What I tried:** port the detector's two JavaScript nodes to Python and check the port against the original by
  running both side by side.
- **Where it resisted:** the comparison agreed 16/16, but when my port was changed on purpose (a threshold from 0.6 to
  0.61, Python's own rounding), it still agreed. None of my test companies stood on the line. Separately, step 4
  left half-built files behind when it stopped.
- **What I did next:** added two companies placed exactly on the line (FXR at confidence 0.6, FXQ at a news average of
  0.625); each change now fails on its own company. Step 4 now writes nothing when it stops, and a break test checks it.
- **Why it's in the film:** these are my own gaps, found by my own checking. They're the film's middle (B07, B08).
- **Evidence:** [FACTCHECK.md](FACTCHECK.md) (C8, C9), [the recorded self-test](https://github.com/nikbearbrown/mycroft/blob/main/logs/contradiction-detection-agent/self-test-results.md) (section B).

## 2026-10-04 — An angle that criticised someone else's work

- **Where it resisted:** the first proposed angle was built around critiquing the original workflow, and it named the
  repository owner as the workflow's author from git history. My response: *"it was not nik's work we don't know
  that and second thing we do not get the right to critise someone's work"*, and the film shouldn't sound
  overconfident.
- **What I did next:** rejected the angle, and asked for the pushed branch's wording to be reworked too. The list of
  issues became neutral *Notes from porting*, and the gate notes and report caveats were reworded. The rework replaced
  the branch's single commit with a force-push. I allowed it only with extreme care, because force-pushes have harmed
  fellows' work before: it was pinned to the old commit, a backup was kept, and GitHub was checked before and after.
  Nothing was removed, and every branch survived.
- **AI and other contributions:** Claude proposed the first angle, then did the rework. I set the rule: no critique,
  no attribution without proof, a humble tone.
- **Evidence:** [ANGLE.md](ANGLE.md), [the recipe's *Notes from porting*](https://github.com/nikbearbrown/mycroft/blob/main/recipes/contradiction-detection-agent.md).

## 2026-10-04 — The film: checking my own version

- **What I tried:** angle B, "checking my own version", titled *Same Logic, Two Languages*, with my report-vs-log
  mismatch kept as the third match (B09).
- **Where it resisted:**
  - Kokoro said "Mycroft" as MICK-roft and the past-tense "read" as "reed".
  - The structure ("pairs") was never said out loud.
  - The first stills were half empty, then overflowed when the type grew.
  - A scratch-run label sat under the wrong column.
- **What I did next:**
  - Respelled "My-croft" for the voice (captions keep "Mycroft") and reworded around "read".
  - Introduced "three matches" in the narration.
  - Re-laid out every beat and checked every still in both formats before any render.
  - At my request, removed the line saying the work was "on my fork, waiting for review" (re-recorded B11), and
    changed every source line to name the recipe instead of the branch.
- **Evidence:** [PROOF-REVIEW.md](PROOF-REVIEW.md), [PEDAGOGY.md](PEDAGOGY.md).

## 2026-10-04 — The Short

- **Where it resisted:** the first Short (1:10) was too hurried. In my words: *"ensure that it gives enough context
  and is not made in hurry"*.
- **What I did next:** rewrote it at 2:20, inside YouTube's 3-minute limit. It now gives the context on its own:
  what Mycroft and the detector are, the invented companies, answers written first, my own changes going unnoticed,
  the fix, and the limits. Checking every cut showed the picture resetting between beats (S07 → S08) and empty
  tables in S02 and S05. State now carries across every cut.
- **Evidence:** [SCRIPT-SHORT.md](SCRIPT-SHORT.md), [PROOF-REVIEW.md](PROOF-REVIEW.md).

## 2026-10-04 — Finishing

- **Where it resisted:** loudness stopped at −15.0 LUFS (where this week's topic video shipped). The final review
  found the captions drifting from the voice by up to a second, with four cues under 1.2 s.
- **What I did next:** a final gain trim under a −2.6 dBFS ceiling reached −14.1 / −14.2 LUFS. The captions were
  rebuilt on the word clock the films are built on.
- **Result:** both films clear to publish, teaching 12/12 on both, GATE V clean, 0 dark frames.
- **Still open:** live mode and attestation for the recipe (people with live access), and the PR to Mycroft's `main`
  (on my word).
- **Evidence:** [PROOF-REVIEW.md](PROOF-REVIEW.md) (final).
