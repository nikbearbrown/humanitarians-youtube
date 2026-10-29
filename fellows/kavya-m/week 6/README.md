# Week 6

**Group:** Brutalist team · **Reporting week:** 2026-10-19 through 2026-10-25

Two videos were produced this week, each in its own folder with its own beat sheet and full evidence trail.

| Folder | Video | Runtime | Beats |
|---|---|---|---:|
| [kavya-ai-junk-data-gate/](kavya-ai-junk-data-gate/README.md) | Half the Data Is Fake: Catching AI Junk Before It Hits Your Pipeline | 2:26 | 9 |
| [kavya-cabstream-week3-progress/](kavya-cabstream-week3-progress/README.md) | CabStream, Week 3 Progress | 2:23 | 8 |

The explainer loads a half-junk batch of rider feedback with and without a validation gate. Provenance,
range and near-duplicate checks quarantine 9 junk rows, and the average rating moves from 4.30 to 3.55
against a true 3.40. One junk row still slips through, traced to the order of the checks. The progress
reel covers the night CabStream's pipeline actually ran on Databricks: a cluster and Key Vault scope, two
infrastructure fixes (including `prevent_destroy` so stored data survives `terraform destroy`), and Bronze
and Silver ingestion. It is explicit that the 1.57B-row total comes from the commit message, not a re-run
count.

Both are Remotion-only builds against brutalist.art at `b21f625`, voice Kokoro `am_onyx`, with the
AI-voice disclosure spoken in B00. Renders are not committed; see each folder's README for its export
details and Drive link.
