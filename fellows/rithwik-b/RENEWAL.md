# Renewal request — Rithwik B.

- **Current agreement:** 1 Aug — 31 Oct 2026
- **Requested period:** 1 Nov 2026 — 31 Jan 2027

- **Project:** AI Fluency × Brutalist — explainer series, and the Medhavy bio-art figure audit
- **Role:** AI Software Engineer
- **Reporting folder:** [fellows/rithwik-b](./README.md)
- **GitHub:** [@rithwikbanala](https://github.com/rithwikbanala)

## What the current period produced

Seven reels — a session replay on the Medhavy bio-art library and a six-film series on
AI fluency, built with the Brutalist toolkit — and the audit the first reel reports.

**Thirteen weeks, 268 hours** across the agreement period; the per-week basis is in
[HOURS.md](HOURS.md). Each series film had two weeks of research and scripting before it
was built.

The through-line is not the videos. It is that **an automatic check passing is not the
output being right**, found twice from opposite ends:

- **AI figures that ignore their prompts.** Of the 49 molecule/drug figures in bio-art, 31
  (63%) are one of five generic templates, and none of the 245 figures draws a real
  chemical structure. Established by grading every figure against its own prompt and
  grepping every annotation.
- **A viewer that crashed before rendering a pixel.** 234 of 245 catalog entries lack the
  `file` field the loader read. Fixed by normalizing both entry shapes.
- **Video gates that passed visible defects.** Across the series, frame review caught 7 of
  11 defects — clipped labels, a comma that split a correction, placeholder images — and
  the toolkit's gates caught 4. Every one is in a 12-entry
  [build log](2026-10-30-show-what-broke/SERIES-BUILD-LOG.md).
- **A claim of my own that did not survive re-checking.** The bio-art reel says 16 figures
  are "pixel-identical". Re-checked for this report: no two files are identical; they are
  visually near-identical. That beat gets re-cut before publication.

### Evidence

| Date | Reel | Runtime | Finding | Log |
|---|---|---:|---|---|
| 21 Sep | [A Blank Page and 49 AI Figures](2026-09-21-a-blank-page-and-49-ai-figures/) | 3:05 | 31 of 49 figures on five templates; 0 chemical structures; 5/7 claims pass, 2 partial | [log](2026-09-21-a-blank-page-and-49-ai-figures/FRICTIONAL.md) |
| 29 Oct | [Fluent Isn't Finished](2026-10-29-fluent-isnt-finished/) | 2:52 | 8 MAJOR → 0 across four compiles; one defect the gate passed | [log](2026-10-29-fluent-isnt-finished/FRICTIONAL.md) |
| 29 Oct | [The Beat Sheet Is the Prompt](2026-10-29-the-beat-sheet-is-the-prompt/) | 2:50 | A comma split the on-screen correction; the gate passed it | [log](2026-10-29-the-beat-sheet-is-the-prompt/FRICTIONAL.md) |
| 29 Oct | [Look at the Frames](2026-10-29-look-at-the-frames/) | 2:48 | Clipped tab labels found on the contact sheet | [log](2026-10-29-look-at-the-frames/FRICTIONAL.md) |
| 29 Oct | [Trust, Then Verify](2026-10-29-trust-then-verify/) | 2:47 | Fact-checks drafted so the gate cannot pass without a human | [log](2026-10-29-trust-then-verify/FRICTIONAL.md) |
| 30 Oct | [Show What Broke](2026-10-30-show-what-broke/) | 2:48 | 11 failures: toolkit caught 4, frame review caught 7 | [log](2026-10-30-show-what-broke/FRICTIONAL.md) |
| 30 Oct | [The Workflow Is the Lesson](2026-10-30-the-workflow-is-the-lesson/) | 2:55 | Rounds of fixes per film fell 4 → 3 → 2 → 2 once the generator held the lessons | [log](2026-10-30-the-workflow-is-the-lesson/FRICTIONAL.md) |

Each folder holds the beat sheet, measured timings, fact-check, sources, QC report and
contact sheets, a rebuild prompt, a YouTube description with validated chapters, and a
Frictional log.

## Stated plainly: nothing is published yet

All seven reels are built. **None is published**, and none of the six series films is a
final master:

- **The six series fact-checks are drafted, not signed.** The final master compiles only
  after I check each one and rename it `FACTCHECK.md`. That is the gate film 4 is about,
  so the series cannot honestly skip it.
- **The bio-art reel needs one beat re-cut** — "pixel-identical" is too strong — and a
  re-voice to match the series.
- **Frame review so far was on stills.** I watch and listen to every cut end to end
  before signing.

## Attribution, stated

- **Mine:** the topic and its framing — AI fluency as the skill, Brutalist as the receipt —
  the film order and outcomes, the figure-audit rubric and verdicts, and what goes on
  camera.
- **Claude:** wrote the beat sheets and the generator scripts from my framing, ran the
  toolkit and its gates, read the frames, kept the build log, and drafted every fact-check
  and Frictional log. Where its output was wrong I changed or rejected it; each reel's
  Frictional log records what was accepted, changed and rejected.
- **Held out:** my original framing credited AI fluency to "Stanford HAI" and to
  "Botspeak". Neither is on camera until I have a source.
- **Honest limit:** the build log says "a person caught 7". In this build that review was
  Claude reading still frames. Film 5 will say "frame review" before its final master.

## Plan for the requested period

Same rhythm as the first period: one sprint a week and one film every two weeks, about
20 hours a week.

| Week | Dates | Work | Film | Hrs |
|---|---|---|---|---:|
| 14 | 2–6 Nov | Watch all seven cuts end to end; sign the six series fact-checks | Film 7 — Why Generators Recycle: research and outline | 20 |
| 15 | 9–13 Nov | Six final masters with `./art final`; renders to Drive; commit the viewer fix to Medhavy/bio-art | Film 7: beat sheet and narration | 20 |
| 16 | 16–20 Nov | Re-cut the bio-art reel's B06; re-voice to `af_bella`; audit protein and receptor figures | Film 8 — Prompt vs Image: research and outline | 20 |
| 17 | 23–27 Nov | Audit cell and structure figures (Thanksgiving week) | Film 8: beat sheet and narration | 12 |
| 18 | 30 Nov – 4 Dec | Duplicate detector — perceptual hash across the full library | Film 9 — Near-Identical Isn't Identical: research and outline | 20 |
| 19 | 7–11 Dec | Check the detector against the hand audit of the 49 molecule/drug figures | Film 9: beat sheet and narration | 20 |
| 20 | 14–18 Dec | RDKit / PubChem structures for the named drugs in `object-inventory.json` | Film 10 — Drawing a Real Molecule: research and outline | 20 |
| 21 | 21–25 Dec | Structures for named molecules (winter break) | Film 10: beat sheet and narration | 10 |
| 22 | 28 Dec – 1 Jan | Swap structures into the viewer (winter break) | Films 7–10: frame QC, end-to-end watch | 10 |
| 23 | 4–8 Jan | Hand-score frames across the series, defect by defect | Film 11 — When the Gate Misses: research and outline | 20 |
| 24 | 11–15 Jan | Compare hand scores with GATE V — one catch-rate figure | Film 11: beat sheet and narration | 20 |
| 25 | 18–22 Jan | Document both checks for Medhavy | Film 12 — What We Measured: research and outline | 20 |
| 26 | 25–29 Jan | End-of-period report | Film 12: beat sheet, narration, QC | 20 |
| | | | **Total** | **232** |

### Across the period

1. **Fact-check before recording, not after.** The one claim that failed — "pixel-identical"
   — was a word I never tested. Every number on camera gets its check first.
2. **Watch, don't only sample.** Stills catch layout; only a full watch catches audio and
   timing.
3. **Write the Frictional log during the build**, not after it.
4. **Publish once signed.** A reel that sits unpublished is evidence only to someone
   reading this folder.

## Open items I am carrying

- Six series fact-checks unsigned → no final masters.
- Bio-art reel: B06 "pixel-identical" and B01 "four bugs" need re-cuts.
- Viewer fix uncommitted in the local bio-art clone.
- Seven reels unpublished.
