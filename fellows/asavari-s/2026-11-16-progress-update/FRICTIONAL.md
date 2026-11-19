# Frictional log — Progress Update, week of November 16

- **Evidence:** [`beat_sheet.json`](beat_sheet.json) · [58bc68a Frictional logs for all 10 folders](https://github.com/nikbearbrown/humanitarians-youtube/commit/58bc68a) · [corrected Trust, but Verify](../2026-10-31-trust-but-verify/)
- **Renders:** `progress-update-2026-11-16.mp4` (16:9, 1:57) and the 9:16 short (2:01). Not committed; viewing link to be added after upload.

## 2026-11-18 — catching up the record, first weekly progress video

**What I was working on.** I had filed no weekly reports since October 31. This week I put the record right first, then made the first of the weekly progress-update videos the program requires.

**What I tried, and what I expected.** I expected the Frictional logs to be paperwork: write them, link the commits, move on.

**Where it resisted, and what I did next.**
- **The logs found a problem in my own work.** Writing them surfaced four overstatements in my Trust, but Verify video. I had the narration corrected and the video re-rendered.
- **Renders were about to slip into git.** The repository's `.gitignore` had stopped ignoring `.mp4` files after the main branch changed its rules. My final masters were one `git add` away from being committed, so I added an ignore rule to my own folder.
- **The first render attempt produced nothing.** A loop in the render command didn't split its arguments in this shell, so every build failed immediately. It was re-run with explicit calls, and all three videos rendered with 0 failures.

**What Claude contributed, and what I did with it.**
- **Claude:**
  - drafted the ten Frictional logs, this video's beat sheet, and the renewal report draft
  - found the fourth overstatement (the video called the agent "verified" when the recipe is still SPECIFIED)
  - wrote and ran the renders
- **Me:**
  - decided to start weekly reporting now rather than at renewal time
  - approved the re-cut
  - supplied my new team and Project Manager (Agents & Jobs, Tanmay Sangam)

**What I understand now, and what I still do not.**
- **Understood:** a weekly record can't be honestly back-filled. Missing weeks have to be reported as missing.
- **Still open:**
  - my hours for the weeks after July 24 still need to go into `weekly-hours/` from my own records
  - viewing links for this week's two videos aren't posted yet
  - my first Agents & Jobs task isn't assigned yet

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._

## 2026-11-19 — choosing my first Agents & Jobs project

**What I was working on.** Picking a next project now that I'm on the Agents & Jobs team, and finishing Tanmay's three deliverables (due Nov 20).

**What I tried, and what I expected.** I asked Claude to survey [nikbearbrown/mycroft](https://github.com/nikbearbrown/mycroft) for work I could pick up. I expected to find open issues to choose from.

**Where it resisted, and what I did next.**
- The repo has **no open issues**; work moves through PMs and open pull requests instead. The survey found:
  - six projects on main
  - several agent-related folders
  - eight open PRs, including my [#13](https://github.com/nikbearbrown/mycroft/pull/13)
- Four options came out of it:
  1. Package my SEC agent as a deterministic tool that other Mycroft agents can call.
  2. Join the Agentic Runway-Risk Pipeline (most active, last commit Nov 16).
  3. Help with insider signals ([PR #86](https://github.com/nikbearbrown/mycroft/pull/86), SEC Form 4).
  4. Work on the provenance-gatekeeper / verification layer.
- I checked [humanitarians.ai/agents](https://www.humanitarians.ai/agents): Mycroft is one of the Agents projects, so option 1 is Agents & Jobs work.
- Uploading the last three videos: after I uploaded, the shared Drive folder still didn't show them, and Trust, but Verify was still the Nov 3 file. Being re-checked.

**What Claude contributed, and what I did with it.**
- **Claude:** ran the survey and recommended option 1.
- **Me:** chose option 1. I'll take it to Tanmay, who decides.

**What I understand now, and what I still do not.**
- **Understood:** the shortest path to my "first PR by Nov 30" deliverable is building on my own SEC agent rather than starting over.
- **Not resolved:** Tanmay's confirmation of the project.
