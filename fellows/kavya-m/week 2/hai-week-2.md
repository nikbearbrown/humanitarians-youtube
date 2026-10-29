# /hai Weekly Report — Week 2

| | |
|---|---|
| **Volunteer** | Kavya Mehta · AI Data Engineer · OPT, 20 hrs/week |
| **Profile** | [humanitarians.ai/kavya-mehta](https://www.humanitarians.ai/kavya-mehta) |
| **Project** | Brutalist (Humanitarians AI) · Manager: Jash |
| **Reporting week** | 2026-09-21 to 2026-09-27 |
| **Status** | Prepared with Addams from project evidence · confirmed by the volunteer on 2026-10-29 |

## Executive summary

Two videos were produced for this week: *Semantic Layers Become AI Context* (2:26, 9 beats) and
*Brutalist Progress, Week 2* (1:56, 8 beats). The explainer's SQLite demo shows two agents disagreeing on
"October revenue" until the semantic layer's definition is in their context. The progress video tests
whether week 1's fixes held. Final renders were produced 2026-10-27 to 2026-10-29.

## Work completed

| Artifact | Link | Status |
|---|---|---|
| Topic explainer | [STEM WEEK 2](https://drive.google.com/drive/folders/1NcG7mhE_Zko30T6LZvBnqhe0u3_rK_t7) | Final |
| Progress video | [PROGRESS WEEK 2](https://drive.google.com/drive/folders/1DnosnDUwHLtq_QgmJgiy-xFhjhDnSjA2) | Final |

**What the demo showed:**
- **Raw schema as context:** agent A answered $8,500 (gross) and agent B $8,200 (minus refunds).
- **Semantic layer as context:** both asked for `net_revenue` and got **$7,300**, finance's number. The
  difference is the cancelled order, which the definition excludes.

## Tier justification

| Activity | Tier | Argument |
|---|---|---|
| Producing both videos with Claude Code | **Tier 1** | AI-drafted production is AI fluency. |
| Defining "revenue" for the demo | **Tier 5** | The demo works only because "revenue" is pinned down: gross minus refunds, with cancelled orders excluded. Each part of that definition changes the number, and the video shows exactly which part causes which difference ($8,500 → $8,200 → $7,300). |
| The progress video's layout bug | **Tier 4 · Tier 5** | The first fix (shortening the footer text) was a false lead. Doubting it and tracing the overlap to the layout math (`colBottom` and the footer's top position) is supervision followed by causal diagnosis. It was verified on a real extracted frame, not the QC thumbnail. |

## Struggle and friction

**Topic video:**
- The landscape final was blocked: small card text measured 38 px against a 41 px floor. The cards were
  removed.
- The portrait final was blocked twice by the type-size gate. The cause was found by probing the exact
  frame the gate measures, after two wrong guesses.

**Progress video:**
- None of week 1's six bugs came back.
- One new layout bug in `SkillTeardownPipeline916`. The first fix attempted was wrong.

## Hours (confirmed)

| Research | Exploration | Building | Review/QC | Documentation | Meetings | Total |
|---|---|---|---|---|---|---|
| 6 | 4 | 4 | 2 | 3 | 1 | 20 |

## Tools

- **Claude Code:** used.
- **Gru:** not used yet.
- **CRITIQ:** not used yet.

## Reflection

1. **Where could CabStream count "trips" two ways?** Bronze keeps every Kafka event, including duplicates
   and late arrivals. Silver deduplicates. A query on bronze and one on silver would disagree the way the
   two agents did. A single shared definition, such as "completed trips = deduplicated silver rows with a
   drop-off time", would settle it.
2. **What happened after the first fix failed?** The approach changed from editing the text to fixing the
   layout calculation. The result was checked on a frame extracted from the compiled video, because the
   contact-sheet thumbnail had hidden the problem.

## Next steps

- **Week 3 (Sep 28 – Oct 4), topic explainer:** OpenTelemetry for AI agents. Contrast a plain log with a
  trace for the same failed run.
- **Week 3, progress video:** a third week on the pipeline, to see whether this week's layout-math fix
  holds.
- **Week 3:** write down a CabStream "completed trips" definition, so trips are counted one way across
  layers.
