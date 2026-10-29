# /hai Weekly Report — Week 3

| | |
|---|---|
| **Volunteer** | Kavya Mehta · AI Data Engineer · OPT, 20 hrs/week |
| **Profile** | [humanitarians.ai/kavya-mehta](https://www.humanitarians.ai/kavya-mehta) |
| **Project** | Brutalist (Humanitarians AI) · Manager: Jash |
| **Reporting week** | 2026-09-28 to 2026-10-04 |
| **Status** | Prepared with Addams from project evidence · confirmed by the volunteer on 2026-10-29 |

## Executive summary

Two videos were produced for this week: *OpenTelemetry for AI Agents* (2:18, 9 beats) and *Brutalist
Progress, Week 3* (1:59, 8 beats). The explainer shows the same failed agent run twice. As a plain log it
says "finished, one warning"; as a trace its spans point at the failing search step. The progress video
reports a week with zero new pipeline bugs. Final renders were produced 2026-10-27 to 2026-10-29.

## Work completed

| Artifact | Link | Status |
|---|---|---|
| Topic explainer | [STEM WEEK 3](https://drive.google.com/drive/folders/1URxX7fBeKwA7w-bvDgDmuZRIkrYV7XHj) | Final |
| Progress video | [PROGRESS WEEK 3](https://drive.google.com/drive/folders/1v_YUlgK4GPa-gI-TiQaGBHm9QotpTOH0) | Final |

**What the demo showed:**
- **The trace** has 5 spans. `search_docs` ran in **11 ms with 0 hits**, because the index name was
  misspelled (`q3-reprots`). The answer still cited "p.4" from zero sources.
- **The tracer is a stdlib recorder shaped like OpenTelemetry's span model, not the SDK.** The video says
  this out loud.

## Tier justification

| Activity | Tier | Argument |
|---|---|---|
| Producing both videos with Claude Code | **Tier 1** | AI-drafted production is AI fluency. |
| Qualifying "zero bugs" | **Tier 4** | The progress video doesn't claim the pipeline is stable. It says this week reused only proven components, so zero new bugs doesn't prove much. Knowing what a result can't show is calibration. |
| Disclosing "not the real SDK" | **Tier 3 · Tier 4** | Presenting a stdlib recorder as OpenTelemetry would misstate the evidence to viewers who might copy it. Saying so on screen was a judgment about honesty to the audience, not a technical requirement. |

## Struggle and friction

**Topic video:**
- The 13-line span tree clipped its last line on screen. The checker missed it; a visual look caught it.
- In portrait, the overview's corrected sentence ran past the safe edge, so the correction was shortened.

**Progress video:**
- The same false-positive size flag hit `ClaudeScienceLayerStack` for the third week running. It was
  logged as something that deserves a real fix rather than another explanation.

## Hours (confirmed)

| Research | Exploration | Building | Review/QC | Documentation | Meetings | Total |
|---|---|---|---|---|---|---|
| 6 | 4 | 4 | 2 | 3 | 1 | 20 |

## Tools

- **Claude Code:** used.
- **Gru:** not used yet.
- **CRITIQ:** not used yet.

## Reflection

1. **How stable is the pipeline after "zero new bugs"?** Moderately. The known paths held, but nothing new
   was exercised. The claim needs a week that uses a new component shape before it can be called stable.
2. **What would you trace first in CabStream?** The Kafka → Delta bronze ingestion job. The attribute to
   record is records consumed vs. records written. A mismatch catches silent drops, the same kind of quiet
   failure as the demo's "0 hits".

## Next steps

- **Week 4 (Oct 5–11), topic explainer:** agents touching data they shouldn't. Wide vs. scoped
  credentials.
- **Week 4, progress video:** start the CabStream series, my own project, from its git history.
- **Week 4:** test a component shape the pipeline hasn't used yet, so "zero new bugs" can be tested
  rather than assumed.
