# Week 4

**Group:** Brutalist team · **Reporting week:** 2026-10-05 through 2026-10-11

Two videos were produced this week, each in its own folder with its own beat sheet and full evidence trail.

| Folder | Video | Runtime | Beats |
|---|---|---|---:|
| [kavya-agent-data-overreach/](kavya-agent-data-overreach/README.md) | Agents Touching Data They Shouldn't | 2:18 | 9 |
| [kavya-cabstream-week1-progress/](kavya-cabstream-week1-progress/README.md) | CabStream, Week 1 Progress | 2:11 | 8 |

The explainer shows that data overreach is usually a credential wider than the task. In a runnable
SQLite demo, the same support-agent query reads another customer's card under a wide grant. Under a
grant scoped to the ticket it is denied and sees one row. The progress reel starts the CabStream
series: a Kafka producer, Delta bronze, deduplicated silver with a weather join, and a dbt gold layer,
scaffolded in the first week. Every stage is traced to the git log, and later scale numbers are not
backdated.

Both are Remotion-only builds against brutalist.art at `b21f625`, voice Kokoro `am_onyx`, with the
AI-voice disclosure spoken in B00. Renders are not committed; see each folder's README for its export
details and Drive link.
