# /hai Weekly Report — Week 4

| | |
|---|---|
| **Volunteer** | Kavya Mehta · AI Data Engineer · OPT, 20 hrs/week |
| **Profile** | [humanitarians.ai/kavya-mehta](https://www.humanitarians.ai/kavya-mehta) |
| **Project** | Brutalist (Humanitarians AI) · Manager: Jash |
| **Reporting week** | 2026-10-05 to 2026-10-11 |
| **Status** | Prepared with Addams from project evidence · confirmed by the volunteer on 2026-10-29 |

## Executive summary

Two videos were produced for this week: *Agents Touching Data They Shouldn't* (2:18, 9 beats) and
*CabStream, Week 1 Progress* (2:11, 8 beats). The explainer's demo runs the same support-agent query under
a wide credential and a scoped one. The progress video starts the CabStream series (my own project). This
is the week closest to my ceiling, Tier 3 data ethics decisions. Final renders were produced 2026-10-27 to
2026-10-29.

## Work completed

| Artifact | Link | Status |
|---|---|---|
| Topic explainer | [STEM WEEK 4](https://drive.google.com/drive/folders/1hDSiSeWRaqv_ol6LgUqW6tv3uKdKWkmm) | Final |
| Progress video | [PROGRESS WEEK 4](https://drive.google.com/drive/folders/1S9b0mVlIn0RU4ZvXKznwvkYtRiRNQXtI) | Final |

**What the demo showed:** ticket 4471 from customer 812, with a search that matches two people named
Rivera. All names and card digits are fake.
- **Wide grant:** both cards appear in the answer, and the audit flags customer 903 as outside the ticket.
- **Scoped grant:** the full-table query is denied, and the answer has one row, one card, customer 812 only.

**Progress video:** Kafka producer, then Delta bronze, then deduplicated silver with a weather join, then
a dbt gold layer, in six days according to the git log. The 1.57B-row scale numbers came later and were
deliberately not backdated.

## Tier justification

| Activity | Tier | Argument |
|---|---|---|
| Producing both videos with Claude Code | **Tier 1** | AI-drafted production is AI fluency. |
| Deduplicating in silver, not bronze | **Tier 5** | Bronze stays an untouched copy of what Kafka delivered, so any later bug can be replayed from raw data. Deduplicating there would destroy the evidence needed to debug it. Moving dedup to silver keeps that "what would have happened" option open. |
| Data-access framing | **Tier 3** | Raw trip rows carry exact pickup and drop-off points and times. Together, those can identify a rider's home or workplace. Analysts and agents need aggregates, not raw rows, and that line has to be drawn even though no rule in the project forces it. |
| Not backdating the scale numbers | **Tier 3 · Tier 4** | Claiming the 1.57B rows for week 1 would have made the progress look bigger than it was. Keeping them in the phase where they happened is honest reporting under no external check. |

## Struggle and friction

**Topic video:**
- The boundary card's items wrapped past the card edge; a visual look caught it, the checker didn't.
- In portrait, the spark line, window titles and a label all overflowed. Each was shortened.
- The portrait final was blocked on contrast: terracotta text was 2.74:1 against a 4.5:1 minimum. It was
  switched to the darker brand terracotta.

**Progress video:**
- The original version lacked the required intro line and AI disclosure. Both were added and the opening
  re-rendered.

## Hours (confirmed)

| Research | Exploration | Building | Review/QC | Documentation | Meetings | Total |
|---|---|---|---|---|---|---|
| 6 | 4 | 4 | 2 | 3 | 1 | 20 |

## Tools

- **Claude Code:** used.
- **Gru:** not used yet. CabStream is the strongest SDD candidate.
- **CRITIQ:** not used yet.

## Reflection

1. **What's CabStream's equivalent of "the ticket"?** The question being asked, for example "trips in one
   borough for one month". An agent answering it should get only the gold views for that scope, the way
   the demo's agent got only the ticket's customer.
2. **Is CabStream's Databricks access narrower than it needs to be?** It hasn't been checked yet. The
   first check is who holds read grants on the bronze tables, since those hold the raw location data.

## Next steps

- **Week 5 (Oct 12–18), topic explainer:** ontologies for observability at scale. One canonical entity for
  a service named three ways.
- **Week 5, progress video:** CabStream week 2, the move toward Azure (Event Hubs, Databricks, Storage, Key
  Vault) in Terraform.
- **Week 5:** check who holds read access to CabStream's raw bronze trip data, as the first data-access
  question.
