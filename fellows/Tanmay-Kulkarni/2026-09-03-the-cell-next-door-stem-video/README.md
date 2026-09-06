# The Cell Next Door

Tanmay Kulkarni, in for Humanitarians AI · Week 21 topic video · built 2026-09-03

Text and code only. **The two masters live in the shared Google Drive**, not in this
repository — see the links below. The working folder and the full build record are outside
this repo.

---

## Watch

| Cut | Aspect | Link |
|---|---|---|
| **Long** | 16:9 | <!-- VIDEO_LINK_LONG --> [Watch on Drive](https://drive.google.com/file/d/1FEjhQy7US0soefKWeZLn0OOtfdTPHWhN/view?usp=drive_link) |
| **Short** | 9:16 | <!-- VIDEO_LINK_SHORT --> [Watch on Drive](https://drive.google.com/file/d/17OuisIQ5a6VEnbCj2m6ilNvIqZgTgt2J/view?usp=drive_link) |

## The two cuts

| File | Aspect | Resolution | Runtime | Loudness |
|---|---|---|---|---|
| `2026-09-03-the-cell-next-door.mp4` | 16:9 | 3840 × 2160 | **8:28.9** | −14.8 LUFS / −1.2 dBFS |
| `2026-09-03-the-cell-next-door-short.mp4` | 9:16 | 2160 × 3840 | **2:21.8** | −14.9 LUFS / −1.3 dBFS |

Both are clean masters. Voice is Kokoro `am_onyx` — the same documented departure from this
series' standing `af_bella` used in Week 20, and the same reason: this film is narration over a
measurement rather than a walkthrough of a build.

**The Short is a trailer, not a shortened film.** It gives the finding away completely — a film
whose ethic is *not* withholding a number cannot advertise itself by withholding one. What
stays unanswered is why the mistake keeps happening, and to whom.

## What it teaches

A cancer-immunotherapy video opened on a number: *pembrolizumab produces five-year survival
above fifty percent in metastatic melanoma.* Its own fact-check caught that and wrote a
correction — about forty-three percent.

**The real figure is 38.7%.** The correction quoted the first-line subgroup. Neither party
opened the paper, which is also cited to the wrong journal.

And the same trial reports **38.7 percent** and **38.7 months** a few lines apart, for
different populations — one a proportion, one a length of time.

The film's structure is **concentric**: the same misreading at three scales, each closer to the
narrator. A video's number, then a field's favourite statistic (r = 0.74 quoted as "mutation
count predicts response", leaving 45% unexplained), then a trial's own report of itself. Then
the film's own: our 45% is the cell next door to 40%, and "pancreatic cancer is an excluded
tumour" is the wrong shape of sentence, spoken for eight minutes by me.

The method a viewer walks away with is not the taxonomy. It is two questions — *which link did
this target, and did the next one move?* — derived at B10 from two trials that produce opposite
mechanistic findings and an identical clinical result.

## The evidence is a script, and it runs

```bash
cd experiment
python3 tmb_orr_audit.py
```

Standard library only — no numpy, no install, about two seconds. It audits the published
Yarchoan regression against the letter's own worked examples, computes residuals against
primary-trial ORRs, and runs a seeded Monte Carlo for the attenuation correction.

Every number on screen comes out of it, and the frame that carries a claim names the section
that produced it.

## What it claims, and what it does not

**The 38.7% / 38.7-months collision is real** and corroborated across three independent
reports of the trial. Graded **B⁺, not A**: the *Lancet Oncology* paper is genuinely closed —
publisher 403, no PMCID, Unpaywall `is_oa: false`, no repository copy, and ClinicalTrials.gov
posts only 12-month OS. The dependency on the un-openable grid was removed rather than papered
over, and the 10-year follow-up supplied a grade-A anchor in its place (34.0% vs 23.6%).

**Two findings cut against the film and are said out loud in it.** The TMB-independent share is
~40%, not the tidier 45% — small-trial attenuation accounts for the difference, and it makes the
argument weaker. And hot/cold/excluded describes a tumour *sample*, not a tumour type, which
invalidates a sentence the narration had been repeating.

**A claim was withdrawn during the build and is listed rather than deleted.** `C1a` — that
"above 50%" is specifically the 24-month figure — was single-sourced. It is a plausible account
of where the error came from, and plausible is not the standard here.

**Three claims are marked CUT and never spoken**, including a "9-month historical median" that
has no citation anywhere in the source material.

## Where this topic came from

Drawn by the randomiser, not chosen. `claude-for-cancer/hot-cold-excluded-tumors` — confirmed
open against Week 20's pool of 905, from 2,170 topic folders.

### The source project

Three persona variants of one project, and **none was ever differentiated**: `claude-liam` is
12-of-12 narration-identical to the base (its metadata still carries an unexecuted
`_variant_todo` to rewrite every line), and `nbb` shares all 11 body beats. One script in three
coats of paint.

The base variant's `FACTCHECK.md` is real work — 11 claims with named primary sources. **It
caught the video's opening overstatement and was then ignored.** That is the film.

Its own `[UNVERIFIED]` note recorded ~43% for the pembrolizumab arm and flagged "above 50%" as
subgroup-conditional. The narration shipped "above 50%" anyway, and B04 re-asserted it as
*confirmed*. The gate ran, wrote the finding down, and nothing downstream consumed it.

## What was inherited, and what was checked

Nothing was inherited. Every claim was re-verified against primary literature — and the
inherited correction turned out to be wrong too, in the same direction, with the journal
misattributed.

The audit of the source is measured rather than asserted: 6 of 10 body beats are bare slates,
4 of them carrying quantitative claims with no artifact; the reel's duration estimates run
1.44× short against its own measured audio; and 89% of its verdict beat is two earlier beats
pasted verbatim.

## Files here

**The six core files**, the same set every episode in this series carries:

| | |
|---|---|
| `README.md` | this file |
| `PEDAGOGY.md` | Gate P, signed before any audio was generated |
| `FACTCHECK.md` | 24 claims, each naming the beat that consumes it — three cut, two retired |
| `QC-REPORT.md` | deliverable specs, loudness, resolution, gates — all measured |
| `beat_sheet.json` | the source of truth for the long cut |
| `beat_sheet-short.json` | the source of truth for the Short |

**Plus the experiment**, because this film's evidence is a program:

| | |
|---|---|
| `experiment/tmb_orr_audit.py` | stdlib only — **every number in the film comes out of this** |
| `experiment/RESULTS.txt` | its saved output |

Not included here: the build scripts, the Manim scenes, the motion work, the read-aloud sheet
and the intermediate reviews. Those live in the working folder — this folder is the deliverable
and its evidence, not the workshop.

Captions (`.srt`/`.vtt`) and the YouTube description are produced at build time and kept with
the masters in the shared Drive, per this collection's convention.
