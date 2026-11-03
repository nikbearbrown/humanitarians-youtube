# Renewal request — Mohan T.

- **Current agreement:** 10 Sep — 31 Oct 2026
- **Requested period:** 1 Nov 2026 — 30 Nov 2026

- **Projects:** National Loon Center educational games (first week); Project Ledger for humanitarians.ai (following six weeks)
- **Role:** Full Stack Developer
- **PM:** Nina Harris
- **Reporting folder:** [fellows/mohan-t](./README.md)
- **Drive (renders):** [all videos](https://drive.google.com/drive/folders/1IDkPJ5rz7ClIZRHDSdUFdfAW-KsQm0BB?usp=sharing)
- **GitHub:** [@MohanKrishna27062001](https://github.com/MohanKrishna27062001)

## What the current period produced

Two pieces of working software, one of them now live on the Humanitarians AI
website, and seven explainer videos documenting them.

**Seven weeks, 182 hours, between 22 and 30 a week** — the per-week basis is in
[HOURS.md](HOURS.md). The weekly figures are my own estimates, not
timesheet records.

- **National Loon Center games (first week).** Integrated the four Godot web games
  for the Loon Center's interactive museum experience — Nest Site, Deep Dive, Runway
  and Chick Taxi — into one Next.js page: a tile per game with its season,
  description and screenshot, an in-page play window, a "4 of 4 games live"
  progress bar, the cross-origin headers the WebAssembly exports need, and the
  required credit to Shesh Narayan Gupta's book on every tile. The games themselves
  were built by Shesh; my part was the integration.
- **Project Ledger, from demo to production (six weeks).** Built the ledger as a
  standalone app (project cards with phases, a needs-attention box, File my week,
  Meeting view, CSV export, Neon Postgres), added sign-in (hashed passwords, a
  signed session cookie, a second session check on every data route), kept a
  weekly history per volunteer, added email password reset with a one-time link
  that expires after 60 minutes, and built the History screen and per-person
  records.
- **Database changes for the live site, additions only.** Designed the
  columns and the `ledger_entries` / `ledger_updates` tables on top of the existing
  `fellows`, `projects` and `fellow_projects`, tested them in a separate schema, and
  handed them to Professor Nik, who ran them on production on 9 Oct.
- **Merged to the live website.** [Pull Request #14](https://github.com/nikbearbrown/humanitarians_html/pull/14)
  — *Add Project Ledger for PMs and admin, and fellow password reset* — moved the
  ledger into the main site at `/ledger` on the real tables, the site's fellow
  login, header and dark mode, with PM-and-admin-only access and a PM able to edit
  only their own project. 21 files, +2,969 / −5, from a fork and the
  `project-ledger` branch; reviewed and merged by Professor Nik on 23 Oct
  (merge commit [`f945421`](https://github.com/nikbearbrown/humanitarians_html/commit/f94542152440ad4fa587590201f0d947d670c5de)).
- **Timesheet redesign review.** Reviewed Professor Nik's design for fellow-submitted
  hours with evidence, and proposed four additions and a pre-rollout test plan
  (see the plan below).

### Evidence

Each video's two cuts are in the Drive folder, in `landscape/` and `vertical/`,
under the file name shown.

| Work | Video (Drive file) | Runtime | Source evidence |
|---|---|---:|---|
| Loon Center games integration | `LoonCenterGames_MohanT.mp4` | 2:26 | `hai-loon-center` (Next.js page, game exports, headers) |
| Ledger week 1 — first version | `ProjectLedgerWeek1_MohanT.mp4` | 2:28 | `hai-ledger-demo` |
| Ledger week 2 — sign-in and weekly history | `ProjectLedgerWeek2_MohanT.mp4` | 2:06 | `hai-ledger-demo` (`lib/auth.ts`, `lib/session.ts`, `middleware.ts`) |
| Ledger week 3 — database for the live site | `ProjectLedgerWeek3_MohanT.mp4` | 2:07 | `sql/real-site-migration.sql`; run on production 9 Oct |
| Ledger week 4 — reset, History, testing | `ProjectLedgerWeek4_MohanT.mp4` | 2:10 | `lib/reset.ts`, History screen, PM guide |
| Ledger week 5 — going live | `ProjectLedgerWeek5_MohanT.mp4` | 2:18 | [PR #14](https://github.com/nikbearbrown/humanitarians_html/pull/14), merged 23 Oct |
| Ledger week 6 — timesheet redesign and testing | `ProjectLedgerWeek6_MohanT.mp4` | 2:06 | Design review and test plan (not yet built) |

Every video has a fact-check that marks each on-screen claim as verified in code
or as coming from my own notes. Week 5's claims are now backed by PR #14 itself.

## Stated plainly

- **Nothing is published to YouTube yet.** All fourteen files (seven videos, two
  cuts each) are uploaded to Drive. PM review is pending.
- **The videos are 1080, not 4K.** The fellows guide asks for 3840×2160 and
  2160×3840. I chose 1080 to fit the render time on my machine; if the review
  needs 4K, the videos can be re-rendered from the same sources.
- **My GitHub reporting folder is still empty.** The beat sheets, fact-checks and
  scripts for the seven videos exist locally but have not been pushed, so the
  table above links to Drive and to the code rather than to work folders.
- **No Frictional logs yet.** I did not keep a `FRICTIONAL.md` during the work.
  Any log I add now for these weeks would be retrospective and labelled as such.

## Found while documenting the work

- `sql/schema.sql` in the ledger demo contains a second, conflicting
  `CREATE TABLE public.projects` block without `IF NOT EXISTS`; running the file as
  its README instructs stops there. The demo only — not the production migration.
- The Loon Center README still says only Deep Dive is live; the code has all four
  games live.

## Attribution, stated

- **Mine:** what to build and how it should work, the database design and the rule
  of additions only, acting on PM and professor feedback, the end-to-end testing,
  the deployment and PR #14, the weekly notes, and the narration drafts the videos
  follow.
- **Claude Code:** used to write code for both the Loon Center integration and the
  Project Ledger, under my direction. I reviewed and tested the changes before they
  went into the PR.
- **Claude:** built the seven videos from my notes and narration drafts using the
  brutalist.art toolkit, fact-checked each on-screen claim against my code, and
  flagged the `schema.sql` defect above. I chose the voice, the length and the
  format, and dropped or kept sections on review.

## Plan for the requested period

**Build and test the timesheet redesign.** Professor Nik's design moves hours from
the PM's keyboard to the fellow: each fellow enters the date, hours, work done and
evidence links (GitHub, YouTube), confirms it is accurate and submits it; the PM
reviews the evidence and approves or returns the hours; every approval and
correction is kept in history.

1. **Build the redesign** on top of the ledger now live at `/ledger`.
2. **Add the four improvements I proposed:** reminder emails before the Friday
   deadline, a review list where PMs check each entry with its evidence, a
   "My hours" summary for fellows, and an approved-hours report to support
   verification letters.
3. **Test before rollout:** a staging copy of the database, a test with many users
   at the same time, an access review, and unit tests for the main logic.

Alongside it:

- Push the source folders for these seven videos to `fellows/mohan-t/`, and keep a
  `FRICTIONAL.md` in each new work folder during the work, not after.
- Fix the `schema.sql` duplicate and the out-of-date Loon Center README.
- Weekly hours in [HOURS.md](HOURS.md), and a video for each week's work.

## Open items I am carrying

- **Videos not published;** PM review pending.
- **Videos at 1080, not 4K.**
- **GitHub reporting folder empty;** no Frictional logs for this period.
- **`schema.sql` duplicate `projects` table** in the ledger demo.
- **Loon Center README** out of date.
