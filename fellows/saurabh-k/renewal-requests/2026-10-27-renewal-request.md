# Fellowship renewal request — Saurabh K. — Brutalist (complete) to Iacon Optimus Program

**Submitted:** 2026-10-27
**Requested duration:** 2026-11-01 through 2027-01-31
**Current agreement ends:** `[TODO — fellow to confirm]`
**Reporting period covered:** 2026-10-05 through 2026-10-26
**Role:** AI Software Engineer · **Reports to:** Sanjana R. · **GitHub:** [@K-sau07](https://github.com/K-sau07)
**Project for the renewal period:** Iacon Optimus Program (approved to move from 2026-11-01)

---

## Executive summary

Six videos produced in the reporting period — three STEM explainers and three weekly
progress reports — each delivered as a 4K landscape master and a 4K vertical master.
Twelve masters in total.

Every reel is reproducible from this repository: the beat sheet, the sources behind every
on-screen number, a claim-level fact check, and the output of every quality gate are
committed beside each video. No renders are committed, per the collection's
GitHub-for-source / Drive-for-renders rule.

Two things in this period went beyond producing to schedule. **Week two corrects week
one** — week one reported a silently skipping typography gate and blamed a missing
library; re-checking showed the library was already installed and the real blocker was the
interpreter version. **Week three is the first reel in this folder built with
hand-authored Manim figures**, 13 drawn beats out of 20, because the subject is a
mechanism and a bullet list cannot show one.

Alongside production: reviewing Brutalist videos and handling upload to the YouTube
channel for the professor's final approval.

**This completes the Brutalist trial month.** I have been approved to move to the Iacon
Optimus Program, so this request is to renew onto that project from 2026-11-01. The work
documented below is the Brutalist trial it rests on.

---

## Completed results

### 1. Six videos, ten 4K masters, all gates passed

| Week | Video | Runtime | Beats | Evidence |
|---|---|---|---:|---|
| 5–12 Oct | MCP, Explained | 2:41 | 11 | [folder](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-1/explainer-mcp-explained/README.md) |
| 5–12 Oct | Brutalist, Week One | 1:52 | 9 | [folder](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-1/progress-week-1/README.md) |
| 13–19 Oct | Agents, On Their Own | 2:14 | 10 | [folder](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-2/explainer-agents-on-their-own/README.md) |
| 13–19 Oct | Brutalist, Week Two | 2:00 | 9 | [folder](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-2/progress-week-2/README.md) |
| 20–26 Oct | Calling Voice AI | 1:59 | 10 | [folder](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-3/explainer-calling-voice-ai/README.md) |
| 20–26 Oct | Repo Sensei, Week Three | 2:27 | 20 | [folder](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-3/progress-week-3/README.md) |

**Contribution:** sole author of all six — research, beat sheet, narration script, figure
design, and clearing every gate the toolkit runs before a master is cut.

Each folder carries [BUILD-LOG](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-3/progress-week-3/BUILD-LOG.md),
[SOURCES](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-3/progress-week-3/SOURCES.md),
[FACTCHECK](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-3/progress-week-3/FACTCHECK.md) and
[CHECKS-REPORT](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-3/progress-week-3/CHECKS-REPORT.md).

### 2. First Manim-authored reel in this folder

[`week-3/progress-week-3/scenes.py`](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-3/progress-week-3/scenes.py) — 13 Manim
Scene classes: a four-stage pipeline, a syntax tree growing beside its source, a trace
running down through UI / API / database, an answer snapping to a file and line, four
measured numbers counting up, and a status bar showing what does not work yet.

The earlier reels were Remotion-only, which caps every beat at a typographic card. The
reasoning for the change and the full figure list is in
[VISUAL-PLAN.md](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-3/progress-week-3/VISUAL-PLAN.md); the gate results are in
[layout_audit.md](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-3/progress-week-3/layout_audit.md).

**Contribution:** wrote the scene code and cleared GATE A (static), GATE B (layout),
GATE V (frame QC) and GATE T (typography and WCAG contrast) on all 13 scenes.

### 3. A correction published rather than quietly dropped

Week one concluded a quality gate was skipping because scipy was missing. Week two
re-checked and found scipy already installed; the gate still failed because the
interpreter on PATH was Python 3.9.6 and the checker annotates `float | None`, which needs
3.10+. Both commands are recorded in
[week-2/progress-week-2/SOURCES.md](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/week-2/progress-week-2/SOURCES.md), and the
correction is the subject of the week-two video.

---

## Hours status

`[TODO — fellow to complete before sending]`

**No weekly hours records exist yet.** The renewal instructions require actual hours for
each week, dated work records, and any week below 20 hours identified. The
[weekly-hours/](https://github.com/nikbearbrown/humanitarians-youtube/blob/saurabh-k/2026-10-26/fellows/saurabh-k/weekly-hours/README.md) folder currently holds only a format template.

This must be filled in from the fellow's own records before this request is sent. A
monthly average is explicitly not acceptable.

---

## Videos and Frictional logs

**Video masters** — all twelve are rendered and uploaded:
<https://drive.google.com/drive/folders/1LEVPhkELBUQBtHTcdykCaaczGpYg38-q>

`[TODO]` Direct YouTube links per video, once uploaded and pre-approved by the PM. Each
video's README carries a viewing-link slot currently marked NOT PROVIDED.

**Frictional logs** — `[TODO — not yet written]`

All six work folders carry a `FRICTIONAL.md`, and **all six are currently empty of dated
entries.** A weekly Frictional log is an explicit renewal requirement. These must be
written by the fellow from contemporaneous notes; they are deliberately not reconstructed
after the fact.

---

## Degree relevance and supervision

`[TODO — fellow to complete]` — how this work relates to the MS in Computer Software
Engineering, plus supervisor name and any available review or feedback evidence.

Supervisor / PM for this period: Sanjana R.

---

## Authorization

`[TODO — fellow to complete]` — authorization type and dates, EAD start and end, current
agreement dates.

**Send authorization documents privately to HR. Do not place them in this repository or
any public log.**

---

## Next period — 2026-11-01 through 2027-01-31 (Iacon Optimus Program)

Moving to the Iacon Optimus Program from 2026-11-01. Specific deliverables and target
dates to be agreed with the PM and recorded here before the period starts.

| Deliverable | Target |
|---|---|
| Optimus onboarding, tool installation and access | `[TODO]` |
| First Optimus work item, scoped with the PM | `[TODO]` |
| Weekly Frictional log entries kept contemporaneously | weekly |
| Weekly hours recorded in `weekly-hours/` as the week happens | weekly |

Carried over from Brutalist, if wanted rather than assumed:

| Carry-over | Status |
|---|---|
| repo-sensei answering and fixing paths, so a cited fix can be shown end to end | personal project, continuing |

## Outstanding issues

1. **Weekly hours are not documented** for any week in this period. This is the largest
   gap against the stated requirements.
2. **Frictional logs are empty** in all six work folders — an explicit renewal requirement.
3. **YouTube links to be added.** All twelve masters are uploaded; the per-video links and
   PM pre-approval go into this report before submission.
4. **Reporting weeks** are 5–12, 13–19 and 20–26 October. Render timestamps in the
   repository fall at the end of each period rather than across it.
6. **SPEC-ASSERTED rows** in each FACTCHECK are awaiting sign-off against primary
   documentation.
