# Project Ledger – Week 3: Extending the Database

On a live database, only add — never change or remove.

| | |
|---|---|
| **Runtime** | 2:06.86 (126.86 s) |
| **Format** | 24 fps · 16:9 (1920×1080) and 9:16 (1080×1920) |
| **Voice** | Kokoro `am_michael` — AI narration of my script, disclosed in the first beat |
| **Beats** | 9 · `ai-explainer` spine |
| **Brand** | `claude-hai` · `@HumanitariansAI` |
| **Presenter** | Mohan T. |
| **Status** | Built · frame QC and type gate passed · fact-checked · **not published** |
| **Renders** | [Google Drive](https://drive.google.com/drive/folders/1IDkPJ5rz7ClIZRHDSdUFdfAW-KsQm0BB?usp=sharing) — `landscape/ProjectLedgerWeek3_MohanT.mp4`, `vertical/ProjectLedgerWeek3_MohanT.mp4` |

## Evidence of the work

- `hai-ledger-demo/sql/real-site-migration.sql`
- [PR #14](https://github.com/nikbearbrown/humanitarians_html/pull/14) description: run on production 9 Oct

## Beats

| Beat | Act | Opens with | Measured |
|---|---|---|---:|
| B00 | INTRO | Hi, I am Mohan and this video is about week three of the Project Ledger: the database chan | 11.65 s |
| B01 | BLUF | In week three, I designed the database changes needed to run the ledger on the real Humani | 11.93 s |
| B02 | BODY | The website already had tables for fellows, projects, and fellow projects, which links fel | 10.79 s |
| B03 | BODY | On fellows, I added an optional GitHub username | 11.88 s |
| B04 | BODY | I added two new tables | 16.15 s |
| B05 | LIMITS | Because this was the real database, I tested the S Q L in a separate test schema first | 17.19 s |
| BVDT | VERDICT | To recap week three | 15.91 s |
| BHTF | YOUR_TURN | Your turn | 24.98 s |
| BOUT | OUTRO | Project Ledger, week three | 6.38 s |

## Fact-check

5 claims verified against code or GitHub; 2 from my own notes with no public record to
check. See [`FACTCHECK.md`](FACTCHECK.md).

## What is in this folder

```
README.md                  this file
FRICTIONAL.md              the process log for this work
beat_sheet.json            every beat: narration, shot, measured duration (16:9)
vertical/beat_sheet.json   the 9:16 cut
FACTCHECK.md               each on-screen claim and its evidence
SOURCES.md · SHOTLIST.md · PROMPTS.md · TYPECHECK.md
```

Videos and audio are not committed; the rendered masters are on Drive.
