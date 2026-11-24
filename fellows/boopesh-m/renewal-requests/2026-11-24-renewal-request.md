# Renewal request — Boopesh M.

**Request date:** 2026-11-24. Prepared with Claude (Claude Code) from the build records and Boopesh's own
account of his hours and review work. This request is sent six days before the agreement ends, one day
later than the seven-day guideline.

## 1. The request

- **Name:** Boopesh M. ([@BoopeshMohanraj](https://github.com/BoopeshMohanraj))
- **Role / project:** Humanitarians AI Fellow, Brutalist team: weekly STEM/AI explainer and progress
  videos made with the Brutalist toolkit ([brutalist.art](https://github.com/nikbearbrown/brutalist.art)),
  plus video and code review for the Raman Effect and AI+1 projects
- **Current agreement:** 2026-10-13 to **2026-11-30**
- **Reporting period:** 2026-10-13 to 2026-11-30
- **Requested renewal dates:** 2026-12-01 to 2027-01-31
- **Project Manager:** Sanjana R.
- **Programme lead:** Professor Nik Bear Brown
- **Fellows folder:** [fellows/boopesh-m](../README.md)

### Open the evidence

| What | Link |
|---|---|
| Every work folder (10 videos, 5 weeks) | [Folder Guide](../README.md#folder-guide-and-evidence) |
| Weekly hours, one row per week | [weekly-hours/README.md](../weekly-hours/README.md) |
| Review records (Raman Effect, AI+1) | [Video Review Logs](https://docs.google.com/spreadsheets/d/1ovAQ1N19bqlFgjhSuC8Aw4wnvSKzbTsFxt5qtOYzaY4/edit?gid=1576859820#gid=1576859820) |
| Rendered videos | [Google Drive folder](https://drive.google.com/drive/folders/1NSKnM6dnnNGqD1_srGPBfVaaS-EXPWXi?usp=sharing) |
| Submission pull request | [nikbearbrown/humanitarians-youtube#446](https://github.com/nikbearbrown/humanitarians-youtube/pull/446) |

## 2. Completed results

**Result A — Ten Brutalist videos over five weeks, two every week, in native 4K.** For each week from
Oct 18 to Nov 21 there is one STEM / AI explainer and one progress update, each as a 16:9 3840×2160 film
and a separate native 9:16 2160×3840 Short. Every film is under 3 minutes, normalised to −14 LUFS, and
passed the toolkit's gates (layout audit, contrast and type-size check, final frame check) before delivery.
*Artifacts:* [Folder Guide](../README.md#folder-guide-and-evidence) ·
[Google Drive folder](https://drive.google.com/drive/folders/1NSKnM6dnnNGqD1_srGPBfVaaS-EXPWXi?usp=sharing).

**Result B — An AI-in-finance series where every number on screen comes from code that was actually run.**
Each STEM film is backed by a seed-locked experiment kept in its folder's `code/`, run twice to show
it is deterministic:
- [Deep Hedging](../2026-10-24-deep-hedging/README.md): a numpy replication of hedging with trading costs.
- [The 99.9% Accuracy Trap](../2026-11-01-fraud-accuracy-trap/README.md): fraud detection at the real
  0.172% fraud rate.
- [The Backtest Mirage](../2026-11-08-backtest-mirage/README.md): 10,000 strategies on pure noise.
- [Why Did the AI Say No?](../2026-11-15-why-did-the-ai-say-no/README.md): credit reason codes with
  exact Shapley values.
- [How an AI Sells a Big Order](../2026-11-22-ai-sells-a-big-order/README.md): Q-learning trade execution
  compared with Almgren–Chriss.

Facts that could not be verified are marked ⚠️ in each FACTCHECK.md rather than stated as fact.

**Result C — Video and code review for the Raman Effect and AI+1 projects.** Review started in week 1:
29 videos in Oct 13–17 (10 Raman Effect, 19 AI+1). After that it took about half of each week: writing
prompts and clear instructions, checking each video and the code behind it, and sending back what needed
to change.
*Artifact:* [Video Review Logs](https://docs.google.com/spreadsheets/d/1ovAQ1N19bqlFgjhSuC8Aw4wnvSKzbTsFxt5qtOYzaY4/edit?gid=1576859820#gid=1576859820) (Google Sheet, open to everyone in the organisation): every review
logged by hand at the end of each week, the first entry on 2026-10-17.

**Result D — Weekly measurements of the fellows programme itself.** The progress videos are built from
scripts that read the fellows repository's git history: merged pull requests, new work folders, frictional
logs, and which paperwork pieces each folder carries. Each script corrects for daylight saving and counts
squash merges, and recounts the previous week so late merges are disclosed rather than hidden.
*Artifact:* [week_stats.py](../2026-11-22-what-a-finished-folder-looks-like/code/week_stats.py) →
[results.json](../2026-11-22-what-a-finished-folder-looks-like/code/results.json).

**Personal contribution, stated plainly.**
- **Boopesh's own work:** he wrote the prompts and clear instructions behind each week's videos, including
  each week's direction (for example, moving the STEM series to AI in finance). He approved the AI narrator
  voice, reviewed the delivered videos and their code, and uploaded the videos to Drive.
- **Claude's part:** Claude (Claude Code) did the research, code, scene building, narration script and
  rendering, working from his instructions.
- **Reviews:** the Raman Effect and AI+1 reviews are Boopesh's own.

## 3. Hours

**120 hours from Oct 13 to Nov 21: 20 hours in each of six weeks.**
- Week 1 (Oct 13–17) was all review and onboarding: 29 videos reviewed.
- From Oct 18, each week split about evenly between review (10 h) and making his own two videos (10 h).

See [weekly-hours/README.md](../weekly-hours/README.md). **No week below 20 hours.**

**Gaps, stated honestly:**
- **Hours were entered here on 2026-11-24,** when this folder was first committed. The review work itself
  was logged in the [Video Review Logs](https://docs.google.com/spreadsheets/d/1ovAQ1N19bqlFgjhSuC8Aw4wnvSKzbTsFxt5qtOYzaY4/edit?gid=1576859820#gid=1576859820) at the end of each week. From the week of Nov 22 the hours are also
  logged here in the week they happen.
- **Week 1 (Oct 13–17):** no videos were due yet; the week was review and onboarding.
- **Nov 22–30:** the current week and the last two days of the agreement, logged as they happen.
- **GitHub evidence arrived late.** All ten folders were delivered in their weeks but could not be committed
  then: the fork attempt failed, and push access only arrived on 2026-11-24.
- **Project-repository code:** my work is video production and review, not development of the Brutalist
  toolkit, so there is no separate project-repository code. The code behind each video lives with that
  video, in its folder here.

## 4. Videos, decks and Frictional logs

| Week | STEM / AI video | Progress video |
|---|---|---|
| Oct 18–24 | [Deep Hedging](../2026-10-24-deep-hedging/README.md) · [log](../2026-10-24-deep-hedging/FRICTIONAL.md) | [Brutalist, Shared](../2026-10-24-brutalist-first-fellow-prs/README.md) · [log](../2026-10-24-brutalist-first-fellow-prs/FRICTIONAL.md) |
| Oct 25–31 | [The 99.9% Accuracy Trap](../2026-11-01-fraud-accuracy-trap/README.md) · [log](../2026-11-01-fraud-accuracy-trap/FRICTIONAL.md) | [One Week of Fellows](../2026-11-01-one-week-of-fellows/README.md) · [log](../2026-11-01-one-week-of-fellows/FRICTIONAL.md) |
| Nov 1–7 | [The Backtest Mirage](../2026-11-08-backtest-mirage/README.md) · [log](../2026-11-08-backtest-mirage/FRICTIONAL.md) | [What the Fellows Taught](../2026-11-08-what-the-fellows-taught/README.md) · [log](../2026-11-08-what-the-fellows-taught/FRICTIONAL.md) |
| Nov 8–14 | [Why Did the AI Say No?](../2026-11-15-why-did-the-ai-say-no/README.md) · [log](../2026-11-15-why-did-the-ai-say-no/FRICTIONAL.md) | [What Got in the Way](../2026-11-15-what-got-in-the-way/README.md) · [log](../2026-11-15-what-got-in-the-way/FRICTIONAL.md) |
| Nov 15–21 | [How an AI Sells a Big Order](../2026-11-22-ai-sells-a-big-order/README.md) · [log](../2026-11-22-ai-sells-a-big-order/FRICTIONAL.md) | [What a Finished Folder Looks Like](../2026-11-22-what-a-finished-folder-looks-like/README.md) · [log](../2026-11-22-what-a-finished-folder-looks-like/FRICTIONAL.md) |

All renders (16:9 and 9:16 for each film) are in the
[Google Drive folder](https://drive.google.com/drive/folders/1NSKnM6dnnNGqD1_srGPBfVaaS-EXPWXi?usp=sharing).
**Presentation decks:** required from 2026-12-01; each week's `slides.html` will go in its own dated folder.

## 5. Next steps

1. **Keep the weekly pair going, ongoing.** One STEM / AI-in-finance explainer and one progress update each
   week, both 16:9 + 9:16 4K, each with code, FACTCHECK, PROOF and a dated FRICTIONAL entry, committed in
   the week they are made.
2. **Keep reviewing for Raman Effect and AI+1, ongoing,** with each week's review records linked from
   `weekly-hours/`.
3. **Weekly presentation decks, from 2026-12-01.** A `slides.html` in a dated folder each week.
4. **Hours recorded weekly, from the week of Nov 22.** Written in the week, never reconstructed later.
5. **Project repository, if the work moves there.** If the next period includes changes to the Brutalist
   toolkit itself, commit them to [brutalist.art](https://github.com/nikbearbrown/brutalist.art) as the work
   happens, and link the commits from the Frictional logs.

**Unresolved issues:**
- the weekly hours were entered here at renewal time, not week by week (now fixed going forward);
- the GitHub folders were committed late because of the failed fork.

## 6. Email to send

Send to **hr@humanitarians.ai** and **bear@humanitarians.ai**, CC **Sanjana R.** (Project Manager),
Monday to Wednesday during business hours, at least 7 days before the agreement ends.

> **Subject:** Fellowship renewal — Boopesh M. — Brutalist team — December 1, 2026 to January 31, 2027
>
> Dear HR team and Professor Bear,
>
> I would like to request a renewal of my fellowship from December 1, 2026 to January 31, 2027. My current
> agreement ends on November 30, 2026. I am sorry this request comes one day later than the seven-day guideline.
>
> My renewal report is here:
> https://github.com/nikbearbrown/humanitarians-youtube/blob/boopesh-m/fellows/boopesh-m/renewal-requests/2026-11-24-renewal-request.md
>
> In short: over five weeks I delivered ten Brutalist videos in 4K, an AI-in-finance explainer and a
> progress update each week, each backed by code that was actually run. I also reviewed videos and code
> for the Raman Effect and AI+1 projects every week, starting with 29 videos in my first week. The report links every video,
> Frictional log and weekly hours record, states the gaps I still need to close, and sets out my plan for
> the next period.
>
> Thank you for considering my request.
>
> Best regards,
> Boopesh M.
