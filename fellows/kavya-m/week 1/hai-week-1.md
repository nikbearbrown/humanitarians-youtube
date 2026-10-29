# /hai Weekly Report — Week 1

| | |
|---|---|
| **Volunteer** | Kavya Mehta · AI Data Engineer · OPT, 20 hrs/week |
| **Profile** | [humanitarians.ai/kavya-mehta](https://www.humanitarians.ai/kavya-mehta) |
| **Project** | Brutalist (Humanitarians AI) · Manager: Jash |
| **Reporting week** | 2026-09-15 to 2026-09-20 |
| **Status** | Prepared with Addams from project evidence · confirmed by the volunteer on 2026-10-29 |

## Executive summary

Two videos were produced for this week: a topic explainer, *Data Agents Win With a Better Harness, Not a
Bigger Model* (2:24, 9 beats), and *Brutalist Progress, Week 1* (2:17, 9 beats). The explainer is backed
by a runnable SQLite demo. The progress video covers setting up the Brutalist toolkit and the six pipeline
bugs found along the way. Final renders were produced 2026-10-27 to 2026-10-29.

## Work completed

| Artifact | Link | Status |
|---|---|---|
| Topic explainer | [STEM WEEK 1](https://drive.google.com/drive/folders/1OI3qO309jkxj4VfsZ0feN8peJT9n2bE-) | Final |
| Progress video | [PROGRESS WEEK 1](https://drive.google.com/drive/folders/1ZHctUKYeYNlVtkcedsqI_JURNZP_QRx0) | Final |

**What the demo showed:** the same scripted SQL went through two harnesses.
- **Thin harness:** returned East 720 / West 800 and ran zero checks.
- **Real harness:** its invariant check failed on try 1 (1,520 ≠ 900, a fan-out join), the retry passed,
  and it returned the correct East 400 / West 500.

## Tier justification

| Activity | Tier | Argument |
|---|---|---|
| Producing both videos with Claude Code | **Tier 1** | Scripts, demo and scenes were drafted with Claude Code. This is AI fluency, the entry point. |
| Choosing the harness thesis and the "hold the model fixed" test | **Tier 4** | The volunteer chose the topic and framed it as a controlled comparison. Changing only the harness turns an opinion ("harness beats model size") into something a demo can show. That is formulating the problem, not just solving one. |
| Toolkit setup and the six bug fixes | **Tier 2 · Tier 4** | Getting the toolkit running on Windows meant diagnosing failures that only show up by running it: file encoding, `npx` resolution, a drive-letter path in ffmpeg. That knowledge comes from doing, not reading. |

## Struggle and friction

**Topic video:**
- The overview beat cut off mid-sentence; the text was shortened to fit the 9.6 s audio.
- The four-parts diagram was too small and revealed everything at once, so a new scene was built.
- The first final export was refused (15 MAJOR defects): the terminal was unreadable at 4K.
- The portrait version failed the type-size gate twice before passing.

**Progress video:** six bugs, all fixed at the root:
- Windows file encoding
- `npx` resolution
- missing Node dependencies
- an ffmpeg drive-letter path
- a visual-QC false positive
- a chart fed the wrong number

## Hours (confirmed)

| Research | Exploration | Building | Review/QC | Documentation | Meetings | Total |
|---|---|---|---|---|---|---|
| 6 | 4 | 4 | 2 | 3 | 1 | 20 |

## Tools

- **Claude Code:** used.
- **Gru (SDD):** not used yet.
- **CRITIQ:** not used yet.

## Reflection

1. **Would the "hold one variable fixed" test work on CabStream?** Yes. Hold the dbt gold models fixed and
   change only the silver dedup rule. If gold row counts move, the difference comes from dedup alone, not
   from the transformation logic.
2. **How wrong was the thin harness?** Its regional totals summed to 1,520 against a true 900, about 69%
   over. The real harness needed exactly one retry to correct it. The error came from the join, not the
   model.

## Next steps

- **Week 2 (Sep 21–27), topic explainer:** semantic layers as AI context. Show what an agent should read
  (the business definition) before it writes a query.
- **Week 2, progress video:** check whether week 1's six pipeline fixes hold when a second video is built
  on top of them.
- **Week 2:** start pinning down metric definitions, since the revenue demo needs one exact definition.
