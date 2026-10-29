# /addams Renewal Report — Kavya Mehta

| | |
|---|---|
| **Volunteer** | Kavya Mehta · AI Data Engineer · OPT, 20 hrs/week |
| **Profile** | [humanitarians.ai/kavya-mehta](https://www.humanitarians.ai/kavya-mehta) |
| **GitHub** | [@Kavya-Mehta](https://github.com/Kavya-Mehta) |
| **Project** | Brutalist (Humanitarians AI) · Manager: Jash |
| **Own project** | CabStream, a Kafka → Delta/Databricks → dbt streaming lakehouse |
| **Period covered** | 2026-09-15 to 2026-10-25 (weeks 1–6) |
| **Weekly `/hai` reports** | 6 of 6 complete |
| **Status** | Prepared with Addams · confirmed by the volunteer on 2026-10-29 |

## Executive summary

Over six weeks I produced twelve videos for the Brutalist project: one STEM/AI topic explainer and one
project-progress video each week, every one in 16:9 and 9:16. All twelve open with the required
introduction, disclose the AI narration voice, and end with a concrete takeaway for the viewer. I drafted
the scripts with help from Claude Code.

The topic explainers argue data-agent and data-engineering ideas, mostly backed by small runnable demos
whose real output appears on screen. The progress videos track two projects from their git history: the
Brutalist toolkit (weeks 1–3) and my own CabStream pipeline (weeks 4–6), reporting what was verified and
what wasn't.

Total time: **120 hours** (20 hours × 6 weeks). The work moved from AI-assisted production (Tier 1) toward
judgment (Tier 4), causal reasoning about system design (Tier 5), and, from week 4, data-ethics decisions
(Tier 3), which is the ceiling I chose to develop.

## Weekly record

| Week | Dates | Topic explainer | Progress video | Weekly report |
|---|---|---|---|---|
| 1 | Sep 15 – Sep 20 | [Data Agents Win With a Better Harness](https://drive.google.com/drive/folders/1OI3qO309jkxj4VfsZ0feN8peJT9n2bE-) | [Brutalist, Week 1](https://drive.google.com/drive/folders/1ZHctUKYeYNlVtkcedsqI_JURNZP_QRx0) | [hai-week-1](hai/hai-week-1.md) |
| 2 | Sep 21 – Sep 27 | [Semantic Layers Become AI Context](https://drive.google.com/drive/folders/1NcG7mhE_Zko30T6LZvBnqhe0u3_rK_t7) | [Brutalist, Week 2](https://drive.google.com/drive/folders/1DnosnDUwHLtq_QgmJgiy-xFhjhDnSjA2) | [hai-week-2](hai/hai-week-2.md) |
| 3 | Sep 28 – Oct 4 | [OpenTelemetry for AI Agents](https://drive.google.com/drive/folders/1URxX7fBeKwA7w-bvDgDmuZRIkrYV7XHj) | [Brutalist, Week 3](https://drive.google.com/drive/folders/1v_YUlgK4GPa-gI-TiQaGBHm9QotpTOH0) | [hai-week-3](hai/hai-week-3.md) |
| 4 | Oct 5 – Oct 11 | [Agents Touching Data They Shouldn't](https://drive.google.com/drive/folders/1hDSiSeWRaqv_ol6LgUqW6tv3uKdKWkmm) | [CabStream, Week 1](https://drive.google.com/drive/folders/1S9b0mVlIn0RU4ZvXKznwvkYtRiRNQXtI) | [hai-week-4](hai/hai-week-4.md) |
| 5 | Oct 12 – Oct 18 | [Ontologies for Observability at Scale](https://drive.google.com/drive/folders/1vIj05MOkZ5nJrQbfFylxjREQ09_WZ2Qy) | [CabStream, Week 2](https://drive.google.com/drive/folders/1dih10GuIGENxQWj4suEFB0z_ro5le0Oe) | [hai-week-5](hai/hai-week-5.md) |
| 6 | Oct 19 – Oct 25 | [Half the Data Is Fake](https://drive.google.com/drive/folders/19Y1_PpiDstUkySnQ4UQaIBI9EBJNWJEg) | [CabStream, Week 3](https://drive.google.com/drive/folders/1m1U4j_JEu6FWTMhRIYnP5hk5NPQaFvaD) | [hai-week-6](hai/hai-week-6.md) |

## Hours (confirmed)

| Category | Per week | Six weeks |
|---|---|---|
| Research | 6 | 36 |
| Exploration (learning) | 4 | 24 |
| Building (beat sheets, demos, rendering) | 4 | 24 |
| Review and QC | 2 | 12 |
| Documentation | 3 | 18 |
| Meetings | 1 | 6 |
| **Total** | **20** | **120** |

Claude Code session time is included under building and documentation.

## Learning trajectory by tier

| Week | Tier 1 | Tier 3 | Tier 4 | Tier 5 | Strongest evidence |
|---|---|---|---|---|---|
| 1 | ✓ | | ✓ | | Framing "harness vs. model size" as a controlled comparison that holds the model fixed |
| 2 | ✓ | | ✓ | ✓ | Defining "revenue" so each part of the definition explains each number; doubting a false fix |
| 3 | ✓ | ✓ | ✓ | | Qualifying "zero new bugs"; disclosing the tracer was not the real SDK |
| 4 | ✓ | ✓ | ✓ | ✓ | Dedup in silver so bronze can be replayed; drawing the line on raw location data |
| 5 | ✓ | ✓ | ✓ | ✓ | Terraform over portal clicks; a deliberate Key Vault access policy |
| 6 | ✓ | ✓ | ✓ | ✓ | Tracing a gate's miss to rule order; `prevent_destroy` for data that outlives compute |

**Pattern:** Tier 1 (AI-assisted production) is present every week, as expected. Every week also carries
Tier 4 evidence. Tier 5 appears from week 2, and Tier 3 data-access judgments from week 3, growing from
week 4 onward in line with the ceiling I chose.

## Friction and what it taught

- **Week 1:** six toolkit bugs on Windows (encoding, `npx`, missing dependencies, ffmpeg paths). I learned
  the pipeline by breaking it.
- **Week 2:** a layout fix that looked right was wrong. Checking the real frame, not the thumbnail, found
  the actual cause.
- **Week 3:** "zero new bugs" was true, but it only covered paths that were already proven.
- **Week 4:** the honest version of CabStream's first week had to leave out scale numbers that came
  later.
- **Week 5:** Terraform defined resources that the git history can't prove were deployed.
- **Week 6:** my own validation gate let one junk row through. I kept the miss visible and traced it to
  rule order.

## Ceiling and exploration plan

- **Ceiling chosen:** Tier 3, data ethics decisions. "I know the technical controls for data access, but
  I'm not yet confident making the judgment call on what data an AI system *should* touch when the rules
  don't say."
- **Exploration (4 hrs/week):** one CabStream data-access question per week, written up as:
  - what the rules say
  - who could be affected
  - my decision and why
  - what I'm still unsure of

  Planned questions:
  - should a Text-to-SQL agent see raw trip rows?
  - who reads Key Vault secrets?
  - is joined taxi-and-weather data personal?
  - what should an audit log never record?
- **Bring one note a month to Jash** for review.

## Tools

| Tool | Use in weeks 1–6 | Plan |
|---|---|---|
| Claude Code | Every week: script drafting, demo code, rendering | Continue |
| Gru (SDD) | Not used yet | Start a CabStream SDD: storage vs. compute lifecycle, access policies, Terraform resources |
| CRITIQ | Not used yet | Review each topic explainer's argument before recording |

## Next term

1. Verify the CabStream totals: `COUNT(*)` on Bronze and Silver against the 1.57B / 252.3M stated in the
   commit.
2. Run the validation gate on real CabStream data and fix its rule-ordering gap.
3. Write the first Gru SDD sections and the weekly Tier 3 data-access notes.
4. Continue two videos a week, one topic explainer and one progress video, in 16:9 and 9:16.

---

*The hours and weekly reports above were confirmed by the volunteer on 2026-10-29. Each weekly report holds
the full evidence, tier arguments and reflections for its week.*
